"""Explicit controlled consumer agreements, not production business DTOs.

Model proof: exactly two MODEL responses, validated locally, then one durable
proof fact. Read proof: exactly one TOOL, reading one immutable MODEL response.
Concurrency is at most two models / one tool respectively. Deadline is required
before execution. Recovery is local only until deadline + 30 seconds (fixed UTC,
never renewed). No tool input is manufactured for an empty waiting Run.
Permission denial -> CONTROLLED_PERMISSION_DENIED; unavailable exact source ->
CONTROLLED_SOURCE_UNAVAILABLE; unknown action -> CONTROLLED_ACTION_UNAVAILABLE;
elapsed window -> TIMED_OUT. Malformed stored records are persistence integrity
failures, not consumer denials.
Unknown permission/storage -> UNRESOLVED. Audit-only lineage is never read.
"""

from collections.abc import Callable
from datetime import datetime, timedelta
from typing import Literal

from jobhunter.application.invocation.ports import Repository
from jobhunter.domain.invocation.format import FORMAT_KEY, decode
from jobhunter.domain.invocation.models import Admission, Denial, LocalRead, Reconciliation, Run
from jobhunter.domain.shared.errors import Failure

READ_ACTION = "controlled.response-read.v1"
type Permission = Literal["ALLOW", "DENY", "UNRESOLVED"]


def allow_local(run_id: str) -> Permission:
    return "ALLOW"


class ControlledFormat:
    key = FORMAT_KEY

    def validate(self, payload: bytes) -> None:
        decode(payload)


class ControlledConsumer:
    def __init__(
        self, kind: Literal["model", "read"], permission: Callable[[str], Permission] = allow_local
    ) -> None:
        self.key = "controlled." + kind + ".v1"
        self.max_models = 2 if kind == "model" else 0
        self.max_tools = 1 if kind == "read" else 0
        self.permission = permission

    def reconcile_result(self, repo: Repository, run: Run) -> Reconciliation:
        if self.max_models:
            return (
                "COMPLETION_CONFIRMED" if repo.proof_complete(run.run_id) else "RECOVERY_REQUIRED"
            )
        reads = repo.tools(run.run_id)
        if len(reads) == 1 and reads[0].result_sha256 is not None:
            # Durable result is self-contained digest/length evidence. No source
            # reread is needed just to recognize already-completed work.
            if reads[0].action_key != READ_ACTION:
                return "RECOVERY_REQUIRED"
            return "COMPLETION_CONFIRMED"
        return "RECOVERY_REQUIRED"

    def admit_recovery(self, repo: Repository, run: Run, now: str) -> Admission:
        permission = self.permission(run.run_id)
        if permission == "UNRESOLVED":
            return "UNRESOLVED"
        if permission == "DENY":
            return Denial("FAILED", "CONTROLLED_PERMISSION_DENIED")
        if run.deadline_at is None:
            return "UNRESOLVED"
        until = datetime.fromisoformat(run.deadline_at) + timedelta(seconds=30)
        if datetime.fromisoformat(now) >= until:
            return Denial("TIMED_OUT", None)
        for tool in repo.tools(run.run_id):
            if tool.action_key != READ_ACTION:
                return Denial("FAILED", "CONTROLLED_ACTION_UNAVAILABLE")
            if tool.result_sha256 is None:
                try:
                    repo.response(tool.source_invocation_id)
                except Failure as exc:
                    if exc.code in (
                        "INVOCATION_NOT_FOUND",
                        "RESPONSE_NOT_DURABLE",
                        "RESPONSE_PAYLOAD_UNAVAILABLE",
                    ):
                        return Denial("FAILED", "CONTROLLED_SOURCE_UNAVAILABLE")
                    raise
        return "ALLOW"

    def resume_local(self, repo: Repository, run: Run) -> None:
        if self.max_models:
            models = repo.models(run.run_id)
            if len(models) != 2 or any(
                m.invocation.durability_phase != "RESPONSE_DURABLE" for m in models
            ):
                return
            for model in models:
                decode(repo.response(model.invocation.invocation_id).serialized_payload)
            if not repo.proof_complete(run.run_id):
                repo.complete_proof(run.run_id)
        else:
            for tool in repo.tools(run.run_id):
                self.read(repo, tool)

    def read(self, repo: Repository, tool: LocalRead) -> LocalRead:
        if tool.action_key != READ_ACTION:
            raise Failure("CONTROLLED_ACTION_UNAVAILABLE")
        if tool.result_sha256 is not None:
            return tool
        source = repo.response(tool.source_invocation_id)
        result = LocalRead.model_validate(
            tool.model_dump()
            | {"result_sha256": source.sha256, "result_byte_length": source.byte_length}
        )
        repo.save_tool(result)
        return result
