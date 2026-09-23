from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timedelta
from hashlib import sha256
from pathlib import Path
from typing import Literal
from uuid import uuid4

import pytest
from jobhunter.agent.harness.runtime import Runtime
from jobhunter.application.invocation.controlled import ControlledConsumer, ControlledFormat
from jobhunter.application.invocation.ports import Frame
from jobhunter.bootstrap.invocation import invocation_runtime
from jobhunter.domain.invocation.format import FORMAT_KEY, ControlledResponse, decode
from jobhunter.domain.invocation.models import (
    Descriptor,
    Publication,
    Qualification,
    Rejected,
    Result,
    Success,
    Unresolved,
)
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault
from sqlalchemy.engine import Connection


def test_grant_revoke_and_cancel_are_durable(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store)
        created = runtime.create_run("controlled.model.v1", "2099-01-01T00:00:00.000Z")
        assert isinstance(created, Success)
        grant = runtime.grant_execution(created.value, 0)
        assert isinstance(grant, Success)
        assert grant.value.execution_generation == 1
        assert isinstance(runtime.revoke_execution(grant.value), Success)
        again = runtime.grant_execution(created.value, 1)
        assert isinstance(again, Success)
        assert again.value.execution_generation == 2
        assert isinstance(runtime.cancel_run(created.value), Success)
        assert not isinstance(runtime.revoke_execution(again.value), Success)


def ok[T](result: Result[T]) -> T:
    assert isinstance(result, Success), result
    return result.value


@dataclass
class TestClock:
    __test__ = False
    wall: str = "2026-09-23T12:00:00.000Z"
    elapsed: float = 0

    def utc(self) -> str:
        return self.wall

    def monotonic(self) -> float:
        return self.elapsed

    def advance(self, seconds: float) -> None:
        self.elapsed += seconds
        self.wall = (
            (datetime.fromisoformat(self.wall) + timedelta(seconds=seconds))
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )


class Echo:
    def __init__(self, *, payload: bytes | None = None, terminal: bool = True) -> None:
        self.calls = 0
        self.interrupted = 0
        self.payload = payload
        self.terminal = terminal

    def receive(self, descriptor: Descriptor, receive_limit: int) -> Iterable[Frame]:
        self.calls += 1
        payload = (
            self.payload
            if self.payload is not None
            else ControlledResponse(
                terminal="STOP", text=descriptor.text, ordinal=descriptor.ordinal
            ).serialize()
        )
        yield Frame(payload, self.terminal)

    def interrupt(self) -> None:
        self.interrupted += 1


def qualified(runtime: Runtime, key: str = "controlled.model.v1") -> Qualification:
    run_id = ok(runtime.create_run(key, "2026-09-23T12:01:00.000Z"))
    return ok(runtime.grant_execution(run_id, 0))


def prepared(runtime: Runtime, q: Qualification, limit: int = 1024) -> str:
    return ok(runtime.prepare_model_invocation(q, FORMAT_KEY, limit))


def request(text: str = 'exact 你好\n"\\', ordinal: int = 7) -> Descriptor:
    return Descriptor(target="controlled.echo.v1", text=text, ordinal=ordinal)


def deliver(
    runtime: Runtime, q: Qualification, inv: str, gateway: Echo | None = None
) -> Publication:
    with runtime.model_path(inv, q):
        ok(runtime.commit_dispatch_intent(inv, q, request()))
        return ok(runtime.send(inv, q, gateway or Echo()))


def test_format_golden_bytes_and_closed_shapes() -> None:
    value = ControlledResponse(
        terminal="LIMIT", text='你好\n"\\\t\u0000é', ordinal=9007199254740991
    )
    expected = (
        b'{"terminal":"LIMIT","text":"'
        + "你好".encode()
        + b'\\n\\"\\\\\\t\\u0000\xc3\xa9","ordinal":9007199254740991}'
    )
    assert value.serialize() == expected
    assert decode(expected) == value
    assert len(expected) == 79
    assert (
        sha256(expected).hexdigest()
        == "1d4fde6a91662bb035fff70d8edfde3e4f21ad4d0cfea558f0cf2b39768ecbea"
    )


@pytest.mark.parametrize(
    "payload",
    [
        b'{"text":"x","terminal":"STOP","ordinal":1}',
        b'{"terminal":"STOP","text":"x","ordinal":1.0}',
        b'{"terminal":"STOP","text":"x","ordinal":true}',
        b'{"terminal":"STOP","text":"x","ordinal":1,"ordinal":1}',
        b'{"terminal":"STOP","text":"\\ud800","ordinal":1}',
        b'{"terminal":"STOP","text":"x","ordinal":NaN}',
    ],
)
def test_noncanonical_response_is_rejected(payload: bytes) -> None:
    with pytest.raises(ValueError):
        decode(payload)


def test_actual_dispatch_bytes_read_only_confirmation_and_siblings(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        first, sibling = prepared(runtime, q), prepared(runtime, q)
        gateway = Echo()
        published = deliver(runtime, q, first, gateway)
        raw = ok(runtime.read_response(first))
        assert raw.byte_length == len(raw.serialized_payload)
        assert raw.sha256 == sha256(raw.serialized_payload).hexdigest()
        assert raw.publication() == published
        ended = ok(runtime.cancel_run(q.run_id))
        # Fails any attempted mutation or COMMIT on a write transaction. Confirmation
        # must still work with a reader removed and a stale generation after ending.
        runtime.formats.clear()
        assert ok(runtime.publish_response(first, q, raw.serialized_payload)) == published
        assert runtime.publish_response(first, q, b"different") == Rejected("INTEGRITY_CONFLICT")
        assert ok(runtime.cancel_run(q.run_id)) == ended
        with runtime.model_path(sibling, q):
            assert runtime.commit_dispatch_intent(sibling, q, request()) == Rejected("RUN_ENDED")
        assert gateway.calls == 1
        assert ok(runtime.read_model_invocation(sibling)).invocation.durability_phase == "PREPARED"


def test_grant_race_stale_revoke_and_overflow(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        identity = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))
        with ThreadPoolExecutor(max_workers=4) as pool:

            def grant(_: int) -> Result[Qualification]:
                return runtime.grant_execution(identity, 0)

            results = list(pool.map(grant, range(4)))
        winners = [r.value for r in results if isinstance(r, Success)]
        assert len(winners) == 1
        q = winners[0]
        ok(runtime.revoke_execution(q))
        q2 = ok(runtime.grant_execution(identity, 1))
        assert runtime.revoke_execution(q) == Rejected("EXECUTION_NOT_CURRENT")
        assert ok(runtime.read_run(identity)).owner_runtime_instance_id == q2.runtime_instance_id
        ok(runtime.revoke_execution(q2))
        store.run(
            lambda c: c.exec_driver_sql(
                "UPDATE agent_runs SET execution_generation=9007199254740991 WHERE run_id=?",
                (identity,),
            ),
            write=True,
        )
        assert runtime.grant_execution(identity, 9007199254740991) == Rejected(
            "GENERATION_EXHAUSTED"
        )


@pytest.mark.parametrize(
    "operation", ["create", "grant", "prepare", "intent", "response", "ending"]
)
@pytest.mark.parametrize("stage", ["commit_before_driver", "commit_after_driver"])
def test_commit_uncertainty_never_replays_commands(
    tmp_path: Path, operation: str, stage: str
) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run_id = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))
        q = None if operation in ("create", "grant") else ok(runtime.grant_execution(run_id, 0))
        inv = (
            prepared(runtime, q) if q is not None and operation in ("intent", "response") else None
        )
        commits = 0

        def fail(point: str) -> None:
            nonlocal commits
            if point == stage:
                commits += 1
                # Read reconciliation is allowed; fault only the first completion.
                if commits == 1:
                    raise OSError("secret payload SQL parameters")

        def execute() -> Result[object]:
            if operation == "create":
                return runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z")
            if operation == "grant":
                return runtime.grant_execution(run_id, 0)
            assert q is not None
            if operation == "prepare":
                return runtime.prepare_model_invocation(q, FORMAT_KEY, 1024)
            if operation == "ending":
                return runtime.cancel_run(run_id)
            assert inv is not None
            with runtime.model_path(inv, q):
                if operation == "intent":
                    return runtime.commit_dispatch_intent(inv, q, request())
                store.fault = no_fault
                ok(runtime.commit_dispatch_intent(inv, q, request()))

                def arm(point: str) -> None:
                    if point == "response_written":
                        store.fault = fail

                runtime.fault = arm
                return runtime.send(inv, q, Echo())

        # Reads before a publication/dispatch must not consume write faults.
        store.fault = fail
        result = execute()
        store.fault = no_fault
        if stage == "commit_after_driver":
            assert isinstance(result, Success), result
        else:
            assert isinstance(result, Unresolved), result
            assert result.identity is not None
        assert "secret" not in repr(result)


def test_original_uncertain_intent_winner_can_send_only_once(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)

        def arm(point: str) -> None:
            if point == "intent_written":

                def fail(stage: str) -> None:
                    if stage == "commit_after_driver":
                        store.fault = no_fault
                        raise OSError("ack lost")

                store.fault = fail

        runtime.fault = arm
        adapter = Echo()
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            ok(runtime.send(inv, q, adapter))
            assert runtime.send(inv, q, adapter) == Rejected("SENDING_PATH_UNAVAILABLE")
        assert adapter.calls == 1


def test_lost_path_and_new_generation_cannot_send_or_first_publish(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
        adapter = Echo()
        with runtime.model_path(inv, q):
            assert runtime.send(inv, q, adapter) == Rejected("SENDING_PATH_UNAVAILABLE")
            assert runtime.commit_dispatch_intent(inv, q, request()) == Rejected(
                "SENDING_PATH_UNAVAILABLE"
            )
        ok(runtime.revoke_execution(q))
        fresh = ok(runtime.grant_execution(q.run_id, 1))
        assert not isinstance(
            runtime.publish_response(
                inv, fresh, ControlledResponse(terminal="STOP", text="x", ordinal=0).serialize()
            ),
            Success,
        )
        assert adapter.calls == 0


@pytest.mark.parametrize("terminal,expected", [(True, "FAILED"), (False, "OUTCOME_UNKNOWN")])
def test_complete_oversize_and_interrupted_stream_are_distinct(
    tmp_path: Path, terminal: bool, expected: str
) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q, 20)
        adapter = Echo(terminal=terminal)
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            result = runtime.send(inv, q, adapter)
        assert not isinstance(result, Success)
        run = ok(runtime.read_run(q.run_id))
        assert run.end_reason == expected
        model = ok(runtime.read_model_invocation(inv)).invocation
        assert model.durability_phase == "DISPATCH_INTENT_DURABLE"
        assert model.response_rejection_code == ("RESPONSE_TOO_LARGE" if terminal else None)
        assert adapter.calls == 1


def test_receive_resource_cutoff_is_unknown_without_unbounded_drain(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q, 20)
        adapter = Echo(payload=b"x" * 1000, terminal=False)
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            assert not isinstance(runtime.send(inv, q, adapter), Success)
        assert ok(runtime.read_run(q.run_id)).end_reason == "OUTCOME_UNKNOWN"
        assert adapter.interrupted == 1


def test_local_recovery_after_deadline_and_whole_run_completion(tmp_path: Path) -> None:
    clock = TestClock()
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=clock)
        q = qualified(runtime)
        first = prepared(runtime, q)
        deliver(runtime, q, first)
        assert runtime.end_run(q, "COMPLETED") == Rejected("COMPLETION_NOT_CONFIRMED")
        second = prepared(runtime, q)
        deliver(runtime, q, second)
        ok(runtime.revoke_execution(q))
        clock.advance(65)
        result = ok(runtime.recover_run(q.run_id))
        assert result is not None and result.end_reason == "COMPLETED"
        assert ok(runtime.read_run(q.run_id)).deadline_at == "2026-09-23T12:01:00.000Z"


@pytest.mark.parametrize("advance", [61, 91])
def test_deadline_forbids_new_dispatch_and_bounds_recovery(tmp_path: Path, advance: int) -> None:
    clock = TestClock()
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=clock)
        q = qualified(runtime)
        inv = prepared(runtime, q)
        clock.advance(advance)
        adapter = Echo()
        with runtime.model_path(inv, q):
            assert not isinstance(runtime.commit_dispatch_intent(inv, q, request()), Success)
        ok(runtime.revoke_execution(q))
        result = ok(runtime.recover_run(q.run_id))
        assert result is not None and result.end_reason == "TIMED_OUT"
        assert adapter.calls == 0


def test_clock_rollback_does_not_renew_live_deadline_or_clamp_ending(tmp_path: Path) -> None:
    clock = TestClock()
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=clock)
        q = qualified(runtime)
        inv = prepared(runtime, q)
        clock.elapsed = 61
        clock.wall = "2025-01-01T00:00:00.000Z"
        with runtime.model_path(inv, q):
            assert runtime.commit_dispatch_intent(inv, q, request()) == Rejected("DEADLINE_EXPIRED")
        ended = ok(runtime.cancel_run(q.run_id))
        assert ended.ended_at < ok(runtime.read_run(q.run_id)).created_at


@pytest.mark.parametrize(
    "damage,expected",
    [
        ("missing", "RESPONSE_PAYLOAD_UNAVAILABLE"),
        ("bytes", "RESPONSE_INTEGRITY_FAILED"),
        ("reader", "RESPONSE_FORMAT_UNAVAILABLE"),
        ("format", "RESPONSE_FORMAT_INVALID"),
        ("consumer", "CONSUMER_UNAVAILABLE"),
    ],
)
def test_recovery_dependency_failures_are_scoped(
    tmp_path: Path, damage: str, expected: str
) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        deliver(runtime, q, inv)
        ok(runtime.revoke_execution(q))
        if damage == "missing":
            store.run(
                lambda c: c.exec_driver_sql(
                    "DELETE FROM invocation_responses WHERE invocation_id=?", (inv,)
                ),
                write=True,
            )
        elif damage == "bytes":
            store.run(
                lambda c: c.exec_driver_sql(
                    "UPDATE invocation_responses SET serialized_payload=x'00' "
                    "WHERE invocation_id=?",
                    (inv,),
                ),
                write=True,
            )
        elif damage == "reader":
            runtime.formats.clear()
        elif damage == "consumer":
            runtime.consumers.clear()
        else:
            payload = b"{}"
            store.run(
                lambda c: c.exec_driver_sql(
                    "UPDATE invocation_responses SET serialized_payload=?,sha256=?,byte_length=? "
                    "WHERE invocation_id=?",
                    (payload, sha256(payload).hexdigest(), len(payload), inv),
                ),
                write=True,
            )
        result = ok(runtime.recover_run(q.run_id))
        assert result is not None and result.failure_code == expected
        assert (
            ok(runtime.read_model_invocation(inv)).invocation.durability_phase == "RESPONSE_DURABLE"
        )


def test_failed_terminal_write_and_unavailable_storage_remain_unresolved(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        ok(runtime.revoke_execution(q))
        runtime.consumers.clear()

        def fail(point: str) -> None:
            if point == "ending_written":
                raise OSError("sensitive payload")

        runtime.fault = fail
        result = runtime.recover_run(q.run_id)
        assert isinstance(result, Unresolved)
        assert ok(runtime.read_run(q.run_id)).run_status == "OPEN"

        def unreadable(point: str) -> None:
            raise OSError("sensitive SQL")

        store.fault = unreadable
        assert isinstance(runtime.read_run(q.run_id), Unresolved)
        store.fault = no_fault
        assert ok(runtime.read_run(q.run_id)).run_status == "OPEN"


def test_pure_exact_local_read_recovers_same_invocation_and_ignores_lineage(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        model_q = qualified(runtime)
        source = prepared(runtime, model_q)
        deliver(runtime, model_q, source)
        q = qualified(runtime, "controlled.read.v1")
        tool = ok(runtime.prepare_local_read(q, source, str(uuid4())))
        ok(runtime.revoke_execution(q))
        newer = ok(runtime.grant_execution(q.run_id, 1))
        result = ok(runtime.resume_local_read(tool, newer))
        assert result.invocation_id == tool and result.source_invocation_id == source
        assert result.result_sha256 == ok(runtime.read_response(source)).sha256
        assert ok(runtime.resume_local_read(tool, newer)) == result
        assert ok(runtime.end_run(newer, "COMPLETED")).end_reason == "COMPLETED"
        assert (
            store.run(
                lambda c: c.exec_driver_sql("SELECT count(*) FROM controlled_local_reads").scalar()
            )
            == 1
        )


def test_completion_skips_unneeded_payload_read(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        for _ in range(2):
            deliver(runtime, q, prepared(runtime, q))
        ok(runtime.revoke_execution(q))
        # Simulate crash after the consumer proof committed but before ending.
        store.run(
            lambda c: c.exec_driver_sql(
                "INSERT INTO controlled_model_proofs VALUES (?)", (q.run_id,)
            ),
            write=True,
        )
        store.run(lambda c: c.exec_driver_sql("DELETE FROM invocation_responses"), write=True)
        runtime.formats.clear()
        result = ok(runtime.recover_run(q.run_id))
        assert result is not None and result.end_reason == "COMPLETED"


def test_startup_fences_previous_owner_and_preserves_prepared(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        old_instance = runtime.runtime_instance_id
    with Store.open(tmp_path) as store:
        restarted = invocation_runtime(store, clock=TestClock())
        assert restarted.runtime_instance_id != old_instance
        assert ok(restarted.read_model_invocation(inv)).invocation.durability_phase == "PREPARED"
        assert restarted.revoke_execution(q) == Rejected("EXECUTION_NOT_CURRENT")
        run = ok(restarted.read_run(q.run_id))
        fresh = ok(restarted.grant_execution(q.run_id, run.execution_generation))
        adapter = Echo()
        deliver(restarted, fresh, inv, adapter)
        assert adapter.calls == 1


def test_startup_lost_intent_never_replays_and_empty_run_is_not_corruption(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
        empty = ok(runtime.create_run("controlled.read.v1", None))
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        assert ok(runtime.read_run(q.run_id)).end_reason == "OUTCOME_UNKNOWN"
        assert ok(runtime.read_run(empty)).run_status == "OPEN"
        assert ok(runtime.read_run(empty)).execution_generation == 0


def test_denial_and_unresolved_permission_are_not_permission(tmp_path: Path) -> None:
    consumer = ControlledConsumer("model", lambda _: "UNRESOLVED")
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock(), consumers=[consumer])
        run = ok(runtime.create_run(consumer.key, "2026-09-23T12:01:00.000Z"))
        assert isinstance(runtime.grant_execution(run, 0), Unresolved)
        assert isinstance(runtime.recover_run(run), Unresolved)

        def deny(_: str) -> Literal["DENY"]:
            return "DENY"

        consumer.permission = deny
        result = ok(runtime.recover_run(run))
        assert result is not None and result.failure_code == "CONTROLLED_PERMISSION_DENIED"


def test_deadline_is_write_once_and_null_is_not_permission(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.create_run("controlled.model.v1", None))
        assert isinstance(runtime.grant_execution(run, 0), Unresolved)
        deadline = "2026-09-23T12:01:00.000Z"
        assert ok(runtime.establish_deadline(run, deadline)) == deadline
        assert ok(runtime.establish_deadline(run, deadline)) == deadline
        assert runtime.establish_deadline(run, "2099-01-01T00:00:00.000Z") == Rejected(
            "DEADLINE_FROZEN"
        )
        ok(runtime.cancel_run(run))
        assert ok(runtime.establish_deadline(run, deadline)) == deadline


def test_duplicate_registration_and_closed_store_fail_before_execution(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        with pytest.raises(Failure, match="DUPLICATE"):
            invocation_runtime(store, formats=[ControlledFormat(), ControlledFormat()])
        runtime = invocation_runtime(store, clock=TestClock())
    assert runtime.create_run("controlled.model.v1", None) == Rejected("ACCESS_DENIED")


@pytest.mark.parametrize("action", ["cancel", "revoke", "deadline"])
def test_response_late_callback_after_cancel_revoke_or_deadline(
    tmp_path: Path, action: str
) -> None:
    directory = tmp_path / action
    directory.mkdir()
    clock = TestClock()
    with Store.open(directory) as store:
        runtime = invocation_runtime(store, clock=clock)
        q = qualified(runtime)
        inv = prepared(runtime, q)
        adapter = Echo()

        def interfere(stage: str) -> None:
            if stage == "response_received":
                if action == "cancel":
                    ok(runtime.cancel_run(q.run_id))
                elif action == "revoke":
                    ok(runtime.revoke_execution(q))
                    ok(runtime.grant_execution(q.run_id, 1))
                else:
                    clock.advance(61)

        runtime.fault = interfere
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            assert not isinstance(runtime.send(inv, q, adapter), Success)
        assert adapter.calls == 1
        assert runtime.read_response(inv) == Rejected("RESPONSE_NOT_DURABLE")
        assert ok(runtime.read_model_invocation(inv)).invocation.dispatch_generation == 1


def test_competing_confirmations_are_exact_and_write_free(tmp_path: Path) -> None:
    from sqlalchemy import event
    from sqlalchemy.engine import Connection
    from sqlalchemy.engine.default import DefaultExecutionContext
    from sqlalchemy.engine.interfaces import DBAPICursor

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        published = deliver(runtime, q, inv)
        payload = ok(runtime.read_response(inv)).serialized_payload
        ok(runtime.cancel_run(q.run_id))
        statements: list[str] = []

        def observe(
            conn: Connection,
            cursor: DBAPICursor,
            statement: str,
            parameters: object,
            context: DefaultExecutionContext,
            executemany: bool,
        ) -> None:
            statements.append(statement.split()[0].upper())

        event.listen(store.engine, "before_cursor_execute", observe)

        def confirm(index: int) -> Result[Publication]:
            return runtime.publish_response(inv, q, payload if index % 2 == 0 else b"different")

        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(confirm, range(12)))
        assert all(
            result == (Success(published) if index % 2 == 0 else Rejected("INTEGRITY_CONFLICT"))
            for index, result in enumerate(results)
        )
        assert not {"INSERT", "UPDATE", "DELETE"}.intersection(statements)


def test_unavailable_writer_prevents_dispatch_and_converges(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        runtime.formats.clear()
        with runtime.model_path(inv, q):
            assert runtime.commit_dispatch_intent(inv, q, request()) == Rejected(
                "RESPONSE_FORMAT_UNAVAILABLE"
            )
        assert ok(runtime.read_run(q.run_id)).failure_code == "RESPONSE_FORMAT_UNAVAILABLE"


@pytest.mark.parametrize("damage", ["permission", "source", "action"])
def test_controlled_read_recovery_denials(tmp_path: Path, damage: str) -> None:
    reader = ControlledConsumer("read")
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(
            store, clock=TestClock(), consumers=[ControlledConsumer("model"), reader]
        )
        q = qualified(runtime)
        source = prepared(runtime, q)
        deliver(runtime, q, source)
        read_q = qualified(runtime, reader.key)
        tool = ok(runtime.prepare_local_read(read_q, source, str(uuid4())))
        ok(runtime.revoke_execution(read_q))
        if damage == "source":
            store.run(
                lambda c: c.exec_driver_sql(
                    "DELETE FROM invocation_responses WHERE invocation_id=?", (source,)
                ),
                write=True,
            )
        elif damage == "action":
            store.run(
                lambda c: c.exec_driver_sql(
                    "UPDATE controlled_local_reads SET action_key='unknown.v1' "
                    "WHERE invocation_id=?",
                    (tool,),
                ),
                write=True,
            )
        else:

            def deny(_: str) -> Literal["DENY"]:
                return "DENY"

            reader.permission = deny
        result = ok(runtime.recover_run(read_q.run_id))
        assert result is not None
        assert (
            result.failure_code
            == {
                "permission": "CONTROLLED_PERMISSION_DENIED",
                "source": "CONTROLLED_SOURCE_UNAVAILABLE",
                "action": "CONTROLLED_ACTION_UNAVAILABLE",
            }[damage]
        )
        assert (
            store.run(
                lambda c: c.exec_driver_sql(
                    "SELECT result_sha256 FROM controlled_local_reads WHERE invocation_id=?",
                    (tool,),
                ).scalar()
            )
            is None
        )


def test_payloads_of_all_open_and_ended_runs_remain_retained(tmp_path: Path) -> None:
    expected: dict[str, bytes] = {}
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        for cancel in (False, True):
            q = qualified(runtime)
            for _ in range(2):
                inv = prepared(runtime, q)
                deliver(runtime, q, inv)
                expected[inv] = ok(runtime.read_response(inv)).serialized_payload
            if cancel:
                ok(runtime.cancel_run(q.run_id))
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        assert {
            identity: ok(runtime.read_response(identity)).serialized_payload
            for identity in expected
        } == expected


def test_live_path_cannot_transfer_to_other_thread_or_async_task(tmp_path: Path) -> None:
    import asyncio
    import contextvars
    from copy import copy, deepcopy

    from jobhunter.agent.harness.runtime import LivePath

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        path = LivePath(inv, q)
        for clone in (copy, deepcopy):
            with pytest.raises(TypeError):
                clone(path)

        async def exercise() -> None:
            with runtime.model_path(inv, q):
                ok(runtime.commit_dispatch_intent(inv, q, request()))
                adapter = Echo()

                async def other() -> Result[Publication]:
                    return runtime.send(inv, q, adapter)

                assert await asyncio.create_task(other()) == Rejected("SENDING_PATH_UNAVAILABLE")
                context = contextvars.copy_context()
                with ThreadPoolExecutor(max_workers=1) as pool:
                    result = pool.submit(context.run, runtime.send, inv, q, adapter).result()
                assert result == Rejected("SENDING_PATH_UNAVAILABLE")
                ok(runtime.send(inv, q, adapter))
                assert adapter.calls == 1

        asyncio.run(exercise())


def test_grant_acknowledgement_proof_cannot_be_manufactured_from_row(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))

        def fail(stage: str) -> None:
            if stage == "commit_after_driver":
                store.fault = no_fault
                raise OSError("lost acknowledgement")

        store.fault = fail
        original = ok(runtime.grant_execution(run, 0))
        assert original.execution_generation == 1
        assert runtime.grant_execution(run, 0) == Rejected("EXECUTION_NOT_CURRENT")
        assert runtime.grant_execution(run, 1) == Rejected("EXECUTION_NOT_CURRENT")
        assert ok(runtime.read_run(run)).execution_generation == 1


def test_ownerless_ending_and_grant_arbitrate_atomically(tmp_path: Path) -> None:
    from threading import Barrier

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        for _ in range(2):
            deliver(runtime, q, prepared(runtime, q))
        ok(runtime.revoke_execution(q))
        store.run(
            lambda c: c.exec_driver_sql(
                "INSERT INTO controlled_model_proofs VALUES (?)", (q.run_id,)
            ),
            write=True,
        )
        barrier = Barrier(2)

        def coordinate() -> Result[object]:
            barrier.wait()
            return runtime.coordinate_ending(q.run_id, 1)

        def grant() -> Result[object]:
            barrier.wait()
            return runtime.grant_execution(q.run_id, 1)

        with ThreadPoolExecutor(max_workers=2) as pool:
            a, b = pool.submit(coordinate), pool.submit(grant)
            results = [a.result(), b.result()]
        assert sum(isinstance(r, Success) for r in results) == 1


@pytest.mark.parametrize(
    "field,value", [("generation", True), ("generation", -1), ("bytes", False), ("bytes", 0)]
)
def test_internal_scalar_admission_is_exact(tmp_path: Path, field: str, value: int) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        if field == "generation":
            result = runtime.grant_execution(q.run_id, value)
        else:
            result = runtime.prepare_model_invocation(q, FORMAT_KEY, value)
        assert result == Rejected("INVALID_INPUT")


def test_cancellation_wins_before_adapter_entry(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        adapter = Echo()

        def cancel(stage: str) -> None:
            if stage == "before_adapter":
                ok(runtime.cancel_run(q.run_id))

        runtime.fault = cancel
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            assert runtime.send(inv, q, adapter) == Rejected("RUN_ENDED")
        assert adapter.calls == 0


def test_structurally_invalid_run_is_not_repaired_or_ended(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)

        def damage(conn: Connection) -> None:
            conn.exec_driver_sql("PRAGMA ignore_check_constraints=ON")
            conn.exec_driver_sql(
                "UPDATE agent_runs SET execution_generation=-1 WHERE run_id=?", (q.run_id,)
            )

        store.run(damage, write=True)
        assert runtime.read_run(q.run_id) == Rejected("PERSISTENCE_INTEGRITY_FAILED")
        assert runtime.cancel_run(q.run_id) == Rejected("PERSISTENCE_INTEGRITY_FAILED")


def test_runtime_busy_commit_is_not_success_or_command_replay(tmp_path: Path) -> None:
    import sqlite3

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))
        reader = sqlite3.connect(tmp_path / "jobhunter.sqlite3", isolation_level=None)
        reader.execute("BEGIN")
        reader.execute("SELECT * FROM agent_runs").fetchall()
        try:
            result = runtime.grant_execution(run, 0)
            assert isinstance(result, Unresolved) and result.code == "STORAGE_UNAVAILABLE"
        finally:
            reader.close()
        assert ok(runtime.read_run(run)).execution_generation == 0


def test_rollback_failure_retains_commit_uncertainty(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))
        original = Connection.rollback
        failures = 0

        def rollback(conn: Connection) -> None:
            nonlocal failures
            failures += 1
            if failures == 1:
                raise OSError("private rollback failure")
            original(conn)

        def fail(stage: str) -> None:
            if stage == "grant_written":
                monkeypatch.setattr(Connection, "rollback", rollback)
                raise OSError("private grant failure")

        runtime.fault = fail
        result = runtime.grant_execution(run, 0)
        assert isinstance(result, Unresolved) and result.code == "OUTCOME_UNKNOWN"
        assert ok(runtime.read_run(run)).execution_generation == 0
        assert "private" not in repr(result)


@pytest.mark.parametrize("committed", [False, True])
def test_local_read_restart_reuses_or_reexecutes_same_exact_input(
    tmp_path: Path, committed: bool
) -> None:
    original = None
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        source = prepared(runtime, q)
        adapter = Echo()
        deliver(runtime, q, source, adapter)
        rq = qualified(runtime, "controlled.read.v1")
        tool_id = ok(runtime.prepare_local_read(rq, source, str(uuid4())))
        if committed:
            original = ok(runtime.resume_local_read(tool_id, rq))
        assert adapter.calls == 1
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.read_run(rq.run_id))
        assert run.end_reason == "COMPLETED"
        from jobhunter.infrastructure.persistence.sqlalchemy.repositories.invocation import (
            InvocationRepository,
        )

        restored = store.run(lambda c: InvocationRepository(c).tool(tool_id))
        assert restored.source_invocation_id == source
        assert restored.result_sha256 == ok(runtime.read_response(source)).sha256
        if committed:
            assert restored == original
        assert (
            store.run(
                lambda c: c.exec_driver_sql("SELECT count(*) FROM controlled_local_reads").scalar()
            )
            == 1
        )


def test_full_response_bound_includes_envelope_and_exact_limit(tmp_path: Path) -> None:
    payload = ControlledResponse(terminal="STOP", text="", ordinal=0).serialize()
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        for size in (len(payload), len(payload) - 1):
            q = qualified(runtime)
            inv = prepared(runtime, q, size)
            with runtime.model_path(inv, q):
                ok(runtime.commit_dispatch_intent(inv, q, request()))
                result = runtime.send(inv, q, Echo(payload=payload))
            assert isinstance(result, Success) == (size == len(payload))


def test_empty_nonterminal_frames_are_bounded(tmp_path: Path) -> None:
    class EmptyGateway(Echo):
        frames = 0

        def receive(self, descriptor: Descriptor, receive_limit: int) -> Iterable[Frame]:
            self.calls += 1
            while True:
                self.frames += 1
                yield Frame(b"", False)

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q, 10)
        gateway = EmptyGateway()
        with runtime.model_path(inv, q):
            ok(runtime.commit_dispatch_intent(inv, q, request()))
            assert runtime.send(inv, q, gateway) == Rejected("REMOTE_OUTCOME_UNKNOWN")
        assert gateway.calls == 1 and gateway.frames == 12
        assert ok(runtime.read_run(q.run_id)).end_reason == "OUTCOME_UNKNOWN"


def test_persistence_cannot_downgrade_or_transfer_dispatch_generation(tmp_path: Path) -> None:
    from jobhunter.domain.invocation.models import ModelInvocation, ModelRead
    from jobhunter.infrastructure.persistence.sqlalchemy.repositories.invocation import (
        InvocationRepository,
    )

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        inv = prepared(runtime, q)
        deliver(runtime, q, inv)
        model = ok(runtime.read_model_invocation(inv))
        for change in ({"dispatch_generation": 2}, {"durability_phase": "DISPATCH_INTENT_DURABLE"}):
            altered = ModelRead(
                invocation=ModelInvocation.model_validate(model.invocation.model_dump() | change),
                descriptor=model.descriptor,
            )
            with pytest.raises(Failure, match="INTEGRITY_CONFLICT"):
                store.run(
                    lambda conn, altered=altered: InvocationRepository(conn).save_model(altered),
                    write=True,
                )
        assert ok(runtime.read_model_invocation(inv)) == model


def test_uncertain_grant_cannot_adopt_competitors_identical_authority(tmp_path: Path) -> None:
    from threading import Event

    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        run = ok(runtime.create_run("controlled.model.v1", "2026-09-23T12:01:00.000Z"))
        compete, finished = Event(), Event()
        observed_rival: list[bool] = []

        def rival() -> Result[Qualification]:
            assert compete.wait(2)
            try:
                return runtime.grant_execution(run, 0)
            finally:
                finished.set()

        def no_commit(stage: str) -> None:
            if stage == "commit_before_driver":
                store.fault = no_fault
                raise OSError("acknowledgement unknown before driver")

        def interleave(stage: str) -> None:
            if stage == "grant_reconciliation":
                compete.set()
                # Without the live arbitration guard, the competing grant can
                # commit the exact same persisted qualification during this gap.
                observed_rival.append(finished.wait(0.1))

        runtime.fault = interleave
        store.fault = no_commit
        with ThreadPoolExecutor(max_workers=1) as pool:
            competing = pool.submit(rival)
            original = runtime.grant_execution(run, 0)
            other = competing.result(timeout=2)
        assert observed_rival == [False]
        assert isinstance(original, Unresolved) and original.code == "OUTCOME_UNKNOWN"
        assert isinstance(other, Success) and other.value.execution_generation == 1


def test_captured_byte_limit_is_exact_beyond_sqlite_integer_range(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        runtime = invocation_runtime(store, clock=TestClock())
        q = qualified(runtime)
        limit = 10**40 + 1
        inv = prepared(runtime, q, limit)
        assert ok(runtime.read_model_invocation(inv)).invocation.max_response_bytes == limit
        assert store.run(
            lambda c: c.exec_driver_sql(
                "SELECT max_response_bytes FROM model_invocations WHERE invocation_id=?", (inv,)
            ).scalar()
        ) == str(limit)
        deliver(runtime, q, inv)
