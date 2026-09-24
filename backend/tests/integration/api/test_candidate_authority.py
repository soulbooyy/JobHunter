"""Independent Resume authority reads, receipt replay and missing-target ordering."""

from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def resume_body() -> dict[str, object]:
    return {
        "request_id": str(uuid4()),
        "resume_name": "R",
        "contacts": {"full_name": None, "phone_number": None, "email": None},
        "header_presentation": {"optional_items": []},
        "sections": [],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#000000",
        },
    }


def test_initial_state_create_and_exact_receipt_replay(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.get("/api/v1/resumes").json() == {
            "resumes": [],
            "default_resume_selection": {"default_resume_id": None, "revision": 1},
        }
        command = resume_body()
        first = client.post("/api/v1/resumes", json=command)
        assert first.status_code == 200
        assert client.post("/api/v1/resumes", json=command).json() == first.json()
        changed = {**command, "resume_name": "changed"}
        response = client.post("/api/v1/resumes", json=changed)
        assert response.status_code == 409 and response.json()["code"] == "REQUEST_CONFLICT"
        assert len(client.get("/api/v1/resumes").json()["resumes"]) == 1


def test_missing_target_and_invalid_state_do_not_publish_receipts(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        missing_request = str(uuid4())
        response = client.post(
            f"/api/v1/resumes/{uuid4()}/rename",
            json={"request_id": missing_request, "revision": 1, "resume_name": "X"},
        )
        assert response.status_code == 404 and response.json()["code"] == "NOT_FOUND"
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT count(*) FROM candidate_command_receipts WHERE request_id=?",
                    (missing_request,),
                ).scalar_one()
                == 0
            )

        command = resume_body()
        created = client.post("/api/v1/resumes", json=command).json()
        remove = {
            "request_id": str(uuid4()),
            "revision": 1,
            "default_resume_selection": {"revision": 2},
            "replacement_resume_id": None,
        }
        target = created["resume"]["resume_id"]
        assert client.post(f"/api/v1/resumes/{target}/remove", json=remove).status_code == 200
        rename = client.post(
            f"/api/v1/resumes/{target}/rename",
            json={"request_id": str(uuid4()), "revision": 2, "resume_name": "X"},
        )
        assert rename.status_code == 409 and rename.json()["code"] == "INVALID_STATE"
