"""Derived schema refinements for independent Resume admission limits."""

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
        section_schema = schemas.get("Section-Input", schemas.get("Section"))
        if section_schema is None:
            return result
        resume_entry_name = "ResumeEntry-Input" if "ResumeEntry-Input" in schemas else "ResumeEntry"
        section_schema["allOf"] = [
            {
                "if": {"properties": {"kind": {"const": kind}}},
                "then": {
                    "properties": {
                        "members": {
                            "items": {
                                "allOf": [
                                    {"$ref": "#/components/schemas/" + resume_entry_name},
                                    {"properties": {"fields": ref}},
                                ]
                            }
                        }
                    }
                },
            }
            for kind, ref in refs.items()
        ]
        for path, operations in result["paths"].items():
            if not path.startswith(
                (
                    "/api/v1/resumes",
                    "/api/v1/workspace/default-resume",
                    "/api/v1/workspace/portrait",
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
                        else 65_536
                    )
                    operation["x-max-body-bytes"] = maximum
                    operation["x-max-json-nodes"] = 100000
                    operation["x-max-json-container-depth"] = 32
                    operation["description"] = (
                        "SAV-018–025: complete closed body, exact JSON numbers, UTF-8 "
                        "application/json, identity encoding, no query or duplicate object "
                        "keys. Shared request_id namespace for these six commands. Receipt"
                        " replay returns the original completion snapshot; read current "
                        "separately. Limits apply before canonicalization. No "
                        "network/model/rendering invocation occurs inside the command transaction."
                    )
        return result

    app.openapi = schema
