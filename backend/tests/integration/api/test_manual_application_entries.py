from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

BASE = "/api/v1/manual-application-entries"


def test_receipt_revision_delete_restart(tmp_path: Path) -> None:
    command = dict(
        request_id=str(uuid4()),
        company_name=" Acme ",
        role_title="工程師",
        application_url="HTTP://Example.test:80/./apply",
    )
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(BASE, json=command)
        assert response.status_code == 200
        identity = response.json()
        assert client.post(BASE, json=command).json() == identity
        path = BASE + "/" + identity["manual_application_entry_id"]
        entry = client.get(path).json()
        assert entry["company_name"] == "Acme"
        assert entry["revision"] == 1
        assert client.post(path + "/resolve-url", json={"revision": 1}).json() == {
            "application_url": command["application_url"]
        }
        assert client.post(path + "/delete", json={"revision": 2}).status_code == 409
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert len(client.get(BASE).json()["items"]) == 1
        assert client.post(path + "/delete", json={"revision": 1}).status_code == 200
        assert client.post(BASE, json=command).json()["code"] == "ORIGINAL_ENTRY_DELETED"


def test_exact_revision(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        path = BASE + "/" + str(uuid4()) + "/delete"
        for value in ["1.0000000000000001", "true", '"1"', "null"]:
            response = client.post(
                path,
                content='{"revision":' + value + "}",
                headers={"Content-Type": "application/json"},
            )
            assert response.status_code == 422
            assert response.json()["field_errors"] == [
                {"field": "revision", "code": "INVALID_TYPE"}
            ]
        for value in ["1.0", "1e0"]:
            assert (
                client.post(
                    path,
                    content='{"revision":' + value + "}",
                    headers={"Content-Type": "application/json"},
                ).status_code
                == 404
            )
