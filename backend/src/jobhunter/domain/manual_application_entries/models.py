"""M1 admission and DTOs; normative owners remain docs/contracts."""

import hashlib
import ipaddress
import re
from decimal import Decimal
from typing import Annotated, LiteralString

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field, WithJsonSchema
from pydantic_core import PydanticCustomError
from urlstd.parse import Host, URLValidator, ValidityState

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


def text_value(value: object, limit: int, url: bool = False) -> str:
    value = scalar(value).strip(TRIM)
    if not value:
        invalid("BLANK_VALUE")
    if len(value) > limit:
        invalid("TOO_LONG")
    if any(ord(c) < 32 or 127 <= ord(c) <= 159 or c in "\u2028\u2029" for c in value):
        invalid("INVALID_CHARACTERS")
    if url:
        if any(c in TRIM or c == "\\" for c in value):
            invalid("INVALID_CHARACTERS")
        match = re.match(r"https?://([^/?#]+)", value, re.IGNORECASE)
        if not match or "@" in match[1] or re.search(r"%(?![0-9a-fA-F]{2})", value):
            invalid("INVALID_FORMAT")
        assert match
        authority = match[1]
        port = authority.rsplit("]", 1)[-1] if authority.startswith("[") else authority
        if ":" in port and not re.fullmatch(r".*:[0-9]+", port):
            invalid("INVALID_FORMAT")
        validation_url = value
        if ":" in port:
            digits = port.rsplit(":", 1)[1].lstrip("0") or "0"
            if len(digits) > 5 or int(digits) > 65535:
                invalid("INVALID_FORMAT")
            # Avoid the parser's Python int digit limit for valid zero-padded ports.
            # This temporary parser input never replaces saved authority.
            authority_end = match.end(1)
            colon = value.rfind(":", 0, authority_end)
            validation_url = value[: colon + 1] + digits + value[authority_end:]
        if not URLValidator.is_valid(validation_url, validity=ValidityState(disable_logging=True)):
            invalid("INVALID_FORMAT")
        host = (
            authority.split("]", 1)[0] + "]"
            if authority.startswith("[")
            else authority.split(":", 1)[0]
        )
        if isinstance(Host.parse(host, validity=ValidityState(disable_logging=True)), int):
            try:
                ipaddress.IPv4Address(host)
            except ipaddress.AddressValueError:
                invalid("INVALID_FORMAT")
    return value


def company(value: object) -> str:
    return text_value(value, 200)


def url_value(value: object) -> str:
    return text_value(value, 8192, True)


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
CompanyText = Annotated[
    str,
    Field(min_length=1, max_length=200),
    BeforeValidator(company),
    WithJsonSchema(
        {
            "type": "string",
            "description": (
                "COM-025/026, MAE-003: scalar text, fixed outer trim; "
                "admitted length 1–200; no controls or line separators."
            ),
            "x-post-trim-maxLength": 200,
        },
        mode="validation",
    ),
]
ApplicationUrl = Annotated[
    str,
    Field(
        min_length=1,
        max_length=8192,
        description=(
            "MAE-004: unnormalized valid absolute HTTP(S) URL; no credentials or validation errors."
        ),
    ),
    BeforeValidator(url_value),
    WithJsonSchema(
        {
            "type": "string",
            "description": (
                "COM-025/026, MAE-004: fixed outer trim; admitted length 1–8192; "
                "HTTP(S), valid host, no credentials, parser validation errors, "
                "controls, whitespace or backslash; spelling preserved."
            ),
            "x-post-trim-maxLength": 8192,
        },
        mode="validation",
    ),
]
Revision = Annotated[int, Field(ge=1, le=MAX_REVISION), BeforeValidator(revision_value)]
UtcTimestamp = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")]


class DTO(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class EntryContent(DTO):
    company_name: CompanyText
    role_title: CompanyText
    application_url: ApplicationUrl


class CreateEntry(EntryContent):
    request_id: UuidV4


class ExpectedRevision(DTO):
    revision: Revision


class UpdateEntry(EntryContent, ExpectedRevision):
    pass


class ManualApplicationEntry(EntryContent, ExpectedRevision):
    manual_application_entry_id: UuidV4
    created_at: UtcTimestamp
    updated_at: UtcTimestamp


class ManualApplicationEntryIdentity(DTO):
    manual_application_entry_id: UuidV4


class ManualApplicationEntryList(DTO):
    items: list[ManualApplicationEntry]


class ManualApplicationEntryUrl(DTO):
    application_url: ApplicationUrl


def fingerprint(content: EntryContent) -> str:
    data = b"ManualApplicationEntryCreate:v1\x00"
    for value in (content.company_name, content.role_title, content.application_url):
        raw = value.encode("utf-8")
        data += len(raw).to_bytes(4, "big") + raw
    return hashlib.sha256(data).hexdigest()
