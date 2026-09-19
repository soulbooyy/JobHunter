# SL-12 Collaboration Memory with independent controls and forgetting

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Carry permitted collaboration preferences between conversations while keeping saved career facts, consent and task evidence under their existing owners.

**Scope:** Admitted user-sourced collaboration Memory, independent background MemoryExtraction, durable ranges/coalescing and isolated failed/unknown ranges; Auto Learning/Recall/manual management, allowed summaries/lookups, source/entry deletion and non-resurrection; independent background budgets/capacity and controlled Memory Eval. Recheck Session deletion, checkpoint source exclusion and current Recall admission.

**Out of Scope:** Career USER_FACT store, unrestricted chat search, automatic historical backfill, complex Memory graphs/vector consolidation, General Assistant/interview Skills, Candidate Evidence RAG and erasure of indirect influence from real past assistant messages.

**Already-decided capabilities and provenance:** Q127–Q133, Q135–Q139, Q145, Q155, Q167, Q169–Q170, Q172, Q187. Actual behavior/mechanism owners: [P10](../../spec.md#10-collaboration-memory); [A10](../../architecture.md#10-context-engineering); [A14](../../architecture.md#14-collaboration-memory); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F03, F04, F08, F09, F10, F11.

**Test / Eval categories:** Three independent controls, Skill allowlists and no Fit/parse Memory exposure, checkpoint exclusion/current Recall, failed-range isolation, deleted Session publication ban, manual edits beating older extraction, forgetting without resurrection, startup/unknown extraction and background capacity, comparable frozen-Memory versus explicit-learning Scenarios. Required proof destinations: [V8.2](../../acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9](../../acceptance.md#9-budget-durable-execution-and-recovery); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [V11](../../acceptance.md#11-collaboration-memory); [Eval acceptance 2.1](../../acceptance/evaluation.md#21-isolation-exact-inputs-and-declared-experiment-scope); [Eval acceptance 2.2](../../acceptance/evaluation.md#22-n1-and-complete-scenarios); [Eval acceptance 3](../../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-12.M1](#sl-12m1-manual-collaboration-memory-and-controlled-recall), [SL-12.M2](#sl-12m2-independent-background-collaboration-learning). Dependencies are implemented components, not completion of upstream parents.

## SL-12.M1 Manual collaboration Memory and controlled Recall

**Goal/value:** Reuse user-managed collaboration preferences without giving them career-fact or command authority.

**Scope:** Manual create/edit/delete/forget, supported sources and authority rules, independent control meanings, permitted summary/lookup and per-Frame Recall, checkpoint exclusion and no resurrection from older content.

**Out of scope:** Background extraction delivery is M2; career-fact storage, arbitrary Skill access and treating Memory as consent.

**Required upstream capability:** [SL-07.M1](sl-07-advisor.md#sl-07m1-durable-advisor-discussion) — valid eligible Session sources and discussion integration

**Reused component/infrastructure:** [SL-07.M1](sl-07-advisor.md#sl-07m1-durable-advisor-discussion) — exact Context/checkpoint and source-validity infrastructure

**Required Contract portions before development:** `agent/memory.md` — entry/source/management/Recall/control meanings, conflicts/forgetting; `agent/sessions.md` — actual source validity; `agent/context.md` — current per-Frame Recall/checkpoint exclusion; `agent/tools.md` — permitted lookups if exposed; `foundation/storage.md` — forgetting/retention agreement; `evaluation/evaluation-observability.md` — controlled Memory snapshots and Recall evidence. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Agree manual edits/forgetting versus later extraction publication before learning is enabled. Turning learning off must not disable manual management or Recall; do not display nonexistent learning execution as delivered. No Fit/parser Memory exposure.

**Research / unresolved Grill detail:** Resolve control and source/permission/forgetting expressions in Grill; defaults, ranges and retrieval policy are not chosen here.

**Tests / Eval:** V8.2, V10–11, V12–13: independent controls, exact Frame, permitted Skills, current Recall after checkpoint, deleted sources, edits/forgetting and frozen-Memory evaluation. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Actual manual management and permitted Recall work with evidence, independently of automatic learning. Parent SL-12 remains incomplete. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-12.M2 Independent background collaboration learning

**Goal/value:** Learn eligible collaboration information without delaying or corrupting foreground work.

**Scope:** Completed eligible Session source ranges, separate background owner/capacity and bounded extraction, isolated failed ranges, deletion/publication arbitration, newer manual changes winning and learning-specific evidence.

**Out of scope:** Proposal/apply success prerequisite, career-fact writes, foreground rollback, silent failed-range concatenation and resurrection.

**Required upstream capability:** [SL-12.M1](#sl-12m1-manual-collaboration-memory-and-controlled-recall) — managed collaboration entries, controls and current Recall; [SL-07.M1](sl-07-advisor.md#sl-07m1-durable-advisor-discussion) — eligible completed Session source ranges

**Reused component/infrastructure:** [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) — bounded invocation/recovery/evidence; background budget and source-publication extensions are part of this milestone

**Required Contract portions before development:** `agent/memory.md` — learning/extraction/source ranges/publication/conflicts; `agent/sessions.md` — completed source and deletion agreement; `agent/execution-runtime.md`, `foundation/budget.md`, `foundation/storage.md` — independent background resources/recovery/retention; `agent/context.md` — extraction input/Recall separation; `evaluation/evaluation-observability.md` — explicit learning Scenarios, measured background evidence and controlled Memory. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Complete source deletion and newer manual edit/forgetting checks at publication; background failure must not undo foreground success. Eligible discussion is sufficient upstream; no Proposal milestone is required.

**Research / unresolved Grill detail:** Resolve source boundaries, extraction policy and background budget/unknown handling in Grill; verify actual provider behavior without changing foreground defaults.

**Tests / Eval:** V9–13: failed/unknown range, startup/cancel, independent headroom, source deletion race, old candidate versus new manual edit, forgetting and explicit learning-on versus frozen-Memory experiments. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real independent learning publishes only eligible current collaboration entries with separately attributable evidence and no foreground authority change. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Permitted collaboration reuse and management work without changing business facts or consent. Background failures do not roll back foreground success or silently rejoin later ranges. Actual learning evidence is separate from learning-disabled Advisor trials. This is required v1 scope, not a post-v1 deferral. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover independent learning/Recall/management, eligible sources, current Context and non-resurrecting forgetting. Parent completion is separate from rollout/production enablement.
