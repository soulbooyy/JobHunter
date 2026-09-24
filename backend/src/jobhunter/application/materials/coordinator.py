"""Short fenced execution transitions; renderer processes never write canonical state."""

import time
from uuid import uuid4

from sqlalchemy.engine import Connection

from jobhunter.application.materials.service import Materials
from jobhunter.domain.derived_work.models import FailureCode, Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials_v2 import (
    MaterialsRepository,
)


class Coordinator:
    def __init__(self, service: Materials) -> None:
        self.service = service
        self.store = service.store

    def queued(self) -> list[str]:
        return self.store.run(
            lambda conn: list(
                conn.exec_driver_sql(
                    "SELECT work_id FROM render_work WHERE status='QUEUED' ORDER BY "
                    "created_at,work_id"
                ).scalars()
            )
        )

    def fail(self, work: Work, code: FailureCode) -> bool:
        def terminal(conn: Connection) -> bool:
            event = self.service.clock()
            result = conn.exec_driver_sql(
                "UPDATE render_work SET "
                "status='FAILED',current_attempt_id=NULL,finished_at=?,failure_code=? WHERE "
                "work_id=? AND status=? AND attempt_count=? AND current_attempt_id IS ?",
                (
                    event,
                    code,
                    work.work_id,
                    work.status,
                    work.attempt_count,
                    work.current_attempt_id,
                ),
            )
            if result.rowcount != 1:
                return False
            conn.exec_driver_sql(
                "UPDATE render_intents SET status='FAILED',finished_at=?,failure_code=? WHERE "
                "work_id=? AND status='PENDING'",
                (event, code, work.work_id),
            )
            return True

        return self.store.run(terminal, write=True)

    def claim(self, identity: str) -> Work | None:
        observed = self.store.run(
            lambda conn, identity=identity: Work.model_validate(
                MaterialsRepository(conn).work(identity)
            )
        )
        if observed.status != "QUEUED":
            return None
        config = self.store.run(
            lambda conn: RenderConfiguration.model_validate(
                MaterialsRepository(conn).configuration(observed.render_configuration_id)
            )
        )
        if not self.service.capability(config):
            self.fail(observed, "CONFIGURATION_UNAVAILABLE")
            return None
        if observed.attempt_count >= observed.max_attempts:
            self.fail(observed, "RECOVERY_EXHAUSTED")
            return None

        def update(conn: Connection) -> Work | None:
            attempt = str(uuid4())
            result = conn.exec_driver_sql(
                "UPDATE render_work SET "
                "status='RUNNING',attempt_count=attempt_count+1,current_attempt_id=? WHERE "
                "work_id=? AND status='QUEUED' AND attempt_count=?",
                (attempt, identity, observed.attempt_count),
            )
            if result.rowcount != 1:
                return None
            return Work.model_validate(MaterialsRepository(conn).work(identity))

        return self.store.run(update, write=True)

    def recover_after_ownership(self) -> None:
        """Call only at startup after the inherited process lock fences every prior writer."""
        identities = self.store.run(
            lambda conn: list(
                conn.exec_driver_sql(
                    "SELECT work_id FROM render_work WHERE status='RUNNING'"
                ).scalars()
            )
        )
        for identity in identities:
            work = self.store.run(
                lambda conn, identity=identity: Work.model_validate(
                    MaterialsRepository(conn).work(identity)
                )
            )
            if work.attempt_count >= work.max_attempts:
                self.fail(work, "RECOVERY_EXHAUSTED")
            else:
                self.store.run(
                    lambda conn, identity=identity, work=work: conn.exec_driver_sql(
                        "UPDATE render_work SET status='QUEUED',current_attempt_id=NULL WHERE "
                        "work_id=? AND status='RUNNING' AND current_attempt_id=?",
                        (identity, work.current_attempt_id),
                    ),
                    write=True,
                )

    def publish(self, work: Work, data: bytes, *, deadline: float | None = None) -> bool:
        "Called with validated bytes after confirmed renderer exit; stale attempts cannot"
        "publish."
        import hashlib

        from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
            MaterialSources,
        )

        identity = str(uuid4())
        self.service.files.place(identity, data)
        self.store.fault("artifact_after_placement")

        def commit(conn: Connection) -> bool:
            repo = MaterialsRepository(conn)
            current = Work.model_validate(repo.work(work.work_id))
            if current.status != "RUNNING" or current.current_attempt_id != work.current_attempt_id:
                return False
            source = MaterialSources(conn).read(work.resume_version_id)
            config = repo.configuration(work.render_configuration_id)
            event = self.service.clock()
            if deadline is not None and time.monotonic() >= deadline:
                conn.exec_driver_sql(
                    "UPDATE render_work SET status='FAILED',current_attempt_id=NULL,finished_at=?,"
                    "failure_code='RESOURCE_LIMIT_EXCEEDED' WHERE work_id=? AND status='RUNNING' "
                    "AND current_attempt_id=?",
                    (event, work.work_id, work.current_attempt_id),
                )
                conn.exec_driver_sql(
                    "UPDATE render_intents SET status='FAILED',finished_at=?,"
                    "failure_code='RESOURCE_LIMIT_EXCEEDED' WHERE work_id=? AND status='PENDING'",
                    (event, work.work_id),
                )
                return False
            repo.insert(
                "artifacts",
                {
                    "artifact_id": identity,
                    "schema_version": 2,
                    "creating_work_id": work.work_id,
                    "creator_status": "SUCCEEDED",
                    "resume_id": source.resume_version.resume_id,
                    "resume_version_id": work.resume_version_id,
                    "render_configuration_id": work.render_configuration_id,
                    "media_type": config["output"]["media_type"],
                    "byte_length": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "created_at": event,
                },
            )
            conn.exec_driver_sql(
                "UPDATE render_work SET "
                "status='SUCCEEDED',current_attempt_id=NULL,artifact_id=?,finished_at=? WHERE "
                "work_id=? AND current_attempt_id=? AND status='RUNNING'",
                (identity, event, work.work_id, work.current_attempt_id),
            )
            conn.exec_driver_sql(
                "UPDATE render_intents SET status='FULFILLED',artifact_id=?,finished_at=? WHERE "
                "work_id=? AND status='PENDING'",
                (identity, event, work.work_id),
            )
            self.store.fault("artifact_before_commit")
            return True

        return self.store.run(commit, write=True)
