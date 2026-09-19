import json
import os
import select
import socket
import subprocess
import sys
import time
from pathlib import Path

import httpx
import pytest
from jobhunter.api.v1.manual_application_entries.routes import BASE
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def test_real_http_restart_privacy_and_bind(tmp_path: Path) -> None:
    port = free_port()
    env = os.environ | {"JOBHUNTER_DATA_DIRECTORY": str(tmp_path), "JOBHUNTER_PORT": str(port)}
    process = subprocess.Popen(
        [sys.executable, "-m", "jobhunter.main"],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    try:
        assert process.stdout is not None
        assert select.select([process.stdout], [], [], 10)[0]
        startup = json.loads(process.stdout.readline())
        assert startup == {
            "outcome": "INITIALIZED",
            "data_directory": str(tmp_path.resolve()),
            "schema_version": 2,
        }
        with httpx.Client(base_url=f"http://127.0.0.1:{port}", trust_env=False) as client:
            for _ in range(100):
                try:
                    response = client.get(BASE)
                    break
                except httpx.ConnectError:
                    time.sleep(0.02)
            else:
                pytest.fail("Listener did not start")
            assert response.json() == {"items": []}
            preference_request = json.loads(
                (Path(__file__).parents[2] / "fixtures/preference_save.json").read_text()
            )
            preference_request["configuration"]["target_job_keywords"] = ["Sensitive preference"]
            preference_base = "/api/v1/preferences"
            assert client.get(preference_base).json() == {"status": "NOT_CONFIGURED"}
            saved = client.post(preference_base + "/save", json=preference_request)
            assert saved.status_code == 200
            assert client.get(preference_base).json()["status"] == "CONFIGURED"
            exact = client.get(
                preference_base + "/versions/" + saved.json()["preference_set_version_id"]
            )
            assert exact.status_code == 200
            assert (
                client.post(preference_base + "/save", json=preference_request).json()
                == saved.json()
            )
            assert client.get(preference_base, headers={"Origin": "null"}).status_code == 403

            data = {
                "request_id": "12345678-1234-4123-8123-123456789abc",
                "company_name": "Sensitive Acme",
                "role_title": "Secret role",
                "application_url": "https://private.test/path?token=secret",
            }
            assert client.post(BASE, json=data).status_code == 200
            assert (
                client.post(BASE, json=data, headers={"Origin": "https://evil.test"}).status_code
                == 403
            )
            assert client.get(BASE, headers={"Host": f"localhost:{port}"}).status_code == 403
            assert (
                client.post(
                    BASE, json=data | {"application_url": "https://private.test/%bad%"}
                ).status_code
                == 422
            )
    finally:
        process.terminate()
        output, errors = process.communicate(timeout=10)
    assert "Sensitive" not in output + errors
    assert "private.test" not in output + errors
    assert "Secret role" not in output + errors
    assert "Traceback" not in output + errors
    with Store.open(tmp_path) as store:
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql("SELECT count(*) FROM manual_application_entries").scalar()
                == 1
            )
    denied = subprocess.run(
        [sys.executable, "-m", "jobhunter.main"],
        env=env | {"JOBHUNTER_BIND": "0.0.0.0"},
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert denied.returncode != 0
    assert json.loads(denied.stdout)["code"] == "ACCESS_DENIED"
