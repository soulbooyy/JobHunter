"""PRF/COM boundary fixtures across HTTP, Application and SQLite."""

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from httpx import Response
from jobhunter.bootstrap.container import create_app
from jobhunter.domain.preferences.models import SavePreferences, fingerprint
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store, no_fault

BASE = "/api/v1/preferences"


def command() -> dict[str, Any]:
    return json.loads((Path(__file__).parents[1] / "fixtures/preference_save.json").read_text())


@pytest.mark.parametrize(
    "field,value,path,code",
    [
        ("target_job_keywords", None, "target_job_keywords", "INVALID_TYPE"),
        ("target_job_keywords", [], "target_job_keywords", "OUT_OF_RANGE"),
        ("target_job_keywords", [" ", "Python"], "target_job_keywords[0]", "BLANK_VALUE"),
        ("target_job_keywords", ["x", "\ud800"], "target_job_keywords[1]", "INVALID_CHARACTERS"),
        ("target_job_keywords", ["x", "bad\ntext"], "target_job_keywords[1]", "INVALID_CHARACTERS"),
        ("target_job_keywords", ["x" * 101], "target_job_keywords[0]", "TOO_LONG"),
        ("target_job_keywords", ["x"] * 1001, "target_job_keywords", "OUT_OF_RANGE"),
        ("target_job_keywords", [str(i) for i in range(21)], "target_job_keywords", "OUT_OF_RANGE"),
        ("accepted_cities", {"mode": "LIMITED"}, "accepted_cities.value", "REQUIRED"),
        (
            "accepted_cities",
            {"mode": "limited", "value": ["x"]},
            "accepted_cities.mode",
            "INVALID_FORMAT",
        ),
        ("accepted_cities", {"mode": True}, "accepted_cities.mode", "INVALID_TYPE"),
        ("accepted_cities", {"value": ["x"]}, "accepted_cities.mode", "REQUIRED"),
        (
            "accepted_cities",
            {"mode": "UNLIMITED", "value": None},
            "accepted_cities",
            "INVALID_FORMAT",
        ),
        (
            "accepted_cities",
            {"mode": "UNLIMITED", "private_secret": 1},
            "accepted_cities",
            "UNKNOWN_FIELD",
        ),
        (
            "minimum_salary",
            {"mode": "LIMITED", "value": True},
            "minimum_salary.value",
            "INVALID_TYPE",
        ),
        (
            "minimum_salary",
            {"mode": "LIMITED", "value": "15000"},
            "minimum_salary.value",
            "INVALID_TYPE",
        ),
        (
            "minimum_salary",
            {"mode": "LIMITED", "value": 300001},
            "minimum_salary.value",
            "OUT_OF_RANGE",
        ),
        ("minimum_salary", {"mode": "LIMITED", "value": 0}, "minimum_salary.value", "OUT_OF_RANGE"),
        (
            "recruitment_types",
            {"mode": "LIMITED", "value": ["CAMPUS", "UNLIMITED"]},
            "recruitment_types.value[1]",
            "INVALID_FORMAT",
        ),
        (
            "max_required_education",
            {"mode": "LIMITED", "value": "HIGH_SCHOOL"},
            "max_required_education.value",
            "INVALID_FORMAT",
        ),
    ],
)
def test_field_admission(tmp_path: Path, field: str, value: object, path: str, code: str) -> None:
    data = command()
    data["configuration"][field] = value
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(
            BASE + "/save", content=json.dumps(data), headers={"content-type": "application/json"}
        )
        assert response.status_code == 422, response.text
        assert response.json()["field_errors"] == [{"field": "configuration." + path, "code": code}]
        assert "private_secret" not in response.text
        assert client.get(BASE).json() == {"status": "NOT_CONFIGURED"}


@pytest.mark.parametrize(
    "number,code",
    [
        ("15000.0", None),
        ("1.5e4", None),
        ("15000.000000000000000001", "INVALID_TYPE"),
        ("300000.000000000000000001", "INVALID_TYPE"),
        ("1e1000", "OUT_OF_RANGE"),
        ("1e-1000", "INVALID_TYPE"),
    ],
)
def test_exact_salary_numbers(tmp_path: Path, number: str, code: str | None) -> None:
    raw = json.dumps(command()).replace("15000", number)
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        response = client.post(
            BASE + "/save",
            content=raw,
            headers={"content-type": 'Application/JSON; charset="UTF-8"'},
        )
        if code:
            assert response.json()["field_errors"] == [
                {"field": "configuration.minimum_salary.value", "code": code}
            ]
        else:
            assert response.status_code == 200
            assert (
                client.get(BASE).json()["current_preference_set_version"]["configuration"][
                    "minimum_salary"
                ]["value"]
                == 15000
            )


def test_independent_fingerprint_and_canonicalization() -> None:
    # PRF-013 literal byte vector: counts and UTF-8 lengths written independently.
    expected = (
        b"PreferenceSetSave:v1\x00\x00"
        b"\x00\x00\x00\x02\x00\x00\x00\x06Python\x00\x00\x00\x09"
        + "工程师".encode()
        + b"\x01\x00\x00\x00\x02\x00\x00\x00\x06"
        + "北京".encode()
        + b"\x00\x00\x00\x06"
        + "深圳".encode()
        + b"\x01\x00\x00\x3a\x98"
        b"\x01\x00\x00\x00\x03\x00\x00\x00\x06CAMPUS\x00\x00\x00\x0aINTERNSHIP\x00\x00\x00\x09PART_TIME"
        b"\x01\x00\x00\x00\x01\x00\x00\x00\x04ACME"
        b"\x01\x00\x00\x00\x08BACHELOR"
    )
    data = command()
    admitted = SavePreferences.model_validate(data)
    assert fingerprint(admitted) == hashlib.sha256(expected).hexdigest()
    data["request_id"] = str(uuid4())
    data["configuration"]["target_job_keywords"] = ["工程师", "Python"]
    assert fingerprint(SavePreferences.model_validate(data)) == fingerprint(admitted)
    data["revision"] = 1
    assert fingerprint(SavePreferences.model_validate(data)) != fingerprint(admitted)
    data["configuration"]["target_job_keywords"] = [
        "\U00010000",
        "\ue000",
        " a,b ",
        "A",
        "a",
        "e\u0301",
        "é",
    ]
    assert SavePreferences.model_validate(data).configuration.target_job_keywords == [
        "A",
        "a",
        "a,b",
        "e\u0301",
        "é",
        "\ue000",
        "\U00010000",
    ]


@pytest.mark.parametrize("mode", ["matching", "different_content", "distinct_ids"])
def test_first_save_races(tmp_path: Path, mode: str) -> None:
    first, second = command(), command()
    if mode == "different_content":
        second["configuration"]["target_job_keywords"] = ["Other"]
    if mode == "distinct_ids":
        second["request_id"] = str(uuid4())
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:

        def post(data: dict[str, Any]) -> Response:
            return client.post(BASE + "/save", json=data)

        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(post, [first, second]))
        assert sorted(r.status_code for r in results) == (
            [200, 200] if mode == "matching" else [200, 409]
        )
        if mode == "matching":
            assert results[0].json() == results[1].json()
        else:
            failed = next(r for r in results if r.status_code == 409)
            assert failed.json()["code"] == (
                "REQUEST_CONFLICT" if mode == "different_content" else "REVISION_CONFLICT"
            )
        with store.engine.connect() as conn:
            for table in ("preference_sets", "preference_set_versions", "preference_save_receipts"):
                assert conn.exec_driver_sql(f"SELECT count(*) FROM {table}").scalar() == 1


@pytest.mark.parametrize(
    "stage,code,count",
    [
        ("preferences_after_publication", "STORAGE_UNAVAILABLE", 0),
        ("preferences_after_receipt", "STORAGE_UNAVAILABLE", 0),
        ("before_commit", "STORAGE_UNAVAILABLE", 0),
        ("commit_before_driver", "OUTCOME_UNKNOWN", 0),
        ("commit_after_driver", "OUTCOME_UNKNOWN", 1),
        ("response_after_commit", "OUTCOME_UNKNOWN", 1),
    ],
)
def test_save_atomicity_and_uncertainty(
    tmp_path: Path, stage: str, code: str, count: int, caplog: pytest.LogCaptureFixture
) -> None:
    seen: list[str] = []

    def fault(point: str) -> None:
        seen.append(point)
        if point == stage:
            raise OSError("secret preference and SQL parameter")

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        store.fault = fault
        response = client.post(BASE + "/save", json=command())
        assert response.status_code == 503
        assert response.json()["code"] == code
        assert "secret" not in response.text + caplog.text
        assert seen.count("preferences_after_publication") == 1
        store.fault = no_fault
        with store.engine.connect() as conn:
            for table in ("preference_sets", "preference_set_versions", "preference_save_receipts"):
                assert conn.exec_driver_sql(f"SELECT count(*) FROM {table}").scalar() == count
        assert client.post(BASE + "/save", json=command()).status_code == 200


def test_revision_clock_and_return_to_original(tmp_path: Path) -> None:
    from jobhunter.application.candidate.preferences import Preferences

    with Store.open(tmp_path) as store:
        preferences = Preferences(store, clock=lambda: "2026-09-20T01:00:00.000Z")
        data = command()
        first = preferences.save(SavePreferences.model_validate(data))
        preferences.clock = lambda: "2026-09-19T01:00:00.000Z"
        data.update(request_id=str(uuid4()), revision=1)
        data["configuration"]["target_job_keywords"] = ["B"]
        second = preferences.save(SavePreferences.model_validate(data))
        data: dict[str, Any] = command() | {"revision": 2, "request_id": str(uuid4())}
        third = preferences.save(SavePreferences.model_validate(data))
        assert len({r.preference_set_version_id for r in (first, second, third)}) == 3
        assert (
            preferences.version(third.preference_set_version_id).created_at
            == "2026-09-20T01:00:00.000Z"
        )
        with TestClient(create_app(store)) as client:
            stale = client.post(
                BASE + "/save", json=command() | {"revision": 1, "request_id": str(uuid4())}
            )
            assert stale.json()["code"] == "REVISION_CONFLICT"
            with store.engine.begin() as conn:
                conn.exec_driver_sql("UPDATE preference_sets SET revision=9007199254740991")
            data: dict[str, Any] = command() | {
                "revision": 9007199254740991,
                "request_id": str(uuid4()),
            }
            assert client.post(BASE + "/save", json=data).json()["outcome"] == "UNCHANGED"
            data["request_id"] = str(uuid4())
            data["configuration"]["target_job_keywords"] = ["change"]
            assert client.post(BASE + "/save", json=data).json()["code"] == "REVISION_EXHAUSTED"


def test_transport_limits_openapi_and_access(tmp_path: Path) -> None:
    with (
        Store.open(tmp_path) as store,
        TestClient(create_app(store, origins=("http://localhost:5173",))) as client,
    ):
        for raw in (b'{"x":1,"\\u0078":2}', b'{"a":{"x":1,"x":2}}', b"\xff", b"{", b'{"x":NaN}'):
            assert (
                client.post(
                    BASE + "/save", content=raw, headers={"content-type": "application/json"}
                ).json()["code"]
                == "BAD_REQUEST"
            )
        for headers in (
            {"content-type": "text/plain"},
            {"content-type": "application/json; charset=latin1"},
            {"content-type": "application/json", "content-encoding": "gzip"},
        ):
            assert client.post(BASE + "/save", content=b"{}", headers=headers).status_code == 400
        raw = json.dumps(command()).encode()
        exact = raw + b" " * (1048576 - len(raw))
        assert (
            client.post(
                BASE + "/save", content=exact, headers={"content-type": "application/json"}
            ).status_code
            == 200
        )
        assert (
            client.post(
                BASE + "/save", content=exact + b" ", headers={"content-type": "application/json"}
            ).status_code
            == 413
        )
        assert client.request("GET", BASE, content=b"x").status_code == 422
        assert client.get(BASE + "?unknown=secret").json()["field_errors"] == [
            {"field": "$", "code": "UNKNOWN_FIELD"}
        ]
        for headers in (
            {"host": "evil.test"},
            {"origin": "null"},
            {"origin": "http://localhost:9999"},
        ):
            assert client.post(BASE + "/save", content=b"{", headers=headers).status_code == 403
        assert (
            client.get(BASE, headers={"origin": "http://localhost:5173"}).headers[
                "access-control-allow-origin"
            ]
            == "http://localhost:5173"
        )
        assert client.get(BASE + "/versions/" + str(uuid4())).status_code == 404
        assert client.get(BASE + "/versions/invalid").json()["field_errors"] == [
            {"field": "preference_set_version_id", "code": "INVALID_FORMAT"}
        ]
        schema = client.get("/openapi.json").json()
        paths = {path for path in schema["paths"] if path.startswith(BASE)}
        assert paths == {BASE, BASE + "/save", BASE + "/versions/{preference_set_version_id}"}
        for path in paths:
            for operation in schema["paths"][path].values():
                assert operation["responses"]["422"]["content"]["application/json"]["schema"][
                    "$ref"
                ].endswith("/ContractError")
        schemas = schema["components"]["schemas"]
        assert schemas["SavePreferences"]["required"] == ["request_id", "revision", "configuration"]
        assert {"type": "null"} in schemas["SavePreferences"]["properties"]["revision"]["anyOf"]
        assert (
            schemas["Configuration-Input"]["properties"]["target_job_keywords"]["maxItems"] == 1000
        )
        assert (
            schemas["Configuration-Output"]["properties"]["target_job_keywords"]["maxItems"] == 20
        )


def test_absence_preconditions_validation_precedes_replay(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = command()
        assert (
            client.post(BASE + "/save", json=data | {"revision": 1}).json()["code"]
            == "REVISION_CONFLICT"
        )
        for revision, code in [(True, "INVALID_TYPE"), ("1", "INVALID_TYPE"), (0, "OUT_OF_RANGE")]:
            assert client.post(BASE + "/save", json=data | {"revision": revision}).json()[
                "field_errors"
            ] == [{"field": "revision", "code": code}]
        missing = dict(data)
        del missing["revision"]
        assert client.post(BASE + "/save", json=missing).json()["field_errors"] == [
            {"field": "revision", "code": "REQUIRED"}
        ]
        first = client.post(BASE + "/save", json=data).json()
        invalid = command()
        invalid["configuration"]["target_job_keywords"] = []
        assert client.post(BASE + "/save", json=invalid).status_code == 422
        assert (
            client.post(BASE + "/save", json=data | {"revision": 1}).json()["code"]
            == "REQUEST_CONFLICT"
        )
        assert (
            client.post(BASE + "/save", json=data | {"request_id": str(uuid4())}).json()["code"]
            == "REVISION_CONFLICT"
        )
        noop = data | {"request_id": str(uuid4()), "revision": 1}
        result = client.post(BASE + "/save", json=noop).json()
        assert result == first | {"outcome": "UNCHANGED"}
        changed: dict[str, Any] = command() | {"request_id": str(uuid4()), "revision": 1}
        changed["configuration"]["target_job_keywords"] = ["next"]
        assert client.post(BASE + "/save", json=changed).status_code == 200
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.post(BASE + "/save", json=noop).json() == result
        assert client.get(BASE).json()["preference_set"]["revision"] == 2


@pytest.mark.parametrize(
    "field,limit,item_length", [("accepted_cities", 50, 100), ("excluded_companies", 200, 200)]
)
def test_set_capacities(tmp_path: Path, field: str, limit: int, item_length: int) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data = command()
        for values, code in [
            ([], "OUT_OF_RANGE"),
            (["x"] * 1001, "OUT_OF_RANGE"),
            ([str(i) for i in range(limit + 1)], "OUT_OF_RANGE"),
            (["x" * (item_length + 1)], "TOO_LONG"),
        ]:
            data["configuration"][field] = {"mode": "LIMITED", "value": values}
            response = client.post(BASE + "/save", json=data)
            assert response.json()["field_errors"][0]["code"] == code
        data["configuration"][field] = {"mode": "LIMITED", "value": ["x" * item_length] * 1000}
        assert client.post(BASE + "/save", json=data).status_code == 200


def test_read_during_publication_is_one_committed_observation(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        assert client.post(BASE + "/save", json=command()).status_code == 200

        def publish() -> None:
            for revision in range(1, 16):
                data: dict[str, Any] = command() | {
                    "request_id": str(uuid4()),
                    "revision": revision,
                }
                data["configuration"]["target_job_keywords"] = [str(revision + 1)]
                assert client.post(BASE + "/save", json=data).status_code == 200

        def read() -> None:
            for _ in range(25):
                response = client.get(BASE)
                assert response.status_code == 200
                result = response.json()
                root, version = result["preference_set"], result["current_preference_set_version"]
                assert (
                    root["current_preference_set_version_id"]
                    == version["preference_set_version_id"]
                )
                if root["revision"] > 1:
                    assert version["configuration"]["target_job_keywords"] == [
                        str(root["revision"])
                    ]

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(publish), pool.submit(read)]
            for future in futures:
                future.result()


def test_stream_limit_stops_receiving_without_content_length(tmp_path: Path) -> None:
    import asyncio

    from starlette.types import Message, Scope

    with Store.open(tmp_path) as store:
        app = create_app(store)
        calls = 0
        messages: list[Message] = []

        async def receive() -> Message:
            nonlocal calls
            calls += 1
            assert calls <= 2, "oversized body must stop receiving"
            return {"type": "http.request", "body": b" " * 600000, "more_body": True}

        async def send(message: Message) -> None:
            messages.append(message)

        scope: Scope = {
            "type": "http",
            "asgi": {"version": "3.0", "spec_version": "2.4"},
            "http_version": "1.1",
            "method": "POST",
            "scheme": "http",
            "path": BASE + "/save",
            "raw_path": (BASE + "/save").encode(),
            "query_string": b"",
            "headers": [(b"host", b"testserver"), (b"content-type", b"application/json")],
            "server": ("testserver", 80),
            "client": ("127.0.0.1", 1),
        }
        asyncio.run(app(scope, receive, send))
        assert calls == 2
        assert messages[0]["status"] == 413
        assert "REQUEST_TOO_LARGE" in b"".join(m.get("body", b"") for m in messages).decode()


@pytest.mark.parametrize("stage", ["commit_after_driver", "response_after_commit"])
def test_post_commit_typed_failure_never_claims_noncommit(tmp_path: Path, stage: str) -> None:
    from jobhunter.domain.shared.errors import Failure

    def fault(point: str) -> None:
        if point == stage:
            raise Failure("STORAGE_UNAVAILABLE")

    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        store.fault = fault
        result = client.post(BASE + "/save", json=command())
        assert result.json()["code"] == "OUTCOME_UNKNOWN"
        store.fault = no_fault
        assert client.post(BASE + "/save", json=command()).json()["outcome"] == "CREATED"


def test_unlimited_fingerprint_revision_spelling_and_receipt_namespace(tmp_path: Path) -> None:
    data = command()
    data["configuration"] = {
        "target_job_keywords": ["x"],
        **{
            name: {"mode": "UNLIMITED"}
            for name in (
                "accepted_cities",
                "minimum_salary",
                "recruitment_types",
                "excluded_companies",
                "max_required_education",
            )
        },
    }
    data["revision"] = 1
    raw_bytes = b"PreferenceSetSave:v1\0\1\0\0\0\x011\0\0\0\x01\0\0\0\x01x" + b"\0" * 5
    assert (
        fingerprint(SavePreferences.model_validate(data)) == hashlib.sha256(raw_bytes).hexdigest()
    )
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:
        data["revision"] = None
        created = client.post(BASE + "/save", json=data)
        assert created.status_code == 200
        # The same request UUID is independent in the Entry-create namespace.
        entry = {
            "request_id": data["request_id"],
            "company_name": "Fixture",
            "role_title": "Engineer",
            "application_url": "https://example.test",
        }
        assert client.post("/api/v1/manual-application-entries", json=entry).status_code == 200
        data.update(revision=1, request_id=str(uuid4()))
        raw = json.dumps(data).replace('"revision": 1', '"revision": 1.0e0')
        assert (
            client.post(
                BASE + "/save", content=raw, headers={"content-type": "application/json"}
            ).json()["outcome"]
            == "UNCHANGED"
        )
        raw = json.dumps(data).replace('"revision": 1', '"revision": 1.000000000000000001')
        assert client.post(
            BASE + "/save", content=raw, headers={"content-type": "application/json"}
        ).json()["field_errors"] == [{"field": "revision", "code": "INVALID_TYPE"}]


def test_unclassified_internal_failure_is_sanitized(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store, TestClient(create_app(store)) as client:

        def fault(point: str) -> None:
            if point == "preferences_after_publication":
                raise RuntimeError("private business detail")

        store.fault = fault
        response = client.post(BASE + "/save", json=command())
        assert response.status_code == 500
        assert response.json()["code"] == "INTERNAL_ERROR"
        assert "private" not in response.text
        store.fault = no_fault
        assert client.get(BASE).json() == {"status": "NOT_CONFIGURED"}
