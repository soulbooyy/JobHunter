# SL-01 Local Workspace, Manual Application Entries and Preferences

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. The later user-approved CG01-BC1 revises its scope; current scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Provide local Workspace, independent manual application entries and explicit search intent, plus a reusable deterministic screening component.

**Scope:** Local configuration and delivered navigation; separate mutable ManualApplicationEntry maintenance and explicit browser opening; global hard Preferences and pure metadata QuickScreen. Formal Job production, immutable versions, formal Job/Company read views and their current-Preferences integration belong to SL-08.M2 under the Job Contract.

**Out of Scope:** Formal Job production in this Slice, JD ingestion into manual entries, analysis/application tracking of entries, BOSS access, model tasks, automated sending, and compatibility-only bookmark/search-profile products. Undelivered entry points cannot appear implemented.

**Already-decided capabilities and provenance:** Q1/Q6/Q8/Q45/Q53/Q55–Q56/S17.1–S17.3 plus [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1). The later user decision supersedes the Manual Job portions of Q12/Q17/Q44/Q48/Q50 and CG01-Q2–Q5; original provenance remains preserved. Owners: [Product 2/4](../../spec.md#2-workspace-and-task-organization), [Architecture 3/4](../../architecture.md#3-authority-identity-and-evolution). The twelve-Slice/24-milestone allocation is retained with this explicit scope revision.

**Dependent Contract families:** F01, F02, F05 organizational grouping, F10. ManualApplicationEntry is outside the formal Job family despite its related document grouping.

**Test / Eval categories:** Entry persistence, repeated edits, separate view and browser-only effects; Preferences authority and deterministic pure screening. [Acceptance 3](../../acceptance.md#3-workspace-jobs-screening-and-collection) and applicable [Acceptance 10](../../acceptance.md#10-privacy-storage-and-honest-history). Component evidence does not prove a populated formal Job Pool.

**Required parent milestones:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-application-entries), [SL-01.M2](#sl-01m2-hard-preferences-and-pure-screening). Dependencies are implemented components, not completion of upstream parents.

## SL-01.M1 Local Workspace and Manual Application Entries

**Goal/value:** Maintain user-provided manual application destinations independently of formal Job workflows.

**Scope:** Local Workspace initialization/configuration; ManualApplicationEntry company, role title and user-provided application URL; repeated mutable edits and removal from current use; a separate view entered through a Job Pool button; explicit browser opening.

**Out of scope:** Formal Job/JobVersion, JD input/version history, freshness/availability reporting, Requirements, both Fits, targeted Advisor, Preparation, automated Execution and Application History. Opening the URL is not collection or an application fact. Physical entry deletion and independently retained create receipts follow the actual Entry/Storage Contracts; no immutable Job history is introduced.

**Required upstream capability:** None.

**Reused component/infrastructure:** None. Follow the [M1 development handoff](../../development/handoff/sl-01-m1-handoff.md) for target-stack adoption and verification of the actual minimal local setup.

**Required Contract portions before development:** [Common](../../contracts/common.md) COM-001–032; [Workspace](../../contracts/foundation/workspace.md) WSP-001–006; [ManualApplicationEntry](../../contracts/jobs/manual-application-entries.md) MAE-001–018; [Storage](../../contracts/foundation/storage.md) STO-001–013, all at scope revision `2026-09-19.M1-r1`. Their actual scope readiness and reviewed interface evidence are recorded in [Progress](../../progress/traceability.md#61-sl-01m1-reviewed-scope-and-interface-evidence). Additional Common/Workspace/Storage scopes and immutable Job history are not M1 prerequisites.

**Joint agreement:** Entry identity and operations do not supply Job identity or downstream eligibility. Browser navigation produces no ExecutionAttempt, approval consumption, application event or hidden conversion/collection. Common/storage guarantees cover actual local entry needs; formal Job semantics remain with `jobs/jobs-screening.md`.

**Research / implementation preparation:** The accepted Grill is complete through CG01-Q45. The [development handoff](../../development/handoff/sl-01-m1-handoff.md) records official-source integration findings, observed host limitations and actual adoption work. Begin by pinning/verifying the selected runtime/dependencies, driver transaction mode, lock and browser implementation; do not treat document research as executed product checks. No further product decision is currently required to start this bounded work.

**Tests / Eval:** [Acceptance 3.1](../../acceptance.md#31-sl-01m1-contract-conformance) maps the real requirement IDs to boundary, persistence, recovery, privacy and browser proof, with applicable V10. These remain future checks, not executed results.

**Milestone completion:** Real entry maintenance and browser opening work through the actual boundary, with truthful failure handling and durable saved records under their Contract. This establishes neither formal Jobs nor their consumers. Record scoped evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning).

## SL-01.M2 Hard Preferences and pure screening

**Goal/value:** Save explicit search intent and provide the deterministic screening component consumed by Collection and formal local views.

**Scope:** One global hard Preferences version; deterministic QuickScreen over admitted Job/source metadata, uncertainty and no model/Candidate/Requirement access. Define the producer/consumer agreement with Collection and formal local filtering without delivering their data producer here.

**Out of scope:** Screening ManualApplicationEntry, formal Job production, populated Job/Company views, remote acquisition and end-to-end filtering integration. Those formal local views and current-Preferences integration are delivered in SL-08.M2.

**Required upstream capability:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-application-entries) — usable local Workspace configuration; no formal Job data is expected from it.

**Reused component/infrastructure:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-application-entries) — applicable implemented local persistence/privacy primitives; add immutable Preference version support required by this consumer rather than claiming entry delivery supplied it.

**Required Contract portions before development:** `candidate/preferences.md` — hard intent and immutable versions; `jobs/jobs-screening.md` — the independently consumable pure metadata screening scope and necessary input/output agreement. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Preferences owns intent; `jobs/jobs-screening.md` owns canonical screening semantics; Collection translates frozen intent. SL-08.M2 integrates latest local filtering. M2 does not depend on SL-08.M2 completion, avoiding a screening/collection cycle.

**Research / unresolved Grill detail:** Resolve actual supported hard dimensions, consumer-justified metadata input and missing-input behavior. Do not infer numeric/default policy or expand the full Job schema merely to deliver this component.

**Tests / Eval:** V3: real Preferences persistence/versioning and executable pure predicates with controlled metadata inputs, deterministic uncertainty and no forbidden dependencies. Fixture checks prove the component only, not a populated user Job Pool or working source adapter.

**Milestone completion:** The actual Preferences boundary and screening component satisfy their owned rules and required checks. Real formal Job list/refilter integration remains SL-08.M2's obligation, not an unimplemented promise counted as complete here.

**Parent completion and remaining work:** Both milestones and their local integration are accepted: Workspace supports entry maintenance/browser opening and persisted Preferences usable by the pure screening component. Manual entries stay separate and are not screened as formal Jobs. Formal Job/Company views and current-Preferences refiltering are verified in SL-08.M2. All 2 milestones need their scoped Contracts, implementation and evidence; no completion is claimed. Parent completion is separate from rollout/production enablement.
