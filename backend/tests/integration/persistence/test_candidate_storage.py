"""Schema 3 initialization, explicit upgrades, constraints and outcome recovery."""

import json
import sqlite3
import subprocess
import sys
from pathlib import Path
from typing import Any
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.application.candidate.preferences import Preferences
from jobhunter.bootstrap.container import create_app
from jobhunter.domain.preferences.models import SavePreferences
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.persistence.sqlalchemy.models.candidate import TABLES
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import (
    ALEMBIC_REVISION as V2,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.preferences import (
    TABLES as PREFERENCE_TABLES,
)
from jobhunter.infrastructure.persistence.sqlalchemy.models.schema import (
    ALEMBIC_DDL,
    ALEMBIC_REVISION,
    APPLICATION_ID,
    ENTRY_DDL,
    RECEIPT_DDL,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault
from sqlalchemy.exc import IntegrityError

Json = dict[str, Any]


def source(directory: Path, version: int) -> None:
    with sqlite3.connect(directory / "jobhunter.sqlite3") as conn:
        for ddl in (
            ENTRY_DDL,
            RECEIPT_DDL,
            ALEMBIC_DDL,
            *(ddl for _, ddl in PREFERENCE_TABLES if version == 2),
        ):
            conn.execute(ddl)
        conn.execute(
            "INSERT INTO alembic_version VALUES (?)", (ALEMBIC_REVISION if version == 1 else V2,)
        )
        conn.execute(f"PRAGMA application_id={APPLICATION_ID}")
        conn.execute(f"PRAGMA user_version={version}")


def profile_command() -> Json:
    return {
        "request_id": str(uuid4()),
        "revision": 1,
        "full_name": "private contact",
        "phone_number": None,
        "email": None,
    }


def evidence_command() -> Json:
    return {
        "request_id": str(uuid4()),
        "kind": "SKILL",
        "fields": {"skill_name": "private fact"},
        "content": [],
    }


@pytest.mark.parametrize("version", [1, 2])
def test_explicit_sources_seed_once_and_preserve_preferences(tmp_path: Path, version: int) -> None:
    source(tmp_path, version)
    preference = None
    body: Json = {}
    with Store.open(tmp_path, migration=True) as store:
        if version == 2:
            body = json.loads(
                (Path(__file__).parents[2] / "fixtures/preference_save.json").read_text()
            )
            preference = Preferences(store).save(SavePreferences.model_validate(body))
    with pytest.raises(Failure, match="SCHEMA_UNSUPPORTED"):
        Store.open(tmp_path)
    with Store.open(tmp_path, migration=True) as store:
        assert store.migrate() == "MIGRATED"
        candidate = CandidateAuthority(store)
        original = candidate.pair("profile")
        baseline = candidate.baseline()
        assert store.migrate() == "UNCHANGED"
        assert candidate.pair("profile") == original
        assert candidate.baseline() == baseline
        assert candidate.list_resumes() == {
            "resumes": [],
            "default_resume_selection": {"default_resume_id": None, "revision": 1},
        }
        if preference is not None:
            assert Preferences(store).save(SavePreferences.model_validate(body)) == preference
        else:
            assert Preferences(store).current().status == "NOT_CONFIGURED"
    with Store.open(tmp_path) as store:
        assert store.recognize() == 4
        assert CandidateAuthority(store).pair("profile") == original


@pytest.mark.parametrize(
    "stage",
    ["migration_" + name for name, _ in TABLES]
    + ["migration_profile_seed", "migration_candidate_seeds", "migration_candidate_version"],
)
@pytest.mark.parametrize("source_version", [0, 2])
def test_candidate_ddl_and_seeds_atomic(tmp_path: Path, stage: str, source_version: int) -> None:
    if source_version:
        source(tmp_path, source_version)

    def fault(point: str) -> None:
        if point == stage:
            raise OSError("private failure")

    if source_version:
        with Store.open(tmp_path, migration=True, fault=fault) as store:
            with pytest.raises(Failure, match="STORAGE_UNAVAILABLE"):
                store.migrate()
            assert store.recognize() == source_version
    else:
        with pytest.raises(Failure, match="INITIALIZATION_FAILED"):
            Store.open(tmp_path, fault=fault)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert conn.execute("PRAGMA user_version").fetchone() == (source_version,)
        for name, _ in TABLES:
            assert (
                conn.execute("SELECT name FROM sqlite_master WHERE name=?", (name,)).fetchall()
                == []
            )


@pytest.mark.parametrize(
    "stage,committed",
    [
        ("candidate_after_publication", False),
        ("candidate_after_receipt", False),
        ("before_commit", False),
        ("commit_before_driver", False),
        ("commit_after_driver", True),
        ("response_after_commit", True),
    ],
)
def test_command_receipt_atomic_and_no_hidden_replay(
    tmp_path: Path, stage: str, committed: bool
) -> None:
    body = profile_command()
    calls: list[str] = []
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:

        def fault(point: str) -> None:
            calls.append(point)
            if point == stage:
                raise OSError("private business/SQL parameter/fingerprint")

        store.fault = fault
        response = client.post("/api/v1/profile/save", json=body)
        assert response.status_code == 503
        assert response.json()["code"] == (
            "OUTCOME_UNKNOWN"
            if stage.startswith(("commit_", "response_"))
            else "STORAGE_UNAVAILABLE"
        )
        assert response.json()["field_errors"] == []
        assert "private" not in response.text
        assert calls.count("candidate_after_publication") == 1
        store.fault = no_fault
        assert client.get("/api/v1/profile").json()["profile"]["revision"] == (
            2 if committed else 1
        )
        with store.engine.connect() as conn:
            assert conn.exec_driver_sql(
                "SELECT count(*) FROM candidate_command_receipts"
            ).scalar_one() == int(committed)
        verified = client.post("/api/v1/profile/save", json=body)
        assert verified.status_code == 200
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.post("/api/v1/profile/save", json=body).json() == verified.json()


@pytest.mark.parametrize(
    "sql",
    [
        "DELETE FROM profiles",
        "DELETE FROM profile_versions",
        "DELETE FROM current_evidence_baseline",
        "DELETE FROM evidence_baselines",
        "DELETE FROM default_resume_selection",
        "UPDATE profile_versions SET full_name=''",
    ],
)
def test_missing_mandatory_authority_is_not_repaired(tmp_path: Path, sql: str) -> None:
    with Store.open(tmp_path):
        pass
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        conn.execute(sql)
        before = conn.iterdump()
        snapshot = list(before)
    with pytest.raises(Failure, match="STORAGE_CORRUPT"):
        Store.open(tmp_path)
    with sqlite3.connect(tmp_path / "jobhunter.sqlite3") as conn:
        assert list(conn.iterdump()) == snapshot


def test_composite_lineage_and_receipt_constraints(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = CandidateAuthority(store)
        one = service.command("EVIDENCE_CREATE", evidence_command())
        two = service.command("EVIDENCE_CREATE", evidence_command())
        a, b = one["evidence_item"]["evidence_item_id"], two["evidence_item"]["evidence_item_id"]
        bv = two["evidence_item_version"]["evidence_item_version_id"]
        statements = [
            (
                (
                    "UPDATE evidence_items SET current_evidence_item_version_id=? WHERE "
                    "evidence_item_id=?"
                ),
                (bv, a),
            ),
            (
                (
                    "UPDATE candidate_command_receipts SET evidence_item_version_id=? WHERE "
                    "evidence_item_id=?"
                ),
                (bv, a),
            ),
            (
                (
                    "UPDATE evidence_baseline_members SET evidence_item_version_id=? WHERE "
                    "evidence_item_id=?"
                ),
                (bv, a),
            ),
            (
                "UPDATE candidate_command_receipts SET evidence_item_id=? WHERE evidence_item_id=?",
                (b, a),
            ),
            ("UPDATE evidence_items SET revision=0", ()),
            ("UPDATE evidence_items SET status='REMOVED'", ()),
            ("UPDATE default_resume_selection SET default_resume_id=?", (str(uuid4()),)),
            ("UPDATE candidate_command_receipts SET schema_version=2", ()),
        ]
        for sql, args in statements:
            with store.engine.connect() as conn, pytest.raises(IntegrityError):
                conn.exec_driver_sql("BEGIN IMMEDIATE")
                conn.exec_driver_sql(sql, args)
                conn.commit()
        assert (
            service.pair("evidence_item", a)["evidence_item_version"]
            == one["evidence_item_version"]
        )


def test_detected_corrupt_historical_body_is_internal_not_missing_reference(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        created = client.post("/api/v1/evidence-items", json=evidence_command()).json()
        version = created["evidence_item_version"]["evidence_item_version_id"]
        with store.engine.begin() as conn:
            conn.exec_driver_sql("UPDATE evidence_item_versions SET fields='{}'")
        response = client.get("/api/v1/evidence-items/versions/" + version)
        assert response.status_code == 500
        assert response.json()["code"] == "INTERNAL_ERROR"
        assert response.json()["field_errors"] == []


@pytest.mark.parametrize(
    "stage,version",
    [("migration_candidate_seeds", 2), ("commit_before_driver", 2), ("commit_after_driver", 4)],
)
def test_migration_process_death_recovers_source_or_target(
    tmp_path: Path, stage: str, version: int
) -> None:
    source(tmp_path, 2)
    script = """
import os,sys
from pathlib import Path
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault
def fault(point):
    if point==sys.argv[2]: os._exit(29)
with Store.open(Path(sys.argv[1]),migration=True,fault=fault) as store: store.migrate()
"""
    result = subprocess.run(
        [sys.executable, "-c", script, str(tmp_path), stage], capture_output=True, timeout=10
    )
    assert result.returncode == 29
    assert not result.stderr
    with Store.open(tmp_path, migration=True) as store:
        assert store.recognize() == version
        assert store.migrate() == ("UNCHANGED" if version == 4 else "MIGRATED")


def test_resume_relational_sources_and_snapshot_corruption(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        service = CandidateAuthority(store)
        a = service.command("EVIDENCE_CREATE", evidence_command())
        b = service.command("EVIDENCE_CREATE", evidence_command())
        body: Json = {
            "request_id": str(uuid4()),
            "resume_name": "R",
            "profile_version_id": service.pair("profile")["profile_version"]["profile_version_id"],
            "header_presentation": {"optional_items": []},
            "sections": [
                {
                    "kind": "SKILL",
                    "members": [
                        {
                            "evidence_item_id": a["evidence_item"]["evidence_item_id"],
                            "evidence_item_version_id": a["evidence_item_version"][
                                "evidence_item_version_id"
                            ],
                            "content": [],
                        }
                    ],
                }
            ],
            "document_presentation": {
                "font_family": "HEITI",
                "font_size_pt": 12,
                "line_spacing_pt": 14,
                "theme_color": "#000000",
            },
        }
        first = service.command("RESUME_CREATE", body)
        second = service.command("RESUME_CREATE", {**body, "request_id": str(uuid4())})
        statements = [
            ("UPDATE resume_versions SET profile_version_id=?", (str(uuid4()),)),
            (
                "UPDATE resumes SET current_resume_version_id=? WHERE resume_id=?",
                (second["resume_version"]["resume_version_id"], first["resume"]["resume_id"]),
            ),
            (
                "UPDATE resume_members SET evidence_item_version_id=?",
                (b["evidence_item_version"]["evidence_item_version_id"],),
            ),
            ("UPDATE resume_members SET kind='PROJECT'", ()),
            (
                "UPDATE candidate_command_receipts SET resume_version_id=? WHERE request_id=?",
                (second["resume_version"]["resume_version_id"], body["request_id"]),
            ),
            (
                "UPDATE current_evidence_baseline SET evidence_baseline_snapshot_id=?",
                (str(uuid4()),),
            ),
        ]
        for sql, args in statements:
            with store.engine.connect() as conn, pytest.raises(IntegrityError):
                conn.exec_driver_sql("BEGIN IMMEDIATE")
                conn.exec_driver_sql(sql, args)
                conn.commit()
        # A malformed persisted receipt must not trigger command execution.
        with store.engine.begin() as conn:
            conn.exec_driver_sql(
                "UPDATE candidate_command_receipts SET result_snapshot='{}' WHERE request_id=?",
                (body["request_id"],),
            )
        response = client.post("/api/v1/resumes", json=body)
        assert response.status_code == 500
        assert response.json()["code"] == "INTERNAL_ERROR"
        assert len(service.list_resumes()["resumes"]) == 2
