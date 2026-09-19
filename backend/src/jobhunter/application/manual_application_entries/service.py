"""Short application commands; no external effects or automatic command retries."""

from collections.abc import Callable
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy.engine import Connection

from jobhunter.domain.manual_application_entries.models import (
    MAX_REVISION,
    CreateEntry,
    ManualApplicationEntry,
    ManualApplicationEntryIdentity,
    ManualApplicationEntryList,
    ManualApplicationEntryUrl,
    UpdateEntry,
    fingerprint,
)
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import ENTRY_TABLE, RECEIPT_TABLE
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class Entries:
    def __init__(
        self,
        store: Store,
        *,
        clock: Callable[[], str] = utc_now,
        new_id: Callable[[], str] = lambda: str(uuid4()),
    ) -> None:
        self.store = store
        self.clock = clock
        self.new_id = new_id

    @staticmethod
    def observe(
        conn: Connection, identity: str, revision: int | None = None
    ) -> ManualApplicationEntry:
        row = (
            conn.exec_driver_sql(
                f"SELECT * FROM {ENTRY_TABLE} WHERE manual_application_entry_id=?",
                (identity,),
            )
            .mappings()
            .first()
        )
        if row is None:
            raise Failure("NOT_FOUND")
        entry = ManualApplicationEntry.model_validate(dict(row))
        if revision is not None and entry.revision != revision:
            raise Failure("REVISION_CONFLICT")
        return entry

    def create(self, command: CreateEntry) -> ManualApplicationEntryIdentity:
        digest = fingerprint(command)

        def execute(conn: Connection) -> ManualApplicationEntryIdentity:
            receipt = (
                conn.exec_driver_sql(
                    f"SELECT * FROM {RECEIPT_TABLE} WHERE request_id=?",
                    (command.request_id,),
                )
                .mappings()
                .first()
            )
            if receipt is not None:
                if receipt["request_fingerprint"] != digest:
                    raise Failure("REQUEST_CONFLICT")
                identity = str(receipt["manual_application_entry_id"])
                try:
                    self.observe(conn, identity)
                except Failure as exc:
                    if exc.code == "NOT_FOUND":
                        raise Failure("ORIGINAL_ENTRY_DELETED") from None
                    raise
                return ManualApplicationEntryIdentity(manual_application_entry_id=identity)
            for _ in range(10):
                identity = self.new_id()
                used = conn.exec_driver_sql(
                    f"SELECT 1 FROM {RECEIPT_TABLE} WHERE manual_application_entry_id=? "
                    f"UNION ALL SELECT 1 FROM {ENTRY_TABLE} WHERE manual_application_entry_id=?",
                    (identity, identity),
                ).first()
                if used is None:
                    break
            else:
                raise Failure("INTERNAL_ERROR")
            now = self.clock()
            conn.exec_driver_sql(
                f"INSERT INTO {ENTRY_TABLE} VALUES (?, ?, ?, ?, 1, ?, ?)",
                (
                    identity,
                    command.company_name,
                    command.role_title,
                    command.application_url,
                    now,
                    now,
                ),
            )
            self.store.fault("after_entry_insert")
            conn.exec_driver_sql(
                f"INSERT INTO {RECEIPT_TABLE} VALUES (?, ?, ?)",
                (command.request_id, digest, identity),
            )
            return ManualApplicationEntryIdentity(manual_application_entry_id=identity)

        return self.store.run(execute, write=True)

    def read(self, identity: str) -> ManualApplicationEntry:
        return self.store.run(lambda conn: self.observe(conn, identity))

    def list(self) -> ManualApplicationEntryList:
        def execute(conn: Connection) -> ManualApplicationEntryList:
            rows = conn.exec_driver_sql(
                f"SELECT * FROM {ENTRY_TABLE} "
                "ORDER BY updated_at DESC, manual_application_entry_id COLLATE BINARY ASC"
            ).mappings()
            return ManualApplicationEntryList(
                items=[ManualApplicationEntry.model_validate(dict(row)) for row in rows]
            )

        return self.store.run(execute)

    def update(self, identity: str, command: UpdateEntry) -> ManualApplicationEntry:
        def execute(conn: Connection) -> ManualApplicationEntry:
            prior = self.observe(conn, identity, command.revision)
            if (prior.company_name, prior.role_title, prior.application_url) == (
                command.company_name,
                command.role_title,
                command.application_url,
            ):
                return prior
            if prior.revision == MAX_REVISION:
                raise Failure("REVISION_EXHAUSTED")
            conn.exec_driver_sql(
                f"UPDATE {ENTRY_TABLE} SET company_name=?, role_title=?, "
                "application_url=?, revision=?, updated_at=? WHERE manual_application_entry_id=?",
                (
                    command.company_name,
                    command.role_title,
                    command.application_url,
                    prior.revision + 1,
                    max(self.clock(), prior.updated_at),
                    identity,
                ),
            )
            return self.observe(conn, identity)

        return self.store.run(execute, write=True)

    def delete(self, identity: str, revision: int) -> ManualApplicationEntryIdentity:
        def execute(conn: Connection) -> ManualApplicationEntryIdentity:
            self.observe(conn, identity, revision)
            conn.exec_driver_sql(
                f"DELETE FROM {ENTRY_TABLE} WHERE manual_application_entry_id=?",
                (identity,),
            )
            return ManualApplicationEntryIdentity(manual_application_entry_id=identity)

        return self.store.run(execute, write=True)

    def resolve(self, identity: str, revision: int) -> ManualApplicationEntryUrl:
        return self.store.run(
            lambda conn: ManualApplicationEntryUrl(
                application_url=self.observe(conn, identity, revision).application_url
            )
        )
