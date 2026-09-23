"""Real SQLite races, independent revision tokens, capacity and publication time."""

from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import (
    CandidateRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
from sqlalchemy.engine import Connection

Json = dict[str, Any]


def evidence() -> Json:
    return {
        "request_id": str(uuid4()),
        "kind": "SKILL",
        "fields": {"skill_name": "S"},
        "content": [],
    }


def draft(service: CandidateAuthority) -> Json:
    return {
        "request_id": str(uuid4()),
        "resume_name": "R",
        "profile_version_id": service.pair("profile")["profile_version"]["profile_version_id"],
        "header_presentation": {"optional_items": []},
        "sections": [],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#000000",
        },
    }


def attempt(
    service: CandidateAuthority, name: str, data: Json, target: str | None = None
) -> Json | str:
    try:
        return service.command(name, data, target)
    except Failure as exc:
        return exc.code


def parallel[T, R](
    pool: ThreadPoolExecutor, function: Callable[[T], R], values: Iterable[T]
) -> list[R]:
    return list(pool.map(function, values))


def test_same_key_and_different_item_concurrency(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        command = evidence()
        with ThreadPoolExecutor(max_workers=6) as pool:
            results = list(
                parallel(pool, lambda _: service.command("EVIDENCE_CREATE", command), range(6))
            )
        assert all(r == results[0] for r in results)
        assert len(service.list_evidence()["evidence_items"]) == 1
        same_key = evidence()
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(
                parallel(
                    pool,
                    lambda name: attempt(
                        service, "EVIDENCE_CREATE", {**same_key, "fields": {"skill_name": name}}
                    ),
                    ["a", "b"],
                )
            )
        assert sum(isinstance(r, dict) for r in results) == 1
        assert "REQUEST_CONFLICT" in results
        items = service.list_evidence()["evidence_items"]

        def update(item: Json) -> Json:
            return service.command(
                "EVIDENCE_UPDATE",
                {
                    "request_id": str(uuid4()),
                    "revision": 1,
                    "fields": {"skill_name": "changed"},
                    "content": [],
                },
                item["evidence_item"]["evidence_item_id"],
            )

        with ThreadPoolExecutor(max_workers=2) as pool:
            updates = list(parallel(pool, update, items))
        members = service.baseline()["members"]
        assert {(m["evidence_item_id"], m["evidence_item_version_id"]) for m in members} == {
            (
                u["evidence_item"]["evidence_item_id"],
                u["evidence_item_version"]["evidence_item_version_id"],
            )
            for u in updates
        }
        target = updates[0]["evidence_item"]["evidence_item_id"]
        with ThreadPoolExecutor(max_workers=2) as pool:
            raced = list(
                parallel(
                    pool,
                    lambda _: attempt(
                        service,
                        "EVIDENCE_UPDATE",
                        {
                            "request_id": str(uuid4()),
                            "revision": 2,
                            "fields": {"skill_name": "race"},
                            "content": [],
                        },
                        target,
                    ),
                    range(2),
                )
            )
        assert sum(isinstance(r, dict) for r in raced) == 1
        assert "REVISION_CONFLICT" in raced


def test_first_resume_concurrency_and_default_tokens(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        command = draft(service)
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(
                parallel(
                    pool,
                    lambda _: service.command(
                        "RESUME_CREATE", {**command, "request_id": str(uuid4())}
                    ),
                    range(4),
                )
            )
        selection = service.list_resumes()["default_resume_selection"]
        assert selection["revision"] == 2
        assert all(r["default_resume_selection"] == selection for r in results)
        others = [
            r["resume"]["resume_id"]
            for r in results
            if r["resume"]["resume_id"] != selection["default_resume_id"]
        ]
        with ThreadPoolExecutor(max_workers=2) as pool:
            switches = list(
                parallel(
                    pool,
                    lambda rid: attempt(
                        service,
                        "DEFAULT_RESUME_SET",
                        {"request_id": str(uuid4()), "revision": 2, "default_resume_id": rid},
                    ),
                    others[:2],
                )
            )
        assert sum(isinstance(r, dict) for r in switches) == 1
        assert "REVISION_CONFLICT" in switches


def test_noop_max_revision_and_clock_rollback(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store, clock=lambda: "2030-01-01T00:00:00.000Z")
        entry = service.command("EVIDENCE_CREATE", evidence())
        eid = entry["evidence_item"]["evidence_item_id"]
        service.clock = lambda: "2020-01-01T00:00:00.000Z"
        updated = service.command(
            "EVIDENCE_UPDATE",
            {
                "request_id": str(uuid4()),
                "revision": 1,
                "fields": {"skill_name": "new"},
                "content": [],
            },
            eid,
        )
        assert updated["evidence_item"]["updated_at"] == entry["evidence_item"]["updated_at"]
        assert updated["evidence_item_version"]["created_at"] == service.baseline()["created_at"]
        prof = service.command(
            "PROFILE_SAVE",
            {
                "request_id": str(uuid4()),
                "revision": 1,
                "full_name": "X",
                "phone_number": None,
                "email": None,
            },
        )
        assert (
            prof["profile"]["updated_at"] < service.baseline()["created_at"]
        )  # No unrelated Baseline clamp.
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE evidence_items SET revision=?", (MAX_REVISION,))
        body: Json = {
            "request_id": str(uuid4()),
            "revision": MAX_REVISION,
            "fields": {"skill_name": "new"},
            "content": [],
        }
        assert service.command("EVIDENCE_UPDATE", body, eid)["outcome"] == "UNCHANGED"
        assert (
            attempt(
                service,
                "EVIDENCE_RETIRE",
                {"request_id": str(uuid4()), "revision": MAX_REVISION},
                eid,
            )
            == "REVISION_EXHAUSTED"
        )
        assert service.pair("evidence_item", eid)["evidence_item"]["status"] == "ACTIVE"
        assert (
            service.command("EVIDENCE_UPDATE", {**body, "request_id": str(uuid4())}, eid)[
                "evidence_baseline_snapshot_id"
            ]
            == updated["evidence_baseline_snapshot_id"]
        )


def test_selection_overflow_rolls_back_default_removal(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        a = service.command("RESUME_CREATE", draft(service))
        b = service.command("RESUME_CREATE", draft(service))
        aid, bid = a["resume"]["resume_id"], b["resume"]["resume_id"]
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE default_resume_selection SET revision=?", (MAX_REVISION,))
        command = {
            "request_id": str(uuid4()),
            "revision": 1,
            "default_resume_selection": {"revision": MAX_REVISION},
            "replacement_resume_id": bid,
        }
        assert attempt(service, "RESUME_REMOVE", command, aid) == "REVISION_EXHAUSTED"
        assert service.pair("resume", aid)["resume"] == a["resume"]
        assert (
            service.command(
                "DEFAULT_RESUME_SET",
                {"request_id": str(uuid4()), "revision": MAX_REVISION, "default_resume_id": aid},
            )["outcome"]
            == "UNCHANGED"
        )
        assert (
            attempt(
                service,
                "DEFAULT_RESUME_SET",
                {"request_id": str(uuid4()), "revision": MAX_REVISION, "default_resume_id": bid},
            )
            == "REVISION_EXHAUSTED"
        )
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT count(*) FROM candidate_command_receipts WHERE request_id=?",
                    (command["request_id"],),
                ).scalar_one()
                == 0
            )


@pytest.mark.parametrize("name,limit", [("evidence_item", 1000), ("resume", 100)])
def test_active_capacity_is_atomic(tmp_path: Path, name: str, limit: int) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        command_type = "EVIDENCE_CREATE" if name == "evidence_item" else "RESUME_CREATE"
        command = evidence() if name == "evidence_item" else draft(service)
        first = service.command(command_type, command)

        # Construct a valid near-capacity storage fixture in one transaction.
        def populate(conn: Connection) -> None:
            repo = CandidateRepository(conn)
            for _ in range(limit - 2):
                rid, vid = str(uuid4()), str(uuid4())
                root = {**first[name], name + "_id": rid, "current_" + name + "_version_id": vid}
                version = {**first[name + "_version"], name + "_id": rid, name + "_version_id": vid}
                repo.publish(name, root, version, first=True)
            if name == "evidence_item":
                repo.publish_baseline(str(uuid4()), first[name]["updated_at"])

        store.run(populate, write=True)
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(
                parallel(
                    pool,
                    lambda _: attempt(
                        service, command_type, {**command, "request_id": str(uuid4())}
                    ),
                    range(2),
                )
            )
        assert sum(isinstance(r, dict) for r in results) == 1
        assert "CAPACITY_EXCEEDED" in results
        assert store.run(lambda conn: CandidateRepository(conn).count(name)) == limit


@pytest.mark.parametrize("name", ["profile", "resume"])
def test_other_roots_noop_at_revision_limit(tmp_path: Path, name: str) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        if name == "profile":
            command_type, target = "PROFILE_SAVE", None
            command: Json = {
                "request_id": str(uuid4()),
                "revision": MAX_REVISION,
                "full_name": None,
                "phone_number": None,
                "email": None,
            }
            changed = {**command, "full_name": "Changed"}
        else:
            result = service.command("RESUME_CREATE", draft(service))
            command_type, target = "RESUME_RENAME", result["resume"]["resume_id"]
            command = {"request_id": str(uuid4()), "revision": MAX_REVISION, "resume_name": "R"}
            changed = {**command, "resume_name": "Changed"}
        with store.engine.begin() as conn:
            conn.exec_driver_sql(f"UPDATE {name}s SET revision=?", (MAX_REVISION,))
        original = service.pair(name, target)
        assert service.command(command_type, command, target)["outcome"] == "UNCHANGED"
        assert (
            attempt(service, command_type, {**changed, "request_id": str(uuid4())}, target)
            == "REVISION_EXHAUSTED"
        )
        assert service.pair(name, target) == original


def test_new_source_race_never_substitutes_latest(tmp_path: Path) -> None:
    from threading import Barrier

    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        fact = service.command("EVIDENCE_CREATE", evidence())
        eid, vid = (
            fact["evidence_item"]["evidence_item_id"],
            fact["evidence_item_version"]["evidence_item_version_id"],
        )
        command = draft(service)
        command["sections"] = [
            {
                "kind": "SKILL",
                "members": [
                    {"evidence_item_id": eid, "evidence_item_version_id": vid, "content": []}
                ],
            }
        ]
        barrier = Barrier(2)

        def race(which: int) -> Json | str:
            barrier.wait(timeout=5)
            if which:
                return service.command(
                    "EVIDENCE_UPDATE",
                    {
                        "request_id": str(uuid4()),
                        "revision": 1,
                        "fields": {"skill_name": "new"},
                        "content": [],
                    },
                    eid,
                )
            return attempt(service, "RESUME_CREATE", command)

        with ThreadPoolExecutor(max_workers=2) as pool:
            saved, updated = parallel(pool, race, [0, 1])
        assert isinstance(updated, dict)
        if isinstance(saved, dict):
            assert (
                saved["resume_version"]["sections"][0]["members"][0]["evidence_item_version_id"]
                == vid
            )
        else:
            assert saved == "SOURCE_CONFLICT"
            assert service.list_resumes()["resumes"] == []
