"""Typed immutable facts and plain semantic bodies; no Resume expression authority."""

import re
from typing import Annotated, Literal, Self

from pydantic import AfterValidator, BeforeValidator, Field, field_validator, model_validator

from jobhunter.domain.manual_application_entries.models import ApplicationUrl
from jobhunter.domain.shared.candidate_values import Month, ShortText, no_controls, short_schema
from jobhunter.domain.shared.values import (
    DTO,
    TRIM,
    UUID_PATTERN,
    Revision,
    UtcTimestamp,
    UuidV4,
    invalid,
    scalar,
)

Kind = Annotated[
    Literal["EDUCATION", "WORK_EXPERIENCE", "PROJECT", "SKILL", "AWARD", "CERTIFICATION"],
    BeforeValidator(scalar),
]
Education = Annotated[
    Literal[
        "SECONDARY_VOCATIONAL", "HIGH_SCHOOL", "ASSOCIATE", "BACHELOR", "MASTER", "MBA", "DOCTORATE"
    ],
    BeforeValidator(scalar),
]


class Period(DTO):
    start_month: Month | None
    end_month: Month | None

    @model_validator(mode="after")
    def interval(self) -> Self:
        if (
            self.start_month is not None
            and self.end_month is not None
            and self.start_month > self.end_month
        ):
            invalid("INVALID_FORMAT")
        return self


class EducationFields(Period):
    school_name: ShortText
    degree: Education
    major: ShortText | None


class WorkFields(Period):
    company_name: ShortText
    role_title: ShortText


class ProjectFields(Period):
    project_name: ShortText
    role_title: ShortText | None
    project_url: ApplicationUrl | None


class SkillFields(DTO):
    skill_name: ShortText


class AwardFields(DTO):
    award_name: ShortText
    awarding_organization: ShortText | None
    awarded_month: Month | None


class CertificationFields(DTO):
    certification_name: ShortText
    issuing_organization: ShortText | None
    issued_month: Month | None


Fields = (
    EducationFields | WorkFields | ProjectFields | SkillFields | AwardFields | CertificationFields
)
FIELD_MODELS: dict[
    str,
    type[
        EducationFields
        | WorkFields
        | ProjectFields
        | SkillFields
        | AwardFields
        | CertificationFields
    ],
] = {
    "EDUCATION": EducationFields,
    "WORK_EXPERIENCE": WorkFields,
    "PROJECT": ProjectFields,
    "SKILL": SkillFields,
    "AWARD": AwardFields,
    "CERTIFICATION": CertificationFields,
}


def body_text(value: object) -> str:
    value = no_controls(value).strip(TRIM)
    if not value:
        invalid("BLANK_VALUE")
    if len(value) > 10000:
        invalid("TOO_LONG")
    return value


BodyText = Annotated[
    str, Field(min_length=1, max_length=10000), BeforeValidator(body_text), short_schema(10000)
]


class Paragraph(DTO):
    type: Literal["PARAGRAPH"]
    text: BodyText


class TextList(DTO):
    type: Literal["UNORDERED_LIST", "ORDERED_LIST"]
    items: list[BodyText] = Field(min_length=1, max_length=100)


Block = Annotated[Paragraph | TextList, Field(discriminator="type")]


def body_capacity(blocks: list[Paragraph | TextList]) -> list[Paragraph | TextList]:
    size = sum(len(b.text) if isinstance(b, Paragraph) else sum(map(len, b.items)) for b in blocks)
    if size > 50000:
        invalid("OUT_OF_RANGE")
    return blocks


Content = Annotated[list[Block], Field(max_length=100), AfterValidator(body_capacity)]


class EvidenceEnvelope(DTO):
    request_id: UuidV4
    fields: dict[str, object]
    content: Content


class EvidenceUpdate(EvidenceEnvelope):
    revision: Revision


class EvidenceCreate(EvidenceEnvelope):
    kind: Kind


class EvidenceRetire(DTO):
    request_id: UuidV4
    revision: Revision


class EvidenceItem(DTO):
    evidence_item_id: UuidV4
    kind: Kind
    status: Literal["ACTIVE", "RETIRED"]
    current_evidence_item_version_id: UuidV4
    revision: Revision
    created_at: UtcTimestamp
    updated_at: UtcTimestamp


class EvidenceVersion(DTO):
    evidence_item_version_id: UuidV4
    evidence_item_id: UuidV4
    schema_version: Literal[1]
    fields: Fields
    content: Content
    created_at: UtcTimestamp


class EvidencePair(DTO):
    evidence_item: EvidenceItem
    evidence_item_version: EvidenceVersion


class EvidenceExact(DTO):
    kind: Kind
    evidence_item_version: EvidenceVersion


class EvidenceMember(DTO):
    evidence_item_id: UuidV4
    evidence_item_version_id: UuidV4


class Baseline(DTO):
    evidence_baseline_snapshot_id: UuidV4
    schema_version: Literal[1]
    members: list[EvidenceMember]
    created_at: UtcTimestamp


class EvidenceProjection(DTO):
    evidence_item: EvidenceItem
    current_evidence_item_version_id: UuidV4
    fields: Fields


class EvidenceList(DTO):
    evidence_items: list[EvidenceProjection]


class EvidenceResult(EvidencePair):
    request_id: UuidV4
    outcome: Literal["CREATED", "UPDATED", "RETIRED", "UNCHANGED"]
    evidence_baseline_snapshot_id: UuidV4


# Current independent-Resume projection. The older authority models above remain only
# as historical types until their callers are removed by this schema transition.
ExtractionKey = Annotated[
    str,
    Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$"),
    BeforeValidator(scalar),
]


class EvidenceRef(DTO):
    resume_version_id: UuidV4
    extraction_key: ExtractionKey
    evidence_id: str

    @field_validator("evidence_id")
    @classmethod
    def exact_id(cls, value: str) -> str:
        value = scalar(value)
        if not re.fullmatch(
            rf"(?:entry/{UUID_PATTERN[1:-1]}|block/{UUID_PATTERN[1:-1]}/{UUID_PATTERN[1:-1]})",
            value,
        ):
            invalid("INVALID_FORMAT")
        return value


class EntryEvidenceUnit(DTO):
    evidence_id: str
    entry_id: UuidV4
    kind: Kind
    fields: dict[str, object]
    content: list[dict[str, object]]


class BlockEvidenceUnit(DTO):
    evidence_id: str
    entry_id: UuidV4
    block_id: UuidV4
    text: str


class CandidateEvidenceProjection(DTO):
    schema_version: Literal[1]
    resume_version_id: UuidV4
    extraction_key: ExtractionKey
    entries: list[EntryEvidenceUnit]
    blocks: list[BlockEvidenceUnit]

    @model_validator(mode="after")
    def coherent_units(self) -> Self:
        entries = {entry.entry_id: entry for entry in self.entries}
        if len(entries) != len(self.entries):
            invalid("INVALID_FORMAT")
        for entry in self.entries:
            if entry.evidence_id != f"entry/{entry.entry_id}":
                invalid("INVALID_FORMAT")
        block_ids: set[str] = set()
        evidence_ids = {entry.evidence_id for entry in self.entries}
        for block in self.blocks:
            if block.entry_id not in entries or block.block_id in block_ids:
                invalid("INVALID_FORMAT")
            if block.evidence_id != f"block/{block.entry_id}/{block.block_id}":
                invalid("INVALID_FORMAT")
            block_ids.add(block.block_id)
            evidence_ids.add(block.evidence_id)
        if len(evidence_ids) != len(self.entries) + len(self.blocks):
            invalid("INVALID_FORMAT")
        return self
