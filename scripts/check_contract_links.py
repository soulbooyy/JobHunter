"""Mechanical requirement/mapping/link checks, not semantic acceptance."""

import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).resolve().parents[1]
contracts = root / "docs/contracts"
expected = {
    "COM": 51,
    "WSP": 15,
    "MAE": 18,
    "STO": 59,
    "PRF": 24,
    "PRO": 20,
    "EVD": 24,
    "RES": 24,
    "SAV": 26,
    "MAT": 33,
    "DRW": 26,
    "EXR": 57,
    "EVO": 28,
    "CTX": 16,
    "TOL": 15,
    "BUD": 25,
}
requirement_pattern = r"\b(?:" + "|".join(expected) + r")-\d{3}\b"
contract_paths = sorted(contracts.rglob("*.md"))
found: list[str] = []
for path in contract_paths:
    source = path.read_text()
    defined = re.findall(r"^\*\*([A-Z]+-\d{3})\.\*\*", source, re.M)
    found.extend(defined)
    for requirement in defined:
        assert f'<a id="{requirement.lower()}"></a>' in source, (path, requirement)
assert len(found) == len(set(found)) == sum(expected.values()), "ID count/uniqueness"
assert set(found) == {
    f"{prefix}-{i:03}" for prefix, count in expected.items() for i in range(1, count + 1)
}, "Unexpected prefix, missing ID or incorrect range"


def anchors(path: Path) -> set[str]:
    """Explicit IDs plus GitHub-style heading slugs, including duplicate suffixes."""
    source = path.read_text()
    result = set(re.findall(r'<a\s+id="([^"]+)"', source))
    seen: Counter[str] = Counter()
    fenced = False
    for line in source.splitlines():
        if line.startswith(("```", "~~~")):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = match[1].lower()
            slug = "".join(c for c in title if c.isalnum() or c in "_- ").replace(" ", "-")
            suffix = f"-{seen[slug]}" if seen[slug] else ""
            result.add(slug + suffix)
            seen[slug] += 1
    return result


trace_path = root / "docs/progress/traceability.md"
trace = trace_path.read_text()
review_paths = [
    trace_path,
    root / "docs/development/handoff/sl-02-m2-handoff.md",
    root / "docs/design/contract/sl-02-m2-grill.md",
    root / "docs/development/handoff/sl-03-m1-handoff.md",
    root / "docs/design/contract/sl-03-m1-grill.md",
    root / "docs/design/contract/sl-03-m2-grill.md",
    root / "docs/development/handoff/sl-03-m2-handoff.md",
    root / "docs/acceptance/evaluation.md",
    root / "docs/architecture.md",
    root / "docs/acceptance.md",
    root / "docs/plans/implementation-plan.md",
    root / "docs/plans/slices/sl-03-invocation-requirements.md",
    root / "docs/progress.md",
    root / "docs/index.md",
    root / "docs/development/README.md",
    root / "docs/design/contract/README.md",
]
# Review current owners and real transfer entries as well as preserved historical maps.
review_paths = sorted(
    set(review_paths)
    | {
        root / "docs/spec.md",
        root / "docs/api/README.md",
        root / "docs/api/sl-02-m1.md",
        root / "docs/api/sl-02-m2.md",
        root / "docs/design/contract/sl-02-m1-supplement-grill.md",
        root / "docs/ui/DESGIN.md",
        *sorted((root / "docs/plans/slices").glob("*.md")),
        *sorted((root / "docs/development/handoff").glob("sl-*-handoff.md")),
    }
)
anchor_cache: dict[Path, set[str]] = {}
link_count = 0
for path in [*contract_paths, *review_paths]:
    source = path.read_text()
    for requirement in re.findall(requirement_pattern, source):
        assert requirement in found, (path, requirement)
    targets: list[str] = re.findall(r"\]\(([^)\s]+)\)", source)
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        assert destination.exists(), (path, target)
        if parsed.fragment and destination.suffix == ".md":
            if destination not in anchor_cache:
                anchor_cache[destination] = anchors(destination)
            assert unquote(parsed.fragment) in anchor_cache[destination], (path, target)
        link_count += 1

review = trace.split("### 6.4 SL-02.M2 reviewed scope and interface evidence", 1)[1].split(
    "\n### 6.5", 1
)[0]
questions = re.findall(r"^\| \[CG04-Q(\d+)\]", review, re.M)
assert len(questions) == 135 and {int(q) for q in questions} == set(range(1, 136)), (
    "CG04 mapping coverage"
)
runtime_review = trace.split("### 6.5 SL-03.M1 reviewed scope and interface evidence", 1)[1].split(
    "\n### 6.6", 1
)[0]
runtime_questions = re.findall(r"^\| \[CG05-Q(\d+)\]", runtime_review, re.M)
assert len(runtime_questions) == 130 and {int(q) for q in runtime_questions} == set(
    range(1, 131)
), "CG05 mapping coverage"
runtime_additions = {
    f"{prefix}-{i:03}"
    for prefix, (start, end) in {
        "EXR": (1, 34),
        "EVO": (1, 7),
        "COM": (47, 48),
        "STO": (40, 45),
    }.items()
    for i in range(start, end + 1)
}
runtime_mapping_rows = "\n".join(
    line for line in runtime_review.splitlines() if line.startswith("| [CG05-Q")
)
assert runtime_additions <= set(re.findall(requirement_pattern, runtime_mapping_rows)), (
    "CG05 normative destination coverage"
)
semantic_review = trace.split("### 6.6 SL-03.M2 reviewed scope and interface evidence", 1)[1].split(
    "\n## 7.", 1
)[0]
semantic_questions = re.findall(r"^\| \[CG06-Q(\d+)\]", semantic_review, re.M)
assert len(semantic_questions) == 219 and {int(q) for q in semantic_questions} == set(
    range(1, 220)
), "CG06 accepted mapping coverage"
semantic_additions = {
    f"{prefix}-{i:03}"
    for prefix, (start, end) in {
        "EXR": (35, 57),
        "EVO": (8, 26),
        "COM": (49, 49),
        "STO": (46, 53),
        "CTX": (1, 15),
        "TOL": (1, 14),
        "BUD": (1, 25),
    }.items()
    for i in range(start, end + 1)
}
semantic_mapping_rows = "\n".join(
    line for line in semantic_review.splitlines() if line.startswith("| [CG06-Q")
)
assert semantic_additions <= set(re.findall(requirement_pattern, semantic_mapping_rows)), (
    "CG06 normative destination coverage"
)
semantic_register = (root / "docs/design/contract/sl-03-m2-grill.md").read_text()
for number in range(1, 220):
    accepted_section = semantic_register.split(f"### CG06-Q{number} —", 1)[1].split("\n### ", 1)[0]
    assert "Status: ACCEPTED" in accepted_section, "CG06 accepted decision status"
supplement_review = trace.split("### 6.7 SL-02.M1 supplement reviewed scope", 1)[1].split(
    "\n## 7.", 1
)[0]
supplement_rows = "\n".join(
    line for line in supplement_review.splitlines() if line.startswith("| [CG03S1-")
)
supplement_questions = re.findall(r"^\| \[CG03S1-Q(\d+)\]", supplement_rows, re.M)
assert len(supplement_questions) == 41 and {int(q) for q in supplement_questions} == set(
    range(6, 47)
), "CG03S1 decision coverage (Q1-Q5 withdrawn; Q24 mapped as superseded)"
for baseline in (1, 2, 3):
    assert f"| [CG03S1-BC{baseline}]" in supplement_rows, "CG03S1 baseline coverage"
supplement_destinations = set(re.findall(requirement_pattern, supplement_rows))
for prefix, start, end in re.findall(r"\b([A-Z]{3})-(\d{3})[–-](\d{3})\b", supplement_rows):
    supplement_destinations.update(f"{prefix}-{i:03}" for i in range(int(start), int(end) + 1))
supplement_additions = {
    f"{prefix}-{i:03}"
    for prefix, (start, end) in {
        "COM": (50, 51),
        "WSP": (13, 15),
        "RES": (17, 24),
        "EVD": (16, 24),
        "PRO": (10, 20),
        "SAV": (18, 26),
        "STO": (54, 59),
        "MAT": (31, 33),
        "PRF": (24, 24),
        "CTX": (16, 16),
        "TOL": (15, 15),
        "EVO": (27, 28),
    }.items()
    for i in range(start, end + 1)
}
assert supplement_additions <= supplement_destinations, "CG03S1 normative destination coverage"
supplement_register = (root / "docs/design/contract/sl-02-m1-supplement-grill.md").read_text()
for number in range(42, 47):
    accepted_section = supplement_register.split(f"### CG03S1-Q{number} —", 1)[1].split(
        "\n### ", 1
    )[0]
    assert "**Status:** ACCEPTED" in accepted_section, "Entry-scoped amendment acceptance"
ledger = trace.split("## 6. Contract normative scope readiness ledger", 1)[1].split("### 6.1", 1)[0]
rows = [line for line in ledger.splitlines() if line.startswith("| `")]
ready = sum(" | Ready" in line for line in rows)
pending = sum(" | Pending |" in line for line in rows)
assert len(rows) == ready + pending, "Unclassified readiness row"
assert f"{ready} rows below are **Ready**" in ledger
assert f"other {pending} rows remain **Pending**" in ledger
assert f"for {len(rows)} rows" in ledger
print(
    f"{len(found)} unique requirements; {link_count} local links/anchors resolve; "
    f"135 CG04 / 130 CG05 / 219 CG06 / 41 CG03S1 question mappings + 3 baselines; "
    f"readiness {ready} Ready / {pending} Pending / {len(rows)} total."
)
