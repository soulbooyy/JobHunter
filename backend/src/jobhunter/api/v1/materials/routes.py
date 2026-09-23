"""Six public operations; no Work, retry or configuration mutation API."""

from collections.abc import Iterator
from typing import Annotated, Any, Literal

from fastapi import APIRouter, FastAPI, Path, Query
from fastapi.responses import StreamingResponse
from starlette.background import BackgroundTask

from jobhunter.api.middleware.material_requests import MaterialRoute
from jobhunter.api.schemas.errors import ContractError
from jobhunter.application.materials.service import Materials
from jobhunter.domain.derived_work.models import Accepted, RenderIntent, RenderRequest
from jobhunter.domain.materials.models import Artifact, ConfigurationAvailability, ConfigurationList
from jobhunter.domain.shared.values import UUID_PATTERN
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json

Identity = Annotated[str, Path(pattern=UUID_PATTERN)]


def register_routes(app: FastAPI, service: Materials) -> None:
    errors: dict[int | str, dict[str, Any]] = {
        status: {"model": ContractError} for status in (400, 403, 422, 500, 503)
    }
    router = APIRouter(
        prefix="/api/v1", route_class=MaterialRoute, responses=errors, tags=["Materials"]
    )

    @router.post(
        "/render-intents",
        response_model=Accepted,
        responses={409: {"model": ContractError}, 413: {"model": ContractError}},
        openapi_extra={"x-max-body-bytes": 4096},
        description="Exact saved target; closed UTF-8 JSON, identity encoding, no query. "
        "Replay the identical request after uncertainty, then poll its original Intent.",
    )
    def request(command: RenderRequest) -> Json:
        return service.request(command)

    @router.get(
        "/render-intents/{render_intent_id}",
        response_model=RenderIntent,
        responses={404: {"model": ContractError}},
    )
    def intent(render_intent_id: Identity) -> Json:
        return service.intent(render_intent_id)

    @router.get("/render-configurations", response_model=ConfigurationList)
    def configurations() -> Json:
        return service.configurations()

    @router.get(
        "/render-configurations/{render_configuration_id}",
        response_model=ConfigurationAvailability,
        responses={404: {"model": ContractError}},
    )
    def configuration(render_configuration_id: Identity) -> Json:
        return service.configuration(render_configuration_id)

    @router.get(
        "/artifacts/{artifact_id}",
        response_model=Artifact,
        responses={404: {"model": ContractError}},
    )
    def artifact(artifact_id: Identity) -> Json:
        return service.artifact(artifact_id)

    @router.get(
        "/artifacts/{artifact_id}/content",
        response_class=StreamingResponse,
        responses={
            404: {"model": ContractError},
            409: {"model": ContractError},
            200: {
                "content": {
                    "application/pdf": {"schema": {"type": "string", "format": "binary"}},
                    "image/png": {"schema": {"type": "string", "format": "binary"}},
                }
            },
        },
    )
    def content(
        artifact_id: Identity,
        disposition: Annotated[Literal["inline", "attachment"], Query()] = "inline",
    ) -> StreamingResponse:
        metadata, snapshot = service.content(artifact_id)

        def chunks() -> Iterator[bytes]:
            try:
                while chunk := snapshot.read(65536):
                    yield chunk
            finally:
                snapshot.close()

        extension = "pdf" if metadata["media_type"] == "application/pdf" else "png"
        return StreamingResponse(
            chunks(),
            media_type=metadata["media_type"],
            headers={
                "Content-Length": str(metadata["byte_length"]),
                "Cache-Control": "no-store",
                "Content-Disposition": (
                    f'{disposition}; filename="artifact-{artifact_id}.{extension}"'
                ),
            },
            background=BackgroundTask(snapshot.close),
        )

    app.include_router(router)
