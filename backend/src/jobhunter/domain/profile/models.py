"""Profile owns only exact nullable contact snapshots."""

import re
from typing import Annotated, Literal

from pydantic import BeforeValidator, Field

from jobhunter.domain.shared.candidate_values import short, short_schema
from jobhunter.domain.shared.values import (
    DTO,
    TRIM,
    Revision,
    UtcTimestamp,
    UuidV4,
    invalid,
    text_value,
)


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
