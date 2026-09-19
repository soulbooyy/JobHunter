"""Compose the local API and its application dependencies."""

from fastapi import FastAPI

from jobhunter.api.errors.handlers import install_error_handlers
from jobhunter.api.middleware.access import install_access
from jobhunter.api.middleware.requests import ExactJsonRoute
from jobhunter.api.v1.manual_application_entries.routes import register_routes
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def create_app(
    store: Store,
    *,
    hosts: tuple[str, ...] = ("testserver",),
    origins: tuple[str, ...] = (),
) -> FastAPI:
    app = FastAPI(
        title="JobHunter Local M1",
        version="2026-09-19.M1-r1",
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
    return app
