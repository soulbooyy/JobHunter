"""Abrupt process exits at real dispatch/response/consumer transaction boundaries."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
from jobhunter.bootstrap.invocation import invocation_runtime
from jobhunter.domain.invocation.models import Success
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

SCRIPT = r"""
import json,os,sys
from pathlib import Path
from jobhunter.bootstrap.invocation import invocation_runtime
from jobhunter.domain.invocation.models import Success,Descriptor
from jobhunter.domain.invocation.format import FORMAT_KEY,ControlledResponse
from jobhunter.application.invocation.ports import Frame
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

def ok(r):
    assert isinstance(r,Success),r
    return r.value
class Clock:
    def utc(self): return '2026-09-23T12:00:00.000Z'
    def monotonic(self): return 0.0
class Gateway:
    def receive(self, descriptor, limit):
        with open(sys.argv[3],'a') as f:
            f.write('call\n'); f.flush(); os.fsync(f.fileno())
        yield Frame(ControlledResponse(terminal='STOP',text='private',ordinal=0).serialize(),True)
    def interrupt(self): pass
with Store.open(Path(sys.argv[1])) as store:
    rt=invocation_runtime(store,clock=Clock())
    run=ok(rt.create_run('controlled.model.v1','2026-09-23T12:01:00.000Z'))
    q=ok(rt.grant_execution(run,0))
    inv=ok(rt.prepare_model_invocation(q,FORMAT_KEY,1024))
    print(json.dumps({'run':run,'inv':inv}),flush=True)
    target=sys.argv[2]
    def fault(stage):
        if stage==target: os._exit(29)
        if stage=='response_written' and target=='response_committed':
            def commit(stage):
                if stage=='commit_after_driver': os._exit(29)
            store.fault=commit
        if stage=='intent_written' and target=='intent_committed':
            def commit(stage):
                if stage=='commit_after_driver': os._exit(29)
            store.fault=commit
    rt.fault=fault
    if target=='prepared': os._exit(29)
    with rt.model_path(inv,q):
        ok(rt.commit_dispatch_intent(inv,q,Descriptor(target='controlled.echo.v1',text='private',ordinal=0)))
        ok(rt.send(inv,q,Gateway()))
    os._exit(30)
"""


class FixedClock:
    def utc(self) -> str:
        return "2026-09-23T12:00:00.000Z"

    def monotonic(self) -> float:
        return 0


@pytest.mark.parametrize(
    "stage,calls,phase,reason",
    [
        ("prepared", 0, "PREPARED", None),
        ("intent_written", 0, "PREPARED", None),
        ("intent_committed", 0, "DISPATCH_INTENT_DURABLE", "OUTCOME_UNKNOWN"),
        ("before_adapter", 0, "DISPATCH_INTENT_DURABLE", "OUTCOME_UNKNOWN"),
        ("response_received", 1, "DISPATCH_INTENT_DURABLE", "OUTCOME_UNKNOWN"),
        ("response_written", 1, "DISPATCH_INTENT_DURABLE", "OUTCOME_UNKNOWN"),
        ("response_committed", 1, "RESPONSE_DURABLE", None),
    ],
)
def test_actual_process_crash_never_replays_remote_work(
    tmp_path: Path, stage: str, calls: int, phase: str, reason: str | None
) -> None:
    directory = tmp_path / "data"
    directory.mkdir()
    call_file = tmp_path / "calls"
    result = subprocess.run(
        [sys.executable, "-c", SCRIPT, str(directory), stage, str(call_file)],
        capture_output=True,
        timeout=15,
    )
    assert result.returncode == 29, result.stderr
    assert not result.stderr and b"private" not in result.stdout
    ids: dict[str, str] = json.loads(result.stdout)
    with Store.open(directory) as store:
        runtime = invocation_runtime(store, clock=FixedClock())
        run = runtime.read_run(ids["run"])
        inv = runtime.read_model_invocation(ids["inv"])
        assert isinstance(run, Success) and isinstance(inv, Success)
        assert run.value.end_reason == reason
        assert inv.value.invocation.durability_phase == phase
    assert (len(call_file.read_text().splitlines()) if call_file.exists() else 0) == calls
