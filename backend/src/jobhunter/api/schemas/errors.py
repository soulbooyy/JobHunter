from typing import Literal

from pydantic import Field

from jobhunter.domain.shared.values import DTO

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
    "REQUEST_TOO_LARGE",
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
    field: str = Field(
        pattern=r"^(\$|[a-z][a-z0-9_]*(\[(0|[1-9][0-9]*)\])?(\.[a-z][a-z0-9_]*(\[(0|[1-9][0-9]*)\])?)*)$",
        description="COM-029/034: known fields only; M2 paths use original array indices.",
    )
    code: FieldCode


class ContractError(DTO):
    code: ErrorCode
    message: str = Field(min_length=1)
    field_errors: list[FieldError]
