"""Shared Common scalar admission and strict DTO base."""

import re
from decimal import Decimal
from typing import Annotated, LiteralString

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from pydantic_core import PydanticCustomError

TRIM = (
    "\u0009\u000a\u000b\u000c\u000d\u0020\u0085\u00a0\u1680"
    + "".join(chr(i) for i in range(0x2000, 0x200B))
    + "\u2028\u2029\u202f\u205f\u3000"
)
UUID_PATTERN = r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
MAX_REVISION = 9007199254740991


def invalid(code: LiteralString) -> None:
    raise PydanticCustomError(code, "Invalid field.")


def scalar(value: object) -> str:
    if not isinstance(value, str):
        invalid("INVALID_TYPE")
    assert isinstance(value, str)
    if any(0xD800 <= ord(c) <= 0xDFFF for c in value):
        invalid("INVALID_CHARACTERS")
    return value


def uuid_value(value: object) -> str:
    value = scalar(value)
    if not re.fullmatch(UUID_PATTERN, value):
        invalid("INVALID_FORMAT")
    return value


def text_value(value: object, limit: int) -> str:
    value = scalar(value).strip(TRIM)
    if not value:
        invalid("BLANK_VALUE")
    if len(value) > limit:
        invalid("TOO_LONG")
    if any(ord(c) < 32 or 127 <= ord(c) <= 159 or c in "\u2028\u2029" for c in value):
        invalid("INVALID_CHARACTERS")
    return value


def revision_value(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, Decimal)):
        invalid("INVALID_TYPE")
    assert isinstance(value, (int, Decimal))
    if isinstance(value, Decimal) and (not value.is_finite() or value != value.to_integral_value()):
        invalid("INVALID_TYPE")
    if not 1 <= value <= MAX_REVISION:
        invalid("OUT_OF_RANGE")
    return int(value)


UuidV4 = Annotated[str, Field(pattern=UUID_PATTERN), BeforeValidator(uuid_value)]
Revision = Annotated[int, Field(ge=1, le=MAX_REVISION), BeforeValidator(revision_value)]
UtcTimestamp = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")]


class DTO(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
