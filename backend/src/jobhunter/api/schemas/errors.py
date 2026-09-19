from typing import Literal

from pydantic import Field

from jobhunter.domain.manual_application_entries.models import DTO

FieldCode = Literal[
    "REQUIRED",
    "UNKNOWN_FIELD",
    "INVALID_TYPE",
    "BLANK_VALUE",
    "TOO_LONG",
    "INVALID_CHARACTERS",
    "INVALID_FORMAT",
    "OUT_OF_RANGE",
]
ErrorCode = Literal[
    "BAD_REQUEST",
    "VALIDATION_ERROR",
    "NOT_FOUND",
    "REVISION_CONFLICT",
    "REQUEST_CONFLICT",
    "ORIGINAL_ENTRY_DELETED",
    "REVISION_EXHAUSTED",
    "STORAGE_UNAVAILABLE",
    "OUTCOME_UNKNOWN",
    "INTERNAL_ERROR",
    "ACCESS_DENIED",
]


class FieldError(DTO):
    field: str
    code: FieldCode


class ContractError(DTO):
    code: ErrorCode
    message: str = Field(min_length=1)
    field_errors: list[FieldError]
