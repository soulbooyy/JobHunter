"""Build approved static logical roles from previously downloaded official sources.

Usage: uv run python scripts/build_render_fonts.py /absolute/source-directory
Downloads are intentionally separate from application startup and rendering.
"""

import hashlib
import importlib
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any, cast

TTFont = cast(Any, importlib.import_module("fontTools.ttLib")).TTFont
TransformPen = cast(Any, importlib.import_module("fontTools.pens.transformPen")).TransformPen
T2CharStringPen = cast(
    Any, importlib.import_module("fontTools.pens.t2CharStringPen")
).T2CharStringPen
TTGlyphPen = cast(Any, importlib.import_module("fontTools.pens.ttGlyphPen")).TTGlyphPen
DecomposingRecordingPen = cast(
    Any, importlib.import_module("fontTools.pens.recordingPen")
).DecomposingRecordingPen
ROOT = Path(__file__).resolve().parents[1] / "backend/assets/rendering"
SHEAR = 0.2125565616700221  # tan(12 degrees), frozen binary64 literal


def synthesize(source: Path, destination: Path, family: str, bold: bool) -> None:
    font = TTFont(source, recalcTimestamp=False)
    glyphs = font.getGlyphSet()
    if "CFF " in font:
        top = font["CFF "].cff.topDictIndex[0]
        for name in font.getGlyphOrder():
            old = top.CharStrings[name]
            recording = DecomposingRecordingPen(glyphs)
            glyphs[name].draw(recording)
            pen = T2CharStringPen(old.width, None)
            recording.replay(TransformPen(pen, (1, 0, SHEAR, 1, 0, 0)))
            top.CharStrings[name] = pen.getCharString(
                private=old.private, globalSubrs=old.globalSubrs
            )
        top.ItalicAngle = -12
        top.FamilyName = family
        top.FullName = family + (" Bold Italic" if bold else " Italic")
        font["CFF "].cff.fontNames = [family + ("-BoldItalic" if bold else "-Italic")]
    else:
        replacements: dict[str, Any] = {}
        for name in font.getGlyphOrder():
            recording = DecomposingRecordingPen(glyphs)
            glyphs[name].draw(recording)
            pen = TTGlyphPen(None)
            recording.replay(TransformPen(pen, (1, 0, SHEAR, 1, 0, 0)))
            replacements[name] = pen.glyph()
        for name, glyph in replacements.items():
            font["glyf"][name] = glyph
    font["post"].italicAngle = -12
    font["head"].macStyle = 3 if bold else 2
    font["OS/2"].fsSelection = (font["OS/2"].fsSelection & ~0x61) | (0x21 if bold else 1)
    font["OS/2"].usWeightClass = 700 if bold else 400
    font["name"].names = [
        record
        for record in font["name"].names
        if record.nameID not in (1, 2, 3, 4, 6, 16, 17, 18, 21, 22)
    ]
    style = "Bold Italic" if bold else "Italic"
    for platform, encoding, language in ((3, 1, 0x409), (1, 0, 0)):
        for key, value in {
            1: family,
            2: style,
            3: family + "-" + style,
            4: family + " " + style,
            6: family + "-" + style.replace(" ", ""),
            16: family,
            17: style,
        }.items():
            font["name"].setName(value, key, platform, encoding, language)
    font["head"].modified = 2082844800
    font.save(destination)
    font.close()


def main() -> None:
    source = Path(sys.argv[1])
    staging = tempfile.TemporaryDirectory(prefix="jobhunter-font-build-")
    fonts = Path(staging.name)
    expected = json.loads((ROOT / "font-manifest.json").read_text())
    mapping = {
        "SOURCE_HAN_SANS": ("sans-regular.otf", "sans-bold.otf", "Source Han Sans SC", "2.005R"),
        "SONGTI": (
            "serif-regular.otf",
            "serif-bold.otf",
            "Source Han Serif CN (SC file)",
            "2.003R",
        ),
        "KAITI": ("wenkai-regular.ttf", "wenkai-medium.ttf", "LXGW WenKai", "1.522"),
        "HEITI": (
            "SarasaGothicSC-Regular.ttf",
            "SarasaGothicSC-Bold.ttf",
            "Sarasa Gothic SC",
            "1.0.40",
        ),
    }
    manifest: dict[str, Any] = {
        "synthesis": {
            "tool": "fontTools",
            "version": "4.65.0",
            "matrix": [1, 0, SHEAR, 1, 0, 0],
            "italic_angle": -12,
            "modified_timestamp": 2082844800,
        },
        "families": {},
    }
    for logical, (regular, bold, family, version) in mapping.items():
        roles: dict[str, Any] = {}
        for role in ("regular", "bold", "italic", "bold_italic"):
            original = regular if role in ("regular", "italic") else bold
            native = logical == "HEITI" or role in ("regular", "bold")
            if logical == "HEITI" and role == "italic":
                original = "SarasaGothicSC-Italic.ttf"
            if logical == "HEITI" and role == "bold_italic":
                original = "SarasaGothicSC-BoldItalic.ttf"
            expected_role = expected["families"][logical]["roles"][role]
            if (
                hashlib.sha256((source / original).read_bytes()).hexdigest()
                != expected_role["source_sha256"]
            ):
                raise ValueError("Font source hash mismatch")
            destination = fonts / (logical + "-" + role + Path(original).suffix)
            if native:
                shutil.copyfile(source / original, destination)
            else:
                synthesize(
                    source / original,
                    destination,
                    "JobHunterDerived" + logical.replace("_", ""),
                    role == "bold_italic",
                )
            roles[role] = {
                "file": destination.name,
                "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
                "source_file": original,
                "source_sha256": hashlib.sha256((source / original).read_bytes()).hexdigest(),
                "synthesis": None if native else "shear_12_degrees_v1",
            }
        manifest["families"][logical] = {"family": family, "version": version, "roles": roles}
    if manifest != expected:
        raise ValueError("Font build differs from the registered manifest; no catalog was changed")
    (ROOT / "fonts").mkdir(parents=True, exist_ok=True)
    for path in fonts.iterdir():
        shutil.copyfile(path, ROOT / "fonts" / path.name)
    staging.cleanup()
    print("Verified and installed 16 fixed font roles.")


if __name__ == "__main__":
    main()
