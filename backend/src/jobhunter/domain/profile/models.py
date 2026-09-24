"""Profile owns only exact nullable contact snapshots."""

import re
from typing import Annotated, Literal, Self

from pydantic import BeforeValidator, Field, field_validator, model_validator

from jobhunter.domain.evidence.models import CandidateEvidenceProjection, EvidenceRef, ExtractionKey
from jobhunter.domain.shared.candidate_values import no_controls, nonblank, short, short_schema
from jobhunter.domain.shared.values import (
    DTO,
    TRIM,
    Revision,
    UtcTimestamp,
    UuidV4,
    invalid,
    text_value,
)
from jobhunter.domain.workspace.selection import DefaultSelection, SelectionToken


def phone(value: object) -> str:
    value = text_value(value, 50)
    if not re.fullmatch(r"\+?[0-9 ()-]+", value) or not re.search("[0-9]", value):
        invalid("INVALID_FORMAT")
    return value


def email(value: object) -> str:
    value = text_value(value, 254)
    if any(c in TRIM for c in value):
        invalid("INVALID_CHARACTERS")
    if value.count("@") != 1 or value.startswith("@") or value.endswith("@"):
        invalid("INVALID_FORMAT")
    return value


Name = Annotated[
    str, Field(min_length=1, max_length=100), BeforeValidator(short(100)), short_schema(100)
]
Phone = Annotated[str, Field(min_length=1, max_length=50), BeforeValidator(phone), short_schema(50)]
Email = Annotated[
    str, Field(min_length=1, max_length=254), BeforeValidator(email), short_schema(254)
]


def profile_text(value: object) -> str:
    value = no_controls(value)
    nonblank(value)
    return value


class ProfileContent(DTO):
    full_name: Name | None
    phone_number: Phone | None
    email: Email | None


class ProfileSave(ProfileContent):
    request_id: UuidV4
    revision: Revision


class Profile(DTO):
    profile_id: UuidV4
    current_profile_version_id: UuidV4
    revision: Revision
    created_at: UtcTimestamp
    updated_at: UtcTimestamp


class ProfileVersion(ProfileContent):
    profile_version_id: UuidV4
    profile_id: UuidV4
    schema_version: Literal[1]
    created_at: UtcTimestamp


class ProfilePair(DTO):
    profile: Profile
    profile_version: ProfileVersion


class ProfileResult(ProfilePair):
    request_id: UuidV4
    outcome: Literal["UPDATED", "UNCHANGED"]


class ProfileIndexEntry(DTO):
    source_entry_id: UuidV4
    name: Annotated[str, BeforeValidator(profile_text)]
    description: Annotated[str, BeforeValidator(profile_text)]
    evidence_refs: list[EvidenceRef] = Field(min_length=1)

    @field_validator("evidence_refs")
    @classmethod
    def unique_refs(cls, refs: list[EvidenceRef]) -> list[EvidenceRef]:
        keys = [(ref.resume_version_id, ref.extraction_key, ref.evidence_id) for ref in refs]
        if len(keys) != len(set(keys)):
            invalid("INVALID_FORMAT")
        return refs


class CandidateProfileProjection(DTO):
    schema_version: Literal[1]
    resume_version_id: UuidV4
    extraction_key: ExtractionKey
    entries: list[ProfileIndexEntry]

    @model_validator(mode="after")
    def exact_refs(self) -> Self:
        if any(
            ref.resume_version_id != self.resume_version_id
            or ref.extraction_key != self.extraction_key
            for entry in self.entries
            for ref in entry.evidence_refs
        ):
            invalid("INVALID_FORMAT")
        return self


class Generation(DTO):
    kind: Literal["MODEL", "INCREMENTAL", "REUSE"]
    run_id: UuidV4 | None
    reused_from_portrait_id: UuidV4 | None

    @model_validator(mode="after")
    def exact_source(self) -> Self:
        valid = (
            (
                self.kind == "MODEL"
                and self.run_id is not None
                and self.reused_from_portrait_id is None
            )
            or (
                self.kind == "INCREMENTAL"
                and self.run_id is not None
                and self.reused_from_portrait_id is not None
            )
            or (
                self.kind == "REUSE"
                and self.run_id is None
                and self.reused_from_portrait_id is not None
            )
        )
        if not valid:
            invalid("INVALID_FORMAT")
        return self


class Portrait(DTO):
    portrait_id: UuidV4
    schema_version: Literal[1]
    resume_version_id: UuidV4
    extraction_key: ExtractionKey
    profile: CandidateProfileProjection
    evidence: CandidateEvidenceProjection
    generation: Generation
    created_at: UtcTimestamp

    @model_validator(mode="after")
    def coherent_pair(self) -> Self:
        if any(
            value != self.resume_version_id
            for value in (self.profile.resume_version_id, self.evidence.resume_version_id)
        ) or any(
            value != self.extraction_key
            for value in (self.profile.extraction_key, self.evidence.extraction_key)
        ):
            invalid("INVALID_FORMAT")
        available = {unit.evidence_id for unit in self.evidence.entries} | {
            unit.evidence_id for unit in self.evidence.blocks
        }
        source_entries = {unit.entry_id for unit in self.evidence.entries}
        if any(
            entry.source_entry_id not in source_entries
            or ref.evidence_id not in available
            or not (
                ref.evidence_id == f"entry/{entry.source_entry_id}"
                or ref.evidence_id.startswith(f"block/{entry.source_entry_id}/")
            )
            for entry in self.profile.entries
            for ref in entry.evidence_refs
        ):
            invalid("INVALID_FORMAT")
        return self


class CurrentPortraitState(DTO):
    default_resume_selection: DefaultSelection
    source_resume_version_id: UuidV4 | None
    status: Literal["NO_SOURCE", "EMPTY_SOURCE", "QUEUED", "RUNNING", "READY", "FAILED"]
    build_id: UuidV4 | None
    portrait_id: UuidV4 | None
    failure_code: (
        Literal[
            "SOURCE_UNAVAILABLE",
            "CONFIGURATION_UNAVAILABLE",
            "INPUT_NOT_ADMITTED",
            "OUTPUT_INVALID",
            "INVOCATION_FAILED",
            "OUTCOME_UNKNOWN",
        ]
        | None
    )

    @model_validator(mode="after")
    def exact_state(self) -> Self:
        has_source = self.source_resume_version_id is not None
        has_build = self.build_id is not None
        has_portrait = self.portrait_id is not None
        has_failure = self.failure_code is not None
        if (self.status != "NO_SOURCE") != has_source:
            invalid("INVALID_FORMAT")
        if (self.status in {"QUEUED", "RUNNING", "READY", "FAILED"}) != has_build:
            invalid("INVALID_FORMAT")
        if (self.status == "READY") != has_portrait:
            invalid("INVALID_FORMAT")
        if (self.status == "FAILED") != has_failure:
            invalid("INVALID_FORMAT")
        return self


class PortraitRead(DTO):
    state: CurrentPortraitState
    portrait: Portrait | None


class PortraitRefresh(DTO):
    request_id: UuidV4
    default_resume_selection: SelectionToken
    source_resume_version_id: UuidV4


class PortraitRefreshResult(DTO):
    request_id: UuidV4
    outcome: Literal["UPDATED", "UNCHANGED"]
    state: CurrentPortraitState
