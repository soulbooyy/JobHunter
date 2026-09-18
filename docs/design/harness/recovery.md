# Harness Recovery — Detailed Architectural Design Record

## Status, scope, and authority

- Primary accepted decision: Q122; supporting boundaries: Q30-Q31, Q40, Q47, Q83, Q94,
  Q116, Q120, Q124-Q125, Q130, and Q132-Q172.
- Last updated: 2026-09-18.
- This is the full design-stage record for recovery, not an implementation report or a new
  authoritative document category. Formal architecture/contracts/acceptance remain the eventual
  destinations for normative rules.
- Object/attribute examples and state labels express semantics, not finalized schemas or an
  exhaustive transition table. Detailed field design belongs to the later Grill.
- Related records: [Budget](budget.md), [Memory](memory.md), [Context](context.md),
  [Storage](storage.md),
  [Decision Register](../grill-me-design-tree.md).

## 1. Four principles

Recovery is common Harness Runtime capability, not a special Fit implementation:

1. **Durable boundary:** continue only from reliably persisted progress.
2. **Execution ownership:** one currently authorized execution owner controls a Run.
3. **Replay safety:** a workflow checkpoint alone never proves a remote action can be repeated.
4. **Execution fencing:** revoked, timed-out, or replaced owners cannot publish results.

The goal is not to resume from an arbitrary code line, nor to guarantee exactly-once remote execution.
The goal is to make uncertainty explicit, avoid silent duplicate remote work, and preserve exact
input/response lineage.

## 2. Ownership boundaries

| Concern | Owner |
| --- | --- |
| Business workflow, frozen inputs, canonical validation/persistence | Application |
| Bounded Run lifecycle, ownership, cancellation, generation | AgentRunRuntime |
| Every real model call: admission/counting/reservation, dispatch intent, fencing, durable response, usage, timeout/cancel/recovery/audit | ModelInvocationRuntime |
| Provider/model abstraction and request/response adaptation | ModelGateway |
| ToolCall admission, replay semantics, and side-effect boundary | ToolInvocationRuntime |
| Workflow/checkpoint state | LangGraph, where used |
| External application authority and verified business events | Application workflow and Browser Executor policies |

Q135 establishes one model execution path:

```text
Skill / AgentRun
       |
ModelInvocationRuntime
       |
ModelGateway
       |
Provider
```

Primary tasks, RequirementParse, Candidate/Resume Fit, validation repair, semantic compaction,
reactive retry, and MemoryExtraction all use it. There is no unobserved "internal model" exception.
The Invocation Runtime uses shared Budget/Storage/Context capabilities; this naming does not imply
separate deployed services or new business authorities.

LangGraph may reconstruct workflow state. It must not replay a model request or browser effect merely
because a graph node was not checkpointed as complete. ModelGateway adaptation likewise does not
own permission to evade invocation accounting or recovery.

Harness does not gain Evidence/Resume/application write authority by owning execution. Business
writes still go through controlled Application commands and canonical results need Domain validation.

### Gateway retry and fallback boundary (Q140)

ModelGateway and underlying Provider SDKs do not own transparent retry, fallback, or model switching.
One Runtime-admitted request cannot secretly fan out into multiple Provider requests. Any permitted
resend is another fully counted/admitted/audited Invocation through ModelInvocationRuntime.

Only accepted bounded validation repair and explicit Context-size rescue use their respective
rules. Timeout, disconnected response, and ambiguous remote execution retain OUTCOME_UNKNOWN and
explicit new-Run Retry; a transport adapter cannot reinterpret them as safely unexecuted.
v1 has no automatic Provider/model fallback. Explicit user selection of a different supported
configuration creates a new Run, retaining earlier outcome and usage lineage. Known local work
that has not crossed dispatch may safely continue under Q122.

### Typed Tool scope and conversational sources (Q138/Q139)

ToolInvocationRuntime checks object/action scope and any SessionContextRef / UserTurnRef used as
input: the Turn must belong to an authorized Session, referenced text must actually exist, and
scope must permit the action. Tools do not discover intent by scanning the whole Session.
ResumeAdvisor is the semantic optimization Skill, not a caller of a duplicate optimization Tool.

Interactive reads are LAZY_TOOL and append exact admitted runtime inputs to later Frames.
EAGER_EXACT headless tasks still freeze their required inputs before the Run. Both share the same
Invocation/permission machinery; changing acquisition does not change business write authority.

## 3. Durable remote Invocation boundary

Accepted ordering:

```text
validate current execution and frozen input
                  |
                  v
budget admission / reservation
                  |
                  v
persist dispatch intent and commit
                  |
                  v
send remote request
                  |
                  v
persist complete business response durably
                  |
                  v
local parse / validation
                  |
                  v
fenced, compatible business-result publication
```

Budget reservation and dispatch intent both precede remote work. Their exact transaction layout
belongs to detailed Contract design; neither may exist only in process memory.

“Complete business response” means the payload required to recover processing. It does not mean
retaining raw Authorization headers, API keys, cookies, login tokens, or other transport secrets.

A network response that has arrived in memory but has not been durably stored is not a recoverable
response. A partial/streamed fragment is not silently treated as a complete response.

### Streaming is transient presentation (Q141)

StreamBridge / SSE can show deltas while the Provider is generating. These fragments are not a
complete durable response, formal Assistant Turn, or business result. They need not be persisted
and may disappear on refresh/recovery; do not add per-delta recovery obligations.

Only a complete response persisted by ModelInvocationRuntime as RESPONSE_DURABLE permits local
parse/validation and eventual formal Turn, Suggestion, or other accepted result. Interruption before
that boundary follows the known failure/unknown-outcome rules; no formal Suggestion or automatic
MemoryExtraction arises from a half stream. Do not stitch old fragments to a Retry's output.

A disconnected frontend does not by itself prove Backend failure or cancel a still-running call.
If Backend completes normally, reconnect reads the eventual complete formal result. Actual business
Save status comes from Application commit evidence, never from streamed "saved" text.

## 4. Recovery cases

| Last durable boundary | Interpretation | Allowed recovery |
| --- | --- | --- |
| No dispatch intent; request not dispatched | Remote work has not crossed the durable dispatch boundary | Validate frozen inputs/permissions/budget and safely continue |
| Dispatch intent exists; no complete durable response | Remote execution may or may not have happened | For model/outcome-sensitive calls: OUTCOME_UNKNOWN; no silent replay |
| Complete durable response exists | Remote output is available for local processing | Resume parse/validation/publication without another model call |
| Canonical result already committed | Business result exists | Preserve it; reconcile local completion without duplicate business assets |
| Old execution generation revoked | That owner no longer has commit authority | Reject its late canonical writes |

The dispatch-intent/no-response window remains ambiguous even if the crash occurred before the
actual network send. Conservatively treating it as unknown is intentional. The protocol cannot
infer “not sent” merely from the absence of a response.

For outcome-unknown work:

- end the old Run as interrupted/outcome-unknown under the eventual state contract;
- release its effective concurrency slot;
- preserve audit, durable inputs, and known/unknown usage;
- require explicit user Retry to create a new Run;
- do not reset the old Run to RUNNING.

## 5. Execution ownership and fencing

Each Run has an execution owner and an execution_generation fencing token. Canonical-state-affecting
writes must validate both current Run eligibility and matching generation at the write boundary.

Timeout, cancel, ownership revoke, or recovery takeover invalidates the former generation.
A late coroutine cannot publish an Analysis, advance a current result, or otherwise commit as
the valid owner merely because it eventually received a response.

Fencing does not imply:

- that the remote Provider stopped executing;
- that network cancellation succeeded;
- that usage is zero;
- that the previous request cannot still consume money.

It protects local execution authority. Remote ambiguity is handled separately through replay
classification, explicit retry, and conservative budget accounting.

The exact claim/revoke protocol, leases if any, atomic writer conditions, and complete transition
table are deliberately left to field-level Runtime Contract design.

## 6. Startup reconciliation

On startup the Harness examines unfinished Runs associated with prior runtime instances and their
last durable Invocation progress.

Responsibilities:

1. identify unfinished work whose former execution ownership is no longer valid;
2. fence prior writers before allowing recovered ownership to publish;
3. inspect the durable dispatch/response boundary;
4. validate the frozen inputs and current permissions before continuation;
5. claim and resume safe local work or undispatched work;
6. end ambiguous remote work instead of silently resending it;
7. release concurrency slots belonging to ended Runs.

Reconciliation never silently upgrades exact JobVersion, RequirementSet, ResumeVersion, baseline,
or other frozen business inputs. A recovery-safe transport state does not make stale business
inputs compatible.

Expired deadlines, revoked permission, stale inputs, and budget limits still matter after restart.
Detailed precedence among failure labels is a later contract question.

## 7. Retry, cancellation, and Fit target serialization

Q116 permits parallel different Fit targets but only one effective RUNNING analysis for a target.
The backend enforces that constraint; UI disabling alone is insufficient.

Q122 adds recovery behavior:

- an ended interrupted/unknown Run stops owning the target slot;
- Retry is explicit and creates a new AgentRun;
- retry_of_run_id preserves lineage to the prior attempt;
- new work performs fresh budget admission and required input validation;
- old successful compatible results remain available if a newer attempt fails;
- stale output cannot become the current result.

A released concurrency slot is not a released cost reservation. An unknown old Invocation may retain
a conservative reservation even while a user retries the target.

Cancellation prevents future valid commits/dispatches from the old owner. It does not authorize
another remote call, rewrite history, or assert a Provider refund.

### Shared parse dependency ownership (Q142)

EnsureRequirementSet's Application-level database atomic claim / active-target uniqueness / CAS
permits one valid producer per exact JobVersion and parser/schema/prompt/policy compatibility target.
Many waiters may reuse its completed immutable RequirementSet. Process-local singleflight is optional.

Only the winning operation owns the Parse Run and pays parse/repair. Waiter cancellation cancels only
waiting. Owner cancellation, failure, or OUTCOME_UNKNOWN exposes dependency-unavailable; do not
silently take over the old Run or its budget and do not restart parsing for waiters. A subsequent
explicit user Retry rechecks for a compatible Set before attempting a new claim. Successful durable
Sets survive downstream task failure; recovery fencing still excludes revoked producers.

### One active foreground Turn per ChatSession (Q155)

Serialize user-facing foreground Turns within a Session. New input waits or explicitly stops the
current Turn before another starts; different Sessions and legitimate independent dependency/
auxiliary/background Runs may progress in parallel. Backend ownership/concurrency controls enforce
this, not UI state alone. Cancellation/fencing excludes late old owners from current writes;
local stop still does not prove the Provider stopped or cost is zero. Detailed claim/release
representation belongs to the later Contract design.

### Proposal confirmation and bounded dependency waiting (Q158-Q159)

Generating/displaying Proposal ends its Turn/Run. Application stores pending confirmation and executes
the exact validated command upon explicit confirmation, without model reinterpretation. It is not
Run recovery or a held foreground slot. A later conversational response uses new bounded execution;
known mutation results/idempotency and revision-conflict rules remain.

Advisor waiting for separate RequirementParse retains its foreground Turn, not a model/Provider
invocation execution slot. Deadline/cancel remain active. Q142 decides whether cancellation affects
only this waiter or the owner operation. Success admits the exact Set and resumes the same task;
failure is explicit, with no silent takeover or remote reparse.

## 8. ToolInvocation replay safety

Tool Contracts declare replay semantics rather than relying on Tool names:

| Conceptual class | Example | Required interpretation |
| --- | --- | --- |
| SAFE_REPLAY | Eligible local read | May repeat only while scope/permission/input validation remains satisfied |
| IDEMPOTENT_REMOTE | Remote operation with genuinely reliable idempotency | Replay depends on that concrete contract, not a generic assertion |
| OUTCOME_SENSITIVE | Model request or external action with uncertain remote result | Do not silently repeat unknown work |

Models/Tools share the Invocation framework, but business safety still takes precedence.

- A Tool label cannot grant ExecutionApproval or consume a single-use approval again.
- Browser Executor remains outside autonomous model-controlled side-effect replay.
- Uncertain actual application outcomes retain the established human-verification boundary.
- v1 Business Tools are typed and scoped, not Shell, arbitrary HTTP, SQL, or filesystem access.

Reliable idempotency behavior, keys, scope, expiry, and resource-specific read-back requirements
must be established in the later Tool/Adapter contract. Do not assume them for a Provider.

Q144 also separates read action semantics from dependency preparation: job.requirements.read returns
a compatible existing Set or explicit missing dependency. No model call, nested Run, or derived asset
creation is concealed inside the read. Application EnsureRequirementSet coordinates the separate
Parse Run through its durable owner/Invocation boundary.

## 9. Durable response versus business authority

Durably storing model output is not accepting it as authoritative:

```text
durable Provider response
        |
        v
schema / reference / domain validation
        |
        v
current-input and execution-fence checks
        |
        v
Application persists immutable business asset
```

Malformed responses may be recoverable as raw payloads but remain invalid business results.
A permitted bounded repair is a new Invocation, not local response parsing, and therefore requires
another budget admission and dispatch record.

If a result has already been committed before a crash, recovery must respect existing identity/
idempotency rules rather than create another copy. Final storage operations remain under the
appropriate Application transaction boundary.

### Committed mutation versus subsequent chat failure (Q156)

A successful Application commit is final business truth. Failure of a later model invocation or
unfinished stream does not roll it back or make that mutation OUTCOME_UNKNOWN. Persisted mutation
result, not assistant wording, determines whether the confirmed Proposal applied.

Recovery/explicit retry consult that result and recognize the same confirmed Proposal idempotently,
avoiding duplicate Evidence/ResumeVersion creation. UI can show "formal changes saved; subsequent
reply unfinished" independently of the narration outcome. A new change needs a new ChangeProposal
and confirmation. Remote retry still obeys Q122; local reconciliation does not authorize silent
Provider replay. Exact result/schema/transaction implementation is deferred.

Q158 narrows the actual ChangeProposal workflow: its generating Run is already ended before
user confirmation. Generic post-write admitted-input mechanics do not keep that Run alive or
revive it. Application confirms/commits independently; any subsequent narration uses new bounded
execution and the actual result, not a second interpretation of the authorized patch.

### Deletion/confirmation arbitration and intentionally unrecoverable UI state (Q166-Q167)

Unsaved page ResumeDraft is transient UI state and may be lost on crash; it is not an Active Recovery
Dependency or promised checkpoint. Save / Discard / Cancel covers normal navigation only.

Deleting a Session invalidates unconfirmed originating Proposals and stops its active foreground
work under cancellation/fencing. Recovery, refresh, or an old Proposal ID cannot restore their action
eligibility. Application atomically checks Session/Proposal state against confirmation/deletion races;
only one competing result succeeds. Preserve already committed mutation results and formal assets.
New changes require new Proposals in a valid context; no implicit authorization resurrection.

## 10. Storage and retention integration

The complete four-layer design now lives in [storage.md](storage.md), which owns the detailed
Business Durable Assets / Harness Recovery Payload / Harness Audit Metadata / Operational Logs
distinction. Recovery uses those boundaries rather than maintaining a competing storage model.

Keep exact payload needed for unfinished recovery until its recovery boundary explicitly ends.
Completed raw payload may be purged under retention; audit must indicate availability honestly.
Cleanup never deletes business history, proves unknown cost was zero, or permits reconstruction of
the old exact Frame from current assets. Do not persist transport secrets or log sensitive payloads.

Q136 makes needed payloads Active Recovery Dependencies until the safe recovery boundary ends.
A later Historical Source Reference may outlive its payload without pinning it forever. Check
availability before continuation; a permitted read of an existing exact business version is a new
ToolInvocation, never the old response. Missing sources are SOURCE_UNAVAILABLE; do not guess, refetch
platform pages automatically, or replay external effects to fill the gap.

## 11. Conceptual object map — not a final schema

```text
Agent Harness
|
+-- AgentRun
|   +-- identity / Skill / frozen Context lineage
|   +-- concurrency / lifecycle / ownership
|   +-- execution_generation / runtime instance
|   +-- retry lineage / budget
|   +-- ContextFrame[]
|   +-- ModelInvocation[]
|   +-- ToolInvocation[]
|
+-- Runtime
    +-- dispatch boundary
    +-- claim / revoke / fencing
    +-- startup reconciliation
    +-- cancellation / explicit retry
    +-- budget / usage
```

Later field-level design must define:

- AgentRun identity, Skill, frozen inputs, concurrency, lifecycle, ownership, retry, budget;
- ModelInvocation sequencing, exact Frame, dispatch state, Provider metadata, durable response,
  usage certainty;
- ToolInvocation action, argument lineage, replay semantics, side-effect state, result;
- ContextFrame exact messages/ToolResults, redaction/compaction, token accounting;
- Runtime claim/revoke/fencing/reconciliation/cancel/retry transitions.

Names in this map identify required semantics. This architecture Grill does not finalize storage
columns or all field values.

## 12. Budget, Memory, and Context Compaction integration

See [Budget](budget.md) for atomic check/reserve, settlement, and unknown exposure. A retry, auxiliary
Invocation, or graph continuation cannot bypass the same admission boundary.

Q130 uses separate owners on common infrastructure: independent MemoryExtraction charges
BackgroundMemoryBudget and respects foreground-priority headroom. Durable pending source ranges
survive restarts, but a pending range does not permit silent replay of a previously unknown remote
extraction. Failed extraction does not undo the completed user-facing Turn.

Q132 semantic Context Compaction normally remains inside the current AgentRun. Its auxiliary
ModelInvocation shares the execution_generation, budget, deadline, audit, and recovery semantics:

```text
dispatch intent durable
   -> complete compaction response durable
   -> local checkpoint validation
   -> fenced checkpoint publication
   -> new ContextFrame
```

If response is not durable after intent, treat the call as unknown rather than automatically
recompacting. If response is durable, resume local validation/publication without another call.
Keep the former recoverable Context until its candidate replacement is validated and published.

An explicit Provider CONTEXT_TOO_LARGE rejection may take Q132's bounded reactive-compaction retry
path. A timeout/disconnection/unknown result cannot be reclassified as that rejection to justify
replay. Q135 fixes semantic compaction and reactive retry at most once each per entire AgentRun,
subject also to the Run's total budget; all calls pass through ModelInvocationRuntime.

Q134 permits an authorized same-task Advisor write to append Application's actual committed exact
references as admitted runtime inputs and build a new Frame. It does not rewrite frozen initial
Context, earlier outputs, or independent Fit inputs, nor reset execution budgets.

Q139 separates gates: automatic extraction publication rechecks Auto Learning, while every new
Frame checks Recall. Recovery cannot use an old Package to bypass either current setting.
Disabling one does not implicitly disable the other, delete entries, or prohibit explicit validated
user management. Direct Memory blocks are excluded from checkpoint sources.

### Recoverable derived work after formal Save (Q147)

Application Prepare validates/reconciles, checks revisions, determines affected current Resumes and
required derived tasks. One short SQLite transaction commits authority changes, exact current
pointers/baseline/Resumes/GroundingSets, and their DerivedWorkItem(PENDING) intents together.
Only after commit do expensive PDF render, preview, index, and cache tasks execute.

Startup reconciliation can find durable pending work even if the process crashed immediately after
commit. Jobs must be explicitly safe to replay and idempotent; no MQ is required. Failure retains
saved authority but may produce readiness such as EXPORT_NOT_READY. Before publishing a current
artifact, validate exact source versions/hashes/current references; stale completion may retain a
historical artifact but must not replace the current artifact.

This is Application-owned derivative recovery, not automatic model/remote-action replay. Provider
calls, recruiting-platform access, email, and browser application continue to use outcome-sensitive
dispatch/unknown/retry semantics. Derivative intent persistence does not give Harness business
mutation authority or create a long database transaction around expensive work.

Q151 uses this atomic boundary for Delete Evidence: logically remove the experience, snapshot current
facts, remove its explicit inclusion/body from all directly affected current Resumes, advance their
formal versions/grounding, and record needed derivative work. No Claim-level semantic scan, automatic
old-version fallback, or historical PDF mutation is part of deletion.

Q152 makes derivative generation demand-driven. Save synchronizes authority and artifact-currentness
metadata, but need not schedule every format for every Resume. Required work at Save is registered
in that transaction; later preview/export/Preparation requests also durably register their exact-source/
configuration intent before executing. Compatible work can be idempotently reused; old completions
cannot publish as current. Current formal-use validation remains distinct from historical readability.

Q148-Q149 confirmation authorizes one target-specific ChangeProposal. Recovery cannot replace its
target/patch with current model output or bypass revision conflicts. Regenerated changes require a
new preview rather than silently transferring consent. Detailed local command replay/authorization
schemas remain contract work; no new remote replay permission is implied.

### Shared platform safety and independent workflow recovery (Q160-Q161)

PlatformAccessSafety persists shared (platform, account) risk/capacity/action admission across all
recruiting workflows. Startup or workflow Retry cannot bypass strong-risk BLOCKED_REQUIRES_USER.
Strong risk needs user handling and explicit resume; predictable capacity may recover by policy.
Ordinary page/selector/browser failure is not automatically account-level risk. Safety is not
ExecutionApproval or permission to replay platform effects.

CollectionRun retains frozen PreferenceSetVersion. User stop prevents subsequent accesses and ends
with retained partial results, never rolling back successfully stored Jobs. Current Preferences
re-filter local data without a new collection, restart, or deletion of now-unmatched Jobs.
This does not weaken outcome-sensitive execution recovery.

### Obsolete derivative dispatch and minimal execution checks (Q164-Q165)

A durable derivative intent does not require execution forever. Before starting expensive work,
recheck exact source/current references and remaining demand; skip obsolete current-artifact work.
In-flight safe computation may finish but cannot overwrite current artifacts. Keep completed history.
This rule does not apply to automatic replay of model/platform calls.

Executor's required live identity/availability checks remain within execution authorization and
shared platform safety. They do not refresh JobVersion, reparse requirements, retarget immutable
Snapshots, or add model analysis. Clear execution-relevant mismatch stops subsequent actions and
requires explicit refresh/repreparation; record actual outcome without inventing successful application.

### Failed Memory ranges, deleted sources, and frozen-input revocation (Q169-Q172)

Failed or outcome-unknown extraction batches remain distinct from newer pending ranges. Later Turns
can proceed, without falsely advancing old work to success or silently re-including its source.
Only explicit Retry reprocesses the failed/unknown old range. Capacity/budget waiting before
dispatch remains pending; it is not an extraction failure.

Deleted source Sessions prevent new extraction/publication; cancel active extraction where possible
and recheck source state before accepting late candidates. Existing Memory is independently retained.
Already-dispatched work still has truthful cost/unknown outcome and necessary recovery audit.

A mid-run revocation affecting protected EAGER_EXACT inputs invalidates continuation of that frozen
task. No silent scope reduction, revoked-content repair/Frame, or valid current-result publication.
New authorized input scope needs a new task. Durable Provider response does not override current
permission; previously transmitted data cannot be locally retracted.

## 13. Non-goals and remaining design work

Not required:

- resuming from every code line;
- a claim of exactly-once remote model execution;
- auto-replaying unknown calls to improve apparent success;
- general distributed workflow infrastructure beyond current local needs;
- model-controlled browser retry;
- treating LangGraph checkpoints as remote-action receipts.

Still to detail later:

- precise Invocation/Run transition representation;
- storage transaction boundaries for reservation, intent, durable response, and canonical commit;
- claim/revoke concurrency protocol and concrete idempotent publication;
- treatment of late diagnostic/usage evidence without permitting stale canonical writers;
- payload retention durations and cleanup coordination;
- concrete Provider/Tool idempotency capabilities.

These are not implemented facts or already approved field-level choices.

## 14. Verification implications and formal writeback

Later acceptance should exercise crash boundaries, not just successful restart:

- crash before dispatch intent;
- crash after intent but before network send;
- response received but not persisted;
- durable response persisted but parsing not complete;
- cancellation while remote work is outstanding;
- old owner returning after takeover;
- restart with stale business input;
- Retry while the former call's usage remains unknown;
- cleanup of terminal payload without business-history loss;
- replay-safe read versus outcome-sensitive remote action;
- durable compaction response recovered without another model call;
- invalidated compaction owner unable to publish a checkpoint;
- background pending-range recovery without replaying an unknown extraction;
- explicit Context rejection distinguished from unknown model outcome.

Expected outcomes follow the accepted rules above; this document does not claim tests exist or pass.
Formalize responsibilities in architecture/contracts, behavior checks in acceptance, and actual
implementation status separately in progress.

Q135-Q137 additionally require auxiliary calls to use the same unique Provider execution boundary,
active recovery dependencies to resist retention cleanup, historical source re-reads to be recorded
as new invocations, and late automatic extraction publication to honor current Auto Learning.

Q140-Q142 add hidden SDK retry prevention, discarded half-streams with preserved invocation outcome,
frontend reconnect to a Backend-completed result, and cross-process parse contention with owner-only
cost and independent waiter cancellation. A half-stream is never a recovery receipt.

Related Tool naming, action purity, typed source validation, and dependency signaling are defined
in [Tool Actions](tool.md). Architectural objects/properties are collected for later design in
[Contract Design Inventory](../contract/contract-design-inventory.md); neither document finalizes
field schemas or reports implementation.
