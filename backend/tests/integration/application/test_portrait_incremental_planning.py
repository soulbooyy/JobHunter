"""Durable Entry-scoped planning, zero-call reuse and refresh-mode fencing."""

from copy import deepcopy
from pathlib import Path
from typing import cast
from uuid import uuid4

from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.application.candidate.portrait import PortraitDerivation
from jobhunter.domain.evidence.models import CandidateEvidenceProjection
from jobhunter.domain.profile.incremental import (
    DerivationPlan,
    ProfileModelOutput,
    assemble_profile,
)
from jobhunter.domain.profile.models import Portrait
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import (
    CandidateRepository,
    Json,
    encoded,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
from sqlalchemy.engine import Connection

NOW = "2026-09-24T00:00:00.000Z"


def identity(number: int) -> str:
    return f"00000000-0000-4000-8000-{number:012d}"


def content(offset: int = 0) -> Json:
    return {
        "contacts": {"full_name": "Ada", "phone_number": None, "email": None},
        "header_presentation": {"optional_items": []},
        "sections": [
            {
                "kind": "SKILL",
                "members": [
                    {
                        "entry_id": identity(offset + 1),
                        "fields": {"skill_name": "Redis"},
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "block_id": identity(offset + 101),
                                "runs": [{"text": "Cache", "marks": []}],
                            }
                        ],
                    },
                    {
                        "entry_id": identity(offset + 2),
                        "fields": {"skill_name": "Python"},
                        "content": [],
                    },
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


def create(authority: CandidateAuthority, name: str, document: Json) -> Json:
    return authority.command(
        "RESUME_CREATE",
        {"request_id": str(uuid4()), "resume_name": name, **document},
    )


def publish_model_fixture(
    store: Store, build_id: str, configuration_key: str = "portrait.v1"
) -> str:
    plan = PortraitDerivation(store, clock=lambda: NOW).plan(build_id, configuration_key)

    def publish(conn: Connection) -> str:
        repo = CandidateRepository(conn)
        evidence = CandidateEvidenceProjection.model_validate(
            repo.evidence_projection(plan["target_resume_version_id"])
        )
        output = ProfileModelOutput.model_validate(
            {
                "entry_results": [
                    {
                        "source_entry_id": entry_id,
                        "entries": [
                            {
                                "name": "Redis",
                                "description": "Independent Entry group",
                                "evidence_refs": [f"entry/{entry_id}"],
                            }
                        ],
                    }
                    for entry_id in plan["generated_entry_ids"]
                ]
            }
        )
        profile = assemble_profile(DerivationPlan.model_validate(plan), evidence, output)
        portrait_id = str(uuid4())
        portrait = Portrait.model_validate(
            {
                "portrait_id": portrait_id,
                "schema_version": 1,
                "resume_version_id": evidence.resume_version_id,
                "extraction_key": evidence.extraction_key,
                "profile": profile.model_dump(mode="json"),
                "evidence": evidence.model_dump(mode="json"),
                "generation": {
                    "kind": "MODEL",
                    "run_id": str(uuid4()),
                    "reused_from_portrait_id": None,
                },
                "created_at": NOW,
            }
        ).model_dump(mode="json")
        repo.insert(
            "portraits",
            {
                "portrait_id": portrait_id,
                "resume_version_id": evidence.resume_version_id,
                "extraction_key": evidence.extraction_key,
                "portrait": encoded(portrait),
                "created_at": NOW,
            },
        )
        resume_id = conn.exec_driver_sql(
            "SELECT resume_id FROM resume_versions WHERE resume_version_id=?",
            (evidence.resume_version_id,),
        ).scalar_one()
        repo.insert(
            "portrait_derivations",
            {
                "portrait_id": portrait_id,
                "resume_id": resume_id,
                "resume_version_id": evidence.resume_version_id,
                "extraction_key": evidence.extraction_key,
                "configuration_key": configuration_key,
                "derivation_order": 1,
                "created_at": NOW,
            },
        )
        conn.exec_driver_sql(
            "UPDATE portrait_builds SET status='SUCCEEDED',result_portrait_id=?,"
            "disposition='NEW_PAIR' WHERE build_id=?",
            (portrait_id, build_id),
        )
        conn.exec_driver_sql(
            "UPDATE current_portrait_state SET status='READY',portrait_id=? WHERE singleton_key=1",
            (portrait_id,),
        )
        return portrait_id

    return store.run(publish, write=True)


def build_row(store: Store, build_id: str) -> Json:
    return store.run(lambda conn: CandidateRepository(conn).portrait_build(build_id))


def test_latest_compatible_baseline_diff_zero_call_and_exact_reattachment(
    tmp_path: Path,
) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store, clock=lambda: NOW)
        derivation = PortraitDerivation(store, clock=lambda: NOW)
        first = create(authority, "Primary", content())
        resume_id = cast(str, first["resume"]["resume_id"])
        first_build = cast(str, authority.portrait()["state"]["build_id"])
        first_portrait = publish_model_fixture(store, first_build)

        changed = deepcopy(content())
        first_member = cast(list[Json], cast(list[Json], changed["sections"])[0]["members"])[0]
        first_block = cast(list[Json], first_member["content"])[0]
        cast(list[Json], first_block["runs"])[0]["text"] = "Changed but failed derivation"
        second = authority.command(
            "RESUME_SAVE",
            {"request_id": str(uuid4()), "revision": 1, **changed},
            resume_id,
        )
        second_build = cast(str, authority.portrait()["state"]["build_id"])
        second_plan = derivation.plan(second_build, "portrait.v1")
        assert second_plan["baseline_portrait_id"] == first_portrait
        assert second_plan["generated_entry_ids"] == [identity(1)]
        assert second_plan["reused_entry_ids"] == [identity(2)]
        assert (
            second_plan["target_resume_version_id"] == second["resume_version"]["resume_version_id"]
        )

        deletion = deepcopy(changed)
        cast(list[Json], cast(list[Json], deletion["sections"])[0]["members"]).pop(0)
        third = authority.command(
            "RESUME_SAVE",
            {"request_id": str(uuid4()), "revision": 2, **deletion},
            resume_id,
        )
        third_build = cast(str, authority.portrait()["state"]["build_id"])
        third_plan = derivation.plan(third_build, "portrait.v1")
        assert third_plan["baseline_portrait_id"] == first_portrait
        assert third_plan["generated_entry_ids"] == []
        assert third_plan["reused_entry_ids"] == [identity(2)]
        assert third_plan["removed_entry_ids"] == [identity(1)]
        ready = derivation.complete_zero_call(third_build)
        assert ready["status"] == "READY"
        third_portrait = cast(str, ready["portrait_id"])
        assert third_portrait != first_portrait
        observed = authority.portrait()["portrait"]
        assert observed["generation"] == {
            "kind": "REUSE",
            "run_id": None,
            "reused_from_portrait_id": first_portrait,
        }
        assert [entry["source_entry_id"] for entry in observed["profile"]["entries"]] == [
            identity(2)
        ]
        assert (
            observed["profile"]["entries"][0]["evidence_refs"][0]["resume_version_id"]
            == third["resume_version"]["resume_version_id"]
        )

        other = create(authority, "Other", content(1000))
        authority.command(
            "DEFAULT_RESUME_SET",
            {
                "request_id": str(uuid4()),
                "revision": 2,
                "default_resume_id": other["resume"]["resume_id"],
            },
        )
        authority.command(
            "DEFAULT_RESUME_SET",
            {
                "request_id": str(uuid4()),
                "revision": 3,
                "default_resume_id": resume_id,
            },
        )
        reattach_build = cast(str, authority.portrait()["state"]["build_id"])
        reattach_plan = derivation.plan(reattach_build, "portrait.v1")
        assert reattach_plan["reattachment_portrait_id"] == third_portrait
        reattached = derivation.complete_zero_call(reattach_build)
        assert reattached["portrait_id"] == third_portrait
        assert (
            store.run(
                lambda conn: conn.exec_driver_sql(
                    "SELECT count(*) FROM portrait_derivations"
                ).scalar_one()
            )
            == 2
        )


def test_full_refresh_supersedes_automatic_and_matching_full_deduplicates(
    tmp_path: Path,
) -> None:
    with Store.open(tmp_path) as store:
        authority = CandidateAuthority(store, clock=lambda: NOW)
        first = create(authority, "Primary", content())
        source_id = first["resume_version"]["resume_version_id"]
        automatic = cast(str, authority.portrait()["state"]["build_id"])
        refreshed = authority.command(
            "PORTRAIT_REFRESH",
            {
                "request_id": str(uuid4()),
                "default_resume_selection": {"revision": 2},
                "source_resume_version_id": source_id,
            },
        )
        full = cast(str, refreshed["state"]["build_id"])
        assert refreshed["outcome"] == "UPDATED"
        assert full != automatic
        assert build_row(store, automatic)["status"] == "OBSOLETE"
        assert build_row(store, full)["trigger_mode"] == "FULL"

        duplicate = authority.command(
            "PORTRAIT_REFRESH",
            {
                "request_id": str(uuid4()),
                "default_resume_selection": {"revision": 2},
                "source_resume_version_id": source_id,
            },
        )
        assert duplicate["outcome"] == "UNCHANGED"
        assert duplicate["state"]["build_id"] == full
        plan = PortraitDerivation(store).plan(full, "portrait.v1")
        assert plan["trigger_mode"] == "FULL"
        assert plan["baseline_portrait_id"] is None
        assert plan["generated_entry_ids"] == [identity(1), identity(2)]
