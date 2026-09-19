# SL-11 Explicit authorized execution and independent batch outcomes

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. Its affected scope/dependencies now reflect user-approved [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1); scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Execute exactly approved applications with trustworthy outcome tracking, bounded shared platform access and honest uncertainty.

**Scope:** Separate exact, scoped, expiring, single-use ExecutionApproval; at most one Attempt consuming it; frozen material/source eligibility; authorized minimal live identity/availability checks; independent per-Job scheduling/outcomes, narrower renewed approval for partial continuation, reliable read-back into real application events and persistent shared risk handling.

**Out of Scope:** Silent Job refresh or Requirement parsing, new model Job analysis, automatic replay after unknown effects, assuming a technical click is business success, cross-Job transactions, undispatched-as-failed reporting and future Monitor.

**Already-decided capabilities and provenance:** Q25, Q30–Q31, Q36–Q37, Q42, Q77, Q122, Q150, Q157, Q160, Q164, Q173–Q174. Actual behavior/mechanism owners: [P8](../../spec.md#8-external-execution-and-application-tracking); [A4.3](../../architecture.md#43-observation-and-safety-boundaries); [A8](../../architecture.md#8-preparation-execution-and-application-events); [A12](../../architecture.md#12-durable-execution-and-recovery); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F04, F05, F07, F10, F11.

**Test / Eval categories:** Concurrent double consumption, stale/changed input, closure/mismatch without refresh, crash around dispatch/receipt, unknown results without success/retry, reliable read-back/human evidence, Collector-to-Executor risk propagation, explicit restoration without auto-resume, independent batch/undispatched outcomes. Required proof destinations: [V7](../../acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.2](../../acceptance.md#92-crash-and-cancellation-boundaries); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 2.1](../../acceptance/evaluation.md#21-isolation-exact-inputs-and-declared-experiment-scope); [Eval acceptance 2.2](../../acceptance/evaluation.md#22-n1-and-complete-scenarios). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-11.M1](#sl-11m1-single-authorized-verified-execution), [SL-11.M2](#sl-11m2-independent-execution-batches). Dependencies are implemented components, not completion of upstream parents.

## SL-11.M1 Single authorized verified execution

**Goal/value:** Execute an explicitly approved application with honest external outcome and history.

**Scope:** Separate scoped single-use ExecutionApproval, Attempt/technical observations, authorized minimal live checks, actual channel action/read-back verification and admitted business events.

**Out of scope:** Advisor/adopt-back, requiring a new collection before each execution, treating collection success as execution consent, model/Requirement/Fit dependency, full refresh during checks and replay of unknown effects. The actual formal Job producer remains an upstream capability through Preparation/history; ManualApplicationEntry browser opening is outside this execution flow.

**Required upstream capability:** [SL-10.M1](sl-10-preparation.md#sl-10m1-ordinary-preparation-and-viewed-material-approval) — exact intended snapshot and eligible material; [SL-09.M1](sl-09-application-history.md#sl-09m1-human-application-history-and-progress) — real event/history authority; [SL-08.M1](sl-08-collection-platform-safety.md#sl-08m1-shared-recruiting-platform-safety) — shared risk admission

**Reused component/infrastructure:** [SL-03.M1](sl-03-invocation-requirements.md#sl-03m1-invocation-durability-and-recovery-foundation) — applicable invocation durability/fencing/unknown-outcome protection

**Required Contract portions before development:** `applications/execution.md` — approval/consumption/Attempt/minimal checks/read-back; `applications/preparation.md` — intended snapshot consumption; `applications/materials.md` — eligibility; `jobs/platform-safety.md` — execution agreement; `applications/application-history.md` — verified channel event admission; `agent/execution-runtime.md`, `foundation/storage.md` — actual external-effect proof/recovery; `evaluation/evaluation-observability.md` — controlled authorization/risk/fault scenarios. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Resolve snapshot → separate consent → risk admission → effect → verified event together. Technical clicks/narration are not application facts. Unknown outcomes use shared recovery and never become automatic resend.

**Research / unresolved Grill detail:** Verify channel feasibility, actual read-back and admissible evidence before implementation; exact payload/approval representation remains Grill work.

**Tests / Eval:** V7, V9.2, V10, applicable V12: wrong/stale scope, duplicate approval, risk, crash/unknown, minimal checks versus refresh, verified success and honest failure. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** One actual authorized attempt produces only justified technical and business outcomes under shared safety/recovery. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-11.M2 Independent execution batches

**Goal/value:** Handle selected prepared applications while preserving each Job's authorization and outcome.

**Scope:** Batch orchestration of independently eligible snapshots, required per-target authorization, shared safety admission and independent Attempt/event outcomes.

**Out of scope:** Batch transaction/rollback fiction, reuse of consumed approvals, automatic authorization by selection and bypass of risk after earlier success.

**Required upstream capability:** [SL-11.M1](#sl-11m1-single-authorized-verified-execution) — single authorized and verified attempt

**Reused component/infrastructure:** [SL-11.M1](#sl-11m1-single-authorized-verified-execution) — per-target approval, outcome and shared safety/recovery components

**Required Contract portions before development:** `applications/execution.md` — batch eligibility/approval consumption and independent outcomes; `jobs/platform-safety.md` — competing batch access; `applications/application-history.md` — independent admitted outcomes; `evaluation/evaluation-observability.md` — partial/risk/fault evidence. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Reuse the complete single-attempt interfaces for every target; shared capacity/risk can stop later work without rewriting already established real outcomes.

**Research / unresolved Grill detail:** Resolve concrete batch admission/stop/reentry interface; no quota or schedule is selected by this plan.

**Tests / Eval:** V7, V9.2, V10: partial success, consumed/stale target, concurrent risk, interruption and no fabricated rollback or repeated side effect. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Actual batches preserve per-target consent, evidence and honest partial outcomes. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** The delivered channel executes only admitted frozen approvals and records real outcomes with traceable evidence; uncertain outcomes remain uncertain. Deterministic/fault/scenario checks use controlled adapters; they grant no live recruiting-site access themselves. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover single and batch attempts through separate consent, safety, verification and real history. Parent completion is separate from rollout/production enablement.
