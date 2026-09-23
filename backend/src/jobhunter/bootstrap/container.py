"""Compose the local API and its application dependencies."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from jobhunter.api.errors.handlers import install_error_handlers
from jobhunter.api.middleware.access import install_access
from jobhunter.api.middleware.requests import ExactJsonRoute
from jobhunter.api.schemas.candidate import refine_candidate_schema
from jobhunter.api.v1.candidate.routes import register_routes as register_candidate
from jobhunter.api.v1.manual_application_entries.routes import register_routes
from jobhunter.api.v1.materials.routes import register_routes as register_materials
from jobhunter.api.v1.preferences.routes import register_routes as register_preferences
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.application.candidate.preferences import Preferences
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.application.materials.coordinator import Coordinator
from jobhunter.application.materials.runner import Runner
from jobhunter.application.materials.service import Materials
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials import (
    MaterialsRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
from jobhunter.infrastructure.rendering.catalog import ASSETS, capability, catalog, environment


def create_app(
    store: Store,
    *,
    hosts: tuple[str, ...] = ("testserver",),
    origins: tuple[str, ...] = (),
) -> FastAPI:
    materials = Materials(store, capability=capability)
    for configuration in catalog():
        store.run(
            lambda conn, configuration=configuration: MaterialsRepository(conn).register(
                configuration
            ),
            write=True,
        )
    runner = Runner(Coordinator(materials), ASSETS, environment)

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
        runner.start()
        try:
            yield
        finally:
            runner.close()

    app = FastAPI(
        title="JobHunter Local",
        lifespan=lifespan,
        version="2026-09-21.S2M2-r1",
        docs_url=None,
        redoc_url=None,
    )
    app.state.store = store
    entries = Entries(store)
    app.state.entries = entries
    app.router.route_class = ExactJsonRoute

    install_access(app, hosts, origins)
    install_error_handlers(app)
    register_routes(app, entries)
    preferences = Preferences(store)
    app.state.preferences = preferences
    register_preferences(app, preferences)

    candidate = CandidateAuthority(store)
    app.state.candidate = candidate
    register_candidate(app, candidate)

    app.state.materials = materials
    register_materials(app, materials)

    refine_candidate_schema(app)
    return app
