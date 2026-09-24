"""Stable logical IDs, exact historical reads and default/portrait lifecycle."""

from copy import deepcopy
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.shared.candidate_values import FieldFailure
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

Json = dict[str, Any]


def content(entry_id: str | None = None, block_id: str | None = None) -> Json:
    return {
        "contacts": {"full_name": "Ada", "phone_number": None, "email": None},
        "header_presentation": {"optional_items": []},
        "sections": [
            {
                "kind": "SKILL",
                "members": [
                    {
                        "entry_id": entry_id or str(uuid4()),
                        "fields": {"skill_name": "Python"},
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "block_id": block_id or str(uuid4()),
                                "runs": [{"text": "Built systems", "marks": []}],
                            }
                        ],
                    }
                ],
            }
        ],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#000000",
        },
    }


def create(authority: CandidateAuthority, **values: object) -> Json:
    return authority.command(
        "RESUME_CREATE",
        {"request_id": str(uuid4()), "resume_name": "R", **content(), **values},
    )


def test_save_preserves_ids_and_historical_versions_are_exact(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        first = create(authority)
        root = cast(Json, first["resume"])
        old = cast(Json, first["resume_version"])
        changed: Json = deepcopy(
            {
                key: old[key]
                for key in (
                    "contacts",
                    "header_presentation",
                    "sections",
                    "document_presentation",
                )
            },
        )
        changed["sections"][0]["members"][0]["content"][0]["runs"][0]["text"] = "Changed"  # type: ignore[index]
        saved = authority.command(
            "RESUME_SAVE",
            {"request_id": str(uuid4()), "revision": 1, **changed},
            cast(str, root["resume_id"]),
        )
        assert saved["resume"]["revision"] == 2
        assert (
            saved["resume_version"]["sections"][0]["members"][0]["entry_id"]
            == old["sections"][0]["members"][0]["entry_id"]
        )
        assert authority.version(cast(str, old["resume_version_id"])) == old
        replay = authority.command(
            "RESUME_SAVE",
            {"request_id": str(uuid4()), "revision": 2, **changed},
            cast(str, root["resume_id"]),
        )
        assert replay["outcome"] == "UNCHANGED"


def test_historical_ids_can_be_restored_but_not_transferred(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        first = create(authority)
        old = cast(Json, first["resume_version"])
        root = cast(Json, first["resume"])
        section = cast(list[Json], old["sections"])[0]
        entry = cast(list[Json], section["members"])[0]
        first_block = cast(list[Json], entry["content"])[0]
        entry_id = cast(str, entry["entry_id"])
        block_id = cast(str, first_block["block_id"])
        empty: Json = content()
        empty["sections"] = []
        authority.command(
            "RESUME_SAVE",
            {"request_id": str(uuid4()), "revision": 1, **empty},
            cast(str, root["resume_id"]),
        )
        restored = authority.command(
            "RESUME_SAVE",
            {
                "request_id": str(uuid4()),
                "revision": 2,
                **content(entry_id, block_id),
            },
            cast(str, root["resume_id"]),
        )
        assert restored["outcome"] == "UPDATED"
        assert restored["resume"]["revision"] == 3
        with pytest.raises(FieldFailure) as transferred:
            create(authority, **content(entry_id, block_id))
        assert transferred.value.field_code == "INVALID_REFERENCE"


def test_default_remove_and_portrait_source_change_atomically(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store)
        first = create(authority)
        second = create(authority, resume_name="Second")
        assert authority.portrait()["state"]["status"] == "QUEUED"
        old_build = authority.portrait()["state"]["build_id"]
        removed = authority.command(
            "RESUME_REMOVE",
            {
                "request_id": str(uuid4()),
                "revision": 1,
                "default_resume_selection": {"revision": 2},
                "replacement_resume_id": second["resume"]["resume_id"],
            },
            first["resume"]["resume_id"],
        )
        assert removed["default_resume_selection"] == {
            "default_resume_id": second["resume"]["resume_id"],
            "revision": 3,
        }
        state = authority.portrait()["state"]
        assert state["source_resume_version_id"] == second["resume_version"]["resume_version_id"]
        assert state["status"] == "QUEUED"
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT status FROM portrait_builds WHERE build_id=?", (old_build,)
                ).scalar_one()
                == "OBSOLETE"
            )
        with pytest.raises(Failure, match="REVISION_CONFLICT"):
            authority.command(
                "DEFAULT_RESUME_SET",
                {
                    "request_id": str(uuid4()),
                    "revision": 2,
                    "default_resume_id": second["resume"]["resume_id"],
                },
            )
