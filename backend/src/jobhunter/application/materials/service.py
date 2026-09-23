"""Accept retained demand without rendering inside the authority transaction."""

from collections.abc import Callable
from typing import BinaryIO
from uuid import uuid4

from sqlalchemy.engine import Connection

from jobhunter.application.candidate.authority import identifier
from jobhunter.application.manual_application_entries.service import utc_now
from jobhunter.domain.derived_work.models import Accepted, Limits, RenderRequest, fingerprint
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.shared.candidate_values import FieldFailure
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.filesystem.artifacts import ArtifactFiles
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json, encoded
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
    MaterialSources,
)
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials import (
    MaterialsRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def unavailable(configuration: RenderConfiguration) -> bool:
    """No unverified renderer/font catalog is advertised as executable."""
    return False


def defaults() -> Limits:
    return Limits(
        max_attempts=3,
        max_pages=50,
        max_png_pixels=100_000_000,
        max_output_bytes=50_000_000,
        timeout_ms=60_000,
    )


class Materials:
    def __init__(
        self,
        store: Store,
        *,
        capability: Callable[[RenderConfiguration], bool] = unavailable,
        limits: Callable[[], Limits] = defaults,
        clock: Callable[[], str] = utc_now,
    ) -> None:
        self.store = store
        self.capability: Callable[[RenderConfiguration], bool] = capability
        self.limits = limits
        self.clock = clock
        self.files = ArtifactFiles(store.directory)

    def configuration(self, identity: str) -> Json:
        identifier(identity, "render_configuration_id")
        config = self.store.run(lambda conn: MaterialsRepository(conn).configuration(identity))
        return {
            "configuration": config,
            "can_generate": self.capability(RenderConfiguration.model_validate(config)),
        }

    def configurations(self) -> Json:
        def read(conn: Connection) -> Json:
            repo = MaterialsRepository(conn)
            items: list[Json] = []
            for identity in conn.exec_driver_sql(
                "SELECT render_configuration_id FROM render_configurations ORDER BY "
                "render_configuration_id"
            ).scalars():
                config = repo.configuration(identity)
                if self.capability(RenderConfiguration.model_validate(config)):
                    items.append({"configuration": config, "can_generate": True})
            return {"items": items}

        return self.store.run(read)

    def intent(self, identity: str) -> Json:
        identifier(identity, "render_intent_id")
        return self.store.run(lambda conn: MaterialsRepository(conn).intent(identity))

    def artifact(self, identity: str) -> Json:
        identifier(identity, "artifact_id")
        return self.store.run(lambda conn: MaterialsRepository(conn).artifact(identity))

    def content(self, identity: str) -> tuple[Json, BinaryIO]:
        artifact = self.artifact(identity)
        return artifact, self.files.snapshot(identity, artifact["byte_length"], artifact["sha256"])

    def request(self, command: RenderRequest) -> Json:
        def accept(conn: Connection) -> Json:
            repo = MaterialsRepository(conn)
            replay = repo.replay(command)
            if replay is not None:
                return replay
            source_row = repo.row(
                "SELECT resume_id FROM resume_versions WHERE resume_version_id=?",
                (command.resume_version_id,),
            )
            if source_row is None:
                raise FieldFailure("resume_version_id", "INVALID_REFERENCE")
            if repo.root("resume", source_row["resume_id"], required=True)["status"] != "ACTIVE":
                raise Failure("INVALID_STATE")
            MaterialSources(conn).read(command.resume_version_id)
            try:
                config = repo.configuration(command.render_configuration_id)
            except Failure as exc:
                if exc.code == "NOT_FOUND":
                    raise FieldFailure("render_configuration_id", "INVALID_REFERENCE") from None
                raise
            if not self.capability(RenderConfiguration.model_validate(config)):
                raise Failure("RENDER_CONFIGURATION_UNAVAILABLE")
            artifact_id: str | None = None
            for identity in conn.exec_driver_sql(
                "SELECT artifact_id FROM artifacts WHERE resume_version_id=? AND "
                "render_configuration_id=? ORDER BY created_at,artifact_id",
                (command.resume_version_id, command.render_configuration_id),
            ).scalars():
                artifact = repo.artifact(identity)
                try:
                    with self.files.snapshot(identity, artifact["byte_length"], artifact["sha256"]):
                        artifact_id = identity
                        break
                except Failure as exc:
                    if exc.code not in ("ARTIFACT_UNAVAILABLE", "ARTIFACT_INTEGRITY_FAILED"):
                        raise
            event = self.clock()
            work_id: str | None = None
            if artifact_id is None:
                work = repo.row(
                    "SELECT work_id FROM render_work WHERE resume_version_id=? AND "
                    "render_configuration_id=? AND status IN ('QUEUED','RUNNING')",
                    (command.resume_version_id, command.render_configuration_id),
                )
                if work is not None:
                    work_id = repo.work(work["work_id"])["work_id"]
                else:
                    limits = Limits.model_validate(self.limits().model_dump())
                    work_id = str(uuid4())
                    repo.insert(
                        "render_work",
                        {
                            "work_id": work_id,
                            "resume_version_id": command.resume_version_id,
                            "render_configuration_id": command.render_configuration_id,
                            "status": "QUEUED",
                            "attempt_count": 0,
                            **limits.model_dump(),
                            "current_attempt_id": None,
                            "created_at": event,
                            "finished_at": None,
                            "artifact_id": None,
                            "failure_code": None,
                        },
                    )
            identity = str(uuid4())
            repo.insert(
                "render_intents",
                {
                    "render_intent_id": identity,
                    "resume_version_id": command.resume_version_id,
                    "render_configuration_id": command.render_configuration_id,
                    "status": "FULFILLED" if artifact_id else "PENDING",
                    "created_at": event,
                    "finished_at": event if artifact_id else None,
                    "artifact_id": artifact_id,
                    "failure_code": None,
                    "work_id": work_id,
                },
            )
            result = Accepted(
                request_id=command.request_id, outcome="ACCEPTED", render_intent_id=identity
            ).model_dump(mode="json")
            repo.insert(
                "material_command_receipts",
                {
                    "request_id": command.request_id,
                    "operation": "RENDER_REQUEST",
                    "request_fingerprint": fingerprint(command),
                    "schema_version": 1,
                    "result_snapshot": encoded(result),
                    "render_intent_id": identity,
                },
            )
            return result

        return self.store.run(accept, write=True)
