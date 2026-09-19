import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.api.v1.manual_application_entries.routes import BASE
from jobhunter.application.manual_application_entries.service import Entries
from jobhunter.bootstrap.container import create_app
from jobhunter.domain.manual_application_entries.models import MAX_REVISION, CreateEntry
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


def payload() -> dict[str, object]:
    return dict(
        request_id=str(uuid4()),
        company_name="Acme",
        role_title="Engineer",
        application_url="https://example.test/apply?q=a%20b#step",
    )


@pytest.mark.parametrize(
    "field,value,code",
    [
        ("role_title", None, "INVALID_TYPE"),
        ("company_name", 3, "INVALID_TYPE"),
        ("company_name", "", "BLANK_VALUE"),
        ("company_name", "x" * 201, "TOO_LONG"),
        ("role_title", "\ud800", "INVALID_CHARACTERS"),
        ("role_title", "a\nb", "INVALID_CHARACTERS"),
        ("role_title", "a\u0085b", "INVALID_CHARACTERS"),
        ("request_id", "ABC", "INVALID_FORMAT"),
        ("request_id", None, "INVALID_TYPE"),
        ("application_url", "https://x.test:/", "INVALID_FORMAT"),
        ("application_url", "http://127.1/", "INVALID_FORMAT"),
        ("application_url", "https:////x.test", "INVALID_FORMAT"),
        ("application_url", "https://u:p@x.test/", "INVALID_FORMAT"),
        ("application_url", "https://x.test/%zz", "INVALID_FORMAT"),
        ("application_url", "http://x.test:65536", "INVALID_FORMAT"),
        ("application_url", "http://x.test:１２", "INVALID_FORMAT"),
        ("application_url", "javascript:alert(1)", "INVALID_FORMAT"),
        ("application_url", "http://x.test/a b", "INVALID_CHARACTERS"),
        ("application_url", "http://x.test/\\b", "INVALID_CHARACTERS"),
    ],
)
def test_field_admission(tmp_path: Path, field: str, value: object, code: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload()
        data[field] = value
        response = client.post(
            BASE, content=json.dumps(data), headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 422, response.text
        assert {"field": field, "code": code} in response.json()["field_errors"]
        assert client.get(BASE).json() == {"items": []}


@pytest.mark.parametrize(
    "url",
    [
        "HTTP://Example.test:80/./apply",
        "http://localhost",
        "http://[::1]/",
        "https://例子.测试/工程師?q=🦄",
        "http://x.test:0/",
        "https://example.test/" + "a" * 8100,
    ],
)
def test_preserved_text_url_and_fingerprint(tmp_path: Path, url: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload() | {
            "company_name": "\u0085🦄\u0085",
            "role_title": "\ufeff工程師",
            "application_url": url,
        }
        result = client.post(BASE, json=data)
        assert result.status_code == 200, result.text
        entry = client.get(BASE + "/" + result.json()["manual_application_entry_id"]).json()
        assert entry["company_name"] == "🦄"
        assert entry["role_title"] == "\ufeff工程師"
        assert entry["application_url"] == url
        encoded = b"ManualApplicationEntryCreate:v1\x00"
        for text in ("🦄", "\ufeff工程師", url):
            raw = text.encode()
            encoded += len(raw).to_bytes(4, "big") + raw
        with store.engine.connect() as conn:
            assert (
                conn.exec_driver_sql(
                    "SELECT request_fingerprint FROM manual_application_entry_create_receipts"
                ).scalar()
                == hashlib.sha256(encoded).hexdigest()
            )


def test_revision_noop_clock_delete_and_identity_fence(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload()
        result = client.post(BASE, json=data).json()
        identity = result["manual_application_entry_id"]
        path = BASE + "/" + identity
        prior = client.get(path).json()
        command = {key: data[key] for key in ("company_name", "role_title", "application_url")} | {
            "revision": 1
        }
        assert client.put(path, json=command).json() == prior
        entries = client.app.state.entries  # type: ignore[union-attr]
        entries.clock = lambda: "2000-01-01T00:00:00.000Z"
        command["company_name"] = "Changed"
        changed = client.put(path, json=command).json()
        assert changed["revision"] == 2
        assert changed["updated_at"] == prior["updated_at"]
        assert client.put(path, json=command).json()["code"] == "REVISION_CONFLICT"
        assert client.post(path + "/resolve-url", json={"revision": 1}).status_code == 409
        assert client.post(BASE, json=data).json() == result
        assert (
            client.post(BASE, json=data | {"company_name": "Changed"}).json()["code"]
            == "REQUEST_CONFLICT"
        )
        with store.engine.begin() as conn:
            conn.exec_driver_sql(
                "UPDATE manual_application_entries SET revision=?", (MAX_REVISION,)
            )
        command["revision"] = MAX_REVISION
        assert client.put(path, json=command).json()["revision"] == MAX_REVISION
        assert (
            client.put(path, json=command | {"role_title": "Other"}).json()["code"]
            == "REVISION_EXHAUSTED"
        )
        assert client.post(path + "/delete", json={"revision": MAX_REVISION}).status_code == 200
        assert client.post(path + "/delete", json={"revision": MAX_REVISION}).status_code == 404
        generated = iter([identity, str(uuid4())])
        service = Entries(store, new_id=lambda: next(generated))
        new = service.create(CreateEntry.model_validate(data | {"request_id": str(uuid4())}))
        assert new.manual_application_entry_id != identity


def test_concurrent_receipts_and_updates(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload()

        def create(_: int) -> str:
            return client.post(BASE, json=data).json()["manual_application_entry_id"]

        with ThreadPoolExecutor(max_workers=8) as pool:
            identities = list(pool.map(create, range(16)))
        assert len(set(identities)) == 1
        path = BASE + "/" + identities[0]

        def update(i: int) -> int:
            return client.put(
                path,
                json={
                    "revision": 1,
                    "company_name": str(i),
                    "role_title": "Engineer",
                    "application_url": "https://example.test",
                },
            ).status_code

        with ThreadPoolExecutor(max_workers=8) as pool:
            statuses = list(pool.map(update, range(8)))
        assert statuses.count(200) == 1
        assert statuses.count(409) == 7
        assert client.post(BASE, json=data | {"request_id": str(uuid4())}).status_code == 200
        assert len(client.get(BASE).json()["items"]) == 2


def test_transport_access_openapi(tmp_path: Path) -> None:
    with (
        Store.open(tmp_path) as store,
        TestClient(create_app(store, origins=("http://localhost:5173",))) as client,
    ):
        for headers in (
            {"Host": "evil.test"},
            {"Origin": "null"},
            {"Origin": "https://evil.test"},
        ):
            response = client.post(BASE, json=payload(), headers=headers)
            assert response.status_code == 403
            assert response.json()["field_errors"] == []
        assert (
            client.post(BASE, content="{}", headers={"Content-Type": "text/plain"}).status_code
            == 400
        )
        assert (
            client.post(BASE, content="{", headers={"Content-Type": "application/json"}).status_code
            == 400
        )
        assert client.post(BASE, json=[]).status_code == 422
        assert client.get(BASE + "?secret=hidden").json()["field_errors"] == [
            {"field": "$", "code": "UNKNOWN_FIELD"}
        ]
        response = client.post(BASE, json=payload() | {"secret": "hidden"})
        assert response.json()["field_errors"] == [{"field": "$", "code": "UNKNOWN_FIELD"}]
        assert "hidden" not in response.text
        data = payload()
        del data["role_title"]
        assert client.post(BASE, json=data).json()["field_errors"] == [
            {"field": "role_title", "code": "REQUIRED"}
        ]
        assert (
            client.get(BASE, headers={"Origin": "http://localhost:5173"}).headers[
                "Access-Control-Allow-Origin"
            ]
            == "http://localhost:5173"
        )
        schema = client.get("/openapi.json").json()
        assert len([p for p in schema["paths"] if p.startswith(BASE)]) == 4
        for path in schema["paths"].values():
            for route in path.values():
                assert route["responses"]["422"]["content"]["application/json"]["schema"][
                    "$ref"
                ].endswith("/ContractError")
        schemas = schema["components"]["schemas"]
        assert schemas["CreateEntry"]["additionalProperties"] is False
        assert schemas["ExpectedRevision"]["properties"]["revision"]["type"] == "integer"
        assert len(schemas["ManualApplicationEntry"]["required"]) == 7


@pytest.mark.parametrize("raw", ["null", "true", "1", '"text"'])
def test_non_object_root(tmp_path: Path, raw: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(BASE, content=raw, headers={"Content-Type": "application/json"})
        assert response.status_code == 422
        assert response.json()["field_errors"] == [{"field": "$", "code": "INVALID_TYPE"}]


@pytest.mark.parametrize(
    "value,code",
    [
        ("0", "OUT_OF_RANGE"),
        ("-1", "OUT_OF_RANGE"),
        ("9007199254740992", "OUT_OF_RANGE"),
        ("9007199254740991.1", "INVALID_TYPE"),
        ("1e-1000", "INVALID_TYPE"),
        ("1e1000", "OUT_OF_RANGE"),
        ("[]", "INVALID_TYPE"),
        ("{}", "INVALID_TYPE"),
    ],
)
def test_revision_limits(tmp_path: Path, value: str, code: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(
            BASE + "/" + str(uuid4()) + "/delete",
            content='{"revision":' + value + "}",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 422
        assert response.json()["field_errors"] == [{"field": "revision", "code": code}]


def test_complete_list_ties_and_resolve_readonly(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        service = Entries(store, clock=lambda: "2026-09-19T00:00:00.000Z")
        identities = [
            service.create(CreateEntry.model_validate(payload())).manual_application_entry_id
            for _ in range(35)
        ]
        before = service.list()
        assert [entry.manual_application_entry_id for entry in before.items] == sorted(identities)
        for identity in identities:
            service.resolve(identity, 1)
        assert service.list() == before


def test_validation_precedes_replay_and_existence(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload()
        assert client.post(BASE, json=data).status_code == 200
        assert client.post(BASE, json=data | {"role_title": None}).status_code == 422
        assert client.put(BASE + "/" + str(uuid4()), json={"revision": 1}).status_code == 422


def test_openapi_does_not_reject_admissible_outer_whitespace(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = payload() | {"company_name": " " * 20 + "x" * 200 + " " * 20}
        assert client.post(BASE, json=data).status_code == 200
        schema = client.get("/openapi.json").json()
        company = schema["components"]["schemas"]["CreateEntry"]["properties"]["company_name"]
        assert "maxLength" not in company
        assert company["x-post-trim-maxLength"] == 200


def test_privacy_invalid_url_logging(tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    import logging

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        with caplog.at_level(logging.DEBUG, logger="urlstd"):
            response = client.post(
                BASE, json=payload() | {"application_url": "https://secret.test:999999/private"}
            )
        assert response.status_code == 422
        assert "secret.test" not in caplog.text
        assert "private" not in response.text


@pytest.mark.parametrize(
    "url",
    ["http://example.test:" + "9" * 5000, "http://" + "9" * 5000],
    ids=["long-port", "long-host"],
)
def test_oversized_numeric_url_parts_are_format_errors(tmp_path: Path, url: str) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(BASE, json=payload() | {"application_url": url})
        assert response.status_code == 422
        assert response.json()["field_errors"] == [
            {"field": "application_url", "code": "INVALID_FORMAT"}
        ]


def test_openapi_operation_error_statuses(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        paths = client.get("/openapi.json").json()["paths"]
        assert "409" not in paths[BASE]["get"]["responses"]
        assert "404" not in paths[BASE]["post"]["responses"]


def test_valid_zero_padded_port_preserved(tmp_path: Path) -> None:
    url = "http://example.test:" + "0" * 5000 + "80/"
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        result = client.post(BASE, json=payload() | {"application_url": url})
        assert result.status_code == 200
        assert client.get(BASE).json()["items"][0]["application_url"] == url
