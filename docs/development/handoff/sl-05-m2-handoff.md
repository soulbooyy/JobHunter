# SL-05.M2 Development Handoff

> English is authoritative. User-requested implementation transfer; no implementation is delivered by this file.

## Current development transfer — 2026-09-24.S2M1S1-r1

**Classification:** First multi-Job/result-management implementation. This addendum controls the replaced source scope; any older body below is a historical snapshot. [Owning plan](../../plans/slices/sl-05-candidate-fit.md) · [Accepted supplement](../../design/contract/sl-02-m1-supplement-grill.md) · [Current scope/evidence](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

**Consumed scope:** CTX-016/EVD-021 and future fit-analysis batch/result/score-policy scope. Read the actual Contract bodies through [Contract Index](../../contracts/index.md); indexes/planned paths are not norms. Read Product/Architecture/Acceptance, AGENTS.md and maintained component guides before implementation. Old shared Profile/Evidence/Baseline authority, Knowledge-first Save, parallel Fits and mandatory current assistant apply are superseded only as recorded in those owners.

**Observed baseline:** HEAD `66e2bb8dfd081a44b3a28873d5b992805ce46d56`; backend runtime schema 5, migration head `d092ea64bf17_invocation_durability.py` after `a41d7e90c263`. Existing SL-02.M1 backend/frontend and M2 backend implement the old model. Runtime M1 is implemented; production SL-03.M2 and later consumers are not. Current documentation publication changes no product code, database, dependency or generated client. Recheck git status and preserve unrelated edits; historical test counts below are not rerun evidence.

**Backend delta:** Compose independently frozen M1 runs; keep per-target results/costs/history and future owned compatibility/rescoring. Remove paired Candidate/Resume scheduling.

**Frontend delta:** Multi-select Jobs and show truthful per-target pending/undispatched/unknown/failure/success with exact source/history.

**Upstream and order:** Actual SL-05.M1 and reviewed batch/result policy.

**Data/API transition:** Q38/Q41 permits later explicit offline reset of the complete configured development DB/generated materials, including test Preferences/Entries/Runtime records, while preserving source/Git/configuration. Never reset on startup or during this documentary transfer. No legacy request adapter/data conversion/archive reader is required. Preserve published migration source history and post-transition immutable source/result/receipt histories. Coordinate changed backend schemas with generated clients; do not fabricate target availability from this handoff.

**Required proof and open blockers:** Future batch schemas/score policy pending. Prove partial failures, duplicate/concurrent targets, source changes mid-batch and old success preserved after failed rerun. This is required future evidence. Ready replacement Contracts do not establish runtime/browser/model acceptance; unrelated Pending future scopes remain blocked until their own consumer definitions and upstream capabilities are ready.

**Maintained verification entry:** [Backend guide](../../../backend/README.md), [frontend guide](../../../frontend/README.md), [Development](../../development.md), [UI system](../../ui/DESGIN.md). From repository root, inspect then use `UV_CACHE_DIR=/tmp/jobhunter-uv-cache ./scripts/check`, `npm --prefix frontend run api:generate`, `npm --prefix frontend run check` and `npm --prefix frontend run test:e2e` as consumed. Rendering requires the actual certified native/font environment; invocation requires its reviewed provider/configuration. For docs run `python3 scripts/check_contract_links.py` and `git diff --check`. Report executed commands and unexecuted scope; backend tests never substitute browser acceptance.
