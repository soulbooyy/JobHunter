"""Bounded PRF transport admission, isolated from the original Entry boundary."""

import json
from collections.abc import Callable, Coroutine
from decimal import Decimal, DecimalException
from email.message import Message
from typing import Any, cast

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

from jobhunter.api.middleware.requests import reject_constant
from jobhunter.domain.preferences.models import AdmissionFailure
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

MAX_BODY = 1_048_576


def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate member")
        result[key] = value
    return result


def parse_json(raw: bytes) -> object:
    return json.loads(
        raw.decode("utf-8"),
        parse_float=Decimal,
        parse_int=Decimal,
        parse_constant=reject_constant,
        object_pairs_hook=unique_object,
    )


class PreferencesRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        handler = super().get_route_handler()

        async def admitted(request: Request) -> Response:
            if request.query_params:
                raise AdmissionFailure("$", "UNKNOWN_FIELD")
            if request.method == "GET":
                async for chunk in request.stream():
                    if chunk:
                        raise AdmissionFailure("$", "INVALID_TYPE")
            else:
                media = Message()
                media["content-type"] = request.headers.get("content-type", "")
                params = media.get_params() or []
                charsets = [
                    str(value).lower() for key, value in params[1:] if key.lower() == "charset"
                ]
                if (
                    len(request.headers.getlist("content-type")) != 1
                    or media.get_content_type().lower() != "application/json"
                    or any(charset != "utf-8" for charset in charsets)
                    or len(request.headers.getlist("content-encoding")) > 1
                    or request.headers.get("content-encoding", "identity").strip().lower()
                    != "identity"
                ):
                    raise Failure("BAD_REQUEST")
                body = bytearray()
                async for chunk in request.stream():
                    if len(body) + len(chunk) > MAX_BODY:
                        raise Failure("REQUEST_TOO_LARGE")
                    body.extend(chunk)
                try:
                    parsed = parse_json(bytes(body))
                except (ValueError, UnicodeError, RecursionError, DecimalException):
                    raise Failure("BAD_REQUEST") from None
                if not isinstance(parsed, dict):
                    raise AdmissionFailure("$", "INVALID_TYPE")
                request._body = bytes(body)  # pyright: ignore[reportPrivateUsage]
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
