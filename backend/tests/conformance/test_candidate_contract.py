"""Independent codec vector and executable HTTP/OpenAPI agreement."""

import json
from decimal import Decimal
from pathlib import Path

from fastapi.testclient import TestClient
from jobhunter.application.candidate.fingerprint import encode, fingerprint
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def test_independent_codec_vector_and_sql_receipt(tmp_path: Path) -> None:
    fixture = json.loads(
        (Path(__file__).parents[1] / "fixtures/candidate_fingerprint.json").read_text()
    )
    assert (
        encode(
            [
                fixture["command_type"],
                None,
                {k: v for k, v in fixture["body"].items() if k != "request_id"},
            ]
        ).decode()
        == fixture["encoded_utf8"]
    )
    assert fingerprint(fixture["command_type"], None, fixture["body"]) == fixture["sha256"]
    assert (
        encode([None, True, False, Decimal("-0.0"), Decimal("1.20e1"), "学"])
        == b"a6:nb1b0d1:0d2:12s3:\xe5\xad\xa6"
    )
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        body = {**fixture["body"], "full_name": " 学 "}
        assert client.post("/api/v1/profile/save", json=body).status_code == 200
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT request_fingerprint FROM candidate_command_receipts"
                ).scalar_one()
                == fixture["sha256"]
            )
            row = conn.exec_driver_sql(
                "SELECT result_snapshot FROM candidate_command_receipts"
            ).scalar_one()
            snapshot = json.loads(row)
            assert set(snapshot) == {"profile", "profile_version_id"}
            assert "full_name" not in row


def test_saved_authority_openapi_and_closed_response_schemas(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        schema = client.get("/openapi.json").json()
        paths = {
            path: value
            for path, value in schema["paths"].items()
            if path.startswith(
                (
                    "/api/v1/profile",
                    "/api/v1/evidence-",
                    "/api/v1/resumes",
                    "/api/v1/workspace/default-resume",
                )
            )
        }
        assert sum("post" in operations for operations in paths.values()) == 9
        assert sum("get" in operations for operations in paths.values()) == 10
        schemas = schema["components"]["schemas"]
        assert "HTTPValidationError" not in schemas
        assert len(schemas["EvidenceCreate"]["allOf"]) == 6
        assert len(schemas["EvidenceUpdate"]["properties"]["fields"]["oneOf"]) == 6
        assert schemas["ProfileSave"]["additionalProperties"] is False
        assert schemas["ProfileSave"]["required"] == [
            "full_name",
            "phone_number",
            "email",
            "request_id",
            "revision",
        ]
        assert schemas["ResumeRemove"]["properties"]["default_resume_selection"]["$ref"].endswith(
            "/SelectionToken"
        )
        assert schemas["Presentation"]["properties"]["font_size_pt"]["multipleOf"] == 0.5
        for operations in paths.values():
            for method, op in operations.items():
                assert op["responses"]["422"]["content"]["application/json"]["schema"][
                    "$ref"
                ].endswith("/ContractError")
                assert "200" in op["responses"]
                if method == "post":
                    assert op["x-max-json-nodes"] == 100000
                    assert op["x-max-json-container-depth"] == 32
                    assert set(op["requestBody"]["content"]) == {"application/json"}
        for path in [
            "/api/v1/profile",
            "/api/v1/evidence-items",
            "/api/v1/evidence-baselines/current",
            "/api/v1/resumes",
        ]:
            assert client.get(path).status_code == 200
