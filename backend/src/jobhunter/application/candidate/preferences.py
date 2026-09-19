"""Atomic configuration publication; no collection or external effects."""

from collections.abc import Callable
from uuid import uuid4

from sqlalchemy.engine import Connection

from jobhunter.application.manual_application_entries.service import utc_now
from jobhunter.domain.preferences.models import (
    Configured,
    NotConfigured,
    PreferenceSet,
    PreferenceSetVersion,
    SavePreferences,
    SaveResult,
    fingerprint,
)
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.preferences import (
    PreferenceRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


class Preferences:
    def __init__(self, store: Store, *, clock: Callable[[], str] = utc_now) -> None:
        self.store = store
        self.clock = clock

    def current(self) -> Configured | NotConfigured:
        def read(conn: Connection) -> Configured | NotConfigured:
            current = PreferenceRepository(conn).current()
            if current is None:
                return NotConfigured(status="NOT_CONFIGURED")
            return Configured(
                status="CONFIGURED",
                preference_set=current[0],
                current_preference_set_version=current[1],
            )

        return self.store.run(read)

    def version(self, identity: str) -> PreferenceSetVersion:
        return self.store.run(lambda conn: PreferenceRepository(conn).version(identity))

    def save(self, command: SavePreferences) -> SaveResult:
        # Re-admit even application callers; model_construct/mutated lists cannot bypass rules.
        command = SavePreferences.model_validate(command.model_dump())
        digest = fingerprint(command)

        def execute(conn: Connection) -> SaveResult:
            repo = PreferenceRepository(conn)
            receipt = repo.receipt(command.request_id, digest)
            if receipt is not None:
                return receipt
            current = repo.current()
            if (current is None and command.revision is not None) or (
                current is not None and command.revision != current[0].revision
            ):
                raise Failure("REVISION_CONFLICT")
            if current is not None and current[1].configuration == command.configuration:
                result = SaveResult(
                    preference_set_id=current[0].preference_set_id,
                    preference_set_version_id=current[1].preference_set_version_id,
                    revision=current[0].revision,
                    outcome="UNCHANGED",
                )
            else:
                if current is not None and current[0].revision == MAX_REVISION:
                    raise Failure("REVISION_EXHAUSTED")
                now = self.clock() if current is None else max(self.clock(), current[0].updated_at)
                root = PreferenceSet(
                    preference_set_id=str(uuid4())
                    if current is None
                    else current[0].preference_set_id,
                    current_preference_set_version_id=str(uuid4()),
                    revision=1 if current is None else current[0].revision + 1,
                    created_at=now if current is None else current[0].created_at,
                    updated_at=now,
                )
                version = PreferenceSetVersion(
                    preference_set_version_id=root.current_preference_set_version_id,
                    preference_set_id=root.preference_set_id,
                    created_at=now,
                    configuration=command.configuration,
                )
                repo.publish(root, version, first=current is None)
                self.store.fault("preferences_after_publication")
                result = SaveResult(
                    preference_set_id=root.preference_set_id,
                    preference_set_version_id=version.preference_set_version_id,
                    revision=root.revision,
                    outcome="CREATED" if current is None else "UPDATED",
                )
            repo.record(command.request_id, digest, result)
            self.store.fault("preferences_after_receipt")
            return result

        return self.store.run(execute, write=True)
