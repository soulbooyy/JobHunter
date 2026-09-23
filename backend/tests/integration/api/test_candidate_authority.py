"""Saved Profile/Evidence/Resume authority through HTTP and real SQLite."""

from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_initial_authority_and_profile_receipt(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        initial = client.get("/api/v1/profile")
        assert initial.status_code == 200
        pair = initial.json()
        assert pair["profile"]["revision"] == 1
        assert pair["profile_version"]["full_name"] is None
        assert client.get("/api/v1/evidence-baselines/current").json()["members"] == []
        assert client.get("/api/v1/resumes").json() == {
            "resumes": [],
            "default_resume_selection": {"default_resume_id": None, "revision": 1},
        }
        command = {
            "request_id": str(uuid4()),
            "revision": 1,
            "full_name": " Ada ",
            "phone_number": None,
            "email": None,
        }
        saved = client.post("/api/v1/profile/save", json=command)
        assert saved.status_code == 200
        assert saved.json()["profile_version"]["full_name"] == "Ada"
        assert client.post("/api/v1/profile/save", json=command).json() == saved.json()


def test_evidence_update_missing_target_precedes_receipt(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        request_id = str(uuid4())
        created = client.post(
            "/api/v1/evidence-items",
            json={
                "request_id": request_id,
                "kind": "SKILL",
                "fields": {"skill_name": "Python"},
                "content": [],
            },
        )
        assert created.status_code == 200
        response = client.post(
            f"/api/v1/evidence-items/{uuid4()}/save",
            json={"request_id": request_id, "revision": 1, "fields": {}, "content": []},
        )
        assert response.status_code == 404
