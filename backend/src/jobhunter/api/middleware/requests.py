"""Admit exact JSON and preserve command outcome uncertainty."""

import json
from collections.abc import Callable, Coroutine
from decimal import Decimal, DecimalException
from typing import Any, cast

from fastapi import Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from starlette.responses import JSONResponse

from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def reject_constant(value: str) -> object:
    raise ValueError("Invalid JSON constant")


class ExactJsonRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        handler = super().get_route_handler()

        async def exact(request: Request) -> Response:
            if request.query_params:
                return JSONResponse(
                    {
                        "code": "VALIDATION_ERROR",
                        "message": "Query options are not accepted.",
                        "field_errors": [{"field": "$", "code": "UNKNOWN_FIELD"}],
                    },
                    status_code=422,
                )
            raw = await request.body()
            if request.method == "GET":
                if raw:
                    raise Failure("BAD_REQUEST")
            else:
                if (
                    request.headers.get("content-type", "").split(";")[0].strip().lower()
                    != "application/json"
                ):
                    raise Failure("BAD_REQUEST")
                try:
                    # FastAPI calls Request.json(); prepopulate its cache with exact numbers.
                    parsed = json.loads(
                        raw.decode("utf-8"),
                        parse_float=Decimal,
                        parse_int=Decimal,
                        parse_constant=reject_constant,
                    )
                    if not isinstance(parsed, dict):
                        return JSONResponse(
                            {
                                "code": "VALIDATION_ERROR",
                                "message": "Expected a JSON object.",
                                "field_errors": [{"field": "$", "code": "INVALID_TYPE"}],
                            },
                            status_code=422,
                        )
                    request._json = parsed  # pyright: ignore[reportPrivateUsage]
                except (ValueError, UnicodeError, RecursionError, DecimalException):
                    raise Failure("BAD_REQUEST") from None
            try:
                response = await handler(request)
                if request.method != "GET" and not request.url.path.endswith("/resolve-url"):
                    store = cast(Store, request.app.state.store)
                    store.fault("response_after_commit")
                return response
            except (Failure, RequestValidationError):
                raise
            except Exception:
                raise Failure(
                    "OUTCOME_UNKNOWN" if request.method != "GET" else "INTERNAL_ERROR"
                ) from None

        return exact
