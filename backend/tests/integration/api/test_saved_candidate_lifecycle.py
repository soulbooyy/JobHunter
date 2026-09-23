"""Historical source/result bindings, lifecycle and independent selection tokens."""

from collections.abc import Iterator
from copy import deepcopy
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


def post(client: TestClient, path: str, body: Json) -> Json:
    response = client.post("/api/v1/" + path, json=body)
    assert response.status_code == 200, response.text
    return response.json()


def skill(client: TestClient, name: str = "Python") -> Json:
    return post(
        client,
        "evidence-items",
        {
            "request_id": str(uuid4()),
            "kind": "SKILL",
            "fields": {"skill_name": name},
            "content": [{"type": "PARAGRAPH", "text": " A fact "}],
        },
    )


def draft(client: TestClient, evidence: Json | None = None) -> Json:
    return {
        "request_id": str(uuid4()),
        "resume_name": "Resume",
        "profile_version_id": client.get("/api/v1/profile").json()["profile_version"][
            "profile_version_id"
        ],
        "header_presentation": {"optional_items": []},
        "sections": []
        if evidence is None
        else [
            {
                "kind": "SKILL",
                "members": [
                    {
                        "evidence_item_id": evidence["evidence_item"]["evidence_item_id"],
                        "evidence_item_version_id": evidence["evidence_item_version"][
                            "evidence_item_version_id"
                        ],
                        "content": [
                            {
                                "type": "PARAGRAPH",
                                "runs": [
                                    {
                                        "text": " Local ",
                                        "marks": [{"type": "ITALIC"}, {"type": "BOLD"}],
                                    },
                                    {
                                        "text": "wording ",
                                        "marks": [{"type": "BOLD"}, {"type": "ITALIC"}],
                                    },
                                ],
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
            "theme_color": "#aabbcc",
        },
    }


def test_retained_sources_independent_expression_and_historic_replay(client: TestClient) -> None:
    evidence = skill(client)
    command = draft(client, evidence)
    created = post(client, "resumes", command)
    rid = created["resume"]["resume_id"]
    version = created["resume_version"]
    assert version["sections"][0]["members"][0]["content"][0]["runs"] == [
        {"text": " Local wording ", "marks": [{"type": "BOLD"}, {"type": "ITALIC"}]}
    ]
    assert version["document_presentation"]["theme_color"] == "#AABBCC"
    assert created["default_resume_selection"] == {"default_resume_id": rid, "revision": 2}
    eid = evidence["evidence_item"]["evidence_item_id"]
    retire = {"request_id": str(uuid4()), "revision": 1}
    retired = post(client, f"evidence-items/{eid}/retire", retire)
    assert client.get("/api/v1/evidence-items").json() == {"evidence_items": []}
    assert client.get("/api/v1/evidence-baselines/current").json()["members"] == []
    old_baseline = client.get(
        "/api/v1/evidence-baselines/" + evidence["evidence_baseline_snapshot_id"]
    ).json()
    assert old_baseline["members"][0]["evidence_item_id"] == eid
    assert post(client, f"evidence-items/{eid}/retire", retire) == retired
    assert (
        client.get(
            "/api/v1/evidence-items/versions/"
            + evidence["evidence_item_version"]["evidence_item_version_id"]
        ).json()["evidence_item_version"]["content"][0]["text"]
        == "A fact"
    )
    profile = post(
        client,
        "profile/save",
        {
            "request_id": str(uuid4()),
            "revision": 1,
            "full_name": "New",
            "phone_number": None,
            "email": None,
        },
    )
    assert client.get("/api/v1/resumes/" + rid).json()["resume_version"] == version
    assert (
        post(client, "resumes", command) == created
    )  # Even after both sources stop being current.
    changed_key = {**command, "request_id": str(uuid4())}
    assert client.post("/api/v1/resumes", json=changed_key).json()["code"] == "SOURCE_CONFLICT"
    saved_body: Json = {k: v for k, v in command.items() if k != "resume_name"} | {
        "request_id": str(uuid4()),
        "revision": 1,
    }
    saved_body["sections"][0]["members"][0]["content"] = []
    saved = post(client, f"resumes/{rid}/save", saved_body)
    assert saved["resume"]["revision"] == 2
    assert saved["resume_version"]["profile_version_id"] == version["profile_version_id"]
    assert client.get("/api/v1/evidence-items/" + eid).json()["evidence_item"]["revision"] == 2
    assert client.get("/api/v1/profile").json()["profile_version"] == profile["profile_version"]
    assert client.get("/api/v1/resumes/versions/" + version["resume_version_id"]).json() == version
    assert post(client, f"resumes/{rid}/save", saved_body) == saved
    assert (
        client.post(
            "/api/v1/resumes/" + rid + "/save", json={**saved_body, "request_id": str(uuid4())}
        ).json()["code"]
        == "REVISION_CONFLICT"
    )
    assert (
        post(
            client, f"resumes/{rid}/save", {**saved_body, "request_id": str(uuid4()), "revision": 2}
        )["outcome"]
        == "UNCHANGED"
    )


def test_selection_aba_remove_order_and_original_selection_replay(client: TestClient) -> None:
    first = post(client, "resumes", draft(client))
    second = post(client, "resumes", draft(client))
    a, b = first["resume"]["resume_id"], second["resume"]["resume_id"]
    assert second["default_resume_selection"] == first["default_resume_selection"]
    switch = {"request_id": str(uuid4()), "revision": 2, "default_resume_id": b}
    switched = post(client, "workspace/default-resume/set", switch)
    post(
        client,
        "workspace/default-resume/set",
        {**switch, "request_id": str(uuid4()), "revision": 3, "default_resume_id": a},
    )
    assert post(client, "workspace/default-resume/set", switch) == switched
    assert (
        client.post(
            "/api/v1/workspace/default-resume/set", json={**switch, "request_id": str(uuid4())}
        ).json()["code"]
        == "REVISION_CONFLICT"
    )
    removal = {
        "request_id": str(uuid4()),
        "revision": 1,
        "default_resume_selection": {"revision": 2},
        "replacement_resume_id": None,
    }
    assert (
        client.post(f"/api/v1/resumes/{b}/remove", json=removal).json()["code"]
        == "REVISION_CONFLICT"
    )  # Non-default still checks selection.
    rename = post(
        client,
        f"resumes/{b}/rename",
        {"request_id": str(uuid4()), "revision": 1, "resume_name": " Replacement "},
    )
    assert rename["resume_version"] == second["resume_version"]
    removal.update(default_resume_selection={"revision": 4}, replacement_resume_id=b)
    removed = post(client, f"resumes/{a}/remove", removal)
    assert removed["default_resume_selection"] == {"default_resume_id": b, "revision": 5}
    assert client.get("/api/v1/resumes").json()["resumes"] == [rename["resume"]]
    assert client.get("/api/v1/resumes/" + a).json()["resume"]["status"] == "REMOVED"
    assert post(client, f"resumes/{a}/remove", removal) == removed
    noop = post(
        client,
        f"resumes/{a}/remove",
        {
            **removal,
            "request_id": str(uuid4()),
            "revision": 2,
            "default_resume_selection": {"revision": 1},
            "replacement_resume_id": str(uuid4()),
        },
    )
    assert noop["outcome"] == "UNCHANGED"
    assert (
        client.post(
            f"/api/v1/resumes/{a}/rename",
            json={"request_id": str(uuid4()), "revision": 2, "resume_name": "X"},
        ).json()["code"]
        == "INVALID_STATE"
    )
    assert (
        client.post(
            f"/api/v1/resumes/{b}/remove",
            json={
                **removal,
                "request_id": str(uuid4()),
                "revision": 2,
                "default_resume_selection": {"revision": 5},
            },
        ).json()["code"]
        == "LAST_RESUME_REQUIRED"
    )
    assert (
        client.get(
            "/api/v1/resumes/versions/" + first["resume_version"]["resume_version_id"]
        ).json()
        == first["resume_version"]
    )


def test_evidence_update_noop_conflict_namespace_and_no_rewind(client: TestClient) -> None:
    created = skill(client)
    eid = created["evidence_item"]["evidence_item_id"]
    command: Json = {
        "request_id": str(uuid4()),
        "revision": 1,
        "fields": {"skill_name": " Rust "},
        "content": [],
    }
    saved = post(client, f"evidence-items/{eid}/save", command)
    assert saved["evidence_item"]["revision"] == 2
    assert saved["evidence_baseline_snapshot_id"] != created["evidence_baseline_snapshot_id"]
    assert post(client, f"evidence-items/{eid}/save", command) == saved
    noop = post(
        client, f"evidence-items/{eid}/save", {**command, "request_id": str(uuid4()), "revision": 2}
    )
    assert noop["outcome"] == "UNCHANGED"
    assert noop["evidence_baseline_snapshot_id"] == saved["evidence_baseline_snapshot_id"]
    assert noop["evidence_item_version"] == saved["evidence_item_version"]
    retire = post(
        client, f"evidence-items/{eid}/retire", {"request_id": str(uuid4()), "revision": 2}
    )
    assert post(client, f"evidence-items/{eid}/save", command) == saved
    assert (
        client.get("/api/v1/evidence-items/" + eid).json()["evidence_item"]
        == retire["evidence_item"]
    )
    assert (
        client.post(
            f"/api/v1/evidence-items/{eid}/save",
            json={**command, "request_id": str(uuid4()), "revision": 3},
        ).json()["code"]
        == "INVALID_STATE"
    )
    assert (
        client.post(
            "/api/v1/profile/save",
            json={
                "request_id": command["request_id"],
                "revision": 1,
                "full_name": None,
                "phone_number": None,
                "email": None,
            },
        ).json()["code"]
        == "REQUEST_CONFLICT"
    )
    assert (
        client.post(
            f"/api/v1/evidence-items/{eid}/save",
            json={**command, "content": [{"type": "PARAGRAPH", "text": ""}]},
        ).status_code
        == 422
    )


def test_wrong_reference_missing_reference_and_canonical_noop(client: TestClient) -> None:
    one, two = skill(client), skill(client, "Go")
    command = draft(client, one)
    wrong = deepcopy(command)
    wrong["sections"][0]["members"][0]["evidence_item_version_id"] = two["evidence_item_version"][
        "evidence_item_version_id"
    ]
    error = client.post("/api/v1/resumes", json=wrong)
    assert error.status_code == 422
    assert error.json()["field_errors"] == [
        {"field": "sections[0].members[0].evidence_item_version_id", "code": "INVALID_REFERENCE"}
    ]
    created = post(client, "resumes", command)
    equivalent = deepcopy(command)
    equivalent["sections"] = created["resume_version"]["sections"]
    equivalent["document_presentation"]["theme_color"] = "#AABBCC"
    assert post(client, "resumes", equivalent) == created
    wrong = {**command, "request_id": str(uuid4()), "profile_version_id": str(uuid4())}
    assert client.post("/api/v1/resumes", json=wrong).json()["field_errors"] == [
        {"field": "profile_version_id", "code": "INVALID_REFERENCE"}
    ]
