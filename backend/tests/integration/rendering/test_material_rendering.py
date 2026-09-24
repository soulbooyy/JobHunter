"""Actual isolated PDF/PNG output, fixed fonts, marks, pagination and resource failures."""

import io
import itertools
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from uuid import uuid4

import pytest
from jobhunter.application.candidate.authority import CandidateAuthority
from jobhunter.domain.derived_work.models import Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate_v2 import Json
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.material_sources import (
    MaterialSources,
)
from jobhunter.infrastructure.persistence.sqlalchemy.uow.store import Store
from jobhunter.infrastructure.rendering.catalog import ASSETS, catalog, environment
from jobhunter.infrastructure.rendering.pipeline import module
from jobhunter.infrastructure.rendering.validation import validate_output


def saved_source(
    store: Store,
    family: str,
    *,
    text: str = "中文 Resume",
    url: str = "https://example.com/exact?value=1#fragment",
) -> Json:
    authority = CandidateAuthority(store)
    blocks: list[Json] = []
    for bold, italic, underline, link in itertools.product((False, True), repeat=4):
        marks: list[Json] = [
            {"type": kind}
            for kind, enabled in (("BOLD", bold), ("ITALIC", italic), ("UNDERLINE", underline))
            if enabled
        ]
        if link:
            marks.append({"type": "LINK", "url": url})
        blocks.append(
            {
                "type": "PARAGRAPH",
                "block_id": str(uuid4()),
                "runs": [{"text": text + "  A\u00a0B\u3000C", "marks": marks}],
            }
        )
    blocks.append(
        {
            "type": "ORDERED_LIST",
            "items": [
                {
                    "block_id": str(uuid4()),
                    "runs": [{"text": f"Item {index} " + "longtoken" * 20, "marks": []}],
                }
                for index in range(45)
            ],
        }
    )
    resume = authority.command(
        "RESUME_CREATE",
        {
            "request_id": str(uuid4()),
            "resume_name": "Renderer fixture",
            "contacts": {
                "full_name": "Renderer fixture",
                "phone_number": None,
                "email": None,
            },
            "header_presentation": {"optional_items": []},
            "sections": [
                {
                    "kind": "SKILL",
                    "members": [
                        {
                            "entry_id": str(uuid4()),
                            "fields": {"skill_name": "Engineering"},
                            "content": blocks,
                        }
                    ],
                }
            ],
            "document_presentation": {
                "font_family": family,
                "font_size_pt": 12,
                "line_spacing_pt": 16,
                "theme_color": "#112233",
            },
        },
    )
    return store.run(
        lambda conn: (
            MaterialSources(conn)
            .read(resume["resume_version"]["resume_version_id"])
            .model_dump(mode="json")
        )
    )


def output(
    store: Store, source: Json, configuration: RenderConfiguration, **limits: int
) -> tuple[str, bytes]:
    work = Work.model_validate(
        {
            "work_id": str(uuid4()),
            "resume_version_id": source["resume_version"]["resume_version_id"],
            "render_configuration_id": configuration.render_configuration_id,
            "status": "RUNNING",
            "attempt_count": 1,
            "current_attempt_id": str(uuid4()),
            "created_at": "2026-09-23T00:00:00.000Z",
            "finished_at": None,
            "artifact_id": None,
            "failure_code": None,
            "max_attempts": 3,
            "max_pages": 50,
            "max_png_pixels": 100_000_000,
            "max_output_bytes": 50_000_000,
            "timeout_ms": 60_000,
            **limits,
        }
    )
    payload = {
        "source": source,
        "configuration": configuration.model_dump(mode="json"),
        "work": work.model_dump(mode="json"),
        "fonts": str(ASSETS / "fonts"),
        "manifest": json.loads((ASSETS / "font-manifest.json").read_text()),
    }
    with tempfile.TemporaryFile() as candidate:
        process = subprocess.run(
            [
                sys.executable,
                "-m",
                "jobhunter.infrastructure.rendering.worker",
                str(candidate.fileno()),
            ],
            input=json.dumps(payload).encode(),
            capture_output=True,
            pass_fds=(candidate.fileno(), store.lock_fd),
            env=environment(),
            timeout=60,
        )
        assert process.returncode == 0, process.stderr.decode()
        candidate.seek(0)
        code, data = process.stdout.decode().strip(), candidate.read()
        if code == "OK":
            validate_output(data, configuration, work, MaterialSource.model_validate(source))
        return code, data


@pytest.mark.parametrize("family", ["SOURCE_HAN_SANS", "HEITI", "SONGTI", "KAITI"])
def test_all_fonts_marks_pagination_text_and_png_assembly(tmp_path: Path, family: str) -> None:
    with Store.open(tmp_path) as store:
        source = saved_source(store, family)
        pdf_config, png_config = catalog()
        code, pdf = output(store, source, pdf_config)
        assert code == "OK"
        reader = module("pypdf").PdfReader(io.BytesIO(pdf))
        assert len(reader.pages) >= 2
        text = "".join(page.extract_text() for page in reader.pages)
        assert "中文" in text and "Resume" in text and "Item 44" in text
        assert re.sub(r"[0-9]+\.\s*", "", text).replace("\n", "").count("longtoken") == 45 * 20
        font_angles: set[float] = set()
        font_names: set[str] = set()
        links: list[str] = []
        for page in reader.pages:
            assert abs(float(page.mediabox.width) - 210 * 72 / 25.4) < 0.00001
            assert abs(float(page.mediabox.height) - 297 * 72 / 25.4) < 0.00001
            for annotation in page.get("/Annots", []):
                action = annotation.get_object().get("/A")
                if action:
                    links.append(str(action["/URI"]))
            for font in page["/Resources"]["/Font"].values():
                descendant = font.get_object()["/DescendantFonts"][0].get_object()
                descriptor = descendant["/FontDescriptor"]
                assert "/FontFile2" in descriptor or "/FontFile3" in descriptor
                embedded = descriptor.get("/FontFile2") or descriptor["/FontFile3"]
                font_file = module("fontTools.ttLib").TTFont(
                    io.BytesIO(embedded.get_object().get_data())
                )
                font_angles.add(float(font_file["post"].italicAngle))
                font_file.close()
                font_names.add(str(descendant["/BaseFont"]))
        assert len(font_names) == 4
        assert 0 in font_angles and any(angle < 0 for angle in font_angles)
        assert links and set(links) == {"https://example.com/exact?value=1#fragment"}
        code, png = output(store, source, png_config)
        assert code == "OK"
        with module("PIL.Image").open(io.BytesIO(png)) as image:
            assert image.mode == "RGB"
            assert image.size == (1120, 1584 * len(reader.pages))
            assert image.getpixel((0, 0)) == (255, 255, 255)
            image.load()


def test_real_renderer_limits_and_missing_glyph(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        source = saved_source(store, "HEITI")
        pdf, png = catalog()
        assert output(store, source, pdf, max_pages=1)[0] == "RESOURCE_LIMIT_EXCEEDED"
        assert output(store, source, pdf, max_output_bytes=10)[0] == "RESOURCE_LIMIT_EXCEEDED"
        assert output(store, source, png, max_png_pixels=100)[0] == "RESOURCE_LIMIT_EXCEEDED"
        source = saved_source(store, "HEITI", text="Unsupported \U0001f984")
        assert output(store, source, pdf)[0] == "OUTPUT_INVALID"


def test_empty_document_is_one_page(tmp_path: Path) -> None:
    with Store.open(tmp_path) as store:
        source = saved_source(store, "KAITI")
        source["resume_version"]["sections"] = []
        pdf, png = catalog()
        code, data = output(store, source, pdf)
        assert code == "OK"
        assert len(module("pypdf").PdfReader(io.BytesIO(data)).pages) == 1
        code, data = output(store, source, png)
        assert code == "OK"
        with module("PIL.Image").open(io.BytesIO(data)) as image:
            assert image.size == (1120, 1584)


def test_pdf_link_retains_admitted_unicode_spelling(tmp_path: Path) -> None:
    target = "https://例子.测试/路径?q=中文#段"
    with Store.open(tmp_path) as store:
        source = saved_source(store, "HEITI", url=target)
        code, data = output(store, source, catalog()[0])
        assert code == "OK"
        reader = module("pypdf").PdfReader(io.BytesIO(data))
        links = [
            str(annotation.get_object()["/A"]["/URI"])
            for page in reader.pages
            for annotation in page.get("/Annots", [])
        ]
        assert links and set(links) == {target}
