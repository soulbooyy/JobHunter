# SL-01 Local Workspace, Manual Application Entries and Preferences

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. The later user-approved CG01-BC1 revises its scope; current scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Provide local Workspace, independent manual application entries and explicit versioned future acquisition intent.

**Scope:** Local configuration and delivered navigation; separate mutable ManualApplicationEntry maintenance and explicit browser opening; complete explicit Preferences and immutable Preference versions. Formal Job production, immutable Job versions, formal Job/Company read views and independent view-query integration belong to SL-08.M2 under the Job Contract.

**Out of Scope:** Formal Job production in this Slice, JD ingestion into manual entries, analysis/application tracking of entries, BOSS access, model tasks, automated sending, and compatibility-only bookmark/search-profile products. Undelivered entry points cannot appear implemented.

**Already-decided capabilities and provenance:** Q1/Q6/Q8/Q45/Q53/Q55–Q56/S17.1–S17.3 plus [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1). The later user decision supersedes the Manual Job portions of Q12/Q17/Q44/Q48/Q50 and CG01-Q2–Q5; original provenance remains preserved. Owners: [Product 2/4](../../spec.md#2-workspace-and-task-organization), [Architecture 3/4](../../architecture.md#3-authority-identity-and-evolution). The twelve-Slice/24-milestone allocation is retained with this explicit scope revision.

**Dependent Contract families:** F01, F02, F05 organizational grouping, F10. ManualApplicationEntry is outside the formal Job family despite its related document grouping.

**Test / Eval categories:** Entry persistence, repeated edits, separate view and browser-only effects; Preferences configuration/version/read/Save/concurrency. [Acceptance 3](../../acceptance.md#3-workspace-jobs-screening-and-collection) and applicable [Acceptance 10](../../acceptance.md#10-privacy-storage-and-honest-history). Component evidence does not prove a populated formal Job Pool.

**Required parent milestones:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-application-entries), [SL-01.M2](#sl-01m2-collection-preferences-and-immutable-versions). Dependencies are implemented components, not completion of upstream parents.

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

<a id="sl-01m2-hard-preferences-and-pure-screening"></a>
## SL-01.M2 Collection Preferences and immutable versions

**Goal/value:** Save complete explicit acquisition intent for future Collection with immutable history and safe concurrent editing.

**Scope:** One global PreferenceSet; six explicitly configured dimensions (job search keywords, cities, salary, recruitment types, company exclusions and required-education ceiling); lazy atomic root/first-version creation, complete immutable PreferenceSetVersion publication, read/Save, canonical equality/no-op, revision admission and exact-reference persistence. [CG02-BC1](../../design/contract/sl-01-m2-grill.md#cg02-bc1) and [CG02-S1](../../design/contract/sl-01-m2-grill.md#cg02-s1) replace the previous pure-screening and deferred-versioning scope. No formal acquisition may start before complete explicit configuration; allowed no-constraint choices are dimension-specific, not missing fields.

**Out of scope:** QuickScreen, candidate admission, source query mapping, formal Job production, Job/Company views or query filters, remote acquisition, implicit keyword expansion, and screening ManualApplicationEntry. These source/admission/query consumers belong to later scopes, principally SL-08.M2. M2 does not create a pure component without a real current consumer.

**Required upstream capability:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-application-entries) — the implemented usable local backend/configuration component; M2 backend need not wait for M1 frontend. Full milestone completion remains governed by each milestone's declared scope.

**Reused component/infrastructure:** Applicable implemented M1 persistence/privacy/startup primitives. Add actual immutable Preference state, current selection and revision support. Define explicit compatible storage evolution before using an existing M1 database; no implicit upgrade or replacement empty store.

**Required Contract portions before development:** [Preferences](../../contracts/candidate/preferences.md) PRF-001–023; [Common](../../contracts/common.md) COM-033–037 and their explicitly reused baseline conventions/scalars/error shape; [Workspace](../../contracts/foundation/workspace.md) WSP-007 and its inherited local guarantees; [Storage](../../contracts/foundation/storage.md) STO-014–020 and inherited M1 durability/privacy/transaction guarantees. M2 scope revision is `2026-09-20.M2-r1`; readiness is in [Progress 6.2](../../progress/traceability.md#62-sl-01m2-reviewed-scope-and-interface-evidence). `jobs/jobs-screening.md` is not an M2 prerequisite.

**Joint agreement:** Preferences owns user intent, not platform query encoding or admission rules. Future Collection consumes one complete exact PreferenceSetVersion; later edits do not change active Runs or existing Jobs. Job Pool view filters are independent of Preferences and do not publish versions. Collection/admission/query details are defined at their real consumers, without requiring them to be implemented for M2.

**Research / implementation preparation:** Accepted Grill is complete through CG02-Q40. [M2 development handoff](../../development/handoff/sl-01-m2-handoff.md) records the actual schema-1 baseline, explicit schema-2 migration obligations, backend-first work and deferred UI design. No Collection mapping is inferred from enums. Concrete migration command, SQL checks and test layout are implementation choices within the normative requirements.

**Tests / Eval:** Real Preference read/Save and restart persistence; six-dimensional configuration admission; immutable version/current/revision atomicity; canonical no-op and stale saves; exact historical reads as consumed; explicit storage evolution and privacy. These prove Preferences, not working Collection, a populated Job Pool or UI/browser acceptance. See [Acceptance 3.2](../../acceptance.md#32-sl-01m2-contract-conformance).

**Milestone completion:** The declared Preference configuration/version/read/Save/concurrency capability and applicable proof are complete under ready Contracts. Collection/admission/query integration remains SL-08.M2's obligation. No implementation or acceptance is claimed by this plan revision.

**Parent completion and remaining work:** Both milestones and their actual local integration are accepted: Workspace supports manual-entry maintenance/browser opening and saved complete versioned acquisition intent. Manual entries stay outside formal Job workflows. Formal Job views, independent queries, source acquisition and admission are verified in SL-08.M2. All 2 milestones require their own Contracts, implementation and evidence; parent completion remains separate from rollout.
