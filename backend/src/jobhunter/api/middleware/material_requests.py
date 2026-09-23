"""Isolated finite JSON admission and pure-read transport for Materials."""

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


def members(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate member")
        result[key] = value
    return result


class MaterialRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        handler = super().get_route_handler()

        async def admitted(request: Request) -> Response:
            query = list(request.query_params.multi_items())
            if query:
                if not request.url.path.endswith("/content") or any(
                    key != "disposition" for key, _ in query
                ):
                    raise FieldFailure("$", "UNKNOWN_FIELD")
                if len(query) != 1 or query[0][1] not in ("inline", "attachment"):
                    raise FieldFailure("disposition", "INVALID_FORMAT")
            if request.method == "GET":
                async for chunk in request.stream():
                    if chunk:
                        raise FieldFailure("$", "INVALID_TYPE")
            else:
                media = Message()
                media["content-type"] = request.headers.get("content-type", "")
                if (
                    len(request.headers.getlist("content-type")) != 1
                    or media.get_content_type().lower() != "application/json"
                    or any(
                        str(value).lower() != "utf-8"
                        for key, value in (media.get_params() or [])[1:]
                        if key.lower() == "charset"
                    )
                    or len(request.headers.getlist("content-encoding")) > 1
                    or request.headers.get("content-encoding", "identity").strip().lower()
                    != "identity"
                ):
                    raise Failure("BAD_REQUEST")
                raw = bytearray()
                async for chunk in request.stream():
                    if len(raw) + len(chunk) > 4096:
                        raise Failure("REQUEST_TOO_LARGE")
                    raw.extend(chunk)
                try:
                    parsed: object = json.loads(
                        bytes(raw).decode("utf-8"),
                        parse_int=Decimal,
                        parse_float=Decimal,
                        parse_constant=reject_constant,
                        object_pairs_hook=members,
                    )
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
