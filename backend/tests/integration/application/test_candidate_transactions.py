"""Real SQLite serialization, rollback, receipts and revision fencing."""

from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault


def draft(request_id: str | None = None) -> dict[str, object]:
    return {
        "request_id": request_id or str(uuid4()),
        "resume_name": "R",
        "contacts": {"full_name": None, "phone_number": None, "email": None},
        "header_presentation": {"optional_items": []},
        "sections": [],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#000000",
        },
    }


def outcome(call: Callable[[], object]) -> object:
    try:
        return call()
    except Failure as exc:
        return exc.code


def parallel[T, R](
    pool: ThreadPoolExecutor, function: Callable[[T], R], values: Iterable[T]
) -> list[R]:
    return list(pool.map(function, values))


def test_same_request_serializes_to_one_resume_and_one_receipt(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        command = draft()
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = parallel(
                pool, lambda _: authority.command("RESUME_CREATE", command), range(8)
            )
        assert all(result == results[0] for result in results)
        with store.engine.connect() as conn:
            assert conn.exec_driver_sql("SELECT count(*) FROM resumes").scalar_one() == 1
            assert (
                conn.exec_driver_sql("SELECT count(*) FROM candidate_command_receipts").scalar_one()
                == 1
            )


def test_first_create_default_selection_is_single_winner(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = parallel(
                pool,
                lambda _: authority.command("RESUME_CREATE", draft()),
                range(8),
            )
        selection = authority.list_resumes()["default_resume_selection"]
        assert selection["revision"] == 2
        assert (
            sum(
                result["resume"]["resume_id"] == selection["default_resume_id"]
                for result in results
            )
            == 1
        )
        assert all(result["default_resume_selection"] == selection for result in results)


@pytest.mark.parametrize(
    "stage,committed",
    [
        ("candidate_after_publication", False),
        ("candidate_after_receipt", False),
        ("before_commit", False),
        ("commit_before_driver", False),
        ("commit_after_driver", True),
    ],
)
def test_publication_and_receipt_commit_together(
    tmp_path: Path, stage: str, committed: bool
) -> None:
    with Store.open(tmp_path) as store:
        command = draft()

        def fault(point: str) -> None:
            if point == stage:
                raise OSError("controlled private failure")

        store.fault = fault
        expected = "OUTCOME_UNKNOWN" if stage.startswith("commit_") else "STORAGE_UNAVAILABLE"
        with pytest.raises(Failure, match=expected):
            CandidateAuthority(store).command("RESUME_CREATE", command)
        store.fault = no_fault
        with store.engine.connect() as conn:
            assert conn.exec_driver_sql("SELECT count(*) FROM resumes").scalar_one() == int(
                committed
            )
            assert conn.exec_driver_sql(
                "SELECT count(*) FROM candidate_command_receipts"
            ).scalar_one() == int(committed)
            assert conn.exec_driver_sql(
                "SELECT count(*) FROM candidate_evidence_projections"
            ).scalar_one() == int(committed)
            assert conn.exec_driver_sql("SELECT count(*) FROM portrait_builds").scalar_one() == 0
        result = CandidateAuthority(store).command("RESUME_CREATE", command)
        assert result["outcome"] == "CREATED"


def test_revision_race_has_one_winner(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        created = authority.command("RESUME_CREATE", draft())
        target = created["resume"]["resume_id"]
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = parallel(
                pool,
                lambda name: outcome(
                    lambda: authority.command(
                        "RESUME_RENAME",
                        {"request_id": str(uuid4()), "revision": 1, "resume_name": name},
                        target,
                    )
                ),
                ("A", "B"),
            )
        assert sum(isinstance(result, dict) for result in results) == 1
        assert "REVISION_CONFLICT" in results


def test_noop_at_revision_limit_and_changed_write_is_fenced(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        created = authority.command("RESUME_CREATE", draft())
        target = created["resume"]["resume_id"]
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE resumes SET revision=?", (MAX_REVISION,))
        unchanged = authority.command(
            "RESUME_RENAME",
            {"request_id": str(uuid4()), "revision": MAX_REVISION, "resume_name": "R"},
            target,
        )
        assert unchanged["outcome"] == "UNCHANGED"
        with pytest.raises(Failure, match="REVISION_EXHAUSTED"):
            authority.command(
                "RESUME_RENAME",
                {"request_id": str(uuid4()), "revision": MAX_REVISION, "resume_name": "Changed"},
                target,
            )
