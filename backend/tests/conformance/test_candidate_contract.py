"""Independent Resume codec and executable HTTP/OpenAPI agreement."""

import json
from decimal import Decimal
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

from fastapi.testclient import TestClient
from jobhunter.application.candidate.fingerprint import encode, fingerprint
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

Json = dict[str, Any]


def empty_resume() -> dict[str, object]:
    return {
        "request_id": str(uuid4()),
        "resume_name": "Independent",
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


def test_independent_codec_vector_and_sql_receipt(tmp_path: Path) -> None:
    fixture = cast(
        Json,
        json.loads((Path(__file__).parents[1] / "fixtures/candidate_fingerprint.json").read_text()),
    )
    assert (
        encode(
            [
                fixture["command_type"],
                fixture["target_id"],
                {k: v for k, v in fixture["body"].items() if k != "request_id"},
            ]
        ).decode()
        == fixture["encoded_utf8"]
    )
    assert (
        fingerprint(fixture["command_type"], fixture["target_id"], fixture["body"])
        == fixture["sha256"]
    )
    assert (
        encode([None, True, False, Decimal("-0.0"), Decimal("1.20e1"), "学"])
        == b"a6:nb1b0d1:0d2:12s3:\xe5\xad\xa6"
    )

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        created = client.post("/api/v1/resumes", json=empty_resume()).json()
        target = created["resume"]["resume_id"]
        body = {**fixture["body"], "request_id": str(uuid4())}
        response = client.post(f"/api/v1/resumes/{target}/rename", json=body)
        assert response.status_code == 200
        expected = fingerprint("RESUME_RENAME", target, cast(dict[str, object], body))
        with store.engine.connect() as conn:
            row = conn.exec_driver_sql(
                "SELECT request_fingerprint,schema_version FROM candidate_command_receipts "
                "WHERE request_id=?",
                (body["request_id"],),
            ).one()
        assert tuple(row) == (expected, 2)


def test_independent_resume_openapi_and_removed_routes(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        schema = client.get("/openapi.json").json()
        paths = schema["paths"]
        expected_posts = {
            "/api/v1/resumes",
            "/api/v1/resumes/{resume_id}/save",
            "/api/v1/resumes/{resume_id}/rename",
            "/api/v1/resumes/{resume_id}/remove",
            "/api/v1/workspace/default-resume/set",
            "/api/v1/workspace/portrait/refresh",
        }
        assert {
            path for path, operations in paths.items() if "post" in operations
        } >= expected_posts
        for path in (
            "/api/v1/profile",
            "/api/v1/evidence-items",
            "/api/v1/evidence-baselines/current",
        ):
            assert path not in paths
            assert client.get(path).status_code == 400
        schemas = schema["components"]["schemas"]
        assert "HTTPValidationError" not in schemas
        section = schemas["Section-Input"] if "Section-Input" in schemas else schemas["Section"]
        assert len(section["allOf"]) == 6
        assert schemas["ResumeCreate"]["additionalProperties"] is False
        assert schemas["ResumeVersion"]["properties"]["schema_version"]["const"] == 2
        for path in expected_posts:
            operation = paths[path]["post"]
            assert operation["x-max-json-nodes"] == 100000
            assert operation["x-max-json-container-depth"] == 32
            assert set(operation["requestBody"]["content"]) == {"application/json"}
            assert operation["responses"]["422"]["content"]["application/json"]["schema"][
                "$ref"
            ].endswith("/ContractError")
