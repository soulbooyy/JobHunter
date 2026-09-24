"""Single execution slot, durable discovery, monotonic budget and conservative uncertainty."""

import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import cast

from jobhunter.application.materials.coordinator import Coordinator
from jobhunter.domain.derived_work.models import FailureCode, Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
    MaterialSources,
)
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials_v2 import (
    MaterialsRepository,
)
from jobhunter.infrastructure.rendering.process import ProcessRenderer
from jobhunter.infrastructure.rendering.validation import validate_output


class Runner:
    def __init__(
        self, coordinator: Coordinator, assets: Path, environment: Callable[[], dict[str, str]]
    ) -> None:
        self.coordinator = coordinator
        self.renderer = ProcessRenderer(assets, environment, coordinator.store.lock_fd)
        self.stop_event = threading.Event()
        self.thread: threading.Thread | None = None
        self.uncertain = False
        self.pending_failures: dict[str, tuple[Work, FailureCode]] = {}

    def start(self) -> None:
        self.coordinator.recover_after_ownership()
        self.thread = threading.Thread(target=self.loop, name="material-worker", daemon=False)
        self.thread.start()

    def close(self) -> None:
        self.stop_event.set()
        if self.thread is not None:
            self.thread.join()

    def loop(self) -> None:
        while not self.stop_event.is_set():
            try:
                for work, code in list(self.pending_failures.values()):
                    self.fail(work, code)
                for identity in self.coordinator.queued():
                    if self.stop_event.is_set():
                        return
                    work = self.coordinator.claim(identity)
                    if work is not None:
                        self.execute(work)
            except Failure as exc:
                if exc.code == "OUTCOME_UNKNOWN":
                    # Stop this execution epoch. Startup must reacquire ownership and recognize
                    # durable state before reconciling; no speculative claim/command replay.
                    self.uncertain = True
                    return
            except Exception:
                # Never expose renderer output, source values or SQL to ordinary logs.
                pass
            self.stop_event.wait(0.25)

    def fail(self, work: Work, code: FailureCode) -> None:
        # A terminal-write outage must not replace the already-known renderer failure.
        original, primary = self.pending_failures.setdefault(work.work_id, (work, code))
        self.coordinator.fail(original, primary)
        self.pending_failures.pop(work.work_id, None)

    def execute(self, work: Work) -> None:
        start = time.monotonic()
        store = self.coordinator.store
        try:
            source = store.run(lambda conn: MaterialSources(conn).read(work.resume_version_id))
        except Failure as exc:
            self.fail(
                work,
                "STORAGE_FAILED" if exc.code == "STORAGE_UNAVAILABLE" else "SOURCE_UNAVAILABLE",
            )
            return
        try:
            configuration = store.run(
                lambda conn: MaterialsRepository(conn).configuration(work.render_configuration_id)
            )
            data = self.renderer.produce(
                source,
                configuration,
                work,
                start + work.timeout_ms / 1000,
                lambda: self.fail(work, "RESOURCE_LIMIT_EXCEEDED"),
            )
            validate_output(data, RenderConfiguration.model_validate(configuration), work, source)
            self.coordinator.publish(work, data, deadline=start + work.timeout_ms / 1000)
        except Failure as exc:
            if exc.code == "OUTCOME_UNKNOWN":
                raise
            failure_code: FailureCode = (
                "STORAGE_FAILED"
                if exc.code == "STORAGE_UNAVAILABLE"
                else cast(FailureCode, exc.code)
                if exc.code
                in (
                    "OUTPUT_INVALID",
                    "RESOURCE_LIMIT_EXCEEDED",
                    "CONFIGURATION_UNAVAILABLE",
                    "PERMISSION_DENIED",
                    "RENDER_FAILED",
                )
                else "INTERNAL_ERROR"
            )
            self.fail(work, failure_code)
        except OSError:
            self.fail(work, "STORAGE_FAILED")
        except Exception:
            self.fail(work, "INTERNAL_ERROR")
