# SL-03.M2 Contract Grill Decision Register

> English is authoritative. This is the single SL-03.M2 decision/provenance register, not a normative Contract or implementation evidence. Chinese interview recommendations become decisions only after the user's answer; preserve effective meaning and scoped supersession.

[Design navigation](README.md) · [Session handoff](../../development/handoff/contract_grill/sl-03-m2-contract-grill-handoff.md) · [Milestone plan](../../plans/slices/sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) · [Contract ownership](../../contracts/structure.md) · [Readiness](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

## Purpose and session state

- Started: 2026-09-23, under the user's explicit instruction to execute the M2 Contract Grill handoff using grill-me/grilling.
- Milestone: SL-03.M2 — Protected semantic invocation and evidence.
- Namespace: CG06-Qn. Entry inspection found no existing M2 register or occupied CG06 decision namespace in the design/progress records.
- Accepted and persisted: Q1–Q219, including Q212's deferred real-consumer repair protocol, Q215's conformance-only exercise/exact-target restriction and Q216's correlated late-accounting representation. Earlier amendments and supersession annotations remain in their decision sections. Authorized normative owner consolidation is complete for the consumed M2 scope; publication mapping and review are recorded below.
- Current frontier: empty after acceptance of Q217–Q219 with their amendments. The existing “同意授权” authorizes this scoped final owner writeback and review; no repeated publication approval is required.
- The seven foundations and concrete conformance consumer agreement are now closed at the documentary level. Final scoped verification/readiness is recorded below and in Progress; implementation, executable configuration and SDK adoption proof remain separate.
- Scope: complete first-use bounded semantic execution, actual Model/Tool admission, exact headless Context, permission/revocation, capacity, budget/reservation/settlement, durable evidence and admitted telemetry.
- Exclusions: RequirementSet meaning/RequirementParse/Ensure (M3), Fit semantics, Advisor workflows, interactive compaction, Memory, platform execution and unrelated future consumers.

<a id="cg06-s1"></a>
## CG06-S1 — Authorized interview and mutation discipline

Status: ACCEPTED session direction, from the user's current request and the executed session handoff. Use ten dependency-ready questions per ordinary round, continuously numbered, with recommendations in Chinese. Do not ask inspectable facts or reopen settled M1/Architecture choices without a concrete conflict. A final frontier may contain fewer than ten genuine questions.

After every answered round, review acceptance/amendments, persist effective English conclusions here, preserve rejected fragments and scoped supersession, identify prospective normative owners and unresolved branches, and perform focused local checks before the next round. An answer accepting all recommendations with named amendments accepts the remainder; a subset-only answer does not imply blanket acceptance.

Ordinary rounds edit only this register. Initial creation, necessary design navigation and a one-time factual Progress/ledger entry are authorized. Important architectural changes require the user's directed scoped owner reconciliation. Starting the interview does not authorize normative publication, feature implementation, installation, live Provider/platform actions, user-data migration, deployment or Git operations. Closure publication and development transfer require their own applicable authorization. Retain the existing scripts/check_contract_links.py until all Contract Grills finish; put new ad hoc helpers outside the repository.

<a id="cg06-s2"></a>
## CG06-S2 — Single production DeepSeek adapter behind the ModelGateway port

Status: ACCEPTED explicit supplementary direction with the Q81–Q90 answer. M2 production integration uses only the official DeepSeek API, through ModelInvocationRuntime -> ModelGateway -> DeepSeekAdapter -> DeepSeek API. One stable internal ModelGateway port and one production DeepSeekAdapter isolate JobHunter-owned execution semantics from third-party protocol details; this is not a mandate to implement multiple Providers.

DeepSeekAdapter interprets/maps DeepSeek messages/tools, thinking behavior, reasoning/cache usage, Provider observations including system_fingerprint, native CNY pricing inputs, and SDK/HTTP errors into controlled internal representations. Runtime, Context and Budget retain their own authority; adapter interpretation of price/usage does not own resource allocation, reservation or settlement policy. Q48 still requires semantic adaptation before Frame freezing, with only semantics-preserving transport adaptation afterward. The responsibility chain does not move semantic mapping after durable intent or grant the adapter an independent sending path.

Exclude a multi-Provider Registry, dynamic plugin loading, OpenAI/Anthropic/Gemini production adapters, arbitrary base_url, a generic Provider configuration platform and a lowest-common-denominator universal Model schema. A second actual Provider consumer must re-evaluate and extend the abstraction when it exists. Controlled test transports/adapters remain proof infrastructure, not another production Provider or alternate Agent.

This explicitly narrows Q79's earlier default-Provider direction to the current single-Provider delivery scope; it does not select an API family, model, SDK or transport library. It preserves Architecture section 9's existing Gateway responsibility. Intended destinations: agent/execution-runtime.md Gateway/adapter agreement, foundation/budget.md CNY integration and implementation scope in the owning plan where necessary at authorized closure. Actual writeback: this register only.

## Verified entry checkpoint

Read-only inspection on 2026-09-23 at HEAD **683fc3fbd4861ea1b30ff1f221ae7531ab20e0ee**, `docs(contracts): publish SL-03.M1 durability and recovery contracts`. Two bounded read-only agents checked actual engineering facts and relevant Harness/Eval provenance. No backend suite, migration, service, dependency installation or live model call was executed.

| Subject | Observed fact | Evidence limit |
| --- | --- | --- |
| Published M1 | EXR-001–034, COM-047–048, STO-040–045 and EVO-001–007 at 2026-09-23.S3M1-r1 | Reviewed foundation; production M2 interfaces remain Pending |
| Working tree | Uncommitted Invocation Domain/Application/Harness/bootstrap/persistence code and tests exist; bootstrap/Store modifications and other concurrent edits are present | Preserve all of that work; source presence is not passed acceptance |
| Schema target | Invocation model declares schema 5 and revision d092ea64bf17, following a41d7e90c263 | Working-tree target only; no user database inspected or migrated; reverify at development entry |
| Controlled integration | Existing source implements controlled model/read consumers, authority, durable intent/response and startup recovery | Controlled echo/response formats, permissive default test admission and consumer recovery bounds are not production M2 norms |
| Production gaps | No production Provider adapter, semantic Skill execution, protected ContextPackage/Frame, budget or Langfuse integration was found in the inspected scope | These are actual M2 gaps, not evidence that M1 code is absent |
| Dependencies | Root pyproject.toml and uv.lock contain no LangGraph, Langfuse or model-provider SDK dependencies | No claim about globally installed packages; versions/integration remain research work |
| Recorded evidence | Progress/README and M1 handoff retain schema-4/pre-implementation observations; prior 330-test evidence belongs to Materials | Historical snapshots stay intact; this interview has not rerun or accepted Invocation tests |
| Normative destinations | agent/context.md, agent/tools.md and foundation/budget.md do not exist | Structure entries are planned owners, not normative definitions; no placeholders created |

The working tree continued changing during inspection, including additional recovery/persistence tests and shared-error edits. This entry is a factual snapshot, not an exhaustive frozen inventory or review of another task's implementation. M1 implementation acceptance is a dependency before M2 development uses it, not a prerequisite for independent M2 Contract discussion.

## Inherited effective boundaries

- Architecture 9–13/15, Product 9/11, Acceptance 8–10 and specialized Eval criteria govern the first-use safeguards and proof. The Harness/Eval design modules explain provenance; examples do not finalize schemas.
- Static Skills, one bounded semantic task per Run, unique ModelInvocationRuntime → ModelGateway execution, typed Application Tools, permission intersection and returned-content admission are already settled.
- ContextPackage is immutable initial scope; ContextFrame records actual sent input. Headless exact inputs cannot be silently truncated or summarized. Protected-input revocation ends the frozen task.
- M1's grant-only generations, original live sending path, read-only existing-response precedence, deterministic stored response bytes and consumer-owned completion/recovery remain effective. Do not restore displaced CG05 proposals.
- Operation budget, Run limits, reservation, settlement and unknown exposure have separate responsibilities from business success, remote cessation and platform risk. Telemetry never owns commit or settlement.
- M2 proves real protected invocation infrastructure; it does not invent a user-facing probe Skill, parallel test Agent or M3 business semantics. Task-specific semantic evaluator meaning stays with its actual consumer.
- M1 retention supplies no generic purge or Pin subsystem. Retry lineage, concrete production response formats, late usage and consumer recovery mappings require their actual first-use decisions; their deferral is not blanket readiness.

## Responsibility and prospective destinations

| Owner under docs/contracts/ | M2 responsibility | Publication state |
| --- | --- | --- |
| agent/execution-runtime.md | Skill/Run semantic entry, real Model/Gateway/stream interfaces, M1 integration | Extension pending |
| agent/context.md | Initial Package, actual Frame, exact input/capacity/revocation | Planned body |
| agent/tools.md | Typed action admission, permission intersection, source/result obligations | Planned body |
| foundation/budget.md | Operation/Run limits, reservation, counters, settlement and unknown exposure | Planned body |
| foundation/storage.md | Semantic payload/evidence integrity, availability and retention | Extension pending |
| evaluation/evaluation-observability.md | Isolated real-path fixtures/checks/judges, retained evidence, re-evaluation and export | Extension pending |
| common.md | Only genuinely shared scalar/reference/error expression | Extension if consumed |

This table preserves the prospective ownership at interview entry. The authorized publication section and Progress mapping below record subsequent actual clauses/readiness. Product, Architecture, plans, Acceptance and Progress keep their existing responsibilities.

## Dependency-ordered design tree and research gates

1. Semantic consumer entry, Skill binding/control, configuration freeze and Run admission.
2. ContextPackage/Frame, exact source/permission/capacity/revocation interfaces and typed Tools.
3. Operation and Run resource ownership, reservation, counters, settlement and unknown exposure.
4. Actual Provider request/response/stream mapping, no hidden retry and integrated recovery.
5. Real-path Eval, complete checks, independent judges, retention/re-evaluation and admitted export.
6. Complete fields/operations/errors, concurrency/storage, producer-consumer compatibility and authorized publication review.

The handoff's estimate of 20–26 ordinary rounds is provisional, not a quota. Recompute from actual open branches and do not repeat accepted decisions to fill rounds.

Before dependent adapter questions, verify selected LangGraph/Provider SDK/Langfuse versions, official sources/licenses, retry/serialization/stream termination and usage, checkpoint behavior, callbacks/masking, judge resources and export failure behavior. The Eval appendix's earlier research is not deployed capability. No SDK-specific behavior is assumed for the opening frontier.

## Round 1 — Semantic entry, ownership and initial admission

The user accepted all ten recommendations, subject to explicit Q3/Q4/Q6/Q8 amendments. The effective conclusions below include those amendments; original displaced proposal fragments are retained as superseded provenance. Ordinary-round writeback is this register only. Prospective destinations remain unpublished.

<a id="cg06-q1"></a>
### CG06-Q1 — Internal semantic entry and real infrastructure exercise

Status: ACCEPTED. Define a typed internal Application/Harness semantic-task start boundary. A thin integration caller exercises the real entry, admission/protection components and actual Provider adapter to obtain results and evidence. Do not introduce a public generic invocation HTTP API, a new product probe Skill or a parallel test-only Agent. Later business consumers use the same protected infrastructure; this exercise does not publish M3 semantics or establish semantic product quality.

Intended destination: agent/execution-runtime.md semantic entry; evaluation/evaluation-observability.md real-path infrastructure proof. Exact input/result shapes and exercise-consumer completion/recovery definitions remain open. Actual writeback: this register only.

<a id="cg06-q2"></a>
### CG06-Q2 — Distinct semantic Skill and recovery-consumer identities

Status: ACCEPTED. skill_key identifies a statically registered Skill definition with immutable interpretation; consumer_key continues to select the consumer recovery protocol established by M1. Validate compatibility through the registration binding. Semantic instruction changes do not necessarily change the recovery protocol, so the two identities need not evolve together. This creates neither a dynamic workflow registry nor business-result authority in AgentRun.

Intended destination: agent/execution-runtime.md semantic binding and static registration. Exact key expression, binding representation and caller-versus-registry derivation remain open. Actual writeback: this register only.

<a id="cg06-q3"></a>
### CG06-Q3 — Complete Skill control with Budget-owned resource authority

Status: ACCEPTED with user amendment. An executable Skill registration declares semantic control/instructions, typed input and output validation, Context acquisition constraints, allowed actions, its semantic execution boundaries and compatible completion/recovery binding. A Skill without Tools declares an empty allowlist. Missing required definition is a configuration error, not permission for permissive runtime defaults.

Skill owns the task's allowed semantic structure: for example whether Tools or repair are permitted and the maximum semantic steps. Budget Runtime owns the shared resource ledger, money/token reservation and resource admission for the current Run/Operation, including shared concurrency capacity under its resource responsibility. Runtime enforces the intersection of the Skill's semantic allowance and actual Budget/resource availability. A Skill allowance does not create spendable credit or an independent remaining-budget authority; runtime ownership and dispatch remain with Execution Runtime.

SUPERSEDED proposal fragment: any reading of the original broad "finite execution limits" that makes Skill own a second money/token ledger, reservation protocol or shared-capacity authority. The amendment narrows ownership without removing semantic bounds or Run-wide resource limits.

Intended destination: agent/execution-runtime.md Skill control; foundation/budget.md sole resource accounting/admission authority and consuming interface. Detailed semantic-step counting and resource units remain open. Actual writeback: this register only.

<a id="cg06-q4"></a>
### CG06-Q4 — Separate static configuration binding, initial scope and actual input

Status: ACCEPTED with user amendment replacing the universal-snapshot proposal. Run/semantic binding retains skill_key, exact static configuration/protocol references and necessary immutable non-secret non-Frame configuration, such as selected Provider/model and controlled parameters. Configuration references may carry exact versions/hashes. ContextPackage owns initial available input/capability/policy scope. The producing ContextFrame owns the complete content actually supplied to that ModelInvocation, including resolved instructions, messages, Tool schemas and admitted data.

Q48 subsequently makes this content boundary precise: the Frame owns Provider-effective semantic input after semantic adaptation, not SDK-private request structure or network bytes. Q47 separates authorized historical evidence reads from permission to reuse that content in a new execution.

A resolved template participating in model input is preserved through its producing Frame; do not duplicate it as a Run-level "true prompt" authority. Frozen references cannot silently resolve to current defaults. Required unavailable historical handlers/configuration must be reported explicitly rather than substituted. Concrete binding fields, configuration representations and availability failures remain open.

SUPERSEDED proposal fragment: a Run effective-config snapshot containing complete resolved instructions/templates together with Context, Tool and Provider configuration. Do not create a universal effective-config blob or competing prompt/Context authority. Exact references and needed immutable non-secret non-Frame parameters remain permitted.

Intended destination: agent/execution-runtime.md semantic/non-Frame configuration binding; agent/context.md Package/Frame responsibilities; foundation/storage.md exact availability/integrity. This amendment also controls the meaning of "configuration references" in Q5. Actual writeback: this register only.

<a id="cg06-q5"></a>
### CG06-Q5 — Atomic publication of the initial semantic binding

Status: ACCEPTED, interpreted with Q4's amended ownership. Publish the Run, its initial ContextPackage, exact semantic/non-Frame configuration association and budget-owner association together in one short transaction before granting semantic execution qualification. Do not publish an executable Run whose initial task basis must later be filled in by repair. This initial publication does not reserve all future Invocation spending; each actual charged/limited invocation retains its own admission/reservation boundary.

Rationale: startup recovery must observe either the complete initial task basis or no such publication, rather than guess how to complete an orphan semantic Run. This is an M2 consumer extension, not replacement of EXR-004's controlled M1 creation operation or grant protocol.

Intended destination: agent/execution-runtime.md semantic start, agent/context.md initial Package, foundation/budget.md owner association and foundation/storage.md atomicity. Concrete identities/fields and final transactional admission predicates remain open. Actual writeback: this register only.

<a id="cg06-q6"></a>
### CG06-Q6 — Pre-Run typed rejection without a rejected-task lifecycle

Status: ACCEPTED with user amendment. Initial invalid input, missing necessary configuration, insufficient permission or unavailable required input returns typed admission rejection without creating AgentRun. Failures arising after a task has been accepted and durably created retain that Run and use the actual owned convergence rules. Acknowledgement uncertainty is not a known pre-Run rejection or proof that creation did not commit; preserve EXR-004/022.

Necessary minimal diagnostics may use ordinary controlled logs, admitted telemetry or the caller result. Do not create a new durable RejectedTask, RejectedRun, AdmissionAttempt or equivalent business/Runtime lifecycle authority. Queryable rejection history requires a future actual consumer and separate definition.

SUPERSEDED proposal interpretation: reading "retain necessary minimal diagnostics" as a requirement to persist a new pre-Run execution entity or history. Typed rejection and ordinary diagnostic handling remain accepted.

Intended destination: agent/execution-runtime.md start rejection/result distinctions, with applicable common.md error expression and existing diagnostic/privacy boundaries. Full rejection taxonomy and precedence remain open. Actual writeback: this register only.

<a id="cg06-q7"></a>
### CG06-Q7 — Headless deadline starts at accepted task publication

Status: ACCEPTED. Establish the M2 headless Run deadline when the task is formally accepted and its initial execution record is persisted. Subsequent Runtime queue time counts toward this deadline. Application dependency preparation before Run start is outside that Run's elapsed allowance and remains subject to its Operation's own bounds. Later execution grant does not restart the full duration.

This supplies the concrete consumer establishment point permitted by EXR-010, without changing M1's general consumer-owned establishment protocol. Preserve non-extension, expiry restrictions and separately admitted finite local recovery under EXR-011. Exact duration configuration and clock/recovery detail remain open.

Intended destination: agent/execution-runtime.md headless start/deadline admission; foundation/budget.md Run/Operation time boundaries. Actual writeback: this register only.

<a id="cg06-q8"></a>
### CG06-Q8 — Serial admission invariant for current M2 semantic Runs

Status: ACCEPTED with user amendment. Current M2 semantic Runs admit at most one active MODEL or TOOL Invocation at any time, supporting sequential MODEL → TOOL → MODEL execution. Runtime enforces the consumer invariant and refuses a second concurrent active Invocation. Cross-Run concurrency remains subject to shared resource admission.

This does not add max_concurrent_invocations=1 to AgentRun, a universal Runtime configuration, or a generic concurrency-policy object. EXR-001's consumer-owned bounded-concurrency foundation remains intact. A future actual parallel Skill closes fan-out reservation, result ordering, cancellation and recovery before use. Defining exactly when an Invocation enters/leaves the active interval, including uncertainty and crashes, remains open.

Subsequent resolution: Q180 defines the current MODEL active interval and action-owned TOOL completion boundary, without equating retained durability or unresolved accounting with permanent active execution. Existing failure/fencing/recovery protocols still apply.

SUPERSEDED proposal interpretation: promoting first-delivery serial execution into a permanent AgentRun field or global single-slot limitation. Only the current M2 semantic-consumer admission invariant is accepted.

Intended destination: agent/execution-runtime.md semantic-consumer admission; agent/tools.md and foundation/budget.md necessary interfaces. Actual writeback: this register only.

<a id="cg06-q9"></a>
### CG06-Q9 — Isolate invalid Skill capability registration

Status: ACCEPTED. Incomplete Skill definition, incompatible binding or conflicting registration disables the affected Skill and produces an explicit configuration failure before execution. A duplicate/conflicting registration cannot be resolved by choosing an arbitrary winner. Independent complete capabilities remain usable; persistence-integrity failures retain Storage's separate rules.

This preserves EXR-002's fail-before-affected-execution rule and does not redefine historical consumer/reader recovery convergence under EXR-031/032. Detailed affected-dependency handling and configuration error expression remain open.

Intended destination: agent/execution-runtime.md Skill enablement and registration; actual bootstrap consumer obligations. Actual writeback: this register only.

<a id="cg06-q10"></a>
### CG06-Q10 — Admit Tool-definition visibility for each Frame

Status: ACCEPTED. Each model Frame includes only Tool definitions currently admitted by registration, Skill allowlist, Context/acquisition restrictions and current permission. The initial Package retains its immutable original capability scope; the actual Frame records the definitions exposed for this invocation. Permission changes may shrink the visible set. An exposed schema never grants later execution: every requested action is revalidated at execution and returned content is independently admitted before entering Context.

Intended destination: agent/context.md actual Frame assembly and agent/tools.md definition/execution admission agreement. Concrete registry/schema representations, initial-scope ceilings and permission-change races remain open at this checkpoint. Subsequent resolution: Q205 closes the initial capability ceiling without prohibiting admitted lazy source resolution. Actual writeback: this register only.

## Round 1 persistence and local review

- All Q1–Q10 are accepted; Q3/Q4/Q6/Q8 are effective only with the recorded amendments. Q4 also narrows Q5's configuration association. No additional answer is inferred from the intervening explanatory turns.
- Decision-to-Document Traceability: each decision above has an intended owner and explicit actual writeback location; no Contract ID is assigned and no recommendation from Round 2 is accepted. Four displaced proposal interpretations are marked SUPERSEDED without deleting provenance.
- Cross-Document Semantic Consistency: checked Architecture 9–11 and EXR-001–014 for Skill versus Budget authority, Package/Frame separation, consumer-owned concurrency, creation/commit uncertainty, deadline timing and isolated registration failures. These are detailed consumer refinements consistent with existing owners; no current Ready scope was invalidated and no high-level owner writeback is needed for this round.
- Only this register was edited. Concurrent backend, index and Progress changes were observed and left untouched; the entry source checkpoint remains historical, not a new current implementation review.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q10 anchors/headings, Q11–Q20 pending topic identities, all four supersession annotations, this register's local file/anchor references, new-file whitespace and conflict-marker checks. git diff --check scoped to this register passed. No full repository audit, backend suite or normative publication check was run.

## Round 2 — Identity, initial binding and Frame publication

The user accepted Q11–Q20 with explicit amendments to Q19 and Q20. Each intended destination below is prospective and unpublished; actual writeback for every decision is this register only.

<a id="cg06-q11"></a>
### CG06-Q11 — Exact static Skill keys

Status: ACCEPTED. skill_key is a nonempty exact case-sensitive static registration string, without trimming, normalization or fallback. It selects an immutably interpreted definition; changed definition meaning uses a new key. Do not introduce an independent generic skill_version field. Exact independently controlled configuration references remain separate under Q4, so not every configuration change becomes a Skill identity change.

Intended destination: agent/execution-runtime.md static Skill definition/evolution and applicable common.md expression. Concrete configuration reference forms remain open. Actual writeback: this register only.

<a id="cg06-q12"></a>
### CG06-Q12 — Derive the recovery consumer from the Skill registration

Status: ACCEPTED. The semantic-start caller selects skill_key; Runtime derives consumer_key from that Skill's controlled static registration binding. The caller does not independently submit an arbitrary semantic/recovery pair. Multiple Skill definitions may share a compatible consumer protocol; each particular Skill definition has an unambiguous binding.

Intended destination: agent/execution-runtime.md start inputs and registration compatibility. No change to the controlled M1 create_run consumer input is implied. Actual writeback: this register only.

<a id="cg06-q13"></a>
### CG06-Q13 — Run-owned immutable semantic binding

Status: ACCEPTED. Each M2 semantic Run has exactly one immutable semantic binding, associated by run_id without a new semantic_binding_id. It contains only the Skill/configuration/association responsibilities admitted by Q4, not a universal prompt/configuration blob. Physical same-table versus associated-table placement is an implementation choice. Existing ordinary controlled M1 Runs are not required to acquire semantic bindings.

Intended destination: agent/execution-runtime.md semantic Run extension and foundation/storage.md association integrity. Complete fields remain open. Actual writeback: this register only.

<a id="cg06-q14"></a>
### CG06-Q14 — One initial ContextPackage per semantic Run

Status: ACCEPTED. Each semantic Run has exactly one immutable initial ContextPackage, located by run_id without an additional Package UUID, revision or historical version sequence. Later acquired inputs are recorded separately; they do not rewrite the initial scope or earlier Frames.

Intended destination: agent/context.md initial Package identity/cardinality and foundation/storage.md integrity. Package content and acquired-input representations remain open. Actual writeback: this register only.

<a id="cg06-q15"></a>
### CG06-Q15 — MODEL Invocation identifies its actual Frame

Status: ACCEPTED. invocation_id uniquely identifies the immutable Frame bound to that MODEL Invocation; no independent context_frame_id or Frame sequence is added. Assembly/capacity candidates may remain transient. Each Invocation binds at most one final fixed input; another model call has its own Invocation/Frame. TOOL Invocations do not acquire a MODEL Frame by this rule.

Intended destination: agent/context.md Frame identity/cardinality and agent/execution-runtime.md association. Full Frame shape remains open. Actual writeback: this register only.

<a id="cg06-q16"></a>
### CG06-Q16 — Publish frozen Frame with dispatch intent

Status: ACCEPTED. Atomically publish the frozen Frame, required associations, dispatch descriptor and dispatch generation in the dispatch-intent transaction. The descriptor references the same input, and actual sending cannot rebuild a different input. This extends the M1 actual-request invariant rather than introducing another sending authority.

A committed Frame/intent records the fixed input for that attempted call; it does not prove Provider receipt. Preserve the difference between determined input content and evidence that transmission/remote execution happened, including an intent-before-send crash. Do not manufacture sent/received evidence from Frame existence.

Intended destination: agent/context.md Frame publication, agent/execution-runtime.md EXR-013 consumer extension and foundation/storage.md atomicity. Complete request/Frame serialization and association checks remain open. Actual writeback: this register only.

<a id="cg06-q17"></a>
### CG06-Q17 — Typed task input, controlled message assembly

Status: ACCEPTED. The internal semantic entry accepts the Skill's typed task inputs; the controlled ContextBuilder assembles model messages. Explicit user instruction can be task input, but caller-supplied role labels cannot replace Skill control, forge Tool results or bypass content admission. Do not accept arbitrary system/developer/tool message arrays or Provider SDK message objects as the semantic-entry authority.

Intended destination: agent/execution-runtime.md typed entry and agent/context.md trusted control versus admitted task-data assembly. Consumer input shapes remain open. Actual writeback: this register only.

<a id="cg06-q18"></a>
### CG06-Q18 — Controlled non-Frame execution configuration selection

Status: ACCEPTED. Application selects a controlled execution-configuration reference. Runtime resolves and validates it, then freezes the actual Provider/model and permitted parameters under Q4. Do not accept arbitrary Provider endpoints, raw parameter dictionaries or unrestricted passthrough. Admitted parameter/override scope belongs to the concrete configuration protocol; selected-adapter research must precede concrete SDK mapping. No database-editable generic configuration platform is introduced.

Intended destination: agent/execution-runtime.md configuration selection/admission and Gateway consumer agreement. Exact configuration identity/content and concrete Provider selection remain open. Actual writeback: this register only.

<a id="cg06-q19"></a>
### CG06-Q19 — Minimal start result with stable logical-start confirmation

Status: ACCEPTED with user amendment. Successful semantic start returns only run_id, meaning accepted durable task creation, not execution grant, dispatch or business completion. Full state/results use their owned reads. Typed rejection and initial-transaction uncertainty remain distinct.

One logical semantic-start must have a stable retry identity that allows the caller to confirm the original committed run_id after acknowledgement loss or caller crash, including when that caller never received run_id. An uncertain initial commit must not be resolved by independently creating a second semantic Run. Confirmation uses the same logical-start identity and preserves the original result.

The concrete carrier remains UNRESOLVED: start_request_id versus an Application-preallocated/stably held run_id, together with caller crash recovery, association/equality/retention and confirmation operations, must be decided in subsequent idempotency questions. Neither alternative is accepted by this amendment. EXR-002/004 Runtime identity allocation remains the current normative baseline pending an explicitly reviewed consumer extension. No Universal Idempotency Framework or new rejected-start lifecycle is authorized.

Subsequent resolution: Q21 selects start_request_id and preserves Runtime-allocated run_id; Q22–Q29 define caller survival, equivalence, arbitration and retention. Q25 expressly declines a separate confirm_start operation. The preceding unresolved statement records this branch's Round 2 state, not its current identity choice. Detailed comparison/storage/error obligations remain open where stated by those decisions.

SUPERSEDED incomplete interpretation of the original recommendation: merely returning run_id on known success, while relying on caller memory or allowing another create after losing that result. The minimal success projection remains effective; stable identity and recoverable original-result confirmation are now mandatory.

Intended destination: agent/execution-runtime.md semantic-start idempotency/confirmation and caller obligations; foundation/storage.md atomic initial-result association. Actual writeback: this register only.

<a id="cg06-q20"></a>
### CG06-Q20 — Publication checks respect each authority's atomic boundary

Status: ACCEPTED with user amendment. Preparation resolves exact inputs and permission requirements. Initial publication atomically validates all applicable local mutable authority facts whose owner participates in that transaction, including exact references, revisions, eligibility, permission state and locally owned budget association validity. Failed required predicates prevent Run creation; do not substitute latest inputs.

Do not require every permission/source-availability check to execute inside SQLite. Non-transactional controlled configuration or another authority may supply admission evidence that cannot participate atomically. Preserve its exact controlled basis and revalidate the conditions that must remain live at grant/dispatch and other owned boundaries. Early preflight is never a permanent permission grant. Do not perform external access while holding the authority transaction.

SUPERSEDED proposal fragment: the blanket requirement to recheck all permission/source conditions inside the initial publication transaction, regardless of authority or ability to participate atomically. Atomic local mutable checks remain required; this refinement also governs Q5's publication preconditions. Exact representation and supported kinds of non-transactional admission basis remain open.

Current M2 scope is narrowed by Q30: immutable/exact static configuration constrains available capabilities but is not an independent permission-granting authority; current permission comes from locally atomically checkable mutable state. Q20's broader other-authority allowance does not enable dynamic remote authorization in M2.

Intended destination: agent/execution-runtime.md admission staging, agent/context.md exact source/permission basis, foundation/budget.md association admission and foundation/storage.md local atomicity. Actual writeback: this register only.

## Round 2 persistence and local review

- All Q11–Q20 are accepted with the Q19/Q20 amendments. Q19 explicitly opens a stable-start identity/confirmation branch; it does not select either proposed identity carrier. Q20 refines the local-versus-other-authority boundary and Q5's transaction interpretation.
- Decision-to-Document Traceability: every effective decision has a prospective owner and register-only writeback; the two displaced proposal interpretations remain visible. No startup idempotency field, request receipt lifecycle or normative requirement ID has been silently added.
- Cross-Document Semantic Consistency: checked EXR-002/004/005/013/022 and STO-007/040/043 for identity allocation, creation uncertainty, execution qualification, frozen descriptor atomicity and no external work in authority transactions. The Q19 protocol is not closed until caller identity survival and duplicate-start handling are defined. This is an open M2 consumer seam, not invalidation of M1's reviewed controlled foundation.
- Ordinary-round write set remains this register only; observed concurrent source and Progress changes are preserved. Readiness remains Pending. No implementation, full repository audit or backend tests are part of this round.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q20 anchors/headings, Q21–Q30 unanswered topic identities, all six supersession annotations, explicit Q19/Q20 amendment checks, this register's local file/anchor references, whitespace and conflict-marker checks. git diff --check scoped to this register passed. These checks establish local document integrity only.

## Round 3 — Idempotent semantic start and permission ownership

The user accepted Q21–Q30 with explicit amendments replacing Q25's independent-query proposal and narrowing Q30's static-configuration meaning. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q21"></a>
### CG06-Q21 — Application start_request_id and Runtime run_id

Status: ACCEPTED. Application supplies a UUIDv4 start_request_id for one logical semantic-start; Runtime continues allocating run_id for the accepted task. The two identities serve distinct request-versus-execution purposes. This resolves Q19's identity carrier without changing M1's Run allocation owner or creating a universal idempotency framework.

Intended destination: agent/execution-runtime.md semantic-start input/identity; applicable common.md UUID expression. Actual writeback: this register only.

<a id="cg06-q22"></a>
### CG06-Q22 — Caller must recover the logical start across crashes

Status: ACCEPTED. Before a call can create a Run, the Application caller must establish a recoverable stable association between start_request_id and its owning operation. On restart it recovers that identity and reconciles the original start rather than allocating another identity to escape uncertainty. Every concrete caller must specify how its association and sufficient original request information survive and are recovered; a coroutine-local variable is insufficient.

This is a caller interface obligation, not authorization for a generic request queue or pre-Run lifecycle entity. The actual consumer persistence/reconstruction agreement must close before enabling that path. Under Q25, recovery uses the idempotent semantic-start input, not an assumed ID-only confirmation API.

Intended destination: agent/execution-runtime.md caller obligations and the actual Application consumer interface. Actual writeback: this register only.

<a id="cg06-q23"></a>
### CG06-Q23 — Same-start equivalence concerns original typed request meaning

Status: ACCEPTED. Reuse of start_request_id requires the same original typed start-request meaning, including selected Skill, task input, configuration selection, budget ownership and any requested deadline configuration. Different request content under the same committed identity conflicts; it cannot overwrite the existing task. Runtime-generated run_id/creation time and deadline derived from the actual start point are not caller-request differences.

Exact normalization/comparison representation and per-field rules remain open; no fingerprint algorithm or universal request blob is selected here. Successful confirmation must not re-resolve mutable current defaults into a different request.

Subsequent resolution: Q31 selects minimum retained request-fingerprint evidence with stable historical format identification. Its exact encoding/representation remains for the next frontier; Q39 prevents this comparison protocol from introducing a universal business-input schema.

Intended destination: agent/execution-runtime.md start equivalence/conflict, with Context/configuration/Budget consumers defining their actual typed inputs. Actual writeback: this register only.

<a id="cg06-q24"></a>
### CG06-Q24 — Confirm existing accepted start before fresh-create admission

Status: ACCEPTED. After necessary input-shape, read-access and same-request checks, recognize an existing successful start and return its original run_id before fresh-create admission. Later permission revocation, configuration disablement or an ended Run does not turn that historical confirmation into a new start rejection. This path does not create, grant execution, dispatch or reopen the Run; actual later execution retains current admission.

Q25 makes this a branch of idempotent semantic-start, not a separate query operation. Required comparison/read failures remain distinguishable from fresh-create rejection and must not trigger replacement creation.

Intended destination: agent/execution-runtime.md semantic-start precedence and existing-result confirmation. Actual writeback: this register only.

<a id="cg06-q25"></a>
### CG06-Q25 — Confirm through idempotent semantic-start, without confirm_start

Status: ACCEPTED with user amendment replacing the proposed independent operation. The actual consumer resubmits the same start_request_id and same request. An existing successful association returns the original run_id; absent an association, the same operation atomically attempts creation; a concurrent original submission is resolved by waiting/arbitration and confirmation of actual committed state. Q22 requires the caller to retain sufficient recoverable input for that logical retry.

Runtime/Repository may internally look up the successful association by start_request_id for idempotency and crash reconciliation. Do not elevate that lookup into a separate Contract operation or grant ID-only access. An eventual consumer needing confirmation with only the ID and without the original request must define its access, comparison and unresolved-state semantics separately.

SUPERSEDED proposal: an independent read-only confirm_start(start_request_id) operation with public Contract outcomes for found/not-found/unresolved. Internal truthful storage distinctions remain required, but no such standalone operation is delivered now. Waiting/arbitration must still be finitely bounded under inherited storage/Runtime rules; detailed operation outcomes remain open.

Intended destination: agent/execution-runtime.md idempotent start branches and foundation/storage.md internal association reads. Actual writeback: this register only.

<a id="cg06-q26"></a>
### CG06-Q26 — Atomic unique successful-start association

Status: ACCEPTED. The start identity's uniqueness constraint and successful run_id association commit with the Run, semantic binding and initial ContextPackage in the same local transaction, retaining Q5's budget-owner association. Do not commit a Run and later repair its confirmation association. At most one creation wins for concurrent submissions of the same identity; other paths inspect and compare the committed winner.

Physical table placement remains an implementation question after the logical fields/integrity requirements close. This adds no durable PENDING/REJECTED request lifecycle. Unknown storage results are not proof that no association exists.

Intended destination: agent/execution-runtime.md start arbitration and foundation/storage.md atomic uniqueness/integrity. Actual writeback: this register only.

<a id="cg06-q27"></a>
### CG06-Q27 — Workspace-local semantic-start uniqueness

Status: ACCEPTED. start_request_id is unique for semantic-start within the current physical Workspace, not separately scoped by runtime instance, Skill or Operation. Changing Skill or budget owner under the same identity conflicts instead of obtaining another namespace. Introduce neither a new Workspace business identity nor a cross-Workspace global lookup service.

Intended destination: agent/execution-runtime.md identity scope and foundation/storage.md uniqueness. Actual writeback: this register only.

<a id="cg06-q28"></a>
### CG06-Q28 — No automatic expiry of successful-start evidence in M2

Status: ACCEPTED. M2 provides no automatic expiry or cleanup of the successful-start association and minimum request-consistency evidence. Run ending does not release start_request_id for a new creation. A future actual cleanup consumer must jointly define identity reuse, historical confirmation and evidence-unavailability behavior; this decision freezes no permanent retention duration.

This concerns minimum start-confirmation evidence, not blanket retention of arbitrary prompt/transport data or a general purge subsystem.

Intended destination: agent/execution-runtime.md start-result stability and foundation/storage.md retention. Actual writeback: this register only.

<a id="cg06-q29"></a>
### CG06-Q29 — No content-based automatic merging of independent starts

Status: ACCEPTED. Different start_request_id values express different logical start intentions even when typed inputs are equal. Subject each to its actual admission; do not merge Runs by content hash. Business single-flight, existing-result reuse and target exclusion stay with the actual consumer's agreement. This does not override resource/target admission or authorize bypassing Q22 by changing identity after uncertainty.

Intended destination: agent/execution-runtime.md idempotency scope and Application consumer boundaries. Actual writeback: this register only.

<a id="cg06-q30"></a>
### CG06-Q30 — Static capability configuration is not permission authority

Status: ACCEPTED with user amendment. Current M2 supports locally atomically checkable mutable permission state plus immutable/exactly identified controlled static configuration. Static configuration describes which Skill/Provider/model/parameters/capabilities are available and allowed by that configuration. Local mutable permission authority determines whether the current subject remains eligible to use them. Runtime intersects both at grant/dispatch and other applicable admission boundaries.

Configuration existence, integrity or a matching version alone grants no current execution permission. This clarifies Q20's non-transactional basis: such static configuration can participate in admission without being an independent permission-granting authority. Do not add a tenant/account/principal system merely from the word "subject"; existing single-local-user scope remains.

Dynamic remote authorization services are deferred until an actual consumer closes availability, revocation, timeout and outcome-unknown seams. Provider authentication/transport failures retain their separate actual adapter meaning; they do not establish local task permission.

SUPERSEDED proposal interpretation: treating immutable/versioned static configuration as a non-transactional authority that can independently grant permission. Its capability/configuration constraints remain effective as one input to admission.

Intended destination: agent/context.md permission/source admission and agent/execution-runtime.md configuration/runtime intersection. Actual writeback: this register only.

## Round 3 persistence and local review

- Q21–Q30 are accepted with the Q25/Q30 refinements. Q19's identity branch is resolved to start_request_id plus Runtime-allocated run_id; its historical open statement is annotated. Q20 now points to the current M2 static-configuration/local-permission split. Q24 confirmation is implemented through semantic-start itself, with no standalone confirm_start Contract operation.
- Decision-to-Document Traceability: each accepted decision has a prospective owner and explicit register-only writeback. Superseded Q25/Q30 proposal fragments remain visible. No fingerprint fields, new request lifecycle, permission entity or remote authority mechanism has been silently finalized.
- Cross-Document Semantic Consistency: reviewed EXR-002/004/022 and STO-007/008/040/043 together with Q4/Q6/Q19–Q24. Caller-retained identity plus atomic association preserves Runtime allocation and uncertain-create truth; internal lookup confers no sending/execution permission. Local mutable authority and static capability constraints stay distinct. Detailed comparison, bounded-arbitration outcomes and concrete caller recovery still need closure.
- Only this register was edited; concurrent backend, index and Progress changes remain untouched. M2 readiness stays Pending; no implementation or publication is authorized by these answers.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q30 anchors/headings, Q31–Q40 unanswered topic identities, all eight supersession annotations, explicit Q25/Q30 refinement checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not execution or publication evidence.

## Round 4 — Historical comparison, bounded start and typed-input admission

The user accepted Q31–Q40 with explicit amendments to Q31's historical fingerprint interpretation and Q39's business-versus-technical input bounds. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q31"></a>
### CG06-Q31 — Minimum comparison evidence with stable fingerprint interpretation

Status: ACCEPTED with user amendment. Retain start_request_id, its successful run_id association and request_fingerprint as minimum request-consistency evidence, without adding a second full original-request or prompt authority. The fingerprint calculation rules must have stable version identification. Each historical successful association is interpreted using its original fingerprint format, never whatever calculation happens to be current at retry time.

A fixed domain prefix/format key, deterministic typed encoding and SHA-256 are a proposed concrete realization; SemanticStartFingerprint:v1 is the user's illustrative initial format identifier. The exact identifier, representation and encoding are still to be selected. Future incompatible rules need a distinguishable format/prefix; no generic revision field is required. The caller's Q22 obligation to recover sufficient original request information remains necessary even though the successful association stores only minimum comparison evidence.

Subsequent resolution: Q41 selects explicit fingerprint_format_key, SemanticStartFingerprint:v1 and SHA-256/Sha256Hex; Q42 selects COM-045 encoding. Q129 subsequently selects the complete top-level request envelope, and Q138 selects its exact domain separator. This historical proposal paragraph is not the final byte specification.

SUPERSEDED proposal interpretation: retaining only a bare hash and implicitly applying the current algorithm to historical requests. The minimum-evidence approach remains accepted, but must carry or otherwise unambiguously identify the historical format. Format identification does not duplicate ContextPackage or producing ContextFrame content.

Intended destination: agent/execution-runtime.md successful-start evidence and comparison; foundation/storage.md retained format interpretation; common.md only for genuinely shared expression. Actual writeback: this register only.

<a id="cg06-q32"></a>
### CG06-Q32 — Definite pre-commit rejection does not consume the start identity

Status: ACCEPTED. A definitely uncommitted admission rejection creates no successful association or rejection receipt and does not consume start_request_id. The caller may retry the same logical request with the same identity after its conditions are restored. A changed logical request requires a new identity as a caller obligation; no rejected-request lifecycle is added merely to enforce that obligation server-side.

An uncertain transaction outcome is not a definite rejection. It retains the original identity/request and follows confirmation/arbitration; it cannot justify replacement creation.

Intended destination: agent/execution-runtime.md rejection/retry distinctions and Application caller obligations. Actual writeback: this register only.

<a id="cg06-q33"></a>
### CG06-Q33 — Bounded arbitration with truthful unresolved outcomes

Status: ACCEPTED. Concurrent-start waiting, storage arbitration and uncertain-commit reconciliation have finite configured time/attempt bounds. This decision freezes no permanent numeric default. If the original committed result cannot be confirmed within the applicable bound, return a typed unresolved/cannot-confirm outcome, preserving the possibility of an already committed Run.

The caller continues with the same identity and original request. Do not fabricate definite failure, allocate a substitute Run or dispatch a model call to resolve storage uncertainty. The exact error vocabulary and precedence remain to be consolidated with the complete operation interface.

Intended destination: agent/execution-runtime.md operation outcomes and foundation/storage.md bounded reconciliation. Actual writeback: this register only.

<a id="cg06-q34"></a>
### CG06-Q34 — Historical comparison is separate from current executability

Status: ACCEPTED. Historical same-request comparison must not depend on the Skill still being enabled for new execution. When the original comparison rules remain available, a matching successful start returns its original run_id even if current execution registration/configuration is disabled. This is historical confirmation, not renewed permission.

If required historical interpretation is unavailable, report inability to confirm rather than guessing with new rules, declaring a content conflict solely from algorithm drift, or creating a new Run. Q31's original-format invariant applies. Concrete comparison capability registration and complete errors remain open.

Intended destination: agent/execution-runtime.md historical confirmation and registered interpretation capabilities. Actual writeback: this register only.

<a id="cg06-q35"></a>
### CG06-Q35 — START_REQUEST_CONFLICT is an operation rejection

Status: ACCEPTED. Reusing a committed start_request_id with a different original typed request produces START_REQUEST_CONFLICT. This rejects the submitted operation; it does not fail, revoke or end the existing Run, overwrite its fingerprint or become that Run's failure_code. Diagnostics must not expose sensitive request differences.

Intended destination: agent/execution-runtime.md start conflict and applicable common.md error distinctions. Actual writeback: this register only.

<a id="cg06-q36"></a>
### CG06-Q36 — Broken successful-start linkage is an integrity failure

Status: ACCEPTED. A successful-start association with missing/inconsistent Run or mandatory initial linkage is a persistence-integrity failure. Do not delete/rebuild it, rebind the identity or treat it as an absent start eligible for replacement creation. Temporary inability to read is distinct from proven mandatory-record absence.

Confirmation checks necessary association/initial-record integrity; it does not require loading all historical Frames, Provider responses or external source payloads merely to prove the start succeeded. Physical integrity constraints and operation-error mapping remain with their actual Storage/Runtime contracts.

Intended destination: foundation/storage.md required semantic-start integrity and agent/execution-runtime.md confirmation failures. Actual writeback: this register only.

<a id="cg06-q37"></a>
### CG06-Q37 — Run duration comes from controlled execution configuration

Status: ACCEPTED. A finite Run-duration setting comes from the selected controlled execution configuration. Budget admission checks applicable bounds; Runtime derives and freezes the actual deadline at initial acceptance under Q7. Do not introduce an arbitrary independent caller timeout override. Same-start confirmation and later grant/recovery do not reset that deadline.

Intended destination: agent/execution-runtime.md configured duration/deadline and foundation/budget.md admission bounds. Actual writeback: this register only.

<a id="cg06-q38"></a>
### CG06-Q38 — Start associates an already valid Operation budget owner

Status: ACCEPTED. The owning Application establishes the required valid Operation budget owner before semantic-start. Start validates and atomically associates that owner under Q5/Q20; it does not create a default wallet, invent funds or silently select another owner. Same-request replay retains the original budget-owner selection.

Concrete Budget identities, owner-creation operations, reservations and settlement remain a dependent Budget branch. This decision alone adds no new generic pre-Run execution record.

Intended destination: foundation/budget.md owner prerequisites and agent/execution-runtime.md start association. Actual writeback: this register only.

<a id="cg06-q39"></a>
### CG06-Q39 — Skill-owned finite typed inputs, distinct from technical protection

Status: ACCEPTED with user amendment. Every registrable Skill must provide deterministic typed-input admission with finite structure/resource bounds. Reject over-limit input before creating a Run; never truncate it and continue. Exact field lengths, collection counts and business-object capacities belong to the first actual consumer Contract for that Skill, not a universal M2 semantic-input schema.

M2 may define genuinely needed bounded technical protections for semantic-start transport/runtime validation and fingerprint computation, including protection against unbounded structures. Such guards must be explicitly technical, not silently promoted to every Skill's business capacity. This round selects no numeric technical ceiling. Input-validation resource protection remains distinct from actual Context capacity and Budget's resource ledger.

SUPERSEDED proposal interpretation: using the requirement for finite admission to freeze uniform text, collection or nesting numbers for all future Skill business inputs. The deterministic admission, finite bounds and pre-Run rejection requirements remain effective; concrete consumer bounds stay with their owners.

Intended destination: agent/execution-runtime.md registration/admission and technical protection; actual Skill consumer Contracts for business-input bounds; agent/context.md only for its separate input-capacity seam. Actual writeback: this register only.

<a id="cg06-q40"></a>
### CG06-Q40 — Business dependency preparation stays outside semantic-start

Status: ACCEPTED. Semantic-start consumes the necessary already-prepared business inputs. Missing required dependencies produce a typed rejection; the start path cannot hide model parsing, another semantic Run or platform fetching. The owning Application explicitly orchestrates any required Ensure/production and owns its execution, cost and committed results.

Once dependencies are ready, freeze the logical request's exact inputs for its own start/confirmation agreement. This does not define RequirementParse/Ensure business semantics early or turn deterministic exact-source resolution into a hidden production operation.

Intended destination: agent/execution-runtime.md start prerequisites and actual Application consumer interfaces. Actual writeback: this register only.

## Round 4 persistence and local review

- Q31–Q40 are accepted, including stable historical fingerprint interpretation and Skill-owned business-input bounds. Q23's previously open representation statement now points to Q31 without rewriting its historical scope. The concrete format and encoder are still proposals for Round 5.
- Decision-to-Document Traceability: each conclusion has a prospective owner and explicit register-only writeback. The displaced Q31/Q39 interpretations remain visible. No universal input schema, bare-hash/current-algorithm assumption or rejection receipt was introduced.
- Cross-Document Semantic Consistency: checked COM-045/047/048, Architecture sections 9–10 and the M2 handoff's inherited creation/uncertainty rules against Q4/Q6/Q19–Q30. The existing Common encoder is available for a proposed M2 consumer, not already selected by this round. Historical confirmation remains distinct from fresh permission/execution, and start evidence does not duplicate actual Frame authority. The planned agent/context.md body is still absent; Architecture and accepted decisions supply the current design basis, not a fictional Ready Contract.
- Ordinary-round write set remains this register only. Concrete caller recovery, final request encoding, technical bounds and complete operation outcomes remain open; readiness remains Pending. No code, migration, live invocation or normative publication was performed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q40 anchors/headings, Q41–Q50 unanswered topic identities, all ten supersession annotations, explicit Q31/Q39 refinement checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish local document integrity only; no execution or publication evidence is claimed.

## Round 5 — Fingerprint representation and semantic Context boundaries

The user accepted Q41–Q50 with explicit amendments to Q47's historical-read/reuse distinction and Q48's Provider-effective semantic Frame boundary. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q41"></a>
### CG06-Q41 — Explicit fingerprint format and SHA-256 evidence

Status: ACCEPTED. The minimum successful-start association retains start_request_id, run_id, fingerprint_format_key and request_fingerprint. The initial format key is SemanticStartFingerprint:v1; the digest uses SHA-256 and existing Sha256Hex expression. Its input includes a fixed format prefix, an explicit separator and the deterministically encoded original typed request.

Runtime selects the format and computes the fingerprint; callers do not supply a claimed digest or select the comparison algorithm. Historical confirmation uses the stored format. Incompatible future rules require a new format, without a generic revision field. The precise separator bytes and complete request-envelope fields remain to be closed before publication.

Subsequent resolution: Q129 closes the top-level request-envelope fields, Q137 selects the configuration-reference shape and Q138 selects separator bytes. Skill-owned input semantics retain their respective owners.

Intended destination: agent/execution-runtime.md fingerprint definition and foundation/storage.md successful-start evidence; common.md for shared scalars only. Actual writeback: this register only.

<a id="cg06-q42"></a>
### CG06-Q42 — Reuse COM-045 deterministic typed encoding

Status: ACCEPTED. Semantic-start fingerprinting reuses COM-045: exact UTF-8 strings, canonical decimal numbers, ordered arrays and deterministically ordered object keys. Do not base equality on SDK serialization, dictionary insertion order, object string representations or a competing canonical-JSON protocol. Boolean values cannot masquerade as numbers.

The encoder acts on already-admitted values. The start envelope and actual Skill consumer own field participation and semantic canonicalization; Q39's business-input boundary remains. Existing COM-045 consumers, prefixes and equality semantics are unchanged.

Intended destination: agent/execution-runtime.md fingerprint consumer and common.md encoder-consumer scope. Actual writeback: this register only.

<a id="cg06-q43"></a>
### CG06-Q43 — Closed typed shapes with explicit field canonicalization

Status: ACCEPTED. Reject undeclared fields rather than silently discarding them. Do not perform implicit type coercion, text trimming or Unicode normalization. The owning field protocol must explicitly define missing/null/default equivalence; any required business canonicalization is a deterministic part of the Skill's admission before fingerprinting.

Historical requests retain their original interpretation rather than inheriting newer defaults. This defines admission discipline, not a universal business schema or a rule that every Skill must have the same fields/nullability.

Intended destination: agent/execution-runtime.md start-shape discipline and actual Skill input Contracts. Actual writeback: this register only.

<a id="cg06-q44"></a>
### CG06-Q44 — Compare submitted exact references without source rehydration

Status: ACCEPTED. Fingerprint the original typed request's exact references and literal inputs, including Skill, configuration selection and budget ownership. Do not dereference current business data or current pointers to reconstruct request meaning. Exclude Runtime-generated Run identity/time and final Frame content. start_request_id locates the association rather than becoming a business-content deduplication criterion.

Q36's necessary initial-record integrity checks remain. Historical confirmation does not require reloading referenced business bodies solely to compare the original request, and equal content under different start identities still does not merge Runs under Q29.

Intended destination: agent/execution-runtime.md fingerprint envelope/comparison and agent/context.md source-reference boundary. Actual writeback: this register only.

<a id="cg06-q45"></a>
### CG06-Q45 — Initial Context resolution uses typed Application reads

Status: ACCEPTED. Deterministic initial source resolution uses typed exact-read interfaces owned by Application/business sources; do not synthesize ToolInvocations for initialization reads. Source owners interpret exact references, supply content and the basis for permission checks. ContextBuilder checks task scope, assembles model input and evaluates capacity. ToolInvocationRuntime owns actual Tool actions during execution.

Initial reads retain scope, permission and persistence obligations. They cannot conceal Ensure, model calls or platform fetching. Do not fabricate a model-requested Tool event merely to populate an execution trajectory.

Intended destination: agent/context.md preparation/source interfaces and actual Application source Contracts; agent/tools.md actual invocation boundary. Actual writeback: this register only.

<a id="cg06-q46"></a>
### CG06-Q46 — Source-owner typed references, not a universal locator

Status: ACCEPTED. Context consumes typed references defined by their source owners. Each first actual consumer closes exact identity, read, permission and unavailability semantics. M2 may define common obligations such as exact identification and no fallback to latest, without an open source_type/arbitrary_id/arbitrary_uri/metadata locator.

When several supported source types require discrimination, use closed typed alternatives for those actual sources. Do not invent future file, URL, Memory or external-source fields before their consumers exist.

Intended destination: agent/context.md source interface obligations and actual source Contracts. Actual writeback: this register only.

<a id="cg06-q47"></a>
### CG06-Q47 — Package scope, source authority and historical read eligibility

Status: ACCEPTED with user amendment. ContextPackage retains initial scope, exact source references, capabilities/policy and admitted literal task inputs actually needed for recovery. It does not default to copying every referenced business body. Immutable business versions retain factual authority; producing Frames retain complete actual model-visible semantic input. A reference alone is not proof that its body has been retained. Any required recovery-source body needs an explicit retention agreement.

Historical Package/Frame evidence may continue to be read under Storage, audit and recovery protocols after execution permission is revoked. Such authorized internal reads can support integrity verification, audit and safe local recovery that does not expose the content to a model again. They are not an unrestricted evidence-access grant or an exemption from the applicable recovery/consumer-write protocol.

Any new model input, Tool-result reinjection or new remote effect must pass current permission/admission. Historical readability does not imply current reuse eligibility. Revocation neither erases the fact of prior input nor permits revoked content to enter a subsequent Frame. The inherited rule ending a frozen task after protected EAGER_EXACT input revocation remains effective.

SUPERSEDED proposal interpretation: the blanket phrase "current permission checks" forbids even authorized internal reading of legally persisted historical Frames after execution permission changes. Current execution/reuse admission and historical evidence-read eligibility are distinct, with their own owners.

Intended destination: agent/context.md Package/source/reuse boundaries; foundation/storage.md historical evidence reads; agent/execution-runtime.md admitted recovery. Actual writeback: this register only.

<a id="cg06-q48"></a>
### CG06-Q48 — Frame records Provider-effective semantic input

Status: ACCEPTED with user amendment. Skill/ContextBuilder forms semantic input; any Provider adapter mapping that changes role or schema semantics completes before the Frame freezes. ContextFrame stores the final determined Provider-effective model-visible semantic content. Gateway/SDK may then perform transport serialization, authentication and protocol adaptation only insofar as those preserve that frozen semantic content.

Retain frame_format_key, deterministic serialized Frame bytes, byte_length and sha256. These identify and verify JobHunter's exact semantic Frame, not the network request bytes. This is neither a stable clone of an SDK request object nor an obligation to retain HTTP bodies, SDK-private fields, authentication secrets or unrelated Provider transport detail. Provider/model and other non-Frame configuration retain Q4's semantic-binding ownership.

If a Provider/SDK can internally rewrite prompt, Tool schemas or role meaning beyond Runtime's control, strict agreement between the frozen Frame and submitted model-visible semantics is unproven. The adapter remains non-executable until research and implementation close that seam; do not manufacture a guessed Frame or claim current support. Exact Frame format fields/bytes and concrete adapter proof remain open. Q16 still means a committed Frame alone does not prove remote receipt.

SUPERSEDED proposal interpretation: Frame is a stable replacement for the SDK's final request object or its hash proves exact transport bytes. Its authority is Provider-effective semantic input, with all semantic mapping before freezing and only semantics-preserving transport work afterward.

Intended destination: agent/context.md exact Frame format/content; agent/execution-runtime.md adapter/Gateway admission; foundation/storage.md semantic-byte integrity. Actual writeback: this register only.

<a id="cg06-q49"></a>
### CG06-Q49 — Capacity capability is required for executable model configuration

Status: ACCEPTED. An executable model configuration must have an explicit context limit, an applicable actual-input calculation/estimation method, output reserve and safety margin. Account for the full actual input, including instructions, messages and Tool schemas. An unsupported capacity calculation blocks that Invocation rather than allowing a trial dispatch based on an informal character count.

A defined estimator with explicit applicability and margin is allowed; no universal exact tokenizer is required. No common numerical threshold is frozen. With Q48, this calculation must account for the effective semantic input and applicable Provider overhead; the semantic Frame hash is not a token estimate or network-body measurement. Concrete model/adapter support requires its own research and proof.

Intended destination: agent/context.md capacity admission and agent/execution-runtime.md executable adapter/configuration capabilities. Actual writeback: this register only.

<a id="cg06-q50"></a>
### CG06-Q50 — Retain committed Packages and Frames without an M2 purge subsystem

Status: ACCEPTED. Retain the initial Package and every committed Frame of an OPEN semantic Run as recovery evidence. Retain terminal Package/Frame payloads too; M2 delivers no cleanup operation. Completion of the producing Invocation alone does not permit deleting its Frame.

This does not pin every referenced business source forever. Source bodies follow their actual recovery dependencies and business-owned retention. A future actual cleanup consumer must close cleanup eligibility, evidence availability and historical confirmation together. No TTL, Pin entity or permanent retention duration is introduced.

Intended destination: agent/context.md evidence retention and foundation/storage.md active/terminal semantic payload retention. Actual writeback: this register only.

## Round 5 persistence and local review

- Q41–Q50 are accepted with Q47/Q48's refined boundaries. Q4 now points to the effective semantic-Frame and historical-read meaning; Q31 records Q41/Q42's later resolution without replacing its original proposal history. Exact fingerprint envelope and Frame bytes remain unfinished representation branches.
- Decision-to-Document Traceability: every accepted conclusion has prospective owners and register-only writeback. Both superseded interpretations remain explicit. No new evidence-access grant, universal source/input schema, SDK request snapshot or network-byte hash claim was introduced.
- Cross-Document Semantic Consistency: reviewed Architecture sections 9–10/12–13, COM-045/047/048 and EXR-018/019/023–025/029–032. Authorized historical reads do not grant execution or permit revoked protected tasks to publish current analysis. Raw byte integrity and semantic interpretation remain separate. Frame-before-intent publication and original live dispatch ownership remain Q16/M1 obligations; semantic adaptation is not an extra remote call. No particular SDK is asserted compatible without the deferred research.
- This round changes only this register. Concurrent implementation/navigation/Progress changes are preserved. M2 remains Pending, with no code, tests of execution, migration, live call or normative publication performed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q50 anchors/headings, Q51–Q60 unanswered topic identities, all twelve supersession annotations, explicit Q47/Q48 refinement checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish local document integrity only, not adapter compatibility or execution readiness.

## Round 6 — Frame evidence, capacity and single-action Tool admission

The user accepted Q51–Q60 with amendments to Q56's optional action replay protocol and Q59's workflow-owned scheduling. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q51"></a>
### CG06-Q51 — Internal raw Frame reads without execution authority

Status: ACCEPTED. Provide an internal raw-Frame read by invocation_id. Validate internal read access, immutable association and actual stored-byte hash/length; do not require an OPEN Run, execution grant or current permission to send the content to a model. Raw bytes remain readable without an available semantic decoder; interpretation separately requires the selected format capability.

Distinguish missing Invocation/type mismatch, Frame not yet published, missing required payload, integrity failure and storage unreadability. Reading performs no repair, Run ending or grant of continuation authority. Exact operation projections/error vocabulary remain for interface consolidation.

Intended destination: agent/context.md raw Frame read and foundation/storage.md evidence access/integrity. Actual writeback: this register only.

<a id="cg06-q52"></a>
### CG06-Q52 — Publication derives Frame integrity from actual bytes

Status: ACCEPTED. frame_format_key derives from the selected controlled protocol binding; the Runtime publication boundary validates the selected format and computes sha256/byte_length from the actual bytes being persisted. Do not trust caller-claimed integrity metadata or an arbitrary caller-selected format.

ContextBuilder and semantic adaptation form valid content. Publish the validated Frame and derived metadata atomically with Invocation intent under Q16. Reject nonconforming bytes rather than repairing, reinterpreting or inserting defaults at publication. This is semantic-byte integrity under Q48, not a transport hash.

Intended destination: agent/context.md Frame publication and agent/execution-runtime.md atomic intent interface. Actual writeback: this register only.

<a id="cg06-q53"></a>
### CG06-Q53 — Retain explainable capacity-admission evidence

Status: ACCEPTED. Retain minimum per-Invocation capacity evidence: exact capacity-rule/estimator identification, calculated or estimated input tokens, context capacity, output reserve and safety margin. All values must correspond to the same frozen Frame and actual model configuration. Exact immutable configuration references may explain applicable values without copying a second configuration authority.

This records the historical admission basis, not remaining budget or actual Provider usage. An earlier successful check grants no new call. Logical placement and complete field definitions remain to be consolidated with Frame/Invocation evidence.

Intended destination: agent/context.md capacity evidence and foundation/storage.md retained Invocation evidence. Actual writeback: this register only.

<a id="cg06-q54"></a>
### CG06-Q54 — One effective output cap across capacity and dispatch

Status: ACCEPTED. Controlled execution configuration determines the Invocation's effective output cap. Context capacity reserves for it, Budget calculates applicable reservation from it, and the adapter maps it to the actual Provider limit. The mapping must establish equivalent units and Provider meaning; similarly named token parameters do not by themselves establish equivalence.

Insufficient budget rejects admission rather than silently lowering the cap; Gateway cannot raise it. Variable-output policies require an actual consumer's explicit allowed range. This does not equate a reservation estimate with a Provider-guaranteed monetary ceiling.

Intended destination: agent/context.md output reserve, foundation/budget.md reservation input and agent/execution-runtime.md Provider mapping. Actual writeback: this register only.

<a id="cg06-q55"></a>
### CG06-Q55 — Finite semantic Frame byte protection

Status: ACCEPTED. A finite controlled max_frame_bytes protects local memory, serialization and persistence, separately from Skill business-input capacities, model token capacity and the Budget ledger. Check it before durable dispatch-intent publication and Provider entry. No permanent MiB value is selected here.

Over-limit Frames fail explicitly. Do not truncate the Frame and continue, or send full input while retaining truncated evidence. Complete typed failures and configuration placement remain open.

Intended destination: agent/context.md Frame-size protection and foundation/storage.md bounded semantic payloads. Actual writeback: this register only.

<a id="cg06-q56"></a>
### CG06-Q56 — Static Tool registration with opt-in re-execution

Status: ACCEPTED with user amendment. Static ToolRegistry registration closes stable action identity, owning Application handler, typed argument/result protocols, object/scope/current-permission admission, returned-content admission and completion evidence. These responsibilities may reference existing protocols/components instead of a single monolithic registration object. Incomplete required capabilities are non-executable; duplicate registrations cannot select an arbitrary winner. No database Tool configuration center, dynamic plugins or user scripts are introduced.

Registration explicitly classifies reexecution_classification as ALLOWED_BY_ACTION_PROTOCOL or NOT_REEXECUTABLE. Only an action allowing re-execution must reference its concrete recovery/replay agreement. Without such an agreement the effective classification is NOT_REEXECUTABLE; naming, read-like behavior or framework defaults cannot confer replay authority. An ALLOWED declaration without its required agreement is incomplete, not an executable permission.

SUPERSEDED proposal fragment: requiring every Tool to supply a complete recovery/re-execution protocol merely to register. Actions that prohibit re-execution need no speculative replay protocol. Typed completion/result evidence and all ordinary admission obligations remain required.

Intended destination: agent/tools.md static registration/classification and Application action interfaces; agent/execution-runtime.md action-protocol consumption. Actual writeback: this register only.

<a id="cg06-q57"></a>
### CG06-Q57 — Stable action identity and explicit Provider-name mapping

Status: ACCEPTED. Internal action keys are stable, exact and case-sensitive. Provider-visible Tool names are controlled mappings to these keys, unambiguous and explainable from the frozen input and associated configuration. Naming collisions make the affected configuration non-executable; do not silently choose or rename a target.

An action key retains its meaning; incompatible semantics require a new key. A model-produced name locates only a candidate action for validation, not permission. Concrete Provider naming support remains subject to adapter research.

Intended destination: agent/tools.md action identity and agent/execution-runtime.md Provider-name mapping. Actual writeback: this register only.

<a id="cg06-q58"></a>
### CG06-Q58 — Durable complete model response precedes Tool dispatch

Status: ACCEPTED. Model-origin Tool execution requires a complete model response persisted under the owned response protocol, followed by request interpretation/validation and current Tool admission. Streamed argument fragments cannot trigger action execution even when they appear complete.

This prevents an action from executing without durable evidence of its producing model response. Response durability alone grants no Tool permission. This decision does not force an invented model parent onto M1's controlled Application-initiated read consumer.

Intended destination: agent/tools.md model-request admission and agent/execution-runtime.md stream/response-to-Tool boundary. Actual writeback: this register only.

<a id="cg06-q59"></a>
### CG06-Q59 — Skill owns Tool-list scheduling; Runtime owns each invocation

Status: ACCEPTED with user amendment replacing the generic list policy. Current M2 semantic Runs retain active MODEL/TOOL Invocation <= 1. ToolInvocationRuntime executes one Tool request explicitly selected by Skill/Application, with independent admission, Invocation identity and evidence. Each selected request rechecks owner, current permission, deadline and its action protocol, together with other applicable resource admission.

The first actual Skill workflow consumer decides how to handle multiple requests in a model response: execute sequentially, select one, reject the list, and whether to continue after a failure. No such list scheduling/failure policy is frozen as a generic ToolInvocationRuntime invariant. Pending candidates are not blanket authorization for a batch.

A controlled M2 integration fixture may explicitly select sequential/stop-on-first-error behavior when its test protocol needs multiple requests. That proves only the declared fixture workflow through the real Harness; it adds no production probe Skill, parallel test Agent or generic Runtime policy.

SUPERSEDED proposal: Runtime universally processes every request in response order and stops on the first failure/rejection. Both ordering/selection and failure continuation belong to the actual Skill workflow. The single-active invariant and independent per-request execution remain effective; no generic batch transaction, durable queue or concurrency-policy object is added.

Intended destination: agent/tools.md single-action execution, agent/execution-runtime.md M2 serial admission and actual Skill consumer Contracts for list policy. Actual writeback: this register only.

<a id="cg06-q60"></a>
### CG06-Q60 — Strict bounded Tool argument parsing

Status: ACCEPTED. Arguments must match the declared action shape. JSON representations reject duplicate keys, trailing content and incomplete documents. Reject undeclared fields and implicit type coercion. Parsing has finite technical resource protection; business capacities remain action-owned. Do not extract a plausible JSON fragment, silently drop fields or repair arguments before execution.

A parse failure supplies no action execution eligibility. If the Skill permits model-guided correction, it is a separately admitted, counted and evidenced model invocation, never a hidden call inside the parser. This grants no generic repair allowance or list-scheduling policy.

Intended destination: agent/tools.md argument admission and common.md only for actually shared validation expression. Actual writeback: this register only.

## Round 6 persistence and local review

- Q51–Q60 are accepted with Q56/Q59 amendments. The register preserves rejected mandatory-recovery and generic sequential/stop-on-error interpretations. The fixture example remains test-scoped and does not supersede Q1's real-path/no-production-probe boundary.
- Decision-to-Document Traceability: each conclusion identifies prospective owners and register-only writeback. No action gains replay permission by registration alone. No Skill list policy, blanket Tool batch authorization or new remaining-budget authority has been silently added.
- Cross-Document Semantic Consistency: checked EXR-029/030's default-deny replay boundary, Architecture sections 9/11/12 and Harness Tool/Budget provenance against Q1/Q3/Q8/Q47–Q50. NOT_REEXECUTABLE does not require speculative replay machinery; current M2 serial admission does not define Agent-loop scheduling. Historical Frame reads remain separate from execution, and capacity evidence is not actual usage. Detailed Tool result protocols and Budget interfaces remain open.
- Only this register was edited. M2 remains Pending; no normative publication, implementation, live invocation or execution test is claimed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q60 anchors/headings, Q61–Q70 unanswered topic identities, all fourteen supersession annotations, explicit Q56/Q59 amendment checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not execution or publication evidence.

## Round 7 — Tool completion truth and initial Budget interfaces

The user accepted Q61–Q70 with amendments to Q63's outcome separation, Q67's optional monetary envelope and RMB default, and Q68's minimum historical pricing basis. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q61"></a>
### CG06-Q61 — Trace a selected Tool request to its durable model response

Status: ACCEPTED. A model-origin Tool request retains a verifiable locator consisting of its producing ModelInvocation identity and deterministic position in the complete durable response. Runtime uses that response and its format to verify that the selected action/arguments agree with the submitted request; intermediaries cannot silently substitute a different model instruction.

Provider tool-call IDs may support protocol correlation, but are neither global invocation identities nor replay permissions. Application-origin controlled reads need no fabricated model parent. Concrete locator fields depend on the response format and remain open; this decision alone does not define workflow scheduling or a generic idempotency framework.

Subsequent resolution: Q141 selects the current DeepSeek locator fields; Q142 bounds the source-request association to one TOOL Invocation, and Q143 derives model-origin action/arguments from the durable response rather than accepting an independent duplicate payload. Other response formats retain their own locator obligations.

Intended destination: agent/tools.md model-request provenance and agent/execution-runtime.md response-to-action association. Actual writeback: this register only.

<a id="cg06-q62"></a>
### CG06-Q62 — Existing result reads are not action re-execution

Status: ACCEPTED. NOT_REEXECUTABLE prohibits invoking the action again through recovery; it does not prohibit authorized reads/integrity checks of existing durable completion evidence. Reading an existing result and calling its handler again are distinct operations.

Reinjection into a model needs current Context admission; a consumer business write needs its own recovery/write eligibility. The classification neither grants these permissions nor makes lawful historical evidence unreadable.

Intended destination: agent/tools.md result reuse/re-execution distinction and actual action recovery consumers. Actual writeback: this register only.

<a id="cg06-q63"></a>
### CG06-Q63 — Invalid result representation cannot erase action completion

Status: ACCEPTED with user amendment. A handler result that violates its declared schema is an action implementation/result-protocol error and cannot enter Context as a valid successful Tool result. Do not repair fields, coerce types or ask a model to fix the representation implicitly.

Keep action outcome separate from Tool result representation/admission outcome. If the action reliably completed and completion evidence exists, that completion remains true even when its projection or result encoding fails. A single aggregate FAILED label must not erase or imply absence of known action completion. If completion is not established, do not fabricate it. Confirmation follows the action's evidence agreement, never re-execution merely to obtain a well-formed return value.

Whether these distinctions require separate persisted fields/records remains open. The invariant is independent preservation of execution truth, consistent with Q64; no universal business-failure object or generic Tool lifecycle is introduced.

SUPERSEDED proposal interpretation: an invalid handler-return schema reduces the entire ToolInvocation to an undifferentiated FAILED outcome that implies the action never completed. Representation/admission failure remains explicit without overwriting reliable completion evidence.

Intended destination: agent/tools.md outcome/evidence distinctions and Application action completion/result protocols. Actual writeback: this register only.

<a id="cg06-q64"></a>
### CG06-Q64 — Context rejection does not rewrite action execution facts

Status: ACCEPTED. Record action execution/completion evidence independently from whether Context admits returned content. Rejection after execution, including permission revocation before the next Frame, cannot rewrite the action as never executed or cost-free. Prior execution success cannot bypass current content permission either.

Internal evidence retention follows Storage/action agreements. Task ending or another workflow branch follows applicable protected-input rules and the actual Skill protocol; no generic continuation policy is added.

Intended destination: agent/tools.md action evidence, agent/context.md returned-content admission and foundation/storage.md internal evidence. Actual writeback: this register only.

<a id="cg06-q65"></a>
### CG06-Q65 — Bounded Tool results without truncated-success fiction

Status: ACCEPTED. Every executable action defines finite result-handling constraints, distinguishing technical protection from action-owned business capacity. No universal business-result length is selected. Over-limit results cannot be silently truncated and reported as complete success.

Pagination, projection or externalization is allowed only under the actual declared action protocol with truthful scope/completeness. Distinguish a known-completed action whose result cannot be fully admitted from interrupted reception with unknown completion; a local limit does not prove absence of remote work. Q63/Q64's separate execution/result facts remain applicable.

Intended destination: agent/tools.md bounded result handling and actual action result/completion Contracts. Actual writeback: this register only.

<a id="cg06-q66"></a>
### CG06-Q66 — M2 Operation allocations are immutable

Status: ACCEPTED. M2 freezes an Operation's allocated limits. Available capacity changes through reservation, settlement and lawful reconciliation, but M2 offers no allocation top-up, cross-Operation transfer or automatic renewal. Configuration updates apply to new Operations; restart, recovery or failure cannot refill an existing allocation.

This is current delivery scope, not a permanent prohibition on future explicitly authorized budget adjustments. A future actual adjustment consumer must define authorization, concurrency and historical interpretation. The decision does not select the complete set of mandatory resource dimensions; Q67 permits Operations without monetary envelopes.

Intended destination: foundation/budget.md Operation allocation and Application owner interfaces. Actual writeback: this register only.

<a id="cg06-q67"></a>
### CG06-Q67 — Optional monetary budgets use exact amounts and RMB by default

Status: ACCEPTED with user amendment. Any Operation that enables a monetary budget must have explicit accounting currency and exact decimal amount semantics with bounded precision/range, not binary-floating-point ledger comparisons. There is no implicit foreign exchange or direct aggregation across unlike monetary units. Currency-bearing defaults throughout this M2 design use renminbi (RMB/CNY), not USD.

An Operation may constrain only nonmonetary resources such as tokens, calls, steps or deadline. Such a consumer is not forced to manufacture currency or a null monetary_limit merely for a uniform schema. Concrete supported currencies, amount precision and rounding remain open; the CNY default is not an assertion that every Provider bills in CNY or that M2 supplies currency conversion.

Q79 subsequently freezes the project default as DeepSeek API with RMB/CNY monetary Budget accounting. This makes the default an explicit prospective Budget Contract decision while preserving optional monetary envelopes and the absence of implicit FX.

SUPERSEDED proposal interpretation: every Operation must declare a currency even when it has no monetary envelope. Explicit currency is required only when monetary accounting applies. Exact amounts, explicit units and no implicit FX remain effective; the user additionally establishes the RMB default.

Intended destination: foundation/budget.md monetary versus nonmonetary scopes and common.md only for shared exact amount expression. Actual writeback: this register only.

<a id="cg06-q68"></a>
### CG06-Q68 — Immutable pricing explanation without a price catalog entity

Status: ACCEPTED with user amendment. A call requiring monetary reservation must have an applicable controlled pricing basis identifying Provider/model, charge dimensions and units. Missing or inapplicable pricing blocks new monetary admission; it is not zero cost. An explicitly supported free capability may have a zero rate with an actual basis. This requirement does not force monetary pricing onto Q67's nonmonetary-only consumers.

Retain enough immutable basis/reference to explain each historical monetary reservation exactly. An exact configuration reference, immutable snapshot or another frozen representation may satisfy this obligation; later configuration changes must not change the original estimate's meaning. This pricing is an admission estimate, not a claim about the Provider's final invoice.

SUPERSEDED proposal interpretation: requiring historical pricing explanation mandates a complete versioned PriceRule entity, price catalog lifecycle or Provider billing subsystem. Only the actual reservation consumer's immutable explanatory basis is required; concrete representation remains open.

Intended destination: foundation/budget.md pricing basis/reservation evidence and controlled Provider configuration references. Actual writeback: this register only.

<a id="cg06-q69"></a>
### CG06-Q69 — Model reservation and dispatch intent commit atomically

Status: ACCEPTED. For M2 MODEL calls, one local atomic boundary validates current execution/budget eligibility and commits the reservation/applicable count occupancy, frozen Frame and dispatch intent. Do not expose an admitted sending intent without budget protection or a separate committed reservation awaiting intent repair.

Computation, semantic mapping and necessary preparation happen outside the transaction; participating mutable authority is rechecked inside. Network work remains outside. This uses Q16's Frame/intent publication boundary and does not impose MODEL's transaction/phase protocol on every TOOL action. Exact budget identity, counters and settlement operations remain open.

Intended destination: foundation/budget.md reservation, agent/execution-runtime.md model admission and foundation/storage.md atomic publication. Actual writeback: this register only.

<a id="cg06-q70"></a>
### CG06-Q70 — Budget reconciliation can outlive Run execution

Status: ACCEPTED. Budget may use trusted late evidence through an independent idempotent reconciliation protocol after a Run ends, updating known usage and unresolved exposure. It must not reopen the Run, authorize stale business-result publication, rewrite the Frame, fabricate a complete response or settle the same work twice.

Do not call the model again to discover cost. Exact evidence sources, conflict handling and release conditions remain to be closed. Execution termination does not imply zero expense or prohibit later lawful accounting clarification. This adds no implicit polling service, remote billing integration or generic late-response acceptance.

Intended destination: foundation/budget.md late evidence/reconciliation and agent/execution-runtime.md terminal execution boundary. Actual writeback: this register only.

## Round 7 persistence and local review

- Q61–Q70 are accepted with Q63/Q67/Q68 refinements. Known action completion survives representation/admission failures. Monetary envelopes are optional; applicable currency defaults are RMB/CNY. Immutable pricing explanation does not imply a PriceRule entity.
- Decision-to-Document Traceability: each conclusion names prospective owners and register-only writeback; all three displaced interpretations remain visible. Separate Tool outcome fields, full monetary representation and pricing-reference shape remain open rather than being inferred from the amendments.
- Cross-Document Semantic Consistency: checked Architecture section 11 and Harness Budget sections 4–7 with Q3/Q47/Q56/Q62–Q64 and M1's action-specific evidence/late-write boundaries. Atomic MODEL reservation adds the M2 consumer seam without changing M1 controlled-call protocols or forcing MODEL phases onto Tools. Late accounting does not restore execution authority. Historical design examples using dollar values remain historical examples, not currency defaults or a reason to rewrite unrelated owners during this round.
- Only this register was edited. M2 remains Pending; no normative publication, implementation, price lookup, conversion service, live invocation or execution test is claimed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q70 anchors/headings, Q71–Q80 unanswered topic identities, all seventeen supersession annotations, explicit Q63/Q67/Q68 refinement checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not execution or publication evidence.

## Round 8 — Reservation, usage evidence and CNY accounting

The user accepted Q71–Q80 and explicitly directed Q79 to freeze DeepSeek API as the intended default Provider and RMB/CNY as the default monetary accounting currency in the prospective Budget Contract. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q71"></a>
### CG06-Q71 — Reservation accounting is keyed by Invocation

Status: ACCEPTED. Use invocation_id to locate an Invocation's logical resource reservation and its Run/Operation ownership. Applicable resource dimensions may share that logical association. Do not add a separate reservation_id or reservation-request idempotency identity merely to express the same accounting event.

Repeated processing confirms the original owner and values rather than charging twice or changing the allocation under the same identity. Physical storage may use separate rows without new business identities. Complete reservation representations remain open.

Intended destination: foundation/budget.md reservation identity and agent/execution-runtime.md Invocation association. Actual writeback: this register only.

<a id="cg06-q72"></a>
### CG06-Q72 — Reserve call allowance before dispatch

Status: ACCEPTED. Occupy the applicable call allowance in Q69's atomic intent transaction rather than waiting for the Provider response. Concurrent paths cannot claim the same last available call. Reliably proven undispatched work may return this occupancy under the safe-release protocol; sent or possibly sent work retains consumed/possibly consumed allowance.

Validation failure, unacceptable business output, timeout or lost response does not automatically refund a call. This concerns call allowance, not erasing elapsed time or local steps/work already performed. Exact count-state representation remains open.

Intended destination: foundation/budget.md call counters and agent/execution-runtime.md dispatch/release boundary. Actual writeback: this register only.

<a id="cg06-q73"></a>
### CG06-Q73 — Response durability does not depend on settlement success

Status: ACCEPTED. Lawful complete-response persistence does not require Budget settlement to succeed first. Preserve the recoverable response and permitted usage evidence; Budget settlement can continue independently and idempotently. Retain the original reservation until its settlement/release is confirmed.

Later dispatch uses the actual ledger including unresolved occupancy. An implementation may combine compatible local operations transactionally, but the Contract does not make response and settlement success inseparable. Never recall the Provider to repair accounting.

Intended destination: agent/execution-runtime.md complete response and foundation/budget.md recoverable settlement; foundation/storage.md corresponding evidence. Actual writeback: this register only.

<a id="cg06-q74"></a>
### CG06-Q74 — Usage certainty is component-specific

Status: ACCEPTED. Represent known, estimated and unknown usage per actual metering component, with its basis. Known input tokens do not imply known output tokens or known cost. Do not fill unknown values with zero or present an estimate as a measurement.

Known tokens evaluated under a controlled price basis explain cost under that basis; they do not automatically prove the Provider's final invoice. Actual fields follow supported dimensions rather than a universal Provider usage schema. Complete expression and settlement eligibility remain to be closed.

Intended destination: foundation/budget.md usage evidence and actual Provider adapter metering interfaces. Actual writeback: this register only.

<a id="cg06-q75"></a>
### CG06-Q75 — Record overruns without refilling or falsifying allocation

Status: ACCEPTED. Record trustworthy usage beyond reservation/allocation honestly, without clipping consumption or automatically enlarging the Operation. Reevaluate subsequent affected-resource dispatch against actual remaining capacity and reject insufficient admission.

Independent committed business results remain intact. Necessary safe local reconciliation follows its own admission. Reservation protects admission against known oversubscription; it is not a guarantee about the final Provider charge. No new budget adjustment operation is authorized.

Intended destination: foundation/budget.md overrun and subsequent admission; Application consumer result boundaries. Actual writeback: this register only.

<a id="cg06-q76"></a>
### CG06-Q76 — Complete response alone does not release unknown usage

Status: ACCEPTED. Response completion and settleable usage are distinct facts. Without sufficient evidence under the settlement protocol, preserve the corresponding conservative occupancy. Do not infer zero usage or release exposure solely because the Run ended or time elapsed.

Controlled estimates may be explicitly recorded, but what estimates authorize settlement and how much occupancy they release require an explicit agreement. M2 introduces no automatic expiry-to-zero policy. Subsequent resolution: Q208 permits estimates for reservation/capacity/evidence but excludes their use to finalize unknown token/CNY usage or release its unresolved reservation.

Intended destination: foundation/budget.md unknown usage/exposure and settlement eligibility. Actual writeback: this register only.

<a id="cg06-q77"></a>
### CG06-Q77 — Only admitted usage evidence informs the ledger

Status: ACCEPTED. Budget accepts usage evidence only from its recognized protocols: controlled adapter extraction of Provider protocol fields, explicitly marked controlled local estimation, or a future actually integrated and verified reconciliation source. Model-generated prose, Tool content and ordinary logs cannot certify their own usage. Derived observability, including Langfuse, is not an independent accounting authority.

The adapter validates field types, units, nonnegative values and applicability. Missing values remain unknown rather than defaulting to zero. Specific Provider fields and supported sources need research and exact mapping before execution.

Intended destination: foundation/budget.md evidence admission, agent/execution-runtime.md adapter usage mapping and evaluation/evaluation-observability.md derived telemetry. Actual writeback: this register only.

<a id="cg06-q78"></a>
### CG06-Q78 — Undispatched release requires proof and fencing

Status: ACCEPTED. Safe release requires reliable proof that adapter entry into the sending boundary has not occurred, plus fencing of the original path before or atomically with release so it cannot send afterward. Missing response or a cancelled coroutine alone proves neither condition.

A restarted process cannot reconstruct this proof merely from durable intent and no response. Cancellation requests, connection errors and timeout do not by themselves prove the remote service received nothing. Preserve M1's original-live-winner distinction and uncertain-outcome truth.

Intended destination: foundation/budget.md safe release, agent/execution-runtime.md original-path/fencing interface and foundation/storage.md atomic coordination. Actual writeback: this register only.

<a id="cg06-q79"></a>
### CG06-Q79 — DeepSeek default and explicit CNY Budget Contract decision

Status: ACCEPTED with explicit user addition. The project intends to use DeepSeek API by default. RMB/CNY is frozen as the default accounting currency for monetary Budget consumers, as an explicit decision for the future foundation/budget.md Contract, not merely an illustrative display preference. This does not enable money budgets for every Operation, select a specific DeepSeek model/SDK or freeze numeric prices.

Subsequent scope refinement: CG06-S2 selects only the official DeepSeek API for M2 production integration while retaining one ModelGateway port/DeepSeekAdapter; Q81 limits M2 monetary accounting to CNY. This historical default statement does not authorize additional production Providers or currencies.

A CNY monetary admission requires an explainable controlled CNY pricing basis. Direct CNY budget rates may be configured. If a basis derives from foreign-currency rates, freeze the source prices, conversion parameters and rules explicitly enough to preserve historical meaning under Q68. Do not reinterpret foreign-currency numbers as CNY, infer free usage, query live FX implicitly or introduce an FX service as M2 infrastructure.

If no applicable CNY basis exists, reject that monetary admission. Nonmonetary-only consumers retain Q67's separate scope. Research must establish actual DeepSeek capabilities/pricing dimensions before dependent adapter choices; default intent is not proof of executable integration.

Intended destination: foundation/budget.md default currency and controlled pricing basis; agent/execution-runtime.md default Provider configuration direction where applicable. Actual writeback: this register only. Normative publication remains the separately authorized closure stage.

<a id="cg06-q80"></a>
### CG06-Q80 — Idempotent settlement and explicit evidence conflicts

Status: ACCEPTED. Repeated identical valid evidence confirms the original settlement without duplicate charge or release. Previously unknown usage may converge through its explicit trusted-evidence protocol. Evidence conflicting with already accepted definite settlement facts produces a conflict rather than last-write-wins replacement or summing both values.

Preserve explainable existing accounting and prevent unsafe release based on disputed evidence. A future actual Provider correction consumer must define its own correction agreement; no generic financial event system is added now. Complete comparison/evidence identities and error projections remain open.

Intended destination: foundation/budget.md settlement/reconciliation and foundation/storage.md atomic accounting consistency. Actual writeback: this register only.

## Round 8 persistence and local review

- Q71–Q80 are accepted. Q79 records the explicit DeepSeek default and CNY monetary accounting decision; Q67 points to that later clarification while retaining optional monetary envelopes. No specific model, SDK, numeric rate or mandatory conversion subsystem was inferred.
- Decision-to-Document Traceability: every decision has prospective owners and register-only writeback. Reservation identity, unknown exposure, settlement independence and trusted evidence are separated from Run/Tool business outcomes. CNY is a Contract-design decision awaiting authorized publication, not a claim that the pending Budget body already exists.
- Cross-Document Semantic Consistency: checked Q69–Q70 with M1 intent/response/recovery boundaries and Harness Budget sections 4–7. Unknown sending cannot obtain a refund through absence of response; late settlement grants no sending or business-write authority. Complete response persistence is independent of accounting progress, with outstanding reservation retained. No zero-cost or automatic replenishment path is added.
- This round changes only this register. Official Provider documentation research is read-only; no installation, live API invocation, billing query, implementation or normative publication is authorized or claimed. M2 remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q80 anchors/headings, Q81–Q90 unanswered topic identities, all prior supersession annotations, the explicit Q79 DeepSeek/CNY decision, the research locator, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish local documentation integrity only, not adapter compatibility or execution readiness.

<a id="cg06-r1"></a>
## CG06-R1 — Bounded DeepSeek documentation research

Read-only official-source inspection on 2026-09-23, assisted by one bounded research agent and checked against the linked pages. These are observed documentation facts, not accepted adapter choices or executable proof.

- [Chinese pricing](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/) lists CNY input cache-hit/cache-miss and output rates, peak/off-peak periods, and mutable legacy model routing. No numeric price, model choice or billing-boundary timestamp rule is frozen here.
- [Cache guidance](https://api-docs.deepseek.com/guides/kv_cache/) describes best-effort caching; future hits are not guaranteed. [Chat Completions reference](https://api-docs.deepseek.com/api/create-chat-completion/) documents input cache partitions, output/reasoning breakdowns and final-chunk usage. This does not guarantee delivery after interruption or select that protocol for M2.
- [Thinking guidance](https://api-docs.deepseek.com/guides/thinking_mode/) describes a current enabled default and mode-dependent handling of prior reasoning content with Tools. [Token guidance](https://api-docs.deepseek.com/quick_start/token_usage/) treats offline token calculation as an estimate. Neither proves a specific SDK preserves exact semantic Frames or supplies a safe complete-request bound.

Remaining research gates: selected API/model/SDK and pinned sources/licenses, hidden retries/semantic transformations, exact complete-response/stream conditions, pricing-time applicability, supported metering fields and capacity proof. The scoped pyproject.toml search found no matching DeepSeek/OpenAI/LangGraph/Langfuse entry; that negative search is not a full dependency audit. No SDK installation or live API call occurred.

## Round 9 — DeepSeek monetary accounting and Provider observations

The user's response supplies the Q89 amendment, no further changes to Q81–Q88/Q90, and affirmative single-DeepSeek/CNY scope rationale. The effective Q81–Q90 recommendations are accepted with that amendment; CG06-S2 records the supplementary architecture/scope direction. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q81"></a>
### CG06-Q81 — CNY-only monetary support in M2

Status: ACCEPTED. M2 monetary budgets accept only CNY; reject non-CNY configuration rather than silently converting it. Do not implement currency conversion or cross-currency aggregation. A future actual consumer may extend this delivery scope. Nonmonetary budgets do not acquire artificial currency fields.

Intended destination: foundation/budget.md supported accounting currency. Actual writeback: this register only.

<a id="cg06-q82"></a>
### CG06-Q82 — Controlled rate configuration, not live discovery

Status: ACCEPTED. Admission uses reviewed, exactly identified controlled pricing configuration containing supported dimensions, units and CNY rates. New configuration affects subsequent admission; historical reservations retain their original basis. Numeric rates belong to configuration, not permanent Contract constants.

Do not query pricing webpages in the invocation path or database transaction, or create a price-catalog entity. This does not establish a live price-monitoring service or claim rates never change.

Intended destination: foundation/budget.md controlled pricing input and Provider configuration. Actual writeback: this register only.

<a id="cg06-q83"></a>
### CG06-Q83 — Reserve input cost without assuming cache hits

Status: ACCEPTED. Default reservation assumes all applicable input misses the Provider cache, together with the applicable output allowance. Later trusted cache metering is handled under settlement rules. Locally equal prompts or recent calls do not prove a future cache discount.

This is a conservative admission policy supported by CG06-R1's best-effort-cache finding, not an assertion about any individual request's actual cache result.

Intended destination: foundation/budget.md input-cost reservation. Actual writeback: this register only.

<a id="cg06-q84"></a>
### CG06-Q84 — Validate cache partitions without double-counting

Status: ACCEPTED. In the supported metering semantics, input_total equals cache_hit plus cache_miss. These are a total and its partition, not three additive charges. Monetary calculation applies the appropriate partition rates; logical token input is counted once.

Validate the relationship. If evidence is inconsistent or required components are missing, preserve reliable components and keep unsupported portions unknown; do not insert zeros or alter values to force agreement. Actual wire-field mapping remains adapter-owned and research-dependent.

Intended destination: foundation/budget.md normalized usage and DeepSeekAdapter metering admission. Actual writeback: this register only.

<a id="cg06-q85"></a>
### CG06-Q85 — Conservative rate choice across uncertain billing time bands

Status: ACCEPTED. When the applicable Provider billing time band cannot be established reliably, reserve using the higher potentially applicable rate within the controlled pricing basis. Local admission in a discount period does not prove discounted Provider billing.

This is a conservative budget policy, not a guarantee about the final charge. Do not add a holiday-calendar service merely to guess billing. Exact controlled rate applicability and billing-time interpretation remain subject to the actual supported protocol.

Intended destination: foundation/budget.md time-dependent pricing uncertainty. Actual writeback: this register only.

<a id="cg06-q86"></a>
### CG06-Q86 — Internal settlement may use trusted usage and frozen budget rates

Status: ACCEPTED. A defined internal Budget protocol may settle trusted usage against the applicable frozen budget rates, release excess reservation or record an overrun without requiring the final Provider invoice first. Preserve the meaning as internal budget-priced usage, not invoice-confirmed cost.

This closes Q76's permitted settlement-basis branch only where usage and applicable pricing suffice. Missing usage or inapplicable pricing does not authorize release. No Provider billing subsystem is required.

Intended destination: foundation/budget.md settlement basis and accounting evidence. Actual writeback: this register only.

<a id="cg06-q87"></a>
### CG06-Q87 — Reasoning is not an additional output total

Status: ACCEPTED. Normalize output accounting using verified containment relationships. Where reasoning tokens are a completion subcomponent, do not add them to the completion total again. Output allowances and cost cover the actual generated total, not just user-visible answer text.

Other supported protocols/models require their own verified mapping; similar field names alone are insufficient. This decision does not select an API family or prescribe retention of reasoning payloads.

Intended destination: foundation/budget.md output metering and DeepSeekAdapter usage interpretation. Actual writeback: this register only.

<a id="cg06-q88"></a>
### CG06-Q88 — Explicit effective thinking configuration

Status: ACCEPTED. Controlled execution configuration explicitly determines thinking mode and applicable parameters, freezing their effective meaning rather than relying on mutable Provider defaults. Supported behavior must close output allowance, complete-response and subsequent-Frame implications; otherwise the configuration is non-executable.

No single enabled/disabled mode is selected for every Skill. Concrete parameter names and capability combinations belong to the selected adapter/configuration protocol.

Intended destination: agent/execution-runtime.md effective model configuration and agent/context.md mode-dependent semantic input. Actual writeback: this register only.

<a id="cg06-q89"></a>
### CG06-Q89 — Optional Provider fingerprint is observation, not immutable model identity

Status: ACCEPTED with user amendment. Retain the configured/requested model identifier and actual returned model identifier, plus returned system_fingerprint when the Provider supplies it, as optional Provider observation evidence. The current DeepSeek Chat Completions description identifies system_fingerprint with backend configuration; it does not establish JobHunter-verifiable immutable model weights.

Eval/audit may report requested model, returned model and observed system_fingerprint. Equal strings/fingerprints across Runs do not prove identical underlying weights. Do not fabricate missing version/fingerprint data. Controlled configuration may explicitly allow an alias, while exact request-configuration reproducibility remains distinct from immutable backend/model reproducibility. Detected capability incompatibility requires adapter review, not silent local fallback.

The optional internal observation does not itself define every selected wire protocol's required-field validation; that interface remains to be closed. This amendment expands Q89's evidence set without superseding its original no-immutable-weight-claim rule. It introduces neither a model-version entity nor a backend identity authority.

Intended destination: agent/execution-runtime.md Provider observations and evaluation/evaluation-observability.md honest reproducibility claims. Actual writeback: this register only.

<a id="cg06-q90"></a>
### CG06-Q90 — Cache discounts do not reduce logical token limits

Status: ACCEPTED. Current token limits count complete logical input, cache hits plus misses. Cache discounts affect applicable monetary pricing, not the amount charged against logical input-token allowances or the input's Context capacity requirement.

Different future compute-resource limits need an actual consumer and explicit meaning rather than silently redefining current token counters.

Intended destination: foundation/budget.md token allowance semantics and agent/context.md capacity distinction. Actual writeback: this register only.

## Round 9 persistence and local review

- Q81–Q90 are accepted with optional Provider system_fingerprint evidence under Q89. CG06-S2 records the supplementary single-production-DeepSeek boundary and preserves ModelGateway/adapter separation; Q79's earlier default scope is annotated rather than rewritten as historical exclusivity.
- Decision-to-Document Traceability: all decisions have prospective owners and register-only writeback. Adapter protocol interpretation does not take over Budget policy or Runtime authority. CNY-only support still does not force every Operation to enable monetary accounting. No actual API family, model, SDK or rate was selected.
- Cross-Document Semantic Consistency: checked Architecture sections 9/11/15 and Q48/Q67–Q70/Q74/Q79 against the new decisions. Semantic preparation still precedes Frame freezing; the dispatch chain does not permit late semantic transformations. Internal priced settlement is distinct from invoice truth, and optional Provider observations are distinct from immutable identity. Official Chat Completions documentation confirms the backend-configuration description; its wire-required marker is not silently generalized into JobHunter's optional observation model.
- This round changes only this register. Source/documentation research is read-only; no install, live Provider call, production integration or normative publication was performed. Readiness remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q90 anchors/headings, Q91–Q100 unanswered topic identities, all prior supersession annotations, Q89's observation amendment, CG06-S2/CG06-R2 identities, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not production transport or adapter proof.

<a id="cg06-r2"></a>
## CG06-R2 — Provider observations and pinned HTTPX transport facts

Read-only inspection on 2026-09-23, with one bounded factual research agent. The [DeepSeek Chat Completions reference](https://api-docs.deepseek.com/api/create-chat-completion) describes system_fingerprint as backend-configuration evidence in both nonstream and stream schemas, currently marked required there. Q89 intentionally treats it as optional internal observation, without an immutable-weight claim; exact external response validation remains unfinished. [DeepSeek's first-call guide](https://api-docs.deepseek.com/) presents multiple compatible API surfaces; single-Provider scope does not select an API family or SDK by itself.

Local pyproject.toml and uv.lock pin HTTPX 0.28.1 in the development dependency group; the maintained technology-stack guide chooses HTTPX for HTTP adapters. Production dependency placement is not yet supplied by these facts. Fixed-version upstream evidence:

- [Client source](https://raw.githubusercontent.com/encode/httpx/0.28.1/httpx/_client.py): AsyncClient defaults follow_redirects to false and trust_env to true. Custom auth, hooks and transports can change behavior; choosing the library alone proves no single-send invariant.
- [Transport source](https://raw.githubusercontent.com/encode/httpx/0.28.1/httpx/_transports/default.py): AsyncHTTPTransport defaults retries to zero. This does not classify a failed connection as proven undispatched or establish exactly-once remote effects.
- [Configuration source](https://raw.githubusercontent.com/encode/httpx/0.28.1/httpx/_config.py) and [proxy utilities](https://raw.githubusercontent.com/encode/httpx/0.28.1/httpx/_utils.py): environment trust affects certificates/proxies, including possible OS proxy discovery. Explicit controlled configuration needs its own choice.
- [Body encoding source](https://raw.githubusercontent.com/encode/httpx/0.28.1/httpx/_content.py): bytes/JSON encoding supplies transport building blocks without DeepSeek role/Tool semantics. A thin direct-HTTP adapter is therefore a feasible candidate, not an accepted implementation.
- [Version manifest](https://raw.githubusercontent.com/encode/httpx/0.28.1/pyproject.toml) and [license](https://raw.githubusercontent.com/encode/httpx/0.28.1/LICENSE.md): BSD-3-Clause, with its distribution/notice obligations. No broader dependency-license or httpcore sending-behavior audit is claimed.

No dependencies were installed or changed. SSE parsing, completion predicates, semantic equivalence, effective request parameters, usage extraction and faults still require a selected adapter's exact protocol and tests. This research does not make M2 ready.

## Round 10 — Controlled DeepSeek transport and response boundaries

The user accepted Q91–Q100 with explicit refinements to Q92/Q93's library-independent Contract boundary and Q98's current DeepSeek configuration scope. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q91"></a>
### CG06-Q91 — First production API is DeepSeek Chat Completions

Status: ACCEPTED. M2 first integrates the official DeepSeek Chat Completions protocol for required text, Tool requests and streamed responses. Do not implement Responses or another API family in this first scope. Close one actual message, terminal, usage and error protocol. This selects no particular model or numeric configuration defaults.

Intended destination: agent/execution-runtime.md supported production adapter protocol. Actual writeback: this register only.

<a id="cg06-q92"></a>
### CG06-Q92 — HTTPX is the first implementation choice, not Runtime law

Status: ACCEPTED with user refinement. M2's first implementation uses the existing HTTPX choice as a thin HTTP client without adding a model SDK. DeepSeekAdapter owns Chat Completions mapping, stream parsing, usage, Tool-call and Provider-error interpretation; ModelGateway remains the stable internal port.

The long-lived Contract requires a controlled HTTP transport satisfying declared transport invariants, not a particular library. A replacement client is valid if it preserves those agreements. HTTPX naming, production dependency placement and concrete library configuration belong to implementation/tooling and a real future handoff; its present dev dependency is not production delivery evidence.

SUPERSEDED proposal interpretation: adopting HTTPX makes its library identity/classes a permanent Runtime Contract dependency. The initial implementation choice remains accepted; normative responsibilities are library-independent.

Intended destination: agent/execution-runtime.md controlled transport responsibilities; implementation/tooling and eventual actual handoff for HTTPX realization. Actual writeback: this register only.

<a id="cg06-q93"></a>
### CG06-Q93 — Stable transport invariants, replaceable library controls

Status: ACCEPTED with user amendment. The Contract prohibits hidden automatic retry, fallback/model switching, implicit changes to the target Provider endpoint and silent environment-driven route changes. TLS must use controlled verification. One admitted Invocation permits at most one real model request; any permitted retry must be a separately admitted controlled Invocation and remains subject to existing no-replay/consumer rules.

Current HTTPX realization explicitly disables retries/redirect following and implicit environment/system proxy inheritance, with verified TLS. follow_redirects, trust_env and concrete timeout knobs are implementation details, not cross-library Contract fields. An actual deployment proxy requires explicit controlled configuration.

Provider guidance to retry later or use another Provider supplies no JobHunter retry/fallback authority. It cannot override the sending boundary, budget admission or unknown-outcome rules.

SUPERSEDED proposal interpretation: freeze HTTPX-specific switches as stable universal transport fields. Their invariant effects remain required; equivalent future transport realizations may differ.

Intended destination: agent/execution-runtime.md transport invariants and implementation/bootstrap configuration for the HTTPX realization. Actual writeback: this register only.

<a id="cg06-q94"></a>
### CG06-Q94 — Process-injected credentials outside semantic persistence

Status: ACCEPTED. First implementation injects the API credential through the process startup environment, such as DEEPSEEK_API_KEY, with bootstrap supplying it to the adapter. Do not put the secret in semantic Run bindings, Package, Frame, fingerprints, ordinary logs or telemetry. No credential database lifecycle/UI is introduced.

Missing credentials disable the relevant model capability with a typed configuration problem without disabling unrelated local capabilities. Multiple accounts, credential rotation and credential registries are outside this first agreement.

Intended destination: adapter/bootstrap credential integration and applicable agent/execution-runtime.md/foundation/storage.md secret exclusion. Actual writeback: this register only.

<a id="cg06-q95"></a>
### CG06-Q95 — Phase timeouts and a nonrenewing overall call bound

Status: ACCEPTED. Apply finite connection/read/write and other applicable phase bounds together with an overall call bound constrained by the Run's remaining deadline. Receiving a stream fragment can satisfy an individual read wait but cannot restart the whole-call bound or Run deadline. Continuous fragments do not permit unbounded execution.

Timeout interpretation follows actual dispatch/completion evidence; timeout alone is neither proof of no dispatch nor zero usage. Concrete transport-library knobs and numeric defaults remain implementation/configuration details within the declared bounds.

Intended destination: agent/execution-runtime.md call timing and adapter transport realization. Actual writeback: this register only.

<a id="cg06-q96"></a>
### CG06-Q96 — Owned complete-response representation

Status: ACCEPTED. Define a JobHunter-owned, versioned response representation retaining the complete content required by the protocol, Tool requests, usage and admitted Provider observations. Do not promote SDK-private objects, all HTTP headers or arbitrary unknown fields into durable authority. Unknown fields cannot silently become new capabilities or pricing evidence.

Preserve actual model-produced Tool argument text rather than repairing it into valid JSON before persistence. Concrete response fields and deterministic serialization remain to be closed for the selected protocol. The owned business-response representation is not a raw transport dump.

Round 11 interface review: "response representation" here has not yet fixed whether accompanying usage/observations share the business payload or are associated evidence. EXR-016 already excludes usage/timing from business-response identity. Q111 is the pending explicit placement choice; this paragraph must not be read as an accepted override of M1 or permission to change response bytes for late usage.

Subsequent resolution: Q111 places usage/timing/Provider observations in associated evidence outside immutable terminal-response bytes; Q115 preserves M1 response-only equality even when usage is captured in the same first-publication transaction. The earlier pending statement records the historical seam, not a remaining alternative shared-blob authority.

Intended destination: agent/execution-runtime.md complete response format, DeepSeekAdapter mapping and foundation/storage.md exact bytes. Actual writeback: this register only.

<a id="cg06-q97"></a>
### CG06-Q97 — Preserve reasoning required by the declared continuation protocol

Status: ACCEPTED. If the selected mode requires reasoning content for a later Tool conversation, preserve that necessary content completely in protected response payload under an explicit protocol. Later Frame inclusion still requires current admission and capacity checks. Keeping only user-visible answer text cannot satisfy a protocol that requires more recovery input.

Reasoning content is not business fact authority, Memory or ordinary log data and is not displayed/exported by default. Nonessential retention requires an explicit protocol basis rather than SDK whole-object copying. Exact supported mode/payload fields remain to be closed.

Intended destination: agent/context.md continuation input, DeepSeekAdapter response handling and foundation/storage.md protected payload. Actual writeback: this register only.

<a id="cg06-q98"></a>
### CG06-Q98 — Exactly one semantic choice for current DeepSeek configuration

Status: ACCEPTED with user amendment. The current controlled M2 DeepSeek Chat Completions configuration accepts exactly one semantic choice. It has no multiple-candidate selection or best-of consumer. Zero/multiple semantic candidates are unsupported protocol outcomes; the adapter cannot silently select the first or a preferred one. Preserve true completion/error evidence rather than treating protocol mismatch as proof of no remote execution.

This does not require every individual SSE event to be a standalone semantic result, nor impose permanent single-candidate behavior on all future ModelGateway consumers. An actual second Provider or new DeepSeek protocol may define its own selection, cost and evidence agreement.

SUPERSEDED proposal interpretation: ModelGateway universally and permanently permits only one candidate. Exactly-one is a support condition of this current DeepSeek adapter/configuration, not the abstract port's lifetime cardinality.

Intended destination: agent/execution-runtime.md current DeepSeek response support and actual future consumers for multi-candidate semantics. Actual writeback: this register only.

<a id="cg06-q99"></a>
### CG06-Q99 — Bounded receiving and parsing before response persistence

Status: ACCEPTED. The adapter needs finite technical constraints on receiving buffers, stream events and parsing work in addition to the persisted-response byte limit. These protections are not business-output capacities; this decision selects no permanent numbers.

If a bound is reached, preserve M1's distinction between confirmed complete oversized output and reception interrupted before confirmed completion. Do not truncate and claim complete success. Existing EXR-026–028 remain the underlying persistence/outcome boundaries.

Intended destination: adapter reception protocol and agent/execution-runtime.md size/termination evidence. Actual writeback: this register only.

<a id="cg06-q100"></a>
### CG06-Q100 — Freeze effective parameter meaning, reject ignored combinations

Status: ACCEPTED. Controlled configuration accepts applicable, explainable parameter combinations. Reject parameters that have no effect in the selected mode before execution. Any explicitly permitted mapping is resolved during controlled configuration interpretation with its effective meaning frozen; the adapter cannot guess, drop parameters or conceal differences behind Provider compatibility behavior.

A supplied parameter value alone does not prove effective model behavior. Concrete accepted parameters/mappings require the selected DeepSeek capability agreement; this selects no universal parameter schema.

Intended destination: agent/execution-runtime.md controlled effective configuration and DeepSeekAdapter mapping. Actual writeback: this register only.

## Round 10 persistence and local review

- Q91–Q100 are accepted with Q92/Q93/Q98 amendments. HTTPX is an initial implementation choice; controlled transport behavior is the enduring agreement. Exactly-one is scoped to current DeepSeek semantic choices, not every SSE event or every future Gateway consumer.
- Decision-to-Document Traceability: all decisions identify prospective owners and register-only writeback; the three displaced interpretations remain explicit. No library knobs were introduced as universal Runtime fields, and Provider retry advice cannot create execution authority.
- Cross-Document Semantic Consistency: checked Q48/Q58/Q73/CG06-S2 and EXR-026–028 against the accepted scope. Semantic mapping still precedes Frame freezing; Tool execution still follows a durable complete model response; timeout/size limits preserve unknown-outcome truth. Stream usage-layout facts need a pinned adapter agreement rather than importing a generic SDK convention.
- Only this register was edited. Bounded official-document research continues; no install, code changes, live API call or normative publication occurred. M2 readiness remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q100 anchors/headings, Q101–Q110 unanswered topic identities, all twenty supersession annotations, Q92/Q93/Q98 amendment checks, the research locator, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not proof that the stream parser or Provider adapter has been implemented or validated.

<a id="cg06-r3"></a>
## CG06-R3 — Stream-document retrieval caveat and terminal evidence research

Bounded read-only official-document research on 2026-09-23: [Chat Completions reference](https://api-docs.deepseek.com/api/create-chat-completion/) describes SSE termination, finish reasons, indexed Tool deltas, nullable content and repeated response identity. Recent search extraction and earlier direct inspection describe final one-choice usage; older cached results describe a separate empty-choice usage event. Direct refetches in this round timed out. Do not merge these layouts or claim every retrieved version is one verified protocol. The exact supported layout remains a research gate before adapter implementation/publication; Round 11's choices below do not require selecting either layout.

The [Provider error guide](https://api-docs.deepseek.com/quick_start/error_codes/) recommends retry for some errors and alternative-provider use for rate limits. These are third-party usage suggestions, not proof of dispatch absence or an exception to Q93. No retry was performed.

Gaps for the concrete parser agreement include missing terminal delimiters, contradictory terminal fields, Tool-index handling and conflicting repeated metadata. Source samples/schema also require reconciliation for nullable terminal delta role. These are factual/representation seams to resolve with the selected protocol, not invitations to silently guess data or broaden Runtime authority.

## Round 11 — Complete terminal response versus semantic success

The user accepted Q101–Q110 with an explicit Q102 amendment preserving every valid complete Provider terminal outcome independently of Skill success. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q101"></a>
### CG06-Q101 — Shared owned response representation across transport modes

Status: ACCEPTED. Stream and nonstream paths normalize to the same owned complete-response representation and corresponding integrity/format checks. Streaming first assembles the result; nonstreaming parses its complete response directly. Transport mode may remain configuration/diagnostic evidence without creating two business-result authorities.

Shared representation does not imply equal model content across separate calls. Exact response bytes and separation of accompanying usage/observation evidence remain to be specified consistently with EXR-016 and Q111's pending choice.

Q111/Q115 subsequently resolve evidence placement and equality; exact terminal-response fields/serialization remain open.

Intended destination: agent/execution-runtime.md owned response format and DeepSeekAdapter normalization. Actual writeback: this register only.

<a id="cg06-q102"></a>
### CG06-Q102 — Protocol-complete Provider termination need not be successful

Status: ACCEPTED with user amendment. For the current DeepSeek streaming agreement, protocol completeness requires one closable semantic choice, consistent response association/structure, a final nonempty finish_reason, receipt of [DONE], and the necessary protocol checks. EOF, timeout or cancellation cannot substitute for these terminal requirements.

When these conditions hold, the complete Provider terminal response may be durably published under M1's existing authority, format and size predicates. This is not restricted to semantically successful endings. stop/tool_calls may support normal Skill processing; length establishes complete Provider termination with possibly truncated content; content_filter, insufficient_system_resource and aborted also establish terminal outcomes without becoming successful Skill results.

Interpret terminal meaning separately after recording the complete response. Missing required completeness evidence cannot be repaired with another remote call; preserve any genuinely observed terminal/usage evidence without inventing a complete response. Exact supported SSE usage layout remains a separate factual parser seam, not a reason to equate all abnormal finish reasons with incomplete reception.

SUPERSEDED proposal interpretation: a "legal terminal reason" means a business-success reason, excluding aborted, insufficient_system_resource or other abnormal but protocol-complete terminal results from durable response. The required framing/structure checks remain; terminal semantic success is not a completeness predicate.

Intended destination: agent/execution-runtime.md complete terminal response and DeepSeekAdapter streaming acceptance. Actual writeback: this register only.

<a id="cg06-q103"></a>
### CG06-Q103 — Length termination preserves complete evidence

Status: ACCEPTED. A protocol-complete response ending with length retains its exact received content and actual finish reason. Content may be cut off or invalid for the Skill while the Provider's terminal response is complete. Do not discard it, relabel it stop or automatically resend.

Consumer validation determines usability; any repair remains subject to the Skill's semantic allowance and Budget admission. Q102 applies the same completeness-versus-success separation to other terminal reasons.

Intended destination: agent/execution-runtime.md terminal interpretation and actual Skill validation/repair protocols. Actual writeback: this register only.

<a id="cg06-q104"></a>
### CG06-Q104 — Metering admission cannot erase a complete response

Status: ACCEPTED. Admit response content/termination independently from usage evidence. A complete valid response can persist when usage is missing or inconsistent. Record reliable metering components and unknown/invalid dispositions through the controlled evidence representation; retain corresponding Budget exposure rather than releasing against untrusted counts.

Do not lose recoverable content because metering fails, or insert zero usage merely to satisfy a schema. The metering evidence's placement is not fixed by this decision; EXR-016 excludes usage/timing from the immutable business-response identity, with the concrete Q111/Q115 seams still open.

Q111/Q115 subsequently resolve the split and optional atomic evidence capture. Usage admission/confirmation remains separate from immutable response confirmation.

Intended destination: agent/execution-runtime.md response acceptance, foundation/budget.md metering evidence and DeepSeekAdapter independent validation. Actual writeback: this register only.

<a id="cg06-q105"></a>
### CG06-Q105 — Assemble Tool fragments before strict argument interpretation

Status: ACCEPTED. Associate Tool fragments by the current response's Tool index and selected protocol rules, concatenate argument text in received order, and validate ID/name fields according to that protocol. Do not repair JSON, insert delimiters or execute a Tool while receiving fragments.

Only after complete-response persistence does Q60's strict argument parsing run. Unknown association, conflicting fields and incomplete fragments cannot be guessed into valid requests. Never join fragments from different Invocations. Precise index/name-fragment rules await the verified wire schema.

Intended destination: DeepSeekAdapter Tool-delta assembly and agent/tools.md post-durability argument admission. Actual writeback: this register only.

<a id="cg06-q106"></a>
### CG06-Q106 — Stream association consistency and observation anomalies

Status: ACCEPTED. Fields used to establish one response must satisfy their consistency rules; conflicting response identity prevents normal assembly rather than last-value-wins replacement or merging unrelated content. The adapter protocol explicitly identifies these fields.

Provider observations remain separate. Conflicting observed system_fingerprint values cannot be silently rewritten into one apparently definite observation; retain the observation anomaly under the applicable evidence protocol, without promoting that fingerprint to business identity. This does not impose a newly invented invariant on every optional Provider field.

Intended destination: DeepSeekAdapter response association and foundation/storage.md admitted observation evidence. Actual writeback: this register only.

<a id="cg06-q107"></a>
### CG06-Q107 — Preserve null, empty and actual text

Status: ACCEPTED. Preserve protocol-admitted null, empty string and actual text distinctly. A Tool-request response may have no ordinary answer text. Do not manufacture an assistant sentence to fill an empty body or persist a presentation placeholder as canonical model output.

Whether the response satisfies the Skill's final-result requirements is consumer-owned. Missing required protocol fields remain distinct from legitimately nullable content.

Intended destination: DeepSeekAdapter response projection and actual Skill output validation. Actual writeback: this register only.

<a id="cg06-q108"></a>
### CG06-Q108 — Stream chunks are transient assembly data

Status: ACCEPTED. M2 needs no per-chunk durable log or chunk-based continuation protocol. Use bounded temporary reception/assembly; the complete final response enters the established durable-response protocol. Necessary timing/stage/diagnostic evidence may follow its own agreement without becoming a second recoverable response authority.

Saved partial text cannot be joined to a new call's output, and a retained prefix confers no replay permission after a crash.

Intended destination: agent/execution-runtime.md stream/persistence boundary and foundation/storage.md canonical response scope. Actual writeback: this register only.

<a id="cg06-q109"></a>
### CG06-Q109 — Provider IDs are correlation evidence only

Status: ACCEPTED. Provider completion IDs support correlation/audit. Local Invocation identity, the original execution path and committed associations continue owning execution/settlement boundaries. Do not merge Invocations, bypass accounting checks or infer one remote execution solely from equal Provider IDs.

Such identifiers also grant no query, replay or recovered sending permission.

Intended destination: agent/execution-runtime.md Provider correlation and foundation/budget.md local accounting identity. Actual writeback: this register only.

<a id="cg06-q110"></a>
### CG06-Q110 — Bounded typed Provider-error projection

Status: ACCEPTED. The adapter exposes a bounded typed error projection with necessary HTTP status, recognized error category and admitted Provider code/diagnostic basis. Do not default to persisting entire error bodies, all headers or exception strings, which can contain request data, credentials or third-party internals.

Error classification alone does not establish undispatched work, zero cost or retry permission. Runtime/Budget use actual evidence and their owned rules. Exact category/field definitions remain open; this is not a new universal error container.

Intended destination: DeepSeekAdapter error mapping and agent/execution-runtime.md evidence-based disposition. Actual writeback: this register only.

## Round 11 persistence and local review

- Q101–Q110 are accepted with Q102's protocol-complete terminal semantics. Its supersession explicitly preserves abnormal but fully received terminal results. Skill success/repair, usage admission and durable-response completeness remain separate.
- Decision-to-Document Traceability: each decision has prospective owners and register-only writeback. Q96/Q101/Q104 are annotated with the unfinished response-versus-metering placement seam; no shared blob or late response-byte mutation has been silently accepted.
- Cross-Document Semantic Consistency: reviewed EXR-016–023/026–028/031 with Q73/Q96/Q98/Q102/Q104. EXR-016 already permits consumer-invalid complete outcomes and excludes usage/timing from business-response identity. Broader M2 "response representation" wording must be concretized without violating that rule; Q111 proposes the explicit split. Complete abnormal terminal evidence still needs lawful first-publication authority and finite payload size. The existing Ready M1 scope is not invalidated by this unresolved M2 representation seam.
- Only this register was edited. No implementation, live Provider call or normative publication occurred; M2 remains Pending. Exact SSE layouts remain subject to the recorded factual verification gate.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q110 anchors/headings, Q111–Q120 unanswered topic identities, all twenty-one supersession annotations, Q102 terminal-completeness checks, the EXR-016 identity-seam annotation, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not adapter or execution proof.

## Round 12 — Independent evidence identity and opaque Budget ownership

The user accepted Q111–Q120 with amendments to Q115/Q116/Q118/Q119. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q111"></a>
### CG06-Q111 — Terminal payload and associated evidence have separate identities

Status: ACCEPTED. Immutable terminal-response content includes content, necessary reasoning, Tool requests and finish_reason. Usage, timing and Provider observations are associated evidence keyed to invocation_id rather than part of those immutable business-response bytes/hash. Each evidence owner supplies its own persistence/confirmation/reconciliation rules.

Protocol-required content such as Tool-call IDs needed for continuation stays in the actual response; do not move all identifiers to optional observations indiscriminately. This resolves Q96/Q101/Q104's broad representation wording consistently with EXR-016, without creating a second response authority or permitting late metering to mutate the terminal payload.

Intended destination: agent/execution-runtime.md terminal/evidence split, foundation/budget.md usage and foundation/storage.md association. Actual writeback: this register only.

<a id="cg06-q112"></a>
### CG06-Q112 — Preserve unknown terminal reasons without granting continuation

Status: ACCEPTED. Preserve an unfamiliar nonempty finish_reason exactly. When the required response framing, structure and association checks establish completeness, an unfamiliar reason does not by itself discard the terminal evidence. Interpret it as an unsupported terminal meaning, not stop or another known code.

Do not automatically execute Tools, repair or otherwise continue from guessed semantics. This admits evidence, not new Provider capabilities; missing required protocol checks still prevent complete-response publication.

Intended destination: DeepSeekAdapter terminal interpretation and agent/execution-runtime.md owned response format. Actual writeback: this register only.

<a id="cg06-q113"></a>
### CG06-Q113 — Tool candidates must agree with terminal semantics

Status: ACCEPTED. The current adapter exposes Tool requests as selectable candidates only when they satisfy tool_calls terminal semantics. Inconsistent combinations, such as proposed Tool requests under stop or aborted, retain their truthful terminal response but do not automatically execute those requests.

Even a consistent tool_calls outcome requires explicit Skill selection and independent action admission. Terminal reason is not execution permission.

Intended destination: DeepSeekAdapter response interpretation, agent/tools.md candidate admission and actual Skill workflow. Actual writeback: this register only.

<a id="cg06-q114"></a>
### CG06-Q114 — Nonstream completeness has its own terminal predicates

Status: ACCEPTED. The nonstream path requires the complete expected HTTP response entity, strict parsing into a complete JSON object, one closable semantic choice, nonempty finish_reason and necessary structural/association checks. HTTP 200 or a plausible partial object alone is insufficient.

These predicates establish Provider terminal completeness, not business success. Each transport mode uses its own terminal evidence before normalizing to Q101's shared owned response representation.

Intended destination: DeepSeekAdapter nonstream acceptance and agent/execution-runtime.md complete-response meaning. Actual writeback: this register only.

<a id="cg06-q115"></a>
### CG06-Q115 — Atomic usage capture does not change response equality

Status: ACCEPTED with user amendment. At first response publication, usage evidence already independently validated as admissible can be captured atomically with the complete response in the local transaction; Budget settlement may occur separately afterward. Missing/invalid usage does not prevent an otherwise lawful complete response, and must not be filled with zero. Derived exports do not enter this transaction.

Response equality and idempotent read-only confirmation remain solely M1's immutable terminal-response comparison: validate retained format/hash/length and compare complete bytes, with hash equality alone insufficient. Associated usage is not part of response conflict detection. The same response first saved without usage and later accompanied by lawful usage cannot become a response integrity conflict. Confirmation does not require resubmitting the usage captured at first publication.

Usage confirmation and later convergence independently obey Budget evidence/reconciliation rules. A response read-only confirmation remains nonmutating; it is not a hidden usage-update operation. M2's combined first-write boundary neither changes the M1 equality authority nor grants stale response publication through a later accounting path.

SUPERSEDED proposal interpretation: co-transaction usage capture makes the response-plus-usage bundle the equality unit or requires historical usage resubmission to confirm the response. Only the first-write atomic coordination is shared; identities and later operations remain separate.

Intended destination: agent/execution-runtime.md first publication/confirmation, foundation/budget.md usage evidence and foundation/storage.md atomic capture. Actual writeback: this register only.

<a id="cg06-q116"></a>
### CG06-Q116 — Opaque foreground operation_id, not an Operation aggregate

Status: ACCEPTED with user amendment. A foreground budget owner has stable operation_id: UUIDv4, created and recoverably held by its calling Application consumer before budget-scope creation can occur. Runtime treats it as an opaque owner identity. No separate budget_id is needed to restate that ownership.

operation_id is neither AgentRun, a business aggregate nor a universal workflow object. One identity may own the envelope shared by multiple Runs while each Run's binding stays fixed. This defines the present foreground budget interface, not a generic Operation lifecycle/state/history/API or a universal foreground/background/Eval owner hierarchy.

SUPERSEDED proposal interpretation: the Application-owned Operation identity entails a new Universal Application Operation Aggregate. Stable identity and consumer-held recoverability are required; a general Operation object/lifecycle is not.

Intended destination: foundation/budget.md foreground owner identity and actual Application caller obligations. Actual writeback: this register only.

<a id="cg06-q117"></a>
### CG06-Q117 — Initial CNY ledger quantum is one hundred-millionth yuan

Status: ACCEPTED. M2's internal CNY ledger quantum is 0.00000001 CNY (eight fractional decimal places). Price multiplication remains exact decimal; ledger amounts use the declared quantization rule. Do not use binary-floating-point ledger comparisons.

This is internal accounting precision, not a claim about Provider invoice precision or a requirement for UI display precision. Future precision changes must preserve historical interpretation rather than silently reinterpret old amounts. Logical scalar bounds/serialization remain to be closed.

Subsequent resolution: Q121 defines externalized ledger strings and Q182 defines the finite current CNY ledger range. Original price/exact-calculation evidence retains its distinct precision.

Intended destination: foundation/budget.md CNY amount semantics and applicable common.md scalar expression. Actual writeback: this register only.

<a id="cg06-q118"></a>
### CG06-Q118 — Quantize ledger debits, preserve exact calculation evidence

Status: ACCEPTED with user amendment. Sum exact applicable cost components for the Invocation before conservatively quantizing the total upward once for the ledger debit. Reservation amounts may likewise round upward. Do not separately round each component and then sum, or round down away repeated low costs.

Keep exact calculated budget cost (usage multiplied by the frozen price basis) distinct from the quantized ledger debit. Retain enough exact calculation evidence to explain both the calculated value and why the ledger debited its quantized amount. Do not rewrite usage, token counts or original price basis as a consequence of ledger rounding. The debit is not Provider invoice-confirmed cost.

SUPERSEDED proposal interpretation: upward rounding replaces the exact usage/cost evidence or makes the rounded amount the sole historical cost truth. Conservative quantization governs reservation/debit only; source evidence and exact arithmetic retain their own meaning.

Intended destination: foundation/budget.md exact calculation/ledger quantization and associated evidence. Actual writeback: this register only.

<a id="cg06-q119"></a>
### CG06-Q119 — Allocation replay uses the original immutable basis

Status: ACCEPTED with user amendment. Reusing the same budget owner identity with the same original allocation confirms the existing scope; different allocation conflicts. Confirmation returns actual current accounting without replenishing reservations, settled usage or unknown exposure. Compare the original allocation, not current remaining capacity.

Interpret sameness using the immutable allocation semantics/basis or fingerprint frozen at creation. Later global configuration/default changes cannot reinterpret the historical request, manufacture conflict or reset the scope. operation_id plus sufficient immutable original allocation basis must support stable confirmation; its concrete representation remained open in this round and is subsequently selected by Q123.

No BudgetStartAttempt/BudgetStartReceipt lifecycle or separate version entity is required by this decision. An uncertain creation retains the original identity rather than substituting another owner.

SUPERSEDED proposal interpretation: retry equivalence resolves the current allocation configuration/defaults again and compares that new interpretation. Historical confirmation is bound to the creation-time semantics.

Intended destination: foundation/budget.md allocation creation/confirmation, actual Application callers and foundation/storage.md immutable basis. Actual writeback: this register only.

<a id="cg06-q120"></a>
### CG06-Q120 — Derive Invocation budget ownership from the Run

Status: ACCEPTED. Runtime resolves the Run from execution qualification and derives its Budget owner from the frozen semantic binding. Per-Invocation admission accepts no independent owner override. Any necessary physical association copy must agree, not become a competing authority.

Model output, Tool arguments and recovery cannot transfer cost to another owner. Different ownership requires a new lawful task binding; an existing Invocation cannot be reassigned.

Intended destination: foundation/budget.md owner derivation and agent/execution-runtime.md admission inputs. Actual writeback: this register only.

## Round 12 persistence and local review

- Q111–Q120 are accepted with Q115/Q116/Q118/Q119 amendments. Earlier pending annotations now point to the resolved response/evidence split without erasing the historical seam. The first publication may capture usage atomically without changing response-only equality.
- Decision-to-Document Traceability: every decision identifies prospective owners and register-only writeback. The four displaced interpretations remain explicit: response/usage bundle equality, universal Operation aggregate, rounding of source truth and current-default allocation replay. No new receipt/version/lifecycle authority was inferred.
- Cross-Document Semantic Consistency: checked EXR-016–021, Architecture section 11 and Q67/Q71/Q73/Q80/Q111/Q115. M1 exact-byte confirmation and read-only behavior remain intact, including the same-response/later-usage case. Accounting arithmetic distinguishes exact evidence from eight-place ledger quantization; immutable original allocation differs from mutable remaining capacity. Opaque owner identity does not create a generic workflow aggregate.
- Only this register was edited. No implementation, live call, normative publication or execution proof was produced. M2 remains Pending; exact schemas, finite scalar ranges and remaining interface/research gates are not silently treated as closed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q120 anchors/headings, Q121–Q130 unanswered topic identities, all twenty-five supersession annotations, explicit Q115/Q116/Q118/Q119 refinement checks, local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are local documentation checks, not implementation or execution evidence.

## Round 13 — Atomic capacity qualification and format-specific bytes

The user accepted Q121–Q130 with amendments to Q127/Q128/Q130. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q121"></a>
### CG06-Q121 — Canonical externalized ledger amounts

Status: ACCEPTED. Externalized CNY ledger amounts use canonical decimal strings with exactly eight fractional digits, such as "0.00000001" and "12.34000000". No exponent, grouping separator or unnecessary leading zeros is admitted. Allocation, reservation and debit amounts are nonnegative under their field definitions; this must not conceal overrun or insufficient remaining capacity.

Exact price inputs and unquantized calculated cost retain their own precision. This serialization does not force source prices or exact calculation evidence into the ledger quantum. Finite scalar ranges remain open.

Intended destination: foundation/budget.md ledger amounts and common.md only for genuinely shared scalar expression. Actual writeback: this register only.

<a id="cg06-q122"></a>
### CG06-Q122 — Zero is a real limit, not unlimited capacity

Status: ACCEPTED. A zero resource limit grants zero units; it is not an unlimited sentinel. Disabling an optional dimension is explicitly distinct, and a missing required limit is invalid. A monetary-disabled allocation need not invent a currency; an enabled zero monetary allocation is a real CNY constraint.

An invocation requiring zero reservation in one dimension must still pass all other applicable limits and admission. Optional-dimension encoding and the actually supported dimension set remain their own pending shape decisions.

Intended destination: foundation/budget.md allocation admission and limit semantics. Actual writeback: this register only.

<a id="cg06-q123"></a>
### CG06-Q123 — Retain original allocation values and their format

Status: ACCEPTED. Retain the complete parsed original allocation values and their exact allocation-format identifier in the budget scope, separately from mutable reservations and settled consumption. This is the minimum concrete historical comparison basis selected for Q119. Compare those creation-time semantics rather than re-resolving current defaults.

Configuration references may support provenance but do not replace the retained original values. No additional allocation_fingerprint, receipt or separately versioned allocation entity is required. This decision selects the historical representation, not a speculative universal resource-dimension schema.

Intended destination: foundation/budget.md immutable allocation basis and foundation/storage.md retention. Actual writeback: this register only.

<a id="cg06-q124"></a>
### CG06-Q124 — Foreground budget identity is Workspace-local

Status: ACCEPTED. operation_id is unique within the current physical Workspace's foreground budget-owner namespace, not merely within a Skill, Run or caller. Multiple Runs may lawfully share that same owner's scope. Run/start identities retain their distinct meanings.

Do not introduce a global ID service or new Workspace identity merely to enforce this namespace. The existing physical Workspace boundary supplies the scope.

Intended destination: foundation/budget.md identity scope and foundation/storage.md uniqueness. Actual writeback: this register only.

<a id="cg06-q125"></a>
### CG06-Q125 — Retain M2 budget-owner and accounting evidence

Status: ACCEPTED. M2 introduces no automatic cleanup or TTL for budget-owner identities, original allocations, reservations or settlement evidence. Ended Runs do not prove all costs known and do not make an owner identity reusable with a fresh allocation.

A future retention consumer must define its actual cleanup and historical-confirmation obligations. No general Operation terminal/archive lifecycle is introduced for this purpose.

Intended destination: foundation/budget.md historical accounting and foundation/storage.md retention. Actual writeback: this register only.

<a id="cg06-q126"></a>
### CG06-Q126 — Settlement and reservation release share an atomic boundary

Status: ACCEPTED. Applying admissible settlement updates the applicable ledger debit/counters and releases the corresponding reservation atomically in one local transaction. Never release exposure first and write consumption later, allowing another invocation to spend the gap.

Independently trustworthy components may settle while unresolved components retain conservative exposure under their evidence rules. Derived summaries may support reads but cannot form a competing balance authority. No network access or Provider-invoice confirmation is required inside this transaction.

Intended destination: foundation/budget.md settlement and foundation/storage.md atomic accounting. Actual writeback: this register only.

<a id="cg06-q127"></a>
### CG06-Q127 — Atomically acquire temporary capacity qualification

Status: ACCEPTED with user amendment. Waiting for model capacity is bounded, cancellable local coordination and counts against the existing Run deadline. Waiting itself creates no dispatch intent, monetary reservation or durable queue.

Obtaining capacity means atomically acquiring a real exclusive Runtime capacity qualification, not observing capacity_available = true. Each admitted path occupies its allocated slot so concurrent check-then-act paths cannot exceed the configured local capacity. The sequence is: wait; atomically acquire temporary qualification; recheck Run/deadline/permission; enter Q69's reservation/counter/Frame/intent transaction; then perform the unique authorized dispatch.

Safely release this qualification if Q69 admission fails or the path does not enter dispatch. This coordination can be entirely short-lived and internal: no durable queue, capacity_reservation_id or new Domain state is required. Qualification is not M1's sending permission, and releasing it does not release unknown monetary exposure. Exact lifetime and uncertain-commit handling remain to be refined.

Subsequent resolution: Q131 distinguishes local transport quiescence from requested cancellation/remote completion; Q132 defines qualification handling during uncertain Q69 acknowledgement.

SUPERSEDED proposal interpretation: a nonexclusive capacity-available check suffices before Q69, even though competing callers can all pass it. The accepted boundary requires actual atomic acquisition.

Intended destination: agent/execution-runtime.md capacity admission and foundation/budget.md shared resource coordination. Actual writeback: this register only.

<a id="cg06-q128"></a>
### CG06-Q128 — Closed current DeepSeek terminal-response payload

Status: ACCEPTED with user amendment. The current DeepSeek Chat Completions adapter's versioned terminal-response format has four fields: nonempty string finish_reason; content as string or null; reasoning_content as string or null; and ordered tool_calls. Each Tool item contains id, name and raw arguments strings. No Tool calls is an empty array; absent reasoning maps to null, distinct from an actual empty string. Content null/empty/exact-text distinctions follow Q107.

Usage, timing, returned model, system_fingerprint and Provider completion ID remain associated evidence outside these response bytes under Q111. The M1 outer association/format/hash/length metadata is not duplicated inside the payload.

This is a DeepSeek-specific supported format, not a permanent universal ModelGateway response schema. Generic Runtime requires each MODEL Invocation to freeze its own response_format_key at PREPARED, with that registered format defining unique deterministic bytes. A future supported adapter may introduce a different format; it need not invent reasoning_content or adopt DeepSeek Tool-call structure. This does not change M1's durable-response model.

SUPERSEDED proposal interpretation: the four-field projection permanently defines every Provider's response through ModelGateway. Only the current versioned DeepSeek format is selected here.

Intended destination: DeepSeekAdapter owned response format and agent/execution-runtime.md format registration/consumption. Actual writeback: this register only.

<a id="cg06-q129"></a>
### CG06-Q129 — Semantic-start fingerprint envelope

Status: ACCEPTED. The original-request fingerprint envelope has exactly skill_key, task_input, execution_config_ref and operation_id. task_input follows the selected Skill's deterministic typed input semantics; execution_config_ref identifies the exact controlled configuration. This outer envelope does not define a universal business-input schema.

Exclude start_request_id, which is the lookup identity, as well as generated run_id/absolute deadline, Package/Frame materialization, current budget balance and secrets. Do not dereference current mutable source contents or defaults to redefine a historical request. Q41/Q42 govern the versioned hash/typed encoder; the exact domain separator and configuration-reference shape remain open.

Subsequent resolution: Q137 selects immutable string configuration references, and Q138 closes the domain-separator bytes.

Intended destination: agent/execution-runtime.md original-request comparison and Application caller recovery obligations. Actual writeback: this register only.

<a id="cg06-q130"></a>
### CG06-Q130 — Fixed field order in the closed DeepSeek response format

Status: ACCEPTED with user amendment. Serialize this closed response format as compact deterministic UTF-8 JSON with no BOM or trailing newline, preserving exact strings and array order. Non-ASCII text uses UTF-8; quote, backslash and control-character escaping is fixed by the format. This format uses objects, arrays, strings and null rather than requiring a general numeric canonicalization scheme.

The top-level field order is content, finish_reason, reasoning_content, tool_calls. Each Tool item's field order is id, name, arguments. Unknown fields do not belong to this owned projection and are not dynamically sorted into it. Hash and measure the actual persisted bytes; do not normalize/re-encode retained bytes to repair an integrity mismatch. Remaining precise escaping/format-key details and golden fixtures still need closure.

Subsequent resolution: Q139 closes string escaping and Unicode validity. The response-format key and golden fixtures retain their remaining closure obligations.

SUPERSEDED proposal fragment: dynamically sort arbitrary object keys by Unicode code point for this response format. Format-prescribed fixed field order replaces it; no Universal canonical JSON mechanism is introduced. COM-045 remains the independently selected typed encoder for semantic-start fingerprints, not this JSON response format.

Intended destination: DeepSeekAdapter terminal format, agent/execution-runtime.md deterministic bytes and foundation/storage.md integrity. Actual writeback: this register only.

## Round 13 persistence and local review

- Q121–Q130 are accepted with Q127/Q128/Q130 amendments. Capacity acquisition is exclusive and atomic, the terminal field set is adapter-specific, and fixed field order replaces the proposed dynamic object-key sorting.
- Decision-to-Document Traceability: each decision identifies prospective owners and register-only writeback; all three displaced interpretations remain explicit. Q31 and Q119 now point to their later envelope/allocation resolutions while preserving their historical open branches.
- Cross-Document Semantic Consistency: reviewed EXR-012–015, Architecture sections 9–11, COM-045 and Q48/Q69/Q78/Q111/Q115/Q119. Temporary capacity qualification neither transfers M1 sending permission nor clears unknown spend. The closed adapter response format preserves response/evidence identity separation. COM-045 continues to serve the start fingerprint without being misrepresented as strict JSON. Original allocations remain separate from mutable balances.
- Only this register was edited. No implementation, live call or normative publication occurred. M2 remains Pending; exact Frame/transport schemas, scalar bounds, stream-layout verification and other interface/research gates remain open.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q130 anchors/headings and register-only writeback, Q131–Q140 unanswered topic identities, all twenty-eight supersession annotations, explicit Q127/Q128/Q130 amendment checks, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish local document integrity, not adapter or execution proof.

## Round 14 — Frame-dependent evidence and shared estimation basis

The user accepted Q131–Q140 with amendments to Q134/Q140. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q131"></a>
### CG06-Q131 — Release local capacity only after local calling has stopped

Status: ACCEPTED. Run cancellation/timeout or a cancellation request alone does not release an occupied capacity qualification. Retain it until the local call has ended, or controlled transport closure and fencing reliably prevent that path from continuing to send.

This bounds locally controlled in-flight calls, not the Provider's unobservable internal execution. A closed local connection can leave remote computation ongoing. Releasing local capacity neither proves remote termination nor releases uncertain cost. No strict bound on all Provider-side execution is inferred from this local mechanism.

Intended destination: agent/execution-runtime.md cancellation/capacity and foundation/budget.md resource distinctions. Actual writeback: this register only.

<a id="cg06-q132"></a>
### CG06-Q132 — Capacity handling during uncertain admission commit

Status: ACCEPTED. The original live path retains temporary capacity qualification during its bounded confirmation of an uncertain Q69 transaction acknowledgement. Proven committed intent plus proven no adapter entry and still-valid authority allows only that original path's M1-permitted dispatch. Proven absence of commit allows capacity release.

If confirmation is abandoned or authority is lost, first prevent that path from later sending, then release temporary capacity. This does not cancel a monetary reservation that may have committed: Budget resolves its durable evidence separately. Crash/replacement cannot reconstruct sending permission or require a new durable capacity receipt.

Intended destination: agent/execution-runtime.md original-path reconciliation and foundation/budget.md uncertain reservation separation. Actual writeback: this register only.

<a id="cg06-q133"></a>
### CG06-Q133 — Dispatch consumes one committed semantic input

Status: ACCEPTED. Dispatch consumes the committed Frame's determined semantic content together with frozen non-Frame execution configuration. Do not accept an independently reassembled messages/tools object as an alternative authority alongside the Frame.

An in-memory representation strictly corresponding to the committed bytes may be used; mandatory database rereads solely for formality are unnecessary. Controlled transport supplies authentication and connection details. All transformations affecting model-visible semantics must already have occurred before Frame freeze.

Intended destination: agent/context.md Frame consumption, agent/execution-runtime.md dispatch input and DeepSeekAdapter handoff. Actual writeback: this register only.

<a id="cg06-q134"></a>
### CG06-Q134 — Provenance is immutable evidence dependent on the Frame

Status: ACCEPTED with user amendment. ContextFrame retains actual model-visible content. Its provenance/inclusion evidence explains which exact sources or admitted literal inputs produced that content, where it appears, and which permitted projection/redaction was applied. The evidence must agree with the actual content.

Provenance may be part of the Frame format or an associated record atomically frozen with it and readable only in association with its invocation_id. It has no independent mutable lifecycle, current pointer or revision, and cannot evolve as a second persistent authority alongside ContextFrame.

Use positions stably defined by the Frame's own format, such as paths/message indices for a closed headless Frame. Do not introduce a generic byte-offset/span reference system or permanent ContextBlock UUID merely for inclusion mapping. A manifest claim of complete inclusion cannot substitute for checking the actual Frame content, and provenance cannot replace retained model-visible input.

SUPERSEDED proposal interpretation: an inclusion manifest becomes an independently evolving persistent authority, or Frame location requires a universal offset/span scheme. The requirement for truthful inclusion/transformation evidence remains; its ownership and position semantics are Frame-dependent.

Intended destination: agent/context.md Frame provenance and foundation/storage.md atomic immutable association. Actual writeback: this register only.

<a id="cg06-q135"></a>
### CG06-Q135 — Validate exact-source and permission predicates at Frame publication

Status: ACCEPTED. Q69 atomically checks the Frame's necessary exact refs, eligibility and permission predicates that participate in local authority, after preparation/assembly. If a necessary condition fails, that Frame and intent cannot publish.

Apply each source's owned protocol: an eligible exact historical version need not mechanically equal latest. Do not silently substitute new source content while retaining old validation. Revocation of protected EAGER_EXACT input ends that frozen task under the existing rule; historical Frame evidence remains separately readable. External access does not enter the authority transaction.

Intended destination: agent/context.md final admission, agent/execution-runtime.md Q69 boundary and source-owned eligibility contracts. Actual writeback: this register only.

<a id="cg06-q136"></a>
### CG06-Q136 — Historical Frame readers are distinct from execution enablement

Status: ACCEPTED. Historical format readers interpret and validate retained data under its original format independently of current Skill/model/adapter execution enablement. A reader does not load historical executable code or re-enable a disabled configuration.

A missing reader makes the historical format currently uninterpretable; it is not evidence that the retained bytes are corrupt. Do not guess using the latest format. Historical interpretation continues to require its own Storage/audit/recovery read admission and never grants model reuse.

Intended destination: agent/context.md historical interpretation and foundation/storage.md availability/integrity distinctions. Actual writeback: this register only.

<a id="cg06-q137"></a>
### CG06-Q137 — Immutable exact execution-configuration keys

Status: ACCEPTED. M2 execution_config_ref is an exact nonempty case-sensitive immutable string key into controlled static configuration. The execution meaning of an existing key cannot change in place. Changes to model, thinking mode, controlled parameters or other configuration semantics require a new key. Reject duplicate/ambiguous registration.

The reference contains no API key and does not require a database configuration-version entity. Retain immutable nonsecret values required for historical recovery under Q4 instead of relying exclusively on current code registration. Current executability remains distinct from historical request comparison.

Intended destination: agent/execution-runtime.md configuration reference/admission and Application controlled configuration. Actual writeback: this register only.

<a id="cg06-q138"></a>
### CG06-Q138 — Exact semantic-start fingerprint domain separation

Status: ACCEPTED. The initial fingerprint is SHA-256 of UTF8("SemanticStartFingerprint:v1"), followed by one zero byte 0x00, followed by COM045_ENCODE(admitted_request_envelope). The separator is one byte, not a textual escape. Q129 supplies the four-field envelope and Q137 supplies the configuration-reference scalar; existing field-owned input admission remains applicable.

Persist the fingerprint under its recorded format and Sha256Hex expression. Incompatible encoding changes need a new format rather than reinterpretation of historical hashes. Existing COM-045 consumers and prefixes remain unchanged.

Intended destination: agent/execution-runtime.md fingerprint bytes and foundation/storage.md historical interpretation. Actual writeback: this register only.

<a id="cg06-q139"></a>
### CG06-Q139 — Exact DeepSeek terminal string escaping

Status: ACCEPTED. For Q128/Q130's current closed response format, escape quotation mark and backslash as \" and \\ respectively. Use \b, \t, \n, \f and \r for backspace, tab, line feed, form feed and carriage return. Encode the remaining U+0000–U+001F characters as lowercase-hex \u00xx. Do not escape solidus; encode other valid Unicode characters directly as UTF-8.

Do not perform Unicode normalization. Reject strings still containing isolated surrogates after parsing. These rules change encoding only, not the values of content, reasoning_content or raw Tool arguments strings. They do not establish a general canonical-JSON facility; exact format-key/golden-fixture closure remains separate.

Intended destination: DeepSeekAdapter owned response format and foundation/storage.md exact byte evidence. Actual writeback: this register only.

<a id="cg06-q140"></a>
### CG06-Q140 — One immutable estimator evaluation, separately owned policies

Status: ACCEPTED with user amendment. Context and Budget consume the immutable basis of one estimator evaluation for the same Frame: exact applicable estimator/version and its estimated_input_tokens value. Do not independently estimate that same Frame as incompatible unexplained input quantities.

Context applies its output reserve and capacity margin to that basis. Budget applies its explicitly declared reservation assumptions, including any additional conservative allowance and applicable cache-miss/pricing basis. Record any additional allowance sufficiently to explain the reservation. Shared evaluation evidence does not require permanently sharing one policy.

The estimate is neither actual Provider usage nor a proven absolute upper bound. Settle against admissible usage and retain overrun truth. Context capacity policy and Budget pricing/reservation policy keep their own owners.

SUPERSEDED proposal interpretation: sharing an estimator basis merges Context margin, monetary conservatism and cache assumptions into one permanent AdmissionPolicy. Only the immutable evaluation basis is shared; policy authority remains separate.

Intended destination: agent/context.md capacity basis and foundation/budget.md reservation calculation/evidence. Actual writeback: this register only.

## Round 14 persistence and local review

- Q131–Q140 are accepted with Q134/Q140 amendments. Provenance has no independent current/revision authority; one immutable estimator evaluation does not merge Context and Budget policy. Prior open fingerprint/capacity/string-encoding statements now identify their subsequent resolutions.
- Decision-to-Document Traceability: all ten decisions identify prospective owners and register-only writeback. Both displaced interpretations remain explicit. No new ContextBlock identity, capacity receipt, configuration entity or AdmissionPolicy is inferred.
- Cross-Document Semantic Consistency: reviewed EXR-013–017, COM-045, Architecture sections 10–11 and Q4/Q47/Q48/Q53/Q69/Q127–Q130. Capacity release preserves remote uncertainty; dispatch consumes committed semantic input; provenance cannot replace input bytes; original-format readers do not confer execution permission. Current source admission preserves exact-version ownership rather than requiring latest universally.
- Only this register was edited. No implementation, live call or normative publication occurred. M2 remains Pending. The following Eval frontier consumes Architecture/Acceptance's existing real-path and independent-evidence boundaries without asserting SDK/platform implementation or research completion.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q140 anchors/headings and register-only writeback, Q141–Q150 unanswered topic identities, all thirty supersession annotations, explicit Q134/Q138/Q139/Q140 detail checks, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These establish local document integrity, not Runtime/adapter/Eval execution proof.

## Round 15 — Tool-source admission and reference-first Eval evidence

The user accepted Q141–Q150 with amendments to Q147/Q150. Every destination below is prospective; actual writeback is this register only. Q147 explicitly distinguishes a Contract invariant from the accepted first-implementation/handoff choice.

<a id="cg06-q141"></a>
### CG06-Q141 — Concrete current DeepSeek Tool-request locator

Status: ACCEPTED. The current DeepSeek response format locates a model-origin Tool request by producing_model_invocation_id and a zero-based integer tool_call_index into the complete ordered Q128 tool_calls array. Runtime reads the selected item from the integrity-checked durable response.

No independent request UUID is introduced. Provider Tool-call IDs retain protocol correlation meaning, not execution identity or replay permission. Future response formats may define their own locator representation.

Intended destination: agent/tools.md selected-request provenance and agent/execution-runtime.md response consumption. Actual writeback: this register only.

<a id="cg06-q142"></a>
### CG06-Q142 — One TOOL Invocation association per accepted source request

Status: ACCEPTED. An accepted model-origin source-request locator associates with at most one TOOL Invocation. Its first association and Invocation creation are atomic, so competing selectors cannot create separate executions for the same request.

Repeated submission confirms the existing association without itself executing again. Existing result reads, waiting and permitted recovery follow the action's own protocol. Different source requests with equal arguments are not content-deduplicated. Creating another Invocation cannot bypass a prohibition on re-executing the original request. Concrete confirmation/error ordering remains subject to the complete operation interface.

Subsequent resolution: Q178 permits existing lawful association confirmation under historical read eligibility before new-execution admission, while preserving structural checks and uncertainty distinctions.

Intended destination: agent/tools.md source-request association and foundation/storage.md atomic uniqueness. Actual writeback: this register only.

<a id="cg06-q143"></a>
### CG06-Q143 — Derive model-origin action input from its durable source

Status: ACCEPTED. The model-origin Tool entry takes execution qualification and the selected durable-response locator. Runtime derives the name and raw arguments from that response, then applies controlled action mapping, strict parsing and admission.

Do not accept an independently supplied action/argument copy as a competing authority. Application-origin controlled actions use their own typed entry and do not fabricate a model parent.

Intended destination: agent/tools.md internal entry and agent/execution-runtime.md response-to-action handoff. Actual writeback: this register only.

<a id="cg06-q144"></a>
### CG06-Q144 — Initial Tool admission rejection creates no Invocation

Status: ACCEPTED. A definite initial Tool admission rejection, such as unknown Tool, invalid arguments or failed initial permission, returns a typed rejection without creating a TOOL Invocation or new RejectedToolRequest durable lifecycle.

The producing MODEL response already retains the proposed request. Necessary rejection diagnostics can enter controlled logs or Eval evidence without becoming an execution record. Successful initial admission precedes atomic Invocation/association creation. Permission changes, cancellation and failures after that creation follow the existing Invocation/action protocol; they cannot be rewritten as never-admitted work. Execution-boundary revalidation remains required.

Intended destination: agent/tools.md initial rejection and action execution boundaries. Actual writeback: this register only.

<a id="cg06-q145"></a>
### CG06-Q145 — Trial identity is separate from Runtime and platform IDs

Status: ACCEPTED. Use local trial_id: UUIDv4 as an Eval evidence association identity for the actual Runs/Invocations, check findings/evidence and optional platform experiment/observation associations.

It is not a production Domain workflow aggregate, the first run_id or a Langfuse trace ID. Repeated experiments create new Trials; reassessing retained evidence remains associated with the original Trial. Detailed Eval storage/operation interfaces do not acquire Runtime execution authority from this identity.

Intended destination: evaluation/evaluation-observability.md Trial evidence correlation. Actual writeback: this register only.

<a id="cg06-q146"></a>
### CG06-Q146 — Whole-path DeepSeek replay replaces controlled HTTP transport

Status: ACCEPTED. Replay intended to prove M2's integrated DeepSeek path supplies recorded or synthetic responses at the controlled HTTP transport boundary while retaining real Runtime, Gateway, DeepSeekAdapter, stream parsing and response encoding.

Declare replay versus live for each Trial. Replay checks the expected request against actual input; mismatch fails without fallback to a real API. Gateway mocks remain valid for scoped unit tests but cannot claim actual adapter mapping/parser coverage. Concrete request matching and replay-cost interpretation remain open. No live call or SDK-specific behavior is authorized or proven by this decision.

Subsequent resolution: Q156 separates replay ledger values from current live cost, and Q157 defines semantic/configuration matching without transport secrets.

Intended destination: evaluation/evaluation-observability.md replay scope and DeepSeekAdapter verification seams. Actual writeback: this register only.

<a id="cg06-q147"></a>
### CG06-Q147 — Versioned reproducible fixture semantics, replaceable storage form

Status: ACCEPTED with user amendment. The Contract requires an explicit fixture format/version identity, sufficient exact inputs/identities/configuration to reconstruct the isolated environment, and deterministic hydration validation. Missing or incompatible necessary content fails; never fall back to latest. Fixture consumers own their closed schemas and coherence checks.

First-implementation/handoff decision: M2 initially uses JSON bundles with a controlled thin hydrator. JSON is not a permanent normative exchange format or compatibility obligation. No general fixture DSL is introduced. A specialized recovery test may use a SQLite snapshot under its declared schema/recovery preconditions without superseding the storage-neutral reproducibility Contract.

SUPERSEDED proposal interpretation: the first JSON fixture bundle becomes the lasting normative fixture storage representation. Reproducible, versioned semantics are normative candidates; JSON plus controlled hydration is the accepted initial implementation choice, consistent with Architecture 15.2's deferred storage form.

Intended destination: evaluation/evaluation-observability.md fixture semantics; eventual M2 implementation/handoff for JSON representation. Actual writeback: this register only.

<a id="cg06-q148"></a>
### CG06-Q148 — Typed check conclusions independent of task outcome

Status: ACCEPTED. Each check has an explicit conclusion: PASS (sufficient evidence meets the check), FAIL (evidence establishes a violation), INCOMPLETE (required evidence/process is incomplete), ERROR (checker execution failed), UNASSESSABLE (expectation or judgment basis cannot support a valid assessment), or NOT_APPLICABLE (declared scope makes the check inapplicable, with reason).

Store check conclusions separately from task success/failure. A required unexecuted check is not inapplicable. INCOMPLETE, ERROR, UNASSESSABLE and NOT_APPLICABLE cannot count as passing results. This does not define an aggregate score, denominator, release threshold or new platform evaluator engine.

Intended destination: evaluation/evaluation-observability.md check result semantics. Actual writeback: this register only.

<a id="cg06-q149"></a>
### CG06-Q149 — Explicit pre-export telemetry allowlist

Status: ACCEPTED. Default M2 export forms a controlled projection from an explicit field allowlist before upload. Admit necessary local correlation IDs, controlled configuration keys, hashes, counts, usage, budget amounts, durations and typed outcome codes.

Do not default-export whole Frames, responses, reasoning, Tool arguments/results, free-text exceptions or credentials, or rely on automatic raw SDK capture followed by later cleanup. A particular evaluator's body access follows its separate evidence-admission protocol. Actual callback/SDK realization remains version-specific research/implementation; no generic Telemetry Port is introduced.

Intended destination: evaluation/evaluation-observability.md default export admission and actual integration masking. Actual writeback: this register only.

<a id="cg06-q150"></a>
### CG06-Q150 — Immutable Trial evidence manifest, canonical references first

Status: ACCEPTED with user amendment. Re-evaluation consumes retained evidence from the original Trial. Use an immutable evidence manifest/retained evidence set that preferentially binds exact references and format/hash/integrity identities to canonical immutable evidence where availability is guaranteed.

Existing retained ContextFrames, terminal responses, Invocation evidence and Budget evidence do not require wholesale copying into another Runtime payload archive. Preserve an admitted Eval-owned evidence copy only where isolation, independent long-term reassessment or permitted source cleanup creates a real retention need. Mere reference existence does not establish payload availability or immutability; mutable summaries need an appropriate exact evidence basis.

If reassessment needs isolated test-database post-state, retain evidence of that Trial's actual post-state. Later hydration of the initial fixture and re-execution/derivation cannot substitute for the original result. Re-evaluation retains prior assessments and records its new evaluator configuration/results; unavailable required evidence yields an explicit incomplete/unavailable assessment, never silent task rerun.

SUPERSEDED proposal interpretation: a Trial evidence package defaults to copying Frame, response and post-state into a third persistent authority or second Runtime archive. Exact canonical references come first; Eval copies only evidence it independently must retain under admission.

Intended destination: evaluation/evaluation-observability.md retained evidence/reassessment and foundation/storage.md applicable availability/integrity boundaries. Actual writeback: this register only.

## Round 15 persistence and local review

- Q141–Q150 are accepted with Q147/Q150 amendments. The JSON choice is explicitly implementation/handoff-only; Trial evidence is reference-first and does not duplicate Runtime payload ownership. Q61's historical locator gap now points to its concrete resolution.
- Decision-to-Document Traceability: all ten decisions identify prospective owners and register-only writeback. Both superseded interpretations remain explicit. No normative JSON storage mandate, generic fixture DSL, RejectedToolRequest lifecycle or duplicate Runtime archive is inferred.
- Cross-Document Semantic Consistency: reviewed Architecture 15.1–15.5, Eval Acceptance 2, EVO-001/003/006 and EXR action-specific evidence against Q58–Q64/Q111/Q134. Initial Tool rejection differs from an action outcome after admission; repeated source association is not re-execution permission. Fixture storage-neutral semantics and reference-first retained evidence preserve the existing architecture. Eval conclusions and export do not become business authority.
- Only this register was edited. No implementation, live call, fixture hydration or normative publication occurred. M2 remains Pending; selected SDK/platform behavior and necessary producer/consumer details still require their own closure.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q150 anchors/headings and register-only writeback, Q151–Q160 unanswered topic identities, all thirty-two supersession annotations, explicit Q141/Q144/Q147/Q148/Q150 detail checks, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish document integrity, not Runtime/adapter/Eval execution proof.

## Round 16 — Consumer-scoped evaluators and stable historical findings

The user accepted Q151–Q160 with amendments to Q154/Q155/Q158. Every destination below is prospective; actual writeback is this register only. No Generic Quality Judge delivery requirement or permanent Eval Provider restriction is introduced.

<a id="cg06-q151"></a>
### CG06-Q151 — Capture exact evidence for mutable observations

Status: ACCEPTED. An object ID resolving to current mutable Budget totals or test-database post-state is insufficient historical evidence. Existing immutable records can be retained by exact reference/integrity identity; otherwise capture the smallest necessary consistent actual-state projection at the declared observation boundary.

Later reads through the same ID cannot substitute latest values for the Trial's original observation. This does not require copying the entire database or adding history/version entities to every business object.

Intended destination: evaluation/evaluation-observability.md evidence capture and foundation/storage.md applicable exact reads. Actual writeback: this register only.

<a id="cg06-q152"></a>
### CG06-Q152 — Declare expected checks before observing results

Status: ACCEPTED. Freeze the expected check set, exact definitions/configuration, applicability conditions and requiredness before observing Trial results. Report coverage against that declaration. A required unexecuted check is explicitly INCOMPLETE rather than absent from the report.

New checks may be introduced in a new evaluation configuration for reassessment; do not retroactively rewrite an earlier evaluation's declared coverage. This is thin evaluation configuration/evidence, not a new general check-planning platform.

Intended destination: evaluation/evaluation-observability.md declared coverage and completeness. Actual writeback: this register only.

<a id="cg06-q153"></a>
### CG06-Q153 — Minimum individual check-result association

Status: ACCEPTED. Each result associates trial_id, check_key, an exact evaluator/check configuration reference, conclusion, typed reason_code and the actual evidence references used. Controlled bounded explanation may supplement these fields. Numeric metrics are supplied only when the individual check defines their units and meaning; no score is mandatory for every check.

The check protocol owns reason_code interpretation rather than a universal failure-code catalog. A bare boolean without evidence traceability is insufficient. Repeated execution identity is independently required by Q155; this projection alone is not a uniqueness key for attempts.

Intended destination: evaluation/evaluation-observability.md individual check results. Actual writeback: this register only.

<a id="cg06-q154"></a>
### CG06-Q154 — Consumer-enabled bounded read-only evaluator protocol

Status: ACCEPTED with user amendment. M2 Eval infrastructure supports independent evaluator invocation, separate resource/configuration/evidence admission, no inherited Agent permissions and no business-result authority. It does not invent or require delivery of a Generic Quality Judge with semantic judgment responsibilities.

When a real consumer enables an LLM evaluator, the initial protocol allows a controlled rubric plus separately admitted evidence to produce a structured judgment through a bounded read-only invocation. It grants no autonomous Tools, Memory, external retrieval or business writes. Task outputs and Tool text remain untrusted evidence, not control. Any additional evidence is admitted by evaluation preparation rather than autonomously acquired by the judge.

The first actual semantic consumer owns the rubric, semantic meaning and evidence sufficiency for PASS/FAIL. An infrastructure verification fixture cannot manufacture product-quality authority. M2 completion does not require a generic semantic Judge; infrastructure isolation/resource/evidence proof remains required.

SUPERSEDED proposal interpretation: “first M2 LLM judge support” requires M2 to deliver a real generic semantic Judge or define its quality rubric and pass/fail semantics. The initial read-only protocol is conditional on an actual consumer; infrastructure obligations remain.

Intended destination: evaluation/evaluation-observability.md infrastructure/consumer split and later semantic consumers for rubric meaning. Actual writeback: this register only.

<a id="cg06-q155"></a>
### CG06-Q155 — Independently identifiable evaluator executions

Status: ACCEPTED with user amendment. Retain every actual evaluator execution's configuration, evidence association, result/error and separate resources. Each execution must have an unambiguous independent identity: trial_id plus check_key plus evaluator configuration cannot distinguish repeated real executions.

A later execution cannot overwrite or impersonate an earlier attempt. The concrete identity may be an evaluator_attempt_id or a stable ordinal within an identified evaluation record; representation remains open. No Universal Attempt lifecycle follows from this identity requirement.

Subsequent resolution: Q161 selects evaluator_attempt_id: UUIDv4 allocated before execution, without a mandatory parent evaluation aggregate or ordinal.

The same configuration does not guarantee the same model judgment, so another actual execution is not idempotent confirmation of the prior one. Explicit reassessment evaluates retained Trial evidence, not the Agent again. The initial implementation has no hidden automatic reassessment or default best-attempt selection; all actual attempts remain visible.

SUPERSEDED incomplete interpretation: preserving repeated results without a stable way to distinguish their actual evaluator executions is sufficient. Independent historical execution identity is mandatory; a universal attempt state machine is not.

Intended destination: evaluation/evaluation-observability.md evaluator identity, resources and reassessment. Actual writeback: this register only.

<a id="cg06-q156"></a>
### CG06-Q156 — Replay accounting is not current live Provider cost

Status: ACCEPTED. An isolated replay ledger may use recorded/synthetic usage to exercise real reservation and settlement logic, but resulting amounts are simulated accounting for that Trial, not cost of a corresponding live Provider request during that replay.

Distinguish historical recorded usage, synthetic usage and current live observations by their evidence origin. A replay's business-like ledger behavior does not change the fact that no corresponding external model request occurred. Preserve the tested Budget calculation rules rather than bypassing accounting in replay.

Intended destination: evaluation/evaluation-observability.md replay evidence interpretation and foundation/budget.md isolated test accounting consumption. Actual writeback: this register only.

<a id="cg06-q157"></a>
### CG06-Q157 — Replay matches exact semantic request and controlled configuration

Status: ACCEPTED. Match actual semantic input and execution-affecting controlled configuration, including messages, Tool schemas, model, thinking mode and effective output limit. Exclude authentication secrets and purely dynamic transport details from fixture matching.

Declared format interpretation may ignore transport-only differences such as JSON object key ordering. It must not ignore message order, text, Tool arguments or additional model parameters. No generic fuzzy matching/request-rewriting system is introduced: undeclared semantic differences fail without nearest-fixture selection or live fallback.

Intended destination: evaluation/evaluation-observability.md replay matching and DeepSeekAdapter controlled transport tests. Actual writeback: this register only.

<a id="cg06-q158"></a>
### CG06-Q158 — Fail-closed Trial isolation with explicitly admitted live configuration

Status: ACCEPTED with user amendment. Before executing a Trial, verify explicit isolated storage, consistency with the declared replay/live mode and controlled recruiting-platform/other external side-effect paths. Missing or contradictory configuration rejects startup; do not inherit a production Workspace or default production connections.

The stable Eval Contract is Provider-neutral: replay uses an explicit controlled replay transport and never falls back to any live Provider; live uses only the controlled Provider configuration expressly allowed by that Trial. The thin test composition boundary enforces this without introducing an environment-management platform.

Current M2 implementation/handoff rule: allowed live Provider configuration is the reviewed DeepSeek configuration, reflecting the sole current production adapter. This is not a permanent generic Eval restriction on future Providers.

SUPERSEDED proposal scope: “live must use DeepSeek official endpoints” as an enduring universal Eval Contract invariant. It remains the current M2 implementation safety rule; explicit admission and isolation are the stable Contract boundary.

Intended destination: evaluation/evaluation-observability.md isolation and eventual M2 implementation/handoff for current DeepSeek configuration. Actual writeback: this register only.

<a id="cg06-q159"></a>
### CG06-Q159 — Later accounting evidence does not rewrite earlier findings

Status: ACCEPTED. Budget may reconcile trustworthy late usage normally while prior evaluations retain the evidence and conclusions they actually used. Reassessing cost with new accounting evidence creates an additional explicit evaluation and keeps its associations and earlier findings.

Current ledger views may change. Historical assessments must not silently replace unknown with known and imply that later information was already available at the original evaluation.

Intended destination: evaluation/evaluation-observability.md historical findings and foundation/budget.md evidence-consumer boundary. Actual writeback: this register only.

<a id="cg06-q160"></a>
### CG06-Q160 — Required local evidence failure differs from optional export failure

Status: ACCEPTED. Optional telemetry upload failure does not invalidate checks with sufficient required local evidence. Failure to retain necessary local Trial evidence prevents dependent checks from claiming complete success.

Preserve truthful task results; report affected check incompleteness and evidence-capture errors without rolling back business facts or automatically rerunning the Agent to manufacture evidence. Other independently supported checks retain their valid conclusions. Production outcome, evidence availability and export success remain separate.

Intended destination: evaluation/evaluation-observability.md evidence failure and foundation/storage.md applicable capture results. Actual writeback: this register only.

## Round 16 persistence and local review

- Q151–Q160 are accepted with Q154/Q155/Q158 amendments. M2 enables independent evaluator infrastructure without a Generic Quality Judge completion requirement. Every actual evaluator execution needs a distinct identity, and DeepSeek-only live configuration is scoped to the current implementation.
- Decision-to-Document Traceability: every decision identifies prospective owners and register-only writeback; all three displaced interpretations remain explicit. Q146's replay matching/cost branches now reference Q156/Q157. No Universal Attempt lifecycle or permanent Eval Provider restriction is inferred.
- Cross-Document Semantic Consistency: checked SL-03.M2's joint agreement/completion scope, Architecture 15, Q111/Q145–Q150 and the existing EVO real-evidence boundaries. First semantic consumers continue owning evaluator meaning. Immutable evaluation evidence can reference canonical payloads while mutable observations require exact capture. Late accounting and failed evidence capture do not alter business outcomes or grant replay.
- Only this register was edited. No implementation, live call, evaluator execution or normative publication occurred. M2 remains Pending; concrete integration research, resource fields/bounds and remaining producer/consumer interfaces are not silently closed.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q160 anchors/headings and register-only writeback, Q161–Q170 unanswered topic identities, all thirty-five supersession annotations, explicit Q154/Q155/Q158 refinement checks, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish document integrity, not Runtime/adapter/Eval execution proof.

## Round 17 — Foreground resource scope without a generic Tool wallet

The user accepted Q161–Q170 with amendments to Q163/Q165/Q170. Every destination below is prospective; actual writeback is this register only. The current Tool proof consumer establishes no need for an Operation-wide Tool quota.

<a id="cg06-q161"></a>
### CG06-Q161 — Concrete evaluator execution identity

Status: ACCEPTED. Allocate evaluator_attempt_id: UUIDv4 before actual evaluator execution. Associate it with the original trial_id, check_key, exact configuration and actual evidence. This distinguishes executions without a mandatory parent evaluation aggregate or concurrently allocated ordinal.

The identity introduces no Universal Attempt lifecycle and does not authorize retransmission after an uncertain outcome. Existing attempt/result confirmation and a new actual execution remain distinct.

Intended destination: evaluation/evaluation-observability.md evaluator execution association. Actual writeback: this register only.

<a id="cg06-q162"></a>
### CG06-Q162 — Freeze Run-local resource limits with semantic binding

Status: ACCEPTED. Freeze the Run's actual resource limits and their interpretation basis in the initial semantic-binding transaction. Configuration changes, recovery and new execution grants do not reset or replace them.

These belong to M2 semantic Run Budget binding, not universal mandatory budget fields on every M1 AgentRun. Freezing ceilings does not reserve all future spending; each actual Invocation still occupies applicable resources at admission.

Intended destination: foundation/budget.md Run-local limits and agent/execution-runtime.md initial binding. Actual writeback: this register only.

<a id="cg06-q163"></a>
### CG06-Q163 — Initial Operation dimensions exclude speculative Tool quotas

Status: ACCEPTED with user amendment. Current M2 foreground Operation Budget supports a closed set of MODEL call count, cumulative total tokens and optional CNY monetary budget. Total tokens count admitted input plus output totals without adding cache-hit or reasoning subcomponents again. An allocation enables at least one finite dimension; enabled/disabled meaning is explicit and zero is not disabled. Runs retain their own finite execution boundaries and deadline.

Tool boundedness remains Skill-owned action allowlists/finite calling boundaries plus ToolInvocationRuntime per-execution admission and action-specific recovery. Add an Operation-wide TOOL count only when an actual Tool consumer needs a shared quota. The present controlled local-read consumer does not establish that need; a cheap exact read and a future expensive action need not share a generic Tool-call wallet.

No arbitrary resource plugin/dictionary, separate input/output token envelopes or general quota platform is introduced. A future actual resource consumer may justify an explicit extension.

SUPERSEDED proposal fragment: including TOOL call count in the initial Operation ledger merely for symmetry with MODEL calls. Tool bounds/admission remain mandatory without this shared ledger dimension. This also narrows any generic MODEL/TOOL counting wording in Q164 to the actually supported resource ownership.

Intended destination: foundation/budget.md foreground dimensions; agent/execution-runtime.md Skill boundaries and agent/tools.md action admission. Actual writeback: this register only.

<a id="cg06-q164"></a>
### CG06-Q164 — Semantic steps are defined by their Skill consumer

Status: ACCEPTED, interpreted with Q163's resource-scope amendment. Do not treat every graph node, function call or validation as one generic semantic step. The Skill's real consumer defines semantic workflow transitions and finite structure; Runtime enforces them.

Budget remains the sole authority for its applicable resource accounting. A Skill step count cannot establish remaining money/token resources. Q163 does not introduce Operation Tool quota, and this decision does not restore it. M2 adds no Operation max_steps lacking a consumer-defined unit. A later real shared step allowance needs an explicit unit and Budget debit boundary.

Intended destination: agent/execution-runtime.md Skill execution bounds and foundation/budget.md actual resource units. Actual writeback: this register only.

<a id="cg06-q165"></a>
### CG06-Q165 — Consistent Budget reads explain exposure by dimension

Status: ACCEPTED with user amendment. A read-only Budget view consistently presents original frozen allocation, settled consumption, outstanding reservations, necessary unresolved exposure facts and derived availability/overrun. It must not hide unknown occupancy or overrun behind one remaining-budget number.

Preserve explainable unresolved exposure/reservation facts per applicable resource dimension. Monetary usage may remain unknown for one Invocation while tokens are settled for another and other reservations remain outstanding. A single unknown_exposure boolean is insufficient to identify which availability cannot safely be released. Component states or associated detail may express this; no Universal Exposure entity is required and the concrete representation remains open.

The read grants no dispatch permission. A recently sufficient view cannot replace atomic reservation for the actual invocation.

SUPERSEDED underspecified interpretation: one global unknown_exposure flag sufficiently explains all resource uncertainty. The view must distinguish the applicable unresolved dimensions and their accounting basis.

Intended destination: foundation/budget.md consistent read projection and uncertainty interpretation. Actual writeback: this register only.

<a id="cg06-q166"></a>
### CG06-Q166 — Insufficient budget rejects admission without a funds queue

Status: ACCEPTED. Current resource insufficiency produces a typed admission rejection. M2 introduces no funds-waiting queue, automatic wakeup or waiting-for-top-up lifecycle. Q127's temporary concurrency-capacity waiting is a different mechanism.

A later release may allow a consumer-protocol-controlled admission attempt; it does not automatically replay already sent or outcome-unknown work. No independent consumer continuation/retry policy is invented here.

Intended destination: foundation/budget.md shortage outcome and agent/execution-runtime.md consumer continuation boundary. Actual writeback: this register only.

<a id="cg06-q167"></a>
### CG06-Q167 — Result publication has no complete-settlement prerequisite

Status: ACCEPTED. Do not add full usage/cost settlement as an extra prerequisite for publishing a valid business result. The consumer may publish only when its own permissions, sources, execution authority and commit/recovery protocol permit it. Unknown cost remains conservatively occupied, never zeroed or released merely because a result is available.

This grants no exception to ended-Run/revocation rules and no permission for subsequent calls. Further invocation admission uses the then-current ledger. Independently valid result authority and accounting convergence remain separate.

Intended destination: foundation/budget.md settlement/result independence and agent/execution-runtime.md consumer publication boundary. Actual writeback: this register only.

<a id="cg06-q168"></a>
### CG06-Q168 — Admit usage counts without coercion

Status: ACCEPTED. Token/count usage values must be exact nonnegative integers within their controlled technical range. Do not coerce strings/booleans, round fractions or truncate invalid values. Missing values are not zero.

Invalid components retain a metering anomaly and unresolved meaning rather than fabricated trusted usage. Apply owned association/consistency rules to determine whether other components remain trustworthy. Metering invalidity does not automatically invalidate independently complete terminal-response evidence. Exact finite scalar bounds remain to be closed.

Intended destination: DeepSeekAdapter metering admission and foundation/budget.md usage evidence. Actual writeback: this register only.

<a id="cg06-q169"></a>
### CG06-Q169 — Explicit units in current DeepSeek pricing basis

Status: ACCEPTED. The current controlled pricing representation explicitly identifies CNY, rates per 1,000,000 tokens, cache-hit input price, cache-miss input price and output price. Use exact decimal values and retain the selected applicability basis.

Do not leave rate units implicit or charge reasoning again as an additional output total. This is the current Adapter/Budget representation, not a generic PriceRule entity. No current numerical rate or live pricing lookup is selected by this decision.

Intended destination: foundation/budget.md exact reservation/cost basis and DeepSeekAdapter metering mapping. Actual writeback: this register only.

<a id="cg06-q170"></a>
### CG06-Q170 — Complete current foreground monetary-allocation representation

Status: ACCEPTED with user amendment. Within M2's current ForegroundBudgetAllocation complete representation, monetary is required and either null (explicitly disabled) or a complete object with currency: CNY and limit in Q121's eight-place decimal-string form. A zero amount is an enabled real constraint.

Do not add a duplicate monetary_enabled flag or retain a meaningless currency for a disabled dimension. Requiring this field belongs to the current foreground schema only; future background/Eval or other budget owners need not adopt this envelope.

SUPERSEDED proposal scope: making mandatory monetary presence a universal rule for every future Budget allocation. The null-versus-zero distinction remains normative for the current foreground representation.

Intended destination: foundation/budget.md M2 foreground allocation shape. Actual writeback: this register only.

Subsequent resolution: Q171 closes the surrounding current foreground allocation fields; Q173 selects its creation/confirmation operation. Future owner schemas remain outside this representation.

## Round 17 persistence and local review

- Q161–Q170 are accepted with Q163/Q165/Q170 amendments. Operation resources exclude speculative Tool count; uncertainty must remain explainable per dimension; the complete monetary field belongs only to M2 foreground allocation. Q155's identity branch resolves to evaluator_attempt_id.
- Decision-to-Document Traceability: each decision identifies prospective owners and register-only writeback; all three displaced interpretations remain explicit. Q164 is explicitly read under Q163's current resource scope rather than restoring a Tool wallet. No Exposure entity, resource plugin or universal allocation envelope is inferred.
- Cross-Document Semantic Consistency: checked Architecture 9/11, EXR-029's concrete local-read consumer, Q3/Q38/Q69–Q80/Q116/Q122/Q140 and Q155. Tool admission/recovery does not imply shared Operation quota. Result publication retains its own authority despite pending settlement. Frozen Run limits are not upfront spending reservations, and historical views cannot authorize new dispatch.
- Only this register was edited. No implementation, live call, pricing verification or normative publication occurred. M2 remains Pending; full operation shapes, scalar ranges, Frame/provider details and integration proof still require closure.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q170 anchors/headings and register-only writeback, Q171–Q180 unanswered topic identities, all thirty-eight supersession annotations, explicit Q163/Q164/Q165/Q170 refinement checks, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish document integrity, not Runtime/adapter/Eval execution proof.

## Round 18 — Complete foreground allocation and safe accounting arithmetic

The user accepted Q171–Q180 with an amendment completing Q172's integer arithmetic boundary. Every destination below is prospective; actual writeback is this register only.

<a id="cg06-q171"></a>
### CG06-Q171 — Complete current foreground allocation fields

Status: ACCEPTED. The current M2 foreground allocation has exactly three required fields: model_call_limit (nonnegative integer or null), total_token_limit (nonnegative integer or null), and monetary (Q170's complete monetary object or null). Null explicitly disables a dimension; zero enables a zero allowance. At least one field must be nonnull. Reject unknown fields and do not add TOOL count.

Creation retains the Runtime-selected allocation format identity. This is a closed current foreground representation, not an arbitrary resource dictionary or an envelope imposed on future unrelated owners.

Intended destination: foundation/budget.md foreground allocation admission/representation. Actual writeback: this register only.

<a id="cg06-q172"></a>
### CG06-Q172 — Bounded integers require checked accounting arithmetic

Status: ACCEPTED with user amendment. Configured MODEL-count and total-token quotas use exact integers in 0 through 2^63 - 1. Reject booleans, strings and out-of-range input rather than truncate or coerce. This is a technical representation boundary, not a recommended business quota.

Every reservation, settled-usage and cumulative-counter update using this integer representation must check overflow. If the next exact accumulation cannot be represented, fail closed: no wrapping, saturation or clipping, and no fabricated available balance. This decision does not introduce arbitrary-precision integer accounting.

Reliably obtained Provider usage must not be reduced to fit a local counter. Preserve the original usage evidence that can be retained and mark affected Budget accounting as unable to safely admit further work. Known overrun remains truthful evidence even when it cannot be incorporated into the supported cumulative representation. Detailed durable blocking/error expression remains to be closed without creating a new business aggregate.

Subsequent resolution: Q181 requires recoverable accounting-obstruction evidence; Q183 distinguishes rejected uncommitted candidates from actual usage that cannot safely accumulate. Concrete error/storage expression remains owner-specific.

SUPERSEDED incomplete proposal: limit allocation inputs to signed-64-bit range while leaving counter updates unspecified or assuming unbounded exact accumulation. The supported representation also requires checked arithmetic and fail-closed accounting; truthful usage is not replaced by a smaller representable value.

Intended destination: foundation/budget.md integer arithmetic, admission and evidence preservation; common.md only if genuinely shared. Actual writeback: this register only.

<a id="cg06-q173"></a>
### CG06-Q173 — One foreground budget creation/confirmation operation

Status: ACCEPTED. The internal idempotent ensure_foreground_budget(operation_id, original_allocation) creates a valid absent scope atomically, confirms an existing same-original-allocation scope through its consistent read view, or returns a typed allocation conflict for a different allocation.

Historical comparison uses the creation-time allocation semantics rather than current defaults. Confirmation does not replenish or reset accounting. Necessary read access and structural checks precede confirmation; no create-attempt identity or separate retry-create/confirm operation is introduced.

Intended destination: foundation/budget.md foreground scope operation and foundation/storage.md atomic uniqueness/confirmation. Actual writeback: this register only.

<a id="cg06-q174"></a>
### CG06-Q174 — Broken committed Budget binding is not absent initial allocation

Status: ACCEPTED. Missing or inconsistent mandatory Budget ownership/records for an already committed Run binding is a persistence-association integrity problem; stop affected admission. Distinguish proven absence/inconsistency from temporary inability to read.

Do not reconstruct default funds, rebind to another owner or infer zero consumption. This differs from semantic-start finding that the caller has not established its required Budget scope, which is an ordinary precondition rejection.

Intended destination: foundation/budget.md bound-owner integrity and foundation/storage.md required associations. Actual writeback: this register only.

<a id="cg06-q175"></a>
### CG06-Q175 — Budget calculates reservation from admitted immutable bases

Status: ACCEPTED. Budget Runtime calculates reservation from Invocation/Run binding, the immutable Q140 estimator basis, effective output cap and frozen reservation/pricing assumptions. An upstream caller may prepare inputs but cannot establish accounting truth by claiming its own reserve_amount or token quantity.

Calculation may occur outside the transaction. Q69 must verify the bases still correspond to the actual Frame/configuration and atomically check/occupy resources. This does not add a second Frame or estimator authority.

Intended destination: foundation/budget.md reservation calculation and agent/execution-runtime.md atomic admission inputs. Actual writeback: this register only.

<a id="cg06-q176"></a>
### CG06-Q176 — Shortage identifies applicable scope and dimension

Status: ACCEPTED. A typed budget-insufficiency rejection identifies actual shortage scope (OPERATION or RUN) and dimension (MODEL_CALLS, TOTAL_TOKENS or MONETARY). Multiple shortages found in one atomic check may be returned in deterministic order. Unknown occupancy is not mislabeled as settled consumption.

PARTIALLY SUPERSEDED scope interpretation by Q186: these scope/dimension alternatives are not an unrestricted cross-product. Current M2 permits OPERATION with its enabled MODEL_CALLS/TOTAL_TOKENS/MONETARY dimensions, and RUN with MODEL_CALLS/TOTAL_TOKENS only. RUN/MONETARY would invent the expressly excluded per-Run monetary cap.

Skill semantic prohibition, permission denial and Context capacity failure retain their own meanings rather than being collapsed into Budget insufficiency. A Budget operation rejection is not automatically a Run terminal failure. Exact error representation/ordering follows the complete owned interface.

Intended destination: foundation/budget.md shortage results and agent/execution-runtime.md consumer disposition. Actual writeback: this register only.

<a id="cg06-q177"></a>
### CG06-Q177 — Model-origin Tool selection stays within its semantic Run

Status: ACCEPTED. In current M2, the producing MODEL Invocation and newly selected TOOL Invocation must belong to the same semantic Run. Shared operation_id does not share Skill, Context or execution authority and cannot authorize borrowing another Run's Tool request.

Lawful reuse of an existing result follows its own read/content-admission agreement, not execution of another Run's model instruction.

Intended destination: agent/tools.md parent association and agent/execution-runtime.md Run ownership validation. Actual writeback: this register only.

<a id="cg06-q178"></a>
### CG06-Q178 — Existing Tool association confirmation is historical and read-only

Status: ACCEPTED. With historical read eligibility and necessary structural/association checks, an existing lawful source-request association can be confirmed read-only first, returning the original invocation_id even when new execution is no longer eligible.

Confirmation does not call the handler or grant recovery permission. Only a proven absent association requiring first creation enters current Run/Skill/permission admission. Storage uncertainty or damaged association cannot be treated as absence and replaced. Complete source/association read integrity remains required without manufacturing a new historical execution authority.

Intended destination: agent/tools.md association confirmation/admission ordering and foundation/storage.md retained association integrity. Actual writeback: this register only.

<a id="cg06-q179"></a>
### CG06-Q179 — Execute against the definition exposed in the Frame

Status: ACCEPTED. Retain and verify the exact action/protocol/schema basis exposed to the model. A current registry item with the same Provider Tool name is insufficient to reinterpret historical arguments.

Compatible implementation fixes need not freeze source-code hashes, but changed parameter meaning, resource scope or action semantics cannot impersonate the original definition. Reject new execution if the original protocol cannot be obtained or verified. Existing completion-evidence reads retain their own agreement, distinct from current executability.

Intended destination: agent/tools.md registered protocol matching and agent/context.md frozen Tool exposure. Actual writeback: this register only.

<a id="cg06-q180"></a>
### CG06-Q180 — Serial execution position is distinct from historical durability

Status: ACCEPTED. Current M2 MODEL execution occupies its Run's serial position from PREPARED. Normal completion of this active interval requires exit from the real calling stage and a durable complete response. TOOL completion uses its action protocol, not copied MODEL phases.

Other terminal/fencing situations follow their existing protocols. Unresolved execution cannot become idle merely by clearing a flag. Historical responses and unsettled monetary reservations may remain after active execution ends; accounting completion is not a prerequisite for a subsequent otherwise-admitted Invocation.

Every next Invocation still passes full admission. This adds neither a permanent max_concurrent_invocations field nor a universal Invocation lifecycle, and does not make a retained durability record permanently active.

Intended destination: agent/execution-runtime.md M2 serial admission and agent/tools.md action-specific completion. Actual writeback: this register only.

## Round 18 persistence and local review

- Q171–Q180 are accepted with Q172's arithmetic amendment. The signed-64-bit quota boundary now includes checked counter updates and evidence-preserving failure; arbitrary-precision accounting, wraparound and saturation are not implicit fallbacks.
- Decision-to-Document Traceability: each decision identifies prospective owners and register-only writeback. Q172 preserves its displaced incomplete proposal. Earlier allocation/association/serial-admission branches now point to their concrete subsequent resolutions without erasing historical wording.
- Cross-Document Semantic Consistency: checked Q69/Q71/Q75/Q118/Q126/Q142–Q144/Q162–Q170 and EXR-006/008/009/027–029. Reservation calculation remains Budget-owned and jointly atomic with Frame/intent. Overflow cannot release exposure or alter Provider evidence. Historical association confirmation creates no execution permission; current seriality neither duplicates Tool phases nor waits for all accounting to settle.
- Only this register was edited. No implementation, live call, arithmetic execution test or normative publication occurred. M2 remains Pending. The scoped research below informs proposed stream support only; it is not wire verification.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q180 anchors/headings and register-only writeback, Q181–Q190 unanswered topic identities, all thirty-nine supersession annotations, explicit Q172/Q178/Q180 checks, the scoped research caveat, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These checks establish document integrity, not Runtime/adapter/Eval execution proof.

<a id="cg06-r4"></a>
## CG06-R4 — Scoped stream-layout recheck, not live protocol proof

A bounded read-only research recheck on 2026-09-23 retrieved indexed official [English Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion/) and [Chinese Chat Completions](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion/) content, both labeled crawled four days earlier. Their prose agrees: one final choice chunk carries nonempty finish_reason and whole-request usage, followed by data: [DONE], without a separate usage-only chunk. Earlier chunks omit usage or carry null according to include_usage. The current example follows the one-choice terminal layout.

Older indexed [Chinese content without the trailing slash](https://api-docs.deepseek.com/zh-cn/api/create-chat-completion), labeled crawled two months earlier, describes a separate usage-only chunk with choices=[], although its example uses the other layout. A separate current schema/example discrepancy remains: terminal delta.role is null in the example while the schema describes assistant text.

Direct page-open attempts timed out. Newer bilingual indexed agreement supports an intended layout, but crawl age does not prove a versioned transition or actual endpoint behavior. Slash/no-slash indexing is not established as a protocol distinction. No live API call, installation or file mutation was performed by research. Accepting only the newer layout or supporting both is a Contract support-policy choice; Q189/Q190 propose narrow choices, and actual parser/wire integration proof remains open. Missing/invalid usage remains separate from terminal-content completeness under Q104/Q111/Q115.

Subsequent resolution: Q189 explicitly selects the current official documented Chat Completions layout without historical usage-only compatibility. Its [DONE] marker is adapter-specific. Q190 closes absent/null role parsing. The preceding paragraph preserves this research checkpoint's open-choice state and retrieval limitations; the support-policy choice is no longer open, while actual integration proof remains outstanding.

## Round 19 — Operation-only money and current documented DeepSeek streams

The user accepted Q181–Q190 with amendments to Q186/Q189. Every destination below is prospective; actual writeback is this register only. Current monetary ownership and stream support are narrowed without changing M1's generic evidence model.

<a id="cg06-q181"></a>
### CG06-Q181 — Preserve accounting obstruction across restart

Status: ACCEPTED. In-memory blocking alone is insufficient when known usage cannot safely accumulate. Retain explainable recoverable obstruction evidence associated with the affected owner/Run, resource dimension and necessary usage so restart cannot silently treat accounting as healthy.

Incomplete settlement does not release the corresponding reservation. Affected accounting refuses new resource admission; independent healthy owners need not be disabled. This does not create a general Budget lifecycle or a freely callable reset-budget/unblock operation.

Intended destination: foundation/budget.md blocked accounting admission and foundation/storage.md durable evidence/recovery. Actual writeback: this register only.

<a id="cg06-q182"></a>
### CG06-Q182 — Finite nonnegative CNY ledger representation

Status: ACCEPTED. Current nonnegative ledger amounts use units of 10^-8 CNY in the nonnegative signed-64-bit range, from 0.00000000 through 92233720368.54775807 CNY. External representation remains Q121's eight-place decimal string. This is a logical representation constraint, not a prescribed physical database column type.

Apply checked arithmetic to monetary reservations, debits and cumulative amounts. Source prices and pre-quantization cost evidence are not forced to eight places. Unrepresentable accounting preserves evidence and fails closed rather than wrapping, saturating or clipping.

Intended destination: foundation/budget.md bounded monetary amounts and exact calculation boundary. Actual writeback: this register only.

<a id="cg06-q183"></a>
### CG06-Q183 — Candidate arithmetic rejection does not damage healthy accounting

Status: ACCEPTED. An uncommitted candidate reservation that cannot be calculated/represented is rejected without writing its Frame, intent or reservation and without marking an otherwise healthy ledger as already damaged.

Distinguish that from real usage which has occurred but cannot safely accumulate: preserve evidence and block affected accounting under Q172/Q181. An actually uninterpretable existing ledger still blocks admission. An invalid proposed request cannot itself manufacture persisted accounting corruption for its owner.

Intended destination: foundation/budget.md arithmetic rejection and agent/execution-runtime.md pre-dispatch atomicity. Actual writeback: this register only.

<a id="cg06-q184"></a>
### CG06-Q184 — Settlement consumes absolute usage facts, not caller deltas

Status: ACCEPTED. Settlement consumes absolute usage facts for the Invocation's applicable components, not caller-interpreted additive/subtractive deltas. Identical evidence confirms without another charge; unknown components may converge under the owned protocol; conflicting trusted evidence cannot simply overwrite prior facts.

The ledger derives the one legitimate accounting change from confirmed state. Estimates and trustworthy usage retain their respective meanings. Repeated reconciliation cannot accumulate the same absolute usage repeatedly.

Intended destination: foundation/budget.md settlement input/equality and derived debit. Actual writeback: this register only.

<a id="cg06-q185"></a>
### CG06-Q185 — Current total-token dimension settles against a trusted full total

Status: ACCEPTED. Current TOTAL_TOKENS settlement requires a trustworthy complete total admitted under the protocol. Do not create input/output token subledgers for M2. Partial input facts may be retained without releasing the full token reservation.

The current DeepSeek mapping forms or validates the total using input/output totals without counting cache/reasoning subcomponents twice. Different supported resource dimensions may converge separately, such as settled tokens with monetary exposure still unresolved. This specializes the current token dimension without erasing per-component source evidence.

Intended destination: foundation/budget.md token settlement and DeepSeekAdapter metering admission. Actual writeback: this register only.

<a id="cg06-q186"></a>
### CG06-Q186 — Run-local limits do not duplicate monetary allocation

Status: ACCEPTED with user amendment. Current M2 semantic Runs require finite model_call_limit, total_token_limit and deadline. The call/token limits freeze with the semantic Budget binding; the deadline uses the existing Run deadline protocol rather than a duplicate time field/authority.

Foreground Operation Budget owns optional model-call and total-token allocations and optional CNY monetary allocation, shared and contested by its Runs. Current Run-local limits contain no monetary limit/envelope. Invocation admission intersects the applicable Run-local and Operation-level constraints; Skill Tool/semantic-step boundaries retain their own owner.

A future real consumer may introduce a per-Run monetary cap only with a clear definition of whether it is an admission ceiling or an actual monetary allocation. M2 does not create RMB subwallets merely for symmetry.

SUPERSEDED proposal fragment: adding optional monetary to the initial Run-local limit shape. Operation monetary ownership remains; no current RUN/MONETARY shortage or reservation authority is introduced. Required finite call/token/deadline limits remain accepted.

Intended destination: foundation/budget.md Operation versus Run ownership and agent/execution-runtime.md semantic Run limits. Actual writeback: this register only.

<a id="cg06-q187"></a>
### CG06-Q187 — Local ceilings need not be clamped to owner allocations

Status: ACCEPTED. Run-local call/token limits may exceed the corresponding Operation limit without a size-comparison-only startup rejection or automatic rewrite. Admission intersects the independent ceilings with current actual availability.

A local ceiling bounds the task, not a promise of funds/units allocated to it. Other Runs' shared-owner reservations remain relevant. No local wallet or upfront suballocation is inferred; Q186 supplies the actual Run-local dimensions.

Intended destination: foundation/budget.md intersecting admission and immutable local limits. Actual writeback: this register only.

<a id="cg06-q188"></a>
### CG06-Q188 — Initial Package format and actual-byte integrity

Status: ACCEPTED. M2 ContextPackage associates by run_id and retains package_format_key, deterministic serialized payload, byte_length and sha256. Publish it atomically with the initial Run/binding. No separate package UUID or mutable revision is introduced; integrity refers to actual retained bytes.

Package still represents initial input/scope/policy/capability manifest. It neither substitutes for an actual Frame nor replaces semantic-start request_fingerprint with its own hash. Concrete Package payload semantics retain Context/Skill/source ownership rather than becoming a universal effective-config blob.

Intended destination: agent/context.md initial Package representation and foundation/storage.md atomic integrity. Actual writeback: this register only.

<a id="cg06-q189"></a>
### CG06-Q189 — Adapter v1 supports the current documented stream layout

Status: ACCEPTED with user amendment. DeepSeek Chat Completions Adapter v1 supports the current official documented streaming layout: data: [DONE] terminates the stream; the last chunk before it contains whole-request usage; no independent choices=[] usage-only chunk is sent; the final content/choice chunk has exactly one choice and nonempty finish_reason. Do not implement a historical usage-only compatibility branch in M2.

The support basis is an explicit current official protocol definition, not merely a speculative preference for a newer-looking layout. CG06-R4 preserves how documentation was retrieved; that retrieval limitation does not leave the selected documented support profile undecided. If actual endpoint integration contradicts it, record a protocol research finding and reconcile the affected Adapter Contract rather than silently adding compatibility/fallback/retry.

[DONE] is adapter-specific terminal evidence, not a permanent ModelGateway invariant or a requirement for every DeepSeek API family. Generic Runtime consumes completion evidence defined by the actual adapter/format. Missing/invalid usage in an otherwise supported layout remains separately governed by Q104/Q111/Q115 and does not automatically invalidate complete terminal content. This decision is not a claim of executed wire verification.

SUPERSEDED proposal uncertainty/scope: treating the selected current documented layout as still an unresolved historical-compatibility choice, or promoting its [DONE] marker into generic Gateway termination. The current Chat Completions profile is selected; actual integration proof remains separate.

Intended destination: DeepSeekAdapter stream support and agent/execution-runtime.md adapter-owned terminal evidence. Actual writeback: this register only.

<a id="cg06-q190"></a>
### CG06-Q190 — Absent/null streamed role carries no role update

Status: ACCEPTED. For the current DeepSeek Chat Completions adapter, an absent or null delta.role supplies no new role information. A nonnull role must equal assistant exactly. The current response protocol's assistant role cannot be changed by fragments to user, system or tool.

Do not case-normalize or guess a repair. This explicit parser rule closes the schema/example discrepancy for the current adapter; it is not a universal role protocol for future Providers.

Intended destination: DeepSeekAdapter stream parsing and protocol conformance fixtures. Actual writeback: this register only.

## Round 19 persistence and local review

- Q181–Q190 are accepted with Q186/Q189 amendments. Monetary allocation remains Operation-owned; Run limits are finite call/token/deadline constraints. Adapter v1 follows the current official documented Chat Completions layout without a historical compatibility branch, and [DONE] remains adapter-specific.
- Decision-to-Document Traceability: all ten decisions identify prospective owners and register-only writeback; the displaced monetary sublimit and stream-support interpretations remain explicit. Q176's earlier scope/dimension wording is narrowed to exclude RUN/MONETARY. Q117/Q172 and CG06-R4 now point to their relevant subsequent resolutions.
- Cross-Document Semantic Consistency: reviewed Architecture 10–11, EXR-010–013 and Q102/Q104/Q111/Q115/Q118/Q126/Q162/Q171–Q180. Finite money does not erase exact source evidence. Candidate rejection differs from accounting obstruction after actual usage. Token settlement has one current total-token dimension. No duplicate deadline, monetary owner, Package request identity or universal stream marker is introduced.
- Only this register was edited. No implementation, live call, evaluator execution or normative publication occurred. M2 remains Pending; selected protocol support is distinct from executed integration proof.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q190 anchors/headings and register-only writeback, ten unanswered Q191–Q200 frontier rows, forty-two supersession sections, explicit Q186/Q189 and Q176 consistency checks, preserved research caveats, all five local file/anchor references, whitespace and conflict markers. git diff --check scoped to this register passed. These are document-integrity checks, not Runtime/adapter execution proof.

<a id="cg06-r5"></a>
## CG06-R5 — Tool continuation documentation facts and support-policy gaps

A bounded read-only official-source check on 2026-09-23 inspected [Tool Calls](https://api-docs.deepseek.com/guides/tool_calls/), [Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode/) and its [executable sample](https://api-docs.deepseek.com/api_samples/thinking_mode_api_example_tool_call/). These pages opened successfully. Direct Chat Completions retrieval timed out; the [official indexed schema](https://api-docs.deepseek.com/api/create-chat-completion/) was reported crawled four days earlier.

The schema requires a string tool_call_id on a tool-role reply, associating it with a returned call whose id is a required string. It explicitly requires unique Tool definition names, but the examined material does not explicitly require unique returned call IDs within a response. The non-thinking guide demonstrates one selected call; the thinking sample appends the full assistant message and replies to each returned call before continuing. Those examples do not establish a normative guarantee for partial reply sets, extra/duplicate replies, duplicate call IDs or ordering. Mandatory thinking guidance concerns preservation of applicable reasoning_content; it must not be misquoted as a complete reply-matching rule.

Q195/Q196 therefore propose conservative JobHunter support-profile admission choices, not claims that undocumented variants are forbidden by DeepSeek. Neither choice grants Tool execution permission or changes Skill ownership of list scheduling. No live Provider request or parser integration proof was executed.

## Round 20 — Discardable preparation and authoritative Tool admission

The user accepted Q191–Q200 with amendments to Q191/Q195/Q198. Every destination below is prospective; actual writeback is this register only. Provider support-profile restrictions do not become universal Harness rules.

<a id="cg06-q191"></a>
### CG06-Q191 — Pre-PREPARED candidates are discardable local preparation

Status: ACCEPTED with user amendment. Normally assemble/map/validate a candidate Frame and perform initial capacity evaluation before creating a MODEL PREPARED Invocation. This work is deterministic, local, discardable and recomputable; it may read authorized exact sources but produces no remote side effects, dispatch authority, reservation or durable Frame authority. After a crash, prepare again from authoritative sources rather than treating an abandoned candidate as recovery evidence.

Concurrent candidate preparation is permitted. Creation of PREPARED atomically competes for the current Run's serial execution position; only a lawful winner occupies it. Time already spent preparing grants no priority or sending permission. Q69 subsequently rechecks its mutable predicates and atomically freezes the actual Frame, reservation and dispatch intent. Failures after PREPARED use the existing M1 fencing/recovery agreements, not deletion or clearing an active flag.

SUPERSEDED incomplete interpretation: moving preparation before PREPARED while leaving its effects or recovery authority unspecified. Only discardable local preparation is permitted there; the atomic serial-position and Q69 boundaries remain authoritative.

Intended destination: agent/context.md candidate preparation and agent/execution-runtime.md serial preparation/admission. Actual writeback: this register only.

<a id="cg06-q192"></a>
### CG06-Q192 — Static guidance for the first headless implementation

Status: ACCEPTED. Required M2 headless Skill guidance comes from exact static Skill/configuration registration. Actual included instructions are retained in the producing Frame. Do not implement filesystem Skill discovery, dynamic plugins or a model-callable guidance loader for this scope.

Architecture's allowance for progressive disclosure remains: its first real consumer must define exact selection and admission rather than silently inheriting an unbounded loader. This decision does not require duplicating prompt bodies in Run configuration.

Intended destination: agent/execution-runtime.md Skill registration, agent/context.md instruction admission and M2 implementation handoff. Actual writeback: this register only.

<a id="cg06-q193"></a>
### CG06-Q193 — Current text and function-call Frame support

Status: ACCEPTED. Current M2 Context/DeepSeek support covers text messages, function Tool definitions/calls/results and required reasoning continuation. Unsupported image/audio/uploaded-file or remote-content forms are rejected rather than automatically fetched or coerced.

This is the current consumer's supported modality boundary, not a permanent restriction on every future ContextFrame or Gateway. A later actual modality consumer defines its own exact evidence and admission requirements.

Intended destination: agent/context.md current Frame profile and DeepSeekAdapter supported mapping. Actual writeback: this register only.

<a id="cg06-q194"></a>
### CG06-Q194 — Context reads Tool results through their owned evidence

Status: ACCEPTED. For the current Tool consumer with a durable result agreement, Context receives an exact TOOL Invocation result/evidence reference and obtains the result through its action-owned reader. New model reuse passes current content admission. Independently supplied caller text cannot impersonate that actual Tool result.

Any permitted projection/redaction is explained by Frame provenance. This does not create a generic Tool payload archive or erase the distinction between action completion and result representation/admission.

Intended destination: agent/tools.md result-read agreement and agent/context.md Tool-result inclusion. Actual writeback: this register only.

<a id="cg06-q195"></a>
### CG06-Q195 — Complete reply association in the current DeepSeek continuation profile

Status: ACCEPTED with user amendment. For current DeepSeek Chat Completions continuation, retaining an assistant turn with N tool_calls requires N corresponding lawful, admitted Tool results before the next MODEL continuation. Applicable thinking-mode reasoning_content is preserved according to the selected Provider protocol.

Skill still owns Tool-list selection and may end the continuation path after executing only a subset. It cannot delete unexecuted tool_calls, fabricate results or rewrite the original assistant turn to contain only executed requests. The adapter cannot execute the remaining Tools to complete the list. Existing action/result protocols define truthful replies; this decision creates no synthetic denial-result protocol.

SUPERSEDED scope interpretation: making complete reply coverage a permanent Harness invariant for all Tool-capable Providers. It is JobHunter's current DeepSeek Chat Completions continuation profile; a future adapter with a proven partial-continuation protocol may define its own lawful mapping. CG06-R5's distinction between official examples and unspecified edge-case guarantees remains intact.

Intended destination: DeepSeekAdapter continuation mapping, agent/context.md conversation integrity and Skill consumer disposition. Actual writeback: this register only.

<a id="cg06-q196"></a>
### CG06-Q196 — Duplicate Provider call IDs are not executable candidates

Status: ACCEPTED. Current JobHunter DeepSeek support rejects an ambiguous duplicate-ID Tool-call set from executable candidates. Preserve an otherwise complete durable terminal response; executable candidate admission cannot erase the Provider termination fact.

Do not rename Provider IDs, merge calls or substitute the internal tool_call_index for Provider identity. This is a JobHunter support restriction, not a claim of an explicit official returned-ID uniqueness guarantee.

Intended destination: DeepSeekAdapter candidate interpretation and agent/tools.md model-origin admission. Actual writeback: this register only.

<a id="cg06-q197"></a>
### CG06-Q197 — Deterministic local output validation

Status: ACCEPTED. Local Skill output validation is deterministic over explicitly supplied exact inputs/evidence and durable response content. It performs no hidden model call, external retrieval or business mutation.

Additional source acquisition uses its explicit admitted Application/Tool path; validation-guided repair is a separate admitted MODEL Invocation. Application retains business publication authority. A validator helper cannot bypass these boundaries.

Intended destination: agent/execution-runtime.md Skill validation and consuming Application interfaces. Actual writeback: this register only.

<a id="cg06-q198"></a>
### CG06-Q198 — Provider schema is a projection; Runtime owns final admission

Status: ACCEPTED with user amendment. The owned typed action input protocol supplies a controlled Provider-visible schema projection and an authoritative Runtime validator. The projection cannot contradict the actual protocol and must accurately express constraints supported by the selected Provider schema profile. Unsupported constraints remain Runtime-enforced; do not weaken the action Contract to fit Provider expressiveness.

Schema-valid generated arguments do not establish Runtime admission. Exact references, resource scope, permission, business eligibility and structural constraints beyond the projection remain subject to the complete Runtime validator. Schema generation techniques/libraries are implementation details, not an independent protocol authority.

SUPERSEDED overly strong equivalence: requiring the Provider schema to encode the entire Runtime input protocol or be equivalent to the complete validator. Shared ownership requires a faithful supported projection, not equal expressive power.

Intended destination: agent/tools.md typed input/projection/admission and DeepSeekAdapter schema mapping. Actual writeback: this register only.

<a id="cg06-q199"></a>
### CG06-Q199 — Historical Package reads distinguish absence and damage

Status: ACCEPTED. Internal Package access by run_id uses historical read eligibility and actual-byte integrity. Raw reads need not require a currently executable Skill or semantic decoder. Distinguish absent Run, nonsemantic Run with no Package by design, missing/corrupt mandatory semantic Package, temporary read unavailability and unavailable format interpretation.

The last case prevents semantic decoding where required, not otherwise-lawful access to integrity-checked raw evidence. Missing mandatory semantic evidence is not repaired by constructing a new Package from current defaults. No new public HTTP operation is introduced.

Intended destination: agent/context.md historical Package reads and foundation/storage.md integrity/availability. Actual writeback: this register only.

<a id="cg06-q200"></a>
### CG06-Q200 — Bound serialized Package size before initial publication

Status: ACCEPTED. Require a finite controlled serialized-Package byte bound checked before initial publication. Exceeding it returns a typed rejection without truncation or a partially created Run.

This technical persistence/admission limit is separate from Skill business-input bounds and Frame/model capacity. No universal business-size constant or new Run resource wallet is created.

Intended destination: agent/context.md Package technical protection and agent/execution-runtime.md initial admission. Actual writeback: this register only.

## Round 20 persistence and local review

- Q191–Q200 are accepted with Q191/Q195/Q198 amendments. Pre-PREPARED candidates have no durable or sending authority; PREPARED creation arbitrates serial occupancy. Complete Tool reply coverage is scoped to current DeepSeek Chat Completions. Provider-visible schema is a controlled projection, with Runtime retaining full admission authority.
- Decision-to-Document Traceability: every decision identifies prospective owners and register-only writeback. All three displaced interpretations remain explicit. Prior CG06-R5 remains a historical research checkpoint; accepted support choices do not invent undocumented Provider guarantees.
- Cross-Document Semantic Consistency: checked Architecture 9.1/9.2/10.1–10.2, EXR-012/013/019/032 and Q4/Q15/Q48/Q56/Q59/Q63/Q69/Q134/Q179/Q180/Q188. Local preparation cannot mint dispatch permission or recovery evidence; Tool projection cannot relax action semantics; historical reads and new model reuse remain distinct. No new Tool scheduling owner, shared Provider invariant or prompt snapshot is introduced.
- Only this register was edited. No implementation, live call, migration or normative publication occurred; M2 consumed scope remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q200 anchors/headings and register-only writeback, ten unanswered Q201–Q210 frontier rows, forty-five supersession sections, all three amendment checks, the scoped Beta research caveat, all five local file/anchor references, whitespace and conflict markers. The scoped git diff --check passed. These checks establish document integrity, not Runtime/adapter execution proof.

<a id="cg06-r6"></a>
## CG06-R6 — Schema expressiveness facts do not enable Beta strict mode

A bounded read-only check on 2026-09-23 successfully retrieved the official [DeepSeek Tool Calls guide](https://api-docs.deepseek.com/guides/tool_calls/). The strict-mode schema section explicitly lists array minItems/maxItems and string minLength/maxLength as unsupported. It labels strict mode Beta, requires the official /beta endpoint and strict: true on each function, and describes server rejection for unsupported/nonconforming schemas. The standard example uses the ordinary official endpoint without strict mode.

These unsupported-keyword statements describe strict-mode validation, not a guarantee of standard-endpoint enforcement. Q198's projection/admission separation does not select Beta strict mode or silently alter the target endpoint. No live request or SDK/transport implementation was executed. Selecting the actual M2 Tool-schema support profile remained a distinct choice at this research checkpoint. Subsequent resolution: Q207 selects the ordinary official endpoint without Beta strict mode for first production M2 Tool integration.

## Round 21 — Per-Invocation preparation and independent historical confirmation

The user accepted Q201–Q210 with amendments to Q201/Q209. Every destination below is prospective; actual writeback is this register only. M1 per-Invocation ownership and historical-read versus fresh-admission boundaries remain intact.

<a id="cg06-q201"></a>
### CG06-Q201 — Derive and freeze response rules per Invocation purpose

Status: ACCEPTED with user amendment. The M2 semantic consumer deterministically derives each MODEL Invocation's response_format_key and max_response_bytes from the Run's frozen Skill/execution binding together with that Invocation's controlled purpose/call role. Freeze the resulting values when creating its M1 PREPARED record. The semantic caller cannot supply arbitrary overrides outside that protocol.

Different legitimate call roles, such as a primary call and validation-guided repair, may derive different formats or limits. Do not create Run.response_format_key or imply that every MODEL Invocation of a Run uses one fixed pair. M1's underlying preparation interface remains valid for other consumers. The protocol determines allowed purposes; this decision alone adds no universal purpose enum or generic call-role lifecycle.

SUPERSEDED overly broad interpretation: deriving from a Run binding implies a single response format/size pair for the entire Run. Derivation is controlled and per Invocation; its frozen PREPARED values remain authoritative for that Invocation.

Intended destination: agent/execution-runtime.md semantic MODEL preparation and Skill call-role binding. Actual writeback: this register only.

<a id="cg06-q202"></a>
### CG06-Q202 — Rebuild a candidate for the same safely recoverable PREPARED Invocation

Status: ACCEPTED. When M1 proves PREPARED with no committed intent and grants fresh lawful recovery qualification, the semantic consumer may locally rebuild its candidate for the same Invocation from the frozen task/configuration basis. Preserve the Invocation's already frozen response format and size limit; recheck current input eligibility, capacity and resources before proceeding.

Missing necessary historical interpretation is explicit unavailability, not permission to substitute current defaults. Do not allocate a second Invocation to escape the first one's serial position. The reconstructed candidate remains local preparation until lawful Q69 publication; an uncertain intent acknowledgement is not proof of absence.

Intended destination: agent/execution-runtime.md semantic preparation recovery and agent/context.md candidate reconstruction. Actual writeback: this register only.

<a id="cg06-q203"></a>
### CG06-Q203 — Confirm the complete semantic admission publication

Status: ACCEPTED. Reconcile Q69 uncertain commit by verifying the original atomic intent/dispatch generation, descriptor, actual Frame association/integrity and applicable reservation/counter publication associations together. Intent existence alone does not prove the complete M2 admission bundle.

Confirm committed facts without reserving again. Account for legitimate subsequent ledger evolution rather than requiring mutable counters to remain at their original values. Missing mandatory associations or conflicting publication facts are integrity/publication failures, not permission to synthesize funds, replace the Frame or rerun admission as a substitute publication. Sending remains separately subject to M1's original live winner, no prior adapter entry and current qualification/admission requirements.

Intended destination: agent/execution-runtime.md semantic intent reconciliation, agent/context.md Frame association, foundation/budget.md accounting association and foundation/storage.md atomic integrity. Actual writeback: this register only.

<a id="cg06-q204"></a>
### CG06-Q204 — Frame absence follows the semantic publication boundary

Status: ACCEPTED. For a semantic MODEL Invocation, proven PREPARED without committed intent means its Frame is not yet published. A committed intent makes the associated Frame mandatory; confirmed missing payload, corrupt bytes or inconsistent binding is an integrity failure. Temporary inability to read remains distinct from proven absence.

Never reconstruct a missing committed Frame from a Package and present it as historical actual input. Nonsemantic M1 Invocations retain their own evidence agreement. A historical read itself performs no repair or Run ending; execution/recovery disposition uses its separately lawful coordination.

Intended destination: agent/context.md Frame read outcomes and foundation/storage.md semantic publication associations. Actual writeback: this register only.

<a id="cg06-q205"></a>
### CG06-Q205 — Initial capability scope is the Run's ceiling

Status: ACCEPTED. The initial Package capability scope bounds later Frame exposure and Tool admission. Current eligibility can narrow or reallow within that ceiling, but later Tool registrations, configuration changes or newly granted permissions cannot expand an existing Run's original scope. A genuinely wider task scope requires a new task.

This does not prohibit already-admitted lazy exact resolution or lawful same-task writes introducing actual committed versions under Architecture 10.1. Protected-input revocation still ends the frozen task; reallowing a capability is not permission to reopen that ended Run.

Intended destination: agent/context.md initial capability ceiling and agent/tools.md effective-action intersection. Actual writeback: this register only.

<a id="cg06-q206"></a>
### CG06-Q206 — Distinguish disabled, calculable and blocked Budget components

Status: ACCEPTED. Budget reads distinguish a disabled resource dimension, an enabled dimension with reliably calculable availability (including a true zero), and an enabled dimension whose accounting obstruction prevents safe availability calculation.

Do not encode the last case as numeric zero or overload null to mean both disabled and blocked. Retain the known allocation/accounting facts and unresolved exposure for each applicable dimension. This is a typed read projection, not a new aggregate or generic accounting lifecycle.

Intended destination: foundation/budget.md complete resource read components and accounting-obstruction presentation. Actual writeback: this register only.

<a id="cg06-q207"></a>
### CG06-Q207 — Ordinary official endpoint without Beta strict mode in M2

Status: ACCEPTED. First production M2 Tool integration uses the ordinary official DeepSeek Chat Completions endpoint without Beta strict mode. Apply the controlled Provider-visible projection and complete Runtime authoritative validator.

Do not silently switch endpoint, enable strict mode or fall back after schema rejection. A future explicit strict-mode consumer requires a reviewed supported profile. CG06-R6's Beta-only schema facts do not imply standard-endpoint enforcement guarantees or authorize weakening the owned action protocol.

Intended destination: DeepSeekAdapter supported configuration and M2 implementation/handoff scope. Actual writeback: this register only.

<a id="cg06-q208"></a>
### CG06-Q208 — Estimates do not close unknown token or CNY exposure

Status: ACCEPTED. Controlled local estimates can inform reservation/capacity and explanatory evidence but cannot finalize unknown token/CNY consumption or release the corresponding unresolved reservation in M2. Admitted trustworthy usage or independently proven safe no-send release is required to close the applicable exposure.

Do not present estimated settlement as measured usage. This narrows Q76's formerly open estimate-release possibility without erasing separately labeled estimates or other dimensions' independently lawful settlement.

Intended destination: foundation/budget.md settlement eligibility and unresolved exposure. Actual writeback: this register only.

<a id="cg06-q209"></a>
### CG06-Q209 — Historical start confirmation precedes all fresh execution admission

Status: ACCEPTED with user amendment. The internal semantic-start outcome vocabulary distinguishes success returning only run_id, definite fresh-admission rejection, START_REQUEST_CONFLICT, required historical interpretation unavailable, storage read/integrity failure, and unconfirmed initial commit. These operation outcomes introduce no durable attempt lifecycle and do not automatically end a Run as FAILED.

First perform basic request-envelope/start_request_id structural checks and verify the caller's eligibility to read the historical start result. Look up the successful association. If present, interpret the original request under that association's retained fingerprint_format_key: an equal original request returns its original run_id; a different request yields START_REQUEST_CONFLICT. Required original interpretation must be available, but current execution eligibility is irrelevant to this confirmation branch.

Only proven absence enters current source, permission, Skill, Budget and other fresh-create admission before atomic creation. Historical confirmation cannot require that exact sources remain usable for new execution, the Skill remain enabled, current permission permit creation, or current Budget remain sufficient. Read uncertainty and bounded arbitration must not be treated as absence; initial commit uncertainty is not known rejection or proof of no Run.

SUPERSEDED ambiguous precheck scope: "necessary input/read checks" could include current business/source/Skill/Budget admission before historical lookup. Only basic structure, original-protocol interpretation and historical result-read eligibility can constrain historical confirmation; fresh execution admission remains in the absent-association branch.

Intended destination: agent/execution-runtime.md complete semantic-start outcomes/precedence and foundation/storage.md historical association interpretation. Actual writeback: this register only.

<a id="cg06-q210"></a>
### CG06-Q210 — Trusted usage may settle without a durable terminal response

Status: ACCEPTED. Independently admitted trustworthy usage may be persisted and settle applicable accounting without a durably published terminal response, provided its exact Invocation/dispatch association and metering validity are established. Deadline/owner fencing of first response publication, response storage failure or a complete oversized response cannot erase separately reliable usage facts.

This gives no late response/business publication authority, fabricates no durable response and cannot trigger another Provider request to discover cost. Do not infer final usage from arbitrary partial fragments or complete protocol termination from usage alone. Evidence-insufficient components retain their unresolved exposure. Independent accounting storage can also fail and must not be reported as committed settlement until confirmed.

Intended destination: foundation/budget.md independent usage admission/settlement and agent/execution-runtime.md adapter evidence handoff. Actual writeback: this register only.

## Round 21 persistence and local review

- Q201–Q210 are accepted with Q201/Q209 amendments. Response rules derive per Invocation role and freeze in PREPARED; no Run-wide response-format field is added. Historical start confirmation uses original comparison rules and historical read eligibility without fresh execution admission.
- Decision-to-Document Traceability: all ten decisions identify prospective owners and register-only writeback. Both displaced interpretations remain explicit. Q10/Q76 and CG06-R6 receive focused subsequent-resolution notes without erasing the earlier open frontier/research state.
- Cross-Document Semantic Consistency: checked EXR-004/012–015/019, Architecture 9.1/10.1/11–12 and Q24/Q34/Q47/Q69/Q70/Q73/Q115/Q180/Q191/Q198. Recovery preserves per-Invocation identity and immutable preparation fields; atomic-bundle confirmation does not grant sending authority; accounting truth and response publication remain independent. No new capability expansion, historical execution gate or estimated final settlement is introduced.
- Only this register was edited. No implementation, live call, migration or normative publication occurred; M2 consumed scope remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q210 anchors/headings and register-only writeback, five unanswered Q211–Q215 closure-frontier rows, forty-seven supersession sections, explicit Q201/Q209 amendment checks, all five local file/anchor references, whitespace and conflict markers. The scoped git diff --check passed. These are document-integrity checks, not consumer/SDK execution proof.

## Round 22 — Consumer-owned repair boundaries and a conformance-only exercise

The user accepted Q211–Q215 with amendments to Q212/Q215. Every destination below is prospective; actual writeback is this register only. Acceptance does not authorize normative publication or implementation.

<a id="cg06-q211"></a>
### CG06-Q211 — Recover the controlled Invocation purpose without guessing

Status: ACCEPTED. The static Skill workflow selects an allowed finite semantic step/purpose before preparation. By PREPARED, preserve or unambiguously derive that binding from durable owned evidence so recovery selects the same controlled instruction/parameter/response and semantic-limit rules.

Neither an arbitrary caller override nor model self-labeling may turn work into a privileged purpose such as repair. Do not infer the historical binding from a current workflow position. This requires no universal purpose enum or independent Step aggregate. Q212 separately limits M2's repair definition; recoverable purpose does not imply a generic repair record schema.

Intended destination: agent/execution-runtime.md Skill purpose/preparation recovery and actual consumer evidence agreement. Actual writeback: this register only.

<a id="cg06-q212"></a>
### CG06-Q212 — M2 freezes repair admission boundaries, not a repair protocol shape

Status: ACCEPTED with user amendment. A repair MODEL Invocation must be authorized by a deterministic validation failure explicitly defined by a real consumer. It cannot originate from transport failure, OUTCOME_UNKNOWN or a Provider retry suggestion. It is a new MODEL Invocation subject to fresh Budget, deadline and execution admission; it cannot reuse the original Invocation's dispatch permission.

M2 has no real semantic validator/repair consumer. RequirementParse first consumes this in M3 and Fits later. Those consumers own the concrete repairable failure set and whether/how to retain source_invocation_id, validator_key, finding/reference and repair-purpose binding. Do not freeze a complete source-response/validator/finding binding shape now or create a Generic Validation/Repair protocol. Q211's general recovery obligation remains without specifying these future fields.

SUPERSEDED proposed detail: requiring in M2 a complete durable-response plus exact-validator/protocol repair binding, even with recomputable diagnostics. The general causality/admission restrictions remain; complete repair input/evidence representation is deferred to the first real consumer.

Intended destination: agent/execution-runtime.md repair boundary and explicit M3/first-consumer deferral. Actual writeback: this register only.

<a id="cg06-q213"></a>
### CG06-Q213 — Explicit Harness observations own countable invocation projections

Status: ACCEPTED. In the first integration, explicit Harness observations derived from canonical Invocation/Budget evidence own countable invocation identity, usage and cost projections. LangGraph callbacks describe workflow mechanics and correlate with those identities; wrapping a MODEL Invocation in a graph node cannot count another model call or charge.

Later settlement updates the corresponding derived observation rather than creating another execution. Unknown usage retains its uncertainty. SDK-specific observation identifiers, update/deduplication and callback controls require selected-source verification. This is an integration responsibility allocation, not a generic Telemetry Port or new accounting authority.

PARTIALLY SUPERSEDED by Q216: the sentence requiring later settlement to update the corresponding observation must not require mutation of an ended SDK span or keeping it open until settlement. Q216 permits an admitted correlated non-generation accounting event. The original Invocation association, no duplicate MODEL count, uncertainty and canonical Budget ownership remain effective. CG06-R8 supplies the research reason for this narrowing.

Intended destination: evaluation/evaluation-observability.md canonical correlation/no duplicate accounting and M2 integration handoff. Actual writeback: this register only.

<a id="cg06-q214"></a>
### CG06-Q214 — First telemetry export is bounded best-effort

Status: ACCEPTED. First M2 optional telemetry export is bounded best-effort. Lost or unconfirmed delivery is possible; do not add a durable export outbox, worker lifecycle or exactly-once promise. Required local evidence is independently retained.

Export buffering/backpressure/shutdown failures cannot block authority transactions, reexecute MODEL/Tool work or turn an otherwise valid task into failure. Selected SDK retry/flush/buffering/masking behavior must be verified and bounded before use. This selects an initial delivery guarantee without converting remote telemetry into Runtime durability or promising future delivery after process loss.

Intended destination: evaluation/evaluation-observability.md export failure boundary and M2 implementation/handoff delivery scope. Actual writeback: this register only.

<a id="cg06-q215"></a>
### CG06-Q215 — Conformance-only Skill exercises the production semantic path

Status: ACCEPTED with user amendment. Define a minimal statically registered M2 conformance/exercise Skill using production semantic-start, Runtime, Context, Budget, Gateway, DeepSeekAdapter and ToolInvocationRuntime. Its consumer_key and recovery agreement serve only the exercise, not a new long-lived Runtime business capability or product Skill catalog entry. It is not a replacement test Agent.

The exercise uses bounded admitted literal input and one explicitly authorized exact historical MODEL response. Its initial protected source-body read follows Q45 and is retained in actual Frame evidence. Its finite MODEL -> TOOL -> MODEL protocol admits at most two MODEL calls and one controlled.response-read.v1 action. The existing action retains its digest/byte-length result meaning; it is not broadened to body retrieval, semantic parsing, Ensure or remote access. Deterministic validation of canonical exercise evidence defines whole-Run completion; abnormal termination or failed validation cannot masquerade as completion. Repair and multi-Tool scheduling are not enabled implicitly.

Keep two associations distinct: the producing MODEL Invocation belongs to the current exercise Run and produces the Tool request; the read target is the preauthorized exact historical response, which may belong to a fixture source Run. The initial Package grants only that exact target's read scope. A different invocation_id supplied by the model must be rejected; this action cannot become an arbitrary response browser. Historical readability alone does not grant model reuse permission.

The exercise proves Context provenance, model-origin Tool selection/admission, exact local read, returned-content admission, next-Frame inclusion and durable evidence/recovery through real components. A digest-only result does not itself prove source-body inclusion. Preserve the existing M1 action/consumer keys and meanings; reuse compatible action logic under the exercise's own serial/completion/recovery binding.

SUPERSEDED scope interpretation: a new permanent infrastructure business Skill/capability, or promotion of the exercise's two-MODEL/one-Tool pattern, response source or digest/length output to all semantic Skills. These are conformance protocol choices only; production consumers define their own task semantics.

Intended destination: evaluation/evaluation-observability.md real-path conformance exercise, actual consumed Runtime/Context/Tool interfaces and M2 implementation handoff; not the product Skill catalog. Actual writeback: this register only.

## Round 22 persistence and local review

- Q211–Q215 are accepted with Q212/Q215 amendments. Repair retains only cross-consumer admission/causality boundaries in M2; its complete binding and repairable findings belong to the first real semantic consumer. The selected exercise is conformance-only and cannot browse arbitrary historical responses.
- Decision-to-Document Traceability: all five decisions identify prospective owners and register-only writeback. Both displaced interpretations remain explicit. Purpose recovery remains meaningful without prescribing a future repair schema; the exercise's source target is distinct from its same-Run producing MODEL request.
- Cross-Document Semantic Consistency: checked Architecture 9/11/12/15, EXR-001/002/011/014/015, Q1/Q45/Q56/Q59/Q149/Q154/Q177/Q194/Q195/Q201/Q205/Q211 and the actual controlled local-read implementation. No product Skill, generic repair protocol, duplicate budget authority or transferable dispatch permission is introduced. Existing controlled M1 consumer completion/concurrency is not silently reused as M2 semantics.
- Only this register was edited. Concurrent frontend/API/plan/Progress changes were observed and preserved. No implementation, live call, migration or normative publication occurred; M2 consumed scope remains Pending.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q215 anchors/headings and register-only writeback, one unanswered Q216 frontier row, forty-nine supersession sections, Q212/Q215 amendment checks and Q213's explicitly pending clarification, the scoped research identities/limitations, all five local file/anchor references, whitespace and conflict markers. The scoped git diff --check passed. These checks establish document integrity, not SDK/runtime conformance or normative readiness.

<a id="cg06-r7"></a>
## CG06-R7 — Bounded LangGraph source review for the conformance path

Read-only research on 2026-09-24 inspected Python [LangGraph 1.2.12](https://github.com/langchain-ai/langgraph/releases/tag/1.2.12), release short commit 49cce0c, and its [tagged MIT license](https://raw.githubusercontent.com/langchain-ai/langgraph/1.2.12/LICENSE). This is a research candidate, not a selected/installed JobHunter dependency. Current project manifest/lock inspection found no LangGraph integration.

The [tagged StateGraph source](https://raw.githubusercontent.com/langchain-ai/langgraph/1.2.12/libs/langgraph/langgraph/graph/state.py) supports ordinary callable nodes, compiled execution and optional persistence. checkpointer=False explicitly prevents parent checkpoint inheritance; None can inherit one. No prebuilt Agent or Provider wrapper is required. The [retry runner](https://github.com/langchain-ai/langgraph/blob/1.2.12/libs/langgraph/langgraph/pregel/_retry.py) propagates failure with no applicable retry policy; configuring a policy can rerun a node. The [types source](https://raw.githubusercontent.com/langchain-ai/langgraph/1.2.12/libs/langgraph/langgraph/types.py) gives RetryPolicy three total attempts by default when such a policy is selected. This is distinct from selecting no policy.

[Checkpoint documentation](https://docs.langchain.com/oss/python/langgraph/checkpointers) describes retained graph state and replay of nodes after the selected checkpoint, including external calls. Such state is not atomically committed with JobHunter admission and grants no remote replay permission. Tagged TracePolicy explicitly covers only a node's own trace, not root/child traces; stream modes can expose state, inputs, results and errors. Node-only filtering does not establish Q149's export safety.

Implementation implications under already accepted decisions: use a small static graph over production Harness calls; control all retries/fallbacks and tracing paths; retain Runtime ownership of dispatch/recovery/cancellation. Omitting framework checkpoint storage for the conformance consumer is a possible minimal realization when its continuation is reconstructed from canonical evidence, not a new universal Contract prohibition. Exact callback dispatch internals were not fully retrieved; no dependency installation, full transitive audit or runtime/cancellation test was executed.

<a id="cg06-r8"></a>
## CG06-R8 — Langfuse export limitations and one remaining late-accounting choice

Read-only research on 2026-09-24 inspected Python SDK [v4.15.4](https://github.com/langfuse/langfuse-python/releases/tag/v4.15.4), release short commit 6c3842a. Its [tagged manifest](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/pyproject.toml) declares MIT and Python >=3.10; the separate SDK LICENSE body was not retrieved. The server [v4.42.0 license](https://raw.githubusercontent.com/langfuse/langfuse/v4.42.0/LICENSE) distinguishes enterprise directories from MIT-covered code and third-party licenses. These are research identities only, not selected SDK/server deployments; SDK metadata does not establish all self-hosted feature licenses.

The [observation source](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/_client/span.py) returns without applying ordinary update() when the underlying OTel span is no longer recording. The [client source](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/_client/client.py) supports a correlated create_event primitive. A safe supported same-ID post-end update through legacy ingestion was not established. Q213 must not be implemented by assuming that its ordinary SDK update mutates ended observations. This was the remaining scope choice at the research checkpoint; the subsequently accepted Q216 permits a correlated non-generation accounting event.

Official [cost documentation](https://langfuse.com/docs/observability/features/token-and-cost-tracking) defines built-in cost_details in USD and allows model-based inference when costs are omitted; the inspected SDK uses float values. Existing CNY/exact-decimal/no-FX decisions already prohibit exporting a CNY amount as one of these USD values or treating inferred cost as Budget truth. An allowlisted exact CNY value with explicit currency and certainty can be represented in metadata; native inferred pricing and countable observations still require a reviewed mapping. No new currency policy is proposed.

The [stock callback](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/langchain/CallbackHandler.py) handles raw chain/model/Tool inputs and outputs, exception text and generation observations; error paths may supply zero cost. Unmodified attachment does not satisfy Q149/Q213. [Masking documentation](https://langfuse.com/docs/observability/features/masking) and the [exporter source](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/_client/span_exporter.py) place export-stage masking after media handling. Therefore the accepted allowlist must apply before raw data enters SDK mechanisms that may process or export it; a late mask alone cannot establish privacy.

The [span processor](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/_client/span_processor.py) delegates span buffering/export to OTel. The [resource manager](https://raw.githubusercontent.com/langfuse/langfuse-python/v4.15.4/langfuse/_client/resource_manager.py) can drop queued data under pressure, joins queues/threads in flush/shutdown and registers shutdown at atexit; the inspected path has no enclosing overall timeout. Exact OTLP retry/timeout behavior depends on resolved transitive dependencies, which are not selected/locked in this project. Stock defaults are not proof of Q214's bounded behavior.

These callback, currency and shutdown findings are implementation-adoption gates under accepted requirements, not exceptions to them or evidence that Runtime authority must change. No deployment, API request, exported sample, failure experiment or dependency installation was performed. Late-accounting representation was the focused decision resulting from this research and is resolved by Q216; no generic custom Telemetry Port or durable outbox is inferred.

## Closure checkpoint — after Q215

At this checkpoint all questions through Q215 were accepted and scoped integration research identified the Q213/SDK interpretation seam. Subsequent resolution: Q216 below is accepted, leaving no currently identified unanswered policy question. Normative representation review and implementation-adoption proof remain distinct from accepted policy.

The existing controlled.response-read.v1 source implements exact response digest/length evidence. Its M1 read consumer treats Tool completion as whole-Run completion; its M1 model consumer expects two MODEL responses with concurrency up to two. The current read recovery entry is coupled to ControlledConsumer. These source facts justify an exercise-specific binding and careful implementation reuse, not a claim that M2 is already implemented. No current source inspection was treated as a rerun of its tests.

Remaining consolidation is limited to accepted scope: exact first-exercise input/result/whole-Run recovery interfaces; Package/Frame/adapter deterministic representations; executable controlled model/capacity/price configuration; and selected LangGraph/Langfuse source/license/callback/export compatibility. Representation-only details may be authored under the handoff's closure procedure, but a newly discovered policy conflict requires an explicit question. Full repair protocol design, M3 semantics and permanent infrastructure product capabilities remain excluded.

Normative publication and owner writeback still require the handoff section 8 authorization. Until then, this register is the only write destination. No Contract readiness or milestone completion follows from accepting the interview decisions.

## Focused closure — Late accounting remains associated with the original Invocation

The user accepted Q216 without amendment. The destination below is prospective; actual writeback is this register only.

<a id="cg06-q216"></a>
### CG06-Q216 — Correlated late accounting without ended-span mutation

Status: ACCEPTED. Late accounting evidence must retain its association with the original invocation_id, must not count as another MODEL execution and must not change the original execution outcome or timing facts.

The first Langfuse integration may append an admitted, allowlisted, correlated non-generation accounting event when the execution observation has ended. It need not mutate an ended SDK span or keep that span open while waiting for settlement. Event/API representation remains implementation-owned; no new ledger, model request or durable telemetry lifecycle is introduced.

Preserve CNY exactness and accounting uncertainty under their existing agreements. Earlier Trial evidence remains immutable. Q214's bounded best-effort export still permits lost/unconfirmed delivery; a local accounting fact does not imply successful remote export. This narrows only Q213's observation-update wording and leaves canonical Runtime/Budget authority and no-duplicate invocation accounting intact.

Intended destination: evaluation/evaluation-observability.md late-accounting correlation and M2 integration handoff. Actual writeback: this register only.

## Focused closure persistence and local review

- Q216 is accepted. Q213 explicitly preserves its displaced update wording as PARTIALLY SUPERSEDED; CG06-R8 and the after-Q215 checkpoint point to the actual resolution.
- Decision-to-Document Traceability: Q216 identifies its prospective owner and register-only writeback. No SDK-specific event shape or version becomes a normative requirement merely from research.
- Cross-Document Semantic Consistency: checked Q70/Q111/Q149/Q150/Q159/Q210/Q213/Q214 and Architecture 15.4–15.5. Accounting evidence can arrive after execution, while earlier execution/Trial facts remain unchanged. Correlation adds neither dispatch permission nor another counted model request; telemetry remains optional and derived.
- Only this register was edited. All unrelated work remains preserved. No normative Contract, Progress record, implementation, dependency, deployment or live model call was changed/executed by this focused closure.
- Focused mechanical verification: an in-memory Python check passed unique Q1–Q216 anchors/headings and register-only writeback, the empty question frontier, fifty supersession sections, explicit Q213/Q216 consistency and pending-publication authorization checks, all five local file/anchor references, whitespace and conflict markers. The scoped git diff --check passed. This is local document verification; full normative mapping/review and execution proof have not been performed by this closure checkpoint.

## Publication proposal checkpoint — after Q216

At this proposal checkpoint the question frontier was empty after Q216: all 216 presented decisions were accepted with their effective amendments. The later authorized review below records the newly discovered Q217–Q219 frontier. This closes the interview frontier, not normative publication, full Contract completeness review or M2 implementation. If consolidation finds a genuinely missing policy, permission or failure meaning, ask a focused question before publishing that affected scope rather than guessing.

The following is a concrete proposed closure write set for authorization under the session handoff section 8. At proposal time it was an authoring/review plan, not authorization already granted or a second Contract body. The subsequent authorization is recorded below.

| Existing or planned owner | Accepted scope to publish/reconcile |
| --- | --- |
| docs/contracts/agent/execution-runtime.md | Extend preserved M1 with semantic-start idempotency/precedence, static Skill/purpose binding, serial semantic admission, real Gateway/DeepSeek protocol boundaries and joined Frame/Budget publication/recovery; retain M1 identities and dispatch rules. |
| docs/contracts/agent/context.md (new consumed body) | Initial Package versus per-Invocation Frame, deterministic exact bytes/provenance, protected exact sources, capability ceilings, current-use admission, headless capacity and historical read/retention interfaces. No interactive compaction/Memory protocol. |
| docs/contracts/agent/tools.md (new consumed body) | Static typed action registry, controlled schema projection, authoritative admission, model-origin association, exact-target conformance read, action completion versus result admission and action-specific recovery. No future business Tool catalog. |
| docs/contracts/foundation/budget.md (new consumed body) | Foreground owner identity/allocation, finite Run call/token/deadline ceilings, CNY-only optional money, checked arithmetic, atomic reservations, trustworthy settlement, unknown exposure, historical confirmation and typed reads. No per-Run money wallet or speculative Tool-count budget. |
| docs/contracts/foundation/storage.md; common.md only where genuinely shared | Actual semantic evidence/association atomicity, retained bytes/integrity and required source/recovery availability; reuse existing scalar/fingerprint conventions and avoid duplicate authority or generic lifecycle expansion. |
| docs/contracts/evaluation/evaluation-observability.md | Preserve M1 evidence clauses and add isolated real-path conformance, reproducible fixtures/retained Trial evidence, independent evaluators when consumed, allowlisted derived observations, best-effort export and Q216 late-accounting correlation. No generic quality Judge or permanent infrastructure product Skill. |
| Contract navigation/structure; Architecture; Acceptance and Eval acceptance; owning SL-03 plan | Reconcile only the approved consumed scope and required proof. Product/global plan changes only if an actual owned discrepancy requires them; no routine unrelated rewrite. |
| This register; Progress/traceability; docs/development/handoff/sl-03-m2-handoff.md | Map all effective decisions to actual normative clauses or explicit future boundaries, preserve supersession, record actual scoped review/checks and create the concrete development transfer. Separate documentary readiness from implementation, source research and executed proof. |

Closure review must cover both Decision-to-Document Traceability and Cross-Document Semantic Consistency, complete first-exercise producer/consumer inputs/results/errors/recovery, deterministic Package/Frame/response representations, compatibility with M1 and exact remaining SDK/model-configuration gates. Run the maintained Contract link/requirement checker and scoped whitespace/anchor checks after publication changes; retain the checker. Do not promote a scope with unresolved necessary semantics to Ready.

Selected model/capacity/pricing configuration and resolved SDK versions/callback/shutdown/export behavior remain explicit executable-integration prerequisites. CG06-R1–R8 contain research, not installed/deployed capability or passing wire/SDK tests. Their limitations must carry into the handoff. The future M3 repair protocol and business semantics remain deferred.

Authorization status: GRANTED by the user's subsequent “同意授权” for the normative owner writeback/publication stage above. Implementation, dependency installation, live calls, deployment, commit and push remain outside this instruction. The prior pending-authorization statements describe their historical checkpoints.

## Entry verification and actual writeback

- Decision-to-Document Traceability: this entry records only the explicitly authorized workflow and verified facts. No numbered recommendation, implementation choice or normative requirement is recorded as accepted.
- Cross-Document Semantic Consistency: inspected the owning SL-03 boundaries, effective M1 clauses, Architecture/Acceptance and current code/evidence distinction. Historical schema-4/no-Runtime observations are not used as current source facts. Planned Context/Tools/Budget and semantic Eval remain Pending.
- Actual write set: this register, its design-navigation entry and factual start/current-source notes in existing Progress records. No Contract body or historical handoff was changed.
- Mechanical checks: python3 scripts/check_contract_links.py passed (300 unique requirements; 2778 resolved local links/anchors; 135 CG04 / 130 CG05 mappings; unchanged 30 Ready / 63 Pending / 93 scopes). git diff --check passed; an additional in-memory check passed new-register whitespace/conflict-marker checks and unique Q1–Q10 topic locators. These are documentation checks, not Runtime acceptance.

<a id="cg06-pub"></a>
## Authorized owner publication — closure review

The user explicitly authorized the proposed write set with “同意授权”. Parent authoring and bounded read-only interface reviews started from HEAD 2c5c69687ea7d43ddb79b5c89828bf54c159440b. Existing frontend/API/SL-02/Progress edits remain separate and preserved. M1 implementation is now recorded as verified; the earlier entry checkpoint remains historical, not current readiness.

Representation-only arrangements under handoff section 8: reuse COM-045 for the closed Package/Frame typed bytes; use a separately fixed-field-order DeepSeek terminal JSON format; define exact provenance tags/keys, the first read action's schema/result projection, and DeepSeekUsage:v1's admitted components. These express accepted inputs, identity, precision and evidence separation; they add no permission, retry or business completion rule. Concrete configuration/rule keys must retain their exact historical meaning. Source research is not an executed integration test.

Review corrected fixture isolation to permit admitted fixture task/source inputs, retained separate evaluator resource evidence, mapped new model-visible source_sha256/source_byte_length to preserved LocalRead result_sha256/result_byte_length, and closed nested format shapes. The concrete conformance completion and postdeadline agreement cannot be inferred from M1's different controlled consumers; the following policy questions were asked rather than filled as representation details. Their subsequent accepted amendments are recorded in place below; the pre-answer verification checkpoint remains historical.

<a id="cg06-q217"></a>
### CG06-Q217 — Conformance completion predicate

Status: ACCEPTED with the user's scope amendment. First MODEL must propose exactly one lawful exact-target Tool request, the TOOL must lawfully complete, and the second MODEL must terminate with stop and strict JSON containing exactly source_sha256/source_byte_length matching the real admitted Tool result. All are required for this infrastructure exercise's success; no automatic repair.

This defines exercise/Trial semantic success only. A real DeepSeek refusal to select the Tool, invalid JSON or result mismatch is retained semantic failure evidence, not proof that Runtime/Context/Budget/Gateway violated their Contracts. Infrastructure acceptance independently requires deterministic proof of admission, fencing, accounting and recovery. The exercise demonstrates one successful real composition path, not a stable product model-quality promise.

PARTIALLY SUPERSEDED interpretation: treating this strict output as a generic M2 semantic quality gate. The original exercise predicate remains; only the implied scope of its acceptance claim is excluded.

Actual destinations: EVO-022–023/026, CTX-003 and Acceptance 9.4.

<a id="cg06-q218"></a>
### CG06-Q218 — Exercise-specific denial mapping

Status: ACCEPTED with owner-preserving failure semantics. For an already accepted exercise Run, an established deterministic rejection that prevents continuation and has no other lawful completion branch is coordinated by the consumer to FAILED. Preserve each owner's stable reason: Runtime/Harness faults remain Runtime-owned; Budget insufficiency is first a Budget rejection; consumer output validation retains consumer-defined meaning. No universal semantic-rejection code or promotion of every consumer validation error into Runtime failure taxonomy is introduced.

Cancellation, timeout, unknown remote outcomes, response failures and Storage uncertainty/integrity retain their established distinctions. Initial admission rejection still creates no Run. Exercise ending requires lawful execution/coordination authority; a read error alone cannot claim a committed FAILED state.

PARTIALLY SUPERSEDED proposal interpretation: one undifferentiated Runtime failure taxonomy for all post-start rejections. FAILED remains the accepted exercise end_reason, with a scoped M2 owner-preserving reason bridge; M1 consumer rules remain unchanged.

Actual destinations: EXR-057, EVO-024 and Acceptance 9.4.

<a id="cg06-q219"></a>
### CG06-Q219 — Exercise postdeadline local recovery

Status: ACCEPTED with consumer-binding and expiry amendments. local_recovery_grace_ms is frozen in this exercise's consumer binding, not a new AgentRun field or a second deadline. Zero disables postdeadline recovery; a positive finite value permits a nonrenewing window [deadline_at, deadline_at + local_recovery_grace_ms]. Only reads/confirmation of already durable Tool results, reads/validation of lawfully durable MODEL responses and deterministic local consumer reconciliation are allowed under applicable current qualification/admission.

No new MODEL Invocation, TOOL handler execution, Frame, deadline extension or reopening of ENDED is permitted. Expiry means no new local-recovery execution qualification; it does not erase evidence or rewrite completed facts into failure. Existing M1 deadline/fencing/ending predicates still apply; a newly granted window is never anchored to restart.

REJECTED alternative: forbidding every postdeadline local recovery for this consumer. PARTIALLY SUPERSEDED interpretations: a universal Run grace field, a renewable deadline or automatic evidence/fact invalidation at window expiry.

Actual destinations: EVO-022/025/026, EXR-057 and the development handoff.

## Foundation publication verification checkpoint — before Q217–Q219 answer

- Actual owner writeback: EXR-035–056, COM-049, CTX-001–015, TOL-001–014, BUD-001–025, STO-046–053 and EVO-008–021 at 2026-09-24.S3M2-r1; related Architecture, Acceptance/Eval acceptance, Contract navigation, owning/global plan, Progress/mapping and the concrete gated development handoff. No Product behavior change was needed. Ordinary-round register-only statements remain historical checkpoints.
- Decision-to-Document Traceability: PASS for effective Q1–Q216 foundation publication, with 216 individual destination rows in Progress §6.6. CG06-S2 lands in the single-adapter boundary; representation-only choices are identified above. Q217–Q219 remain PENDING and have no published acceptance or implicit policy answer. CTX-003 states conformance representation constraints, not a complete enabled consumer format.
- Cross-Document Semantic Consistency: PASS for the seven scoped foundations after parent and bounded read-only reviews of M1 compatibility, exact representations, metering, evidence/Eval and owning Architecture/Acceptance/plan. The concrete exercise's input/completion/denial/recovery agreement is excluded from Ready; whole M2 closure remains incomplete. Source configuration and selected SDK behavior remain executable-adoption gates.
- Compatibility check compared each complete prior normative body from its first requirement anchor against HEAD: Common, Execution Runtime, Storage and Eval are preserved verbatim; only their introductory navigation/scope text and appended M2 sections changed. Existing M1 IDs, receipts, controlled consumer meaning and historical handoffs were not rewritten.
- Executed checks: `python3 scripts/check_contract_links.py` PASS — 399 unique requirements, 4787 local links/anchors, 135 CG04 / 130 CG05 / 216 CG06 mappings, 37 Ready / 63 Pending / 100 scopes. The seven additional Ready rows are foundation portions; the separately Pending exercise row prevents whole-M2 readiness. `git diff --check` PASS; equivalent whitespace/conflict-marker/anchor-uniqueness checks passed for new untracked publication files.
- Modified checker validation: `UV_CACHE_DIR=/tmp/jobhunter-uv-cache uv run --locked ruff check scripts/check_contract_links.py`, Ruff `format --check` and strict `pyright scripts/check_contract_links.py` PASS (0 errors/warnings). Initial formatting differences were corrected before the final check. Isolated temporary copies passed a baseline and restored baseline; all six negative fixtures were correctly rejected: duplicate requirement ID, missing accepted decision mapping, unmapped new normative clause, nonexistent local anchor, readiness count drift and unapproved pending-question promotion. New ad hoc helpers stayed outside the repository.
- Not executed: backend feature tests, browser acceptance, migration, dependency installation, SDK deployment/export or live DeepSeek calls. Inherited M1 416-test evidence is recorded source history, not a rerun. No commit/push was made. Concurrent frontend/API/SL-02/technology/design-system/Progress work remains preserved.
- Next required user input is only Q217–Q219. Existing publication authorization persists; do not ask again for the same owner writeback. After their answer, persist effective semantics, close the exercise-specific protocol, extend mapping/checker and re-review that affected scope before promoting it to Ready.


## Final closure — Q217–Q219 accepted with amendments

The user's response addresses all three pending questions with clear accepted refinements. It closes the frontier; no additional permission for the already authorized owner writeback was requested. Q217 separates this exercise's strict semantic predicate from infrastructure Contract compliance. Q218 preserves owner-defined rejection reasons while allowing this consumer to coordinate FAILED when no lawful continuation remains. Q219 freezes a consumer-bound finite local-recovery window, with no Run field, renewable deadline, evidence deletion or rewriting of completed facts.

Actual final scope: **2026-09-24.S3M2-r1**, COM-049, EXR-035–057, CTX-001–015, TOL-001–014, BUD-001–025, STO-046–053 and EVO-008–026. There are 105 additions to the preserved 300 requirements. All 219 accepted decisions map to actual clauses or explicit deferred consumer boundaries in Progress §6.6. The eight consumed documentary portions are Ready; implementation/adoption and executed milestone acceptance remain separate. Source research does not certify the selected model/configuration, SDK export or live composition.

Representation-only closure fixes the conformance's instruction/source_invocation_id input, two named MODEL purposes, original-result proof projection, exact static keys and owner-coded terminal finding. These express the accepted two-MODEL/one-exact-read path and owned semantics, not a product Skill, new generic result entity or arbitrary failure API. The consumer input permits empty literal instruction and requires explicit finite configuration bounds; unrelated business inputs remain consumer-owned. EXR-057 explicitly scopes the M2 owner-preserving ending extension to EXR-003/009/011/033 while leaving all prior normative bodies and M1 consumers unchanged.

**Decision-to-Document Traceability: PASS for the consumed M2 scope.** Q217 lands in EVO-022–023/026; Q218 in EVO-024 and EXR-057; Q219 in EVO-022/025/026 and EXR-057. Earlier accepted destinations remain mapped. The pre-answer 399-requirement/37-Ready checkpoint above remains historical; its pending-frontier statements are resolved by these accepted decisions and this closure.

**Cross-Document Semantic Consistency: PASS for the consumed M2 scope.** Parent and bounded read-only review checked failure-owner preservation, lawful current/ownerless ending, completion-before-time-denial, uncommitted verdict versus durable receipt, nonrenewing consumer grace, retained completed facts and first-consumer field/proof closure against M1. The review corrected Tool admission causes that had been overgrouped as consumer failure, and made PERMISSION_DENIED's RUNTIME/Harness permission ownership explicit even when relayed through the Tool wrapper. Architecture, Acceptance/Eval acceptance, SL-03 plan, Contract navigation, Progress and the development handoff now agree on documentary readiness and remaining adoption/implementation proof.

Executed final verification: Contract checker PASS for 405 unique requirements and 135 CG04 / 130 CG05 / 219 CG06 mappings; readiness 38 Ready / 62 Pending / 100 scopes. Modified checker Ruff lint, Ruff format check and strict Pyright PASS (zero errors/warnings). Six isolated negative fixtures correctly reject duplicate IDs, missing accepted mappings, unmapped EXR-057, invalid anchors, readiness count drift and an unaccepted decision included in accepted coverage; restored baseline passes. Complete previous Common/Runtime/Storage/Eval normative bodies remain byte-for-byte present. git diff --check and new-file whitespace/marker/anchor checks pass.

No backend feature suite, browser test, live DeepSeek request, SDK/export deployment, dependency installation or migration was executed. No commit/push was requested or made; unrelated worktree changes remain preserved. The maintained development handoff records actual upstream evidence and remaining executable configuration/SDK integration gates. The Contract Grill/publication is complete; this is not M2 feature implementation or milestone completion.
