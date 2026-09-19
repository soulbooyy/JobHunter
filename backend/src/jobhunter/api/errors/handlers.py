"""Map failures to sanitized HTTP Contract errors."""

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from jobhunter.domain.shared.errors import Failure


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(Failure)
    async def failure(request: Request, exc: Failure) -> JSONResponse:
        return JSONResponse(exc.body(), status_code=STATUS.get(exc.code, 500))

    @app.exception_handler(RequestValidationError)
    async def validation(request: Request, exc: RequestValidationError) -> JSONResponse:
        fields: list[dict[str, str]] = []
        if request.url.path.startswith("/api/v1/preferences"):
            known_preferences = {
                "request_id",
                "revision",
                "configuration",
                "preference_set_version_id",
            }
            for error in exc.errors():
                kind = error["type"]
                code = {
                    "missing": "REQUIRED",
                    "extra_forbidden": "UNKNOWN_FIELD",
                    "string_pattern_mismatch": "INVALID_FORMAT",
                }.get(kind, kind if kind.isupper() else "INVALID_TYPE")
                loc = error["loc"]
                field = (
                    str(loc[-1])
                    if len(loc) > 1 and loc[-1] in known_preferences and code != "UNKNOWN_FIELD"
                    else "$"
                )
                fields.append({"field": field, "code": code})
            return JSONResponse(
                {
                    "code": "VALIDATION_ERROR",
                    "message": "Request validation failed.",
                    "field_errors": fields,
                },
                status_code=422,
            )
        known = {
            "request_id",
            "company_name",
            "role_title",
            "application_url",
            "revision",
            "manual_application_entry_id",
        }
        for error in exc.errors():
            kind = error["type"]
            code = {
                "missing": "REQUIRED",
                "extra_forbidden": "UNKNOWN_FIELD",
                "string_pattern_mismatch": "INVALID_FORMAT",
            }.get(kind, kind if kind.isupper() else "INVALID_TYPE")
            loc = error["loc"]
            field = (
                str(loc[-1])
                if len(loc) > 1 and loc[-1] in known and code != "UNKNOWN_FIELD"
                else "$"
            )
            item = {"field": field, "code": code}
            if item not in fields:
                fields.append(item)
        return JSONResponse(
            {
                "code": "VALIDATION_ERROR",
                "message": "Request validation failed.",
                "field_errors": fields,
            },
            status_code=422,
        )

    @app.exception_handler(HTTPException)
    async def transport(request: Request, exc: HTTPException) -> JSONResponse:
        return JSONResponse(Failure("BAD_REQUEST").body(), status_code=400)


STATUS = {
    "BAD_REQUEST": 400,
    "REQUEST_TOO_LARGE": 413,
    "VALIDATION_ERROR": 422,
    "NOT_FOUND": 404,
    "REVISION_CONFLICT": 409,
    "REQUEST_CONFLICT": 409,
    "ORIGINAL_ENTRY_DELETED": 409,
    "REVISION_EXHAUSTED": 409,
    "STORAGE_UNAVAILABLE": 503,
    "OUTCOME_UNKNOWN": 503,
    "INTERNAL_ERROR": 500,
    "ACCESS_DENIED": 403,
}
