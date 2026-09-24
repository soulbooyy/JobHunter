# Contract Index

[Global documentation index](../index.md) · [Contracts Overview](README.md)

## Existing supporting documents

These existing files provide navigation or organization, not normative Contract bodies.

| Document | Navigation destination |
| --- | --- |
| [README.md](README.md) | Contracts Overview |
| [index.md](index.md) | This Contract Index |
| [structure.md](structure.md) | Contract Structure, planned catalog and consumer locators |

## Existing normative Contracts

Sixteen scoped normative bodies now exist: the preserved `2026-09-19.M1-r1`, `2026-09-20.M2-r1` and `2026-09-21.S2M1-r1` baselines plus `2026-09-21.S2M2-r1`, `2026-09-23.S3M1-r1` and `2026-09-24.S3M2-r1`. There are 453 stable requirement IDs, including 48 scoped additions in **2026-09-24.S2M1S1-r1**; replaced IDs remain historical with explicit applicability notices. Existence does not complete their future families; actual readiness/evidence is in [Progress](../progress/traceability.md#6-contract-normative-scope-readiness-ledger).

| Document | Existing scope | Requirement IDs |
| --- | --- | --- |
| [Common](common.md) | Shared expression and scoped SL-01/S2/SL-03.M1/M2 identity, scalar, path and error vocabulary | COM-001–051 |
| [Workspace](foundation/workspace.md) | Local initialization/runtime and scoped default Resume selection | WSP-001–015 |
| [ManualApplicationEntry](jobs/manual-application-entries.md) | Seven-field mutable entry, commands, HTTP, browser handoff and client recovery | MAE-001–018 |
| [Storage](foundation/storage.md) | Explicit development reset/new source/projection persistence plus surviving local/runtime/material durability | STO-001–058 |
| [Preferences](candidate/preferences.md) | Complete collection intent, immutable history, Save/read/replay and future UI boundary | PRF-001–024 |
| [Profile](candidate/profile.md) | Read-only schema-v1 capability projection; historical contact values reused by Resume | PRO-001–016 |
| [Evidence/Baseline](candidate/evidence.md) | Deterministic exact-version Entry/Block projection; historical independent fact/Baseline model superseded | EVD-001–023 |
| [Resume](candidate/resumes-grounding.md) | Complete independent document/contacts/structured fields/canonical AST and stable logical IDs | RES-001–024 |
| [Candidate Save](candidate/candidate-save.md) | Six current document/default/refresh commands, schema-2 receipts and atomic portrait obligation; legacy protocol superseded | SAV-001–025 |
| [Materials](applications/materials.md) | Direct exact Resume source/schema-2 manifest; surviving explicit demand/configuration/verified bytes | MAT-001–033 |
| [Derived Work](foundation/derived-work.md) | Exact demand/receipts, atomic Work selection, execution/fencing/recovery and client protocol | DRW-001–026 |
| [Execution Runtime](agent/execution-runtime.md) | Preserved M1 plus protected semantic-start/dispatch and controlled DeepSeek interface | EXR-001–057 |
| [Evaluation / Observability](evaluation/evaluation-observability.md) | Preserved M1 plus isolated M2 evidence/evaluators/export and required proof | EVO-001–027 |
| [Tools](agent/tools.md) | Static typed registry, one-request admission, exact read projection and action recovery | TOL-001–015 |
| [Context](agent/context.md) | Exact headless Package/Frame, provenance, capacity and historical access | CTX-001–016 |
| [Budget](foundation/budget.md) | Foreground allocation, CNY reservation, absolute metering and unresolved exposure | BUD-001–025 |

[SL-03.M1 review](../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) covers only its foundation. The [M2 scope review](../progress/traceability.md#66-sl-03m2-reviewed-scope-and-interface-evidence) records its published foundations and closed concrete exercise agreement; implementation/adoption proof remains outstanding. Future platform reuse and cleanup remain Pending.

The [supplemental review](../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope) replaces shared candidate authority, two-stage import and parallel Fits. SL-05 owns DeepFit; SL-06 owns selected-Resume optimization; SL-07.M3/SL-10.M2 apply/adoption is deferred. Earlier source reviews/evidence remain historical. Future consumer Contracts remain pending as scoped in the ledger.

## Planned normative Contract documents

The following 12 destinations are planned only. Links open their entries in Contract Structure; they do not point to nonexistent files.

| Planned path relative to this directory | Structure entry |
| --- | --- |
| `candidate/resume-import.md` | [Planned catalog entry](structure.md#planned-resume-import) |
| `candidate/advisor-changes.md` | [Planned catalog entry](structure.md#planned-advisor-changes) |
| `jobs/jobs-screening.md` | [Planned catalog entry](structure.md#planned-jobs-screening) |
| `jobs/collection.md` | [Planned catalog entry](structure.md#planned-collection) |
| `jobs/platform-safety.md` | [Planned catalog entry](structure.md#planned-platform-safety) |
| `jobs/requirements.md` | [Planned catalog entry](structure.md#planned-requirements) |
| `jobs/fit-analysis.md` | [Planned catalog entry](structure.md#planned-fit-analysis) |
| `applications/preparation.md` | [Planned catalog entry](structure.md#planned-preparation) |
| `applications/execution.md` | [Planned catalog entry](structure.md#planned-execution) |
| `applications/application-history.md` | [Planned catalog entry](structure.md#planned-application-history) |
| `agent/sessions.md` | [Planned catalog entry](structure.md#planned-sessions) |
| `agent/memory.md` | [Planned catalog entry](structure.md#planned-memory) |

For family mapping and references, open [Contract Structure](structure.md). For each consuming milestone, open the [Slice plan index](../plans/slices/README.md). This index records navigation, not detailed rules or a readiness decision.
