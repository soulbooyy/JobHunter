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

Sixteen scoped normative bodies now exist: the preserved `2026-09-19.M1-r1`, `2026-09-20.M2-r1` and `2026-09-21.S2M1-r1` baselines plus `2026-09-21.S2M2-r1`, `2026-09-23.S3M1-r1` and `2026-09-24.S3M2-r1`. There are 405 stable requirements, including 105 scoped SL-03.M2 additions. Existence does not complete their future families; actual readiness/evidence is in [Progress](../progress/traceability.md#6-contract-normative-scope-readiness-ledger).

| Document | Existing scope | Requirement IDs |
| --- | --- | --- |
| [Common](common.md) | Shared expression and scoped SL-01/S2/SL-03.M1/M2 identity, scalar, path and error vocabulary | COM-001–049 |
| [Workspace](foundation/workspace.md) | Local initialization/runtime and scoped default Resume selection | WSP-001–012 |
| [ManualApplicationEntry](jobs/manual-application-entries.md) | Seven-field mutable entry, commands, HTTP, browser handoff and client recovery | MAE-001–018 |
| [Storage](foundation/storage.md) | Preserved schema-1/2/3 consumers plus M2 forward migration, Materials relationships/files, recovery integrity and M1/M2 invocation/accounting evidence | STO-001–053 |
| [Preferences](candidate/preferences.md) | Complete collection intent, immutable history, Save/read/replay and future UI boundary | PRF-001–023 |
| [Profile](candidate/profile.md) | Exact three-field contact snapshots/privacy and Materials projection | PRO-001–009 |
| [Evidence/Baseline](candidate/evidence.md) | Six typed facts, semantic body, current/history, Baseline and Materials structured projection | EVD-001–015 |
| [Resume](candidate/resumes-grounding.md) | Exact lineage, local expression/presentation, editor/lifecycle and Materials source interface | RES-001–016 |
| [Candidate Save](candidate/candidate-save.md) | Nine preserved commands/results/receipts plus exact-only Materials consumer agreement | SAV-001–017 |
| [Materials](applications/materials.md) | Preserved source boundary plus exact source projection, immutable configuration/provenance/Artifact, PDF/PNG and read/content APIs | MAT-001–030 |
| [Derived Work](foundation/derived-work.md) | Exact demand/receipts, atomic Work selection, execution/fencing/recovery and client protocol | DRW-001–026 |
| [Execution Runtime](agent/execution-runtime.md) | Preserved M1 plus protected semantic-start/dispatch and controlled DeepSeek interface | EXR-001–057 |
| [Evaluation / Observability](evaluation/evaluation-observability.md) | Preserved M1 plus isolated M2 evidence/evaluators/export and required proof | EVO-001–026 |
| [Tools](agent/tools.md) | Static typed registry, one-request admission, exact read projection and action recovery | TOL-001–014 |
| [Context](agent/context.md) | Exact headless Package/Frame, provenance, capacity and historical access | CTX-001–015 |
| [Budget](foundation/budget.md) | Foreground allocation, CNY reservation, absolute metering and unresolved exposure | BUD-001–025 |

[SL-03.M1 review](../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) covers only its foundation. The [M2 scope review](../progress/traceability.md#66-sl-03m2-reviewed-scope-and-interface-evidence) records its published foundations and closed concrete exercise agreement; implementation/adoption proof remains outstanding. Future platform reuse and cleanup remain Pending.

The planned S2+ scopes follow [CG03-BC3/A1–A5](../design/contract/sl-02-m1-grill.md#cg03-bc3): separate Knowledge/Profile/Resume commands, exact historical lineage/local expression and unified DeepFit with independent analyses. Former universal GroundingSet/Ensure representation is reopened. Existing SL-01 clauses are preserved; S2 adds scoped shared clauses and five actual bodies. [S2 review](../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) records consumed readiness. [SL-02.M2 review](../progress/traceability.md#64-sl-02m2-reviewed-scope-and-interface-evidence) covers its actual consumed portions and preserved consumers. Future AI/Import/Fit/Preparation and follow-current extensions remain pending; renderer implementation/evidence is separate.

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
