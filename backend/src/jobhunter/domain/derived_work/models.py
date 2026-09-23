"""Exact demand, captured execution constraints and fenced state invariants."""

import hashlib
from typing import Literal, Self

from pydantic import model_validator

from jobhunter.domain.materials.models import Nonnegative, Positive
from jobhunter.domain.shared.canonical import encode
from jobhunter.domain.shared.values import DTO, UtcTimestamp, UuidV4, invalid

FailureCode = Literal[
    "SOURCE_UNAVAILABLE",
    "CONFIGURATION_UNAVAILABLE",
    "PERMISSION_DENIED",
    "RENDER_FAILED",
    "OUTPUT_INVALID",
    "RESOURCE_LIMIT_EXCEEDED",
    "STORAGE_FAILED",
    "RECOVERY_EXHAUSTED",
    "INTERNAL_ERROR",
]


class RenderRequest(DTO):
    request_id: UuidV4
    resume_version_id: UuidV4
    render_configuration_id: UuidV4


class Accepted(DTO):
    request_id: UuidV4
    outcome: Literal["ACCEPTED"]
    render_intent_id: UuidV4


class RenderIntent(DTO):
    render_intent_id: UuidV4
    resume_version_id: UuidV4
    render_configuration_id: UuidV4
    status: Literal["PENDING", "FULFILLED", "FAILED"]
    created_at: UtcTimestamp
    finished_at: UtcTimestamp | None
    artifact_id: UuidV4 | None
    failure_code: FailureCode | None

    @model_validator(mode="after")
    def state(self) -> Self:
        if (
            (self.finished_at is not None) != (self.status != "PENDING")
            or (self.artifact_id is not None) != (self.status == "FULFILLED")
            or (self.failure_code is not None) != (self.status == "FAILED")
        ):
            invalid("INVALID_FORMAT")
        return self


class Limits(DTO):
    max_attempts: Positive
    max_pages: Positive
    max_png_pixels: Positive
    max_output_bytes: Positive
    timeout_ms: Positive


class Work(Limits):
    work_id: UuidV4
    resume_version_id: UuidV4
    render_configuration_id: UuidV4
    status: Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED"]
    attempt_count: Nonnegative
    current_attempt_id: UuidV4 | None
    created_at: UtcTimestamp
    finished_at: UtcTimestamp | None
    artifact_id: UuidV4 | None
    failure_code: FailureCode | None

    @model_validator(mode="after")
    def state(self) -> Self:
        if (
            (self.finished_at is not None) != (self.status in ("SUCCEEDED", "FAILED"))
            or (self.current_attempt_id is not None) != (self.status == "RUNNING")
            or (self.artifact_id is not None) != (self.status == "SUCCEEDED")
            or (self.failure_code is not None) != (self.status == "FAILED")
            or self.attempt_count > self.max_attempts
            or (self.status in ("RUNNING", "SUCCEEDED") and self.attempt_count == 0)
        ):
            invalid("INVALID_FORMAT")
        return self


def fingerprint(command: RenderRequest) -> str:
    body = command.model_dump(exclude={"request_id"})
    return hashlib.sha256(
        b"JobHunter:SL02:Materials:1\n" + encode(["RENDER_REQUEST", None, body])
    ).hexdigest()
