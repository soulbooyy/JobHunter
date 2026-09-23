"""Actual API acceptance through the lifespan worker to verified downloadable bytes."""

import hashlib
import time
from pathlib import Path
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_render_demand_to_download_and_restart_replay(tmp_path: Path) -> None:
    completed: list[tuple[Json, Json, str, Json]] = []
    with Store.open(tmp_path) as store:
        with TestClient(create_app(store)) as client:
            configurations = client.get("/api/v1/render-configurations").json()["items"]
            assert len(configurations) == 2
            profile = client.get("/api/v1/profile").json()["profile_version"]
            saved = client.post(
                "/api/v1/resumes",
                json={
                    "request_id": str(uuid4()),
                    "resume_name": "Empty permitted",
                    "profile_version_id": profile["profile_version_id"],
                    "header_presentation": {"optional_items": []},
                    "sections": [],
                    "document_presentation": {
                        "font_family": "KAITI",
                        "font_size_pt": 12,
                        "line_spacing_pt": 14,
                        "theme_color": "#123456",
                    },
                },
            ).json()
            for item in configurations:
                command = {
                    "request_id": str(uuid4()),
                    "resume_version_id": saved["resume_version"]["resume_version_id"],
                    "render_configuration_id": item["configuration"]["render_configuration_id"],
                }
                response = client.post("/api/v1/render-intents", json=command)
                assert response.status_code == 200, response.text
                accepted = response.json()
                deadline = time.monotonic() + 30
                while True:
                    intent = client.get(
                        "/api/v1/render-intents/" + accepted["render_intent_id"]
                    ).json()
                    if intent["status"] != "PENDING":
                        break
                    assert time.monotonic() < deadline
                    time.sleep(0.05)
                assert intent["status"] == "FULFILLED", intent
                url = "/api/v1/artifacts/" + intent["artifact_id"]
                metadata = client.get(url).json()
                content = client.get(
                    url + "/content?disposition=attachment",
                    headers={"Range": "bytes=0-3", "Accept-Encoding": "gzip"},
                )
                assert content.status_code == 200
                assert content.headers["content-type"] == metadata["media_type"]
                assert content.headers["content-length"] == str(metadata["byte_length"])
                assert content.headers["cache-control"] == "no-store"
                assert 'attachment; filename="artifact-' in content.headers["content-disposition"]
                assert "content-encoding" not in content.headers and "etag" not in content.headers
                assert hashlib.sha256(content.content).hexdigest() == metadata["sha256"]
                assert client.post("/api/v1/render-intents", json=command).json() == accepted
                completed.append((command, accepted, url, metadata))
    with Store.open(tmp_path) as reopened:
        with TestClient(create_app(reopened)) as client:
            for command, accepted, url, metadata in completed:
                assert client.post("/api/v1/render-intents", json=command).json() == accepted
                assert client.get(url).json() == metadata
