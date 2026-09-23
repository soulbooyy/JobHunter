# SL-03.M1 Contract Grill Decision Register

> English is authoritative. This is the single decision/provenance record for SL-03.M1, not normative Contract text or implementation evidence. Preserve accepted conclusions and scoped supersession; do not copy question transcripts or present recommendations as accepted decisions.

[Design navigation](README.md) · [Milestone plan](../../plans/slices/sl-03-invocation-requirements.md#sl-03m1-invocation-durability-and-recovery-foundation) · [Contract ownership](../../contracts/structure.md) · [Readiness ledger](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

## Purpose and session state

- Started: 2026-09-23, following the user's explicit instruction to start this Grill.
- Milestone: SL-03.M1 — Invocation durability and recovery foundation.
- Skill: grill-me/grilling; Chinese discussion and English formal documentation.
- Decision namespace: CG05-Qn. No existing CG05 decision or milestone handoff was found at entry.
- Closure: **2026-09-23.S3M1-r1**, explicitly authorized and published; see [CG05-PUB](#cg05-pub) for scope, writeback and evidence.
- Q1–Q130 are resolved with recorded refinements. Q129 narrows MODEL preparation inputs by deriving run_id from execution qualification; Q130 preserves Invocation-owned format authority in response metadata. No additional numbered batch remains; the original pre-closure consolidation below is preserved as historical stage evidence.
- Four consumed M1 Contract portions are Ready; implementation is Not started and acceptance Not executed. Future production/cleanup/platform-consumer scopes remain Pending.
- No backend/frontend implementation, dependency installation, migration, normative publication, commit or push is authorized by starting the interview.

<a id="cg05-s1"></a>
## CG05-S1 — User-directed interview and maintenance discipline

Status: ACCEPTED session direction inherited from the user's explicit workflow corrections and current start instruction. Use ten independent questions per ordinary round, with stable numbering and recommendations; wait for answers. Do not infer acceptance from silence or turn factual research into questions for the user. Use bounded agents for key factual checks only, not full review every round.

After an answered round, persist effective conclusions, reasons/boundary examples, intended normative destinations, unresolved branches and any scoped SUPERSEDED relationship here before asking the next round. Ordinary rounds update this register only and perform focused consistency/reference checks. Product, Architecture, Acceptance, plans and status are not routine round outputs. An explicit architecture change or important decision needing owner reconciliation requires the user's directed review/writeback plan; do not silently edit those owners. Start-of-Grill status is recorded once now without changing readiness. Later material scope/readiness changes and authorized publication are separate update occasions.

The user subsequently permitted temporary repository retention of scripts/check_contract_links.py for repeated Contract Grills, superseding the proposed immediate removal. Keep the existing script and invocation for now; removal and current-reference cleanup are due after all Contract Grills finish, not after this milestone alone. Do not create additional per-round audit scripts or reports in the repository.

At authorized closure, complete decision-to-document traceability and cross-document/interface consistency, publish the actual consumed scope with stable IDs, reconcile necessary owners/navigation/readiness, and create docs/development/handoff/sl-03-m1-handoff.md for a real development transfer. Do not create an empty or unreviewed development handoff now. Publication authorization for the completed SL-02.M2 stage does not automatically publish SL-03.M1's unanswered scope.

## Verified entry checkpoint

Read-only inspection on 2026-09-23; HEAD 362ff36. Existing M1 backend/API/handoff modifications and untracked files remain untouched. One bounded factual agent checked actual persistence, migration, composition and test-source boundaries; no tests or database operations were run.

| Subject | Observed evidence | Interpretation |
| --- | --- | --- |
| Existing local persistence | [Store](../../../backend/src/jobhunter/infrastructure/persistence/sqlalchemy/uow/store.py) supplies physical-directory ownership, SQLite recognition, explicit transactions and commit-uncertainty handling | Reusable local primitives; not proof of external dispatch or Invocation fencing |
| Current migration source | b720a94fd381 → cd891047a2e6 → ef03c92ba671; the candidate migration is untracked and Store/bootstrap changes remain uncommitted | Working-tree target is schema 3; no actual user database was inspected; reverify head at implementation |
| Current composition | [Container](../../../backend/src/jobhunter/bootstrap/container.py) assembles Entry, Preferences and Candidate Authority | No Model/Tool/Run runtime, Gateway/provider adapter or invocation startup reconciliation found in the inspected backend |
| Dependencies | [Root manifest](../../../pyproject.toml) has no LangGraph, model-provider SDK or Langfuse dependency | Target technology is not installed capability; adapter behavior requires later focused research |
| Existing evidence | [Recorded M1 backend evidence](../../progress/traceability.md#saved-candidate-backend-evidence) reports 294 passing tests; existing storage/transaction tests include process faults | Inherited evidence, not rerun here; transaction/receipt proof does not prove remote replay safety |
| Normative scope | execution-runtime.md and evaluation-observability.md are planned destinations without bodies; Common/Storage/Workspace and Derived Work have prior reviewed portions | Preserve prior consumers; M1 invocation scope remains Pending |

No required upstream business capability is named by the SL-03.M1 plan. Applicable local persistence is reused; Materials rendering and formal Job production are not entry gates for this Contract interview.

## Controlling inherited boundaries

- [Architecture §§9/12](../../architecture.md#12-durable-execution-and-recovery), [Recovery provenance](../harness/recovery.md) and [Acceptance §9.2](../../acceptance.md#92-crash-and-cancellation-boundaries) control dispatch, complete response, execution authority and recovery. Historical state labels and Inventory examples are not frozen fields or enums.
- Persist dispatch intent before remote send and a complete business response before recoverable local processing. Intent without a complete durable response is ambiguous even when actual send may not have occurred. No silent model replay, hidden SDK retry/fallback or graph-checkpoint replay permission is introduced.
- Complete durable response permits local parse/validation under current eligibility and fencing; it does not establish a valid canonical business result. Reconcile already committed results without duplicate business assets.
- AgentRunRuntime owns bounded Run execution authority; ModelInvocationRuntime owns the admitted provider-call boundary; Gateway adapts transport; ToolInvocationRuntime preserves concrete action admission/replay. Runtime does not gain business write authority.
- Revocation/cancel/timeout/takeover invalidates old writers. Local cancellation does not prove remote cessation, zero usage or a refund. Run-level retry of ended unknown semantic work creates a new Run under fresh admission and preserved lineage/exposure. Q11 distinguishes this from safe same-Run recovery/continuation and consumer-defined Invocation repair/retry; it does not authorize silent replay of unknown remote work.
- [Storage provenance](../harness/storage.md) and Architecture §13 separate business assets, recovery payload, audit metadata and operational logs. Protect active recovery dependencies; missing historical payload cannot be reconstructed from current data. Payload storage excludes transport secrets and does not bypass permission.
- Safe local Materials recovery, Candidate Save, platform risk/approval, business workflows and budget settlement remain with their owners. Deterministic platform callers are not forced into AgentRun merely to reuse an applicable primitive. No universal side-effect framework is authorized.
- SL-03.M2 owns full protected semantic invocation, Context/Tools/Budget and real-path semantic evidence infrastructure; M3 owns RequirementParse/Ensure. This Grill closes necessary producer/consumer interfaces without pretending those later scopes are already implemented or reviewed.

## Responsibility and prospective document map

| Owner/destination | M1 consumed responsibility | Boundary |
| --- | --- | --- |
| Planned agent/execution-runtime.md | Minimum Run execution-control and Invocation persistence/recovery interfaces; dispatch/response, fencing, cancellation, startup and unknown outcomes | One protocol owner; full Skill/Context/Budget/business definitions remain with their consumers |
| Existing foundation/storage.md | Recovery payload/audit availability, integrity, active dependencies, cleanup, transaction and migration agreement | Extend actual consumed scope; preserve earlier receipt/Materials semantics |
| Planned evaluation/evaluation-observability.md | Deterministic invocation-boundary evidence and failure/concurrency proof | No complete semantic Eval, judge, Langfuse integration or rollout policy |
| Existing common.md | Only necessary shared identity/scalar/reference/error expression | Reuse current conventions; new IDs await accepted scope and publication |
| Existing foundation/workspace.md | Reused physical ownership and startup applicability if affected | No new workspace/product configuration surface by implication |
| Product/Architecture/Acceptance/Plans | Current behavior, responsibility and proof owners | Review/writeback only through the user's directed process |

## Dependency-ordered design tree

1. Internal consumer boundary, identity and minimal execution-control representation; protected record/response meaning.
2. Complete shapes, required/null fields, exact references and immutable versus mutable portions.
3. Durable transitions, dispatch authorization, complete response and local commit uncertainty; owner changes and cancellation races.
4. Restart reconciliation, safe local continuation, explicit retry lineage and action-specific replay interfaces.
5. Storage availability, active recovery dependencies, retention/cleanup arbitration, integrity and migration.
6. Consumer/error contracts and deterministic fault/concurrency evidence; prior-consumer compatibility.
7. Authorized publication, both verification seams, truthful readiness and backend handoff.

Initial planning estimate: 8–10 ten-question rounds; material new branches may require about 12. This is not a question quota or a promise to stop before interfaces close. Provider/adapter facts, transaction races and cleanup behavior require focused evidence where a branch consumes them.

## Round 1 — Invocation Boundary, Execution Identity and Durable Response

<a id="cg05-q1"></a>
### CG05-Q1 — Internal M1 interfaces

Status: ACCEPTED. M1 exposes internal Application/Runtime interfaces, not a new public HTTP API for Run creation, polling, cancellation or Retry. Internal operations still require explicit input/result/error and transaction contracts and must be exercisable by real consumers and deterministic boundary tests. User-facing HTTP protocols belong to their actual consuming milestones.

Intended destination: execution-runtime interface scope and deterministic evidence scope. This does not remove cancellation/recovery from M1's internal responsibilities.

<a id="cg05-q2"></a>
### CG05-Q2 — Minimum AgentRun execution-control portion

Status: ACCEPTED. M1 defines only the durable Run identity, execution authority and ending/recovery information needed for this foundation. These are portions of the same AgentRun, not a second generic Job entity. Complete Skill, Context, Budget and business-input definitions remain with their later scopes. M2 must close those interfaces before actual protected model invocation; an M1 minimum record is not complete call admission.

Intended destination: execution-runtime's bounded M1 Run portion and later-consumer interface boundary. Exact fields remain open beyond separately accepted decisions.

<a id="cg05-q3"></a>
### CG05-Q3 — Independent Invocation identity

Status: ACCEPTED. Every Invocation has an independent server-generated UUIDv4 invocation_id. A Run-local sequence, if later needed, does not own identity. Provider request IDs are external correlation only and cannot replace local identity. Equal inputs do not merge two distinct calls. This does not grant permission for a new call or settle action-specific replay mechanics.

Intended destination: execution-runtime identity and necessary Common scalar applicability.

<a id="cg05-q4"></a>
### CG05-Q4 — Fresh backend runtime identity

Status: ACCEPTED. Generate a fresh UUIDv4 runtime_instance_id for each backend startup; keep it stable for that instance's lifetime. Do not use a PID or restore the prior instance's identity from configuration. Runtime identity distinguishes execution instances, but persisted execution-authority conditions determine valid writes; matching a process identifier alone is insufficient.

Intended destination: execution-runtime ownership/startup interface and necessary Workspace applicability.

<a id="cg05-q5"></a>
### CG05-Q5 — Generation advances only when execution authority is granted

Status: ACCEPTED with user correction. execution_generation identifies successive grants of execution authority within one Run. The first successful grant uses generation 1; each subsequent successful grant or regrant increments it monotonically. Revocation/expiration of the current execution qualification alone does not increment the counter. Generations never decrease or get reused; this is neither Provider-call count nor retry count.

Every state-affecting submission requires the correct run_id, matching current execution_generation and currently valid execution qualification at its write boundary. A former owner is rejected after revocation even while the stored generation still has its old value. After a later grant, the old generation also fails. Example: grant 1 → revoke qualification while retaining 1 → grant 2. No intermediate ownerless generation is manufactured by counting both revocation and regrant.

SUPERSEDED proposal fragment: the first recommendation's blanket advancement on authority invalidation. It was corrected before acceptance; only grant/regrant advancement is effective. The correction changes no accepted architectural fencing invariant: Architecture §12.2 requires exclusion of former writers but leaves the detailed claim/revoke representation open. At Round 1, representation before the first grant, integer limits, exact atomic grant conditions and overflow behavior were unanswered. Q12/Q13/Q15 subsequently settle the initial value, owner reference and atomic grant/revoke principle; numeric limits and complete transition admission still require closure.

Intended destination: execution-runtime ownership/fencing and Storage atomic writer conditions; no routine Architecture writeback is needed or performed.

<a id="cg05-q6"></a>
### CG05-Q6 — Immutable committed dispatch descriptor

Status: ACCEPTED. Once dispatch intent commits, freeze the actual invocation descriptor: selected target and actual request data or exact references, as defined by the relevant consumer. Recovery cannot replace Provider/model, parameters, action or sources under the same Invocation. Changes require the consumer's permitted new Invocation/new Run path and admission. This defines immutability at the committed dispatch boundary, not a universal arbitrary-effect request schema.

Intended destination: execution-runtime dispatch and consumer-owned descriptor agreement; Storage immutability.

<a id="cg05-q7"></a>
### CG05-Q7 — Versioned data-only complete response

Status: ACCEPTED. Persist a versioned data representation defined by the corresponding adapter, sufficient to recover processing. Preserve necessary complete output and structure without unapproved summarization, truncation or rewriting. Do not persist SDK object snapshots, exception objects or complete raw HTTP messages. Required output validity remains a later validation concern; this decision selects no concrete Provider, SDK or complete response field inventory.

Intended destination: execution-runtime response/adapter interface and protected Storage payload representation.

<a id="cg05-q8"></a>
### CG05-Q8 — One immutable complete response per Invocation

Status: ACCEPTED. Each Invocation has at most one published immutable complete response. Repeating the same response may be acknowledged idempotently; attempting a different response is an integrity conflict and preserves the original rather than overwriting it. Equality details remain to be frozen with the representation. Response-write admission still follows the eventual execution-authority protocol; idempotency does not independently authorize a revoked writer. Q89 subsequently clarifies that read-only confirmation of an already published identical response is not a new response write and can succeed after ending, revocation or expiry.

PARTIALLY SUPERSEDED by CG05-Q89: any interpretation requiring current execution qualification for that read-only confirmation. The at-most-one-response rule, different-response conflict and current authority requirement for first publication remain effective.

Intended destination: execution-runtime response publication and Storage uniqueness/integrity.

<a id="cg05-q9"></a>
### CG05-Q9 — Response completeness is separate from usage completeness

Status: ACCEPTED. Complete recoverable business output may be durably published even when token/cost usage information is incomplete. Preserve missing usage as unknown, never zero. Durable response permits eligible local processing; it does not alone authorize releasing cost exposure/reservation. Detailed accounting and settlement belong to the later Budget interface.

Intended destination: execution-runtime response evidence and explicit Budget-consumer agreement; no Budget schema is published in this round.

<a id="cg05-q10"></a>
### CG05-Q10 — Resolve local commit uncertainty from durable facts

Status: ACCEPTED. An uncertain local response-persistence commit is distinct from an unknown remote invocation outcome. Reconcile committed facts by Invocation identity before choosing dependent continuation. A confirmed complete durable response permits eligible local recovery. If no recoverable response is established, interpret the known dispatch boundary; if local commit truth itself remains unresolved, retain that uncertainty and stop dependent advancement. A database-driver exception after receiving output never authorizes another Provider request.

Intended destination: execution-runtime recovery/result classification and Storage commit-uncertainty interface. Concrete result/error representation and bounded reconciliation remain open.

## Round 1 persistence and local review

Actual writeback: this register only. Reviewed Q5 against Architecture §12.2 and the Recovery record's authority/fencing boundary: revocation without increment still excludes old writers through current qualification, and regrant changes the generation. Common's distinction between row revision, identity and structural schema version remains intact. Q7–Q10 preserve complete-response versus domain-validity versus usage versus local-commit truth as separate concerns. No prior normative ID, readiness state or owner document is changed; no agent, runtime test, dependency installation or migration is needed for this ordinary round.

The new working-tree status also shows concurrent Materials code/tests and migration source a41d7e90c263_materials.py. This is an observed change since the entry checkpoint, not a review of that implementation or proof of a new installed schema/head. Preserve those files; reverify applicable migration/composition facts when a later branch actually consumes them. The source-time entry table remains historical.

## Round 2 — Run Identity, Ownership and Invocation Relationships

<a id="cg05-q11"></a>
### CG05-Q11 — Stable Run identity and specifically Run-level retry

Status: ACCEPTED with user refinement. AgentRun uses a server-generated UUIDv4 run_id, not an identity derived from target, input hash or time. Equal task inputs can belong to different Runs. Crash recovery or safe continuation of the same AgentRun preserves its original run_id. A user- or consumer-initiated new Run-level retry creates a new run_id, with fresh applicable admission and retained lineage/exposure; it does not reopen or recycle the old Run identity.

Invocation-level retry/repair is defined separately by its consuming Contract. This decision neither requires every operation called retry to create a new Run nor permits hidden transport retry, unknown-call replay or unadmitted repair. Existing bounded repair and safe local continuation remain governed by their distinct accepted rules.

SUPERSEDED proposal fragment: the unqualified wording that every explicit Retry creates a new Run. Only the Run-level retry case has that identity rule. No inherited ban on silent replay of unknown remote effects is weakened. Exact retry linkage fields were open at this decision; Q22 subsequently defers them to the first actual Run-level retry consumer, outside M1.

Intended destination: execution-runtime Run identity and consumer-owned retry/repair interface; Common UUID applicability.

<a id="cg05-q12"></a>
### CG05-Q12 — Zero records that authority has never been granted

Status: ACCEPTED. execution_generation is 0 before the first successful execution-authority grant. Zero never authorizes execution. The first grant changes it to 1; subsequent regrants advance it. Revocation retains the last granted value rather than resetting it to 0. This avoids a nullable counter while preserving Q5's grant-only meaning. Numeric ceiling/overflow behavior was open at this decision and is subsequently settled by Q21.

Intended destination: execution-runtime initial record and grant conditions; Storage representation/integrity.

<a id="cg05-q13"></a>
### CG05-Q13 — Nullable current runtime-owner reference

Status: ACCEPTED. Use nullable owner_runtime_instance_id for the backend instance currently holding Run execution authority. A grant sets it and revocation clears it, retaining execution_generation. Do not add a redundant has_owner Boolean. A non-null owner alone does not establish valid submission: current Run state, matching generation and other applicable eligibility/admission conditions still apply.

Intended destination: execution-runtime ownership representation and Storage conditional writer rules.

<a id="cg05-q14"></a>
### CG05-Q14 — Existing exclusive local ownership without distributed leases

Status: ACCEPTED. The initial delivery reuses the existing physical data-directory exclusive-owner mechanism instead of adding distributed lease expiry, renewal or heartbeat tables. After acquiring actual directory ownership, startup coordinates prior-instance records; in-process tasks arbitrate using persisted execution qualification and generation. Cancellation, call timeout and revocation remain required and are not removed by omitting a lease protocol.

Intended destination: execution-runtime startup/ownership interface with Workspace/Storage. No multi-backend same-Workspace execution or new deployment model is authorized.

<a id="cg05-q15"></a>
### CG05-Q15 — Atomic grant and revoke arbitration

Status: ACCEPTED. Execute grant/revoke through persisted atomic conditional updates. A successful grant commits its qualification checks, generation advancement and owner assignment together. Losing a claim race does not increment the counter. Revocation targets the expected current execution authority so a delayed old revoke cannot clear a newer owner. In-process locks may assist but cannot alone establish correctness.

Intended destination: execution-runtime ownership operations and Storage atomicity. Exact operation inputs, full Run-state predicates and uncertain-grant reconciliation remain later details.

<a id="cg05-q16"></a>
### CG05-Q16 — Frozen dispatch-generation provenance

Status: ACCEPTED. Capture dispatch_generation when dispatch intent commits and never rewrite it. It identifies the execution-authority generation that initiated this Invocation, not the generation currently processing a saved response. A later authorized generation may locally process a prior generation's complete durable response without relabeling its dispatch or sending it again.

Example: generation 1 dispatches and durably records a response; after restart generation 2 obtains valid authority and resumes local validation. Invocation provenance remains generation 1. The representation before dispatch was open at this decision and is subsequently settled by Q26.

Intended destination: execution-runtime Invocation lineage/dispatch/recovery and Storage immutability.

<a id="cg05-q17"></a>
### CG05-Q17 — Model and Tool invocation kinds only

Status: ACCEPTED. M1 defines MODEL and TOOL Invocation kinds for its actual Harness consumers. Shared portions express identity, durable progress and recovery relationships; corresponding interfaces own Model request and typed Tool action data. Do not add HTTP, BROWSER or CUSTOM_EFFECT extension kinds, and do not force deterministic platform workflows into AgentRun solely to reuse a primitive. Applicable future reuse still requires the concrete interface agreement in the plan.

Intended destination: execution-runtime kind/shared-versus-consumer representation. Complete per-kind fields and replay semantics remain open.

<a id="cg05-q18"></a>
### CG05-Q18 — No speculative Run-local invocation sequence

Status: ACCEPTED. M1 does not add invocation_sequence. Recovery does not require a contiguous Run-local ordinal; a later consumer needing explicit order must define that relation or field. Timestamps cannot stand in for strict execution order, and an Invocation ordinal must not substitute for budget call accounting. This does not grant permission for concurrent dispatch or define an ordering API.

Intended destination: execution-runtime minimum field scope and later-consumer boundary.

<a id="cg05-q19"></a>
### CG05-Q19 — Complete provider termination can still yield unusable output

Status: ACCEPTED. A response with an explicit output-limit ending may qualify as complete when the adapter establishes the protocol's complete terminal result. Preserve output and the ending reason; business validation separately determines usability. A disconnected partial stream without terminal completeness evidence does not qualify. No extra repair is authorized merely because output ended at a limit: any repair remains a separately admitted call within its consumer's accepted bounds.

Intended destination: execution-runtime response-completeness/adapter agreement and deterministic evidence. This does not claim a selected SDK's finish events are already researched or implemented.

<a id="cg05-q20"></a>
### CG05-Q20 — Response identity belongs to its Invocation

Status: ACCEPTED. A complete response is an Invocation-owned one-to-one record located by invocation_id; do not introduce a separate business response_id. Storage may use an internal payload locator without creating a second call-result identity. Equal payload hashes cannot merge the response relationships of distinct Invocations. Q8 still limits each Invocation to one published immutable complete response.

Intended destination: execution-runtime response relationship and Storage identity/integrity.

## Round 2 persistence and local review

Actual writeback: this register only. Q11 explicitly narrows retry identity without reviving unknown remote calls: same-Run safe continuation, Run-level retry and consumer-defined Invocation repair/retry are distinct. The inherited-boundary summary above now uses that qualification. Q12/Q13/Q15 preserve Q5: generation 0/null owner before first grant; grant 1/current owner; revoke retaining 1/null owner; valid regrant 2/new owner. A response's original dispatch_generation under Q16 is provenance, not a reason to reject legitimate local recovery by a newly authorized generation. Q19 preserves the complete-versus-business-valid distinction in Q7, and Q20 preserves Q3/Q8 identity/cardinality.

Local checks cover decision locators, accepted/amended scope, referenced paths/anchors and whitespace. No authority-document writeback, readiness change, agent review, runtime test, dependency installation, migration or implementation is performed for this ordinary round.

## Round 3 — Dispatch Authority, Recovery Boundaries and Scope Correction

<a id="cg05-q21"></a>
### CG05-Q21 — Exact bounded execution-generation integer

Status: ACCEPTED. execution_generation is an exact integer in 0–9007199254740991, using the same exact-integer representability boundary already used by Common. It is not a business revision and does not inherit revision increment semantics. Exhaustion refuses a further grant without wrapping, resetting or reusing a generation; reading and revoking existing qualification remain possible.

Intended destination: execution-runtime counter/admission and necessary Common scalar applicability; Storage integrity.

<a id="cg05-q22"></a>
### CG05-Q22 — Defer Run-level retry linkage until its first consumer

Status: ACCEPTED scoped deferral after the user's conditional refinement and a focused scope check. The current SL-03.M1 plan defines persistence, ownership, cancellation, reconciliation, unknown outcomes and safe local continuation; it does not identify an internal retry_run() capability or a Run-level retry consumer. Accepted Q1/Q2 define internal interfaces and the minimum execution-control portion, not authorization to deliver every future Run operation. Therefore M1 does not add retry_of_run_id or a Run-level retry command.

Preserve Q11's identity boundary: safe recovery/continuation retains run_id, whereas an actual new Run-level retry uses a new identity and applicable fresh admission. The first actual retry consumer must define its lineage/interface, including whether a direct predecessor reference is sufficient. No root retry ID, retry sequence or general lineage entity is introduced now.

SUPERSEDED proposal fragment: adding nullable retry_of_run_id to M1 with same-Workspace/ended-predecessor constraints. These field/validation suggestions are not current M1 norms. The user permitted retaining that proposal only if M1 already delivered retry_run(); the current scope does not meet that condition. This narrows speculative scope without changing the current milestone plan or weakening unknown-call replay restrictions.

Intended destination: execution-runtime M1 exclusions and future-consumer boundary. No Product/Architecture/Plan writeback is needed for this scope correction.

<a id="cg05-q23"></a>
### CG05-Q23 — One immutable owning Run for each Harness Invocation

Status: ACCEPTED. Each MODEL/TOOL Harness Invocation has exactly one required, immutable run_id. It cannot transfer between Runs or acquire another Run owner. Safe continuation processes it under its original Run; a new Run needing a call creates its own Invocation. Business-result reuse does not share Invocation execution identity. This is not a requirement to wrap all platform operations in AgentRun.

Intended destination: execution-runtime relationships and Storage reference integrity.

<a id="cg05-q24"></a>
### CG05-Q24 — Consumer-owned bounded invocation concurrency

Status: ACCEPTED. M1 does not impose a universal maximum of one Invocation per Run, nor authorize unlimited concurrency. The actual consumer defines permitted dependency/order and bounded concurrency; Runtime enforces that admission. The foundation guarantees each Invocation's dispatch/recovery correctness. Absence of invocation_sequence under Q18 creates no implicit parallel-execution permission.

Intended destination: execution-runtime consumer interface; later execution/Budget integration, without a new generic scheduler.

<a id="cg05-q25"></a>
### CG05-Q25 — MODEL durable progress is separate from outcomes and availability

Status: ACCEPTED. MODEL Invocation durable progress uses PREPARED → DISPATCH_INTENT_DURABLE → RESPONSE_DURABLE. PREPARED means the record exists without committed dispatch intent. Progress never regresses because of cancellation, parsing failure or historical payload cleanup. Known failure, ending reason and current payload availability are separate concerns; progress alone cannot decide every recovery outcome. These MODEL stages are not automatically imposed on every Tool action.

Intended destination: execution-runtime MODEL progress and Storage durable fact/availability agreement. The exact field name and full record/outcome shape remain open.

<a id="cg05-q26"></a>
### CG05-Q26 — Dispatch generation is null until intent commits

Status: ACCEPTED. dispatch_generation is null before committed dispatch intent, not 0 or a speculative future grant. The intent transaction atomically captures the then-valid execution_generation and publishes the intent. The value is immutable afterward, including when another generation performs permitted local recovery. Q16's provenance/current-owner distinction remains intact.

Intended destination: execution-runtime dispatch and Storage atomicity/reference conditions.

<a id="cg05-q27"></a>
### CG05-Q27 — A committed intent is not a reusable send permit

Status: ACCEPTED. Only the valid live execution path that won the original atomic dispatch arbitration may proceed to that request. Other paths observing an existing intent may observe, reconcile or process an eligible durable response, not invoke the adapter again. Runtime encapsulates arbitration and sending rather than returning an indefinitely reusable allow_send flag. This establishes local authorization control, not exactly-once remote execution.

Q28 permits the original still-live winning path to reconcile its own temporarily uncertain commit and continue; that is not another dispatch authorization or a second path. At that decision continuity/winner proof remained open; Q31 subsequently defines the non-transferable live-path context without requiring a new persistent token identity.

Intended destination: execution-runtime dispatch interface and deterministic duplicate-entry/race evidence.

<a id="cg05-q28"></a>
### CG05-Q28 — Preserve proven original-path continuation after uncertain commit

Status: ACCEPTED with user correction. An uncertain dispatch-intent commit acknowledgment initially prevents sending while commit truth is unresolved. The original winning path may subsequently continue the original send if it remains alive, positively establishes its own intent committed, can still prove the adapter has never begun, and retains current owner/generation/execution qualification. This does not create a new Invocation or new send permission and is not a replay.

After crash, owner/generation change, loss of original-path continuity, or inability to prove the adapter has not started, observing an intent cannot authorize sending. Apply conservative recovery to the durable boundary. Being in the same process/runtime instance and seeing the same generation is not by itself proof of being the unique original winning path. If non-commit and no-send are both established, any further attempt must pass the applicable admission/arbitration rather than infer permission from the failed write.

SUPERSEDED proposal fragment: permanently stopping the original path solely because commit acknowledgment was once uncertain, even after that same qualified path proves commit and no-send. Q27's ban on reusing intent from a second path remains effective. Q10 similarly reconciles durable facts, but its response-persistence scenario must not be confused with authorization to send a request.

Boundary examples: live winning path → uncertain acknowledgment → confirmed own committed intent/no adapter entry/current authority → original send may continue. Crash or takeover → persisted intent/no complete response → no send merely from reading the intent. No new Provider retry, fallback or authorization reconstruction is permitted.

Intended destination: execution-runtime dispatch/reconciliation, Storage commit-truth interface and deterministic fault/race evidence. No blanket architectural replay permission changes.

<a id="cg05-q29"></a>
### CG05-Q29 — Revoked callbacks cannot publish recoverable response bodies

Status: ACCEPTED. A callback whose execution qualification was revoked cannot publish the complete recoverable response, advance execution progress or resume business processing. Initial delivery does not separately retain that late callback's full response body. Trusted correlation, arrival facts and usage may enter a separately constrained audit/accounting path; they do not restore authority or overwrite the execution result. Budget remains responsible for cost/exposure interpretation.

This does not delete a response validly committed before revocation. Q35 subsequently defines the response-publication/cancellation race agreement. Q89 permits read-only confirmation of an identical existing response without restoring callback execution authority; this is not new publication or workflow progression. Q78 defers the concrete late usage subsystem to its M2 consumers.

Intended destination: execution-runtime response admission, protected Storage/audit and necessary Budget interface.

<a id="cg05-q30"></a>
### CG05-Q30 — Reconcile prior execution authority before enabling affected work

Status: ACCEPTED. After acquiring exclusive data-directory ownership, startup invalidates prior-instance execution qualifications and reconciles each affected Run against durable facts before allowing it to execute. A safe continuation obtains a new grant; uncoordinated old records cannot dispatch or publish. Unrelated local business capabilities may open according to startup composition; no exhaustive scan of all historical payloads is required merely to start the application.

Intended destination: execution-runtime startup/recovery with Workspace/Storage and deterministic startup ordering proof.

## Round 3 persistence and local review

Actual writeback: this register only. A focused reread of the current M1 plan and accepted Q1/Q2 confirms that retry_run() is not an identified delivered consumer; Q22 applies the user's non-speculative branch and preserves Q11's identity invariant. No assertion is made about unrelated ongoing implementation. Q28 narrows the earlier overly conservative recommendation without changing the crash-recovery ban: volatile original-path/no-send proof and current authority are required in addition to committed intent. Q27 cannot be implemented by treating an existing row as a transferable send permit. Q29 is checked against Q8/Q16: it rejects newly arriving stale callbacks while preserving previously admitted immutable response facts and legitimate new-owner local continuation.

Local verification checks stable decision locators, these scoped replacements, accepted versus future-only fields, local references and whitespace. No normative body, authority document, plan, Progress/readiness entry, implementation or test is changed. No full review or extra agent is used for this ordinary round.

## Round 4 — Live-Path Proof, Run Ending and Response Publication

<a id="cg05-q31"></a>
### CG05-Q31 — Unique non-transferable live send context

Status: ACCEPTED. Runtime controls one live sending path per Invocation and records whether that path has begun calling the adapter. Its one-time in-process execution qualification cannot be copied, transferred or reconstructed from database state; path exit or process crash destroys it. The same runtime_instance_id and generation alone cannot distinguish two concurrent entry paths. Implementations must prove duplicate entry cannot obtain a second sending qualification.

No new persistent dispatch_token_id is mandated. The representation may use an implementation-owned execution context, provided it proves unique arbitration/continuity and the no-adapter-entry condition required by Q28. This volatile proof supplements durable intent and current authority; it does not replace them or permit recovery to manufacture a send context for an existing intent.

Intended destination: execution-runtime dispatch/coordinator boundary and duplicate-entry/commit-uncertainty evidence.

<a id="cg05-q32"></a>
### CG05-Q32 — Minimal open versus ended Run lifecycle

Status: ACCEPTED. run_status is OPEN or ENDED. OPEN may be awaiting a grant, executing, or awaiting safe recovery; owner/generation and other applicable admission decide whether execution is permitted. ENDED cannot acquire execution authority or reopen. Safe same-Run continuation occurs only while the original Run remains open. Ending reason is separate and remains to be specified; neither a non-null owner nor OPEN alone establishes complete semantic call admission.

Intended destination: execution-runtime minimum Run shape, transitions and Storage integrity.

<a id="cg05-q33"></a>
### CG05-Q33 — In-flight progress does not itself establish an unknown outcome

Status: ACCEPTED. DISPATCH_INTENT_DURABLE without a response can describe a healthy in-flight request as well as interrupted work. Do not derive OUTCOME_UNKNOWN solely from that progress value. The valid live path continues observing its result; interruption, loss of path or recovery facts determine when the outcome must be treated as unknown. Durable progress and final interpretation remain separate.

Intended destination: execution-runtime observation/recovery/result interpretation and evidence.

<a id="cg05-q34"></a>
### CG05-Q34 — Run cancellation differs from old-owner cleanup

Status: ACCEPTED. A legitimate explicit cancellation targets the entire Run: it atomically ends the Run and revokes its current execution qualification, without requiring the cancelling consumer to provide the execution generation. Runtime handles the actual current qualification within the transaction. By contrast, an old executor's exit/cleanup targets its expected owner and generation and cannot revoke a newer grant. Neither operation is an unconditional generic clear-owner write.

This scopes Q15's stale-owner revoke condition rather than allowing delayed executor cleanup to cancel replacement authority. Run-wide cancellation and generation-scoped cleanup have different admitted intent; both retain atomic race arbitration and Q5's no-increment-on-revocation rule.

Intended destination: execution-runtime internal cancel/revoke operations and Storage conditional writes.

<a id="cg05-q35"></a>
### CG05-Q35 — Response publication and revocation arbitrate atomically

Status: ACCEPTED. The atomic commit ordering decides the response-versus-cancel/revoke race. A response validly committed first remains immutable evidence; subsequent cancellation may still stop unfinished business processing. If cancellation or revocation commits first, the former callback cannot publish its response and follows Q29. An out-of-transaction qualification check followed by an unconditional response write is insufficient. Later cancellation does not erase prior valid response publication.

Intended destination: execution-runtime response/cancel agreement, Storage atomicity and concurrency proof.

<a id="cg05-q36"></a>
### CG05-Q36 — Consumer publication checks fencing at its atomic write boundary

Status: ACCEPTED. Application-owned canonical result publication must validate current Run qualification, matching generation and consumer-required source/permission conditions within the same transaction or equivalent atomic commit boundary as the business write. A successful earlier Runtime check is not a permanent permit. Application retains business validation/commit authority; Runtime supplies the necessary execution-authority conditions.

This concerns actual Run-produced canonical results; it does not move independent Candidate Save, user confirmation or platform-effect ownership into the Invocation foundation. Concrete consumer transaction/result-reconciliation interfaces still require closure.

Intended destination: execution-runtime consumer publication seam and necessary Storage agreement.

<a id="cg05-q37"></a>
### CG05-Q37 — Consumer-established deadline is not extended by recovery

Status: ACCEPTED with user correction. deadline_at is a finite cutoff once the actual consumer determines and persists it; that established deadline must not be extended or reset by recovery. Use Common's UTC timestamp representation. M1 does not equate it with Run creation time plus timeout and does not select a universal timeout duration.

The actual consumer Contract defines when the deadline is established and whether queueing, dependency waiting and other phases count. Record creation alone does not decide those product/resource semantics. The representation before establishment and required consumer admission gate remain to be specified; this decision does not authorize unlimited execution or a generic deadline-editing operation. Clock-change and process-local timing details remain open.

SUPERSEDED proposal fragment: always determining deadline_at at Run creation. Preserve the non-extension/recovery invariant without silently charging every pre-execution wait to the same budget. The correction requires no ordinary-round Product, Architecture or Plan writeback because it leaves their existing consumer-owned limits intact.

Intended destination: execution-runtime deadline representation/enforcement and explicit later-consumer timing agreement.

<a id="cg05-q38"></a>
### CG05-Q38 — Commit-truth reconciliation is bounded

Status: ACCEPTED. Local reconciliation of uncertain commit truth has finite attempt/time bounds. Exhaustion preserves uncertainty and stops dependent execution rather than guessing success/rollback or calling the Provider. Concrete bounds are execution configuration, not a permanent three-attempt rule or a new Policy entity. Distinguish this local read/reconciliation activity from another remote call or a Run-level retry.

Intended destination: execution-runtime recovery results, Storage reconciliation and deterministic exhaustion proof.

<a id="cg05-q39"></a>
### CG05-Q39 — Complete response becomes atomically visible with its durable dependencies

Status: ACCEPTED. RESPONSE_DURABLE cannot become visible before complete payload and required recovery metadata are reliably stored and published together as a coherent response. Do not publish that progress and asynchronously fill in the body. Physical database-versus-file representation is not selected here; file existence alone would not establish response publication. Incomplete usage stays independent under Q9 rather than blocking an otherwise complete recoverable response.

Intended destination: execution-runtime response boundary and Storage atomic visibility/durability.

<a id="cg05-q40"></a>
### CG05-Q40 — Response equality excludes separate observations

Status: ACCEPTED. Idempotent response equality compares its format version and complete business payload, including necessary terminal information. Independently evolving usage, receiving/recording timestamps and other separate audit observations do not manufacture a different response. Usage updates use their separate interface and never mutate the original business response.

Structural object-key ordering has no business meaning; array order and text remain exact. Do not trim, summarize or use semantic similarity. Text containing apparent JSON is still text unless the owned representation explicitly defines a structured value; this rule does not authorize reinterpretation of raw business output. Full encoding/shape details remain to be closed; Q45–Q47 subsequently require one deterministic persisted UTF-8 serialization per versioned response format, distinct from SQLite physical representation.

Intended destination: execution-runtime response equality/codec interface, shared canonical conventions where applicable, and Storage immutable response versus usage/audit separation.

## Round 4 persistence and local review

Actual writeback: this register only. Q37 preserves the user-approved non-extension rule and leaves establishment/wait accounting to the consumer; no default create-time deadline is carried into the next shape decisions. Q31 supplements Q28's positive continuity proof instead of making persisted intent a new sending permit. Q34/Q35 preserve grant-only generations and distinguish Run-wide cancel from stale-owner cleanup. Q36 places fencing at the actual canonical commit seam. Q39/Q40 preserve Q7–Q10's complete payload, immutable result, separate usage and commit-truth boundaries.

Local checks cover decision IDs, corrected versus effective deadline wording, accepted scope, local references and whitespace. No normative Contract, high-level owner, plan, Progress/readiness, implementation or test is changed; no agent review, installation or migration is performed.

## Round 5 — Run Ending, Stable Response Bytes and Cleanup Scope

<a id="cg05-q41"></a>
### CG05-Q41 — Null deadline before consumer-defined establishment

Status: ACCEPTED. deadline_at may be null while the consumer has not yet established its deadline; null is not unlimited execution permission. The actual consumer must define the admission stage requiring a determined deadline, and Runtime enforces that gate. M1 does not universally count queueing/dependency waiting or bypass execution limits because the field is null.

Intended destination: execution-runtime nullable deadline and explicit consumer admission agreement.

<a id="cg05-q42"></a>
### CG05-Q42 — Run ending reason is separate from invocation facts

Status: ACCEPTED. end_reason is null before Run ending and required at ending, from COMPLETED, FAILED, CANCELLED, TIMED_OUT or OUTCOME_UNKNOWN. It explains why the Run ended, not every Invocation's remote certainty or business result. Cancellation does not prove remote non-execution; COMPLETED requires the consumer's completion conditions, not merely response arrival. Arbitration/precedence among competing reasons remains open.

Intended destination: execution-runtime Run ending shape and consumer completion boundary.

<a id="cg05-q43"></a>
### CG05-Q43 — Creation and ending timestamps only

Status: ACCEPTED. Run lifecycle timestamps initially comprise immutable created_at and nullable ended_at, using Common's UTC timestamp type. Ended_at is published atomically with ending information and does not change afterward. Recovery does not reset creation time. No generic updated_at or execution-grant history table is introduced without an actual consumer. Q119 subsequently closes wall-clock rollback handling without inferring causal order from timestamps.

Intended destination: execution-runtime Run shape and Storage event atomicity.

<a id="cg05-q44"></a>
### CG05-Q44 — Cancellation observes an already ended Run without rewriting it

Status: ACCEPTED. Repeated or delayed cancellation of an ended Run returns an already-ended result with the original ending information. Do not rewrite ending reason/time, revoke or grant again, or advance generation. This internal operation's idempotence does not introduce a client request_id or generic receipt table.

Intended destination: execution-runtime internal cancellation results and conditional updates.

<a id="cg05-q45"></a>
### CG05-Q45 — Versioned JSON response with deterministic per-format serialization

Status: ACCEPTED with the user's Q46/Q47 refinement. Complete response payload uses a strict bounded UTF-8 JSON object whose exact logical shape is owned by its versioned response format. Text output stays in explicit strings unless its owner defines structured data; arbitrary SDK objects and implicit binary serialization are excluded. A real future binary/special-type consumer must define its encoding explicitly.

Each versioned response format must define a unique deterministic persistence serialization for its logical payload. It cannot leave key order, whitespace, escaping or other byte-affecting choices to incidental serializer defaults. There is no newly introduced general canonical-JSON framework and no requirement that all providers expose the same business fields. Q40's array/text fidelity and separate usage/audit observations remain effective.

SUPERSEDED proposal fragment: interpreting the original no-fixed-key-order/indentation wording as permission for arbitrary persisted bytes for the same format and logical payload. M1 need not choose one universal JSON layout, but a selected response format must determine its own exact bytes. The concrete per-format serialization specification and versioning agreement remain to be completed.

Intended destination: execution-runtime response-format interface and Storage byte representation.

<a id="cg05-q46"></a>
### CG05-Q46 — Integrity metadata covers the exact deterministic serialized payload

Status: ACCEPTED with user refinement. Store sha256 and byte_length for the exact deterministic UTF-8 serialized payload produced under Q45's versioned format. These are actual byte-integrity values, not business fingerprints or response identities. Verify recovered bytes against them. Equal hashes cannot merge different Invocation response relationships; idempotent response equality retains Q40's format/content semantics.

The authoritative serialization boundary is logical complete response → format-defined deterministic UTF-8 bytes → length/hash and storage. Re-serializing an equivalent JSON object with different incidental key order/spacing is not a substitute for recovering and validating those bytes. A codec change affecting bytes under the same format must not silently alter the historical representation.

Intended destination: execution-runtime response metadata and Storage integrity/codec agreement.

<a id="cg05-q47"></a>
### CG05-Q47 — SQLite initial storage preserves the format-defined byte representation

Status: ACCEPTED with user refinement. Initial delivery stores complete response payload in the existing jobhunter.sqlite3 and commits payload, necessary metadata and durable response progress together. Physical tables and TEXT/BLOB choice remain implementation details, but the stored/read representation must preserve and recover the same format-defined UTF-8 payload bytes used for Q46 integrity checks. Database encoding or conversion choices cannot redefine the hashed serialization.

No separate response-file publication protocol is introduced for speculative large responses. A later actual large-payload consumer requires scoped extension review; Materials artifact file storage remains independent.

Intended destination: Storage response persistence/atomicity and execution-runtime publication interface.

<a id="cg05-q48"></a>
### CG05-Q48 — Finite response-size limit captured before dispatch

Status: ACCEPTED. Snapshot a finite max_response_bytes for each Invocation before dispatch so changing defaults during execution/recovery cannot silently change that call's storage constraint. Concrete initial values require implementation evidence; no permanent MiB constant is selected. Exceeding the bound cannot silently truncate output and claim a complete durable response or automatically call the Provider again. Failure classification against actually known remote facts remains to be closed.

Intended destination: execution-runtime bounded response admission and Storage representation limits.

<a id="cg05-q49"></a>
### CG05-Q49 — Conservatively protect all response payloads of an open Run

Status: ACCEPTED. Initial M1 protection retains all response payloads belonging to OPEN Runs and is based on persisted relationships. Invocation completion alone does not release that protection. Ending the owning Run removes this particular protection but does not itself delete payload; any deletion must satisfy a real admitted retention/cleanup consumer's rules. No step-level release, independent Pin business entity or reference-count service is introduced now. Actual cross-Run recovery dependencies require their first consumer's explicit extension.

This does not promise permanent retention for every ended Run. The delivery-depth branch was conditional under Q50 and is subsequently resolved by Q51: M1 delivers recovery protection, while an actual purge consumer is deferred.

Intended destination: Storage active recovery protection and execution-runtime ending/dependency agreement.

<a id="cg05-q50"></a>
### CG05-Q50 — Conditional purge representation pending delivery-depth closure

Status: RESOLVED — the original conditional proposal is deferred by CG05-Q51. Historical condition: the user required checking whether M1 actually delivers a payload cleanup consumer. Do not unconditionally add payload_retention = RETAINED | PURGED merely to reserve future structure. If M1 has no operation that can legitimately purge payload, defer that field and its transitions to the first actual cleanup consumer while preserving Q49. If M1 delivers an actual cleanup operation, the proposed distinction between intentional purge and unexpectedly missing/corrupt retained bytes remains applicable and needs the full operation/transaction agreement.

Focused source check: the M1 plan's required Storage portions explicitly include active recovery dependencies and cleanup; the shared readiness row likewise names pins/cleanup. However, the M1 Scope names active payload retention and identifies no purge entry point, trigger or concrete retention policy. Architecture §13 and the Storage provenance defer cleanup timing, representation and exact coordination, while global Acceptance includes eventual cleanup proof. Thus no-code is not evidence of out-of-scope, but the existing cleanup reference also does not establish a fully specified M1 purge feature.

At Round 5, the remaining M1 delivery-depth decision was carried to Q51. Q51 subsequently selects protection-only delivery and defers the RETAINED/PURGED field and actual purge operation. Never interpret deferral as permission to mislabel corruption, fabricate historical payload, replay a Provider request, or permanently erase the later cleanup obligations.

Intended destination if consumed: Storage cleanup/disposition and execution-runtime historical read agreement. If deferred: explicit future scope and no speculative field. Any required plan/readiness-scope reconciliation follows the user's authorized writeback process, not this ordinary round.

## Round 5 persistence and focused consistency review

Actual writeback: this register only. Q45–Q47 now separate logical JSON equality, format-owned deterministic serialization, actual byte-integrity metadata and SQLite physical representation. Object-key ordering is not business identity under Q40, but its persistence bytes are fixed by the selected versioned codec; stored hashes are not recalculated from a newly chosen serializer to conceal byte changes. Q41 preserves consumer-owned deadline establishment and Q42–Q44 preserve immutable Run ending.

One narrowly scoped read-only agent checked only Q50's cleanup-delivery condition against the Slice plan, scope ledger, Structure and existing Storage/Acceptance boundaries. It confirmed the delivery-depth ambiguity above, not a new implementation fact or whole-document review. This factual result does not decide the branch for the user. No file other than this register is changed; no normative publication, status/readiness advancement, implementation, installation, migration or runtime test occurs.

## Round 6 — Failure Ownership, Response Formats and Deadline Recovery

<a id="cg05-q51"></a>
### CG05-Q51 — M1 protects recovery payloads without delivering purge

Status: ACCEPTED. Select protection-only delivery for M1: preserve Q49's active recovery dependencies, but defer an actual payload purge operation and payload_retention = RETAINED | PURGED to the first real cleanup consumer. Terminal payloads remain retained in this delivery; this is not a permanent retention guarantee or authorization for out-of-band deletion. Q50's conditional branch is now resolved without introducing an unreachable PURGED state.

At authorized closure, reconcile the plan and consumed readiness scope so that references to cleanup do not claim a delivered purge feature or review of the whole future cleanup scope. Unexpectedly missing/corrupt bytes remain failures, never an implied intentional purge. Existing receipt and Materials retention semantics are unaffected.

Intended destination: Storage active recovery protection and explicit future cleanup scope; necessary plan/readiness reconciliation at authorized closure.

<a id="cg05-q52"></a>
### CG05-Q52 — Atomic Run field consistency

Status: ACCEPTED. An OPEN Run has null end_reason and ended_at; its owner may be null or hold current qualification. An ENDED Run has null owner_runtime_instance_id and non-null end_reason and ended_at. Ending atomically publishes the ending fields and removes execution qualification while retaining the last execution_generation. An ENDED Run with generation zero is valid when cancelled before any execution grant. No ending transition advances the generation or reopens the Run.

Intended destination: execution-runtime Run shape/invariants and Storage ending atomicity.

<a id="cg05-q53"></a>
### CG05-Q53 — Failure codes belong to Runtime and Invocation

Status: ACCEPTED with user refinement. failure_code is nullable, required for end_reason = FAILED and null for OPEN Runs or other ending reasons. It identifies only a stable failure cause owned by the Runtime/Invocation layer. Do not persist raw exceptions, response bodies or mutable diagnostic prose in this field, or turn AgentRun into a universal taxonomy of consumer business failures.

DeepFit validation failures, Requirement parsing results and other domain outcomes remain defined and stored by their consumer Contracts. The user's examples, including response-size, response-format availability, storage and uncertain-outcome failures, illustrate ownership boundaries rather than freezing a code enum or assigning every example to FAILED. In particular, Q42 already defines OUTCOME_UNKNOWN as an ending reason; this round does not silently duplicate it as a FAILED code. At Round 6, exact mappings and the Run completion treatment of a successfully computed negative business result remained open. Q61 subsequently closes the negative-business-result boundary; Q64/Q67/Q69 further settle specific Runtime ending classifications.

SUPERSEDED proposal interpretation: treating any consumer business failure as a Run-owned failure_code merely because it occurred during a Run. The nullable/required field invariant remains accepted; consumer outcome and runtime completion must be reconciled without silently relaxing it.

Intended destination: execution-runtime owned failure vocabulary and explicit consumer result/completion interface.

<a id="cg05-q54"></a>
### CG05-Q54 — Static versioned response-format key

Status: ACCEPTED. response_format_key identifies a statically registered, versioned response format and its logical shape, deterministic serializer and reader. Choose it before dispatch and freeze it with dispatch intent. A change to the interpretation or serialization rules requires a new key; do not rewrite historical responses using a current default. No independent Configuration entity, database format-catalog CRUD or generic serializer framework is introduced.

Intended destination: execution-runtime response-format registration and immutable dispatch/response metadata.

<a id="cg05-q55"></a>
### CG05-Q55 — Missing historical format support stops dependent processing

Status: ACCEPTED. If the installed runtime cannot read a saved response's historical format, stop dependent processing with an explicit unsupported/unavailable-format result and retain its bytes and metadata. Do not guess a current reader, relabel/rewrite the format, call the Provider again or erase the historical RESPONSE_DURABLE fact. Lack of a reader is distinct from a response that was never durably published. The failure convergence and isolation behavior are subsequently refined by Q69: an affected OPEN Run ends as FAILED with a Runtime-owned format-unavailable code; other capabilities remain available.

Intended destination: execution-runtime local recovery errors and Storage preservation of historical response facts.

<a id="cg05-q56"></a>
### CG05-Q56 — Per-format serialization conformance evidence

Status: ACCEPTED. Each actually supported response format needs byte-level golden fixtures with logical input, expected exact UTF-8 bytes, byte_length and sha256. Cover the byte-affecting cases allowed by its schema, including object ordering, escaping, Unicode, numeric representation and array order where applicable. These fixtures prove Q45–Q47's format boundary, not a new general canonical-JSON framework. No fixture implementation or test execution is claimed by this decision.

Intended destination: execution-runtime format obligations and deterministic evaluation/observability boundary proof.

<a id="cg05-q57"></a>
### CG05-Q57 — Conditional write-once deadline establishment

Status: ACCEPTED. Establish deadline_at through a conditional operation while the Run is OPEN and the field is unset. A repeat with the same established value can confirm that value idempotently; a different value is rejected. An ENDED Run cannot receive a new or changed deadline. M1 adds no deadline-editing, extension or scheduling API; cancellation remains the way to stop early. Consumer-owned establishment timing and wait accounting under Q37/Q41 remain unchanged.

Intended destination: execution-runtime deadline operation and Storage conditional-write semantics.

<a id="cg05-q58"></a>
### CG05-Q58 — Expiry blocks new remote execution without erasing durable local recovery

Status: ACCEPTED with user refinement. Enforce an established deadline at the relevant admission/publication boundaries rather than relying only on a timer callback. Once it expires, prohibit new dispatch, publication of a new response by a late old executor, and new remote side effects. An in-memory response, partial stream or response not legally made durable before expiry does not gain recovery eligibility from this exception.

For a response legally made RESPONSE_DURABLE before expiry, the actual consumer Contract determines whether deterministic local validation and canonical business submission may continue after expiry. Deadline expiry alone does not destroy that response's recovery value. Example: a response is legally persisted before the deadline, the application crashes, and restart occurs afterward; recovery must distinguish that case from another remote call or a late response publication.

Such continuation still requires current execution qualification, current permissions and applicable source/business admission. It neither revives an ENDED Run under Q32 nor restores the old executor's authority. The original deadline is not extended or reset. Q62/Q63 subsequently close restricted recovery qualification and ending arbitration; detailed operation mechanics and consumer-local bounds remain to be closed; this round does not introduce an unlimited local continuation permit.

SUPERSEDED proposal fragment: universally rejecting every canonical business submission after deadline expiry. The exception is consumer-authorized deterministic local recovery from a response legally made durable before expiry. The bans on new remote execution and late old-writer publication, and all other authority/admission checks, remain effective. Read access to existing results and separately admitted limited usage/audit observations do not create new execution authority.

Intended destination: execution-runtime deadline/recovery interface, explicit consumer continuation obligations and deterministic before/after-expiry crash proof.

<a id="cg05-q59"></a>
### CG05-Q59 — Process-local elapsed bounds and the persisted deadline have distinct roles

Status: ACCEPTED. Use process-local monotonic elapsed-time accounting alongside the established UTC deadline for execution governed by that deadline. After restart, consult the original persisted UTC deadline; do not restart a full timeout or claim that a monotonic reading from an old process establishes a new process's clock. M1 introduces no trusted-time service or guarantee against wall-clock manipulation across restart. Platform clock/sleep behavior requires implementation research where consumed.

This timing rule does not override Q58's consumer-defined local continuation. Any admitted continuation retains the original remote-execution cutoff and must have bounded local processing; exact local-bound admission remains open, rather than silently reusing a reset remote-call budget.

Intended destination: execution-runtime deadline enforcement and recovery timing proof, with platform facts in implementation research.

<a id="cg05-q60"></a>
### CG05-Q60 — Canonical business results remain with their consumer

Status: ACCEPTED. Do not add a generic result_type, result_id or business_result JSON object to AgentRun. The consumer owns canonical result identity, commit idempotence and result reconciliation. Runtime coordinates execution authority and completion, but recovery checks the consumer's actual commit/result boundary instead of inferring a business asset or business success from Run status. This does not prescribe the consumer's own result schema or duplicate Candidate Save authority.

Intended destination: execution-runtime consumer completion/reconciliation interface and consumer-owned canonical commit agreement.

## Round 6 persistence and local review

Actual writeback: this register only. Q51 resolves the conditional purge proposal as deferred delivery, leaving plan/readiness scope clarification for authorized closure. Q53 restricts failure ownership without freezing example codes or assigning domain failures to a generic Run taxonomy. Q58 partially supersedes the blanket post-deadline business-commit prohibition, while Q32/Q36/Q52 retain terminal immutability, commit fencing and current authority. Q59 preserves the original deadline across recovery without cancelling Q58's consumer-defined local continuation.

The next frontier explicitly includes runtime completion versus business invalidity and the restricted grant/admission needed for post-deadline local recovery. No normative Contract or high-level owner, plan, Progress/readiness, implementation or test is changed. Local checks cover stable decision locators, supersession scope, references and whitespace; no sub-agent, full audit, installation or migration is used this round.

## Round 7 — Recovery Failure Convergence and Consumer Boundaries

<a id="cg05-q61"></a>
### CG05-Q61 — Completed execution may produce a negative business result

Status: ACCEPTED. When a consumer successfully executes parsing/validation and produces a legitimate negative business result, use COMPLETED if its defined execution-completion conditions are satisfied. Persist the business outcome with the consumer, not as a Runtime failure_code. COMPLETED neither guarantees business success nor asserts that a particular business asset exists. Runtime-owned execution failures remain FAILED with an owned failure_code under Q53.

Intended destination: execution-runtime completion semantics and consumer-owned result agreement.

<a id="cg05-q62"></a>
### CG05-Q62 — Restricted post-deadline local recovery qualification

Status: ACCEPTED. An expired deadline does not by itself prevent a new execution grant for an OPEN Run when a response was legally made durable before expiry and the consumer explicitly permits bounded local recovery from it. Grant a new generation under the usual atomic authority rules; do not revive the prior executor. Admission permits only the authorized bounded local processing, never a new dispatch, remote side effect or deadline extension. Enforce that restriction at the applicable operations rather than treating the new generation as unrestricted execution permission.

Absent the consumer's explicit local-recovery agreement, reject that continuation. ENDED Runs cannot reopen. No independent persisted recovery-mode entity is introduced. The concrete local bounds and consumer interface must be explicit where consumed, without silently resetting the remote-execution deadline.

Intended destination: execution-runtime grant/admission interface and consumer-defined bounded local recovery proof.

<a id="cg05-q63"></a>
### CG05-Q63 — First valid committed ending wins

Status: ACCEPTED. Competing ending operations must satisfy their own admission conditions and atomically arbitrate OPEN → ENDED. The first valid committed transition determines immutable ending information. Later operations observe the existing ending result; no priority ordering permits rewriting history. Ending still clears current qualification without incrementing generation under Q52.

Preserve independently committed canonical business results and Invocation facts regardless of the ending reason. A CANCELLED or FAILED ending alone does not prove that no business result exists or no remote work occurred. This decision does not bypass consumer completion requirements, execution fencing or conditional authority checks for executor-owned endings.

Intended destination: execution-runtime ending operations, Storage concurrency and consumer result reconciliation.

<a id="cg05-q64"></a>
### CG05-Q64 — Confirmed unavailable or corrupt recovery payload ends the open Run

Status: ACCEPTED with user refinement. When a required persisted response payload is confirmed to be missing despite its retained/durable relationship, or its actual bytes fail sha256/byte_length integrity checks, stop recovery and converge the affected still-OPEN Run to FAILED using a stable Runtime-owned cause. The user's proposed classifications are RESPONSE_PAYLOAD_UNAVAILABLE for confirmed missing payload and RESPONSE_INTEGRITY_FAILED for failed byte-integrity checks. Do not leave that Run indefinitely OPEN merely because processing stopped.

Preserve existing response metadata and historical durability_phase; do not roll back to PREPARED, label the failure as intentional PURGED state, reconstruct a historical response from current data or call the Provider again. Failure ending uses the current authorized atomic ending boundary, clears execution qualification and respects Q63 if another valid ending already committed. Q72/Q73 subsequently distinguish transient storage-read failure and uncertain/unavailable failure-state persistence from confirmed response failure; neither permits claiming an uncommitted FAILED state.

Refinement of the original proposal: stopping dependent recovery is insufficient by itself; confirmed payload failure also requires Run convergence. No accepted durability or replay rule is superseded.

Intended destination: execution-runtime recovery failure/ending interface, Storage integrity classification and deterministic convergence proof.

<a id="cg05-q65"></a>
### CG05-Q65 — MODEL durability_phase names persistent facts

Status: ACCEPTED. Name the MODEL progress field durability_phase with the previously accepted PREPARED → DISPATCH_INTENT_DURABLE → RESPONSE_DURABLE values. It expresses persisted facts, not whether execution is currently running, whether business succeeded or whether payload is currently readable. Cancellation, failure and reader unavailability never regress that history. These three MODEL values do not automatically define TOOL's action-specific lifecycle.

Intended destination: execution-runtime MODEL record shape and monotonic transition invariants.

<a id="cg05-q66"></a>
### CG05-Q66 — Prepared MODEL recovery requires confirmed commit truth and fresh admission

Status: ACCEPTED. After confirming that a MODEL Invocation remains PREPARED and no dispatch intent committed, recovery may retain the same invocation_id, obtain fresh Run execution authority and pass current consumer admission before committing intent and sending. Preserve already frozen Invocation configuration and limits; this is not permission to rewrite them from current defaults.

An absent commit acknowledgement is not proof that dispatch intent is absent. If commit truth remains uncertain, this path is unavailable; apply bounded reconciliation and stop dependent execution under Q10/Q38. Once intent committed, Q27/Q28's original-live-path-only rule applies and persisted intent never becomes recovery's send permit.

Intended destination: execution-runtime prepared recovery and dispatch admission, with Storage commit-truth proof.

<a id="cg05-q67"></a>
### CG05-Q67 — Unknown remote outcome uses its dedicated ending reason

Status: ACCEPTED. When remote outcome uncertainty causes an OPEN Run to end, use end_reason = OUTCOME_UNKNOWN and failure_code = null. Do not duplicate that same classification as FAILED plus an OUTCOME_UNKNOWN failure_code. If the Run already ended for cancellation or another reason, retain the original ending information; Invocation evidence separately preserves remote uncertainty. Neither a cancelled Run nor a missing response by itself proves remote non-execution.

Intended destination: execution-runtime ending/failure vocabulary and Invocation evidence agreement.

<a id="cg05-q68"></a>
### CG05-Q68 — Response-size accounting uses the complete persisted representation

Status: ACCEPTED. max_response_bytes limits the complete deterministic UTF-8 payload serialized by the selected response format, using the same byte boundary as byte_length. Include that format's required structural and terminal information, not just output text. Transport size and finite buffering limits may be separate implementation constraints but cannot replace this bound. Do not truncate the payload and claim complete persistence. This decision does not require constructing an unbounded in-memory serialization before enforcing limits.

Intended destination: execution-runtime response-size validation and Storage format/integrity agreement.

<a id="cg05-q69"></a>
### CG05-Q69 — Unavailable historical reader fails only affected recovery

Status: ACCEPTED with user refinement. Isolate Runs/Invocations that depend on a historical response format whose reader is unavailable. Stop dependent processing and converge an affected still-OPEN Run to FAILED with a stable Runtime-owned RESPONSE_FORMAT_UNAVAILABLE classification instead of waiting indefinitely for reader support to return. Preserve original payload, response_format_key and durable history. Reader restoration does not reopen an ENDED Run.

Other capabilities that do not depend on that format may open normally. Missing reader support alone neither establishes database corruption nor requires whole-application startup failure. Apply current authority and Q63's atomic ending arbitration; an already ended Run is not rewritten. As with Q64, failure to persist the ending must not be misreported as a committed FAILED state.

Refinement of Q55 and the original isolation proposal: affected OPEN Runs require an ending result, not merely an indefinite isolated wait. Whole-application isolation and historical preservation rules remain unchanged.

Intended destination: execution-runtime format availability/failure convergence, startup isolation and Storage payload preservation.

<a id="cg05-q70"></a>
### CG05-Q70 — Tool replay requires the concrete action's recovery agreement

Status: ACCEPTED. M1 requires a concrete Tool action to supply its applicable completion evidence, result reconciliation method and re-execution permission conditions before replay can be admitted. Default to denying re-execution when the agreement or required evidence is absent. A query-like name or a shared Invocation identity does not prove repeat safety.

Actual permissions, budget and business side effects remain owned by the Tool and its consumer. M1 neither supplies a universal retry mechanism nor defines one shared lifecycle for all Tools. Concrete action interfaces remain to be specified only to the depth actually consumed by this milestone.

Intended destination: execution-runtime Tool recovery extension seam and consumer-owned action/replay obligations.

## Round 7 persistence and local review

Actual writeback: this register only. Q64/Q69 incorporate the user's explicit convergence requirement: confirmed required payload loss/corruption and unavailable historical readers end affected OPEN Runs through Runtime-owned FAILED causes. These transitions preserve immutable response history, forbid remote replay and respect an already committed ending. Q61 separates negative business results from Runtime failures, while Q62 preserves bounded local recovery under new authority and the unchanged original deadline.

Local consistency checks cover the prior failure-code nullability, grant-only generation advancement, Q63 ending arbitration, Q51's absence of purge, and preservation of Q27/Q28 dispatch safety. The next frontier distinguishes confirmed unavailable data from temporarily unreadable storage, and requested failure convergence from a failure transaction whose commit truth is unknown. No authority-document writeback, readiness advancement, implementation, runtime test, sub-agent or full audit is performed.

## Round 8 — Result Reconciliation, Storage Truth and Consumer Binding

<a id="cg05-q71"></a>
### CG05-Q71 — Reconcile committed consumer results without bypassing Run authority

Status: ACCEPTED with user refinement. First use the consumer-owned reconciliation interface to determine whether its canonical result has already committed and satisfies its execution-completion conditions. If so, skip unnecessary response reads/parsing, repeated business validation and duplicate business submission. Response availability must not become an artificial prerequisite for acknowledging an already committed result. Independently report response integrity problems where applicable without denying the committed business fact.

The result's existence does not authorize an arbitrary Run update. Converging a still-OPEN Run to COMPLETED requires lawful recovery execution qualification or a dedicated authorized atomic reconciliation boundary. That boundary must check current Run state and applicable generation/fencing predicates before atomically ending it; Q63's existing-ending arbitration remains effective. Do not let a stale executor use business-result existence to bypass current authority. This is result reconciliation, not permission to perform new business work or reopen an ENDED Run.

Refinement of the original proposal: skipping response processing never means skipping recovery arbitration. Exact internal coordination operation mechanics remain to be closed. This accepted result-only reconciliation is distinct from Q62's response-dependent local continuation and does not inherit an unnecessary payload-read prerequisite.

Intended destination: execution-runtime consumer result reconciliation/completion interface, atomic ending authority and deterministic post-business-commit crash proof.

<a id="cg05-q72"></a>
### CG05-Q72 — Unreadable storage is not confirmed missing payload

Status: ACCEPTED. A busy database, failed read or unresolved commit truth is not evidence that payload is absent. Use Q64's missing-payload classification only after a trustworthy read confirms absence where retained payload is required; use its integrity classification only after checking actual recovered bytes against length/hash. Temporarily unreadable storage follows bounded reconciliation. If its bound is exhausted, explicitly report storage unavailability or unresolved reconciliation and stop dependent execution rather than inventing RESPONSE_PAYLOAD_UNAVAILABLE.

Intended destination: Storage read/error semantics and execution-runtime bounded recovery classification.

<a id="cg05-q73"></a>
### CG05-Q73 — Failure convergence must itself be durably truthful

Status: ACCEPTED. If a required FAILED ending cannot be persisted, immediately stop the current path's further execution and remote sending, but do not claim the Run is durably FAILED. If commit acknowledgement is uncertain, reconcile the ending transaction within the existing finite bounds. Unresolved truth is reported as storage blockage/commit uncertainty, not a guessed success or rollback.

Once storage is available, reconcile against actual persisted Run state and finish the required coordination under current authority where still applicable. Never call the Provider again to resolve the local failure, and never overwrite another ending that already committed. This distinction qualifies the liveness obligations in Q64/Q69: a stored terminal outcome cannot be promised while its storage boundary is unavailable; local execution must nevertheless stop.

Intended destination: execution-runtime internal operation results, Storage uncertain-ending handling and fault proof.

<a id="cg05-q74"></a>
### CG05-Q74 — Invalid response format is not consumer business invalidity

Status: ACCEPTED. When exact bytes pass integrity checks and the selected reader exists, but the payload violates that response format's structural/encoding protocol, end the affected OPEN Run through Runtime-owned FAILED with RESPONSE_FORMAT_INVALID. Preserve the original evidence and apply normal authority/ending arbitration.

This code covers the response envelope/format protocol only. Invalid Requirement content inside a valid output string remains the consumer's domain validation result under Q61, not a Runtime format failure. Reader absence remains RESPONSE_FORMAT_UNAVAILABLE; failed length/hash checks remain RESPONSE_INTEGRITY_FAILED.

Intended destination: execution-runtime format validation/failure vocabulary and consumer-owned content interpretation.

<a id="cg05-q75"></a>
### CG05-Q75 — Dispatch requires known response-format read and write support

Status: ACCEPTED. Before dispatch, verify support for the selected response format's serializer and reader. If either is known to be unavailable, do not send; end the affected OPEN Run with Runtime-owned RESPONSE_FORMAT_UNAVAILABLE through the authorized ending boundary. A preflight check does not guarantee dependencies remain available throughout execution or restart; later loss follows the accepted response/recovery failure rules.

Intended destination: execution-runtime pre-dispatch admission and deterministic no-send proof.

<a id="cg05-q76"></a>
### CG05-Q76 — Known complete response rejected for size is a local failure

Status: ACCEPTED. When the remote protocol is known to have completed and the complete response exceeds the persisted representation's size limit, end the affected OPEN Run as FAILED with RESPONSE_TOO_LARGE. Durably record the observed remote completion and local rejection cause through the applicable authorized persistence boundary. This is not OUTCOME_UNKNOWN merely because the response cannot be accepted into durable payload storage.

Do not publish RESPONSE_DURABLE, truncate output or retry the Provider. If remote completion is genuinely uncertain, preserve that uncertainty rather than claiming a known completion. Q99 explicitly confirms that stopping an oversized stream before a complete terminal result is known does not qualify for this RESPONSE_TOO_LARGE evidence. Usage/cost information remains separately owned and is not assumed to be zero or settled by this classification. Q73 governs inability to persist the failure evidence/ending itself. Q87 subsequently defines the minimum Invocation-level response_rejection_code for this known rejection.

Intended destination: execution-runtime size rejection and canonical Invocation evidence, with atomic persistence and failure proof.

<a id="cg05-q77"></a>
### CG05-Q77 — One dispatch authorization does not hide multiple model requests

Status: ACCEPTED. A dispatch authorization permits at most one actual Model request. Adapter/SDK-internal retries, fallback or repair must not hide extra requests behind one admitted call. Any additional request requires explicit consumer authorization and a newly admitted Invocation; a Run-level retry is not implied. This preserves the inherited no-silent-replay boundary without claiming remote exactly-once execution.

M1 proves the boundary with controlled adapters. The actual SDK's configuration and behavior require evidence when a real integration is delivered; a single mocked method call is not proof that a production SDK cannot retry underneath it.

Intended destination: execution-runtime adapter invocation boundary and deterministic evidence, with real SDK proof owned by actual integration.

<a id="cg05-q78"></a>
### CG05-Q78 — M1 late-callback fencing does not deliver the usage subsystem

Status: ACCEPTED. M1 defines and proves that a late/revoked callback cannot publish a response, advance execution or complete an Intent/business workflow. Preserve an extension seam for separately admitted limited observations, but defer concrete late usage ingestion, deduplication, merge and settlement to SL-03.M2's actual consumers. Do not introduce a generic late-event table or arbitrary JSON container in M1.

This narrows delivery depth, not the truthfulness or fencing obligations in Q9/Q29/Q58. Permitting a future bounded usage/audit observation does not itself claim that M1 implements its full protocol, budget ledger or settlement. Materials Intent ownership remains outside this Runtime foundation.

Intended destination: execution-runtime late-callback/extension boundary and accurate M1 versus M2 consumed-scope mapping at authorized closure.

<a id="cg05-q79"></a>
### CG05-Q79 — Immutable consumer key selects an owned recovery interface

Status: ACCEPTED. Add immutable consumer_key to AgentRun, referencing a concrete consumer recovery interface statically registered in code. An incompatible consumer recovery protocol uses a new key where needed. The consumer owns completion conditions, canonical-result reconciliation and recovery admission; the key does not copy business results into Run or redefine their authority.

Do not introduce a database-editable workflow registry or generic workflow engine. Actual key syntax, missing-handler behavior and the minimal interface operations remain to be closed for the consumed scope. Registration is not evidence that a later consumer is implemented or ready.

Intended destination: execution-runtime Run shape and static consumer binding/recovery interface.

<a id="cg05-q80"></a>
### CG05-Q80 — Forward migration from the actual implementation-time head

Status: ACCEPTED. Reinspect the actual migration head when implementation begins and add a forward migration preserving existing data and references. Do not freeze a currently observed schema number into the business Contract or rewrite a published historical migration. Do not synthesize AgentRun/Invocation records for historical Resume, Materials or other pre-existing business records. Concrete revision identifiers belong in implementation and handoff evidence at that time.

Intended destination: Storage migration preservation/applicability and implementation handoff; no migration is created or executed by this decision.

## Round 8 persistence and local review

Actual writeback: this register only. Q71 incorporates the user's explicit authority qualification: committed consumer results remove unnecessary payload work, not generation/fencing or atomic ending arbitration. Q72/Q73 distinguish confirmation of data loss from failed reads and distinguish a required failure ending from a known committed ending. Q74/Q76 preserve domain-versus-Runtime failure ownership and known-versus-unknown remote completion. Q78 keeps late usage subsystem delivery with its actual M2 consumer, while Q79 establishes only the minimum static recovery binding.

Local review checks these decisions against Q5/Q15/Q32/Q36/Q52/Q63, immutable response phases, Q64/Q69 convergence and Q60's consumer-owned results. The newly recorded consumer_key and response rejection evidence leave explicit shape/interface branches below; no guessed implementation fields are introduced. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified; no agent, full audit, installation or migration is used.

## Round 9 — Run Shape, Coordination and Existing-Response Confirmation

<a id="cg05-q81"></a>
### CG05-Q81 — M1 Run execution-control projection

Status: ACCEPTED. M1's consumed Run execution-control projection has ten required fields. Nullable fields are present with explicit null, not omitted.

| Field | Nullability |
| --- | --- |
| run_id | Non-null |
| consumer_key | Non-null |
| run_status | Non-null |
| execution_generation | Non-null |
| owner_runtime_instance_id | Nullable |
| deadline_at | Nullable |
| created_at | Non-null |
| ended_at | Nullable |
| end_reason | Nullable |
| failure_code | Nullable |

Apply the previously accepted identity, immutability, generation, deadline and ending invariants. This projection does not predefine all future Skill, Context or Budget fields; later actual consumers require explicit extensions. No arbitrary JSON extension container is added.

Intended destination: execution-runtime M1 Run shape and consumed-versus-future scope boundaries.

<a id="cg05-q82"></a>
### CG05-Q82 — Missing consumer recovery handler ends affected open Runs

Status: ACCEPTED. If an existing Run's consumer_key has no available registered recovery handler, do not guess a substitute. End the affected OPEN Run through lawful coordination as FAILED with CONSUMER_UNAVAILABLE, preserving its key, Invocations and payloads. Other consumers can operate normally; this missing handler alone does not require application startup failure. Restoring the handler does not reopen an ENDED Run.

Intended destination: execution-runtime consumer availability, startup isolation and failure vocabulary.

<a id="cg05-q83"></a>
### CG05-Q83 — Restricted atomic ending coordination for an unowned Run

Status: ACCEPTED. The current lawful Workspace Runtime may perform a restricted reconciliation ending for an unowned Run. Atomically require OPEN, owner_runtime_instance_id = null and the expected execution_generation, and derive the ending from confirmed consumer completion or Runtime-owned failure facts. This is an authorized coordination boundary under Q71, not permission for arbitrary callers to update Run state.

The operation grants no execution authority, does not advance generation and cannot dispatch, publish a response or submit a new business result. If a new grant or another valid ending commits first, coordination fails its conditions or returns the existing ending as appropriate. Missing handlers/readers can therefore converge without granting an unusable normal execution path. Q73 still governs ending commit uncertainty.

Intended destination: execution-runtime reconciliation operation, Storage conditional ending and race proof.

<a id="cg05-q84"></a>
### CG05-Q84 — Creation uncertainty retains the allocated identity

Status: ACCEPTED. Runtime allocates a Run/Invocation UUID before its creation transaction and retains it throughout that logical creation's commit-truth reconciliation. If acknowledgement is uncertain, inspect the original identity and expected immutable content. Do not generate a different UUID and create another record or advance dependent execution before establishing the original transaction's truth. This internal creation agreement adds neither a public request_id nor a generic receipt system.

Intended destination: execution-runtime internal creation inputs/results and Storage creation uncertainty.

<a id="cg05-q85"></a>
### CG05-Q85 — Uncertain grant acknowledgement needs proof of the winning path

Status: ACCEPTED. After an uncertain execution-grant acknowledgement, only the still-live original arbitration path that can establish its own grant committed and remains valid may proceed. Merely observing matching persisted owner/generation values does not prove that another in-process path won that grant. If continuity or ownership of the winning operation cannot be established, stop execution and let Runtime safely arbitrate again; do not adopt the observed qualification by inference.

No generic grant-receipt entity is introduced. This is distinct from Q28's dispatch-intent continuity rule, but preserves the same separation between persisted facts and a particular path's authorization to act. Recovery after a lost path still follows revocation/regrant rules, not reconstruction of the old path from database values.

Intended destination: execution-runtime grant uncertainty/qualification and deterministic no-duplicate-owner proof.

<a id="cg05-q86"></a>
### CG05-Q86 — Defer a separate response durability timestamp

Status: ACCEPTED user correction — defer response_durable_at. M1 does not add this field merely for potential audit value. Its current recovery correctness relies on the legally established RESPONSE_DURABLE fact, payload/hash/length integrity, atomic publication and applicable deadline/generation admission. A later actual observability/audit consumer may introduce a timestamp with its own meaning and consumption requirements.

REJECTED proposal: adding immutable response_durable_at in the response publication transaction solely as additional deadline/provenance evidence. Do not imply that the proposed field was previously published or implemented. This deferral does not weaken publication admission or permit inferring validity from Provider timestamps.

Focused read-only source check: current Acceptance §9.2, Architecture §12 and Harness recovery provenance require complete durable response, eligibility/deadline checks and fencing, but do not consume a separate response_durable_at for a recovery decision. Architecture §13's generic audit timing does not prescribe this field. No execution-runtime normative body exists yet; its final consumed atomic protocol remains to be published through this Grill's closure.

Intended destination: execution-runtime minimum response shape; future audit scope only when actually consumed.

<a id="cg05-q87"></a>
### CG05-Q87 — Minimal MODEL evidence for a known complete size rejection

Status: ACCEPTED. Add nullable response_rejection_code to MODEL Invocation. M1 initially supports RESPONSE_TOO_LARGE only for an observed complete remote response that cannot be accepted because of its persisted size bound. Atomically record it with the corresponding Run's FAILED ending. Keep durability_phase = DISPATCH_INTENT_DURABLE and do not manufacture RESPONSE_DURABLE or persist the oversized body.

This records which Invocation had a known completion rejected locally, not a universal Invocation outcome taxonomy or a new terminal state machine. It does not cover an incomplete/unknown stream or automatically supply future Provider failure codes. Q99 makes confirmed complete remote termination an explicit prerequisite; merely crossing a receive/buffer threshold is insufficient. Q73 preserves truthful behavior when the evidence/ending transaction cannot be confirmed.

Intended destination: execution-runtime MODEL evidence shape, Storage atomic rejection/ending and deterministic size-failure proof.

<a id="cg05-q88"></a>
### CG05-Q88 — Deterministic boundary proof uses actual Runtime and persistence

Status: ACCEPTED. M1 conformance exercises actual execution and durable persistence components with controlled adapters and bounded fault injection. Required scenarios include crashes before/after dispatch, restart after response persistence, stale executor submissions, cancellation races, lost commit acknowledgements, corrupt payload, missing reader and reconciliation of a committed consumer result. Pure in-memory state-machine mocks cannot substitute for persistence/restart/fencing proof.

This does not require a real business Skill or production Provider integration in M1. Controlled adapter evidence must not be presented as proof of production SDK behavior, semantic quality or a delivered later consumer. Test implementation and execution remain future work.

Intended destination: deterministic evaluation/observability consumed scope and implementation verification obligations.

<a id="cg05-q89"></a>
### CG05-Q89 — Existing-response confirmation is separate from first publication

Status: ACCEPTED with user correction. After validating inputs and reference relationships, determine whether the Invocation already has a durable response. If it does, an identical response returns the original publication result without new writes; a different response produces an integrity conflict and preserves the original. Read-only confirmation does not require the Run to remain OPEN, the original execution generation to remain current or its deadline to remain unexpired. It acknowledges an existing immutable fact, not a fresh publication or permission to continue execution.

If no durable response exists, enforce Run OPEN, current owner/generation qualification, applicable deadline and consumer admission, then format/size validity and atomic first publication. Checks of mutable admission facts must hold at the write boundary. Q8's at-most-one-response invariant remains effective.

SUPERSEDED original Q89 proposal fragment: checking ENDED/current qualification/deadline before recognizing every identical existing response, including a pure confirmation after the original acknowledgement was lost. This also partially supersedes an overbroad interpretation of Q8's admission sentence, now annotated there. Q29/Q35 remain effective for new publication by revoked callbacks, and Q36 still controls every new canonical business write.

Boundary example: a response legally commits, the Run later ends, and the original submitting path repeats the same response because its acknowledgement was lost. Confirmation may return the original publication result, but must not write a new response, modify timestamps, grant execution, advance the Run or trigger business processing. Input/reference and applicable read-access checks still apply. Q91–Q94 subsequently close equality, missing/corrupt existing payload handling, publication-result shape and concurrent first-publication reconciliation.

Intended destination: execution-runtime response publication/confirmation operation, Storage immutable equality and race proof.

<a id="cg05-q90"></a>
### CG05-Q90 — M1 format protocol does not freeze production Provider schemas

Status: ACCEPTED. M1 freezes response-format registration, completeness obligations, deterministic serialization, integrity, size and recovery interfaces. Use explicitly test-only response formats to prove this foundation. The concrete production format fields and SDK mapping are closed with SL-03.M2's actual adapter research and Contract scope. Do not promote a test fixture into a universal Provider response schema or claim that its conformance proves a real integration is ready.

Intended destination: execution-runtime format interface, deterministic conformance scope and explicit M2 production integration boundary.

## Round 9 persistence and local review

Actual writeback: this register only. Q86 removes the proposed timestamp from M1's intended shape; one bounded read-only check confirmed that existing recovery/Acceptance requirements do not consume it. Q89 records the user's confirmation-versus-publication split and explicitly annotates the affected Q8 wording. It leaves new-write fencing, terminal immutability, response identity and consumer business authority unchanged. Q83 gives lawful unowned-Run reconciliation its own atomic predicates; an observed business result never authorizes an arbitrary Run mutation.

Local review checks decision IDs, effective versus rejected/superseded wording, required/null Run fields, response-rejection atomicity and the absence of new-write authority on confirmation. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified. No full audit, dependency installation or migration occurs.

## Round 10 — Response Confirmation, Recovery Interfaces and Completion Evidence

<a id="cg05-q91"></a>
### CG05-Q91 — Existing-response equality uses the exact format and complete serialized bytes

Status: ACCEPTED. Compare exact response_format_key and the complete deterministic UTF-8 serialized bytes under that format, verifying integrity of the stored bytes. Q118 subsequently fixes format-key provenance: the publication caller does not resubmit a key; Runtime resolves the Invocation-owned immutable value. A caller-provided hash or hash equality alone does not establish response equality. Do not reinterpret historical content using a current default format. Q40's logical equality remains expressed through Q45's deterministic per-format encoding, not incidental serializer output.

If the submitter already holds the original format's exact bytes, confirmation need not reinterpret the business body. If a valid comparable representation cannot be obtained, return an explicit failure rather than guessing equivalence. Q89's confirmation path grants no new execution/write authority.

Intended destination: execution-runtime response confirmation inputs/equality and Storage byte-integrity verification.

<a id="cg05-q92"></a>
### CG05-Q92 — Confirmation reports corruption without becoming a Run mutation interface

Status: ACCEPTED. When read-only confirmation discovers missing existing payload or failed byte integrity, return the explicit payload-unavailable/integrity failure. Do not refill the response or directly change Run state from that confirmation operation. Convergence of an affected OPEN Run belongs to the authorized Runtime recovery/coordination boundary under Q64/Q73/Q83; discovering the problem does not give a stale submitter Run-write authority.

The confirmation path remains read-only; the separate recovery obligation remains effective. Do not interpret this separation as permission to leave a confirmed required-payload failure indefinitely OPEN when lawful coordination and storage are available.

Intended destination: execution-runtime read-only confirmation results and authorized failure-coordination interface.

<a id="cg05-q93"></a>
### CG05-Q93 — Immutable response publication result

Status: ACCEPTED. Successful first publication and successful confirmation of the same response return the same four-field publication result: invocation_id, response_format_key, sha256 and byte_length. Values come directly from the immutable published response record. No current Run state, owner, readiness or payload-availability state is included. Such current facts belong to independent reads.

No separate receipt entity is required to reconstruct these immutable values. The result acknowledges the original publication; it does not promise permanent future payload readability or permit skipping Q91/Q92's confirmation checks.

Intended destination: execution-runtime publication/confirmation success result shape.

<a id="cg05-q94"></a>
### CG05-Q94 — Reconcile a winning concurrent response publication

Status: ACCEPTED. If first publication loses a race after an earlier absence check, re-establish committed truth. If another path published the same response, use Q89's read-only confirmation; a different response is an integrity conflict. If no response exists, return the actual admission/commit failure. An earlier observation of absence does not justify overwriting a winner, creating a second response or returning an incidental storage uniqueness error instead of the owned result.

Unresolved commit truth still follows bounded reconciliation and cannot be treated as confirmed absence. This race handling does not authorize a losing path to make a new write after revocation or ending.

Intended destination: execution-runtime concurrent publication results and Storage uniqueness/commit reconciliation.

<a id="cg05-q95"></a>
### CG05-Q95 — Three minimum consumer recovery responsibilities

Status: ACCEPTED. A statically registered consumer recovery interface supplies three responsibilities: reconcile_result determines whether the consumer's canonical result already committed and meets completion conditions; admit_recovery determines current eligibility, allowed scope and finite budget; resume_local performs admitted local recovery under valid execution qualification. Exact implementation method names are not normative.

The first two responsibilities do not submit new business results. The third preserves consumer-owned permissions, bounds and atomic business commit rules. Do not return arbitrary workflow scripts or a generic execution-plan language. Q104/Q105 subsequently define result-reconciliation and recovery-admission variants without duplicating business result schemas in AgentRun.

Intended destination: execution-runtime consumer protocol and later consumer-owned completion/admission agreement.

<a id="cg05-q96"></a>
### CG05-Q96 — Local recovery bounds remain consumer-owned across restart

Status: ACCEPTED. The actual consumer defines finite local-recovery constraints that remain meaningful across restart and may reuse its existing persisted state. Restart must not automatically restore a fresh full recovery budget. M1 consumes and enforces these admission conditions without adding a universal RecoveryPolicy entity or common recovery-limit field to every Run.

This implements Q58/Q62's bounded local continuation without extending the original remote-execution deadline. Each actual consumer must supply concrete valid bounds before that recovery path is admitted; an unspecified bound is not an unlimited allowance.

Intended destination: execution-runtime bounded local recovery seam and consumer-owned persistent budget/eligibility obligations.

<a id="cg05-q97"></a>
### CG05-Q97 — Registered keys use exact identity

Status: ACCEPTED. consumer_key and response_format_key are non-empty, case-sensitive registered strings matched exactly. Do not trim, case-fold, normalize or fall back to an allegedly similar version. New object creation rejects an unregistered selected key; a historical object's key that is no longer supported follows the already accepted consumer/format-unavailable recovery rules.

This requires no new database-editable registry or universal version entity. Static registration does not waive incompatibility/version-change requirements under Q54/Q79.

Intended destination: execution-runtime key scalar/equality and new-versus-historical admission.

<a id="cg05-q98"></a>
### CG05-Q98 — Invalid caller operations are not automatic Run failures

Status: ACCEPTED. Return stable internal rejection results for caller-level failures such as RUN_NOT_FOUND, INVOCATION_NOT_FOUND, REFERENCE_MISMATCH, RUN_ENDED and EXECUTION_NOT_CURRENT. A stale generation, wrong reference or prohibited new write to an ended Run does not by itself establish failure of the lawful execution.

The rejection itself changes no Run state and fills no failure_code. Only an actually defined Runtime execution/recovery failure may end the Run through an authorized boundary. Existing-response confirmation retains Q89's earlier branch and is not indiscriminately rejected as RUN_ENDED or EXECUTION_NOT_CURRENT.

Intended destination: execution-runtime internal rejection vocabulary and separation from persisted failure causes.

<a id="cg05-q99"></a>
### CG05-Q99 — Size rejection requires confirmed complete remote termination

Status: ACCEPTED with user refinement. response_rejection_code is required and nullable in the MODEL record. Its only initially supported non-null value is RESPONSE_TOO_LARGE. That value requires Runtime confirmation of a complete remote terminal result and a complete deterministic serialized payload that exceeds max_response_bytes. The cause is rejection of a known complete response at the persisted representation boundary, not simply observation that incoming data crossed a local limit.

For a non-null code, durability_phase is DISPATCH_INTENT_DURABLE, no durable response exists, and the corresponding FAILED Run ending and rejection evidence commit atomically under Q87. Once recorded, the code is immutable. It must be null in PREPARED and RESPONSE_DURABLE. Other failures do not borrow this field.

Counterexample: streaming reception crosses a resource limit and is stopped before a complete terminal result is established. Runtime knows that local reception was interrupted; it does not thereby know whether the Provider completed normally. Do not record RESPONSE_TOO_LARGE as known-complete evidence in this case. Classify it through the applicable remote-uncertainty/execution-interruption rules, preserving any already committed cancellation/timeout ending. Q101/Q102 subsequently define the interrupted-reception ending and bounded resource-protection behavior without inventing remote completion.

Refinement of the original Q99 field constraints: confirmed complete remote termination is an essential prerequisite, consistent with Q76/Q87. This does not require retaining oversized output, unbounded buffering or continuing to receive an unbounded stream merely to obtain a terminal result. No previously accepted complete-response requirement is weakened or superseded.

Intended destination: execution-runtime MODEL record consistency, size-rejection evidence and complete-versus-interrupted stream proof.

<a id="cg05-q100"></a>
### CG05-Q100 — Minimum durable-response record

Status: ACCEPTED. The durable-response record has five non-null fields: invocation_id, response_format_key, serialized_payload, sha256 and byte_length. serialized_payload denotes the exact format-defined UTF-8 bytes. SQLite TEXT/BLOB representation remains an implementation detail only if those bytes are preserved. The one-to-one relationship is identified by invocation_id.

No independent response_id, response_durable_at or retention-state field is introduced. Publish the complete record and RESPONSE_DURABLE atomically, applying Q45–Q47's encoding/integrity and Q89's existing-response versus new-publication distinction.

Intended destination: execution-runtime response record shape and Storage one-to-one byte-preserving atomic persistence.

## Round 10 persistence and local review

Actual writeback: this register only. Q99 incorporates the user's completion prerequisite and adds an explicit early-stream-interruption counterexample; Q76/Q87 point to that clarification without changing their known-complete semantics. Q91–Q94 preserve read-only confirmation while retaining current authority for new writes. Q95/Q96 leave actual consumer recovery bounds owned and finite, and Q98 separates caller rejections from Run failure transitions.

Local review covers the response record/result distinction, nullability and uniqueness, the conditional size-rejection evidence, Q63's first-valid-ending arbitration and Q89's scoped supersession. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified. No sub-agent, full audit, installation or migration is used this round.

## Round 11 — Interruption, Admission and Internal Interface Boundaries

<a id="cg05-q101"></a>
### CG05-Q101 — Interrupted reception without known remote completion

Status: ACCEPTED. If local reception stops before a complete remote terminal result can be established, remote completion remains unknown. Unless another ending already committed, end the Run as OUTCOME_UNKNOWN with null failure_code through the authorized ending boundary. Keep DISPATCH_INTENT_DURABLE and null response_rejection_code; do not claim RESPONSE_DURABLE or known-complete RESPONSE_TOO_LARGE evidence.

If cancellation, timeout or another valid ending committed first, preserve it under Q63 while retaining the fact that remote execution was not proved absent. A local interruption does not establish Provider success, failure, cessation, zero usage or refund. Q73 still governs inability to persist the ending itself.

Intended destination: execution-runtime interrupted-reception classification and deterministic known-versus-unknown evidence.

<a id="cg05-q102"></a>
### CG05-Q102 — Resource protection does not require draining an unbounded stream

Status: ACCEPTED. Runtime may stop reception when a finite resource-protection condition is reached and request cancellation where the adapter supports it. It need not drain the stream to obtain terminal evidence merely to qualify for RESPONSE_TOO_LARGE. No unbounded buffering or waiting, and no automatic Provider recall, is authorized to make the outcome certain.

Classify the result using facts actually established at the boundary. If a complete terminal result is known, the applicable complete-response rule may apply; otherwise preserve uncertainty under Q101. A receive/buffer threshold is not itself Q68's complete deterministic persisted-payload measurement.

Intended destination: execution-runtime bounded adapter reception and resource-interruption proof.

<a id="cg05-q103"></a>
### CG05-Q103 — MODEL Invocation metadata projection

Status: ACCEPTED. The MODEL metadata projection contains eight required fields: invocation_id, run_id, kind = MODEL, durability_phase, dispatch_generation, response_format_key, max_response_bytes and response_rejection_code. Only dispatch_generation and response_rejection_code are nullable.

At PREPARED creation, choose and freeze the response format key and finite positive integer response-size bound; initialize both nullable fields to null. Existing UUID, owning-Run, monotonic phase and generation-provenance rules apply. This projection does not replace Q6's actual dispatch descriptor, which must be durably recorded and frozen with committed intent. Physical decomposition remains an implementation concern, not permission to omit the descriptor.

Intended destination: execution-runtime MODEL metadata shape/initialization and dispatch-descriptor agreement.

<a id="cg05-q104"></a>
### CG05-Q104 — Consumer result reconciliation distinguishes known incompletion from uncertainty

Status: ACCEPTED. The consumer result-reconciliation operation returns COMPLETION_CONFIRMED when its completion conditions are established, RECOVERY_REQUIRED when further recovery is definitely needed, or UNRESOLVED when current truth cannot be determined. Failed reads do not imply RECOVERY_REQUIRED or absence of a committed result.

UNRESOLVED enters bounded coordination and does not permit repeated business submission or remote invocation. The operation does not itself mutate Run state or return a generic business-result JSON object. Actual Run ending still uses Q71/Q83's lawful boundary.

Intended destination: execution-runtime consumer result-reconciliation outcomes and uncertain-result proof.

<a id="cg05-q105"></a>
### CG05-Q105 — Definite recovery denial converges without a universal failure code

Status: ACCEPTED with user correction. admit_recovery returns ALLOW, DENY or UNRESOLVED. ALLOW requires the consumer's valid allowed scope and finite constraints. UNRESOLVED stops dependent execution and enters bounded coordination; it is not a definite denial or proof that execution may proceed.

A definite DENY prevents recovery execution and converges the Run through an authorized ending boundary. When denial is explicitly due to the applicable deadline or time-budget exhaustion, use TIMED_OUT. For other denial reasons, the first actual consuming Contract must define the corresponding stable Runtime-owned failure code and ending mapping. Do not invent a fallback generic code for source eligibility loss, permission revocation or incompatible consumer state. FAILED still requires an actually defined non-null Runtime-owned failure_code under Q53; no speculative value or raw consumer business error may be substituted.

REJECTED proposal fragment: freezing RECOVERY_NOT_ADMITTED as M1's catch-all code for non-time recovery denial. Preserve the definite-denial convergence obligation while leaving actual cause mappings to their first real consumers. This does not authorize indefinite OPEN state for a fully specified definite denial, or promote a business-content validation result into Runtime failure. Q111 subsequently requires actual consumer DENY mappings and verification before its recovery path is enabled.

Intended destination: execution-runtime recovery-admission results and explicit consumer-owned failure-mapping obligations.

<a id="cg05-q106"></a>
### CG05-Q106 — Raw response reads are independent of business decoding

Status: ACCEPTED. Internal raw response reading returns Q100's record after verifying stored length/hash and applicable read access. It does not inherently require the Run's execution generation to remain current or a current business parser. Interpretation of the bytes belongs to the response-format reader and actual consumer.

Distinguish Invocation absence, response not yet durable, confirmed payload absence, failed integrity and failed storage reading. The read operation itself does not mutate the Run; authorized recovery/coordination retains any required failure-convergence obligation under Q92. Missing format support does not authorize reinterpreting raw bytes with another format.

Intended destination: execution-runtime raw read results and Storage byte-integrity/access boundary.

<a id="cg05-q107"></a>
### CG05-Q107 — Minimal execution qualification value

Status: ACCEPTED. Internal execution qualification carries run_id, runtime_instance_id and execution_generation. It conveys claimed qualification to be verified, not an independently valid offline authorization token. Every state-affecting operation still checks its applicable current atomic authority conditions; dispatch additionally requires Q31's original live-path proof.

No execution_token_id is introduced. The value neither replaces the server's current owner record nor bypasses dedicated cancellation/reconciliation rules. Q89's existing-response confirmation remains read-only and does not acquire new-write permission merely by carrying an old qualification value.

Intended destination: execution-runtime internal qualification value and operation admission.

<a id="cg05-q108"></a>
### CG05-Q108 — Logical fencing is mandatory; physical interruption follows adapter capability

Status: ACCEPTED. Cancellation/timeout must prevent the invalidated path from first publishing a response or advancing business execution. Request physical interruption where the adapter supports it, but do not promise that the remote Provider actually ceased execution or treat a cancellation acknowledgement as proof of non-execution, zero cost or refund.

Logical fencing is independent of whether local or remote execution can be physically stopped. Q89's read-only confirmation of an already published identical response remains valid and is not new execution by a revoked callback.

Intended destination: execution-runtime adapter interruption/fencing interface and cancellation fault proof.

<a id="cg05-q109"></a>
### CG05-Q109 — Duplicate static registration is rejected

Status: ACCEPTED. Reject duplicate registration of the same static consumer/response-format key during composition. The affected Runtime cannot begin execution until the registration conflict is resolved; there is no last-registration-wins override. Incompatible definitions require a new key, not rewriting historical records to evade the conflict.

This is distinct from ordinary missing support for an existing historical key, which follows Q69/Q82's scoped recovery isolation and convergence. It introduces no mutable database registry or speculative registry-management API.

Intended destination: execution-runtime static registration integrity and startup composition obligations.

<a id="cg05-q110"></a>
### CG05-Q110 — Structurally invalid persisted Runtime records are not silently repaired

Status: ACCEPTED. Persisted negative generations, unknown state enums, OPEN Runs with ending information and similar structural contradictions produce a persistence-integrity error and stop affected Runtime operations. Do not guess a generation reset, phase rollback or fabricated historical record to make them loadable.

Whole-database opening policy remains owned by existing Storage rules; M1 does not independently expand every Runtime inconsistency into a universal application failure. Confirmed missing/corrupt payload covered by Q64 still follows its defined authorized failure convergence rather than being silently reclassified as normal purge or a reason to repair response history.

Intended destination: execution-runtime persisted-shape validation and Storage integrity/failure applicability.

## Round 11 persistence and focused interface review

Actual writeback: this register only. Q105 rejects the proposed generic recovery-denial code while preserving definite-denial convergence and Q53's failure ownership/nullability rules. Q101/Q102 close the incomplete-stream branch without weakening Q99's complete-termination prerequisite. Q103/Q106/Q107 distinguish durable metadata, immutable raw bytes and currently validated execution qualification.

One bounded read-only check examined the known Tool consumers and current M1/M2 ownership split. Existing Tool provenance names job.requirements.read as an accepted read of an existing compatible RequirementSet; it does not perform Application-owned Ensure. resume.read and evidence.read/search are illustrative exact-version reads, not a frozen catalog. Confirmed Proposal writes remain Application-owned, and the inspected recovery sources identify no concrete remote Tool idempotency consumer to implement in M1. This supports asking a narrow pure-read proof boundary below; it does not by itself select that delivery scope or claim the actual Tools exist.

Local review covers decision numbering, rejected versus effective denial wording, interruption evidence, metadata nullability, references and whitespace. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified; no full audit, dependency installation or migration is performed.

## Round 12 — Internal Operations, Tool Proof Scope and Publication Authority

<a id="cg05-q111"></a>
### CG05-Q111 — Actual consumers close their denial mappings before enabling recovery

Status: ACCEPTED. Before an actual consumer enables its recovery path, it defines the definite DENY branches it consumes, their ending reasons, any required stable Runtime-owned failure codes and verification. Missing mappings mean that consumer interface is not closed; do not choose a code at runtime or use a generic fallback. This requirement does not disable unrelated consumers whose interfaces are already closed.

M1's shared foundation does not claim all future denial causes are specified. Consumer business outcomes remain separately owned under Q61, and Q105's definite-denial convergence obligation remains effective once the actual mapping is defined.

Intended destination: execution-runtime consumer integration obligations and scope-level readiness evidence.

<a id="cg05-q112"></a>
### CG05-Q112 — Conditional execution grant operation

Status: ACCEPTED. Grant input contains run_id and expected execution_generation; the current runtime_instance_id comes from Runtime rather than a caller-selected owner. Atomically require OPEN, null owner, matching expected generation, an unexhausted counter and satisfied consumer admission. Success increments generation once, assigns the current owner and returns Q107's qualification value.

A failed grant does not advance generation. An existing owner belonging to the same Runtime does not turn another invocation of grant into a second successful grant; Q85 still governs uncertain acknowledgement of the original operation. The current state and operation admission, not just a matching runtime instance, arbitrate the winner.

Intended destination: execution-runtime grant inputs/results and Storage conditional ownership update.

<a id="cg05-q113"></a>
### CG05-Q113 — Revocation targets a specific current qualification

Status: ACCEPTED. Revoke accepts Q107's qualification tuple. Clear owner only if that tuple still matches current owner/generation; retain the generation. Repeated revocation or an old qualification reports that it is no longer current without changing a newer owner. No generation reset or increment occurs.

Run-wide cancellation remains a separate internal operation and does not require the cancelling user/consumer to possess an executor's qualification. This distinction preserves Q34 rather than letting stale executor cleanup cancel a replacement owner.

Intended destination: execution-runtime revoke operation and stale-cleanup race proof.

<a id="cg05-q114"></a>
### CG05-Q114 — Minimum Run creation input and initial state

Status: ACCEPTED. Create Run accepts consumer_key and nullable deadline_at. Runtime supplies the UUID and created_at. Initialize OPEN, execution_generation = 0, null owner_runtime_instance_id, and null end_reason/ended_at/failure_code. The caller cannot choose the initial owner, generation or ending information.

Successful creation returns stable run_id; full current state is obtained by a separate read. Q84 retains the originally allocated identity during uncertain creation reconciliation. A supplied deadline is the consumer's established deadline under Q37/Q41, not an automatic create-time timeout calculation or a later extension permission.

Intended destination: execution-runtime Run creation interface and initial persisted invariants.

<a id="cg05-q115"></a>
### CG05-Q115 — MODEL preparation requires current owning-Run authority

Status: ACCEPTED; the original input list is PARTIALLY SUPERSEDED by CG05-Q129. Historical input included a separate owning run_id alongside execution qualification, registered response_format_key and finite max_response_bytes. The effective input now omits that separate run_id and derives it from execution qualification. Runtime allocates invocation_id and atomically verifies that the owning Run is OPEN, qualification is current and applicable consumer admission is satisfied before creating Q103's PREPARED record.

Preparation success proves only that this record is durable; it is not dispatch authorization. The record binds its owning Run immutably and captures its format/limit before any intent is committed. Q129 removes the duplicate parent identifier, not the need to validate that the qualification identifies the current owning Run. Preparation authority and immutable owning-Run binding remain unchanged.

Intended destination: execution-runtime MODEL preparation interface and atomic reference/admission checks.

<a id="cg05-q116"></a>
### CG05-Q116 — M1 Tool recovery proof uses a controlled exact-version local read

Status: ACCEPTED. Bound M1's Tool recovery proof to a controlled exact-version local-read action. Before a permitted re-execution, revalidate current permission/scope and the exact retained input; never substitute current data for the admitted exact version. An action without a supplied recovery agreement is not replayable merely because it is called a read.

This exercises the foundation against the known local-read consumer pattern without claiming a production business Tool is delivered. Actual business Tools, controlled writes and remote actions close in their owning consumer milestones. Do not add a universal remote replay mechanism or invent a concrete remote idempotency consumer for M1. Q121–Q123 subsequently close the minimum Tool envelope and the admitted local-read recovery boundary; production action data remains consumer-owned.

Intended destination: execution-runtime minimum Tool recovery seam, deterministic conformance scope and explicit M2/business-consumer exclusions.

<a id="cg05-q117"></a>
### CG05-Q117 — Consumer-validated dispatch descriptor commits with intent

Status: ACCEPTED. The actual consumer supplies a dispatch descriptor or exact references validated under its owning Contract. The intent transaction completely persists and freezes that description. Sending uses the committed description, not a new request reconstructed from current defaults. M1 owns the persistence/consistency seam; actual Provider/Tool request structures remain with their consumers rather than becoming one arbitrary universal request JSON.

Q103's metadata cannot replace this required description. Physical decomposition is free only if required references/data and the intent become atomically valid together. No sender may treat an incomplete descriptor publication as permission to execute.

Intended destination: execution-runtime dispatch producer/consumer interface and Storage atomic descriptor/intent persistence.

<a id="cg05-q118"></a>
### CG05-Q118 — Publication derives format authority from the Invocation

Status: ACCEPTED with user correction. The internal MODEL response publication input is exactly invocation_id, execution_qualification and serialized_payload. Runtime resolves the already frozen response_format_key from that Invocation; the caller does not resubmit it. Runtime computes sha256 and byte_length itself rather than accepting asserted integrity metadata.

For first publication, validate the payload using the Invocation's selected format and enforce the current authority, deadline, format and size gates. Existing-response handling still takes Q89/Q91's read-only confirmation branch: exact historical byte confirmation does not become a new publication or require a current generation, unexpired deadline or reinterpretation by an available business reader. The format key in stored/read response metadata and the publication result is derived from the Invocation-owned value, never a competing caller-selected authority.

REJECTED proposal fragment: accepting response_format_key as a fourth publication argument and then comparing it with the stored selection. The single source is the immutable Invocation field; response validation remains mandatory for new publication. This changes the producer input, not Q93/Q100's output/record projections or existing historical-byte equality.

Intended destination: execution-runtime publication command, Invocation-to-response provenance and Runtime-computed integrity metadata.

<a id="cg05-q119"></a>
### CG05-Q119 — Wall-clock rollback does not fabricate causal timestamp order

Status: ACCEPTED. A system-clock rollback may yield ended_at earlier than created_at; that inequality alone is not corruption. Record actually observed canonical UTC timestamps instead of altering them to manufacture order. State transitions, generation and atomic commits determine execution causality, not timestamp or UUID ordering.

Deadline and process-local timing still follow Q59. This introduces no trusted-time service, clock-repair mechanism or permission to reset the stored deadline across restart. Existing ending timestamp immutability remains effective.

Intended destination: execution-runtime timestamp semantics and scoped Common/Storage applicability.

<a id="cg05-q120"></a>
### CG05-Q120 — Reuse scoped Common scalars and closed interface shapes

Status: ACCEPTED. Consume existing UUIDv4, canonical UTC timestamp, Sha256Hex and exact integer conventions. Declared consumed interface field sets are closed: reject unknown fields, invalid types and implicit coercion. Size/length fields use exact integers with explicit positive bounds; Boolean values are not numbers. The owner defines actual applicable bounds without silently inheriting an unrelated object's revision meaning.

Do not mechanically add schema_version, revision or updated_at to Run/Invocation merely because another Slice uses them. These interface shape rules do not freeze physical table layout or introduce a public HTTP protocol. Q81/Q103/Q100 remain the accepted consumed projections, with separately owned future extensions.

Intended destination: execution-runtime scalar/shape admission and narrowly scoped Common applicability at publication.

## Round 12 persistence and local review

Actual writeback: this register only. Q118 removes the duplicate format-key input and keeps the Invocation as the unique format-selection authority. Q91 now points to that provenance rule; Q93/Q100 retain their derived output fields. First-publication validation and existing-response confirmation remain separate, so unavailable current reader support does not invalidate a proven exact historical-byte confirmation. Q111 closes consumer mapping readiness without restoring the rejected generic denial code.

Local review checks the grant/revoke/creation/preparation inputs against qualification and initial-state invariants, the Model-versus-Tool proof scope, publication input/output ownership and the clock-order correction. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified; no sub-agent, full audit, installation or migration is used.

## Round 13 — Tool Boundaries, Publication Provenance and Final Input Simplification

<a id="cg05-q121"></a>
### CG05-Q121 — Minimum common Tool envelope

Status: ACCEPTED. The shared TOOL record portion contains invocation_id, immutable run_id and kind = TOOL. The owning action protocol defines and associates its concrete action, typed input, exact references, completion evidence and recovery data with that Invocation. These owned data requirements cannot be replaced by the three common identity fields alone.

M1 does not copy MODEL's three durability phases into TOOL or introduce a universal lifecycle for all Tool actions. The actually consumed controlled local-read protocol must satisfy the already accepted recovery/fencing interface; broader production Tool schemas remain with their real consumers.

Intended destination: execution-runtime common TOOL envelope, typed action extension seam and scope-level ownership mapping.

<a id="cg05-q122"></a>
### CG05-Q122 — Admitted pure local reads may recover within the original Invocation

Status: ACCEPTED. When no reusable durable result exists and the concrete pure-read protocol permits recovery re-execution, keep the original invocation_id under the same Run's new valid execution qualification and reread the original exact input. A valid reusable durable result is reused rather than executing the read again. Current permission, scope and dependency admission remain required.

This is the selected local-read action's recovery rule, not a MODEL replay permission or a generic permission for every Tool. Changing the action or substituting current input is not same-Invocation recovery. ENDED Runs remain closed.

Intended destination: execution-runtime controlled Tool recovery and deterministic same-identity/exact-input proof.

<a id="cg05-q123"></a>
### CG05-Q123 — The controlled read has no hidden Ensure or business side effects

Status: ACCEPTED. M1's controlled local-read proof reads already existing exact data. It does not implicitly parse, generate missing dependencies, commit business writes or initiate remote calls. Missing dependencies produce explicit owned results rather than causing an Ensure operation hidden inside a read.

Actual Ensure remains Application-consumer-owned. This bound is essential to the selected action's repeat-safety proof and cannot be inferred merely from an action name containing read.

Intended destination: execution-runtime Tool proof scope, action admission and no-hidden-effect conformance.

<a id="cg05-q124"></a>
### CG05-Q124 — Provenance references do not automatically become recovery dependencies

Status: ACCEPTED. The consumer explicitly identifies the exact dependencies actually required for recovery and current admission. Runtime does not automatically reread every reference present in a dispatch descriptor or promote provenance-only references into mandatory recovery inputs.

Required dependencies must resolve exactly and pass applicable current permission checks; never substitute current content. This avoids artificial dependencies while preserving all genuinely consumed source and eligibility requirements. The consumer, not Runtime inference, distinguishes those roles.

Intended destination: execution-runtime consumer dependency/admission seam and exact provenance versus recovery requirements.

<a id="cg05-q125"></a>
### CG05-Q125 — First publication requires the selected deterministic byte representation

Status: ACCEPTED. First response publication validates strict encoding, the selected format's structural rules and its deterministic serialization requirements. Parseable JSON alone is insufficient. Reject nonconforming serialized_payload instead of silently reordering keys, filling fields or rewriting bytes and claiming the original input was stored.

Concrete byte rules stay with the versioned response format; no general canonical-JSON framework is introduced. Existing-response confirmation continues to use Q89/Q91's immutable historical-byte comparison rather than reserializing with a current default.

Intended destination: execution-runtime first-publication format validation and per-format byte conformance.

<a id="cg05-q126"></a>
### CG05-Q126 — First MODEL response publication belongs to the original dispatch generation

Status: ACCEPTED. First MODEL response publication requires durability_phase = DISPATCH_INTENT_DURABLE and equality among execution_qualification.execution_generation, Invocation.dispatch_generation and the Run's current execution_generation, together with valid current owner/qualification and all other publication admission.

A new generation may process an already durable response from an earlier generation, but cannot first publish that earlier generation's previously undurable response by relabeling a late callback with new qualification. This supplements, rather than replaces, original-path and owner checks. Q89's read-only confirmation of an already published response remains exempt from new-publication qualification checks.

Intended destination: execution-runtime first-publication fencing/provenance and stale-response laundering prevention proof.

<a id="cg05-q127"></a>
### CG05-Q127 — Run ending fences every remaining Invocation without fabricating outcomes

Status: ACCEPTED. Ending a Run invalidates its execution qualification for all remaining executing Invocations. Apply fencing throughout and request physical interruption where adapters support it. Do not bulk-rewrite them as known remote failures or manufacture complete responses; retain each Invocation's actual persistent facts and evidence.

The Run ending reason is not a replacement for per-Invocation remote outcome truth. Consumer completion conditions still govern whether COMPLETED is valid, and Q89's read-only existing-response confirmation remains possible without resurrecting any execution path.

Intended destination: execution-runtime Run-wide ending effects, multi-Invocation fencing and outcome-evidence preservation.

<a id="cg05-q128"></a>
### CG05-Q128 — No Invocation yet is not itself an unknown remote outcome

Status: ACCEPTED. An OPEN Run found at restart with no prepared Invocation may have crashed before preparation or be in a consumer-permitted waiting stage. Do not classify it as OUTCOME_UNKNOWN or corrupt solely on that basis. Use consumer result reconciliation and current admission to determine the next action; continuing work obtains lawful execution qualification and retains run_id.

Without committed dispatch intent, do not invent an uncertain remote call. This does not grant unrestricted dispatch, bypass an established deadline or invent a general waiting workflow beyond the actual consumer's agreement.

Intended destination: execution-runtime startup reconciliation before first preparation and no-fabricated-dispatch proof.

<a id="cg05-q129"></a>
### CG05-Q129 — MODEL preparation derives its owning Run from qualification

Status: ACCEPTED. The effective MODEL preparation input consists of execution_qualification, response_format_key and max_response_bytes. Resolve and validate the owning Run through execution_qualification.run_id and create the immutable association; Runtime still allocates invocation_id. Do not accept another independently submitted run_id to compare or choose between.

PARTIALLY SUPERSEDES CG05-Q115's original separate run_id input and dual-identifier comparison. All Q115 current qualification, OPEN state, consumer admission and atomic creation requirements remain effective. This changes input representation, not the source of execution authority.

Intended destination: execution-runtime MODEL preparation signature and derived owning-Run binding.

<a id="cg05-q130"></a>
### CG05-Q130 — Response format metadata is derived from Invocation authority

Status: ACCEPTED. response_format_key in the response record/result is derived metadata and must equal the Invocation's immutable selected key. Storage may derive the field through a relation rather than physically duplicating it; if it stores a copy, it must maintain equality.

An inconsistent copy is a persistence-integrity error. Do not choose whichever value is convenient to decode payload, or rewrite the Invocation to accommodate the copy. The accepted response/result projections remain intact without becoming second authorities for format selection.

Intended destination: execution-runtime response provenance/record consistency and Storage reference integrity.

## Round 13 persistence and local review

Actual writeback: this register only. Q129 explicitly supersedes the duplicate parent input in Q115 while retaining all authority checks. Q126 distinguishes first response publication by the original dispatch generation from new-generation local processing and read-only confirmation. Q121–Q124 close the selected controlled Tool and exact-dependency responsibilities without extending M1 into production Tool execution or hidden Ensure. Q130 preserves the single format-selection authority established by Q118.

Local checks cover decision anchors, effective preparation/publication inputs, Tool-versus-MODEL recovery, scoped supersession, references and whitespace. No high-level owner, normative Contract, plan, Progress/readiness, implementation or test is modified. No sub-agent, full cross-document review, dependency installation or migration is used.

## Pre-closure branch disposition

This is a local consolidation of accepted decisions, not normative publication or a claim that the full closure audit has passed. Earlier rounds' statements that a detail remained open describe the frontier at that time. The following later decisions govern the current disposition; preserve the earlier history and explicit supersession rather than restoring its obsolete proposals.

| Branch | Current accepted disposition and source decisions |
| --- | --- |
| M1 scope and minimum objects | Internal foundation and controlled proof, not public HTTP or a universal workflow: Q1/Q2/Q17/Q81/Q90/Q103/Q116/Q121 |
| Identity, ownership and generation | UUID identities, grant-only generations, current qualification and bounded grant uncertainty: Q3–Q5/Q12–Q16/Q21/Q23/Q31/Q85/Q107/Q112/Q113 |
| Run creation, preparation and dispatch | Minimum creation/preparation inputs, stable IDs on uncertain creation, committed immutable descriptor and unique live sending path: Q6/Q26–Q28/Q31/Q66/Q84/Q114/Q117/Q129 |
| Response storage, format and publication | Versioned deterministic bytes, SQLite atomic publication, owned size limits, immutable response/result projections, Invocation-derived format: Q39/Q45–Q48/Q54/Q68/Q75/Q93/Q100/Q118/Q125/Q126/Q130 |
| Existing-response confirmation | Read-only exact-byte confirmation, no second response, no new execution authority, corruption and concurrency reconciliation: Q8 as refined by Q89, plus Q91/Q92/Q94/Q106 |
| Ending and business result coordination | Immutable first valid ending, Runtime-owned failure taxonomy, consumer business outcomes, lawful reconciliation and sibling fencing: Q32/Q34/Q35/Q42–Q44/Q52/Q53/Q61/Q63/Q67/Q71/Q73/Q83/Q98/Q127 |
| Deadline, eligibility and local continuation | Consumer-established non-extending deadline, qualified bounded local recovery, no artificial provenance dependency, truthful clock limitations: Q37/Q41/Q57–Q59/Q62/Q96/Q105/Q111/Q119/Q124 |
| Failure and integrity distinctions | Confirmed missing/corrupt/unsupported response versus unreadable storage; known complete size rejection versus interrupted reception; structural record errors: Q64/Q69/Q72/Q74/Q76/Q82/Q87/Q99/Q101/Q102/Q110 |
| Consumer recovery interface | Immutable static binding, result/admission variants, exact key identity, registration consistency and no-Invocation startup handling: Q79/Q95/Q97/Q104/Q105/Q109/Q111/Q128 |
| Tool recovery seam | Action-owned typed data and evidence; controlled exact-version local read may recover under fresh authority without hidden writes, remote effects or Ensure: Q70/Q116/Q121–Q123 |
| Storage protection and migration | Protect OPEN recovery payloads; preserve existing data; forward migration from actual head: Q47/Q49/Q51/Q80 |
| Common and conformance | Scoped scalar/closed-shape reuse, per-format byte fixtures and actual persistence/Runtime fault proof: Q56/Q77/Q88/Q120 |

Explicitly deferred scope remains deferred: Run-level retry and its lineage (Q22), actual payload purge/disposition (Q50 resolved by Q51), the full late-usage subsystem (Q78), response_durable_at (Q86), production Provider response schemas (Q90), production Tool action schemas/side effects (Q116/Q121), and concrete consumer denial codes/recovery bounds (Q96/Q105/Q111). Their first consumers must close them before use; deferral is not whole-family readiness.

## Pre-publication closure work — historical checklist

No additional numbered question batch is queued from this local register review. This does not assert that a complete normative operation/error matrix or cross-document review has already passed. During authorized closure:

1. Consolidate the effective decisions into the consumed Contract bodies, including complete operation inputs/results, field/null/type constraints, atomic predicates, error precedence, producer/consumer obligations and stable requirement IDs. Preserve the Q8/Q89 and Q115/Q129 partial supersessions; do not restore rejected fields or generic failure codes. If that consolidation reveals a genuine semantic choice, record it and ask a targeted follow-up before publishing the affected scope.
2. Audit every current decision's normative destination or explicit future boundary, then check semantics against the current Product, Architecture, Acceptance, Plan, Storage/Common/Workspace and existing consumers. Review only affected high-level owners for necessary writeback under the user's authorization. Required scope clarifications include protection-only cleanup delivery, controlled Tool proof and the distinction between M1 interfaces and M2 production integrations.
3. Produce the actual prescribed mechanical and interface checks, then record reviewed scope and evidence truthfully. Normative review is not executed migrations, runtime tests, SDK integration, business functionality or acceptance completion. Current Contract readiness stays Pending until the relevant publication/review evidence exists.
4. At the authorized publication/handoff stage, reconcile Contract navigation and status evidence, and create docs/development/handoff/sl-03-m1-handoff.md with exact consumed scope, reverified upstream/migration state, implementation order, required proof and remaining consumer dependencies. Do not create a placeholder now or claim backend/frontend implementation from document completion.

Starting this Grill or accepting its numbered decisions does not automatically authorize high-level owner writeback, normative release, implementation or Git operations. The present turn completes the answered round and this local pre-closure consolidation only; it does not run the full closure review or publish Contracts.

<a id="cg05-pub"></a>
## CG05-PUB — Authorized closure and normative publication

Status: PUBLISHED at **2026-09-23.S3M1-r1**. The user's subsequent explicit agreement authorized closure review, necessary owner writeback, normative release and development handoff. This supersedes the pre-publication checklist's pending-stage statements, not any recorded decision or historical evidence. It does not authorize implementation, dependency installation, user-data migration or Git operations.

All CG05-Q1–Q130 have [individual normative destinations](../../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence). New Runtime EXR-001–034 and deterministic evidence EVO-001–007, plus Common COM-047–048 and Storage STO-040–045, publish 49 additions. Preserve Q8/Q89 and Q115/Q129 partial supersession, deterministic format bytes, the grant-only generation model and all explicit deferrals. Internal operation/result projections formalize accepted field/predicate decisions without a new HTTP or business lifecycle.

Necessary writeback is limited to Architecture §12/13, Acceptance §9.2, SL-03/global plans, actual Contract bodies/navigation, this register/design navigation, actual status/evidence and the new [backend handoff](../../development/handoff/sl-03-m1-handoff.md). Product and Workspace were reviewed and need no new normative behavior. Original provenance, prior milestone handoffs and prior normative consumers remain preserved. Protection-only retention, controlled exact-read proof, limited postdeadline local recovery and original-live-path reconciliation are now aligned across owners.

The current source checkpoint is HEAD 1277e2af7180f9765c0542c92c1fb4d1ffb44800 with committed Candidate/Materials and schema-4 migration head a41d7e90c263. No AgentRun/Invocation runtime exists in the inspected source. This replaces the entry checkpoint only as the next-development baseline; the earlier schema-3 snapshot remains historically accurate. No actual user database was inspected and inherited 330-test evidence was not rerun.

Both verification seams and required interface closure are recorded in traceability §6.5. Four M1 portions are Ready; no implementation or acceptance is claimed. Later production Provider/Tool/Context/Budget, semantic evidence, retry lineage, purge, late usage and actual business-consumer mappings remain scoped Pending. Temporary authoring helpers stayed outside the repository; the existing link checker remains under the user's earlier express temporary-retention instruction.

Executed closure checks: 300 unique anchored requirements, 2773 resolved local links/anchors, 135 CG04 and 130 CG05 mappings, all 49 new normative destinations, and 30 Ready / 63 Pending / 93 scopes. Checker Ruff lint/format and Pyright pass; seven isolated negative fixtures and restored baseline pass. All 251 previous requirement bodies compare unchanged against HEAD. New/changed-file whitespace and conflict-marker checks and git diff --check pass. Backend tests, live model calls and migration execution were not run.
