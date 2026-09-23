"""Admission ordering, retained receipts and exact-pair concurrency in real SQLite."""

from pathlib import Path
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.application.materials.service import Materials
from jobhunter.domain.derived_work.models import RenderRequest
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.materials import (
    MaterialsRepository,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault


def configuration() -> RenderConfiguration:
    roles = dict.fromkeys(("regular", "bold", "italic", "bold_italic"), "a" * 64)
    return RenderConfiguration.model_validate(
        {
            "render_configuration_id": str(uuid4()),
            "schema_version": 1,
            "template": {"template_key": "test_fixture", "template_version": "1"},
            "renderer": {"pipeline_key": "test_fixture", "pipeline_version": "1"},
            "fonts": dict.fromkeys(("HEITI", "SONGTI", "KAITI", "SOURCE_HAN_SANS"), roles),
            "output": {"media_type": "application/pdf"},
        }
    )


def source(store: Store) -> str:
    candidate = CandidateAuthority(store)
    saved = candidate.command(
        "RESUME_CREATE",
        {
            "request_id": str(uuid4()),
            "resume_name": "Local",
            "profile_version_id": candidate.pair("profile")["profile_version"][
                "profile_version_id"
            ],
            "header_presentation": {"optional_items": []},
            "sections": [],
            "document_presentation": {
                "font_family": "HEITI",
                "font_size_pt": 12,
                "line_spacing_pt": 14,
                "theme_color": "#000000",
            },
        },
    )
    return saved["resume_version"]["resume_version_id"]


def test_replay_precedes_current_capability_and_new_demand_joins(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        joined = service.request(command.model_copy(update={"request_id": str(uuid4())}))
        assert accepted["render_intent_id"] != joined["render_intent_id"]
        assert (
            store.run(
                lambda conn: conn.exec_driver_sql("SELECT count(*) FROM render_work").scalar()
            )
            == 1
        )
        service.capability = lambda _: False
        assert service.request(command) == accepted
        with pytest.raises(Failure, match="RENDER_CONFIGURATION_UNAVAILABLE"):
            service.request(command.model_copy(update={"request_id": str(uuid4())}))
        with pytest.raises(Failure, match="REQUEST_CONFLICT"):
            service.request(command.model_copy(update={"resume_version_id": str(uuid4())}))


def test_preflight_fails_without_attempt_and_recovery_fences_old_attempt(tmp_path: Path) -> None:
    from jobhunter.application.materials.coordinator import Coordinator

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        request = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        intent = service.request(request)
        coordinator = Coordinator(service)
        identity = coordinator.queued()[0]
        service.capability = lambda _: False
        assert coordinator.claim(identity) is None
        work = store.run(lambda conn: MaterialsRepository(conn).work(identity))
        assert (work["status"], work["attempt_count"], work["failure_code"]) == (
            "FAILED",
            0,
            "CONFIGURATION_UNAVAILABLE",
        )
        assert (
            service.intent(intent["render_intent_id"])["failure_code"]
            == "CONFIGURATION_UNAVAILABLE"
        )
        service.capability = lambda _: True
        service.request(request.model_copy(update={"request_id": str(uuid4())}))
        old = coordinator.claim(coordinator.queued()[0])
        assert old is not None
        coordinator.recover_after_ownership()
        new = coordinator.claim(old.work_id)
        assert new is not None and new.current_attempt_id != old.current_attempt_id
        assert new.attempt_count == 2
        assert coordinator.fail(old, "RENDER_FAILED") is False
        assert coordinator.fail(new, "RENDER_FAILED") is True


def test_publish_reuse_snapshot_loss_and_uncertain_commit(tmp_path: Path) -> None:
    from jobhunter.application.materials.coordinator import Coordinator

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        second = service.request(command.model_copy(update={"request_id": str(uuid4())}))
        coordinator = Coordinator(service)
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None
        # This test owns orchestration/file integrity only, not PDF conformance.
        payload = b"controlled already-validated renderer result"
        assert coordinator.publish(work, payload)
        result = service.intent(accepted["render_intent_id"])
        assert result["status"] == "FULFILLED"
        assert service.intent(second["render_intent_id"])["artifact_id"] == result["artifact_id"]
        reuse = service.request(command.model_copy(update={"request_id": str(uuid4())}))
        assert service.intent(reuse["render_intent_id"])["artifact_id"] == result["artifact_id"]
        _, snapshot = service.content(result["artifact_id"])
        path = tmp_path / "artifacts" / result["artifact_id"]
        path.write_bytes(b"changed")
        with snapshot:
            assert snapshot.read() == payload
        with pytest.raises(Failure, match="ARTIFACT_INTEGRITY_FAILED"):
            service.content(result["artifact_id"])
        path.unlink()
        assert service.artifact(result["artifact_id"])["byte_length"] == len(payload)
        assert service.request(command) == accepted
        new = service.request(command.model_copy(update={"request_id": str(uuid4())}))
        assert service.intent(new["render_intent_id"])["status"] == "PENDING"
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None

        def uncertain(stage: str) -> None:
            if stage == "commit_after_driver":
                raise OSError("private failure")

        store.fault = uncertain
        with pytest.raises(Failure, match="OUTCOME_UNKNOWN"):
            coordinator.publish(work, payload)
        store.fault = no_fault
        assert service.intent(new["render_intent_id"])["status"] == "FULFILLED"
    with Store.open(tmp_path) as reopened:
        assert Materials(reopened).request(command) == accepted


def test_receipt_and_demand_rollback_together(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )

        def fail(stage: str) -> None:
            if stage == "before_commit":
                raise OSError("private failure")

        store.fault = fail
        with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
            service.request(command)
        store.fault = no_fault
        for table in ("render_work", "render_intents", "material_command_receipts"):
            assert (
                store.run(
                    lambda conn, table=table: conn.exec_driver_sql(
                        "SELECT count(*) FROM " + table
                    ).scalar()
                )
                == 0
            )
        assert service.request(command)["outcome"] == "ACCEPTED"


def test_same_request_and_target_concurrency(tmp_path: Path) -> None:
    from concurrent.futures import ThreadPoolExecutor

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        with ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(service.request, command) for _ in range(8)]
            results = [future.result() for future in futures]
            assert all(result == results[0] for result in results)
            futures = [
                pool.submit(
                    service.request, command.model_copy(update={"request_id": str(uuid4())})
                )
                for _ in range(8)
            ]
            assert len({future.result()["render_intent_id"] for future in futures}) == 8
        assert (
            store.run(
                lambda conn: conn.exec_driver_sql("SELECT count(*) FROM render_work").scalar()
            )
            == 1
        )
        assert (
            store.run(
                lambda conn: conn.exec_driver_sql("SELECT count(*) FROM render_intents").scalar()
            )
            == 9
        )


def test_captured_limit_survives_restarts_and_exhaustion(tmp_path: Path) -> None:
    from jobhunter.application.materials.coordinator import Coordinator
    from jobhunter.application.materials.service import defaults
    from jobhunter.domain.derived_work.models import Limits

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(
            store,
            capability=lambda _: True,
            limits=lambda: Limits.model_validate({**defaults().model_dump(), "max_attempts": 1}),
        )
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        coordinator = Coordinator(service)
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None and work.max_attempts == 1
    with Store.open(tmp_path) as reopened:
        service = Materials(reopened, capability=lambda _: True)
        coordinator = Coordinator(service)
        coordinator.recover_after_ownership()
        assert service.intent(accepted["render_intent_id"])["failure_code"] == "RECOVERY_EXHAUSTED"
        assert service.request(command) == accepted


@pytest.mark.parametrize(
    "program,expected",
    [
        ("import time;time.sleep(30)", "RESOURCE_LIMIT_EXCEEDED"),
        ("import os,sys;os.write(int(sys.argv[1]),b'invalid');print('OK')", "OUTPUT_INVALID"),
    ],
)
def test_timeout_or_invalid_candidate_never_publishes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, program: str, expected: str
) -> None:
    import subprocess
    import sys
    from typing import Any, cast

    from jobhunter.application.materials.coordinator import Coordinator
    from jobhunter.application.materials.runner import Runner
    from jobhunter.application.materials.service import defaults
    from jobhunter.domain.derived_work.models import Limits
    from jobhunter.infrastructure.rendering.catalog import ASSETS, environment

    actual = subprocess.Popen
    children: list[subprocess.Popen[bytes]] = []

    def slow(args: object, **kwargs: Any) -> subprocess.Popen[bytes]:
        child = cast(
            "subprocess.Popen[bytes]",
            actual([sys.executable, "-c", program, cast(list[str], args)[3]], **kwargs),
        )
        children.append(child)
        return child

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(
            store,
            capability=lambda _: True,
            limits=lambda: Limits.model_validate(
                {
                    **defaults().model_dump(),
                    "timeout_ms": 100 if expected == "RESOURCE_LIMIT_EXCEEDED" else 2000,
                }
            ),
        )
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        coordinator = Coordinator(service)
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None
        monkeypatch.setattr(subprocess, "Popen", slow)
        Runner(coordinator, ASSETS, environment).execute(work)
        assert len(children) == 1 and children[0].poll() is not None
        assert service.intent(accepted["render_intent_id"])["failure_code"] == expected
        assert (
            store.run(lambda conn: conn.exec_driver_sql("SELECT count(*) FROM artifacts").scalar())
            == 0
        )
        assert coordinator.queued() == []


def test_removed_source_finishes_and_expired_prepublication_cannot_publish(tmp_path: Path) -> None:
    import time

    from jobhunter.application.materials.coordinator import Coordinator

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        version = source(store)
        replacement = source(store)
        authority = CandidateAuthority(store)
        removed_id = authority.version("resume", version)["resume_id"]
        replacement_id = authority.version("resume", replacement)["resume_id"]
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=version,
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        authority.command(
            "RESUME_REMOVE",
            {
                "request_id": str(uuid4()),
                "revision": 1,
                "default_resume_selection": {"revision": 2},
                "replacement_resume_id": replacement_id,
            },
            removed_id,
        )
        assert service.request(command) == accepted
        with pytest.raises(Failure, match="INVALID_STATE"):
            service.request(command.model_copy(update={"request_id": str(uuid4())}))
        coordinator = Coordinator(service)
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None
        assert coordinator.publish(work, b"validated historical bytes")
        assert service.intent(accepted["render_intent_id"])["status"] == "FULFILLED"
        pending = service.request(
            RenderRequest(
                request_id=str(uuid4()),
                resume_version_id=replacement,
                render_configuration_id=config.render_configuration_id,
            )
        )
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None
        assert not coordinator.publish(
            work, b"validated but expired", deadline=time.monotonic() - 1
        )
        assert (
            service.intent(pending["render_intent_id"])["failure_code"] == "RESOURCE_LIMIT_EXCEEDED"
        )
        assert (
            store.run(lambda conn: conn.exec_driver_sql("SELECT count(*) FROM artifacts").scalar())
            == 1
        )


def test_terminal_storage_outage_preserves_known_renderer_failure(tmp_path: Path) -> None:
    from jobhunter.application.materials.coordinator import Coordinator
    from jobhunter.application.materials.runner import Runner
    from jobhunter.infrastructure.rendering.catalog import ASSETS, environment

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        coordinator = Coordinator(service)
        work = coordinator.claim(coordinator.queued()[0])
        assert work is not None
        runner = Runner(coordinator, ASSETS, environment)

        def outage(stage: str) -> None:
            if stage == "before_commit":
                raise OSError("controlled storage outage")

        store.fault = outage
        with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
            runner.fail(work, "OUTPUT_INVALID")
        store.fault = no_fault
        runner.fail(work, "STORAGE_FAILED")
        assert service.intent(accepted["render_intent_id"])["failure_code"] == "OUTPUT_INVALID"
        assert not runner.pending_failures


def test_multiple_claimers_and_publication_join_race(tmp_path: Path) -> None:
    from concurrent.futures import ThreadPoolExecutor

    from jobhunter.application.materials.coordinator import Coordinator

    with Store.open(tmp_path) as store:
        config = configuration()
        store.run(lambda conn: MaterialsRepository(conn).register(config), write=True)
        service = Materials(store, capability=lambda _: True)
        command = RenderRequest(
            request_id=str(uuid4()),
            resume_version_id=source(store),
            render_configuration_id=config.render_configuration_id,
        )
        accepted = service.request(command)
        coordinator = Coordinator(service)
        identity = coordinator.queued()[0]
        with ThreadPoolExecutor(max_workers=4) as pool:
            claims = [pool.submit(coordinator.claim, identity) for _ in range(4)]
            winners = [work for future in claims if (work := future.result()) is not None]
            assert len(winners) == 1 and winners[0].attempt_count == 1
            publications = [
                pool.submit(coordinator.publish, winners[0], b"validated fixture bytes")
                for _ in range(2)
            ]
            demands = [
                pool.submit(
                    service.request, command.model_copy(update={"request_id": str(uuid4())})
                )
                for _ in range(2)
            ]
            assert sorted(future.result() for future in publications) == [False, True]
            for result in [accepted, *(future.result() for future in demands)]:
                assert service.intent(result["render_intent_id"])["status"] == "FULFILLED"
        assert (
            store.run(lambda conn: conn.exec_driver_sql("SELECT count(*) FROM artifacts").scalar())
            == 1
        )
