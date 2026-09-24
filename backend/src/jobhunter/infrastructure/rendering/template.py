"""A4 template v1: English labels, exact local expression and explicit date semantics."""

from html import escape

from jobhunter.domain.materials.sources import MaterialSource
from jobhunter.infrastructure.persistence.sqlalchemy.repositories.candidate import Json

LABELS = {
    "EDUCATION": "Education",
    "WORK_EXPERIENCE": "Work experience",
    "PROJECT": "Projects",
    "SKILL": "Skills",
    "AWARD": "Awards",
    "CERTIFICATION": "Certifications",
    "JOB_SEARCH_STATUS": "Job search status",
    "JOB_INTENTION": "Job intention",
    "EXPECTED_POSITION": "Expected position",
    "EXPECTED_CITY": "Expected city",
    "EXPECTED_SALARY": "Expected salary",
    "HIGHEST_EDUCATION": "Highest education",
    "GENDER": "Gender",
    "POLITICAL_AFFILIATION": "Political affiliation",
    "YEARS_OF_EXPERIENCE": "Years of experience",
}
DEGREES = {
    "SECONDARY_VOCATIONAL": "Secondary vocational",
    "HIGH_SCHOOL": "High school",
    "ASSOCIATE": "Associate",
    "BACHELOR": "Bachelor",
    "MASTER": "Master",
    "MBA": "MBA",
    "DOCTORATE": "Doctorate",
}


def runs(values: list[Json]) -> str:
    result = ""
    for run in values:
        value = escape(run["text"])
        for mark in run["marks"]:
            tag = {"BOLD": "b", "ITALIC": "i", "UNDERLINE": "u"}.get(mark["type"])
            if tag:
                value = f"<{tag}>{value}</{tag}>"
            else:
                value = '<a href="' + escape(mark["url"], quote=True) + '">' + value + "</a>"
        result += value
    return result


def document(source: MaterialSource) -> tuple[str, str]:
    data = source.model_dump(mode="json")
    resume = data["resume_version"]
    profile = resume["contacts"]
    parts: list[str] = []
    if profile["full_name"] is not None:
        parts.append("<h1>" + escape(profile["full_name"]) + "</h1>")
    contacts = [profile[key] for key in ("phone_number", "email") if profile[key] is not None]
    if contacts:
        parts.append("<p>" + escape(" | ".join(contacts)) + "</p>")
    for item in resume["header_presentation"]["optional_items"]:
        parts.append("<p>" + LABELS[item["kind"]] + ": " + escape(item["value"]) + "</p>")
    for section in resume["sections"]:
        parts.append("<h2>" + LABELS[section["kind"]] + "</h2>")
        for member in section["members"]:
            fields = member["fields"]
            values: list[str] = []
            for key, value in fields.items():
                if value is not None and key not in ("start_month", "end_month"):
                    values.append(DEGREES[value] if key == "degree" else value)
            if "start_month" in fields and (
                fields["start_month"] is not None or fields["end_month"] is not None
            ):
                # Nulls do not imply "Present"; show only supplied bounds.
                values.append((fields["start_month"] or "") + " – " + (fields["end_month"] or ""))
            if values:
                parts.append('<p class="facts">' + escape(" | ".join(values)) + "</p>")
            for block in member["content"]:
                if block["type"] == "PARAGRAPH":
                    parts.append("<p>" + runs(block["runs"]) + "</p>")
                else:
                    tag = "ol" if block["type"] == "ORDERED_LIST" else "ul"
                    parts.append(
                        f"<{tag}>"
                        + "".join("<li>" + runs(item["runs"]) + "</li>" for item in block["items"])
                        + f"</{tag}>"
                    )
    presentation = resume["document_presentation"]
    css = f"""@page {{ size:210mm 297mm; margin:18mm; }}
html {{ font-family:JobHunter; font-size:{presentation["font_size_pt"]}pt;
line-height:{presentation["line_spacing_pt"]}pt; color:#202020; }}
body {{ margin:0; }} p,li {{ white-space:pre-wrap; overflow-wrap:anywhere; }}
p {{ margin:0 0 5pt; }}
h1,h2 {{ font-size:inherit; line-height:inherit;
font-weight:bold; color:{presentation["theme_color"]};
white-space:pre-wrap; overflow-wrap:anywhere; }}
h1 {{ margin:0 0 8pt; }} h2 {{ margin:10pt 0 5pt; break-after:avoid; }}
ul,ol {{ margin:0 0 5pt; padding-left:20pt; }} li {{ margin:0; }}
a {{ color:inherit; text-decoration:underline; }}"""
    return '<!doctype html><html><meta charset="utf-8"><body>' + "".join(
        parts
    ) + "</body></html>", css
