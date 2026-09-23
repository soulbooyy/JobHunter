"""Closed execution projections; no business lifecycle or transport envelope."""

import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Annotated, Literal, Self

from jobhunter.domain.shared.values import DTO, MAX_REVISION, UuidV4, scalar
from pydantic import BeforeValidator, ConfigDict, Field, model_validator


def integer(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, Decimal)):
        raise ValueError("Invalid integer")
    if isinstance(value, Decimal) and (not value.is_finite() or value != value.to_integral_value()):
        raise ValueError("Invalid integer")
    return int(value)


def instant(value: object) -> str:
    value = scalar(value)
    if (
        re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z", value)
        is None
    ):
        raise ValueError("Invalid instant")
    parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    if len(value) != 24 or parsed.microsecond % 1000:
        raise ValueError("Invalid instant")
    return value


def key(value: object) -> str:
    value = scalar(value)
    if not value:
        raise ValueError("Empty key")
    return value


Generation = Annotated[int, Field(ge=0, le=MAX_REVISION), BeforeValidator(integer)]
Positive = Annotated[int, Field(gt=0), BeforeValidator(integer)]
Instant = Annotated[str, BeforeValidator(instant)]
Key = Annotated[str, BeforeValidator(key)]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
EndReason = Literal["COMPLETED", "FAILED", "CANCELLED", "TIMED_OUT", "OUTCOME_UNKNOWN"]
FailureCode = Literal[
    "RESPONSE_PAYLOAD_UNAVAILABLE",
    "RESPONSE_INTEGRITY_FAILED",
    "RESPONSE_FORMAT_UNAVAILABLE",
    "RESPONSE_FORMAT_INVALID",
    "RESPONSE_TOO_LARGE",
    "CONSUMER_UNAVAILABLE",
    "CONTROLLED_PERMISSION_DENIED",
    "CONTROLLED_SOURCE_UNAVAILABLE",
    "CONTROLLED_ACTION_UNAVAILABLE",
]


class Value(DTO):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True, hide_input_in_errors=True)


class Run(Value):
    run_id: UuidV4
    consumer_key: Key
    run_status: Literal["OPEN", "ENDED"]
    execution_generation: Generation
    owner_runtime_instance_id: UuidV4 | None
    deadline_at: Instant | None
    created_at: Instant
    ended_at: Instant | None
    end_reason: EndReason | None
    failure_code: FailureCode | None

    @model_validator(mode="after")
    def consistent(self) -> Self:
        if self.run_status == "OPEN":
            if (
                self.ended_at is not None
                or self.end_reason is not None
                or self.failure_code is not None
            ):
                raise ValueError("Invalid open Run")
        elif (
            self.ended_at is None
            or self.end_reason is None
            or self.owner_runtime_instance_id is not None
        ):
            raise ValueError("Invalid ending")
        if (self.end_reason == "FAILED") != (self.failure_code is not None):
            raise ValueError("Invalid failure")
        if self.owner_runtime_instance_id is not None and self.execution_generation == 0:
            raise ValueError("Invalid authority")
        return self


class Qualification(Value):
    run_id: UuidV4
    runtime_instance_id: UuidV4
    execution_generation: Annotated[Generation, Field(gt=0)]


class Ending(Value):
    run_id: UuidV4
    execution_generation: Generation
    ended_at: Instant
    end_reason: EndReason
    failure_code: FailureCode | None


class ModelInvocation(Value):
    invocation_id: UuidV4
    run_id: UuidV4
    kind: Literal["MODEL"]
    response_format_key: Key
    max_response_bytes: Positive
    durability_phase: Literal["PREPARED", "DISPATCH_INTENT_DURABLE", "RESPONSE_DURABLE"]
    dispatch_generation: Annotated[Generation, Field(gt=0)] | None
    response_rejection_code: Literal["RESPONSE_TOO_LARGE"] | None

    @model_validator(mode="after")
    def consistent(self) -> Self:
        if (self.durability_phase == "PREPARED") != (self.dispatch_generation is None):
            raise ValueError("Invalid dispatch")
        if (
            self.response_rejection_code is not None
            and self.durability_phase != "DISPATCH_INTENT_DURABLE"
        ):
            raise ValueError("Invalid rejection")
        return self


class Publication(Value):
    invocation_id: UuidV4
    response_format_key: Key
    sha256: Digest
    byte_length: Positive


class Response(Publication):
    serialized_payload: bytes = Field(repr=False)

    def publication(self) -> Publication:
        return Publication.model_validate(self.model_dump(exclude={"serialized_payload"}))


class Descriptor(Value):
    """Controlled echo request v1. No production target, secrets or SDK objects."""

    target: Literal["controlled.echo.v1"]
    text: Annotated[str, BeforeValidator(scalar)] = Field(repr=False)
    ordinal: Annotated[int, Field(ge=0, le=MAX_REVISION), BeforeValidator(integer)]


class ModelRead(Value):
    invocation: ModelInvocation
    descriptor: Descriptor | None


class LocalRead(Value):
    """Action v1 inputs are exact response identity, never a latest pointer.

    Result is the verified exact source digest/length; lineage_id is audit-only.
    It is never dereferenced. Missing source and permission have distinct denials.
    """

    invocation_id: UuidV4
    run_id: UuidV4
    kind: Literal["TOOL"]
    action_key: Key
    source_invocation_id: UuidV4
    lineage_id: UuidV4 | None
    result_sha256: Digest | None
    result_byte_length: Positive | None

    @model_validator(mode="after")
    def consistent(self) -> Self:
        if (self.result_sha256 is None) != (self.result_byte_length is None):
            raise ValueError("Invalid read result")
        return self


@dataclass(frozen=True)
class Success[T]:
    value: T


@dataclass(frozen=True)
class Rejected:
    code: str


@dataclass(frozen=True)
class Unresolved:
    code: str
    identity: str | None = None


type Result[T] = Success[T] | Rejected | Unresolved


@dataclass(frozen=True)
class Denial:
    reason: EndReason
    failure_code: FailureCode | None


type Admission = Literal["ALLOW", "UNRESOLVED"] | Denial
type Reconciliation = Literal["COMPLETION_CONFIRMED", "RECOVERY_REQUIRED", "UNRESOLVED"]
