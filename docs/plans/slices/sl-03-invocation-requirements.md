# SL-03 Shared controlled execution with RequirementParse

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. Its affected scope/dependencies now reflect user-approved [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1); scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 3 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Deliver the first reusable semantic capability through the real protected execution path, making later Skills consumers of one verified runtime rather than separate ad hoc integrations.

**Scope:** Application Ensure and pure requirement reads for exact complete Jobs; durable single-flight parsing, compatible reuse, owner-only charging, bounded repair and usable-target checks. Introduce the shared Run/Model/Tool admission, exact Context, budget/reservation, response/recovery/fencing, cancellation, protected-input revocation and privacy/audit substrate required by this task, plus its real-path Eval/observability support.

**Out of Scope:** Candidate/Resume Fit judgments, interactive Advisor/Session compaction, Memory learning, autonomous RAG, hidden SDK retries, whole-system generic framework work, fixed rollout thresholds or mandatory annotated parser certification.

**Already-decided capabilities and provenance:** Q10, Q14, Q58–Q59, Q83, Q110–Q111, Q117, Q120–Q126, Q132, Q135–Q136, Q140–Q144, Q159, Q171–Q187, S7.1, S22.1, S24.1, S35.1. Actual behavior/mechanism owners: [P5.1](../../spec.md#51-shared-on-demand-requirements); [P9](../../spec.md#9-privacy-controlled-execution-and-honest-recovery); [P11](../../spec.md#11-quality-and-evidence-boundaries); [A6.1](../../architecture.md#61-independent-dependency-preparation); [A9](../../architecture.md#9-shared-harness-skills-and-controlled-actions); [A10](../../architecture.md#10-context-engineering); [A11](../../architecture.md#11-budgets-and-resource-admission); [A12](../../architecture.md#12-durable-execution-and-recovery); [A13](../../architecture.md#13-storage-retention-and-audit); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F05, F06, F08, F09, F10, F11.

**Test / Eval categories:** Bounded parse success/repair/failure and unusable targets; concurrent Ensure/waiter cancellation/owner failure; exact admitted inputs/capacity/revocation; hidden retry prevention, atomic budget/race/fault-injection and unknown usage; real-JD/manual semantic review; isolated replay/live trials, alternative valid outputs, independent judge and telemetry-failure evidence. Required proof destinations: [V5.1](../../acceptance.md#51-dependency-preparation-and-bounded-parsing); [V8](../../acceptance.md#8-harness-tools-and-actual-context); [V9](../../acceptance.md#9-budget-durable-execution-and-recovery); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 2](../../acceptance/evaluation.md#2-eval-execution-and-evidence-integrity); [Eval acceptance 3](../../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-03.M1](#sl-03m1-invocation-durability-and-recovery-foundation), [SL-03.M2](#sl-03m2-protected-semantic-invocation-and-evidence), [SL-03.M3](#sl-03m3-requirementparse-and-shared-ensure). Dependencies are implemented components, not completion of upstream parents.

## SL-03.M1 Invocation durability and recovery foundation

**Goal/value:** Establish bounded invocation durability and recovery primitives for known Harness consumers, with only demonstrated applicable reuse by platform callers.

**Scope:** Invocation intent/dispatch/complete-response persistence, ownership/fencing, cancellation/startup reconciliation, unknown-outcome handling and safe local continuation from a durable response; canonical invocation evidence and active payload retention. Derive the minimum interfaces from the known Model/Tool invocation consumers, not from hypothetical external systems.

**Out of scope:** A universal external-side-effect framework, generic workflow/command bus, arbitrary effect adapters, shared business lifecycle, authority Save/Proposal commit protocol, safe render scheduling, platform risk policy, approval/event semantics, platform access itself and RequirementParse. Do not require AgentRun for deterministic workflows. Do not move these responsibilities into this foundation to increase reuse.

**Required upstream capability:** None.

**Reused component/infrastructure:** [SL-01.M1](sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-application-entries) — only applicable durable local persistence/diagnostic facilities; extend reference/recovery support for this consumer where needed, with no Job workflow prerequisite

**Required Contract portions before development:** `agent/execution-runtime.md` — bounded invocation durability/recovery primitives; `foundation/storage.md` — durable payload/audit, active recovery dependencies and cleanup; `evaluation/evaluation-observability.md` — evidence of these deterministic boundary checks only. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** execution-runtime remains the single owner of invocation/recovery protocol; storage owns availability. Budget, platform-safety, candidate-save, derived-work, collection and execution keep their existing responsibilities. A Collector/Executor may reuse compatible persistence/fencing/unknown-outcome primitives with a concrete interface justification; its workflow, consent, risk and business result stay with its owner. Similar failure terminology alone does not justify a universal abstraction.

**Research / unresolved Grill detail:** Confirm crash/transaction/adapter behavior required by the bounded component. Implement only the minimum invocation interfaces exercised by identified consumers; justify any platform reuse against its actual invocation boundary. Do not expand the foundation to make every side effect look alike.

**Tests / Eval:** V9.2, V10: controlled actual invocation component calls, before/after-dispatch crashes, durable response reuse, stale owner and unknown outcomes; controlled adapters may fault the boundary without pretending to be a business Skill. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Invocation persistence/recovery primitives have executable boundary and fault proof, and the ownership review confirms that Save, derived work, consent, platform risk and business workflows remain outside this foundation. This enabling milestone proves no working parser, collector or sender. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-03.M2 Protected semantic invocation and evidence

**Goal/value:** Make real model invocation safe and inspectable before any semantic task uses it.

**Scope:** Bounded Skill/Run and actual Model/Tool execution, Gateway/stream boundary, permissions, exact headless Context/capacity/revocation, foreground/operation budget and settlement, no hidden retry, canonical evidence and admitted telemetry.

**Out of scope:** Requirement meaning/Ensure comes in M3; interactive compaction and Memory extensions belong to their first consumers.

**Required upstream capability:** None.

**Reused component/infrastructure:** [SL-03.M1](#sl-03m1-invocation-durability-and-recovery-foundation) — bounded invocation persistence, ownership/fencing and recovery primitives

**Required Contract portions before development:** `agent/execution-runtime.md` — bounded semantic execution and presentation; `agent/tools.md` — capability intersection and owned action admission; `agent/context.md` — exact actual Frame, headless capacity/revocation; `foundation/budget.md` — owner/reservation/settlement/unknown limits; `foundation/storage.md` — semantic evidence/payload retention; `evaluation/evaluation-observability.md` — isolated real-path infrastructure, fixtures/configuration, checker completeness, separate judge resources, regression retention, output-preserving re-evaluation and derived export. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Runtime/Context/Tools/Budget/Storage jointly close first-call safeguards. Business commits and settlement never depend on telemetry. Task-specific evaluator meaning is completed by each first semantic consumer, not invented in this enabling milestone.

**Research / unresolved Grill detail:** Verify selected LangGraph, provider SDK, self-hosted Langfuse, callback/masking and judge integration against pinned sources/licenses; no deployment or version is assumed.

**Tests / Eval:** V8.1–8.2 headless scope, V9–10, V12 infrastructure: real invocation admission and provider-adapter fault paths, exact Frames, whole-Run budget, streams, hidden retry, masking/export failure and retained evidence. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real bounded invocation can be exercised with complete safety/evidence scope. No test-only replacement Agent or claim of semantic product quality; M3 or another actual Skill supplies its own real-path task Eval. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-03.M3 RequirementParse and shared Ensure

**Goal/value:** Provide reusable usable requirements without duplicate parsing or hidden dependency calls.

**Scope:** Exact complete Job input, bounded parsing/repair/validation, usable RequirementSets, compatibility/default activation, durable single-flight producer/waiter and owner-only cost; pure reads and explicit Application Ensure.

**Out of scope:** Fit judgments, mandatory career data, interactive conversation and deferred parser release certification.

**Required upstream capability:** [SL-08.M2](sl-08-collection-platform-safety.md#sl-08m2-boss-collection-and-explicit-refresh) — exact complete formal JobVersion; ManualApplicationEntry is not a producer

**Reused component/infrastructure:** [SL-03.M2](#sl-03m2-protected-semantic-invocation-and-evidence) — protected semantic invocation, budget and evidence infrastructure

**Required Contract portions before development:** `jobs/requirements.md` — Set/units, usable target, producer/waiter/reuse and activation; `jobs/jobs-screening.md` — exact complete Job input; `agent/tools.md` — pure read/dependency handoff; `foundation/budget.md` — parse owner and waiter accounting; `evaluation/evaluation-observability.md` — real parser tasks, real-JD/manual quality, task-scoped judges and actual-output checks. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Requirements owns dependency production; runtime executes and budget accounts. Empty unusable targets must fail honestly; valid unscored Fit results are a later distinct concept. Waiter cancellation cannot counterfeit producer cost or result.

**Research / unresolved Grill detail:** Verify the selected parser/provider against representative JD material. Q111/Q117/Q121/Q135 already require one extraction and at most one deterministic-validation-guided repair within total Run limits; continued invalidity fails closed. Contract Grill resolves concrete validation, error and invocation representations within that bound, not a new repair allowance.

**Tests / Eval:** V5.1, V8–10, V12–13: races, owner failure, cancellation/reuse, bounded repair, omitted/unsupported requirements, alternative valid output and incomplete evaluator evidence. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real Ensure produces or reuses a compatible validated usable Set, with honest failure/cost and deterministic plus semantic evidence. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Compatible validated Requirements are reusable without duplicate producer cost or invented downstream requirements. Crash/unknown/cancel paths neither replay unsafe calls nor lose local authority/evidence. The real task's deterministic and semantic checks execute with explicit limits; other Harness features are not declared complete merely because this path works. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 3 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover real RequirementParse → protected invocation → durable evidence/recovery and shared Ensure. Parent completion is separate from rollout/production enablement.
