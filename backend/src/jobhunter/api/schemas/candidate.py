"""Derived schema refinements for kind-selected fields and raw admission limits."""

from typing import Any

from fastapi import FastAPI

from jobhunter.domain.evidence.models import FIELD_MODELS


def refine_candidate_schema(app: FastAPI) -> None:
    original = app.openapi

    def schema() -> dict[str, Any]:
        result = original()
        schemas = result["components"]["schemas"]
        refs: dict[str, dict[str, str]] = {}
        for kind, model in FIELD_MODELS.items():
            name = model.__name__ + "Input"
            schemas[name] = model.model_json_schema(mode="validation")
            refs[kind] = {"$ref": "#/components/schemas/" + name}
        schemas["EvidenceCreate"]["allOf"] = [
            {
                "if": {"properties": {"kind": {"const": kind}}},
                "then": {"properties": {"fields": ref}},
            }
            for kind, ref in refs.items()
        ]
        schemas["EvidenceUpdate"]["properties"]["fields"] = {
            "oneOf": list(refs.values()),
            "description": (
                "Selected by the target Item permanent kind (SAV-003). An absent"
                " target precedes this schema admission and receipt lookup."
            ),
        }
        for path, operations in result["paths"].items():
            if not path.startswith(
                (
                    "/api/v1/profile",
                    "/api/v1/evidence-",
                    "/api/v1/resumes",
                    "/api/v1/workspace/default-resume",
                )
            ):
                continue
            for method, operation in operations.items():
                if method == "get":
                    for status in ("409", "413"):
                        operation["responses"].pop(status, None)
                    operation["description"] = (
                        "Consistent read; no query parameters or request body. Historical "
                        "exact reads never substitute current versions."
                    )
                elif method == "post":
                    maximum = (
                        8_388_608
                        if path == "/api/v1/resumes"
                        or (path.startswith("/api/v1/resumes/") and path.endswith("/save"))
                        else 1_048_576
                        if path == "/api/v1/evidence-items"
                        or (path.startswith("/api/v1/evidence-items/") and path.endswith("/save"))
                        else 65_536
                    )
                    operation["x-max-body-bytes"] = maximum
                    operation["x-max-json-nodes"] = 100000
                    operation["x-max-json-container-depth"] = 32
                    operation["description"] = (
                        "SAV-001–016: complete closed body, exact JSON numbers, UTF-8 "
                        "application/json, identity encoding, no query or duplicate object "
                        "keys. Shared request_id namespace for these nine commands. Receipt"
                        " replay returns the original completion snapshot; read current "
                        "separately. Limits apply before canonicalization. No "
                        "network/model/rendering invocation."
                    )
        return result

    app.openapi = schema
