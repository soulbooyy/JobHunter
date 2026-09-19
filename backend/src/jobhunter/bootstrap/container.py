"""Compose the local API and its application dependencies."""

from fastapi import FastAPI

from jobhunter.api.errors.handlers import install_error_handlers
from jobhunter.api.middleware.access import install_access
from jobhunter.api.middleware.requests import ExactJsonRoute
from jobhunter.api.v1.manual_application_entries.routes import register_routes
from jobhunter.api.v1.preferences.routes import register_routes as register_preferences
from jobhunter.application.candidate.preferences import Preferences
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def create_app(
    store: Store,
    *,
    hosts: tuple[str, ...] = ("testserver",),
    origins: tuple[str, ...] = (),
) -> FastAPI:
    app = FastAPI(
        title="JobHunter Local",
        version="2026-09-20.M2-r1",
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
    return app
