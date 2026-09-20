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

Ten scoped normative bodies now exist: the preserved `2026-09-19.M1-r1` and `2026-09-20.M2-r1` baselines plus `2026-09-21.S2M1-r1`. There are 178 stable requirements, including 73 S2 additions. Existence does not complete their future families; actual readiness/evidence is in [Progress](../progress/traceability.md#6-contract-normative-scope-readiness-ledger).

| Document | Existing scope | Requirement IDs |
| --- | --- | --- |
| [Common](common.md) | Shared expression and scoped SL-01/S2 identity, scalar, path and error vocabulary | COM-001–042 |
| [Workspace](foundation/workspace.md) | Local initialization/runtime and scoped default Resume selection | WSP-001–011 |
| [ManualApplicationEntry](jobs/manual-application-entries.md) | Seven-field mutable entry, commands, HTTP, browser handoff and client recovery | MAE-001–018 |
| [Storage](foundation/storage.md) | Published schema-1/2 baseline plus schema-3 authority, receipts, lineage and evolution | STO-001–028 |
| [Preferences](candidate/preferences.md) | Complete collection intent, immutable history, Save/read/replay and future UI boundary | PRF-001–023 |
| [Profile](candidate/profile.md) | Exact three-field contact snapshots/privacy | PRO-001–008 |
| [Evidence/Baseline](candidate/evidence.md) | Six typed facts, semantic body, current/history and complete Baseline | EVD-001–014 |
| [Resume](candidate/resumes-grounding.md) | Exact lineage, local expression/presentation, editor and lifecycle | RES-001–015 |
| [Candidate Save](candidate/candidate-save.md) | Nine commands, results, receipts, canonical fingerprint, HTTP and recovery | SAV-001–016 |
| [Materials source boundary](applications/materials.md) | Saved sources/currentness and Save-not-output-ready only; actual rendering remains M2 | MAT-001–003 |

The planned S2+ scopes follow [CG03-BC3/A1–A5](../design/contract/sl-02-m1-grill.md#cg03-bc3): separate Knowledge/Profile/Resume commands, exact historical lineage/local expression and unified DeepFit with independent analyses. Former universal GroundingSet/Ensure representation is reopened. Existing SL-01 clauses are preserved; S2 adds scoped shared clauses and five actual bodies. [S2 review](../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) records consumed readiness. Future AI/Import/Fit/material-work extensions remain pending.

## Planned normative Contract documents

The following 18 destinations are planned only. Links open their entries in Contract Structure; they do not point to nonexistent files.

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
| `agent/execution-runtime.md` | [Planned catalog entry](structure.md#planned-execution-runtime) |
| `agent/tools.md` | [Planned catalog entry](structure.md#planned-tools) |
| `agent/context.md` | [Planned catalog entry](structure.md#planned-context) |
| `agent/sessions.md` | [Planned catalog entry](structure.md#planned-sessions) |
| `agent/memory.md` | [Planned catalog entry](structure.md#planned-memory) |
| `foundation/budget.md` | [Planned catalog entry](structure.md#planned-budget) |
| `foundation/derived-work.md` | [Planned catalog entry](structure.md#planned-derived-work) |
| `evaluation/evaluation-observability.md` | [Planned catalog entry](structure.md#planned-evaluation-observability) |

For family mapping and references, open [Contract Structure](structure.md). For each consuming milestone, open the [Slice plan index](../plans/slices/README.md). This index records navigation, not detailed rules or a readiness decision.
