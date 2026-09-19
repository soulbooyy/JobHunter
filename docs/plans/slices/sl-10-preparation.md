# SL-10 Preparation, viewed-material confirmation and adopt-back

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. Its affected scope/dependencies now reflect user-approved [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1); scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Prepare exact current materials and a manually editable Greeting for each Job, making confirmed content and later execution authorization distinct.

**Scope:** Single/multi-Job independent Preparation, idempotent create/resume/reentry and revision conflicts; formal material selection/view, fixed generic Greeting, eligibility/render/readiness, actual-view MaterialApproval and exact snapshot preparation. Integrate existing Advisor through the same Session/entry semantics and explicit narrow adopt-and-return.

**Out of Scope:** Automatic sending, ExecutionApproval/Attempt consumption, editing Resume body inside Preparation, personalized/generated Greeting or silent adoption of changed facts.

**Already-decided capabilities and provenance:** Q16, Q25, Q30, Q36, Q42, Q77, Q91, Q108, Q118, Q146–Q147, Q150, Q152, Q157, Q162, Q165. Actual behavior/mechanism owners: [P7](../../spec.md#7-application-preparation-and-materials); [A5.4](../../architecture.md#54-grounding-and-demand-driven-artifacts); [A7](../../architecture.md#7-session-advisor-proposal-and-confirmed-changes); [A8](../../architecture.md#8-preparation-execution-and-application-events). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F05, F07, F09, F10, F11.

**Test / Eval categories:** Actual rendered artifact versus mere version, Greeting reconfirmation, unchanged bytes with revoked eligibility, concurrent edits, duplicate reentry and multiple candidates, explicit adopt-back preserving Greeting/unrelated edits, render failure and independent batch preparation. Required proof destinations: [V4.3](../../acceptance.md#43-demand-and-safe-derivative-recovery); [V6](../../acceptance.md#6-advisor-proposal-confirmation-and-session); [V7](../../acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.3](../../acceptance.md#93-streams-presentation-and-safe-work); [Eval acceptance 2.2](../../acceptance/evaluation.md#22-n1-and-complete-scenarios). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-10.M1](#sl-10m1-ordinary-preparation-and-viewed-material-approval), [SL-10.M2](#sl-10m2-explicit-advisor-adopt-back). Dependencies are implemented components, not completion of upstream parents.

## SL-10.M1 Ordinary Preparation and viewed-material approval

**Goal/value:** Prepare exact materials and Greeting for a chosen Job before deciding to execute.

**Scope:** Preparation selection/reentry, required material demand, fixed default/manual Greeting, actual viewed-content approval and immutable intended-input snapshot.

**Out of scope:** Advisor dependency, adopt-back, Resume-body editing in Preparation, automatic sending or inferred ExecutionApproval.

**Required upstream capability:** [SL-02.M2](sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) — eligible actual rendered materials and their saved sources; [SL-08.M2](sl-08-collection-platform-safety.md#sl-08m2-boss-collection-and-explicit-refresh) — eligible formal Job targets; ManualApplicationEntry is excluded

**Reused component/infrastructure:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — source/currentness checks and durable demanded intent

**Required Contract portions before development:** `applications/preparation.md` — ordinary preparation, selection/reentry/Greeting/viewed approval and ApplicationExecutionSnapshot definition; `applications/materials.md`, `foundation/derived-work.md` — required channel demand/readiness; `candidate/resumes-grounding.md`, `candidate/profile.md`, `candidate/evidence.md`, `jobs/jobs-screening.md` — actual eligibility; `applications/execution.md` — necessary snapshot-consumer agreement only. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Preparation owns snapshot meaning. Agree execution's reference/eligibility boundary now, without requiring all sending protocol or implementation. Frozen viewed material/Greeting is not consent to send.

**Research / unresolved Grill detail:** Research actual material/channel requirements and readiness; no channel format/payload is frozen here.

**Tests / Eval:** V4.3, V7, V10: reentry/conflicts, exact viewed material versus later edits, Greeting, demand/readiness and absence of accidental execution consent. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real ordinary Preparation produces a correctly bound intended snapshot and preserves separate send authorization without Advisor. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-10.M2 Explicit Advisor adopt-back

**Goal/value:** Use Advisor optimization without silently overwriting ongoing Preparation edits.

**Scope:** Preparation-origin Advisor entry, saved confirmed formal result and explicit narrow compare-and-set return/adoption.

**Out of scope:** Implicit adoption, replacing unrelated mutable fields, reviving old Advisor drafts and automatic send.

**Required upstream capability:** [SL-10.M1](#sl-10m1-ordinary-preparation-and-viewed-material-approval) — ordinary Preparation; [SL-07.M2](sl-07-advisor.md#sl-07m2-job-targeted-discussion-and-dependency-waiting) — Job-originated Advisor integration; [SL-07.M3](sl-07-advisor.md#sl-07m3-exact-proposals-and-confirmed-formal-changes) — explicitly confirmed saved formal result

**Reused component/infrastructure:** [SL-07.M1](sl-07-advisor.md#sl-07m1-durable-advisor-discussion) — Session/source references and foreground coordination

**Required Contract portions before development:** `applications/preparation.md` — Advisor entry/reentry and narrow adoption/conflicts; `agent/sessions.md` — actual source/entry linkage; `candidate/advisor-changes.md` — eligible committed result reference; `applications/materials.md` — newly demanded current output; `evaluation/evaluation-observability.md` — adoption/conflict Scenario. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Proposal Save remains the formal authority boundary; later adoption changes only authorized Preparation selection. Concurrent Greeting/other preparation work must survive.

**Research / unresolved Grill detail:** Resolve reference and conflict semantics across the three owners; reuse material feasibility rather than inventing new output formats.

**Tests / Eval:** V6, V7, V12–13: actual saved result, explicit adopt, competing Preparation edits, cancellation/reentry and no implied send approval. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real optimization can be explicitly adopted without unrelated data loss or a second formal mutation authority. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Prepared and confirmed content is inspectable and exactly bound, including an honest readiness failure when required materials are absent. Neither approval nor snapshot performs external action; adopted formal changes require no hidden target or permission. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover ordinary Preparation and optional Advisor optimization/adoption without implicit send consent. Parent completion is separate from rollout/production enablement.
