"""Enforce configured local Host and browser Origin admission."""

from collections.abc import Awaitable, Callable

from fastapi import FastAPI, Request, Response
from starlette.responses import JSONResponse

from jobhunter.domain.shared.errors import Failure


def install_access(app: FastAPI, hosts: tuple[str, ...], origins: tuple[str, ...]) -> None:
    @app.middleware("http")
    async def access(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        host_values = request.headers.getlist("host")
        origin_values = request.headers.getlist("origin")
        if (
            len(host_values) != 1
            or host_values[0] not in hosts
            or (origin_values and (len(origin_values) != 1 or origin_values[0] not in origins))
        ):
            return JSONResponse(Failure("ACCESS_DENIED").body(), status_code=403)
        if request.method == "OPTIONS" and origin_values:
            if request.headers.get("access-control-request-method") not in (
                "GET",
                "POST",
                "PUT",
            ) or any(
                h.strip().lower() != "content-type"
                for h in request.headers.get("access-control-request-headers", "").split(",")
                if h.strip()
            ):
                return JSONResponse(Failure("ACCESS_DENIED").body(), status_code=403)
            response = Response(status_code=204)
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        else:
            response = await call_next(request)
        if origin_values:
            response.headers["Access-Control-Allow-Origin"] = origin_values[0]
            response.headers["Vary"] = "Origin"
        return response
