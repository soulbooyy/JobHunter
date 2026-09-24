"""Materials consume one exact independent ResumeVersion and no retired authorities."""

from pathlib import Path
from typing import Any, cast
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
    MaterialSources,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

Json = dict[str, Any]


def create_resume(store: Store, *, populated: bool) -> Json:
    sections: list[Json] = []
    if populated:
        sections = [
            {
                "kind": "PROJECT",
                "members": [
                    {
                        "entry_id": str(uuid4()),
                        "fields": {
                            "project_name": "Engine",
                            "role_title": "Author",
                            "project_url": "https://example.test/exact",
                            "start_month": "2026-01",
                            "end_month": None,
                        },
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "block_id": str(uuid4()),
                                "runs": [{"text": "Exact body", "marks": []}],
                            }
                        ],
                    }
                ],
            }
        ]
    return CandidateAuthority(store).command(
        "RESUME_CREATE",
        {
            "request_id": str(uuid4()),
            "resume_name": "Exact source",
            "contacts": {
                "full_name": "Ada Lovelace" if populated else None,
                "phone_number": None,
                "email": "ada@example.test" if populated else None,
            },
            "header_presentation": {"optional_items": []},
            "sections": sections,
            "document_presentation": {
                "font_family": "HEITI",
                "font_size_pt": 12,
                "line_spacing_pt": 14,
                "theme_color": "#112233",
            },
        },
    )


def test_material_source_is_the_exact_saved_resume_version(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        saved = create_resume(store, populated=True)
        version = cast(Json, saved["resume_version"])
        result = store.run(
            lambda conn: MaterialSources(conn).read(cast(str, version["resume_version_id"]))
        )
        assert result.model_dump(mode="json") == {"resume_version": version}


def test_material_source_rejects_corrupt_saved_payload(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        saved = create_resume(store, populated=False)
        version = cast(Json, saved["resume_version"])
        identity = cast(str, version["resume_version_id"])
        with store.engine.begin() as conn:
            conn.exec_driver_sql(
                "UPDATE resume_versions SET contacts='{}' WHERE resume_version_id=?", (identity,)
            )
        with pytest.raises(Failure, match="INTERNAL_ERROR"):
            store.run(lambda conn: MaterialSources(conn).read(identity))
