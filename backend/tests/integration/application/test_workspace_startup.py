import json
import os
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_initialization_rollback_and_residue(tmp_path: Path) -> None:
    def fail(stage: str) -> None:
        if stage == "initialization_before_commit":
            raise OSError("controlled failure")

    with pytest.raises(Failure, match="INITIALIZATION_FAILED"):
        Store.open(tmp_path, fault=fail)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert conn.execute("SELECT name FROM sqlite_master").fetchall() == []
        assert conn.execute("PRAGMA application_id").fetchone() == (0,)
        assert conn.execute("PRAGMA user_version").fetchone() == (0,)
    with pytest.raises(Failure, match="STORAGE_NOT_RECOGNIZED"):
        Store.open(tmp_path)


@pytest.mark.parametrize(
    "kind,code",
    [
        ("missing", "DATA_DIRECTORY_UNAVAILABLE"),
        ("hidden", "STORAGE_NOT_RECOGNIZED"),
        ("foreign", "STORAGE_NOT_RECOGNIZED"),
        ("corrupt", "STORAGE_CORRUPT"),
        ("unsupported", "SCHEMA_UNSUPPORTED"),
        ("incomplete", "STORAGE_NOT_RECOGNIZED"),
        ("migration", "STORAGE_NOT_RECOGNIZED"),
        ("constraints", "STORAGE_NOT_RECOGNIZED"),
    ],
)
def test_recognition(tmp_path: Path, kind: str, code: str) -> None:
    db = tmp_path / "jobhunter.sqlite3"
    if kind == "missing":
        tmp_path = tmp_path / "absent"
    elif kind == "hidden":
        (tmp_path / ".hidden").touch()
    elif kind == "corrupt":
        db.write_bytes(b"not a sqlite database")
    elif kind == "foreign":
        with sqlite3.connect(db) as conn:
            conn.execute("CREATE TABLE unrelated (value TEXT)")
    else:
        with Store.open(tmp_path):
            pass
        with sqlite3.connect(db) as conn:
            if kind == "unsupported":
                conn.execute("PRAGMA user_version=2")
            elif kind == "incomplete":
                conn.execute("DROP TABLE manual_application_entries")
            elif kind == "migration":
                conn.execute("DROP TABLE alembic_version")
            else:
                conn.execute("DROP TABLE manual_application_entry_create_receipts")
                conn.execute(
                    "CREATE TABLE manual_application_entry_create_receipts "
                    "(request_id TEXT, request_fingerprint TEXT, manual_application_entry_id TEXT)"
                )
    before = db.read_bytes() if db.exists() else None
    with pytest.raises(Failure, match=code):
        Store.open(tmp_path)
    if before is not None:
        assert db.read_bytes() == before


def test_independent_process_lock_alias_and_kill(tmp_path: Path) -> None:
    alias = tmp_path.parent / (tmp_path.name + "-alias")
    alias.symlink_to(tmp_path, target_is_directory=True)
    script = (
        "import sys,time; from pathlib import Path; "
        "from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store; "
        's=Store.open(Path(sys.argv[1])); print("ready",flush=True); time.sleep(30)'
    )
    process = subprocess.Popen(
        [sys.executable, "-c", script, str(tmp_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        assert process.stdout is not None
        assert process.stdout.readline().strip() == "ready"
        with pytest.raises(Failure, match="DATA_DIRECTORY_IN_USE"):
            Store.open(alias)
    finally:
        process.kill()
        process.communicate(timeout=5)
    with Store.open(alias) as store:
        assert store.outcome == "OPENED"
        assert store.directory == tmp_path.resolve()


def test_migration_metadata_constraint_recognition(tmp_path: Path) -> None:
    with Store.open(tmp_path):
        pass
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        conn.execute("ALTER TABLE alembic_version RENAME TO old")
        conn.execute("CREATE TABLE alembic_version (version_num TEXT)")
        conn.execute("INSERT INTO alembic_version SELECT * FROM old")
        conn.execute("DROP TABLE old")
    with pytest.raises(Failure, match="STORAGE_NOT_RECOGNIZED"):
        Store.open(tmp_path)


@pytest.mark.parametrize(
    "stage",
    [
        "initialization_entry",
        "initialization_receipt",
        "initialization_identity",
        "initialization_version",
    ],
)
def test_each_initialization_boundary(tmp_path: Path, stage: str) -> None:
    def fail(point: str) -> None:
        if point == stage:
            raise OSError("controlled DDL interruption")

    with pytest.raises(Failure, match="INITIALIZATION_FAILED"):
        Store.open(tmp_path, fault=fail)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert conn.execute("SELECT name FROM sqlite_master").fetchall() == []
        assert conn.execute("PRAGMA application_id").fetchone() == (0,)
        assert conn.execute("PRAGMA user_version").fetchone() == (0,)


def test_startup_failure_nonzero_and_default(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    missing = tmp_path / "missing"
    result = subprocess.run(
        [sys.executable, "-m", "jobhunter.main"],
        env=os.environ | {"JOBHUNTER_DATA_DIRECTORY": str(missing)},
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 1
    assert json.loads(result.stdout) == {
        "code": "DATA_DIRECTORY_UNAVAILABLE",
        "message": "Data directory unavailable.",
        "field_errors": [],
    }
    assert not missing.exists()
    monkeypatch.setattr(
        "jobhunter.infrastructure.persistence.sqlalchemy.uow.store.default_directory",
        lambda: missing,
    )
    with Store.open() as store:
        assert store.outcome == "INITIALIZED"
    assert missing.is_dir()
