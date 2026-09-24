"""Materials public operations and isolated request admission."""

from pathlib import Path
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from jobhunter.bootstrap.container import create_app
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store


@pytest.mark.parametrize(
    "path",
    [
        "render-configurations",
        "render-configurations/{id}",
        "render-intents/{id}",
        "artifacts/{id}",
        "artifacts/{id}/content",
    ],
)
def test_material_gets_are_closed_and_present_in_openapi(tmp_path: Path, path: str) -> None:
    with Store.open(tmp_path) as store:
        client = TestClient(create_app(store))
        url = "/api/v1/" + path.replace("{id}", str(uuid4()))
        response = client.get(url)
        assert response.status_code == (200 if path == "render-configurations" else 404)
        assert client.get(url + "?unknown=secret").json()["field_errors"] == [
            {"field": "$", "code": "UNKNOWN_FIELD"}
        ]
        assert client.request("GET", url, content="{}").status_code == 422
        assert "secret" not in client.get(url + "?unknown=secret").text


def test_material_command_admission_and_binary_schema(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        client = TestClient(create_app(store))
        url = "/api/v1/render-intents"
        assert (
            client.post(url, content="{}", headers={"Content-Type": "text/plain"}).status_code
            == 400
        )
        assert (
            client.post(
                url, content=" " * 4097, headers={"Content-Type": "application/json"}
            ).status_code
            == 413
        )
        assert (
            client.post(
                url,
                content='{"request_id":1,"request_id":2}',
                headers={"Content-Type": "application/json"},
            ).status_code
            == 400
        )
        for body in (
            {},
            {"request_id": False},
            {
                "request_id": str(uuid4()),
                "resume_version_id": str(uuid4()),
                "render_configuration_id": str(uuid4()),
                "secret": True,
            },
        ):
            response = client.post(url, json=body)
            assert response.status_code == 422
            assert "secret" not in response.text
        content_url = "/api/v1/artifacts/" + str(uuid4()) + "/content"
        assert client.get(content_url + "?disposition=inline&disposition=inline").status_code == 422
        schema = client.get("/openapi.json").json()
        binary = schema["paths"]["/api/v1/artifacts/{artifact_id}/content"]["get"]["responses"][
            "200"
        ]["content"]
        assert set(binary) == {"application/pdf", "image/png"}
        assert schema["components"]["schemas"]["RenderRequest"]["additionalProperties"] is False


def test_missing_fonts_retains_catalog_and_other_api(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import shutil

    from jobhunter.infrastructure.rendering import catalog as rendering_catalog

    assets = tmp_path / "assets"
    assets.mkdir()
    for name in ("catalog.json", "pipeline.json", "font-manifest.json"):
        shutil.copyfile(rendering_catalog.ASSETS / name, assets / name)
    monkeypatch.setattr(rendering_catalog, "ASSETS", assets)
    directory = tmp_path / "store"
    directory.mkdir()
    with Store.open(directory) as store:
        client = TestClient(create_app(store))
        assert client.get("/api/v1/render-configurations").json() == {"items": []}
        identity = rendering_catalog.catalog()[0].render_configuration_id
        exact = client.get("/api/v1/render-configurations/" + identity)
        assert exact.status_code == 200 and exact.json()["can_generate"] is False
        assert client.get("/api/v1/resumes").status_code == 200
