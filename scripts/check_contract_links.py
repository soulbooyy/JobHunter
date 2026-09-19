"""Mechanical requirement/mapping checks, not semantic acceptance."""

import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
contracts = root / "docs/contracts"
expected = {"COM": 32, "WSP": 6, "MAE": 18, "STO": 13}
found: list[str] = []
for path in contracts.rglob("*.md"):
    found.extend(re.findall(r"^\*\*((?:COM|WSP|MAE|STO)-\d{3})\.\*\*", path.read_text(), re.M))
assert len(found) == len(set(found)) == 69
for prefix, count in expected.items():
    assert {f"{prefix}-{i:03}" for i in range(1, count + 1)} <= set(found)
trace = (root / "docs/progress/traceability.md").read_text()
for requirement in re.findall(r"\b(?:COM|WSP|MAE|STO)-\d{3}\b", trace):
    assert requirement in found, requirement
for path in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", trace):
    if not path.startswith(("http:", "https:")):
        assert (root / "docs/progress" / path).resolve().exists(), path
print("69 unique requirements; traceability IDs and linked files resolve.")
