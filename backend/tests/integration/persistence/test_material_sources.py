"""Materials reads consumed exact inputs without requiring unused Evidence expression."""

from pathlib import Path
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_material_projection_ignores_unused_body_but_full_reader_rejects(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        candidate = CandidateAuthority(store)
        fact = candidate.command(
            "EVIDENCE_CREATE",
            {
                "request_id": str(uuid4()),
                "kind": "SKILL",
                "fields": {"skill_name": "Python"},
                "content": [],
            },
        )
        evidence_id = fact["evidence_item"]["evidence_item_id"]
        evidence_version = fact["evidence_item_version"]["evidence_item_version_id"]
        saved = candidate.command(
            "RESUME_CREATE",
            {
                "request_id": str(uuid4()),
                "resume_name": "Name",
                "profile_version_id": candidate.pair("profile")["profile_version"][
                    "profile_version_id"
                ],
                "header_presentation": {"optional_items": []},
                "sections": [
                    {
                        "kind": "SKILL",
                        "members": [
                            {
                                "evidence_item_id": evidence_id,
                                "evidence_item_version_id": evidence_version,
                                "content": [],
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
            },
        )
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE evidence_item_versions SET content='[{}]'")
        with pytest.raises(Failure, match="INTERNAL_ERROR"):
            candidate.version("resume", saved["resume_version"]["resume_version_id"])
        from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
            MaterialSources,
        )

        result = store.run(
            lambda conn: MaterialSources(conn).read(saved["resume_version"]["resume_version_id"])
        )
        assert result.model_dump(mode="json") == {
            "resume_version": saved["resume_version"],
            "profile_version": candidate.pair("profile")["profile_version"],
            "evidence_sources": [
                {
                    "evidence_item_id": evidence_id,
                    "evidence_item_version_id": evidence_version,
                    "kind": "SKILL",
                    "fields": {"skill_name": "Python"},
                }
            ],
        }
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE evidence_item_versions SET fields='{}'")
        with pytest.raises(Failure, match="INTERNAL_ERROR"):
            store.run(
                lambda conn: MaterialSources(conn).read(
                    saved["resume_version"]["resume_version_id"]
                )
            )
