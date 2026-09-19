"""Three Preferences operations and their owned schema/error boundary."""

from typing import Annotated, Any

from fastapi import APIRouter, FastAPI, Path

from jobhunter.api.middleware.preferences_requests import PreferencesRoute
from jobhunter.api.schemas.errors import ContractError
from jobhunter.application.candidate.preferences import Preferences
from jobhunter.domain.preferences.models import (
    Configured,
    NotConfigured,
    PreferenceSetVersion,
    SavePreferences,
    SaveResult,
)
from jobhunter.domain.shared.values import UUID_PATTERN

BASE = "/api/v1/preferences"


def register_routes(app: FastAPI, preferences: Preferences) -> None:
    router = APIRouter(route_class=PreferencesRoute)
    errors: dict[int | str, dict[str, Any]] = {
        status: {"model": ContractError} for status in (400, 403, 404, 409, 413, 422, 500, 503)
    }

    @router.post(
        BASE + "/save",
        response_model=SaveResult,
        responses={k: v for k, v in errors.items() if k != 404},
        description=(
            "PRF-012–023: complete canonical Save; null revision requires absence. "
            "1 MiB UTF-8 JSON; duplicate members forbidden; max 1000 raw items per array. "
            "Retry preserves the original request and never resets current. "
            "Integer-valued numbers admit decimal/exponent spellings without rounding."
        ),
    )
    def save(command: SavePreferences) -> SaveResult:
        return preferences.save(command)

    @router.get(
        BASE,
        response_model=Configured | NotConfigured,
        responses={k: v for k, v in errors.items() if k not in (404, 409, 413)},
    )
    def current() -> Configured | NotConfigured:
        return preferences.current()

    @router.get(
        BASE + "/versions/{preference_set_version_id}",
        response_model=PreferenceSetVersion,
        responses={k: v for k, v in errors.items() if k not in (409, 413)},
    )
    def version(
        preference_set_version_id: Annotated[str, Path(pattern=UUID_PATTERN)],
    ) -> PreferenceSetVersion:
        return preferences.version(preference_set_version_id)

    app.include_router(router)
