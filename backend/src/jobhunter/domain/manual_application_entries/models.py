"""Entry-specific content, URL admission and DTOs."""

import hashlib
import ipaddress
import re
from typing import Annotated

from pydantic import BeforeValidator, Field, WithJsonSchema
from urlstd.parse import Host, URLValidator, ValidityState

from jobhunter.domain.shared.values import (
    DTO,
    TRIM,
    Revision,
    UtcTimestamp,
    UuidV4,
    invalid,
    text_value,
)
from jobhunter.domain.shared.values import MAX_REVISION as MAX_REVISION
from jobhunter.domain.shared.values import UUID_PATTERN as UUID_PATTERN


def company(value: object) -> str:
    return text_value(value, 200)


def url_value(value: object) -> str:
    value = text_value(value, 8192)
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
