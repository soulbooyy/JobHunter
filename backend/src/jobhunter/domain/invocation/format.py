"""Controlled response v1: fixed key order, UTF-8, no ASCII escaping, integer ordinal.

JSON uses compact separators, standard JSON string escaping, exact scalar text,
no floats/NaN, no BOM/newline and no duplicate keys. STOP and LIMIT are complete
protocol terminations; LIMIT is not a transport interruption.
"""

import json
from typing import Annotated, Literal

from jobhunter.domain.invocation.models import Value, integer
from jobhunter.domain.shared.values import MAX_REVISION, scalar
from pydantic import BeforeValidator, Field

FORMAT_KEY = "controlled.response.v1"


class ControlledResponse(Value):
    terminal: Literal["STOP", "LIMIT"]
    text: Annotated[str, BeforeValidator(scalar)] = Field(repr=False)
    ordinal: Annotated[int, Field(ge=0, le=MAX_REVISION), BeforeValidator(integer)]

    def serialize(self) -> bytes:
        return json.dumps(self.model_dump(), ensure_ascii=False, separators=(",", ":")).encode(
            "utf-8"
        )


def decode(payload: bytes) -> ControlledResponse:
    result = ControlledResponse.model_validate_json(payload)
    if result.serialize() != payload:
        raise ValueError("Noncanonical response")
    return result
