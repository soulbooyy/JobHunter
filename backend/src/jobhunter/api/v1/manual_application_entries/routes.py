"""Versioned HTTP routes for manual application entries."""

from typing import Annotated, Any

from fastapi import FastAPI, Path

from jobhunter.api.schemas.errors import ContractError
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.domain.manual_application_entries.models import (
    UUID_PATTERN,
    CreateEntry,
    ExpectedRevision,
    ManualApplicationEntry,
    ManualApplicationEntryIdentity,
    ManualApplicationEntryList,
    ManualApplicationEntryUrl,
    UpdateEntry,
)

BASE = "/api/v1/manual-application-entries"
Identity = Annotated[str, Path(pattern=UUID_PATTERN)]


def register_routes(app: FastAPI, entries: Entries) -> None:
    errors: dict[int | str, dict[str, Any]] = {
        status: {"model": ContractError} for status in (400, 403, 404, 409, 422, 500, 503)
    }

    @app.post(
        BASE,
        response_model=ManualApplicationEntryIdentity,
        responses={key: val for key, val in errors.items() if key != 404},
    )
    def create(command: CreateEntry) -> ManualApplicationEntryIdentity:
        return entries.create(command)

    @app.get(
        BASE,
        response_model=ManualApplicationEntryList,
        responses={key: val for key, val in errors.items() if key not in (404, 409)},
    )
    def list_entries() -> ManualApplicationEntryList:
        return entries.list()

    @app.get(
        BASE + "/{manual_application_entry_id}",
        response_model=ManualApplicationEntry,
        responses={key: val for key, val in errors.items() if key != 409},
    )
    def read(manual_application_entry_id: Identity) -> ManualApplicationEntry:
        return entries.read(manual_application_entry_id)

    @app.put(
        BASE + "/{manual_application_entry_id}",
        response_model=ManualApplicationEntry,
        responses=errors,
    )
    def update(
        manual_application_entry_id: Identity, command: UpdateEntry
    ) -> ManualApplicationEntry:
        return entries.update(manual_application_entry_id, command)

    @app.post(
        BASE + "/{manual_application_entry_id}/delete",
        response_model=ManualApplicationEntryIdentity,
        responses=errors,
    )
    def delete(
        manual_application_entry_id: Identity, command: ExpectedRevision
    ) -> ManualApplicationEntryIdentity:
        return entries.delete(manual_application_entry_id, command.revision)

    @app.post(
        BASE + "/{manual_application_entry_id}/resolve-url",
        response_model=ManualApplicationEntryUrl,
        responses=errors,
    )
    def resolve(
        manual_application_entry_id: Identity, command: ExpectedRevision
    ) -> ManualApplicationEntryUrl:
        return entries.resolve(manual_application_entry_id, command.revision)
