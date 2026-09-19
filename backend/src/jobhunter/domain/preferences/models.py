"""PRF canonical admission, immutable DTOs and binary Save identity."""

import hashlib
from decimal import Decimal
from typing import Annotated, Literal, cast

from pydantic import Field, WithJsonSchema, model_validator
from pydantic_core import PydanticCustomError

from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import (
    DTO,
    Revision,
    UtcTimestamp,
    UuidV4,
    scalar,
    text_value,
)

RECRUITMENT = ("CAMPUS", "INTERNSHIP", "EXPERIENCED", "PART_TIME")
EDUCATION = (
    "JUNIOR_HIGH_OR_BELOW",
    "UPPER_SECONDARY",
    "ASSOCIATE",
    "BACHELOR",
    "MASTER",
    "DOCTORATE",
)
Recruitment = Literal["CAMPUS", "INTERNSHIP", "EXPERIENCED", "PART_TIME"]
Education = Literal[
    "JUNIOR_HIGH_OR_BELOW", "UPPER_SECONDARY", "ASSOCIATE", "BACHELOR", "MASTER", "DOCTORATE"
]


class AdmissionFailure(Failure):
    def __init__(self, field: str, field_code: str) -> None:
        super().__init__("VALIDATION_ERROR")
        self.field = field
        self.field_code = field_code

    def body(self) -> dict[str, object]:
        return {**super().body(), "field_errors": [{"field": self.field, "code": self.field_code}]}


def reject(field: str, code: str) -> None:
    raise AdmissionFailure(field, code)


def object_fields(value: object, names: set[str], path: str) -> dict[str, object]:
    if not isinstance(value, dict):
        reject(path, "INVALID_TYPE")
    result = cast(dict[str, object], value)
    if result.keys() - names:
        reject(path, "UNKNOWN_FIELD")
    for name in sorted(names - result.keys()):
        reject(f"{path}.{name}" if path != "$" else name, "REQUIRED")
    return result


def enum_value(value: object, allowed: tuple[str, ...], path: str) -> str:
    try:
        text = scalar(value)
    except PydanticCustomError as exc:
        raise AdmissionFailure(path, exc.type) from None
    if text not in allowed:
        reject(path, "INVALID_FORMAT")
    return text


def canonical_set(value: object, path: str, capacity: int, length: int) -> list[str]:
    if not isinstance(value, list):
        reject(path, "INVALID_TYPE")
    items = cast(list[object], value)
    if not 1 <= len(items) <= 1000:
        reject(path, "OUT_OF_RANGE")
    canonical: set[str] = set()
    for index, item in enumerate(items):
        location = f"{path}[{index}]"
        try:
            text = (
                enum_value(item, RECRUITMENT, location) if length == 0 else text_value(item, length)
            )
        except PydanticCustomError as exc:
            raise AdmissionFailure(location, exc.type) from None
        canonical.add(text)
    if len(canonical) > capacity:
        reject(path, "OUT_OF_RANGE")
    return [x for x in RECRUITMENT if x in canonical] if length == 0 else sorted(canonical)


def salary_value(value: object, path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, Decimal)):
        reject(path, "INVALID_TYPE")
    assert isinstance(value, (int, Decimal))
    if isinstance(value, Decimal) and (not value.is_finite() or value != value.to_integral_value()):
        reject(path, "INVALID_TYPE")
    if not 1 <= value <= 300000:
        reject(path, "OUT_OF_RANGE")
    return int(value)


class Unlimited(DTO):
    mode: Literal["UNLIMITED"]


def text_set_schema(capacity: int, length: int) -> WithJsonSchema:
    return WithJsonSchema(
        {
            "type": "array",
            "minItems": 1,
            "maxItems": 1000,
            "items": {"type": "string", "x-post-trim-maxLength": length},
            "x-canonical-maxItems": capacity,
            "description": "PRF-003/004/016: validate every raw item; fixed trim, exact dedup, "
            "Unicode code-point sort; no controls, blank or non-scalar text.",
        },
        mode="validation",
    )


Keywords = Annotated[
    list[Annotated[str, Field(min_length=1, max_length=100)]],
    Field(min_length=1, max_length=20),
    text_set_schema(20, 100),
]
Cities = Annotated[
    list[Annotated[str, Field(min_length=1, max_length=100)]],
    Field(min_length=1, max_length=50),
    text_set_schema(50, 100),
]
Companies = Annotated[
    list[Annotated[str, Field(min_length=1, max_length=200)]],
    Field(min_length=1, max_length=200),
    text_set_schema(200, 200),
]
Recruitments = Annotated[
    list[Recruitment],
    Field(min_length=1, max_length=4),
    WithJsonSchema(
        {
            "type": "array",
            "minItems": 1,
            "maxItems": 1000,
            "items": {"type": "string", "enum": list(RECRUITMENT)},
            "x-canonical-maxItems": 4,
        },
        mode="validation",
    ),
]


class CityLimited(DTO):
    mode: Literal["LIMITED"]
    value: Cities


class CompanyLimited(DTO):
    mode: Literal["LIMITED"]
    value: Companies


class SalaryLimited(DTO):
    mode: Literal["LIMITED"]
    value: int = Field(ge=1, le=300000)


class RecruitmentLimited(DTO):
    mode: Literal["LIMITED"]
    value: Recruitments


class EducationLimited(DTO):
    mode: Literal["LIMITED"]
    value: Education


class Configuration(DTO):
    target_job_keywords: Keywords
    accepted_cities: Annotated[Unlimited | CityLimited, Field(discriminator="mode")]
    minimum_salary: Annotated[Unlimited | SalaryLimited, Field(discriminator="mode")]
    recruitment_types: Annotated[Unlimited | RecruitmentLimited, Field(discriminator="mode")]
    excluded_companies: Annotated[Unlimited | CompanyLimited, Field(discriminator="mode")]
    max_required_education: Annotated[Unlimited | EducationLimited, Field(discriminator="mode")]

    @model_validator(mode="before")
    @classmethod
    def canonicalize(cls, value: object) -> object:
        if isinstance(value, cls):
            value = value.model_dump()
        fields = object_fields(value, set(cls.model_fields), "configuration")
        result: dict[str, object] = {
            "target_job_keywords": canonical_set(
                fields["target_job_keywords"], "configuration.target_job_keywords", 20, 100
            )
        }
        for name in cls.model_fields:
            if name == "target_job_keywords":
                continue
            path = "configuration." + name
            choice = fields[name]
            if not isinstance(choice, dict):
                reject(path, "INVALID_TYPE")
            choice = cast(dict[str, object], choice)
            if choice.keys() - {"mode", "value"}:
                reject(path, "UNKNOWN_FIELD")
            if "mode" not in choice:
                reject(path + ".mode", "REQUIRED")
            mode = enum_value(choice["mode"], ("UNLIMITED", "LIMITED"), path + ".mode")
            if mode == "UNLIMITED":
                if "value" in choice:
                    reject(path, "INVALID_FORMAT")
                result[name] = {"mode": mode}
                continue
            if "value" not in choice:
                reject(path + ".value", "REQUIRED")
            raw = choice["value"]
            location = path + ".value"
            if name == "minimum_salary":
                canonical = salary_value(raw, location)
            elif name == "max_required_education":
                canonical = enum_value(raw, EDUCATION, location)
            else:
                capacity, length = {
                    "accepted_cities": (50, 100),
                    "excluded_companies": (200, 200),
                    "recruitment_types": (4, 0),
                }[name]
                canonical = canonical_set(raw, location, capacity, length)
            result[name] = {"mode": mode, "value": canonical}
        return result


class SavePreferences(DTO):
    request_id: UuidV4
    revision: Revision | None
    configuration: Configuration


class PreferenceSet(DTO):
    preference_set_id: UuidV4
    current_preference_set_version_id: UuidV4
    revision: Revision
    created_at: UtcTimestamp
    updated_at: UtcTimestamp


class PreferenceSetVersion(DTO):
    preference_set_version_id: UuidV4
    preference_set_id: UuidV4
    created_at: UtcTimestamp
    configuration: Configuration


class NotConfigured(DTO):
    status: Literal["NOT_CONFIGURED"]


class Configured(DTO):
    status: Literal["CONFIGURED"]
    preference_set: PreferenceSet
    current_preference_set_version: PreferenceSetVersion


class SaveResult(DTO):
    preference_set_id: UuidV4
    preference_set_version_id: UuidV4
    revision: Revision
    outcome: Literal["CREATED", "UPDATED", "UNCHANGED"]


def fingerprint(command: SavePreferences) -> str:
    def string(text: str) -> bytes:
        raw = text.encode("utf-8")
        return len(raw).to_bytes(4, "big") + raw

    def array(values: list[str]) -> bytes:
        return len(values).to_bytes(4, "big") + b"".join(string(v) for v in values)

    config = command.configuration
    data = b"PreferenceSetSave:v1\0"
    data += b"\0" if command.revision is None else b"\1" + string(str(command.revision))
    data += array(config.target_job_keywords)
    for choice in (
        config.accepted_cities,
        config.minimum_salary,
        config.recruitment_types,
        config.excluded_companies,
        config.max_required_education,
    ):
        if isinstance(choice, Unlimited):
            data += b"\0"
        else:
            data += b"\1"
            value = choice.value
            if isinstance(value, int):
                data += value.to_bytes(4, "big")
            elif isinstance(value, str):
                data += string(value)
            else:
                data += array(list(value))
    return hashlib.sha256(data).hexdigest()
