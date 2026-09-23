"""Internal execution authority and bounded recovery. No public API or SDK."""

import asyncio
from collections.abc import Callable, Generator, Sequence
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import UTC, datetime
from hashlib import sha256
from threading import Lock, get_ident
from time import monotonic
from typing import Never, Self
from uuid import uuid4

from jobhunter.application.invocation.controlled import READ_ACTION, ControlledConsumer
from jobhunter.application.invocation.ports import (
    Clock,
    Consumer,
    Gateway,
    Persistence,
    Repository,
    ResponseFormat,
)
from jobhunter.domain.invocation.models import (
    Admission,
    Denial,
    Descriptor,
    Ending,
    EndReason,
    FailureCode,
    Generation,
    Instant,
    LocalRead,
    ModelInvocation,
    ModelRead,
    Publication,
    Qualification,
    Rejected,
    Response,
    Result,
    Run,
    Success,
    Unresolved,
)
from jobhunter.domain.shared.errors import Failure
from jobhunter.domain.shared.values import MAX_REVISION, UuidV4
from pydantic import TypeAdapter


class SystemClock:
    def utc(self) -> str:
        return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")

    def monotonic(self) -> float:
        return monotonic()


def no_fault(stage: str) -> None:
    pass


def ending(run: Run) -> Ending:
    if run.end_reason is None or run.ended_at is None:
        raise Failure("RUN_NOT_ENDED")
    return Ending(
        run_id=run.run_id,
        execution_generation=run.execution_generation,
        ended_at=run.ended_at,
        end_reason=run.end_reason,
        failure_code=run.failure_code,
    )


def changed(run: Run, **values: object) -> Run:
    return Run.model_validate(run.model_dump() | values)


def task_identity() -> object:
    try:
        return asyncio.current_task()
    except RuntimeError:
        return None


class LivePath:
    """Identity-checked, thread/context-bound, never serialized or reconstructed."""

    def __init__(self, invocation_id: str, qualification: Qualification) -> None:
        self.invocation_id = invocation_id
        self.qualification = qualification
        self.thread = get_ident()
        self.task = task_identity()
        self.entered = False
        self.won = False
        self.closed = False
        self.gateway: Gateway | None = None
        self.interrupted = False
        self.interrupt_lock = Lock()
        self.lock = Lock()

    def __copy__(self) -> Self:
        raise TypeError("Live execution paths cannot be copied")

    def __deepcopy__(self, memo: object) -> Self:
        raise TypeError("Live execution paths cannot be copied")

    def __reduce__(self) -> Never:
        raise TypeError("Live execution paths cannot be serialized")


class Runtime:
    def __init__(
        self,
        persistence: Persistence,
        consumers: Sequence[Consumer],
        formats: Sequence[ResponseFormat],
        *,
        clock: Clock | None = None,
        fault: Callable[[str], None] = no_fault,
    ) -> None:
        self.persistence = persistence
        self.consumers = {c.key: c for c in consumers}
        self.formats = {f.key: f for f in formats}
        if (
            len(self.consumers) != len(consumers)
            or len(self.formats) != len(formats)
            or any(not k for k in (*self.consumers, *self.formats))
        ):
            raise Failure("DUPLICATE_OR_INVALID_REGISTRATION")
        persistence.claim_runtime()
        self.runtime_instance_id = str(uuid4())
        self.clock = clock or SystemClock()
        self.fault = fault
        self._path: ContextVar[LivePath | None] = ContextVar("invocation_path", default=None)
        self._paths: dict[str, LivePath] = {}
        self._paths_lock = Lock()
        self._grant_lock = Lock()
        self._deadlines: dict[str, tuple[str, float]] = {}
        self._deadline_lock = Lock()
        self.ready = False

    def _result[T](self, operation: Callable[[], T], identity: str | None = None) -> Result[T]:
        try:
            self.persistence.check_owner()
            if not self.ready:
                raise Failure("RUNTIME_NOT_READY")
            value = operation()
            if isinstance(value, Ending):
                self._interrupt(value.run_id)
            return Success(value)
        except Failure as exc:
            if exc.code in ("OUTCOME_UNKNOWN", "STORAGE_UNAVAILABLE", "CONSUMER_UNRESOLVED"):
                return Unresolved(exc.code, identity)
            return Rejected(exc.code)
        except (ValueError, TypeError, OverflowError):
            return Rejected("INVALID_INPUT")
        except Exception:
            return Unresolved("INTERNAL_ERROR", identity)

    def _interrupt_path(self, path: LivePath) -> None:
        with path.interrupt_lock:
            if path.interrupted or path.gateway is None:
                return
            path.interrupted = True
        try:
            path.gateway.interrupt()
        except Exception:
            pass

    def _interrupt(self, run_id: str) -> None:
        with self._paths_lock:
            paths = list(self._paths.values())
        for path in paths:
            if path.qualification.run_id == run_id:
                self._interrupt_path(path)

    def _write[T](
        self, operation: Callable[[Repository], T], truth: Callable[[Repository], T]
    ) -> T:
        try:
            return self.persistence.transact(operation, write=True)
        except Failure as exc:
            if exc.code != "OUTCOME_UNKNOWN":
                raise
        # One fresh read, no command/COMMIT replay. This is the finite bound.
        try:
            return self.persistence.transact(truth)
        except Exception:
            raise Failure("OUTCOME_UNKNOWN") from None

    def _consumer(self, run: Run) -> Consumer:
        consumer = self.consumers.get(run.consumer_key)
        if consumer is None:
            raise Failure("CONSUMER_UNAVAILABLE")
        return consumer

    def _admission(self, repo: Repository, run: Run) -> Admission:
        return self._consumer(run).admit_recovery(repo, run, self._now(run))

    def _admit(self, repo: Repository, run: Run) -> None:
        result = self._admission(repo, run)
        if result == "UNRESOLVED":
            raise Failure("CONSUMER_UNRESOLVED")
        if isinstance(result, Denial):
            raise Failure(result.failure_code or "DEADLINE_EXPIRED")

    def _now(self, run: Run) -> str:
        now = self.clock.utc()
        if run.deadline_at is None:
            return now
        with self._deadline_lock:
            baseline = self._deadlines.get(run.run_id)
            if baseline is None:
                self._deadlines[run.run_id] = (now, self.clock.monotonic())
                return now
        # Monotonic elapsed prevents a live wall-clock rollback renewing a budget.
        from datetime import timedelta

        floor = datetime.fromisoformat(baseline[0]) + timedelta(
            seconds=max(0, self.clock.monotonic() - baseline[1])
        )
        floor_text = floor.isoformat(timespec="milliseconds").replace("+00:00", "Z")
        return max(now, floor_text)

    def _remote(self, repo: Repository, run: Run) -> None:
        self._admit(repo, run)
        if run.deadline_at is None or self._now(run) >= run.deadline_at:
            raise Failure("DEADLINE_EXPIRED")

    def _current(self, repo: Repository, qualification: Qualification) -> Run:
        q = Qualification.model_validate(qualification.model_dump())
        run = repo.run(q.run_id)
        if run.run_status != "OPEN":
            raise Failure("RUN_ENDED")
        if q.runtime_instance_id != self.runtime_instance_id or (
            run.owner_runtime_instance_id,
            run.execution_generation,
        ) != (q.runtime_instance_id, q.execution_generation):
            raise Failure("EXECUTION_NOT_CURRENT")
        return run

    def _finish(
        self, repo: Repository, run: Run, reason: EndReason, code: FailureCode | None = None
    ) -> Ending:
        if run.run_status == "ENDED":
            return ending(run)
        result = changed(
            run,
            run_status="ENDED",
            owner_runtime_instance_id=None,
            ended_at=self.clock.utc(),
            end_reason=reason,
            failure_code=code,
        )
        repo.save_run(result)
        self.fault("ending_written")
        return ending(result)

    def create_run(self, consumer_key: str, deadline_at: str | None) -> Result[str]:
        identity = str(uuid4())

        def create() -> str:
            run = Run(
                run_id=identity,
                consumer_key=consumer_key,
                run_status="OPEN",
                execution_generation=0,
                owner_runtime_instance_id=None,
                deadline_at=deadline_at,
                created_at=self.clock.utc(),
                ended_at=None,
                end_reason=None,
                failure_code=None,
            )
            self._consumer(run)

            def write(repo: Repository) -> str:
                repo.insert_run(run)
                self.fault("run_written")
                return identity

            def truth(repo: Repository) -> str:
                if repo.run(identity) != run:
                    raise Failure("OUTCOME_UNKNOWN")
                return identity

            return self._write(write, truth)

        return self._result(create, identity)

    def read_run(self, run_id: str) -> Result[Run]:
        return self._result(
            lambda: self.persistence.transact(
                lambda repo: repo.run(TypeAdapter[str](UuidV4).validate_python(run_id))
            )
        )

    def grant_execution(self, run_id: str, expected_generation: int) -> Result[Qualification]:
        def grant() -> Qualification:
            identity = TypeAdapter[str](UuidV4).validate_python(run_id)
            generation = TypeAdapter[int](Generation).validate_python(expected_generation)
            candidate: Qualification | None = None

            def write(repo: Repository) -> Qualification:
                nonlocal candidate
                run = repo.run(identity)
                if run.run_status != "OPEN":
                    raise Failure("RUN_ENDED")
                if (
                    run.owner_runtime_instance_id is not None
                    or run.execution_generation != generation
                ):
                    raise Failure("EXECUTION_NOT_CURRENT")
                if generation == MAX_REVISION:
                    raise Failure("GENERATION_EXHAUSTED")
                self._admit(repo, run)
                q = Qualification(
                    run_id=identity,
                    runtime_instance_id=self.runtime_instance_id,
                    execution_generation=generation + 1,
                )
                repo.save_run(
                    changed(
                        run,
                        execution_generation=q.execution_generation,
                        owner_runtime_instance_id=q.runtime_instance_id,
                    )
                )
                candidate = q  # Only this live serialized transaction won.
                self.fault("grant_written")
                return q

            def truth(repo: Repository) -> Qualification:
                self.fault("grant_reconciliation")
                if candidate is None:
                    raise Failure("OUTCOME_UNKNOWN")
                self._current(repo, candidate)
                self._admit(repo, repo.run(identity))
                return candidate

            # Retain live arbitration through bounded commit-truth inspection.
            # Otherwise a rolled-back attempt could mistake a rival's identical
            # instance/generation row for proof of its own grant commitment.
            with self._grant_lock:
                return self._write(write, truth)

        return self._result(grant, run_id)

    def revoke_execution(self, qualification: Qualification) -> Result[int]:
        def write(repo: Repository) -> int:
            run = self._current(repo, qualification)
            repo.save_run(changed(run, owner_runtime_instance_id=None))
            return run.execution_generation

        def truth(repo: Repository) -> int:
            run = repo.run(qualification.run_id)
            if (
                run.run_status != "OPEN"
                or run.owner_runtime_instance_id is not None
                or run.execution_generation != qualification.execution_generation
            ):
                raise Failure("OUTCOME_UNKNOWN")
            return run.execution_generation

        return self._result(lambda: self._write(write, truth), qualification.run_id)

    def establish_deadline(self, run_id: str, deadline_at: str) -> Result[str]:
        def establish() -> str:
            identity = TypeAdapter[str](UuidV4).validate_python(run_id)
            deadline = TypeAdapter[str](Instant).validate_python(deadline_at)

            def write(repo: Repository) -> str:
                run = repo.run(identity)
                self._consumer(run)  # Internal consumer establishment boundary.
                if run.deadline_at == deadline:
                    return deadline
                if run.run_status == "ENDED":
                    raise Failure("RUN_ENDED")
                if run.deadline_at is not None:
                    raise Failure("DEADLINE_FROZEN")
                repo.save_run(changed(run, deadline_at=deadline))
                return deadline

            def truth(repo: Repository) -> str:
                if repo.run(identity).deadline_at != deadline:
                    raise Failure("OUTCOME_UNKNOWN")
                return deadline

            return self._write(write, truth)

        return self._result(establish, run_id)

    def cancel_run(self, run_id: str) -> Result[Ending]:
        def cancel() -> Ending:
            identity = TypeAdapter[str](UuidV4).validate_python(run_id)
            result = self._write(
                lambda repo: self._finish(repo, repo.run(identity), "CANCELLED"),
                lambda repo: ending(repo.run(identity)),
            )
            return result

        return self._result(cancel, run_id)

    def end_run(
        self,
        qualification: Qualification,
        end_reason: EndReason,
        failure_code: FailureCode | None = None,
    ) -> Result[Ending]:
        def write(repo: Repository) -> Ending:
            run = repo.run(qualification.run_id)
            if run.run_status == "ENDED":
                return ending(run)
            run = self._current(repo, qualification)
            if end_reason == "COMPLETED":
                if self._consumer(run).reconcile_result(repo, run) != "COMPLETION_CONFIRMED":
                    raise Failure("COMPLETION_NOT_CONFIRMED")
            elif end_reason == "TIMED_OUT":
                if run.deadline_at is None or self._now(run) < run.deadline_at:
                    raise Failure("DEADLINE_NOT_EXPIRED")
            else:
                raise Failure("ENDING_NOT_AUTHORIZED")
            if failure_code is not None:
                raise Failure("INVALID_INPUT")
            return self._finish(repo, run, end_reason)

        return self._result(
            lambda: self._write(write, lambda repo: ending(repo.run(qualification.run_id))),
            qualification.run_id,
        )

    def prepare_model_invocation(
        self, qualification: Qualification, response_format_key: str, max_response_bytes: int
    ) -> Result[str]:
        identity = str(uuid4())

        def prepare() -> str:
            inv = ModelInvocation(
                invocation_id=identity,
                run_id=qualification.run_id,
                kind="MODEL",
                response_format_key=response_format_key,
                max_response_bytes=max_response_bytes,
                durability_phase="PREPARED",
                dispatch_generation=None,
                response_rejection_code=None,
            )
            if response_format_key not in self.formats:
                raise Failure("RESPONSE_FORMAT_UNAVAILABLE")

            def write(repo: Repository) -> str:
                run = self._current(repo, qualification)
                self._remote(repo, run)
                if len(repo.models(run.run_id)) >= self._consumer(run).max_models:
                    raise Failure("CONSUMER_CAPACITY_EXCEEDED")
                repo.insert_model(ModelRead(invocation=inv, descriptor=None))
                self.fault("invocation_written")
                return identity

            def truth(repo: Repository) -> str:
                if repo.model(identity).invocation != inv:
                    raise Failure("OUTCOME_UNKNOWN")
                return identity

            return self._write(write, truth)

        return self._result(prepare, identity)

    def read_model_invocation(self, invocation_id: str) -> Result[ModelRead]:
        return self._result(
            lambda: self.persistence.transact(
                lambda repo: repo.model(TypeAdapter[str](UuidV4).validate_python(invocation_id))
            )
        )

    def read_response(self, invocation_id: str) -> Result[Response]:
        return self._result(
            lambda: self.persistence.transact(
                lambda repo: repo.response(TypeAdapter[str](UuidV4).validate_python(invocation_id))
            )
        )

    @contextmanager
    def model_path(self, invocation_id: str, qualification: Qualification) -> Generator[None]:
        self.persistence.check_owner()
        path = LivePath(invocation_id, qualification)
        with self._paths_lock:
            if invocation_id in self._paths:
                raise Failure("SENDING_PATH_UNAVAILABLE")
            self._paths[invocation_id] = path
        token = self._path.set(path)
        try:
            yield
        finally:
            path.closed = True
            self._path.reset(token)
            with self._paths_lock:
                self._paths.pop(invocation_id, None)

    def _live(self, invocation_id: str, qualification: Qualification) -> LivePath:
        path = self._path.get()
        if (
            path is None
            or path.closed
            or path.thread != get_ident()
            or path.task is not task_identity()
            or path.invocation_id != invocation_id
            or path.qualification != qualification
            or self._paths.get(invocation_id) is not path
        ):
            raise Failure("SENDING_PATH_UNAVAILABLE")
        return path

    def _association(
        self, repo: Repository, invocation_id: str, qualification: Qualification
    ) -> ModelRead:
        TypeAdapter[str](UuidV4).validate_python(invocation_id)
        Qualification.model_validate(qualification.model_dump())
        model = repo.model(invocation_id)
        if model.invocation.run_id != qualification.run_id:
            raise Failure("REFERENCE_MISMATCH")
        repo.run(qualification.run_id)
        return model

    def commit_dispatch_intent(
        self, invocation_id: str, qualification: Qualification, descriptor: Descriptor
    ) -> Result[None]:
        def commit() -> None:
            exact = Descriptor.model_validate(descriptor.model_dump())
            path = self._live(invocation_id, qualification)
            with path.lock:
                if path.won or path.entered:
                    raise Failure("SENDING_PATH_UNAVAILABLE")
                proposed: ModelRead | None = None
                format_unavailable = False

                def write(repo: Repository) -> None:
                    nonlocal proposed, format_unavailable
                    model = self._association(repo, invocation_id, qualification)
                    run = self._current(repo, qualification)
                    self._remote(repo, run)
                    if model.invocation.response_format_key not in self.formats:
                        format_unavailable = True
                        self._finish(repo, run, "FAILED", "RESPONSE_FORMAT_UNAVAILABLE")
                        return
                    if model.invocation.durability_phase != "PREPARED":
                        raise Failure("SENDING_PATH_UNAVAILABLE")
                    inv = ModelInvocation.model_validate(
                        model.invocation.model_dump()
                        | {
                            "durability_phase": "DISPATCH_INTENT_DURABLE",
                            "dispatch_generation": qualification.execution_generation,
                        }
                    )
                    proposed = ModelRead(invocation=inv, descriptor=exact)
                    repo.save_model(proposed)
                    self.fault("intent_written")

                def truth(repo: Repository) -> None:
                    if format_unavailable:
                        run = repo.run(qualification.run_id)
                        if run.failure_code == "RESPONSE_FORMAT_UNAVAILABLE":
                            return
                        raise Failure("OUTCOME_UNKNOWN")
                    if proposed is None or repo.model(invocation_id) != proposed or path.entered:
                        raise Failure("OUTCOME_UNKNOWN")
                    self._remote(repo, self._current(repo, qualification))

                self._write(write, truth)
                if format_unavailable:
                    self._interrupt(qualification.run_id)
                    raise Failure("RESPONSE_FORMAT_UNAVAILABLE")
                path.won = True

        return self._result(commit, invocation_id)

    def publish_response(
        self, invocation_id: str, qualification: Qualification, serialized_payload: bytes
    ) -> Result[Publication]:
        def publish() -> Publication:
            if type(serialized_payload) is not bytes:
                raise ValueError("Invalid bytes")

            def existing(repo: Repository) -> Publication | None:
                model = self._association(repo, invocation_id, qualification)
                if model.invocation.durability_phase != "RESPONSE_DURABLE":
                    # Also detects an inconsistent extra response record.
                    try:
                        repo.response(invocation_id)
                    except Failure as exc:
                        if exc.code == "RESPONSE_NOT_DURABLE":
                            return None
                        raise
                response = repo.response(invocation_id)
                if response.serialized_payload != serialized_payload:
                    raise Failure("INTEGRITY_CONFLICT")
                return response.publication()

            confirmed = self.persistence.transact(existing)
            if confirmed is not None:
                return confirmed

            def write(repo: Repository) -> Publication:
                winner = existing(repo)
                if winner is not None:
                    return winner
                model = self._association(repo, invocation_id, qualification)
                path = self._live(invocation_id, qualification)
                if not path.won or not path.entered:
                    raise Failure("SENDING_PATH_UNAVAILABLE")
                run = self._current(repo, qualification)
                self._remote(repo, run)
                inv = model.invocation
                if (
                    inv.durability_phase != "DISPATCH_INTENT_DURABLE"
                    or inv.dispatch_generation != qualification.execution_generation
                ):
                    raise Failure("EXECUTION_NOT_CURRENT")
                reader = self.formats.get(inv.response_format_key)
                if reader is None:
                    raise Failure("RESPONSE_FORMAT_UNAVAILABLE")
                try:
                    reader.validate(serialized_payload)
                except (ValueError, TypeError):
                    raise Failure("RESPONSE_FORMAT_INVALID") from None
                if len(serialized_payload) > inv.max_response_bytes:
                    rejected = ModelInvocation.model_validate(
                        inv.model_dump() | {"response_rejection_code": "RESPONSE_TOO_LARGE"}
                    )
                    repo.save_model(ModelRead(invocation=rejected, descriptor=model.descriptor))
                    self._finish(repo, run, "FAILED", "RESPONSE_TOO_LARGE")
                    # Return a marker internally so the transaction commits its evidence.
                    raise _Oversized()
                response = Response(
                    invocation_id=invocation_id,
                    response_format_key=inv.response_format_key,
                    serialized_payload=serialized_payload,
                    sha256=sha256(serialized_payload).hexdigest(),
                    byte_length=len(serialized_payload),
                )
                repo.insert_response(response)
                repo.save_model(
                    ModelRead(
                        invocation=ModelInvocation.model_validate(
                            inv.model_dump() | {"durability_phase": "RESPONSE_DURABLE"}
                        ),
                        descriptor=model.descriptor,
                    )
                )
                self.fault("response_written")
                return response.publication()

            # Oversize uses a transaction return, never an exception-triggered rollback.
            def save(repo: Repository) -> Publication | None:
                try:
                    return write(repo)
                except _Oversized:
                    return None

            def truth(repo: Repository) -> Publication | None:
                result = existing(repo)
                if result is not None:
                    return result
                inv = repo.model(invocation_id).invocation
                run = repo.run(inv.run_id)
                if (
                    inv.response_rejection_code == "RESPONSE_TOO_LARGE"
                    and run.end_reason == "FAILED"
                    and run.failure_code == "RESPONSE_TOO_LARGE"
                ):
                    return None
                raise Failure("OUTCOME_UNKNOWN")

            result = self._write(save, truth)
            if result is None:
                self._interrupt(qualification.run_id)
                raise Failure("RESPONSE_TOO_LARGE")
            return result

        return self._result(publish, invocation_id)

    def send(
        self, invocation_id: str, qualification: Qualification, gateway: Gateway
    ) -> Result[Publication]:
        def dispatch() -> Result[Publication]:
            path = self._live(invocation_id, qualification)
            with path.lock:
                if not path.won or path.entered:
                    raise Failure("SENDING_PATH_UNAVAILABLE")

                def admit(repo: Repository) -> ModelRead:
                    model = self._association(repo, invocation_id, qualification)
                    self._remote(repo, self._current(repo, qualification))
                    if (
                        model.invocation.dispatch_generation != qualification.execution_generation
                        or model.invocation.durability_phase != "DISPATCH_INTENT_DURABLE"
                    ):
                        raise Failure("SENDING_PATH_UNAVAILABLE")
                    return model

                model = self.persistence.transact(admit)
                assert model.descriptor is not None
                path.entered = True  # Before adapter entry; never reset even on exceptions.
                path.gateway = gateway
            self.fault("before_adapter")
            self.persistence.transact(admit)
            limit = 2 * model.invocation.max_response_bytes + 256
            data = bytearray()
            try:
                for index, frame in enumerate(gateway.receive(model.descriptor, limit)):
                    # Bound even a stream of empty nonterminal frames. Recheck
                    # live time/authority while receiving, not only at publication.
                    if index >= model.invocation.max_response_bytes + 1:
                        break
                    self.persistence.transact(
                        lambda repo: self._remote(repo, self._current(repo, qualification))
                    )
                    if len(data) + len(frame.data) > limit:
                        break
                    data.extend(frame.data)
                    if frame.terminal:
                        self.fault("response_received")
                        return self.publish_response(invocation_id, qualification, bytes(data))
            except Exception:
                pass  # No exception text/transport secrets escape.
            self._interrupt_path(path)

            def unknown(repo: Repository) -> Ending:
                run = repo.run(qualification.run_id)
                if run.run_status == "ENDED":
                    return ending(run)
                self._current(repo, qualification)
                return self._finish(repo, run, "OUTCOME_UNKNOWN")

            result = self._result(
                lambda: self._write(unknown, lambda repo: ending(repo.run(qualification.run_id))),
                qualification.run_id,
            )
            if not isinstance(result, Success):
                return result
            return Rejected("REMOTE_OUTCOME_UNKNOWN")

        result = self._result(dispatch, invocation_id)
        return result.value if isinstance(result, Success) else result

    def prepare_local_read(
        self, qualification: Qualification, source_invocation_id: str, lineage_id: str | None = None
    ) -> Result[str]:
        identity = str(uuid4())

        def prepare() -> str:
            tool = LocalRead(
                invocation_id=identity,
                run_id=qualification.run_id,
                kind="TOOL",
                action_key=READ_ACTION,
                source_invocation_id=source_invocation_id,
                lineage_id=lineage_id,
                result_sha256=None,
                result_byte_length=None,
            )

            def write(repo: Repository) -> str:
                run = self._current(repo, qualification)
                self._remote(repo, run)  # New acquisitions stop at the original deadline.
                if len(repo.tools(run.run_id)) >= self._consumer(run).max_tools:
                    raise Failure("CONSUMER_CAPACITY_EXCEEDED")
                repo.response(source_invocation_id)
                repo.insert_tool(tool)
                return identity

            def truth(repo: Repository) -> str:
                if repo.tool(identity) != tool:
                    raise Failure("OUTCOME_UNKNOWN")
                return identity

            return self._write(write, truth)

        return self._result(prepare, identity)

    def resume_local_read(
        self, invocation_id: str, qualification: Qualification
    ) -> Result[LocalRead]:
        def write(repo: Repository) -> LocalRead:
            tool = repo.tool(TypeAdapter[str](UuidV4).validate_python(invocation_id))
            if tool.run_id != qualification.run_id:
                raise Failure("REFERENCE_MISMATCH")
            run = self._current(repo, qualification)
            self._admit(repo, run)
            consumer = self._consumer(run)
            if not isinstance(consumer, ControlledConsumer) or consumer.max_tools != 1:
                raise Failure("CONTROLLED_ACTION_UNAVAILABLE")
            result = consumer.read(repo, tool)
            self.fault("tool_result_written")
            return result

        def truth(repo: Repository) -> LocalRead:
            tool = repo.tool(invocation_id)
            if tool.result_sha256 is None:
                raise Failure("OUTCOME_UNKNOWN")
            return tool

        return self._result(lambda: self._write(write, truth), invocation_id)

    def coordinate_ending(self, run_id: str, expected_generation: int) -> Result[Ending | None]:
        """Derive facts afresh; callers cannot submit arbitrary reason/evidence flags."""

        def write(repo: Repository) -> Ending | None:
            run = repo.run(TypeAdapter[str](UuidV4).validate_python(run_id))
            generation = TypeAdapter[int](Generation).validate_python(expected_generation)
            if run.run_status == "ENDED":
                return ending(run)
            if run.owner_runtime_instance_id is not None or run.execution_generation != generation:
                raise Failure("EXECUTION_NOT_CURRENT")
            consumer = self.consumers.get(run.consumer_key)
            if consumer is None:
                return self._finish(repo, run, "FAILED", "CONSUMER_UNAVAILABLE")
            completion = consumer.reconcile_result(repo, run)
            if completion == "UNRESOLVED":
                raise Failure("CONSUMER_UNRESOLVED")
            if completion == "COMPLETION_CONFIRMED":
                return self._finish(repo, run, "COMPLETED")
            try:
                admission = self._admission(repo, run)
            except Failure as exc:
                if exc.code == "RESPONSE_INTEGRITY_FAILED":
                    return self._finish(repo, run, "FAILED", "RESPONSE_INTEGRITY_FAILED")
                raise
            if admission == "UNRESOLVED":
                raise Failure("CONSUMER_UNRESOLVED")
            if isinstance(admission, Denial):
                return self._finish(repo, run, admission.reason, admission.failure_code)
            for model in repo.models(run_id):
                inv = model.invocation
                if inv.durability_phase == "DISPATCH_INTENT_DURABLE":
                    # No owner; any former live path has been revoked/lost.
                    return self._finish(repo, run, "OUTCOME_UNKNOWN")
                if inv.durability_phase == "RESPONSE_DURABLE":
                    try:
                        response = repo.response(inv.invocation_id)
                        reader = self.formats.get(inv.response_format_key)
                        if reader is None:
                            return self._finish(repo, run, "FAILED", "RESPONSE_FORMAT_UNAVAILABLE")
                        try:
                            reader.validate(response.serialized_payload)
                        except (ValueError, TypeError):
                            return self._finish(repo, run, "FAILED", "RESPONSE_FORMAT_INVALID")
                    except Failure as exc:
                        if exc.code in (
                            "RESPONSE_PAYLOAD_UNAVAILABLE",
                            "RESPONSE_INTEGRITY_FAILED",
                        ):
                            code: FailureCode = (
                                "RESPONSE_PAYLOAD_UNAVAILABLE"
                                if exc.code == "RESPONSE_PAYLOAD_UNAVAILABLE"
                                else "RESPONSE_INTEGRITY_FAILED"
                            )
                            return self._finish(repo, run, "FAILED", code)
                        raise
                elif inv.response_format_key not in self.formats:
                    return self._finish(repo, run, "FAILED", "RESPONSE_FORMAT_UNAVAILABLE")
            if run.deadline_at is not None and self._now(run) >= run.deadline_at:
                models = repo.models(run_id)
                if (
                    not models
                    and not repo.tools(run_id)
                    or any(m.invocation.durability_phase == "PREPARED" for m in models)
                ):
                    return self._finish(repo, run, "TIMED_OUT")
            return None

        def truth(repo: Repository) -> Ending:
            return ending(repo.run(run_id))

        return self._result(lambda: self._write(write, truth), run_id)

    def recover_run(self, run_id: str) -> Result[Ending | None]:
        observed = self.read_run(run_id)
        if not isinstance(observed, Success):
            return observed
        run = observed.value
        if run.run_status == "ENDED":
            return Success(ending(run))
        # Healthy in-flight owners are not crash evidence.
        if run.owner_runtime_instance_id is not None:
            return Rejected("EXECUTION_NOT_CURRENT")
        coordinated = self.coordinate_ending(run_id, run.execution_generation)
        if not isinstance(coordinated, Success) or coordinated.value is not None:
            return coordinated
        grant = self.grant_execution(run_id, run.execution_generation)
        if not isinstance(grant, Success):
            return grant
        q = grant.value

        def resume(repo: Repository) -> None:
            current = self._current(repo, q)
            self._admit(repo, current)
            self._consumer(current).resume_local(repo, current)
            self.fault("local_result_written")

        def truth(repo: Repository) -> None:
            if (
                self._consumer(repo.run(run_id)).reconcile_result(repo, repo.run(run_id))
                != "COMPLETION_CONFIRMED"
            ):
                raise Failure("OUTCOME_UNKNOWN")

        resumed = self._result(lambda: self._write(resume, truth), run_id)
        if not isinstance(resumed, Success):
            return resumed
        completed = self.end_run(q, "COMPLETED")
        if isinstance(completed, Rejected) and completed.code == "COMPLETION_NOT_CONFIRMED":
            revoked = self.revoke_execution(q)
            if not isinstance(revoked, Success):
                return revoked
            return Success(None)
        return completed

    def startup(self) -> Result[list[Result[Ending | None]]]:
        if self.ready:
            return Rejected("RUNTIME_ALREADY_STARTED")
        try:

            def fence(repo: Repository) -> list[str]:
                runs = repo.open_runs()
                for run in runs:
                    repo.save_run(changed(run, owner_runtime_instance_id=None))
                return [r.run_id for r in runs]

            def truth(repo: Repository) -> list[str]:
                runs = repo.open_runs()
                if any(r.owner_runtime_instance_id is not None for r in runs):
                    raise Failure("OUTCOME_UNKNOWN")
                return [r.run_id for r in runs]

            identities = self._write(fence, truth)
            self.ready = True
            return Success([self.recover_run(identity) for identity in identities])
        except Failure as exc:
            return Unresolved(exc.code)


class _Oversized(Exception):
    pass
