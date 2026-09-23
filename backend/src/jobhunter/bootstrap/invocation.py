"""Compose controlled internal runtime only; no HTTP registration or production adapter."""

from collections.abc import Sequence

from jobhunter.agent.harness.runtime import Runtime
from jobhunter.application.invocation.controlled import ControlledConsumer, ControlledFormat
from jobhunter.application.invocation.ports import Clock, Consumer, ResponseFormat
from jobhunter.domain.invocation.models import Success
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.invocation import (
    InvocationPersistence,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def invocation_runtime(
    store: Store,
    *,
    clock: Clock | None = None,
    consumers: Sequence[Consumer] | None = None,
    formats: Sequence[ResponseFormat] | None = None,
) -> Runtime:
    runtime = Runtime(
        InvocationPersistence(store),
        consumers
        if consumers is not None
        else (ControlledConsumer("model"), ControlledConsumer("read")),
        formats if formats is not None else (ControlledFormat(),),
        clock=clock,
    )
    outcome = runtime.startup()
    if not isinstance(outcome, Success):
        raise Failure(outcome.code)
    store.execution_runtime = runtime
    return runtime
