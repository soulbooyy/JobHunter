"""Explicit reproducible font installation, never invoked during backend startup."""

import hashlib
import json
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    sources = json.loads((ROOT / "backend/assets/rendering/font-sources.json").read_text())
    with tempfile.TemporaryDirectory(prefix="jobhunter-font-download-") as temporary:
        directory = Path(temporary)
        for filename, source in sources.items():
            destination = directory / filename
            urllib.request.urlretrieve(source["url"], destination)
            if hashlib.sha256(destination.read_bytes()).hexdigest() != source["sha256"]:
                raise ValueError("Official source hash mismatch")
        subprocess.run(
            [
                "bsdtar",
                "-xf",
                str(directory / "sarasa.7z"),
                "-C",
                str(directory),
                *[
                    f"SarasaGothicSC-{role}.ttf"
                    for role in ("Regular", "Bold", "Italic", "BoldItalic")
                ],
            ],
            check=True,
        )
        subprocess.run(
            [sys.executable, str(ROOT / "scripts/build_render_fonts.py"), str(directory)],
            check=True,
        )


if __name__ == "__main__":
    main()
