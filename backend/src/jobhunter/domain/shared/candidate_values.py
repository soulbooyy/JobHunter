"""Shared scalar and error admission for the saved-authority consumer."""

import re
from collections.abc import Callable
from decimal import Decimal
from typing import Annotated, cast

from pydantic import BaseModel, BeforeValidator, Field, ValidationError, WithJsonSchema

from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import TRIM, invalid, scalar, text_value


class FieldFailure(Failure):
    def __init__(self, field: str, code: str) -> None:
        super().__init__("VALIDATION_ERROR")
        self.field = field
        self.field_code = code

    def body(self) -> dict[str, object]:
        return {**super().body(), "field_errors": [{"field": self.field, "code": self.field_code}]}


def short(limit: int) -> Callable[[object], str]:
    return lambda value: text_value(value, limit)


def short_schema(limit: int) -> WithJsonSchema:
    return WithJsonSchema(
        {
            "type": "string",
            "x-post-trim-maxLength": limit,
            "description": "Common fixed outer trim; nonblank scalar single-line text.",
        },
        mode="validation",
    )


ShortText = Annotated[
    str, Field(min_length=1, max_length=200), BeforeValidator(short(200)), short_schema(200)
]


def no_controls(value: object) -> str:
    value = scalar(value)
    if any(ord(c) < 32 or 127 <= ord(c) <= 159 or c in "\u2028\u2029" for c in value):
        invalid("INVALID_CHARACTERS")
    return value


def month(value: object) -> str:
    value = scalar(value)
    if not re.fullmatch(r"(?!0000)[0-9]{4}-(0[1-9]|1[0-2])", value):
        invalid("INVALID_FORMAT")
    return value


Month = Annotated[str, Field(pattern=r"^[0-9]{4}-(0[1-9]|1[0-2])$"), BeforeValidator(month)]


def half_number(value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, Decimal, float)):
        invalid("INVALID_TYPE")
    # HTTP numbers are Decimal. Stored DTO floats here are exact half-integers.
    number = Decimal(str(value))
    if (
        not number.is_finite()
        or not 0 <= number <= 30
        or number not in {Decimal(i) / 2 for i in range(61)}
    ):
        invalid("OUT_OF_RANGE")
    return float(number)


def error_field(error: dict[str, object], prefix: str = "") -> FieldFailure:
    # Pydantic union labels are implementation detail, never client field names.
    known = {
        "request_id",
        "revision",
        "full_name",
        "phone_number",
        "email",
        "kind",
        "fields",
        "content",
        "type",
        "text",
        "items",
        "runs",
        "marks",
        "url",
        "school_name",
        "degree",
        "major",
        "start_month",
        "end_month",
        "company_name",
        "role_title",
        "project_name",
        "project_url",
        "skill_name",
        "award_name",
        "awarding_organization",
        "awarded_month",
        "certification_name",
        "issuing_organization",
        "issued_month",
        "resume_name",
        "profile_version_id",
        "header_presentation",
        "optional_items",
        "value",
        "sections",
        "members",
        "evidence_item_id",
        "evidence_item_version_id",
        "document_presentation",
        "font_family",
        "font_size_pt",
        "line_spacing_pt",
        "theme_color",
        "default_resume_id",
        "replacement_resume_id",
        "default_resume_selection",
        "resume_id",
        "resume_version_id",
        "evidence_baseline_snapshot_id",
    }
    kind = str(error["type"])
    code = {
        "missing": "REQUIRED",
        "extra_forbidden": "UNKNOWN_FIELD",
        "literal_error": "INVALID_FORMAT",
        "union_tag_invalid": "INVALID_FORMAT",
        "union_tag_not_found": "REQUIRED",
        "string_pattern_mismatch": "INVALID_FORMAT",
        "too_long": "OUT_OF_RANGE",
        "too_short": "OUT_OF_RANGE",
        "greater_than_equal": "OUT_OF_RANGE",
        "less_than_equal": "OUT_OF_RANGE",
        "multiple_of": "OUT_OF_RANGE",
    }.get(kind, kind if kind.isupper() else "INVALID_TYPE")
    if kind in ("union_tag_invalid", "union_tag_not_found"):
        supplied = error.get("input")
        if isinstance(supplied, dict) and "type" in supplied:
            tag = cast(dict[str, object], supplied)["type"]
            if not isinstance(tag, str):
                code = "INVALID_TYPE"
            elif any(0xD800 <= ord(c) <= 0xDFFF for c in tag):
                code = "INVALID_CHARACTERS"
    loc = error.get("loc", ())
    assert isinstance(loc, (tuple, list))
    path = prefix
    loc = cast(tuple[object, ...] | list[object], loc)
    for part in loc[:-1] if code == "UNKNOWN_FIELD" else loc:
        if isinstance(part, int):
            path += f"[{part}]"
        elif part in known:
            path += ("." if path else "") + str(part)
    if kind in ("union_tag_invalid", "union_tag_not_found"):
        path += ("." if path else "") + "type"
    return FieldFailure(path or "$", code)


def admit[T: BaseModel](model: type[T], data: object, prefix: str = "") -> T:
    try:
        return model.model_validate(data)
    except ValidationError as exc:
        raise error_field(dict(exc.errors()[0]), prefix) from None


def nonblank(value: str) -> None:
    if not value.strip(TRIM):
        invalid("BLANK_VALUE")
