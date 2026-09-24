"""Independent schema-2 Resume documents with stable logical entry/block identities."""

import re
from typing import Annotated, Literal, Self, cast

from pydantic import AfterValidator, BeforeValidator, Field, field_validator, model_validator

from jobhunter.domain.evidence.models import FIELD_MODELS, Kind
from jobhunter.domain.manual_application_entries.models import ApplicationUrl
from jobhunter.domain.profile.models import ProfileContent
from jobhunter.domain.shared.candidate_values import (
    ShortText,
    half_number,
    no_controls,
    nonblank,
    short,
    short_schema,
)
from jobhunter.domain.shared.values import (
    DTO,
    TRIM,
    Revision,
    UtcTimestamp,
    UuidV4,
    invalid,
    scalar,
)
from jobhunter.domain.workspace.selection import DefaultSelection, SelectionToken


class Emphasis(DTO):
    type: Literal["BOLD", "ITALIC", "UNDERLINE"]


class Link(DTO):
    type: Literal["LINK"]
    url: ApplicationUrl


Mark = Annotated[Emphasis | Link, Field(discriminator="type")]
MARK_ORDER = ("BOLD", "ITALIC", "UNDERLINE", "LINK")


def run_text(value: object) -> str:
    value = no_controls(value)
    if not value:
        invalid("BLANK_VALUE")
    return value


class TextRun(DTO):
    text: Annotated[str, BeforeValidator(run_text)]
    marks: list[Mark]

    @field_validator("marks")
    @classmethod
    def admit_marks(cls, marks: list[Emphasis | Link]) -> list[Emphasis | Link]:
        if len({m.type for m in marks}) != len(marks):
            invalid("INVALID_FORMAT")
        return sorted(marks, key=lambda mark: MARK_ORDER.index(mark.type))

    @model_validator(mode="after")
    def whitespace(self) -> Self:
        if not self.text.strip(TRIM) and self.marks:
            invalid("INVALID_FORMAT")
        return self


def merge_runs(runs: list[TextRun]) -> list[TextRun]:
    text = "".join(run.text for run in runs)
    nonblank(text)
    if len(text) > 10000:
        invalid("TOO_LONG")
    result: list[TextRun] = []
    for run in runs:
        if result and result[-1].marks == run.marks:
            result[-1] = TextRun(text=result[-1].text + run.text, marks=run.marks)
        else:
            result.append(run.model_copy(deep=True))
    if len(result) > 256:
        invalid("OUT_OF_RANGE")
    return result


Runs = Annotated[list[TextRun], Field(min_length=1), AfterValidator(merge_runs)]


class Paragraph(DTO):
    type: Literal["PARAGRAPH"]
    block_id: UuidV4
    runs: Runs


class ListItem(DTO):
    block_id: UuidV4
    runs: Runs


class RunList(DTO):
    type: Literal["UNORDERED_LIST", "ORDERED_LIST"]
    items: list[ListItem] = Field(min_length=1, max_length=100)


Block = Annotated[Paragraph | RunList, Field(discriminator="type")]


def block_items(blocks: list[Paragraph | RunList]) -> list[Paragraph | ListItem]:
    return [
        item
        for block in blocks
        for item in ([block] if isinstance(block, Paragraph) else block.items)
    ]


def text_size(blocks: list[Paragraph | RunList]) -> int:
    return sum(sum(len(run.text) for run in item.runs) for item in block_items(blocks))


def body_capacity(blocks: list[Paragraph | RunList]) -> list[Paragraph | RunList]:
    if text_size(blocks) > 50000:
        invalid("OUT_OF_RANGE")
    ids = [item.block_id for item in block_items(blocks)]
    if len(ids) != len(set(ids)):
        invalid("INVALID_FORMAT")
    return blocks


Content = Annotated[list[Block], Field(max_length=100), AfterValidator(body_capacity)]


class ResumeEntry(DTO):
    entry_id: UuidV4
    fields: dict[str, object]
    content: Content


class Section(DTO):
    kind: Kind
    members: list[ResumeEntry] = Field(min_length=1, max_length=100)

    @model_validator(mode="before")
    @classmethod
    def canonical_fields(cls, value: object) -> object:
        if not isinstance(value, dict):
            return value
        raw = cast(dict[str, object], value)
        kind, members = raw.get("kind"), raw.get("members")
        if isinstance(kind, str) and kind in FIELD_MODELS and isinstance(members, list):
            copied = dict(raw)
            normalized: list[object] = []
            for member in cast(list[object], members):
                if not isinstance(member, dict) or "fields" not in member:
                    normalized.append(cast(object, member))
                    continue
                item = dict(cast(dict[str, object], member))
                item["fields"] = (
                    FIELD_MODELS[kind].model_validate(item["fields"]).model_dump(mode="json")
                )
                normalized.append(item)
            copied["members"] = normalized
            return copied
        return raw


class HeaderItem(DTO):
    kind: Annotated[
        Literal[
            "JOB_SEARCH_STATUS",
            "JOB_INTENTION",
            "EXPECTED_POSITION",
            "EXPECTED_CITY",
            "EXPECTED_SALARY",
            "HIGHEST_EDUCATION",
            "GENDER",
            "POLITICAL_AFFILIATION",
            "YEARS_OF_EXPERIENCE",
        ],
        BeforeValidator(scalar),
    ]
    value: ShortText


class Header(DTO):
    optional_items: list[HeaderItem]

    @field_validator("optional_items")
    @classmethod
    def unique(cls, items: list[HeaderItem]) -> list[HeaderItem]:
        if len({item.kind for item in items}) != len(items):
            invalid("INVALID_FORMAT")
        return items


def color(value: object) -> str:
    value = scalar(value)
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        invalid("INVALID_FORMAT")
    return value.upper()


class Presentation(DTO):
    font_family: Annotated[
        Literal["SOURCE_HAN_SANS", "HEITI", "SONGTI", "KAITI"], BeforeValidator(scalar)
    ]
    font_size_pt: Annotated[
        float, Field(ge=12, le=20, multiple_of=0.5), BeforeValidator(half_number)
    ]
    line_spacing_pt: Annotated[
        float, Field(ge=14, le=30, multiple_of=0.5), BeforeValidator(half_number)
    ]
    theme_color: Annotated[str, Field(pattern=r"^#[0-9A-Fa-f]{6}$"), BeforeValidator(color)]

    @model_validator(mode="after")
    def line_height(self) -> Self:
        if self.line_spacing_pt < self.font_size_pt + 2:
            invalid("INVALID_FORMAT")
        return self


def sections_admission(sections: list[Section]) -> list[Section]:
    entries = [member for section in sections for member in section.members]
    entry_ids = [entry.entry_id for entry in entries]
    block_ids = [item.block_id for entry in entries for item in block_items(entry.content)]
    if (
        len({section.kind for section in sections}) != len(sections)
        or len(entry_ids) != len(set(entry_ids))
        or len(block_ids) != len(set(block_ids))
    ):
        invalid("INVALID_FORMAT")
    if len(entries) > 100 or sum(text_size(entry.content) for entry in entries) > 200000:
        invalid("OUT_OF_RANGE")
    return sections


ResumeName = Annotated[
    str, Field(min_length=1, max_length=120), BeforeValidator(short(120)), short_schema(120)
]


class ResumeContent(DTO):
    contacts: ProfileContent
    header_presentation: Header
    sections: Annotated[list[Section], AfterValidator(sections_admission)]
    document_presentation: Presentation


class ResumeCreate(ResumeContent):
    request_id: UuidV4
    resume_name: ResumeName


class ResumeSave(ResumeContent):
    request_id: UuidV4
    revision: Revision


class ResumeRename(DTO):
    request_id: UuidV4
    revision: Revision
    resume_name: ResumeName


class ResumeRemove(DTO):
    request_id: UuidV4
    revision: Revision
    default_resume_selection: SelectionToken
    replacement_resume_id: UuidV4 | None


class Resume(DTO):
    resume_id: UuidV4
    resume_name: ResumeName
    status: Literal["ACTIVE", "REMOVED"]
    current_resume_version_id: UuidV4
    revision: Revision
    created_at: UtcTimestamp
    updated_at: UtcTimestamp


class ResumeVersion(ResumeContent):
    resume_version_id: UuidV4
    resume_id: UuidV4
    schema_version: Literal[2]
    created_at: UtcTimestamp


class ResumePair(DTO):
    resume: Resume
    resume_version: ResumeVersion

    @model_validator(mode="after")
    def exact_current(self) -> Self:
        if (
            self.resume.resume_id != self.resume_version.resume_id
            or self.resume.current_resume_version_id != self.resume_version.resume_version_id
        ):
            invalid("INVALID_FORMAT")
        return self


class ResumeList(DTO):
    resumes: list[Resume]
    default_resume_selection: DefaultSelection


class ResumeResult(ResumePair):
    request_id: UuidV4
    outcome: Literal["UPDATED", "UNCHANGED"]


class ResumeSelectionResult(ResumePair):
    request_id: UuidV4
    outcome: Literal["CREATED", "REMOVED", "UNCHANGED"]
    default_resume_selection: DefaultSelection


class SelectionResult(DTO):
    request_id: UuidV4
    outcome: Literal["UPDATED", "UNCHANGED"]
    default_resume_selection: DefaultSelection
