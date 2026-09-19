import json
from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.api.v1.manual_application_entries.routes import BASE
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_language_neutral_fixtures(tmp_path: Path) -> None:
    fixtures = json.loads(
        (Path(__file__).parents[1] / "fixtures/manual_application_entry_admission.json").read_text()
    )
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        for case in fixtures["revision"]:
            response = client.post(
                BASE + "/" + str(uuid4()) + "/delete",
                content='{"revision":' + case["raw"] + "}",
                headers={"Content-Type": "application/json"},
            )
            assert response.status_code == case["status"]
            if "code" in case:
                assert response.json()["field_errors"][0]["code"] == case["code"]
        for case in fixtures["urls"]:
            response = client.post(
                BASE,
                json={
                    "request_id": str(uuid4()),
                    "company_name": "Fixture",
                    "role_title": "Engineer",
                    "application_url": case["value"],
                },
            )
            assert response.status_code == case["status"]
