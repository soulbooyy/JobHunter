"""Transport and canonical-value conformance through the actual saved-authority API."""

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store

Json = dict[str, Any]


@pytest.fixture
def client(tmp_path: Path) -> Iterator[TestClient]:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        yield client


def profile(**values: Any) -> Json:
    return {
        "request_id": str(uuid4()),
        "revision": 1,
        "full_name": None,
        "phone_number": None,
        "email": None,
        **values,
    }


def resume(client: TestClient) -> Json:
    return {
        "request_id": str(uuid4()),
        "resume_name": "Name",
        "profile_version_id": client.get("/api/v1/profile").json()["profile_version"][
            "profile_version_id"
        ],
        "header_presentation": {"optional_items": []},
        "sections": [],
        "document_presentation": {
            "font_family": "HEITI",
            "font_size_pt": 12,
            "line_spacing_pt": 14,
            "theme_color": "#123abc",
        },
    }


@pytest.mark.parametrize(
    "field,value,code",
    [
        ("full_name", "", "BLANK_VALUE"),
        ("full_name", "a" * 101, "TOO_LONG"),
        ("full_name", True, "INVALID_TYPE"),
        ("full_name", "a\x00b", "INVALID_CHARACTERS"),
        ("full_name", "\ud800", "INVALID_CHARACTERS"),
        ("phone_number", " +12 (3)-4 ", None),
        ("phone_number", "１２", "INVALID_FORMAT"),
        ("phone_number", "+()-", "INVALID_FORMAT"),
        ("phone_number", "12+3", "INVALID_FORMAT"),
        ("email", " a@b ", None),
        ("email", "@b", "INVALID_FORMAT"),
        ("email", "a@b@c", "INVALID_FORMAT"),
        ("email", "a b@c", "INVALID_CHARACTERS"),
        ("revision", True, "INVALID_TYPE"),
        ("revision", "1", "INVALID_TYPE"),
        ("revision", 0, "OUT_OF_RANGE"),
    ],
)
def test_profile_values(client: TestClient, field: str, value: Any, code: str | None) -> None:
    response = client.post(
        "/api/v1/profile/save",
        content=json.dumps(profile(**{field: value})),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == (200 if code is None else 422), response.text
    if code:
        assert response.json()["field_errors"] == [{"field": field, "code": code}]


@pytest.mark.parametrize(
    "kind,fields",
    [
        (
            "EDUCATION",
            {
                "school_name": " 学校 ",
                "degree": "MBA",
                "major": None,
                "start_month": "0001-01",
                "end_month": "9999-12",
            },
        ),
        (
            "WORK_EXPERIENCE",
            {
                "company_name": "Employer",
                "role_title": "Role",
                "start_month": None,
                "end_month": None,
            },
        ),
        (
            "PROJECT",
            {
                "project_name": "Project",
                "role_title": None,
                "project_url": "HTTPS://Example.test:443/a%2Fb?x=1#f",
                "start_month": None,
                "end_month": None,
            },
        ),
        ("SKILL", {"skill_name": "Python"}),
        ("AWARD", {"award_name": "Award", "awarding_organization": None, "awarded_month": None}),
        (
            "CERTIFICATION",
            {"certification_name": "Cert", "issuing_organization": None, "issued_month": "2020-01"},
        ),
    ],
)
def test_six_exact_schemas(client: TestClient, kind: str, fields: Json) -> None:
    body: Json = {
        "request_id": str(uuid4()),
        "kind": kind,
        "fields": fields,
        "content": [{"type": "UNORDERED_LIST", "items": [" <b>literal</b> ", "same", "same"]}],
    }
    result = client.post("/api/v1/evidence-items", json=body)
    assert result.status_code == 200, result.text
    saved = result.json()
    assert saved["evidence_item"]["kind"] == kind
    assert saved["evidence_item_version"]["content"][0]["items"] == [
        "<b>literal</b>",
        "same",
        "same",
    ]
    if kind == "PROJECT":
        assert saved["evidence_item_version"]["fields"]["project_url"] == fields["project_url"]
    eid = saved["evidence_item"]["evidence_item_id"]
    missing = dict(fields)
    omitted = next(iter(fields))
    missing.pop(omitted)
    error = client.post(
        f"/api/v1/evidence-items/{eid}/save",
        json={"request_id": str(uuid4()), "revision": 1, "fields": missing, "content": []},
    )
    assert error.status_code == 422
    assert error.json()["field_errors"] == [{"field": "fields." + omitted, "code": "REQUIRED"}]
    error = client.post(
        f"/api/v1/evidence-items/{eid}/save",
        json={
            "request_id": str(uuid4()),
            "revision": 1,
            "fields": {**fields, "SECRET-UNKNOWN": 0},
            "content": [],
        },
    )
    assert error.json()["field_errors"] == [{"field": "fields", "code": "UNKNOWN_FIELD"}]
    assert "SECRET-UNKNOWN" not in error.text


@pytest.mark.parametrize(
    "start,end,code",
    [
        ("0000-01", None, "INVALID_FORMAT"),
        ("2026-1", None, "INVALID_FORMAT"),
        (" 2026-01", None, "INVALID_FORMAT"),
        ("2026-13", None, "INVALID_FORMAT"),
        ("2026-12", "2026-11", "INVALID_FORMAT"),
        ("2026-12", "2026-12", None),
    ],
)
def test_months(client: TestClient, start: str, end: str | None, code: str | None) -> None:
    body: Json = {
        "request_id": str(uuid4()),
        "kind": "WORK_EXPERIENCE",
        "fields": {"company_name": "C", "role_title": "R", "start_month": start, "end_month": end},
        "content": [],
    }
    response = client.post("/api/v1/evidence-items", json=body)
    assert response.status_code == (422 if code else 200)
    if code:
        assert response.json()["field_errors"][0]["code"] == code


BODY_CASES: list[tuple[list[Json], str, str]] = [
    ([{"type": "PARAGRAPH", "text": "\ttrim"}], "INVALID_CHARACTERS", "content[0].text"),
    ([{"type": "PARAGRAPH", "text": " "}], "BLANK_VALUE", "content[0].text"),
    ([{"type": "PARAGRAPH", "text": "a" * 10001}], "TOO_LONG", "content[0].text"),
    ([{"type": "ORDERED_LIST", "items": []}], "OUT_OF_RANGE", "content[0].items"),
    ([{"type": "ORDERED_LIST", "items": ["ok"] * 101}], "OUT_OF_RANGE", "content[0].items"),
    ([{"type": "PARAGRAPH", "text": "x"}] * 101, "OUT_OF_RANGE", "content"),
    ([{"type": "PARAGRAPH", "text": "a" * 10000}] * 6, "OUT_OF_RANGE", "content"),
    (
        [{"type": "PARAGRAPH", "text": "okay", "private-unknown": "sensitive"}],
        "UNKNOWN_FIELD",
        "content[0]",
    ),
    ([{"type": "HTML", "text": "okay"}], "INVALID_FORMAT", "content[0].type"),
]


@pytest.mark.parametrize("content,code,path", BODY_CASES)
def test_evidence_plain_body(client: TestClient, content: list[Json], code: str, path: str) -> None:
    response = client.post(
        "/api/v1/evidence-items",
        json={
            "request_id": str(uuid4()),
            "kind": "SKILL",
            "fields": {"skill_name": "S"},
            "content": content,
        },
    )
    assert response.status_code == 422
    assert response.json()["field_errors"] == [{"field": path, "code": code}]


@pytest.mark.parametrize(
    "number,accepted",
    [
        ("12.0", True),
        ("1.2e1", True),
        ("12.5", True),
        ("12.50000000000000000000000000000000001", False),
        ("11.999999999999999999999999999999999", False),
        ("true", False),
        ('"12"', False),
    ],
)
def test_exact_presentation_numbers(client: TestClient, number: str, accepted: bool) -> None:
    body = resume(client)
    body["document_presentation"]["line_spacing_pt"] = 16
    raw = json.dumps(body).replace('"font_size_pt": 12', '"font_size_pt": ' + number)
    response = client.post(
        "/api/v1/resumes", content=raw, headers={"content-type": "application/json"}
    )
    assert response.status_code == (200 if accepted else 422), response.text


@pytest.mark.parametrize(
    "raw,status,code",
    [
        (b'{"x":0,"\\u0078":1}', 400, "BAD_REQUEST"),
        (b'{"x":{"y":1,"y":2}}', 400, "BAD_REQUEST"),
        (b"[]", 422, "VALIDATION_ERROR"),
        (b'{"x":NaN}', 400, "BAD_REQUEST"),
        (b'{"x":' + b"[" * 32 + b"0" + b"]" * 32 + b"}", 422, "VALIDATION_ERROR"),
        (b'{"x":[' + b"0," * 99999 + b"0]}", 422, "VALIDATION_ERROR"),
    ],
)
def test_raw_json(client: TestClient, raw: bytes, status: int, code: str) -> None:
    response = client.post(
        "/api/v1/evidence-items", content=raw, headers={"content-type": "application/json"}
    )
    assert response.status_code == status
    assert response.json()["code"] == code
    if len(raw) > 1000 or raw.count(b"[") > 30:
        assert response.json()["field_errors"] == [{"field": "$", "code": "STRUCTURE_TOO_COMPLEX"}]


def test_transport_access_media_budgets_and_get_shape(client: TestClient) -> None:
    for path, budget in [
        ("/profile/save", 65536),
        ("/evidence-items", 1048576),
        ("/resumes", 8388608),
    ]:
        response = client.post(
            "/api/v1" + path,
            content=b" " * (budget + 1),
            headers={"content-type": "application/json"},
        )
        assert response.status_code == 413
        assert response.json()["field_errors"] == []
    for headers in [
        {"content-type": "text/plain"},
        {"content-type": "application/json; charset=latin-1"},
        {"content-type": "application/json", "content-encoding": "gzip"},
    ]:
        assert (
            client.post("/api/v1/profile/save", content=b"{}", headers=headers).status_code == 400
        )
    assert client.post("/api/v1/profile/save?unknown=value", json=profile()).json()[
        "field_errors"
    ] == [{"field": "$", "code": "UNKNOWN_FIELD"}]
    assert client.request("GET", "/api/v1/profile", content=b"{}").status_code == 422
    assert client.get("/api/v1/resumes?sort=x").status_code == 422
    for headers in [{"Host": "evil.test"}, {"Origin": "http://evil.test"}]:
        assert client.get("/api/v1/profile", headers=headers).status_code == 403
    assert client.get("/api/v1/resumes/not-a-uuid").json()["field_errors"] == [
        {"field": "resume_id", "code": "INVALID_FORMAT"}
    ]


def test_required_fields_and_exact_revision(client: TestClient) -> None:
    raw = json.dumps(profile()).replace(
        '"revision": 1', '"revision": 1.00000000000000000000000000000000001'
    )
    assert (
        client.post(
            "/api/v1/profile/save", content=raw, headers={"content-type": "application/json"}
        ).status_code
        == 422
    )
    for field in profile():
        body = profile()
        body.pop(field)
        assert client.post("/api/v1/profile/save", json=body).json()["field_errors"] == [
            {"field": field, "code": "REQUIRED"}
        ]


RUN_CASES: list[tuple[list[Json], str | None]] = [
    ([{"text": "", "marks": []}, {"text": "ok", "marks": []}], "BLANK_VALUE"),
    ([{"text": "\t", "marks": []}, {"text": "ok", "marks": []}], "INVALID_CHARACTERS"),
    (
        [{"text": " ", "marks": [{"type": "BOLD"}]}, {"text": "ok", "marks": []}],
        "INVALID_FORMAT",
    ),
    ([{"text": "ok", "marks": [{"type": "BOLD"}, {"type": "BOLD"}]}], "INVALID_FORMAT"),
    (
        [{"text": "ok", "marks": [{"type": "LINK", "url": "javascript:alert(1)"}]}],
        "INVALID_FORMAT",
    ),
    ([{"text": "a" * 10001, "marks": []}], "TOO_LONG"),
    (
        [{"text": "x", "marks": [{"type": "BOLD"}] if i % 2 else []} for i in range(257)],
        "OUT_OF_RANGE",
    ),
    ([{"text": "x", "marks": []} for _ in range(300)], None),
    (
        [
            {"text": "\u00a0\u3000", "marks": []},
            {
                "text": "text",
                "marks": [{"type": "LINK", "url": "HTTPS://Example.test:443/a%2Fb#f"}],
            },
        ],
        None,
    ),
]


@pytest.mark.parametrize("runs,code", RUN_CASES)
def test_raw_runs_and_canonical_limits(
    client: TestClient, runs: list[Json], code: str | None
) -> None:
    evidence = client.post(
        "/api/v1/evidence-items",
        json={
            "request_id": str(uuid4()),
            "kind": "SKILL",
            "fields": {"skill_name": "S"},
            "content": [],
        },
    ).json()
    command = resume(client)
    command["sections"] = [
        {
            "kind": "SKILL",
            "members": [
                {
                    "evidence_item_id": evidence["evidence_item"]["evidence_item_id"],
                    "evidence_item_version_id": evidence["evidence_item_version"][
                        "evidence_item_version_id"
                    ],
                    "content": [{"type": "PARAGRAPH", "runs": runs}],
                }
            ],
        }
    ]
    response = client.post("/api/v1/resumes", json=command)
    assert response.status_code == (200 if code is None else 422), response.text
    if code:
        assert response.json()["field_errors"][0]["code"] == code
    else:
        result = response.json()["resume_version"]["sections"][0]["members"][0]["content"][0][
            "runs"
        ]
        assert "".join(r["text"] for r in result) == "".join(r["text"] for r in runs)
        if len(runs) == 300:
            assert result == [{"text": "x" * 300, "marks": []}]


@pytest.mark.parametrize(
    "value,code", [(True, "INVALID_TYPE"), (None, "INVALID_TYPE"), ("\ud800", "INVALID_CHARACTERS")]
)
def test_discriminator_scalar_errors(client: TestClient, value: Any, code: str) -> None:
    raw = json.dumps(
        {
            "request_id": str(uuid4()),
            "kind": "SKILL",
            "fields": {"skill_name": "S"},
            "content": [{"type": value, "text": "x"}],
        }
    )
    response = client.post(
        "/api/v1/evidence-items", content=raw, headers={"content-type": "application/json"}
    )
    assert response.status_code == 422
    assert response.json()["field_errors"] == [{"field": "content[0].type", "code": code}]


def test_document_count_text_duplicates_and_presentation(client: TestClient) -> None:
    command = resume(client)
    command["document_presentation"]["line_spacing_pt"] = 14.5
    command["document_presentation"]["font_size_pt"] = 13
    error = client.post("/api/v1/resumes", json=command).json()
    assert error["field_errors"] == [{"field": "document_presentation", "code": "INVALID_FORMAT"}]
    command["document_presentation"]["font_size_pt"] = 12
    command["header_presentation"]["optional_items"] = [{"kind": "GENDER", "value": "wording"}] * 2
    assert client.post("/api/v1/resumes", json=command).json()["field_errors"] == [
        {"field": "header_presentation.optional_items", "code": "INVALID_FORMAT"}
    ]
    command["header_presentation"]["optional_items"] = []
    member: Json = {
        "evidence_item_id": str(uuid4()),
        "evidence_item_version_id": str(uuid4()),
        "content": [],
    }
    command["sections"] = [{"kind": "SKILL", "members": [member, member]}]
    assert client.post("/api/v1/resumes", json=command).json()["field_errors"] == [
        {"field": "sections", "code": "INVALID_FORMAT"}
    ]
    command["sections"] = [
        {
            "kind": "SKILL",
            "members": [
                {
                    **member,
                    "evidence_item_id": str(uuid4()),
                    "content": [{"type": "PARAGRAPH", "runs": [{"text": "x" * 10000, "marks": []}]}]
                    * 5,
                }
                for _ in range(5)
            ],
        }
    ]
    assert client.post("/api/v1/resumes", json=command).json()["field_errors"] == [
        {"field": "sections", "code": "OUT_OF_RANGE"}
    ]
