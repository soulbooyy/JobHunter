from pathlib import Path
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.api.v1.manual_application_entries.routes import BASE
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault


@pytest.mark.parametrize(
    "stage,code,count",
    [
        ("after_entry_insert", "STORAGE_UNAVAILABLE", 0),
        ("before_commit", "STORAGE_UNAVAILABLE", 0),
        ("commit_before_driver", "OUTCOME_UNKNOWN", 0),
        ("commit_after_driver", "OUTCOME_UNKNOWN", 1),
        ("response_after_commit", "OUTCOME_UNKNOWN", 1),
    ],
)
def test_commit_and_response_boundaries(tmp_path: Path, stage: str, code: str, count: int) -> None:
    seen: list[str] = []

    def fail(point: str) -> None:
        seen.append(point)
        if point == stage:
            raise OSError("secret company https://secret.test SQL parameters")

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        store.fault = fail
        command = dict(
            request_id=str(uuid4()),
            company_name="secret company",
            role_title="Engineer",
            application_url="https://secret.test",
        )
        response = client.post(BASE, json=command)
        assert response.status_code == 503
        assert response.json()["code"] == code
        assert "secret" not in response.text
        assert seen.count("after_entry_insert") == 1
        store.fault = no_fault
        assert len(client.get(BASE).json()["items"]) == count
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT count(*) FROM manual_application_entry_create_receipts"
                ).scalar()
                == count
            )
        assert client.post(BASE, json=command).status_code == 200
        assert len(client.get(BASE).json()["items"]) == 1


def test_sqlite_busy_commit_has_confirmed_noncommit(tmp_path: Path) -> None:
    import sqlite3

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        reader = sqlite3.connect(tmp_path / "jobhunter.sqlite3", isolation_level=None)
        reader.execute("BEGIN")
        reader.execute("SELECT * FROM manual_application_entries").fetchall()
        try:
            response = client.post(
                BASE,
                json=dict(
                    request_id=str(uuid4()),
                    company_name="Fixture",
                    role_title="Engineer",
                    application_url="https://example.test",
                ),
            )
            assert response.status_code == 503
            assert response.json()["code"] == "STORAGE_UNAVAILABLE"
        finally:
            reader.close()
        assert client.get(BASE).json() == {"items": []}
