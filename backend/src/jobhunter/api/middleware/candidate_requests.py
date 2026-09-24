"""Stream byte bounds and parse-time JSON depth/node admission for SAV-013."""

import json
from collections.abc import Callable, Coroutine
from decimal import Decimal, DecimalException
from email.message import Message
from typing import Any, cast

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from jobhunter.api.middleware.requests import reject_constant
from jobhunter.domain.shared.candidate_values import FieldFailure
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


class BoundedJson:
    def __init__(self, raw: bytes) -> None:
        self.text = raw.decode("utf-8")
        self.index = 0
        self.nodes = 0
        self.decoder = json.JSONDecoder(
            parse_int=Decimal, parse_float=Decimal, parse_constant=reject_constant
        )

    def space(self) -> None:
        while self.index < len(self.text) and self.text[self.index] in " \t\r\n":
            self.index += 1

    def take(self, token: str) -> bool:
        self.space()
        if self.text.startswith(token, self.index):
            self.index += len(token)
            return True
        return False

    def value(self, depth: int = 0) -> object:
        self.space()
        self.nodes += 1
        if self.nodes > 100000:
            raise FieldFailure("$", "STRUCTURE_TOO_COMPLEX")
        if self.index >= len(self.text):
            raise ValueError("Incomplete JSON")
        token = self.text[self.index]
        if token in "[{":
            depth += 1
            if depth > 32:
                raise FieldFailure("$", "STRUCTURE_TOO_COMPLEX")
            self.index += 1
            if token == "[":
                values: list[object] = []
                if self.take("]"):
                    return values
                while True:
                    values.append(self.value(depth))
                    if self.take("]"):
                        return values
                    if not self.take(","):
                        raise ValueError("Invalid array")
            result: dict[str, object] = {}
            if self.take("}"):
                return result
            while True:
                self.space()
                if not self.text.startswith('"', self.index):
                    raise ValueError("Invalid key")
                key, self.index = self.decoder.raw_decode(self.text, self.index)
                if key in result or not self.take(":"):
                    raise ValueError("Duplicate or invalid member")
                result[key] = self.value(depth)
                if self.take("}"):
                    return result
                if not self.take(","):
                    raise ValueError("Invalid object")
        value, self.index = self.decoder.raw_decode(self.text, self.index)
        return value

    def parse(self) -> object:
        value = self.value()
        self.space()
        if self.index != len(self.text):
            raise ValueError("Trailing data")
        return value


class CandidateRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        handler = super().get_route_handler()

        async def admitted(request: Request) -> Response:
            if request.query_params:
                raise FieldFailure("$", "UNKNOWN_FIELD")
            if request.method == "GET":
                async for chunk in request.stream():
                    if chunk:
                        raise FieldFailure("$", "INVALID_TYPE")
            else:
                media = Message()
                media["content-type"] = request.headers.get("content-type", "")
                params = media.get_params() or []
                if (
                    len(request.headers.getlist("content-type")) != 1
                    or media.get_content_type().lower() != "application/json"
                    or any(
                        str(v).lower() != "utf-8" for k, v in params[1:] if k.lower() == "charset"
                    )
                    or len(request.headers.getlist("content-encoding")) > 1
                    or request.headers.get("content-encoding", "identity").strip().lower()
                    != "identity"
                ):
                    raise Failure("BAD_REQUEST")
                path = request.url.path
                limit = (
                    8_388_608
                    if path == "/api/v1/resumes"
                    or (path.startswith("/api/v1/resumes/") and path.endswith("/save"))
                    else 65_536
                )
                raw = bytearray()
                async for chunk in request.stream():
                    if len(raw) + len(chunk) > limit:
                        raise Failure("REQUEST_TOO_LARGE")
                    raw.extend(chunk)
                try:
                    parsed = BoundedJson(bytes(raw)).parse()
                except (ValueError, UnicodeError, DecimalException, RecursionError):
                    raise Failure("BAD_REQUEST") from None
                if not isinstance(parsed, dict):
                    raise FieldFailure("$", "INVALID_TYPE")
                request._body = bytes(raw)  # pyright: ignore[reportPrivateUsage]
                request._json = parsed  # pyright: ignore[reportPrivateUsage]
            try:
                response = await handler(request)
                if request.method == "POST":
                    try:
                        cast(Store, request.app.state.store).fault("response_after_commit")
                    except Exception:
                        raise Failure("OUTCOME_UNKNOWN") from None
                return response
            except (Failure, RequestValidationError):
                raise
            except Exception:
                raise Failure(
                    "OUTCOME_UNKNOWN" if request.method == "POST" else "INTERNAL_ERROR"
                ) from None

        return admitted
