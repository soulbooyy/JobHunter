# SL-07 Durable optimization conversations

> Revised by accepted CG03S1-Q26 at **2026-09-24.S2M1S1-r1**. Planning is not implemented capability or whole-file Contract readiness. Earlier source-model/allocation descriptions are superseded.

[Global rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) · [Decisions](../../design/contract/sl-02-m1-supplement-grill.md) · [Progress](../../progress.md)

Ordinary and Job-targeted conversations reuse SL-06 suggestion capabilities with strict selected-Resume candidate context. Current scope has no assistant write application.

<a id="sl-07m1-durable-advisor-discussion"></a>
## SL-07.M1 Durable Advisor discussion

**Scope:** One durable Session/Turn model, explicit selected Resume, ordinary discussion and reuse of SL-06.M1 suggestions. Preserve actual inputs, bounded execution, completed suggestions versus temporary streams, privacy/revocation/deletion and conversation Context maintenance. Career assertions in history/summaries/Memory cannot supplement selected Resume.

**Upstream/reuse:** Actual SL-06.M1 and SL-03.M2 protected invocation, applicable runtime/Context/storage. No DeepFit, Job or ready global portrait prerequisite. Collaboration Memory arrives through its separate SL-12 interface, never career facts.

**Required Contracts/blockers:** RES-024/CTX-016/EVO-027 source boundary is reviewed; planned sessions and advisor-changes discussion/result scopes and interactive Context/Budget/Runtime need actual consumer definitions. This is first backend/frontend implementation, not adaptation of an existing chat engine.

**Concurrency:** At most one foreground Turn per Session; new input waits or follows explicit stop. Separate Sessions may progress. Pin the task’s exact selected Resume.

**Proof/completion:** Durable ordinary interaction, useful source-bound suggestions, actual Frame isolation, uncertainty/cost, deletion/revocation and bounded Context behavior. No implicit target switch, Save or assistant apply. Frontend clearly identifies selected Resume and empty-input message.

**Development entry:** [SL-07.M1 handoff](../../development/handoff/sl-07-m1-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

<a id="sl-07m2-job-targeted-discussion-and-dependency-waiting"></a>
## SL-07.M2 Job-targeted discussion and dependency waiting

**Scope:** Same Session model and SL-06.M2 targeted suggestion reuse with exact selected Resume/Job. Explicit requirements dependency waiting is distinct from model progress or hypothetical human confirmation.

**Upstream:** Actual SL-07.M1, SL-06.M2 and its Requirements/formal-Job producer. No completed DeepFit prerequisite.

**Required scope/blockers:** Source isolation remains RES-024/CTX-016; future sessions/advisor-changes targeted-entry and requirements producer/waiter agreements remain pending. First backend/frontend implementation.

**Wait boundary:** RequirementParse waiting retains the active foreground Turn, releases Provider capacity and obeys original deadline/cancellation; no model polling, hidden inline parsing or producer takeover.

**Proof/completion:** Exact target and source, dependency unavailable/failure/changed input, truthful wait/cost, no hidden Tool parsing or other-Resume augmentation, same durable result and no writes. Reuse the optimizer, not duplicate it in Advisor.

**Development entry:** [SL-07.M2 handoff](../../development/handoff/sl-07-m2-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

<a id="sl-07m3-exact-proposals-and-confirmed-formal-changes"></a>
## SL-07.M3 Assistant application — deferred

**Status:** Explicitly deferred by CG03S1-Q14/Q26. No current backend/frontend implementation or current parent completion gate. Historical exact Proposal/confirmation design is context, not a published new-model protocol.

**Future prerequisite:** A separately approved consumed advisor-changes/Session/Save application agreement, exact target authorization, revisions/idempotency/delete arbitration and real earlier suggestion capability. If implemented later, application advances the same Resume and ordinary default-rebuild consequences, never another document or independently editable Knowledge.

**Current transfer:** Remove apply controls/automatic Save from current delivery criteria. Preserve source/consent/history invariants; do not implement an old Knowledge correction flow. No acceptance claim or hidden automatic mutation.

**Development entry:** [SL-07.M3 handoff](../../development/handoff/sl-07-m3-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

**Parent completion:** Current required milestones are M1/M2 with integrated conversation proof. M3 remains explicitly Deferred and must be shown separately; current completion does not claim assistant application. Collaboration Memory remains separately planned SL-12 work.
