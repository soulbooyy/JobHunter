# SL-07 Advisor discussion, exact Proposals and confirmed changes

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 3 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Turn conversational resume advice into trustworthy, explicitly confirmed formal changes without creating a second editing authority.

**Scope:** One durable Session model, bounded foreground Turns, general and Job-specific Advisor entry, lazy exact admitted reads, verifiable user statements, discussion/default/apply-target distinctions, Suggestions and concrete target-specific Proposals; ended generating Run and later Application confirmation, shared Save, narration/commit separation and deletion races. Include necessary interactive Context reduction/checkpoints, auxiliary limits and exact source retention. Add full Scenario/N+1 evaluation for these interactions.

**Out of Scope:** Either Fit as a prerequisite, Advisor ResumeDraft/export, inferred target or consent, continuing a Run through human confirmation, unrestricted chat search; persistent collaboration Memory itself is SL-12 and remains required v1 work.

**Already-decided capabilities and provenance:** Q24, Q41, Q47, Q52, Q85, Q88–Q89, Q93–Q94, Q128, Q132–Q144, Q146, Q148–Q149, Q155–Q159, Q166–Q167, Q178, Q180, Q183–Q185. Actual behavior/mechanism owners: [P6](../../spec.md#6-job-assistant-and-resume-advisor); [P9.3](../../spec.md#93-conversation-context-and-retention); [A7](../../architecture.md#7-session-advisor-proposal-and-confirmed-changes); [A9](../../architecture.md#9-shared-harness-skills-and-controlled-actions); [A10](../../architecture.md#10-context-engineering); [A12](../../architecture.md#12-durable-execution-and-recovery); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F05, F06, F08, F09, F10, F11.

**Test / Eval categories:** Lazy actual visibility, target/default and exact patch, one concrete confirmation, ended Run and free Session, dependency wait versus human wait, source spoofing and privacy, concurrent deletion/confirmation, saved result with failed narration, budgeted compaction/fencing, exact-one Proposal selection in real-path Scenarios. Required proof destinations: [V6](../../acceptance.md#6-advisor-proposal-confirmation-and-session); [V8](../../acceptance.md#8-harness-tools-and-actual-context); [V9](../../acceptance.md#9-budget-durable-execution-and-recovery); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 2.2](../../acceptance/evaluation.md#22-n1-and-complete-scenarios); [Eval acceptance 2.3](../../acceptance/evaluation.md#23-evaluator-inputs-authority-and-conclusions); [Eval acceptance 3](../../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-07.M1](#sl-07m1-durable-advisor-discussion), [SL-07.M2](#sl-07m2-job-targeted-discussion-and-dependency-waiting), [SL-07.M3](#sl-07m3-exact-proposals-and-confirmed-formal-changes). Dependencies are implemented components, not completion of upstream parents.

## SL-07.M1 Durable Advisor discussion

**Goal/value:** Discuss saved material and produce useful Suggestions through a durable conversation.

**Scope:** General Advisor entry, default/discussion selection, durable Session/Turns/provenance, foreground serialization, authorized reads, exact lazy pinning, required interactive reduction/checkpoints and bounded rescue, cancellation/deletion and honest narration.

**Out of scope:** Job requirement-specific mode is M2; formal Proposal/confirmation is M3; discussion is not an implicit write and Memory is later.

**Required upstream capability:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — saved formal Resume/default and authorized facts

**Reused component/infrastructure:** [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) — protected invocation, budget and evidence; interactive extensions are part of this milestone

**Required Contract portions before development:** `sessions.md` — general entry/source/Turn/foreground/deletion; `advisor-changes.md` — discussion and Suggestions; `tools.md` — permitted discussion reads; `context.md` — lazy acquisition, interactive capacity/reduction/checkpoint/rescue; `execution-runtime.md`, `budget.md`, `storage.md` — foreground/auxiliary/stream/retention extensions; `evaluation-observability.md` — fixed-input interactive Scenario/N+1, task-scoped checks and answer/control isolation. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Discussion selection differs from later actual apply target. Session source deletion, Context revocation and runtime cancellation agree now; later Proposal arbitration extends this interface before any Proposal consumer exists.

**Research / unresolved Grill detail:** Validate interactive Context/compaction and UI stream behavior under selected integrations; numerical triggers remain Grill work.

**Tests / Eval:** V6 discussion, V8–10, V12–13: real input/provenance, foreground races, source loss, stream interruption, bounded compaction/rescue and Scenario completeness. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real durable discussion yields Suggestions with exact input evidence and no factual mutation; Memory and formal changes are not claimed. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-07.M2 Job-targeted discussion and dependency waiting

**Goal/value:** Let the same Advisor discuss a Job using prepared usable requirements.

**Scope:** Job-side entry and target context in the unified Session model; pure requirement read and Application-controlled dependency wait/resumption.

**Out of scope:** Fit prerequisite, a second Assistant/Session type, human confirmation conflated with dependency waiting and hidden Tool parsing.

**Required upstream capability:** [SL-07.M1](#sl-07m1-durable-advisor-discussion) — durable Advisor conversation; [SL-03.M3](sl-03-invocation-requirements.md#sl-03m3-requirementparse-and-shared-ensure) — usable Requirements/Ensure when the targeted task requires them

**Reused component/infrastructure:** [SL-07.M1](#sl-07m1-durable-advisor-discussion) — Session/foreground/Context machinery

**Required Contract portions before development:** `sessions.md` — Job entry and dependency waiting; `advisor-changes.md` — targeted discussion scope; `requirements.md` and `tools.md` — explicit Ensure/pure reads; `context.md` — exact acquired Job/Set; `evaluation-observability.md` — targeted multi-step Scenario. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Keep the producer/waiter and foreground boundaries distinct from ended-Run human confirmation. No completed Fit is necessary.

**Research / unresolved Grill detail:** Resolve exact resume/cancel/source-change behavior at the dependency boundary without inventing a new generic workflow.

**Tests / Eval:** V5.1, V6, V8, V12–13: missing dependencies, concurrent Ensure, wait/resume/cancel, exact target changes and no hidden model call in a read. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** The actual targeted conversation uses compatible requirements and preserves one Session/foreground authority. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-07.M3 Exact Proposals and confirmed formal changes

**Goal/value:** Turn reviewed Advisor suggestions into explicitly authorized formal changes.

**Scope:** Actual apply target, noneditable exact Proposal, replacement/idempotency, complete confirmation after generating Run ends, Application-side shared Save, durable result independent of narration and Session-delete arbitration.

**Out of scope:** Unconfirmed writes, Advisor working drafts/source selection, Preparation adoption and a required Job-specific discussion.

**Required upstream capability:** [SL-07.M1](#sl-07m1-durable-advisor-discussion) — discussion/Suggestion and valid Session; [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — formal target preparation and full Save capability

**Reused component/infrastructure:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — all-affected transaction, intent and idempotent result protocol

**Required Contract portions before development:** `advisor-changes.md` — actual target, Proposal eligibility/confirmation/replacement/result and confirm-delete arbitration; `sessions.md` — source existence/deletion interface; `candidate-save.md` — confirmed entry/committed result; `resumes-grounding.md` — target/support preparation; `tools.md` — authorized actions; `evaluation-observability.md` — confirmed-mutation Scenarios. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Resolve both sides of Proposal/Session and Proposal/Save together. Shared all-affected authority/intent never waits for narration; losing delete/confirmation races cannot mutate.

**Research / unresolved Grill detail:** Resolve precise concurrency/confirmation interface in Contract Grill while preserving the ended generating Run and complete consent boundaries.

**Tests / Eval:** V4.1, V6, V9–10, V12–13: exact replacement/duplicate confirmation, source deletion races, conflict/rollback and narration loss after commit. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real confirmed Proposal commits through the complete existing Save exactly within authorization, with durable explainable result. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Advice and an exact confirmed change work through the real Application/Save boundary, with honest independent commit/presentation outcomes and full boundary evidence. Any pre-SL-12 delivery is explicitly partial against full v1 Memory capability, not a change to v1 scope or default enablement. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 3 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover general/Job-targeted discussion, dependency wait, exact Proposal and confirmation/delete arbitration. Parent completion is separate from rollout/production enablement.
