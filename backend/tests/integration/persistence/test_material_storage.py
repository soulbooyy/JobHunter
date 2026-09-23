"""Materials schema is a forward-only consumer of retained candidate authority."""

from pathlib import Path

from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_fresh_material_storage_creates_no_speculative_demand(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        assert store.recognize() == 5
        with store.engine.connect() as conn:
            for table in (
                "render_intents",
                "render_work",
                "artifacts",
                "material_command_receipts",
            ):
                assert conn.exec_driver_sql(f"SELECT count(*) FROM {table}").scalar_one() == 0


def test_renderer_inherits_directory_ownership_after_parent_death(tmp_path: Path) -> None:
    import os
    import signal
    import subprocess
    import sys
    import time

    import pytest
    from jobhunter.domain.shared.errors import Failure

    parent = """
import os,subprocess,sys
from pathlib import Path
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
with Store.open(Path(sys.argv[1])) as store:
    child=subprocess.Popen(
        [sys.executable,'-c','import time;time.sleep(30)'],pass_fds=(store.lock_fd,),
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print(child.pid,flush=True)
    os._exit(23)
"""
    result = subprocess.run(
        [sys.executable, "-c", parent, str(tmp_path)], capture_output=True, timeout=10
    )
    assert result.returncode == 23
    pid = int(result.stdout.strip())
    try:
        with pytest.raises(Failure, match="DATA_DIRECTORY_IN_USE"):
            Store.open(tmp_path)
    finally:
        os.kill(pid, signal.SIGTERM)
    deadline = time.monotonic() + 5
    while True:
        try:
            with Store.open(tmp_path) as store:
                assert store.recognize() == 5
            break
        except Failure as exc:
            assert exc.code == "DATA_DIRECTORY_IN_USE" and time.monotonic() < deadline
            time.sleep(0.02)


def historical_three(directory: Path) -> None:
    import sqlite3

    from alembic import command
    from alembic.config import Config
    from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import no_fault
    from sqlalchemy import create_engine

    database = directory / "jobhunter.sqlite3"
    engine = create_engine(
        "sqlite://", creator=lambda: sqlite3.connect(database, isolation_level=None)
    )
    try:
        with engine.connect() as conn:
            conn.exec_driver_sql("PRAGMA foreign_keys=ON")
            conn.exec_driver_sql("BEGIN IMMEDIATE")
            config = Config(str(Path(__file__).resolve().parents[3] / "alembic.ini"))
            config.attributes["connection"] = conn
            config.attributes["fault"] = no_fault
            command.upgrade(config, "ef03c92ba671")
            conn.commit()
    finally:
        engine.dispose()


def test_explicit_schema_three_migration_preserves_authority(tmp_path: Path) -> None:
    import pytest
    from jobhunter.application.candidate.authority import CandidateAuthority
    from jobhunter.domain.shared.errors import Failure

    historical_three(tmp_path)
    with Store.open(tmp_path, migration=True) as store:
        original = CandidateAuthority(store).pair("profile")
    with pytest.raises(Failure, match="SCHEMA_UNSUPPORTED"):
        Store.open(tmp_path)
    with Store.open(tmp_path, migration=True) as store:
        assert store.migrate() == "MIGRATED"
        assert CandidateAuthority(store).pair("profile") == original
        assert store.recognize() == 5
        assert store.migrate() == "UNCHANGED"


def test_material_ddl_interruption_leaves_schema_three(tmp_path: Path) -> None:
    import pytest
    from jobhunter.domain.shared.errors import Failure
    from jobhunter.infrastructure.persistence.sqlalchemy.models.materials import INDEXES, TABLES
    from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import no_fault

    for name, _ in (*TABLES, *INDEXES):
        directory = tmp_path / name
        directory.mkdir()
        historical_three(directory)

        def fault(stage: str, name: str = name) -> None:
            if stage == "migration_" + name:
                raise OSError("controlled interruption")

        with Store.open(directory, migration=True, fault=fault) as store:
            with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
                store.migrate()
            assert store.recognize() == 3
            store.fault = no_fault
            assert store.migrate() == "MIGRATED"
