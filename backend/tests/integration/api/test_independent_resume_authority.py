"""Independent schema-2 Resume authority and deterministic portrait preparation."""

from copy import deepcopy
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def identifier() -> str:
    return str(uuid4())


Json = dict[str, Any]


def document(*, entry_id: str | None = None, block_id: str | None = None) -> Json:
    return {
        "contacts": {
            "full_name": "Ada Lovelace",
            "phone_number": None,
            "email": "ada@example.test",
        },
        "header_presentation": {"optional_items": []},
        "sections": [
            {
                "kind": "PROJECT",
                "members": [
                    {
                        "entry_id": entry_id or identifier(),
                        "fields": {
                            "project_name": "Analytical Engine",
                            "role_title": "Author",
                            "project_url": "https://example.test/engine",
                            "start_month": "1842-01",
                            "end_month": "1843-12",
                        },
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "block_id": block_id or identifier(),
                                "runs": [{"text": "  Exact visible text  ", "marks": []}],
                            }
                        ],
                    }
                ],
            }
        ],
        "document_presentation": {
            "font_family": "SOURCE_HAN_SANS",
            "font_size_pt": 12,
            "line_spacing_pt": 18,
            "theme_color": "#1f2937",
        },
    }


def create(client: TestClient, name: str, content: Json) -> Json:
    response = client.post(
        "/api/v1/resumes", json={"request_id": identifier(), "resume_name": name, **content}
    )
    assert response.status_code == 200, response.text
    return response.json()


def test_schema_two_resume_and_deterministic_evidence(tmp_path: Path) -> None:
    content = document()
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.get("/api/v1/profile").status_code == 400
        assert client.get("/api/v1/evidence-items").status_code == 400
        assert client.get("/api/v1/resumes").json() == {
            "resumes": [],
            "default_resume_selection": {"default_resume_id": None, "revision": 1},
        }

        created = create(client, "Primary", content)
        resume_id = created["resume"]["resume_id"]
        version = created["resume_version"]
        assert version["schema_version"] == 2
        assert version["contacts"] == content["contacts"]
        assert version["sections"] == content["sections"]
        assert created["default_resume_selection"] == {
            "default_resume_id": resume_id,
            "revision": 2,
        }

        portrait = client.get("/api/v1/workspace/portrait")
        assert portrait.status_code == 200
        assert portrait.json()["portrait"] is None
        state = portrait.json()["state"]
        assert state["status"] == "QUEUED"
        assert state["source_resume_version_id"] == version["resume_version_id"]
        assert state["build_id"] is not None

        projection = store.run(
            lambda conn: (
                __import__(
                    "jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2",
                    fromlist=["CandidateRepository"],
                )
                .CandidateRepository(conn)
                .evidence_projection(version["resume_version_id"])
            )
        )
        entry = projection["entries"][0]
        block = projection["blocks"][0]
        assert entry["evidence_id"] == "entry/" + content["sections"][0]["members"][0]["entry_id"]
        assert block["evidence_id"] == (
            "block/"
            + content["sections"][0]["members"][0]["entry_id"]
            + "/"
            + content["sections"][0]["members"][0]["content"][0]["block_id"]
        )
        assert block["text"] == "  Exact visible text  "
        assert entry["fields"]["project_url"] == "https://example.test/engine"


def test_stable_ids_noop_receipt_and_cross_resume_fence(tmp_path: Path) -> None:
    content = document()
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        first = create(client, "One", content)
        resume_id = first["resume"]["resume_id"]
        request = {
            "request_id": identifier(),
            "revision": 1,
            **deepcopy(content),
        }
        sections = cast(list[Json], request["sections"])
        members = cast(list[Json], sections[0]["members"])
        content_blocks = cast(list[Json], members[0]["content"])
        runs = cast(list[Json], content_blocks[0]["runs"])
        runs[0]["text"] = "Edited but same IDs"
        saved = client.post(f"/api/v1/resumes/{resume_id}/save", json=request)
        assert saved.status_code == 200, saved.text
        assert saved.json()["outcome"] == "UPDATED"
        assert client.post(f"/api/v1/resumes/{resume_id}/save", json=request).json() == saved.json()

        no_op = {**deepcopy(request), "request_id": identifier(), "revision": 2}
        unchanged = client.post(f"/api/v1/resumes/{resume_id}/save", json=no_op)
        assert unchanged.status_code == 200
        assert unchanged.json()["outcome"] == "UNCHANGED"

        without_entries: Json = {
            **deepcopy(request),
            "request_id": identifier(),
            "revision": 2,
            "sections": [],
        }
        removed = client.post(f"/api/v1/resumes/{resume_id}/save", json=without_entries)
        assert removed.status_code == 200, removed.text
        restored: Json = {
            **deepcopy(request),
            "request_id": identifier(),
            "revision": 3,
        }
        restored_response = client.post(f"/api/v1/resumes/{resume_id}/save", json=restored)
        assert restored_response.status_code == 200, restored_response.text
        assert restored_response.json()["resume_version"]["sections"] == request["sections"]

        other = document(
            entry_id=content["sections"][0]["members"][0]["entry_id"],
            block_id=identifier(),
        )
        collision = client.post(
            "/api/v1/resumes",
            json={"request_id": identifier(), "resume_name": "Two", **other},
        )
        assert collision.status_code == 422
        assert collision.json()["field_errors"][0]["code"] == "INVALID_REFERENCE"


def test_default_final_removal_and_refresh_are_durable_without_model(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        empty = create(client, "Empty", {**document(), "sections": []})
        assert client.get("/api/v1/workspace/portrait").json()["state"]["status"] == "EMPTY_SOURCE"
        second = create(client, "Useful", document())

        selected = client.post(
            "/api/v1/workspace/default-resume/set",
            json={
                "request_id": identifier(),
                "revision": 2,
                "default_resume_id": second["resume"]["resume_id"],
            },
        )
        assert selected.status_code == 200, selected.text
        assert client.get("/api/v1/workspace/portrait").json()["state"]["status"] == "QUEUED"

        source_id = second["resume_version"]["resume_version_id"]
        refresh = {
            "request_id": identifier(),
            "default_resume_selection": {"revision": 3},
            "source_resume_version_id": source_id,
        }
        refreshed = client.post("/api/v1/workspace/portrait/refresh", json=refresh)
        assert refreshed.status_code == 200
        assert refreshed.json()["outcome"] == "UPDATED"
        assert client.post("/api/v1/workspace/portrait/refresh", json=refresh).json() == (
            refreshed.json()
        )
        duplicate = client.post(
            "/api/v1/workspace/portrait/refresh",
            json={**refresh, "request_id": identifier()},
        )
        assert duplicate.status_code == 200
        assert duplicate.json()["outcome"] == "UNCHANGED"
        assert duplicate.json()["state"]["build_id"] == refreshed.json()["state"]["build_id"]

        removed_non_default = client.post(
            f"/api/v1/resumes/{empty['resume']['resume_id']}/remove",
            json={
                "request_id": identifier(),
                "revision": 1,
                "default_resume_selection": {"revision": 3},
                "replacement_resume_id": None,
            },
        )
        assert removed_non_default.status_code == 200
        final = client.post(
            f"/api/v1/resumes/{second['resume']['resume_id']}/remove",
            json={
                "request_id": identifier(),
                "revision": 1,
                "default_resume_selection": {"revision": 3},
                "replacement_resume_id": None,
            },
        )
        assert final.status_code == 200, final.text
        assert final.json()["default_resume_selection"] == {
            "default_resume_id": None,
            "revision": 4,
        }
        assert client.get("/api/v1/workspace/portrait").json()["state"]["status"] == "NO_SOURCE"
