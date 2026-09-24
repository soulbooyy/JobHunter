"""Pure Entry diff, grouped output and exact-reference conformance."""

from copy import deepcopy
from typing import Any, cast

import pytest
from jobhunter.domain.evidence.models import CandidateEvidenceProjection
from jobhunter.domain.profile.incremental import (
    ProfileModelOutput,
    assemble_profile,
    evidence_diff,
    make_plan,
)
from jobhunter.domain.profile.models import Portrait

Json = dict[str, Any]


def identity(number: int) -> str:
    return f"00000000-0000-4000-8000-{number:012d}"


def projection(version: int, entries: list[Json]) -> CandidateEvidenceProjection:
    blocks: list[Json] = []
    projected: list[Json] = []
    for item in entries:
        entry_id = item["entry_id"]
        content = item.get("content", [])
        projected.append(
            {
                "evidence_id": f"entry/{entry_id}",
                "entry_id": entry_id,
                "kind": item["kind"],
                "fields": item["fields"],
                "content": content,
            }
        )
        for block in content:
            values = [block] if block["type"] == "PARAGRAPH" else cast(list[Json], block["items"])
            for value in values:
                blocks.append(
                    {
                        "evidence_id": f"block/{entry_id}/{value['block_id']}",
                        "entry_id": entry_id,
                        "block_id": value["block_id"],
                        "text": "".join(run["text"] for run in value["runs"]),
                    }
                )
    return CandidateEvidenceProjection.model_validate(
        {
            "schema_version": 1,
            "resume_version_id": identity(version),
            "extraction_key": "resume.v1",
            "entries": projected,
            "blocks": blocks,
        }
    )


def paragraph(entry: int, text: str, marks: list[dict[str, str]] | None = None) -> Json:
    return {
        "type": "PARAGRAPH",
        "block_id": identity(entry + 100),
        "runs": [{"text": text, "marks": marks or []}],
    }


def portrait(evidence: CandidateEvidenceProjection) -> Portrait:
    entries: list[Json] = []
    for index, source in enumerate(evidence.entries):
        entries.append(
            {
                "source_entry_id": source.entry_id,
                "name": "Redis",
                "description": f"Supported in Entry {index}",
                "evidence_refs": [
                    {
                        "resume_version_id": evidence.resume_version_id,
                        "extraction_key": evidence.extraction_key,
                        "evidence_id": source.evidence_id,
                    }
                ],
            }
        )
    return Portrait.model_validate(
        {
            "portrait_id": identity(900),
            "schema_version": 1,
            "resume_version_id": evidence.resume_version_id,
            "extraction_key": evidence.extraction_key,
            "profile": {
                "schema_version": 1,
                "resume_version_id": evidence.resume_version_id,
                "extraction_key": evidence.extraction_key,
                "entries": entries,
            },
            "evidence": evidence.model_dump(mode="json"),
            "generation": {
                "kind": "MODEL",
                "run_id": identity(901),
                "reused_from_portrait_id": None,
            },
            "created_at": "2026-09-24T00:00:00.000Z",
        }
    )


def test_diff_ignores_excluded_values_and_global_order_but_detects_entry_semantics() -> None:
    first: Json = {
        "entry_id": identity(1),
        "kind": "PROJECT",
        "fields": {
            "project_name": "Cache",
            "role_title": "Engineer",
            "project_url": "https://old.example.test",
            "start_month": None,
            "end_month": None,
        },
        "content": [paragraph(1, "Redis")],
    }
    second: Json = {
        "entry_id": identity(2),
        "kind": "SKILL",
        "fields": {"skill_name": "Python"},
        "content": [],
    }
    old = projection(10, [first, second])
    changed_presentation = deepcopy(first)
    cast(Json, changed_presentation["fields"])["project_url"] = "https://new.example.test"
    changed_block = cast(list[Json], changed_presentation["content"])[0]
    cast(list[Json], changed_block["runs"])[0]["marks"] = [
        {"type": "LINK", "url": "https://hidden.example.test"}
    ]
    reordered = projection(11, [second, changed_presentation])
    diff = evidence_diff(old, reordered)
    assert diff.dirty_entry_ids == []
    assert diff.unchanged_entry_ids == [identity(2), identity(1)]
    assert diff.target_entry_order == [identity(2), identity(1)]

    changed_background = deepcopy(changed_presentation)
    cast(Json, changed_background["fields"])["role_title"] = "Lead"
    dirty = evidence_diff(old, projection(12, [changed_background, second]))
    assert dirty.dirty_entry_ids == [identity(1)]
    assert dirty.unchanged_entry_ids == [identity(2)]


@pytest.mark.parametrize(
    "kind,fields",
    [
        (
            "EDUCATION",
            {
                "school_name": "A",
                "degree": "BACHELOR",
                "major": None,
                "start_month": None,
                "end_month": None,
            },
        ),
        (
            "WORK_EXPERIENCE",
            {"company_name": "A", "role_title": "R", "start_month": None, "end_month": None},
        ),
        (
            "PROJECT",
            {
                "project_name": "A",
                "role_title": None,
                "project_url": None,
                "start_month": None,
                "end_month": None,
            },
        ),
        ("SKILL", {"skill_name": "A"}),
        ("AWARD", {"award_name": "A", "awarding_organization": None, "awarded_month": None}),
        (
            "CERTIFICATION",
            {"certification_name": "A", "issuing_organization": None, "issued_month": None},
        ),
    ],
)
def test_every_entry_kind_and_structured_only_entry_is_diffed(
    kind: str, fields: dict[str, Any]
) -> None:
    source: Json = {
        "entry_id": identity(1),
        "kind": kind,
        "fields": fields,
        "content": [],
    }
    target = deepcopy(source)
    first_key = next(iter(fields))
    cast(Json, target["fields"])[first_key] = "Changed"
    diff = evidence_diff(projection(10, [source]), projection(11, [target]))
    assert diff.dirty_entry_ids == [identity(1)]


def test_grouped_assembly_replaces_dirty_group_and_keeps_same_label_entries_separate() -> None:
    one: Json = {
        "entry_id": identity(1),
        "kind": "SKILL",
        "fields": {"skill_name": "Redis"},
        "content": [paragraph(1, "Old")],
    }
    two: Json = {
        "entry_id": identity(2),
        "kind": "PROJECT",
        "fields": {
            "project_name": "Redis service",
            "role_title": None,
            "project_url": None,
            "start_month": None,
            "end_month": None,
        },
        "content": [],
    }
    baseline_evidence = projection(10, [one, two])
    changed = deepcopy(one)
    changed_block = cast(list[Json], changed["content"])[0]
    cast(list[Json], changed_block["runs"])[0]["text"] = "New"
    target = projection(11, [two, changed])
    plan = make_plan(
        build_id=identity(800),
        trigger_mode="AUTOMATIC",
        configuration_key="portrait.v1",
        target=target,
        baseline=portrait(baseline_evidence),
    )
    assert plan.generated_entry_ids == [identity(1)]
    assert plan.reused_entry_ids == [identity(2)]
    assert plan.target_entry_order == [identity(2), identity(1)]

    empty_replacement = ProfileModelOutput.model_validate(
        {"entry_results": [{"source_entry_id": identity(1), "entries": []}]}
    )
    assembled = assemble_profile(plan, target, empty_replacement)
    assert [entry.source_entry_id for entry in assembled.entries] == [identity(2)]
    assert assembled.entries[0].evidence_refs[0].resume_version_id == identity(11)

    with pytest.raises(ValueError):
        assemble_profile(plan, target, ProfileModelOutput(entry_results=[]))
    with pytest.raises(ValueError):
        assemble_profile(
            plan,
            target,
            ProfileModelOutput.model_validate(
                {
                    "entry_results": [
                        {
                            "source_entry_id": identity(1),
                            "entries": [
                                {
                                    "name": "Bad",
                                    "description": "Cross Entry",
                                    "evidence_refs": [f"entry/{identity(2)}"],
                                }
                            ],
                        }
                    ]
                }
            ),
        )


def test_full_plan_bypasses_baseline_and_generates_every_current_entry() -> None:
    evidence = projection(
        10,
        [
            {
                "entry_id": identity(1),
                "kind": "SKILL",
                "fields": {"skill_name": "Python"},
                "content": [],
            }
        ],
    )
    plan = make_plan(
        build_id=identity(800),
        trigger_mode="FULL",
        configuration_key="portrait.v1",
        target=evidence,
        baseline=portrait(evidence),
    )
    assert plan.baseline_portrait_id is None
    assert plan.generated_entry_ids == [identity(1)]
    assert plan.reused_entry_ids == []
