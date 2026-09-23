"""Immutable shipped catalog, separate verified local execution capability."""

import hashlib
import importlib.metadata
import json
import os
import platform
import sys
from pathlib import Path
from typing import Any

from jobhunter.domain.materials.models import RenderConfiguration

ASSETS = Path(__file__).resolve().parents[4] / "assets/rendering"


def catalog() -> list[RenderConfiguration]:
    return [
        RenderConfiguration.model_validate(value)
        for value in json.loads((ASSETS / "catalog.json").read_text())
    ]


def capability(configuration: RenderConfiguration) -> bool:
    try:
        if configuration not in catalog():
            return False
        runtime: dict[str, Any] = json.loads((ASSETS / "pipeline.json").read_text())
        if (
            not runtime["conformance_verified"]
            or sys.platform != runtime["platform"]
            or platform.machine() != runtime["machine"]
            or platform.python_version() != runtime["python"]
            or platform.mac_ver()[0] != runtime["macos"]
        ):
            return False
        for package, version in runtime["packages"].items():
            if configuration.output.media_type == "application/pdf" and package in (
                "pypdfium2",
                "pillow",
            ):
                continue
            if importlib.metadata.version(package) != version:
                return False
        for path, digest in runtime["native_libraries"].items():
            if hashlib.sha256(Path(path).read_bytes()).hexdigest() != digest:
                return False
        manifest: dict[str, Any] = json.loads((ASSETS / "font-manifest.json").read_text())
        for family, roles in configuration.fonts.model_dump().items():
            for role, digest in roles.items():
                asset = manifest["families"][family]["roles"][role]
                if (
                    asset["sha256"] != digest
                    or hashlib.sha256((ASSETS / "fonts" / asset["file"]).read_bytes()).hexdigest()
                    != digest
                ):
                    return False
        return True
    except (OSError, ValueError, KeyError, importlib.metadata.PackageNotFoundError):
        return False


def environment() -> dict[str, str]:
    # Fixed verified native path; no system-font directories in the child Fontconfig file.
    return {
        **os.environ,
        "DYLD_FALLBACK_LIBRARY_PATH": "/opt/homebrew/lib",
        "FONTCONFIG_FILE": str(ASSETS / "fontconfig.xml"),
    }
