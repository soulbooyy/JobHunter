"""Schema evolution uses real SQLite and preserves the frozen source revision."""

import sqlite3
from pathlib import Path

import pytest
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    ALEMBIC_DDL,
    ALEMBIC_REVISION,
    APPLICATION_ID,
    ENTRY_DDL,
    RECEIPT_DDL,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def schema_one(directory: Path) -> None:
    with sqlite3.connect(directory / "jobhunter.sqlite3") as conn:
        for ddl in (ENTRY_DDL, RECEIPT_DDL, ALEMBIC_DDL):
            conn.execute(ddl)
        conn.execute("INSERT INTO alembic_version VALUES (?)", (ALEMBIC_REVISION,))
        conn.execute(f"PRAGMA application_id={APPLICATION_ID}")
        conn.execute("PRAGMA user_version=1")


def test_source_refused_by_runtime(tmp_path: Path) -> None:
    schema_one(tmp_path)
    with pytest.raises(Failure, match="SCHEMA_UNSUPPORTED"):
        Store.open(tmp_path)


def test_fresh_schema_two(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        with store.engine.connect() as conn:
            assert conn.exec_driver_sql("PRAGMA user_version").scalar() == 2
            assert conn.exec_driver_sql("PRAGMA foreign_keys").scalar() == 1
            assert conn.exec_driver_sql("SELECT count(*) FROM preference_sets").scalar() == 0


def test_migration_preserves_entries_and_deleted_receipts(tmp_path: Path) -> None:
    from uuid import uuid4

    from fastapi.testclient import TestClient
    from jobhunter.bootstrap.container import create_app
    from jobhunter.domain.manual_application_entries.models import CreateEntry, fingerprint

    schema_one(tmp_path)
    data = CreateEntry(
        request_id=str(uuid4()),
        company_name="Fixture",
        role_title="Engineer",
        application_url="https://example.test",
    )
    live, deleted = str(uuid4()), str(uuid4())
    deleted_request = str(uuid4())
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        conn.execute(
            "INSERT INTO manual_application_entries VALUES (?,?,?,?,?,?,?)",
            (
                live,
                data.company_name,
                data.role_title,
                data.application_url,
                3,
                "2026-09-19T00:00:00.000Z",
                "2026-09-20T00:00:00.000Z",
            ),
        )
        conn.execute(
            "INSERT INTO manual_application_entry_create_receipts VALUES (?,?,?)",
            (data.request_id, fingerprint(data), live),
        )
        conn.execute(
            "INSERT INTO manual_application_entry_create_receipts VALUES (?,?,?)",
            (deleted_request, fingerprint(data), deleted),
        )
        before = [
            conn.execute(f"SELECT * FROM {table}").fetchall()
            for table in ("manual_application_entries", "manual_application_entry_create_receipts")
        ]
    with Store.open(tmp_path, migration=True) as store:
        assert store.migrate() == "MIGRATED"
        assert store.migrate() == "UNCHANGED"
        with store.engine.connect() as conn:
            assert [
                list(map(tuple, conn.exec_driver_sql(f"SELECT * FROM {table}").all()))
                for table in (
                    "manual_application_entries",
                    "manual_application_entry_create_receipts",
                )
            ] == before
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        base = "/api/v1/manual-application-entries"
        assert client.post(base, json=data.model_dump()).json() == {
            "manual_application_entry_id": live
        }
        assert (
            client.post(base, json=data.model_dump() | {"request_id": deleted_request}).json()[
                "code"
            ]
            == "ORIGINAL_ENTRY_DELETED"
        )
        assert client.get("/api/v1/preferences").json() == {"status": "NOT_CONFIGURED"}


@pytest.mark.parametrize(
    "stage,target",
    [
        ("migration_preference_sets", 1),
        ("migration_preference_set_versions", 1),
        ("migration_preference_save_receipts", 1),
        ("migration_version", 1),
        ("before_commit", 1),
        ("commit_before_driver", 1),
        ("commit_after_driver", 2),
    ],
)
def test_migration_atomicity_and_completion(tmp_path: Path, stage: str, target: int) -> None:
    schema_one(tmp_path)

    def fault(point: str) -> None:
        if point == stage:
            raise OSError("private migration failure")

    with Store.open(tmp_path, migration=True, fault=fault) as store:
        if target == 1:
            with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
                store.migrate()
        else:
            assert store.migrate() == "MIGRATED"
        assert store.recognize() == target
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert conn.execute("PRAGMA user_version").fetchone() == (target,)
        assert conn.execute(
            "SELECT count(*) FROM sqlite_master WHERE name LIKE 'preference_%'"
        ).fetchone()[0] == (0 if target == 1 else 3)


@pytest.mark.parametrize(
    "stage",
    [
        "migration_preference_sets",
        "migration_preference_set_versions",
        "migration_preference_save_receipts",
        "migration_version",
    ],
)
def test_fresh_initialization_rolls_back_all_ddl(tmp_path: Path, stage: str) -> None:
    def fault(point: str) -> None:
        if point == stage:
            raise OSError("interrupted")

    with pytest.raises(Failure, match="INITIALIZATION_FAILED"):
        Store.open(tmp_path, fault=fault)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall() == []
        assert conn.execute("PRAGMA user_version").fetchone() == (0,)
    with pytest.raises(Failure, match="STORAGE_NOT_RECOGNIZED"):
        Store.open(tmp_path)


def test_migration_missing_empty_and_incomplete_source(tmp_path: Path) -> None:
    with pytest.raises(Failure, match="STORAGE_NOT_RECOGNIZED"):
        Store.open(tmp_path, migration=True)
    assert list(tmp_path.iterdir()) == []
    with pytest.raises(Failure, match="DATA_DIRECTORY_UNAVAILABLE"):
        Store.open(tmp_path / "missing", migration=True)
    schema_one(tmp_path)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        conn.execute("DROP TABLE manual_application_entries")
    with pytest.raises(Failure, match="STORAGE_NOT_RECOGNIZED"):
        Store.open(tmp_path, migration=True)


def test_database_reference_constraints(tmp_path: Path) -> None:
    import json
    from uuid import uuid4

    from jobhunter.application.candidate.preferences import Preferences
    from jobhunter.domain.preferences.models import SavePreferences
    from sqlalchemy.exc import IntegrityError

    data = json.loads((Path(__file__).parents[2] / "fixtures/preference_save.json").read_text())
    with Store.open(tmp_path) as store:
        result = Preferences(store).save(SavePreferences.model_validate(data))
        # Exercise the real connection factory: deferred FKs reject at COMMIT.
        statements = [
            ("UPDATE preference_sets SET current_preference_set_version_id=?", (str(uuid4()),)),
            ("UPDATE preference_set_versions SET preference_set_id=?", (str(uuid4()),)),
            ("UPDATE preference_save_receipts SET preference_set_id=?", (str(uuid4()),)),
            ("UPDATE preference_save_receipts SET preference_set_version_id=?", (str(uuid4()),)),
            (
                "INSERT INTO preference_sets SELECT ?,singleton_key,"
                "current_preference_set_version_id,"
                "revision,created_at,updated_at FROM preference_sets",
                (str(uuid4()),),
            ),
            ("UPDATE preference_sets SET singleton_key=2", ()),
            ("UPDATE preference_set_versions SET configuration='[]'", ()),
            ("UPDATE preference_save_receipts SET outcome='FAILED'", ()),
            ("UPDATE preference_save_receipts SET result_revision=0", ()),
            ("UPDATE preference_sets SET revision=1.5", ()),
            ("UPDATE preference_sets SET updated_at='bad'", ()),
            ("UPDATE preference_save_receipts SET request_fingerprint='ABC'", ()),
        ]
        for sql, params in statements:
            with store.engine.connect() as conn, pytest.raises(IntegrityError):
                conn.exec_driver_sql("BEGIN IMMEDIATE")
                conn.exec_driver_sql(sql, params)
                conn.commit()
        assert (
            Preferences(store).version(result.preference_set_version_id).preference_set_id
            == result.preference_set_id
        )


@pytest.mark.parametrize("damage", ["configuration", "foreign_key", "metadata"])
def test_recognition_rejects_corrupted_authority(tmp_path: Path, damage: str) -> None:
    import json

    from jobhunter.application.candidate.preferences import Preferences
    from jobhunter.domain.preferences.models import SavePreferences

    data = json.loads((Path(__file__).parents[2] / "fixtures/preference_save.json").read_text())
    with Store.open(tmp_path) as store:
        Preferences(store).save(SavePreferences.model_validate(data))
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        if damage == "configuration":
            conn.execute("UPDATE preference_set_versions SET configuration='{}'")
        elif damage == "foreign_key":
            conn.execute(
                "UPDATE preference_sets SET "
                "current_preference_set_version_id='11111111-1111-4111-8111-111111111111'"
            )
        else:
            conn.execute("UPDATE alembic_version SET version_num='b720a94fd381'")
    with pytest.raises(
        Failure, match="STORAGE_CORRUPT" if damage != "metadata" else "STORAGE_NOT_RECOGNIZED"
    ):
        Store.open(tmp_path)


def test_json_spelling_is_not_equality(tmp_path: Path) -> None:
    import json

    from jobhunter.application.candidate.preferences import Preferences
    from jobhunter.domain.preferences.models import SavePreferences

    data = json.loads((Path(__file__).parents[2] / "fixtures/preference_save.json").read_text())
    with Store.open(tmp_path) as store:
        service = Preferences(store)
        first = service.save(SavePreferences.model_validate(data))
        version = service.version(first.preference_set_version_id)
        with store.engine.begin() as conn:
            conn.exec_driver_sql(
                "UPDATE preference_set_versions SET configuration=?",
                (json.dumps(version.configuration.model_dump(), indent=4, sort_keys=True),),
            )
    with Store.open(tmp_path) as store:
        service = Preferences(store)
        assert service.version(first.preference_set_version_id) == version
        data.update(revision=1, request_id="22222222-2222-4222-8222-222222222222")
        assert service.save(SavePreferences.model_validate(data)).outcome == "UNCHANGED"


def test_offline_cli_lock_alias_and_exit_release(tmp_path: Path) -> None:
    import json
    import subprocess
    import sys

    schema_one(tmp_path)
    alias = tmp_path.parent / (tmp_path.name + "-alias")
    alias.symlink_to(tmp_path, target_is_directory=True)
    args = [sys.executable, "-m", "jobhunter.bootstrap.migrate", "--data-directory", str(alias)]
    with Store.open(tmp_path, migration=True):
        blocked = subprocess.run(args, capture_output=True, text=True, timeout=10)
        assert blocked.returncode == 1
        assert json.loads(blocked.stdout)["code"] == "DATA_DIRECTORY_IN_USE"
        assert not blocked.stderr
    migrated = subprocess.run(args, capture_output=True, text=True, timeout=10)
    assert migrated.returncode == 0, migrated.stderr
    assert json.loads(migrated.stdout) == {
        "outcome": "MIGRATED",
        "data_directory": str(tmp_path.resolve()),
        "schema_version": 2,
    }
    assert not migrated.stderr
    unchanged = subprocess.run(args, capture_output=True, text=True, timeout=10)
    assert json.loads(unchanged.stdout)["outcome"] == "UNCHANGED"


@pytest.mark.parametrize(
    "stage,target", [("migration_preference_set_versions", 1), ("commit_after_driver", 2)]
)
def test_migration_process_death_recovers_and_releases_lock(
    tmp_path: Path, stage: str, target: int
) -> None:
    import subprocess
    import sys

    schema_one(tmp_path)
    script = """
import os, sys
from pathlib import Path
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
def fault(point):
    if point == sys.argv[2]:
        os._exit(23)
with Store.open(Path(sys.argv[1]), migration=True, fault=fault) as store:
    store.migrate()
"""
    result = subprocess.run(
        [sys.executable, "-c", script, str(tmp_path), stage], capture_output=True, timeout=10
    )
    assert result.returncode == 23
    with Store.open(tmp_path, migration=True) as store:
        assert store.recognize() == target
        assert store.migrate() == ("MIGRATED" if target == 1 else "UNCHANGED")


def test_composite_constraints_reject_existing_cross_owner_pair(tmp_path: Path) -> None:
    """Relax only singleton CHECK to construct two otherwise valid reference families."""
    import json
    from uuid import uuid4

    from jobhunter.application.candidate.preferences import Preferences
    from jobhunter.domain.preferences.models import SavePreferences
    from sqlalchemy.exc import IntegrityError

    data = json.loads((Path(__file__).parents[2] / "fixtures/preference_save.json").read_text())
    with Store.open(tmp_path) as store:
        first = Preferences(store).save(SavePreferences.model_validate(data))
        second_root, second_version = str(uuid4()), str(uuid4())
        with store.engine.connect() as conn:
            conn.exec_driver_sql("PRAGMA ignore_check_constraints=ON")
            conn.exec_driver_sql("BEGIN IMMEDIATE")
            conn.exec_driver_sql(
                "INSERT INTO preference_sets SELECT ?,2,?,revision,created_at,updated_at "
                "FROM preference_sets",
                (second_root, second_version),
            )
            conn.exec_driver_sql(
                "INSERT INTO preference_set_versions SELECT ?,?,created_at,configuration "
                "FROM preference_set_versions",
                (second_version, second_root),
            )
            conn.commit()
        for sql, args in [
            (
                "UPDATE preference_sets SET current_preference_set_version_id=? "
                "WHERE preference_set_id=?",
                (second_version, first.preference_set_id),
            ),
            ("UPDATE preference_save_receipts SET preference_set_version_id=?", (second_version,)),
            ("UPDATE preference_save_receipts SET preference_set_id=?", (second_root,)),
        ]:
            with store.engine.connect() as conn, pytest.raises(IntegrityError):
                assert conn.exec_driver_sql("PRAGMA ignore_check_constraints").scalar() == 0
                conn.exec_driver_sql("BEGIN IMMEDIATE")
                conn.exec_driver_sql(sql, args)
                conn.commit()
