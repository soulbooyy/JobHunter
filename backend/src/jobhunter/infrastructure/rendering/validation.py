"""Coordinator-side validation of the final bytes received after renderer exit."""

import io
import logging
from typing import Any, cast

from jobhunter.domain.derived_work.models import Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.domain.resume.models import Link, Paragraph
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.rendering.pipeline import module


def validate_output(
    data: bytes, configuration: RenderConfiguration, work: Work, source: MaterialSource
) -> None:
    for name in ("pypdf", "PIL"):
        logging.getLogger(name).disabled = True
    if len(data) > work.max_output_bytes:
        raise Failure("RESOURCE_LIMIT_EXCEEDED")
    try:
        if configuration.output.media_type == "image/png":
            width = configuration.output.page_width_px
            page_height = (width * 297 * 2 + 210) // 420
            with module("PIL.Image").open(io.BytesIO(data)) as image:
                if (
                    image.format != "PNG"
                    or image.mode != "RGB"
                    or image.width != width
                    or image.height < page_height
                    or image.height % page_height
                ):
                    raise Failure("OUTPUT_INVALID")
                if (
                    image.width * image.height > work.max_png_pixels
                    or image.height // page_height > work.max_pages
                ):
                    raise Failure("RESOURCE_LIMIT_EXCEEDED")
                image.load()
            return
        reader = module("pypdf").PdfReader(io.BytesIO(data), strict=True)
        if reader.is_encrypted or len(reader.pages) < 1:
            raise Failure("OUTPUT_INVALID")
        if len(reader.pages) > work.max_pages:
            raise Failure("RESOURCE_LIMIT_EXCEEDED")
        targets = {
            mark.url
            for section in source.resume_version.sections
            for member in section.members
            for block in member.content
            for item in ([block] if isinstance(block, Paragraph) else block.items)
            for run in item.runs
            for mark in run.marks
            if isinstance(mark, Link)
        }
        seen: set[int] = set()

        def inspect(value: Any) -> None:
            value = value.get_object() if hasattr(value, "get_object") else value
            if id(value) in seen:
                return
            seen.add(id(value))
            if isinstance(value, dict):
                mapping = cast(dict[str, Any], value)
                if set(mapping).intersection(
                    (
                        "/JavaScript",
                        "/JS",
                        "/OpenAction",
                        "/AA",
                        "/AcroForm",
                        "/EmbeddedFiles",
                        "/Launch",
                    )
                ):
                    raise Failure("OUTPUT_INVALID")
                if "/S" in mapping and (
                    mapping["/S"] != "/URI" or mapping.get("/URI") not in targets
                ):
                    raise Failure("OUTPUT_INVALID")
                for child in mapping.values():
                    inspect(child)
            elif isinstance(value, list):
                for child in cast(list[Any], value):
                    inspect(child)

        inspect(reader.trailer)
        for page in reader.pages:
            if (
                abs(float(page.mediabox.width) - 210 * 72 / 25.4) > 0.00001
                or abs(float(page.mediabox.height) - 297 * 72 / 25.4) > 0.00001
            ):
                raise Failure("OUTPUT_INVALID")
            fonts = page["/Resources"].get("/Font", {})
            fonts = fonts.get_object() if hasattr(fonts, "get_object") else fonts
            for font in fonts.values():
                descendants = font.get_object().get("/DescendantFonts", [])
                if not descendants:
                    raise Failure("OUTPUT_INVALID")
                for descendant in descendants:
                    descriptor = descendant.get_object()["/FontDescriptor"]
                    if "/FontFile2" not in descriptor and "/FontFile3" not in descriptor:
                        raise Failure("OUTPUT_INVALID")
    except Failure:
        raise
    except Exception:
        raise Failure("OUTPUT_INVALID") from None
