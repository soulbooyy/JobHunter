import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import APPLICATION_ID
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_settings_permissions_constraints(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        with store.engine.connect() as conn:
            assert conn.exec_driver_sql("PRAGMA synchronous").scalar() == 3
            assert conn.exec_driver_sql("PRAGMA fullfsync").scalar() == 1
            assert conn.exec_driver_sql("PRAGMA journal_mode").scalar() == "delete"
            assert conn.exec_driver_sql("PRAGMA application_id").scalar() == APPLICATION_ID
        assert tmp_path.stat().st_mode & 0o777 == 0o700
        assert (tmp_path / "jobhunter.sqlite3").stat().st_mode & 0o777 == 0o600


def test_no_implicit_ddl_commit(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        with store.engine.connect() as conn:
            conn.exec_driver_sql("BEGIN IMMEDIATE")
            conn.exec_driver_sql("CREATE TABLE probe (value TEXT)")
            conn.rollback()
            assert (
                conn.exec_driver_sql("SELECT name FROM sqlite_master WHERE name='probe'").first()
                is None
            )


@pytest.mark.parametrize("stage,expected", [("after_entry_insert", 0), ("commit_after_driver", 1)])
def test_process_crash_transaction_recovery(tmp_path: Path, stage: str, expected: int) -> None:
    script = """
import os, sys
from pathlib import Path
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.domain.manual_application_entries.models import CreateEntry

def crash(point):
    if point == sys.argv[2]:
        os._exit(71)

with Store.open(Path(sys.argv[1])) as store:
    store.fault = crash
    Entries(store).create(CreateEntry(request_id='12345678-1234-4123-8123-123456789abc',
        company_name='Fixture', role_title='Engineer', application_url='https://example.test'))
"""
    result = subprocess.run(
        [sys.executable, "-c", script, str(tmp_path), stage],
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 71
    with Store.open(tmp_path) as store, store.engine.connect() as conn:
        assert (
            conn.exec_driver_sql("SELECT count(*) FROM manual_application_entries").scalar()
            == expected
        )
        assert (
            conn.exec_driver_sql(
                "SELECT count(*) FROM manual_application_entry_create_receipts"
            ).scalar()
            == expected
        )


@pytest.mark.parametrize(
    "column,value",
    [
        ("company_name", ""),
        ("role_title", "x" * 201),
        ("application_url", ""),
        ("revision", 0),
        ("revision", 9007199254740992),
        ("revision", 1.5),
        ("manual_application_entry_id", "12345678-1234-1123-8123-123456789abc"),
        ("created_at", "2026-09-19T01:02:03Z"),
        ("updated_at", "2020-01-01T00:00:00.000Z"),
    ],
)
def test_database_value_constraints(tmp_path: Path, column: str, value: object) -> None:
    with Store.open(tmp_path):
        pass
    row: dict[str, object] = dict(
        manual_application_entry_id="12345678-1234-4123-8123-123456789abc",
        company_name="Fixture",
        role_title="Engineer",
        application_url="https://example.test",
        revision=1,
        created_at="2026-09-19T01:02:03.000Z",
        updated_at="2026-09-19T01:02:03.000Z",
    )
    row[column] = value
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO manual_application_entries VALUES (?, ?, ?, ?, ?, ?, ?)",
                tuple(row.values()),
            )
