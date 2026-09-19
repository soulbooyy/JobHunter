"""Preferences HTTP publication, receipts and admission through real SQLite."""

from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

BASE = "/api/v1/preferences"


def configuration() -> dict[str, object]:
    return {
        "target_job_keywords": [" Python ", "Python"],
        "accepted_cities": {"mode": "LIMITED", "value": ["深圳", "北京"]},
        "minimum_salary": {"mode": "LIMITED", "value": 15000},
        "recruitment_types": {"mode": "UNLIMITED"},
        "excluded_companies": {"mode": "UNLIMITED"},
        "max_required_education": {"mode": "LIMITED", "value": "BACHELOR"},
    }


def test_publication_replay_and_history(tmp_path: Path) -> None:
    command = {"request_id": str(uuid4()), "revision": None, "configuration": configuration()}
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.get(BASE).json() == {"status": "NOT_CONFIGURED"}
        first = client.post(BASE + "/save", json=command)
        assert first.status_code == 200, first.text
        result = first.json()
        assert result["outcome"] == "CREATED"
        before = client.get(BASE).json()
        assert before["current_preference_set_version"]["configuration"]["target_job_keywords"] == [
            "Python"
        ]
        noop = client.post(
            BASE + "/save", json={**command, "request_id": str(uuid4()), "revision": 1}
        )
        assert noop.json()["outcome"] == "UNCHANGED"
        changed = configuration()
        changed["target_job_keywords"] = ["Rust"]
        update = client.post(
            BASE + "/save",
            json={"request_id": str(uuid4()), "revision": 1, "configuration": changed},
        )
        assert update.json()["revision"] == 2
        assert client.post(BASE + "/save", json=command).json() == result
        assert client.get(BASE).json()["preference_set"]["revision"] == 2
        exact = client.get(BASE + "/versions/" + result["preference_set_version_id"])
        assert exact.json() == before["current_preference_set_version"]
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.post(BASE + "/save", json=command).json() == result
        assert client.get(BASE).json()["preference_set"]["revision"] == 2


def test_duplicate_members_and_nested_errors(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(
            BASE + "/save",
            content='{"configuration":{"x":1,"x":2}}',
            headers={"content-type": "application/json"},
        )
        assert response.status_code == 400
        invalid = configuration()
        invalid["accepted_cities"] = {"mode": "UNLIMITED", "value": []}
        response = client.post(
            BASE + "/save",
            json={"request_id": str(uuid4()), "revision": None, "configuration": invalid},
        )
        assert response.status_code == 422
        assert response.json()["field_errors"] == [
            {"field": "configuration.accepted_cities", "code": "INVALID_FORMAT"}
        ]
