"""Pure Entry-scoped diff, frozen-plan and grouped-profile assembly rules."""

from collections import defaultdict
from typing import Annotated, Any, Literal, Self

from pydantic import BeforeValidator, Field, field_validator, model_validator

from jobhunter.domain.evidence.models import CandidateEvidenceProjection, EvidenceRef, ExtractionKey
from jobhunter.domain.profile.models import (
    CandidateProfileProjection,
    Portrait,
    ProfileIndexEntry,
    profile_text,
)
from jobhunter.domain.shared.values import DTO, UuidV4, invalid


class EntryDiff(DTO):
    target_entry_order: list[UuidV4]
    dirty_entry_ids: list[UuidV4]
    unchanged_entry_ids: list[UuidV4]
    removed_entry_ids: list[UuidV4]

    @model_validator(mode="after")
    def complete_partition(self) -> Self:
        target = self.dirty_entry_ids + self.unchanged_entry_ids
        if (
            len(self.target_entry_order) != len(set(self.target_entry_order))
            or len(target) != len(set(target))
            or set(target) != set(self.target_entry_order)
            or len(self.removed_entry_ids) != len(set(self.removed_entry_ids))
            or set(target) & set(self.removed_entry_ids)
        ):
            invalid("INVALID_FORMAT")
        return self


ConfigurationKey = Annotated[
    str,
    Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._+-]{0,127}$"),
    BeforeValidator(profile_text),
]


class DerivationPlan(DTO):
    schema_version: Literal[1]
    build_id: UuidV4
    trigger_mode: Literal["AUTOMATIC", "FULL"]
    configuration_key: ConfigurationKey
    target_resume_version_id: UuidV4
    extraction_key: ExtractionKey
    baseline_portrait_id: UuidV4 | None
    baseline_resume_version_id: UuidV4 | None
    reattachment_portrait_id: UuidV4 | None
    target_entry_order: list[UuidV4]
    generated_entry_ids: list[UuidV4]
    reused_entry_ids: list[UuidV4]
    removed_entry_ids: list[UuidV4]
    reused_profile_entries: list[ProfileIndexEntry]

    @model_validator(mode="after")
    def exact_plan(self) -> Self:
        target = self.generated_entry_ids + self.reused_entry_ids
        reused_sources = {entry.source_entry_id for entry in self.reused_profile_entries}
        is_reattachment = self.reattachment_portrait_id is not None
        if (
            len(self.target_entry_order) != len(set(self.target_entry_order))
            or len(target) != len(set(target))
            or (not is_reattachment and set(target) != set(self.target_entry_order))
            or len(self.removed_entry_ids) != len(set(self.removed_entry_ids))
            or set(target) & set(self.removed_entry_ids)
            or not reused_sources.issubset(set(self.reused_entry_ids))
        ):
            invalid("INVALID_FORMAT")
        if (self.baseline_portrait_id is None) != (self.baseline_resume_version_id is None):
            invalid("INVALID_FORMAT")
        if self.trigger_mode == "FULL" and (
            self.baseline_portrait_id is not None
            or self.reattachment_portrait_id is not None
            or self.reused_entry_ids
            or self.removed_entry_ids
            or self.reused_profile_entries
            or self.generated_entry_ids != self.target_entry_order
        ):
            invalid("INVALID_FORMAT")
        if is_reattachment and (
            self.trigger_mode != "AUTOMATIC"
            or self.reattachment_portrait_id != self.baseline_portrait_id
            or self.baseline_resume_version_id != self.target_resume_version_id
            or self.generated_entry_ids
            or self.reused_entry_ids
            or self.removed_entry_ids
            or self.reused_profile_entries
        ):
            invalid("INVALID_FORMAT")
        if (
            self.trigger_mode == "AUTOMATIC"
            and self.baseline_portrait_id is None
            and (
                self.generated_entry_ids != self.target_entry_order
                or self.reused_entry_ids
                or self.removed_entry_ids
                or self.reused_profile_entries
            )
        ):
            invalid("INVALID_FORMAT")
        return self


class ModelProfileEntry(DTO):
    name: Annotated[str, BeforeValidator(profile_text)]
    description: Annotated[str, BeforeValidator(profile_text)]
    evidence_refs: list[str] = Field(min_length=1)

    @field_validator("evidence_refs")
    @classmethod
    def unique_refs(cls, refs: list[str]) -> list[str]:
        if len(refs) != len(set(refs)):
            invalid("INVALID_FORMAT")
        return refs


class EntryResult(DTO):
    source_entry_id: UuidV4
    entries: list[ModelProfileEntry]


class ProfileModelOutput(DTO):
    entry_results: list[EntryResult]

    @field_validator("entry_results")
    @classmethod
    def unique_groups(cls, groups: list[EntryResult]) -> list[EntryResult]:
        if len(groups) != len({group.source_entry_id for group in groups}):
            invalid("INVALID_FORMAT")
        return groups


def semantic_entry(entry: dict[str, Any]) -> dict[str, Any]:
    """Project one retained Entry to the exact model-admitted diff representation."""
    fields = {key: value for key, value in entry["fields"].items() if key != "project_url"}
    content: list[dict[str, Any]] = []
    for block in entry["content"]:
        if block["type"] == "PARAGRAPH":
            content.append(
                {
                    "type": "PARAGRAPH",
                    "block_id": block["block_id"],
                    "text": "".join(run["text"] for run in block["runs"]),
                }
            )
        else:
            content.append(
                {
                    "type": block["type"],
                    "items": [
                        {
                            "block_id": item["block_id"],
                            "text": "".join(run["text"] for run in item["runs"]),
                        }
                        for item in block["items"]
                    ],
                }
            )
    return {"kind": entry["kind"], "fields": fields, "content": content}


def evidence_diff(
    baseline: CandidateEvidenceProjection, target: CandidateEvidenceProjection
) -> EntryDiff:
    if baseline.extraction_key != target.extraction_key:
        invalid("INVALID_FORMAT")
    old = {entry.entry_id: entry.model_dump(mode="json") for entry in baseline.entries}
    new = {entry.entry_id: entry.model_dump(mode="json") for entry in target.entries}
    order = [entry.entry_id for entry in target.entries]
    dirty = [
        identity
        for identity in order
        if identity not in old or semantic_entry(old[identity]) != semantic_entry(new[identity])
    ]
    unchanged = [identity for identity in order if identity in old and identity not in dirty]
    removed = [entry.entry_id for entry in baseline.entries if entry.entry_id not in new]
    return EntryDiff(
        target_entry_order=order,
        dirty_entry_ids=dirty,
        unchanged_entry_ids=unchanged,
        removed_entry_ids=removed,
    )


def rebind_profile_entries(
    baseline: Portrait,
    target: CandidateEvidenceProjection,
    reusable_entry_ids: list[str],
) -> list[ProfileIndexEntry]:
    available = {entry.evidence_id for entry in target.entries} | {
        block.evidence_id for block in target.blocks
    }
    reusable = set(reusable_entry_ids)
    result: list[ProfileIndexEntry] = []
    for entry in baseline.profile.entries:
        if entry.source_entry_id not in reusable:
            continue
        refs: list[EvidenceRef] = []
        for ref in entry.evidence_refs:
            if ref.evidence_id not in available:
                invalid("INVALID_FORMAT")
            refs.append(
                EvidenceRef(
                    resume_version_id=target.resume_version_id,
                    extraction_key=target.extraction_key,
                    evidence_id=ref.evidence_id,
                )
            )
        result.append(
            ProfileIndexEntry(
                source_entry_id=entry.source_entry_id,
                name=entry.name,
                description=entry.description,
                evidence_refs=refs,
            )
        )
    return result


def make_plan(
    *,
    build_id: str,
    trigger_mode: Literal["AUTOMATIC", "FULL"],
    configuration_key: str,
    target: CandidateEvidenceProjection,
    baseline: Portrait | None,
    exact_reattachment: bool = False,
) -> DerivationPlan:
    target_order = [entry.entry_id for entry in target.entries]
    base = {
        "schema_version": 1,
        "build_id": build_id,
        "trigger_mode": trigger_mode,
        "configuration_key": configuration_key,
        "target_resume_version_id": target.resume_version_id,
        "extraction_key": target.extraction_key,
        "target_entry_order": target_order,
    }
    if trigger_mode == "FULL" or baseline is None:
        return DerivationPlan.model_validate(
            {
                **base,
                "baseline_portrait_id": None,
                "baseline_resume_version_id": None,
                "reattachment_portrait_id": None,
                "generated_entry_ids": target_order,
                "reused_entry_ids": [],
                "removed_entry_ids": [],
                "reused_profile_entries": [],
            }
        )
    if baseline.extraction_key != target.extraction_key:
        invalid("INVALID_FORMAT")
    if exact_reattachment:
        if baseline.resume_version_id != target.resume_version_id:
            invalid("INVALID_FORMAT")
        return DerivationPlan.model_validate(
            {
                **base,
                "baseline_portrait_id": baseline.portrait_id,
                "baseline_resume_version_id": baseline.resume_version_id,
                "reattachment_portrait_id": baseline.portrait_id,
                "generated_entry_ids": [],
                "reused_entry_ids": [],
                "removed_entry_ids": [],
                "reused_profile_entries": [],
            }
        )
    diff = evidence_diff(baseline.evidence, target)
    return DerivationPlan.model_validate(
        {
            **base,
            "baseline_portrait_id": baseline.portrait_id,
            "baseline_resume_version_id": baseline.resume_version_id,
            "reattachment_portrait_id": None,
            "generated_entry_ids": diff.dirty_entry_ids,
            "reused_entry_ids": diff.unchanged_entry_ids,
            "removed_entry_ids": diff.removed_entry_ids,
            "reused_profile_entries": rebind_profile_entries(
                baseline, target, diff.unchanged_entry_ids
            ),
        }
    )


def assemble_profile(
    plan: DerivationPlan,
    target: CandidateEvidenceProjection,
    output: ProfileModelOutput | None,
) -> CandidateProfileProjection:
    if plan.reattachment_portrait_id is not None:
        invalid("INVALID_FORMAT")
    if (
        target.resume_version_id != plan.target_resume_version_id
        or target.extraction_key != plan.extraction_key
    ):
        invalid("INVALID_FORMAT")
    groups: dict[str, list[ProfileIndexEntry]] = defaultdict(list)
    for entry in plan.reused_profile_entries:
        groups[entry.source_entry_id].append(entry)
    requested = set(plan.generated_entry_ids)
    if requested:
        if output is None:
            invalid("INVALID_FORMAT")
        assert output is not None
        if {group.source_entry_id for group in output.entry_results} != requested:
            invalid("INVALID_FORMAT")
        available = {entry.evidence_id for entry in target.entries} | {
            block.evidence_id for block in target.blocks
        }
        for group in output.entry_results:
            for entry in group.entries:
                refs: list[EvidenceRef] = []
                for evidence_id in entry.evidence_refs:
                    if evidence_id not in available or not (
                        evidence_id == f"entry/{group.source_entry_id}"
                        or evidence_id.startswith(f"block/{group.source_entry_id}/")
                    ):
                        invalid("INVALID_FORMAT")
                    refs.append(
                        EvidenceRef(
                            resume_version_id=target.resume_version_id,
                            extraction_key=target.extraction_key,
                            evidence_id=evidence_id,
                        )
                    )
                groups[group.source_entry_id].append(
                    ProfileIndexEntry(
                        source_entry_id=group.source_entry_id,
                        name=entry.name,
                        description=entry.description,
                        evidence_refs=refs,
                    )
                )
    elif output is not None:
        invalid("INVALID_FORMAT")
    return CandidateProfileProjection(
        schema_version=1,
        resume_version_id=target.resume_version_id,
        extraction_key=target.extraction_key,
        entries=[entry for identity in plan.target_entry_order for entry in groups[identity]],
    )
