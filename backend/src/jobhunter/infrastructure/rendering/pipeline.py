"""Fixed renderer adapter; imported only in the isolated worker process."""

import hashlib
import importlib
import io
import logging
import math
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, cast

from jobhunter.domain.derived_work.models import Work
from jobhunter.domain.materials.models import RenderConfiguration
from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.domain.shared.errors import Failure
from jobhunter.infrastructure.rendering.template import document


def module(name: str) -> Any:
    return cast(Any, importlib.import_module(name))


def render(
    source: MaterialSource,
    configuration: RenderConfiguration,
    work: Work,
    fonts: Path,
    manifest: dict[str, Any],
) -> bytes:
    for name in ("weasyprint", "fontTools", "pypdf"):
        logger = logging.getLogger(name)
        logger.disabled = True
        logger.propagate = False
    weasy = module("weasyprint")
    font_config = module("weasyprint.text.fonts").FontConfiguration()
    family = source.resume_version.document_presentation.font_family
    family_roles = manifest["families"][family]["roles"]
    html, css = document(source)
    glyph_text: dict[str, str] = dict.fromkeys(("regular", "bold", "italic", "bold_italic"), "")

    class VisibleText(HTMLParser):
        def __init__(self) -> None:
            super().__init__(convert_charrefs=True)
            self.tags: list[str] = []

        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            if tag not in ("meta",):
                self.tags.append(tag)
            if tag == "li":
                glyph_text["regular"] += "0123456789. •"

        def handle_endtag(self, tag: str) -> None:
            if self.tags and self.tags[-1] == tag:
                self.tags.pop()

        def handle_data(self, data: str) -> None:
            bold = any(tag in self.tags for tag in ("b", "h1", "h2"))
            italic = "i" in self.tags
            role = (
                "bold_italic"
                if bold and italic
                else "bold"
                if bold
                else "italic"
                if italic
                else "regular"
            )
            glyph_text[role] += data

    VisibleText().feed(html)
    font_css = ""
    allowed: dict[str, bytes] = {}
    for role in ("regular", "bold", "italic", "bold_italic"):
        asset = family_roles[role]
        data = (fonts / asset["file"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != getattr(getattr(configuration.fonts, family), role):
            raise Failure("CONFIGURATION_UNAVAILABLE")
        font = module("fontTools.ttLib").TTFont(io.BytesIO(data))
        cmap = font.getBestCmap()
        # Template generated text is checked too; only whitespace without visible glyph is exempt.
        text = glyph_text[role]
        if any(ord(char) not in cmap for char in text if char not in "\n\r\t"):
            raise Failure("OUTPUT_INVALID")
        font.close()
        url = "jobhunter-font:" + role
        allowed[url] = data
        style = "italic" if "italic" in role else "normal"
        weight = 700 if "bold" in role else 400
        font_css += (
            f"@font-face{{font-family:JobHunter;src:url('{url}');"
            f"font-weight:{weight};font-style:{style};}}"
        )

    class LocalFetcher:
        _fail_on_errors = True

        def __call__(self, url: str) -> Any:
            if url not in allowed:
                raise Failure("OUTPUT_INVALID")
            return module("weasyprint.urls").URLFetcherResponse(url, allowed[url])

    fetch = LocalFetcher()
    html, css = document(source)
    targets: dict[str, str] = {}

    def exact_link(match: re.Match[str]) -> str:
        marker = "https://jobhunter.invalid/annotation/" + str(len(targets))
        targets[marker] = unescape(match.group(1))
        return 'href="' + marker + '"'

    # Use non-fetchable internal markers while laying out; restore only admitted original
    # targets in PDF URI objects. This avoids the layout library's IRI normalization.
    html = re.sub(r'href="([^"]*)"', exact_link, html)
    sheet = weasy.CSS(string=font_css + css, url_fetcher=fetch, font_config=font_config)
    rendered = weasy.HTML(string=html, url_fetcher=fetch).render(
        stylesheets=[sheet], font_config=font_config
    )
    if not 1 <= len(rendered.pages) <= work.max_pages:
        raise Failure("RESOURCE_LIMIT_EXCEEDED")

    class BoundedOutput(io.BytesIO):
        def write(self, buffer: Any) -> int:
            if self.tell() + len(buffer) > work.max_output_bytes:
                raise Failure("RESOURCE_LIMIT_EXCEEDED")
            return super().write(buffer)

    pdf = cast(bytes, rendered.write_pdf())
    reader = module("pypdf").PdfReader(io.BytesIO(pdf), strict=True)
    if reader.is_encrypted or len(reader.pages) != len(rendered.pages):
        raise Failure("OUTPUT_INVALID")
    forbidden = {
        "/JavaScript",
        "/JS",
        "/OpenAction",
        "/AA",
        "/AcroForm",
        "/EmbeddedFiles",
        "/Launch",
    }
    seen: set[int] = set()

    def inspect(value: Any) -> None:
        value = value.get_object() if hasattr(value, "get_object") else value
        identity = id(value)
        if identity in seen:
            return
        seen.add(identity)
        if isinstance(value, dict):
            if forbidden.intersection(cast(dict[str, Any], value)):
                raise Failure("OUTPUT_INVALID")
            if "/S" in value and value["/S"] != "/URI":
                raise Failure("OUTPUT_INVALID")
            for child in cast(dict[str, Any], value).values():
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
    generic = module("pypdf.generic")
    for page in reader.pages:
        for annotation in page.get("/Annots", []):
            action = annotation.get_object().get("/A")
            if not action or action.get("/S") != "/URI" or action.get("/URI") not in targets:
                raise Failure("OUTPUT_INVALID")
            action[generic.NameObject("/URI")] = generic.TextStringObject(targets[action["/URI"]])
    writer = module("pypdf").PdfWriter(clone_from=reader)
    final_pdf = (
        BoundedOutput() if configuration.output.media_type == "application/pdf" else io.BytesIO()
    )
    writer.write(final_pdf)
    pdf = final_pdf.getvalue()
    # Parse the final representation, not only the layout library's intermediate PDF.
    verified_pdf = module("pypdf").PdfReader(io.BytesIO(pdf), strict=True)
    if verified_pdf.is_encrypted or len(verified_pdf.pages) != len(reader.pages):
        raise Failure("OUTPUT_INVALID")
    if configuration.output.media_type == "application/pdf":
        return pdf
    width = configuration.output.page_width_px
    height = math.floor(width * 297 / 210 + 0.5)
    if width * height * len(reader.pages) > work.max_png_pixels:
        raise Failure("RESOURCE_LIMIT_EXCEEDED")
    image_module = module("PIL.Image")
    canvas = image_module.new("RGB", (width, height * len(reader.pages)), (255, 255, 255))
    pdfium = module("pypdfium2")
    raw = module("pypdfium2.raw")
    with pdfium.PdfDocument(pdf) as pdf_document:
        for index in range(len(pdf_document)):
            page = pdf_document[index]
            bitmap = pdfium.PdfBitmap.new_native(width, height, format=raw.FPDFBitmap_BGR)
            bitmap.fill_rect((255, 255, 255, 255), 0, 0, width, height)
            raw.FPDF_RenderPageBitmap(bitmap, page, 0, 0, width, height, 0, raw.FPDF_ANNOT)
            image = bitmap.to_pil()
            canvas.paste(image, (0, index * height))
            image.close()
            bitmap.close()
            page.close()
    output = BoundedOutput()
    canvas.save(output, format="PNG")
    canvas.close()
    data = output.getvalue()
    if len(data) > work.max_output_bytes:
        raise Failure("RESOURCE_LIMIT_EXCEEDED")
    with image_module.open(io.BytesIO(data)) as verified:
        if verified.size != (width, height * len(reader.pages)) or verified.mode != "RGB":
            raise Failure("OUTPUT_INVALID")
        verified.load()
    return data
