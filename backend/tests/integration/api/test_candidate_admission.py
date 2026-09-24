"""Independent Resume transport and domain admission at the real HTTP boundary."""

from pathlib import Path
from typing import Any, cast
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

Json = dict[str, Any]


def body(*, kind: str = "SKILL", fields: object | None = None) -> Json:
    return {
        "request_id": str(uuid4()),
        "resume_name": "Resume",
        "contacts": {"full_name": "Ada", "phone_number": "+12 (3)-4", "email": "a@b"},
        "header_presentation": {"optional_items": []},
        "sections": [
            {
                "kind": kind,
                "members": [
                    {
                        "entry_id": str(uuid4()),
                        "fields": fields if fields is not None else {"skill_name": "Python"},
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "block_id": str(uuid4()),
                                "runs": [{"text": "Exact text", "marks": []}],
                            }
                        ],
                    }
                ],
            }
        ],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#112233",
        },
    }


def assert_error(response: object, code: str, field: str | None = None) -> None:
    assert hasattr(response, "status_code")
    payload = response.json()  # type: ignore[attr-defined]
    transport = {"BAD_REQUEST", "REQUEST_TOO_LARGE", "REVISION_CONFLICT"}
    if code in transport:
        assert payload["code"] == code
    else:
        assert payload["code"] == "VALIDATION_ERROR"
        assert payload["field_errors"][0]["code"] == code
        if field is not None:
            assert payload["field_errors"][0]["field"] == field


@pytest.mark.parametrize(
    "kind,fields",
    [
        (
            "EDUCATION",
            {
                "school_name": "U",
                "degree": "BACHELOR",
                "major": None,
                "start_month": "2020-01",
                "end_month": "2024-01",
            },
        ),
        (
            "WORK_EXPERIENCE",
            {"company_name": "C", "role_title": "R", "start_month": None, "end_month": None},
        ),
        (
            "PROJECT",
            {
                "project_name": "P",
                "role_title": None,
                "project_url": "https://example.test",
                "start_month": None,
                "end_month": None,
            },
        ),
        ("SKILL", {"skill_name": "Python"}),
        ("AWARD", {"award_name": "A", "awarding_organization": None, "awarded_month": None}),
        (
            "CERTIFICATION",
            {"certification_name": "C", "issuing_organization": None, "issued_month": None},
        ),
    ],
)
def test_six_kind_selected_field_schemas(tmp_path: Path, kind: str, fields: object) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post("/api/v1/resumes", json=body(kind=kind, fields=fields))
        assert response.status_code == 200, response.text
        saved = response.json()["resume_version"]["sections"][0]
        assert saved["kind"] == kind and saved["members"][0]["fields"] == fields


@pytest.mark.parametrize(
    "field,value,code",
    [
        ("full_name", "", "BLANK_VALUE"),
        ("email", "a b@c", "INVALID_CHARACTERS"),
        ("phone_number", "12+3", "INVALID_FORMAT"),
        ("kind", True, "INVALID_TYPE"),
        ("fields", {}, "REQUIRED"),
        ("font_size_pt", "12", "INVALID_TYPE"),
        ("line_spacing_pt", 13, "OUT_OF_RANGE"),
    ],
)
def test_exact_value_admission(tmp_path: Path, field: str, value: object, code: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        command = body()
        if field in {"full_name", "email", "phone_number"}:
            cast(Json, command["contacts"])[field] = value
        elif field == "kind":
            cast(list[Json], command["sections"])[0][field] = value
        elif field == "fields":
            section = cast(list[Json], command["sections"])[0]
            cast(list[Json], section["members"])[0][field] = value
        else:
            cast(Json, command["document_presentation"])[field] = value
        response = client.post("/api/v1/resumes", json=command)
        assert response.status_code == 422
        assert_error(response, code)


def test_run_canonicalization_and_stable_id_uniqueness(tmp_path: Path) -> None:
    command = body()
    member = command["sections"][0]["members"][0]  # type: ignore[index]
    member["content"] = [  # type: ignore[index]
        {
            "type": "UNORDERED_LIST",
            "items": [
                {
                    "block_id": str(uuid4()),
                    "runs": [
                        {"text": "A", "marks": [{"type": "ITALIC"}, {"type": "BOLD"}]},
                        {"text": "B", "marks": [{"type": "BOLD"}, {"type": "ITALIC"}]},
                    ],
                }
            ],
        }
    ]
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post("/api/v1/resumes", json=command)
        assert response.status_code == 200, response.text
        runs = response.json()["resume_version"]["sections"][0]["members"][0]["content"][0][
            "items"
        ][0]["runs"]
        assert runs == [{"text": "AB", "marks": [{"type": "BOLD"}, {"type": "ITALIC"}]}]
        command["request_id"] = str(uuid4())
        command["sections"].append(command["sections"][0])  # type: ignore[union-attr,index]
        duplicate = client.post("/api/v1/resumes", json=command)
        assert duplicate.status_code == 422


def test_transport_media_query_and_json_shape(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        endpoint = "/api/v1/resumes"
        assert_error(client.post(endpoint, content=b"{}"), "BAD_REQUEST")
        assert_error(
            client.post(
                endpoint,
                content=b"{}",
                headers={"Content-Type": "application/json", "Content-Encoding": "gzip"},
            ),
            "BAD_REQUEST",
        )
        assert_error(client.post(endpoint + "?x=1", json=body()), "UNKNOWN_FIELD")
        assert_error(
            client.post(
                endpoint,
                content=b'{"request_id":"x","request_id":"y"}',
                headers={"Content-Type": "application/json"},
            ),
            "BAD_REQUEST",
        )
        assert_error(client.post(endpoint, json=[]), "INVALID_TYPE")
        assert client.get(endpoint + "?x=1").status_code == 422


def test_closed_fields_required_ids_and_exact_save_revision(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        command = body()
        command["unexpected"] = True
        response = client.post("/api/v1/resumes", json=command)
        assert_error(response, "UNKNOWN_FIELD", "$")
        command = body()
        del command["contacts"]
        assert_error(client.post("/api/v1/resumes", json=command), "REQUIRED", "contacts")

        created = client.post("/api/v1/resumes", json=body()).json()
        version = created["resume_version"]
        save = {
            key: version[key]
            for key in ("contacts", "header_presentation", "sections", "document_presentation")
        }
        save.update(request_id=str(uuid4()), revision=2)
        response = client.post(f"/api/v1/resumes/{created['resume']['resume_id']}/save", json=save)
        assert response.status_code == 409
        assert response.json()["code"] == "REVISION_CONFLICT"


def test_raw_body_limits_are_declared_and_enforced(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        schema = client.get("/openapi.json").json()
        assert schema["paths"]["/api/v1/resumes"]["post"]["x-max-body-bytes"] == 8_388_608
        huge = b'{"padding":"' + b"x" * 8_388_608 + b'"}'
        response = client.post(
            "/api/v1/resumes", content=huge, headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 413
        assert response.json()["code"] == "REQUEST_TOO_LARGE"
