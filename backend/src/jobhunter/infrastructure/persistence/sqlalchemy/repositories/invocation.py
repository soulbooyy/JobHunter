"""Exact-byte persistence. Caller owns the surrounding short authority transaction."""

import os
from collections.abc import Callable
from hashlib import sha256
from typing import TypeVar

from pydantic import ValidationError
from sqlalchemy.engine import Connection

from jobhunter.application.invocation.ports import Repository
from jobhunter.domain.invocation.models import (
    Descriptor,
    LocalRead,
    ModelInvocation,
    ModelRead,
    Response,
    Run,
    Value,
)
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

T = TypeVar("T", bound=Value)


class InvocationRepository:
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def _get(self, table: str, column: str, identity: str, model: type[T], missing: str) -> T:
        row = (
            self.conn.exec_driver_sql(f"SELECT * FROM {table} WHERE {column}=?", (identity,))
            .mappings()
            .first()
        )
        if row is None:
            raise Failure(missing)
        try:
            return model.model_validate(dict(row))
        except (ValueError, ValidationError):
            raise Failure("PERSISTENCE_INTEGRITY_FAILED") from None

    def _insert(self, table: str, record: Value) -> None:
        values = record.model_dump()
        if isinstance(record, ModelInvocation):
            # Byte limits have no Contract-wide upper ceiling. Preserve the
            # exact integer instead of SQLite INTEGER/REAL overflow or rounding.
            values["max_response_bytes"] = str(record.max_response_bytes)
        self.conn.exec_driver_sql(
            f"INSERT INTO {table} ({','.join(values)}) VALUES ({','.join('?' for _ in values)})",
            tuple(values.values()),
        )

    def run(self, run_id: str) -> Run:
        return self._get("agent_runs", "run_id", run_id, Run, "RUN_NOT_FOUND")

    def open_runs(self) -> list[Run]:
        ids = self.conn.exec_driver_sql(
            "SELECT run_id FROM agent_runs WHERE run_status='OPEN'"
        ).scalars()
        return [self.run(str(identity)) for identity in ids]

    def insert_run(self, run: Run) -> None:
        self._insert("agent_runs", run)

    def save_run(self, run: Run) -> None:
        old = self.run(run.run_id)
        if (old.consumer_key, old.created_at) != (run.consumer_key, run.created_at):
            raise Failure("PERSISTENCE_INTEGRITY_FAILED")
        if old.run_status == "ENDED" and old != run:
            raise Failure("RUN_ENDED")
        if old.deadline_at is not None and old.deadline_at != run.deadline_at:
            raise Failure("DEADLINE_FROZEN")
        values = run.model_dump(exclude={"run_id", "consumer_key", "created_at"})
        self.conn.exec_driver_sql(
            f"UPDATE agent_runs SET {','.join(k + '=?' for k in values)} WHERE run_id=?",
            (*values.values(), run.run_id),
        )

    def model(self, invocation_id: str) -> ModelRead:
        row = (
            self.conn.exec_driver_sql(
                "SELECT * FROM model_invocations WHERE invocation_id=?", (invocation_id,)
            )
            .mappings()
            .first()
        )
        if row is None:
            raise Failure("INVOCATION_NOT_FOUND")
        values = dict(row)
        descriptor = values.pop("descriptor")
        try:
            values["max_response_bytes"] = int(values["max_response_bytes"])
            invocation = ModelInvocation.model_validate(values)
            parsed = (
                Descriptor.model_validate_json(descriptor) if isinstance(descriptor, str) else None
            )
            if (parsed is None) != (invocation.durability_phase == "PREPARED"):
                raise ValueError("Invalid descriptor")
            self.run(invocation.run_id)
            return ModelRead(invocation=invocation, descriptor=parsed)
        except ValueError:
            raise Failure("PERSISTENCE_INTEGRITY_FAILED") from None

    def models(self, run_id: str) -> list[ModelRead]:
        return [
            self.model(str(i))
            for i in self.conn.exec_driver_sql(
                "SELECT invocation_id FROM model_invocations WHERE run_id=?", (run_id,)
            ).scalars()
        ]

    def insert_model(self, model: ModelRead) -> None:
        self._insert("model_invocations", model.invocation)

    def save_model(self, model: ModelRead) -> None:
        old = self.model(model.invocation.invocation_id)
        inv = model.invocation
        if old.invocation.model_dump(
            exclude={"durability_phase", "dispatch_generation", "response_rejection_code"}
        ) != inv.model_dump(
            exclude={"durability_phase", "dispatch_generation", "response_rejection_code"}
        ):
            raise Failure("PERSISTENCE_INTEGRITY_FAILED")
        if old.descriptor is not None and old.descriptor != model.descriptor:
            raise Failure("INTEGRITY_CONFLICT")
        phases = {"PREPARED": 0, "DISPATCH_INTENT_DURABLE": 1, "RESPONSE_DURABLE": 2}
        if phases[inv.durability_phase] < phases[old.invocation.durability_phase]:
            raise Failure("INTEGRITY_CONFLICT")
        if (
            old.invocation.dispatch_generation is not None
            and inv.dispatch_generation != old.invocation.dispatch_generation
        ):
            raise Failure("INTEGRITY_CONFLICT")
        if (
            old.invocation.response_rejection_code is not None
            and inv.response_rejection_code != old.invocation.response_rejection_code
        ):
            raise Failure("INTEGRITY_CONFLICT")
        self.conn.exec_driver_sql(
            "UPDATE model_invocations SET durability_phase=?,dispatch_generation=?,"
            "response_rejection_code=?,descriptor=? WHERE invocation_id=?",
            (
                inv.durability_phase,
                inv.dispatch_generation,
                inv.response_rejection_code,
                model.descriptor.model_dump_json() if model.descriptor else None,
                inv.invocation_id,
            ),
        )

    def response(self, invocation_id: str) -> Response:
        inv = self.model(invocation_id).invocation
        row = (
            self.conn.exec_driver_sql(
                "SELECT * FROM invocation_responses WHERE invocation_id=?", (invocation_id,)
            )
            .mappings()
            .first()
        )
        if row is None:
            raise Failure(
                "RESPONSE_PAYLOAD_UNAVAILABLE"
                if inv.durability_phase == "RESPONSE_DURABLE"
                else "RESPONSE_NOT_DURABLE"
            )
        try:
            response = Response.model_validate(dict(row))
        except ValueError:
            raise Failure("RESPONSE_INTEGRITY_FAILED") from None
        if (
            inv.durability_phase != "RESPONSE_DURABLE"
            or response.response_format_key != inv.response_format_key
        ):
            raise Failure("PERSISTENCE_INTEGRITY_FAILED")
        if (
            len(response.serialized_payload) != response.byte_length
            or sha256(response.serialized_payload).hexdigest() != response.sha256
        ):
            raise Failure("RESPONSE_INTEGRITY_FAILED")
        return response

    def insert_response(self, response: Response) -> None:
        self._insert("invocation_responses", response)

    def tools(self, run_id: str) -> list[LocalRead]:
        return [
            self.tool(str(i))
            for i in self.conn.exec_driver_sql(
                "SELECT invocation_id FROM controlled_local_reads WHERE run_id=?", (run_id,)
            ).scalars()
        ]

    def tool(self, invocation_id: str) -> LocalRead:
        return self._get(
            "controlled_local_reads",
            "invocation_id",
            invocation_id,
            LocalRead,
            "INVOCATION_NOT_FOUND",
        )

    def insert_tool(self, tool: LocalRead) -> None:
        self._insert("controlled_local_reads", tool)

    def save_tool(self, tool: LocalRead) -> None:
        old = self.tool(tool.invocation_id)
        if old.model_dump(exclude={"result_sha256", "result_byte_length"}) != tool.model_dump(
            exclude={"result_sha256", "result_byte_length"}
        ):
            raise Failure("REFERENCE_MISMATCH")
        if old.result_sha256 is not None and old != tool:
            raise Failure("INTEGRITY_CONFLICT")
        self.conn.exec_driver_sql(
            "UPDATE controlled_local_reads SET result_sha256=?,result_byte_length=? "
            "WHERE invocation_id=?",
            (tool.result_sha256, tool.result_byte_length, tool.invocation_id),
        )

    def proof_complete(self, run_id: str) -> bool:
        return (
            self.conn.exec_driver_sql(
                "SELECT 1 FROM controlled_model_proofs WHERE run_id=?", (run_id,)
            ).first()
            is not None
        )

    def complete_proof(self, run_id: str) -> None:
        self.conn.exec_driver_sql(
            "INSERT INTO controlled_model_proofs(run_id) VALUES (?)", (run_id,)
        )


class InvocationPersistence:
    def __init__(self, store: Store) -> None:
        self.store = store
        self.pid = os.getpid()

    def check_owner(self) -> None:
        if self.store.lock_fd < 0 or os.getpid() != self.pid:
            raise Failure("ACCESS_DENIED")

    def claim_runtime(self) -> None:
        self.check_owner()
        # One composition per Store lifetime, including competing constructors.
        with self.store.runtime_lock:
            if self.store.runtime_claimed:
                raise Failure("RUNTIME_ALREADY_STARTED")
            self.store.runtime_claimed = True

    def transact[T](self, operation: Callable[[Repository], T], *, write: bool = False) -> T:
        self.check_owner()
        return self.store.run(lambda conn: operation(InvocationRepository(conn)), write=write)
