# Harness Budget — Detailed Architectural Design Record

## Status, scope, and authority

- Primary accepted decisions: Q124, extended by Q130's scope/ownership and Q132's auxiliary
  Invocation accounting and Q135/Q140's unified invocation limits, plus Q142/Q144 parse ownership; supporting boundaries include Q35, Q40, Q80, Q110-Q112, Q120-Q125, Q127.
- Last updated: 2026-09-18.
- This file preserves the complete architectural budget design. It is a design-stage record,
  not an implementation report, billing platform, or replacement for formal project documents.
- Conceptual names and formulas state invariants. Exact schema, currency values, token thresholds,
  pricing sources, allocations, and status enums belong to the later field-level Contract Grill.
- Related: [Recovery](recovery.md), [Memory](memory.md),
  [Context Engineering](context.md), [Storage](storage.md),
  [Decision Register](../grill-me-design-tree.md).

## 1. One Budget Runtime, multiple owners

Q130 extends Q124 without replacing its reservation/settlement mechanism:

```text
shared Harness Budget Runtime
             |
conceptual Workspace / Usage Envelope
             |
    +--------+--------------------------+
    |                                   |
Foreground Budget Scope          Background Budget Scope
    |                                   |
user-triggered operation         BackgroundMemoryBudget
    |                                   |
AgentRun local budget/limits      MemoryExtraction Run limits
    |                                   |
    +---------------+-------------------+
                    |
        shared Invocation Runtime
        check / atomic reserve / dispatch
        settle / preserve unknown usage
```

ExecutionBudget means the resource envelope for an explicit execution scope, not one global wallet
for the entire Harness. The Workspace/usage-envelope level expresses overall capacity context, not
a new multi-tenant account, mandatory billing platform, or finalized schema.

Three layers remain distinct:

- Budget Scope identifies which work owns the allowance.
- AgentRun Budget/local limits bound this execution's consumption and steps.
- Invocation Reservation decides whether the next real dispatch may consume capacity.

Application owns foreground operation scopes. Background Memory maintenance has its own owner.
All reuse the same budget/runtime/recovery infrastructure; no Skill implements a private accounting
system. Provider/Tool usage remains measured, estimated, or unknown as appropriate.

## 2. Foreground operation scopes and DeepFit's shared budget

One user batch DeepFit operation accounts for actual work performed for that operation:

- RequirementParse when a compatible RequirementSet is not already reusable;
- CandidateJobFit;
- ResumeJobFit;
- each permitted repair;
- future Retrieval Mode Model/Tool Invocations, once that deferred mode is implemented.

A compatible exact RequirementSet can serve both Fits without charging the parsing cost twice.
Reusing an existing durable Set does not invent a new Invocation or usage event.

Candidate Fit and Resume Fit still have independent results and failure boundaries. Sharing a
budget does not merge their semantic tasks, Context, AgentRuns, or business transaction boundaries.

This decision does not introduce a separate parser fee, budget per saved Job, or a new analysis
object. The unit of accounting is work that actually invoked a charged or limited capability.

A ResumeAdvisor Turn has its own foreground operation envelope; a background extraction combining
several completed Turns cannot be charged to whichever Turn happened last. Future MockInterview or
other user operations illustrate the same ownership rule, not an expansion of current v1 scope.

Compaction that exists only to continue a current foreground Run is different: Q132 makes it an
auxiliary Invocation inside that Run, charged to that Run's current operation envelope.

### One parse producer, many waiters (Q142)

EnsureRequirementSet coordinates the same exact JobVersion + parser/schema/prompt/policy
compatibility target with a database-backed atomic claim / unique active-target constraint / CAS.
At most one valid RequirementParse AgentRun produces that target at a time, even across processes.
A process-local mutex/singleflight helper is only an optimization, never the correctness boundary.

The operation whose atomic claim creates the producer owns its ExecutionBudget and pays the actual
parse and any admitted repair. Concurrent Candidate Fit, Resume Fit, or other authorized workflows
wait for the same immutable result; they do not reserve or charge duplicate parse calls.

A waiter's cancellation removes only its wait. Producer-owner cancellation, parse failure, or
OUTCOME_UNKNOWN yields dependency-unavailable to waiters; do not transfer the Run/budget, elect an
automatic substitute, or silently reparse. Explicit user Retry calls EnsureRequirementSet again:
reuse a compatible durable Set if present, otherwise compete for a new owner. Unknown old invocation
usage remains conservatively accounted to its original owner, not reset or charged to a waiter.

This is Application dependency coordination, not multiple Jobs in one AgentRun or a cross-operation
transaction boundary.

Q144 applies the same owner-only accounting when Advisor's job.requirements.read reports a missing
Set. The read itself neither calls a model nor creates an asset. Application's EnsureRequirementSet
starts a distinct Parse Run only if needed; it is charged to its actual operation owner, including
repair, rather than hidden in Tool read cost. Waiters reuse success and never pay duplicate parsing.

## 3. Local limits remain mandatory

A shared balance is not permission for one AgentRun to consume arbitrarily much work.

Each Skill may constrain:

- model calls;
- Tool calls;
- AgentLoop steps;
- input/output or total token consumption;
- deadline and elapsed execution;
- applicable runtime/background concurrency constraints;
- permitted repair count.

The exact numerical values and complete attribute list are not frozen here. Existing accepted
v1 limits do apply: RequirementParse and Full-Context Fits permit one primary evaluation and at
most one deterministic-validation-guided repair; Fit Full Context does not expose autonomous
Evidence Tools.

A Run must satisfy its local limits, its explicit owner scope's remaining budget, and runtime
capacity admission. Cheap calls are not permission for unlimited work. Money, token consumption,
model/Tool invocation counts, steps, deadlines, and concurrency are distinct constrained resources.

### Kind-local allowance and whole-Run ceilings (Q135)

All business Provider calls enter ModelInvocationRuntime, including primary evaluation, validation
repair, semantic compaction, reactive retry, and independent MemoryExtraction calls. Conceptual
invocation_kind values distinguish their purpose; no helper path bypasses counting or charging.
Q176 places LLM judges outside this business execution boundary: their separate Eval accounting
must not charge a business AgentRun or appear in its invocation/token/cost totals.

The accepted local ceilings are at most one Skill validation repair, at most one semantic compaction
per AgentRun, and at most one reactive rescue retry per AgentRun. Later AgentLoop steps do not renew
allowances. These caps are not extra credit above a Run total: every call consumes total invocation,
input/output token, cost/reservation, deadline, and applicable step limits. Both the kind-local
allowance and the Run total must admit dispatch. The concrete total values remain deferred.

Deterministic context reductions incur no model invocation but still obey execution bounds. An
explicit Provider size rejection alone qualifies for reactive rescue; timeout, disconnect, and
OUTCOME_UNKNOWN never do. An oversized protected Full Context input fails without semantic
summarization of authority.

## 4. Atomic dispatch admission

ModelInvocationRuntime is the sole execution boundary for Provider requests. It uses this shared
Budget Runtime and then ModelGateway for transport adaptation. ToolInvocationRuntime applies
corresponding admission to Tool actions; separate Runtime responsibilities do not create separate
unaccounted budget systems.

Before each charged or rate/resource-limited Invocation:

1. establish current execution authority, applicable Skill policy, and frozen input;
2. satisfy Provider/runtime capacity admission; background work additionally yields to foreground
   demand under the headroom gate described below;
3. calculate required_reservation using the selected model, input size, output allowance,
   and applicable operational policy;
4. atomically check the correct budget owner scope, Run-total limits, and applicable kind-local
   allowance/eligibility, then reserve; concurrent paths cannot spend the same balance or allowance;
5. only an admitted Invocation may proceed through durable dispatch intent to remote execution.

The budget operation uses a short local transaction/CAS. Do not hold a database transaction open
while waiting for network completion.

Conceptually:

```text
available_budget
  = total_budget
  - settled_usage
  - outstanding_reservations

admit only if required_reservation fits available_budget
and local execution limits still permit the Invocation
```

The formula describes one consistent accounting unit. It is not a final schema, exchange-rate rule,
or claim that a monetary estimate is a Provider-guaranteed billing cap.

### Concurrent admission example

Available balance: $0.10. Run A and Run B each require $0.08.

- One atomic check/reserve succeeds.
- The remaining available balance becomes $0.02.
- The other request cannot reserve $0.08 and must not dispatch.
- Both reading $0.10 before separate non-atomic writes is prohibited.

The dollar values illustrate concurrency only; they are not product defaults.

Q140 forbids transparent Gateway/SDK resends and automatic Provider/model fallback. Any permitted
real resend must reenter ModelInvocationRuntime counting, allowance, reservation, durable dispatch,
and audit. Known pre-send local preparation recovery is distinct from an ambiguous remote call.
User-selected alternative configurations use a new Run; existing failure/cost history remains.

## 5. Reservation and durable dispatch integration

[Recovery](recovery.md) requires write-ahead dispatch intent before the remote call.

Budget reservation and dispatch intent must both be durable before the relevant external work.
Every reservation belongs to the explicit foreground/background scope responsible for the Invocation.
Exact transaction composition will be defined later, but recovery must distinguish:

- safely undispatched work;
- dispatch-intent work whose remote outcome is unknown;
- completed work with durable response and known or unknown usage.

A process restart does not reconstruct a fresh unused budget while ignoring earlier reservations.
Retry does not bypass either the shared check or the per-Run limits.

Concrete idempotent reservation and settlement mechanics are field-contract work; the invariant is
that duplicate local processing must not reserve or settle the same Invocation twice.

## 6. Settlement

Once actual usage is available, settle that Invocation against its reservation.

| Outcome | Budget treatment |
| --- | --- |
| Actual cost below reservation | Settle actual cost and release the difference |
| Actual cost equals reservation | Settle the reserved amount |
| Actual cost above reservation | Record real usage and apply the overrun policy; never falsify usage |
| Dispatched but result/usage unknown | Preserve unknown status and conservative outstanding exposure |
| Proven not dispatched | No remote usage may be invented; reservation release follows the safe-boundary policy |

Repair is a new real Invocation. It must reserve again, satisfy remaining local limits, and be
settled as actual work. Validation failure does not make a successfully executed model call free.

The handling of actual cost above reservation is deliberately not finalized. Required later policy
includes how overrun affects remaining dispatch, user reporting, and estimation adjustment.
The current design prevents known balance oversubscription at admission; it does not promise that
all Provider bills must exactly equal estimates.

## 7. Unknown usage and retry

After dispatch intent, timeout/crash without a durable response creates OUTCOME_UNKNOWN under Q122.

Required behavior:

- do not record usage as zero;
- do not immediately release the entire reservation as if no call occurred;
- preserve unknown/conservative exposure in budget state;
- end the old effective Run and release its concurrency slot as appropriate;
- require explicit Retry into a new Run;
- perform fresh budget admission for that Retry.

Releasing a target slot permits another authorized local execution attempt. It does not erase the
old remote call's possible cost.

The mechanism for later reconciling unknown cost with Provider evidence, and whether/when to expire
a conservative hold, must be specified later. No automatic timeout-to-zero policy is assumed.

## 8. Budget exhaustion and partial success

Insufficient budget stops work that has not yet dispatched. It does not roll back already durable:

- RequirementSets;
- CandidateJobFitAnalysis;
- ResumeJobFitAnalysis;
- other independently completed results.

A budget-exhausted task is not evidence that the Candidate failed to match a Job and must not
produce MISSING or a zero score.

Batch presentation should distinguish completed work from work not run because of budget.
Exact status labels and UI layout remain later design choices.

Cancellation likewise does not make outstanding dispatched work cost-free. Remote work may still
finish after local fencing prevents canonical publication.

## 9. Context capacity is a separate boundary

A task can have spending budget but still not fit the model Context limit.

Q123's v1 Full-Context rule:

- check actual serialized inputs plus system/instruction overhead, output allowance, and safety margin;
- if the task cannot fit, stop before the model call with a clear capacity explanation;
- do not silently drop Evidence and claim FULL_CONTEXT;
- do not fabricate a formal score or MISSING from uninspected inputs;
- do not silently change model/Provider or enable an unimplemented retrieval fallback;
- one over-budget Candidate task does not prevent a fitting independent Resume task;
- where an already supported larger-context configuration exists, the user may explicitly select
  it and retry;
- do not require deleting genuine career facts merely to satisfy an implementation limit.

Resume inputs are usually small but still require the same real capacity check. Q132 may compact
transient history before Frame assembly, but may not summarize the required exact Resume/Evidence/
RequirementSet to make a protected-input overflow disappear. Candidate Agentic RAG remains a
post-v1 extension. A typed Provider Context-size rejection permits only Q132's bounded, budgeted
reactive rescue; an unknown remote outcome never qualifies for that exception.

## 10. Background Memory ownership and foreground-priority capacity

### Separate owners, shared mechanisms

MemoryExtraction is independent background work. Its merged source range can cover several Turns
and AgentRuns, so it charges BackgroundMemoryBudget, never an arbitrary foreground Turn's completed
ExecutionBudget. It still has per-Run bounds and uses the same atomic reservation, settlement,
unknown-usage, Provider admission, and audit mechanisms.

Example:

```text
BackgroundMemoryBudget available = $0.10

Run A needs $0.06 -> reserve succeeds -> $0.04 remains
Run B needs $0.06 -> insufficient -> no dispatch
```

The amounts are examples only. Run B may stay pending for later scheduling or be recorded as not
executed for budget reasons under later policy; v1 does not require a complex queue platform.

If A reserved $0.06 and actually used $0.04, settlement releases $0.02. If it becomes OUTCOME_UNKNOWN
after dispatch intent, preserve unknown/conservative exposure exactly as for foreground work.
Pending extraction does not authorize silently retrying a possibly executed remote call.

### Provider headroom is not budget

Before background dispatch, require:

```text
BackgroundMemoryBudget sufficient
           |
Provider headroom sufficient
           |
foreground capacity protected
           |
runtime concurrency available
           |
atomic budget reservation
           |
dispatch
```

Foreground user work has priority over background Memory maintenance. Provider rate-limit pressure,
runtime contention, or tight overall usage capacity can postpone extraction even when its monetary
budget is sufficient.

Budget answers “how much may be spent”; capacity/headroom answers “is now an appropriate time.”
Both must permit dispatch. Concrete percentages, queueing/fairness, and scheduling mechanisms are
not frozen, and there is no blanket permission to cancel already dispatched work to reclaim money.

### Current-Run Context Compaction is not background Memory

Q132's semantic checkpoint invocation belongs to the Run it helps continue. It shares that Run's
ExecutionBudget, generation, deadline, local limits, audit, and recovery. It does not charge
BackgroundMemoryBudget and does not create an independent MemoryExtraction Run.

Each semantic compaction and reactive retry is real work requiring admission/reservation/settlement.
Insufficient budget never licenses a hidden helper model call. Reuse sufficient deterministic
compaction if possible; otherwise stop with an explicit Context/budget failure.

### Scope does not grant capability

Fit and Tool permissions remain separate. Budget cannot authorize writes, grow an allowlist, or
bypass admission. Future Candidate Retrieval Invocations follow the same operation budget once that
deferred capability exists; documenting Memory lookup and compaction does not implement it.

Q135's once-per-Run semantic compaction and reactive retry allowances do not reset in another loop
step. They share the total Run envelope; unused local allowance does not imply available total
budget. All such calls use ModelInvocationRuntime, not an unobserved auxiliary ModelGateway call.

Automatic Memory work requires Auto Learning, independently of Recall. Manual Memory management
does not require an extraction model call. Interactive LAZY_TOOL reads still obey applicable
Tool/step/context limits; choosing a lazy acquisition mode does not grant unbudgeted nested model
calls. EAGER_EXACT Fit retains the protected-input capacity check.

### Foreground Session serialization does not merge budget ownership (Q155)

One active foreground Turn per ChatSession does not forbid concurrent different Sessions or permitted
independent dependency/auxiliary/background Runs. This scheduling constraint does not replace operation
budgets, Run limits, or atomic Invocation reservations. Waiting input is not permission to dispatch
against another Turn's budget. Background Memory and parse-owner accounting retain their own owners.

### Waits, confirmation, and platform capacity (Q158-Q160)

Pending Proposal is Application state after its generating Turn ends, not a reason to hold model
capacity or a running budget. Confirmation needs no model reinterpretation; subsequent narrative,
if requested, uses new bounded execution. Advisor dependency wait remains within its overall
deadline but holds no model/Provider invocation slot or repeated polling calls. Actual parse/repair
cost retains Q142's owner; waiting does not merge budgets or reset limits.

PlatformAccessSafety shares recruiting capacity/risk by (platform, account) across Collector/
Executor/future Monitor, separate from monetary/token budget ownership and model Provider admission.
Capacity can recover by policy, but strong risk requires explicit user restoration. No numeric quota
or mandatory Monitor implementation is established here.

### Failed Memory ranges and permission/source revocation (Q169-Q172)

Only explicit Retry reprocesses failed/unknown extraction source ranges, with fresh Run budget
admission; later independent ranges may proceed without inheriting old failed work. Undispatched
capacity/budget waiting remains pending. Deleting a source Session or revoking task input permission
does not prove an already-dispatched request stopped or cost zero. Preserve uncertainty/reservations
under existing settlement rules; do not spend more to silently repair/replay revoked work.

## 11. Privacy and audit

Store only the necessary accounting facts in lightweight audit metadata: identities/references,
policy/model lineage, reservation/settlement state, known or unknown usage, and timing/outcome.

Sensitive prompt, Resume, Evidence, Tool payload, or complete response content is not needed in an
ordinary budget log. Protected recovery payloads have their own retention lifecycle under Q125;
see [storage.md](storage.md).

Exact field names, amount precision, pricing versions, settlement representations, and certainty
enums are deferred. Audit must nonetheless preserve the distinction between measured, estimated,
and unknown costs rather than report a fabricated precise number.

## 12. v1 boundaries and deferred detail

In scope now:

- explicitly owned foreground/background scopes on a shared Budget Runtime;
- operation-owned shared DeepFit budget;
- Skill/Run local limits;
- atomic Invocation check and reservation;
- settlement of actual usage;
- conservative unknown-cost handling;
- preservation of successful partial results;
- no silent model/Provider fallback for Context capacity;
- foreground-priority background headroom/capacity admission;
- same-Run auxiliary compaction budget accounting.

Not introduced now:

- fixed dollar/token defaults or allocation percentages;
- a general billing product;
- customer accounts, payment processing, or multi-tenancy;
- a forecasting or pricing-optimization platform;
- free automatic retries of unknown calls;
- Agentic RAG implementation.

Later detailed Contract work must settle:

- precise accounting units and pricing sources;
- reservation estimation and overrun policy;
- atomicity/idempotency of reservation and settlement;
- recovery of pre-dispatch reservations;
- reconciliation of unknown usage;
- concrete per-Skill limits and user-facing reporting;
- concrete BackgroundMemoryBudget amounts and scheduling/headroom thresholds;
- concrete total per-Run ceilings and accounting representation for invocation kinds; Q135 already
  fixes once-per-Run semantic compaction and reactive retry, alongside the once-per-Skill repair rule.

## 13. Verification implications and formal writeback

Derived scenarios for later tests:

- Two concurrent $0.08 requests cannot both pass a $0.10 balance.
- Reusing a RequirementSet does not create duplicate parse charges.
- Repair cannot dispatch without another admission.
- A restart preserves outstanding reservations.
- An unknown old call is not reset to zero before Retry.
- Failing or exhausting one task preserves independent successful analyses.
- Budget exhaustion creates no business fit judgment.
- Insufficient Context capacity fails before invocation without silent trimming.
- Settling the same Invocation again does not duplicate usage.
- Two $0.06 background reservations cannot both pass a $0.10 remaining scope.
- A multi-Turn extraction does not debit the last foreground Turn's envelope.
- Background work waits for headroom even with sufficient budget.
- Same-Run compaction charges that Run's scope and cannot bypass its limits.

These are architectural consequences, not a claim of completed tests. Freeze stable ownership and
invariants in architecture/contracts, verification in acceptance/development, and implementation
progress only in progress documents.

Additional cases: unused repair allowance with exhausted Run totals cannot dispatch; two later loop
steps cannot each claim a semantic-compaction allowance; reactive rescue cannot reclassify an unknown
call; all auxiliary Provider paths reserve and settle through ModelInvocationRuntime.

Q140/Q142 require adapter retry to produce no hidden Provider request, database-backed parse
claims to prevent duplicate producers, waiter reuse to incur no duplicate parse charge, and owner
failure/unknown outcome to stop waiters without transferring budget or automatically reparsing.

Related Tool naming, action purity, typed source validation, and dependency signaling are defined
in [Tool Actions](tool.md). Architectural objects/properties are collected for later design in
[Contract Design Inventory](../contract/contract-design-inventory.md); neither document finalizes
field schemas or reports implementation.
