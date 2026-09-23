# Execution Runtime Contract — SL-03.M1

> English is authoritative. Normative scope revision: **2026-09-23.S3M1-r1**. This body publishes the internal durability/recovery foundation only. Full protected invocation, production Provider/Tool schemas, Context, Budget and semantic Eval remain later consumed scopes.

[Index](../index.md) · [Decision provenance](../../design/contract/sl-03-m1-grill.md) · [Common](../common.md#com-047) · [Storage](../foundation/storage.md#sto-040) · [Required proof](../evaluation/evaluation-observability.md) · [Readiness](../../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence)

The numbered requirements below define the logical protocol. Internal names denote typed outcomes, not new HTTP statuses or endpoints. Tables inside a requirement are part of that requirement.

<a id="exr-001"></a>
**EXR-001.** **Scope and ownership.** M1 MUST expose internal Application/Runtime interfaces without a public Run HTTP API. AgentRunRuntime owns execution authority; ModelInvocationRuntime owns admitted MODEL dispatch/durability; Gateway adapts transport; ToolInvocationRuntime preserves action-specific admission/recovery. Invocation kinds are exactly `MODEL | TOOL`. Business writes, consumer completion, Save, Materials, platform consent/risk and budget settlement MUST remain with their owners. Deterministic workflows are not required to become AgentRuns. Invocation concurrency is bounded by its consumer, not a universal single slot or an unlimited default. M1 MUST NOT add a Run-level retry command/lineage, generic business-result JSON/reference fields, a late-usage subsystem or production Provider response schema merely to complete this foundation. Controlled adapters and test formats prove this scope; they do not authorize production model calls.

Decision sources: CG05-Q1, CG05-Q2, CG05-Q17, CG05-Q22, CG05-Q24, CG05-Q60, CG05-Q78, CG05-Q90.

<a id="exr-002"></a>
**EXR-002.** **Identity and static keys.** Runtime MUST allocate independent UUIDv4 `run_id` and `invocation_id`; every process startup MUST allocate a fresh UUIDv4 `runtime_instance_id`. An Invocation's owning `run_id` is immutable. Same-Run crash recovery/continuation preserves `run_id`; a future Run-level retry creates a new Run, while Invocation repair/retry is separately consumer-owned. No invocation sequence, response ID or hash identity is introduced. `consumer_key` and `response_format_key` are nonempty, exact case-sensitive registered code keys: no trimming, normalization, fallback or substitution. Incompatible interpretation requires a new key. Duplicate registrations MUST fail before the affected Runtime executes; newly supplied unknown keys are rejected. Historical missing handlers/readers follow EXR-031/032, not a global application startup failure.

Decision sources: CG05-Q3, CG05-Q4, CG05-Q11, CG05-Q18, CG05-Q20, CG05-Q23, CG05-Q79, CG05-Q97, CG05-Q109.

<a id="exr-003"></a>
**EXR-003.** **AgentRun shape.** The minimum logical Run has exactly the following required fields, including explicit nullable values. Future consumed scopes require explicit extensions, not arbitrary properties.

| Field | Type / constraint |
| --- | --- |
| run_id | UUIDv4; immutable |
| consumer_key | Registered exact string; immutable |
| run_status | `OPEN \| ENDED` |
| execution_generation | Exact integer, 0 through 9007199254740991 |
| owner_runtime_instance_id | UUIDv4 or null |
| deadline_at | Common UTC instant or null; EXR-010 |
| created_at | Immutable Common UTC instant |
| ended_at | Common UTC instant or null |
| end_reason | Null or `COMPLETED \| FAILED \| CANCELLED \| TIMED_OUT \| OUTCOME_UNKNOWN` |
| failure_code | Stable Runtime/Invocation-owned code or null |

Initial generation is zero, which never authorizes execution. OPEN requires null end fields; ENDED requires nonnull ended_at/end_reason, null owner, and retains generation. `failure_code` is nonnull exactly for FAILED, otherwise null. ENDED cannot reopen or acquire execution; ending before any grant is legal. Wall-clock rollback may produce ended_at before created_at; do not reject or fabricate/clamp it. Transaction order and generation establish causality. No updated_at, revision, generic schema_version, ownership boolean or grant history is implied. Existing consumer-specific timestamp ordering rules remain scoped to those consumers.

Decision sources: CG05-Q12, CG05-Q13, CG05-Q21, CG05-Q32, CG05-Q41, CG05-Q42, CG05-Q43, CG05-Q52, CG05-Q53, CG05-Q81, CG05-Q119, CG05-Q120.

<a id="exr-004"></a>
**EXR-004.** **Run creation and uncertain creation.** `create_run(consumer_key, deadline_at)` MUST validate its registered consumer and nullable deadline, allocate run_id/created_at in Runtime, and atomically persist an OPEN generation-zero ownerless Run with null ending fields. Success returns run_id; full reads are separate. Preallocated identity MUST remain stable while reconciling an uncertain creation commit. The caller MUST NOT infer rollback from an absent acknowledgement or create another Run/Invocation to bypass uncertainty. Apply the same stable-identity rule to Invocation creation.

Decision sources: CG05-Q84, CG05-Q114.

<a id="exr-005"></a>
**EXR-005.** **Execution qualification.** Execution qualification contains exactly `run_id`, `runtime_instance_id`, `execution_generation`. It is a reference to live durable authority, not an offline bearer permission or a new persisted token ID. Every protected mutation MUST atomically validate the corresponding Run and current authority. Use the existing exclusive physical Workspace-directory owner and a fresh runtime identity; M1 introduces no distributed lease service. Generation counts grants only: first grant is 1; revocation does not increment it. A later generation can process an earlier legally durable response, but cannot inherit an unconsumed send authorization.

Decision sources: CG05-Q5, CG05-Q14, CG05-Q15, CG05-Q16, CG05-Q107.

<a id="exr-006"></a>
**EXR-006.** **Grant.** `grant_execution(run_id, expected_generation)` derives this Runtime instance internally. In one transaction it MUST require OPEN, null owner, exact expected generation, generation below its maximum, and applicable consumer admission, then increment generation once and set owner. Return the resulting qualification. Failed or repeated grants do not increment; matching current owner/generation does not prove another caller won. On uncertain commit, only the original live arbitration winner with proof of its own grant may continue after confirming commitment; reading a matching row alone is insufficient. Bound reconciliation; absent proof, stop instead of manufacturing a winner or adding a receipt subsystem.

Decision sources: CG05-Q85, CG05-Q112.

<a id="exr-007"></a>
**EXR-007.** **Revocation.** `revoke_execution(execution_qualification)` MUST clear owner only when Run is OPEN and every submitted qualification field matches the current authority. It retains generation. A stale or repeated revocation returns not-current and MUST NOT clear a replacement owner. Revocation does not by itself end the Run. Cancellation is the separate Run-wide operation in EXR-008.

Decision sources: CG05-Q5, CG05-Q15, CG05-Q113.

<a id="exr-008"></a>
**EXR-008.** **Atomic ending and cancellation.** A valid end operation MUST atomically arbitrate on OPEN, persist one immutable ending and clear owner; the first valid committed ending wins. Executor-originated ending requires current qualification. A separately authorized Run-wide `cancel_run(run_id)` need not carry the executor's generation; it ends as CANCELLED, and an already-ended Run returns its original ending unchanged. Every Run ending fences all sibling Invocations against new dispatch, first response publication and protected business writes. Request physical interruption when the execution model supports it, but never claim remote cessation/refund from local termination. Do not fabricate terminal responses for remaining Invocations. A response-versus-ending race preserves any response legitimately published first.

Decision sources: CG05-Q34, CG05-Q35, CG05-Q44, CG05-Q63, CG05-Q108, CG05-Q127.

<a id="exr-009"></a>
**EXR-009.** **Completion and ownerless coordination.** COMPLETED requires the consumer's whole-Run completion criteria, not merely one saved result or a universal rule that every Invocation is RESPONSE_DURABLE. A completed negative business assessment can be COMPLETED; business validation failure is not automatically Runtime FAILED. Remote uncertainty uses OUTCOME_UNKNOWN with null failure_code unless another ending already won. When consumer reconciliation proves whole-Run completion, recovery MUST skip unnecessary response decoding and duplicate business writes but still end lawfully. The Workspace-owning Runtime MAY atomically coordinate ending on `OPEN + owner is null + expected_generation`, based on confirmed consumer completion or a Runtime-owned failure. This boundary grants no executor, increments no generation and performs no new business write; a racing claim invalidates its predicate. Otherwise use lawful recovery qualification. Failure to persist an ending MUST NOT be reported as a committed terminal state: stop unsafe work, bound commit-truth reconciliation and retain uncertainty for later actual-state recovery.

Decision sources: CG05-Q61, CG05-Q67, CG05-Q71, CG05-Q73, CG05-Q83.

<a id="exr-010"></a>
**EXR-010.** **Deadline establishment.** The consumer defines when deadline_at must be established and whether queue/dependency waiting counts; it is not universally created_at plus timeout. Null before that stage is not unlimited execution permission. Establishment requires OPEN and an unset deadline: an equal already-established value can be confirmed, a different value is rejected, and ENDED cannot acquire a new deadline. Once established, deadline_at MUST NOT extend or reset on recovery. Combine monotonic elapsed time within a live process with retained UTC bounds after restart; never restart the full timeout or claim protection against arbitrary system-clock changes.

Decision sources: CG05-Q37, CG05-Q41, CG05-Q57, CG05-Q59.

<a id="exr-011"></a>
**EXR-011.** **Deadline and local recovery.** Deadline expiry MUST prohibit new dispatch, new remote effects and late first response publication. A response lawfully durable before expiry MAY still support deterministic local validation/business submission only when the consumer explicitly admits bounded local recovery under current valid qualification; this cannot reopen ENDED or extend the deadline. Consumer bounds remain finite across crashes/restarts and MUST NOT silently reset. Canonical business writes retain consumer current permission/source checks and current fencing at their transaction boundary. Only exact historical payloads actually needed for that operation are dependencies; lineage alone does not require rereading every source. Before enabling recovery, the consumer MUST define finite bounds, actual denial mappings and proof. Time-budget DENY converges as TIMED_OUT; other DENY causes require their actual Runtime-owned mapping. M1 defines no generic RECOVERY_NOT_ADMITTED fallback or universal policy object.

Decision sources: CG05-Q36, CG05-Q58, CG05-Q62, CG05-Q96, CG05-Q105, CG05-Q111, CG05-Q124.

<a id="exr-012"></a>
**EXR-012.** **MODEL Invocation shape and preparation.** `prepare_model_invocation(execution_qualification, response_format_key, max_response_bytes)` derives the owning Run from qualification; it MUST NOT accept another run_id. Runtime allocates invocation_id and atomically requires OPEN, current qualification and applicable consumer admission. The minimum logical MODEL projection has the following required fields; the separately committed dispatch descriptor is governed by EXR-013.

| Field | Type / constraint |
| --- | --- |
| invocation_id | UUIDv4, immutable |
| run_id | Derived UUIDv4, immutable |
| kind | `MODEL` |
| response_format_key | Registered exact string, immutable |
| max_response_bytes | Positive finite integer, snapshotted before dispatch |
| durability_phase | `PREPARED \| DISPATCH_INTENT_DURABLE \| RESPONSE_DURABLE` |
| dispatch_generation | Null while PREPARED; immutable positive generation captured with dispatch intent |
| response_rejection_code | Null or `RESPONSE_TOO_LARGE`, subject to EXR-027 |

Start PREPARED with null dispatch_generation/rejection. Phase advances monotonically; no rollback or shared TOOL copy. No response_durable_at or retention enum is added. The size bound has no permanent MiB default and covers the full stored representation, not only output text.

Decision sources: CG05-Q25, CG05-Q26, CG05-Q48, CG05-Q65, CG05-Q86, CG05-Q87, CG05-Q99, CG05-Q103, CG05-Q115, CG05-Q129.

<a id="exr-013"></a>
**EXR-013.** **Dispatch intent and descriptor.** Before adapter entry, the original execution path MUST win atomic intent publication under OPEN/current qualification/current consumer admission and deadline. Freeze the actual validated target/request descriptor and exact references in the same transaction as transition from PREPARED to DISPATCH_INTENT_DURABLE and capture dispatch_generation. Concrete descriptor fields belong to the consuming call schema; arbitrary SDK objects, current defaults or guessed request reconstruction cannot substitute. The actual send MUST use that committed descriptor. Intent existence alone is not a reusable send permit.

Decision sources: CG05-Q6, CG05-Q26, CG05-Q117.

<a id="exr-014"></a>
**EXR-014.** **Single live sending path.** Only the original live arbitration winner MAY enter the adapter, once, with its still-valid execution authority. Maintain one non-copyable, non-transferable live context per Invocation that records whether adapter entry has begun; do not reconstruct it from the database or introduce a durable dispatch-token identity. If intent commit acknowledgement is uncertain, that same path MAY continue after proving its intent committed, adapter entry has not begun and current qualification/admission remain valid. Crash, owner replacement, lost live context or inability to prove no adapter entry MUST fail closed: a later path cannot consume the old intent. A healthy current in-flight call is not OUTCOME_UNKNOWN merely because no response is yet durable. One admitted MODEL dispatch permits at most one actual request: hidden SDK retries/fallbacks are forbidden; production adapter proof belongs to M2.

Decision sources: CG05-Q27, CG05-Q28, CG05-Q31, CG05-Q33, CG05-Q77.

<a id="exr-015"></a>
**EXR-015.** **Safe preparation recovery.** Startup MUST fence former owners under the physical Workspace owner before reconciling unfinished Runs. Proven PREPARED with no committed intent permits continuation of the same Invocation only under freshly granted authority and current admission. An uncertain acknowledgement is not proof of absence. OPEN with no Invocation can represent pre-preparation or consumer-permitted waiting, not automatic corruption/remote uncertainty; consult consumer result/admission before continuing. Startup MUST NOT infer remote intent, silently substitute current references, block unrelated capabilities for one unavailable handler, or scan every historical payload merely to open the application.

Decision sources: CG05-Q30, CG05-Q66, CG05-Q128.

<a id="exr-016"></a>
**EXR-016.** **Complete response meaning.** A response format MUST define a strict data-only JSON object and a unique deterministic UTF-8 serialized representation for that format version, including key order, numbers, escaping and envelope/terminal data. No universal canonical-JSON framework is required. Complete protocol termination, including an output-limit terminal result, can produce a durable response even if consumer validation will reject its business content. A partial stream, raw HTTP/SDK object or transport secret is not such a response. Logical object order is not business identity, while array order/text remain exact; the format's unique serialization provides persisted-byte equality. Usage/timing telemetry does not enter this business-response identity. Incomplete usage does not prevent complete response persistence, become zero usage, or authorize reservation release.

Decision sources: CG05-Q7, CG05-Q9, CG05-Q19, CG05-Q40, CG05-Q45, CG05-Q54, CG05-Q68.

<a id="exr-017"></a>
**EXR-017.** **Response record and format authority.** Each MODEL Invocation has at most one immutable response. The logical record contains exactly five required nonnull fields: `invocation_id: UUIDv4`, `response_format_key: exact string`, `serialized_payload: UTF-8 bytes`, `sha256: Sha256Hex`, `byte_length: positive integer`. Format metadata MUST derive from the immutable Invocation key; a physical copy must agree, and disagreement is persistence corruption, not a second authority or permission to rewrite a key. Hash/length refer to the actual complete persisted bytes, not reserialization or business identity. Payload, integrity metadata and RESPONSE_DURABLE transition MUST commit atomically in the existing Workspace SQLite database. TEXT/BLOB is an implementation choice only if exact bytes are preserved.

Decision sources: CG05-Q20, CG05-Q39, CG05-Q46, CG05-Q47, CG05-Q100, CG05-Q130.

<a id="exr-018"></a>
**EXR-018.** **Publication input and precedence.** `publish_response(invocation_id, execution_qualification, serialized_payload)` accepts no response_format_key, caller hash or caller length. Runtime resolves the immutable format through Invocation and computes integrity metadata. Apply this precedence: validate input shapes, references/association and read access; then inspect any existing durable response before checking new-write execution eligibility. If one exists, follow EXR-019. If absent, require OPEN, current qualification, applicable deadline/consumer admission, the dispatch predicates of EXR-021, and valid format/size, then atomically publish. Ended state, expired deadline or old generation MUST NOT suppress legal confirmation of an already-existing immutable fact, nor authorize any new write.

Decision sources: CG05-Q8, CG05-Q89, CG05-Q118.

<a id="exr-019"></a>
**EXR-019.** **Read-only confirmation.** For an existing response, verify retained metadata and actual stored byte integrity, compare the Invocation-derived format and complete submitted bytes: identical response returns the original publication result with no mutation; differing bytes are an integrity conflict. Hash equality alone is insufficient. Confirming the original bytes MUST NOT require a now-unavailable business reader or guess semantic equivalence by decoding/re-encoding. Missing/corrupt payload returns the corresponding read failure; this confirmation path MUST NOT end or repair the Run. Any later OPEN-Run convergence uses separately lawful EXR-009 coordination.

Decision sources: CG05-Q40, CG05-Q55, CG05-Q89, CG05-Q91, CG05-Q92.

<a id="exr-020"></a>
**EXR-020.** **Immutable publication result.** First successful publication and identical confirmation return exactly the same immutable projection: `invocation_id`, `response_format_key`, `sha256`, `byte_length`, all nonnull with EXR-017 types. Do not rebuild it using current Run/Invocation state or add a separate receipt table. A losing first-publication race MUST reread the committed winner: equal response confirms, different response conflicts, and absence follows the actual failure/uncertainty outcome. An uncertain commit cannot be treated as known absence.

Decision sources: CG05-Q93, CG05-Q94.

<a id="exr-021"></a>
**EXR-021.** **First-publication authority.** First publication MUST still originate from the original valid execution path; matching generation values alone cannot establish that path. It requires DISPATCH_INTENT_DURABLE and equality of submitted qualification generation, current Run generation and immutable dispatch_generation, with the current owner/OPEN/admission/deadline checks. A new generation may recover an existing response, never publish an old undurable callback. Validate the registered format and its deterministic serialization; reject nonconforming new bytes rather than silently normalize them. The atomic write must recheck authority so revocation/ending wins safely. These predicates do not apply as new-write requirements to EXR-019's read-only confirmation. Late callback audit is not permission to publish or advance business state.

Decision sources: CG05-Q29, CG05-Q35, CG05-Q125, CG05-Q126.

<a id="exr-022"></a>
**EXR-022.** **Commit uncertainty.** Creation, grant, intent, response and ending commit uncertainty MUST be reconciled against the actual durable identity/state with finite attempt/time bounds chosen by implementation/consumer. No permanent retry count is frozen. Database busy, unreadable storage or an unconfirmed read is not absence, missing payload or rollback. After bounded inability to establish truth, return unresolved/storage failure and cease unsafe effects without claiming a terminal write succeeded. Never call the Provider again to resolve local persistence uncertainty.

Decision sources: CG05-Q10, CG05-Q38, CG05-Q72, CG05-Q73, CG05-Q84.

<a id="exr-023"></a>
**EXR-023.** **Raw response reads.** A raw response read by invocation_id MUST validate read access, associated immutable metadata and stored bytes/hash/length. It returns EXR-017 or distinctly reports Invocation not found, response not yet durable, required payload missing, integrity failure or storage read failure. It requires neither an execution grant nor an available business decoder and performs no mutation. It must not classify unreadable storage as proven missing or substitute another response/current input.

Decision sources: CG05-Q106.

<a id="exr-024"></a>
**EXR-024.** **Consumer recovery protocol.** The immutable consumer_key selects three typed responsibilities: `reconcile_result` reads consumer truth without business mutation; `admit_recovery` evaluates current eligibility, permitted scope and finite bounds without effects; `resume_local` runs only with valid qualification and retains consumer write ownership. Reconciliation returns `COMPLETION_CONFIRMED | RECOVERY_REQUIRED | UNRESOLVED`; confirmation means whole-Run criteria, not one arbitrary result. Admission returns `ALLOW | DENY | UNRESOLVED`. Unknown reads are UNRESOLVED, not negative evidence. Bound unresolved coordination and do not execute effects. DENY performs no recovery and converges through the authorized ending boundary with EXR-011's scoped mapping. Concrete typed inputs/result refs and failure mappings must be supplied and tested by each consumer before enabling that path; no generic workflow plan or business failure container is introduced.

Decision sources: CG05-Q70, CG05-Q79, CG05-Q95, CG05-Q104, CG05-Q105, CG05-Q111.

<a id="exr-025"></a>
**EXR-025.** **Recovery order.** Under lawful startup/recovery coordination, reconcile consumer completion first. Confirmed whole-Run completion can converge without unnecessary payload/reader dependencies. If recovery is required, evaluate current admission and required exact dependencies, then acquire applicable authority for local execution. Needed response bytes MUST be integrity-checked before decoding. Missing/corrupt payload or unavailable/invalid format follows EXR-031; a missing historical consumer follows EXR-032. Never downgrade durability_phase or redial the Provider. Previously ENDED stays ENDED even when dependencies later return.

Decision sources: CG05-Q55, CG05-Q58, CG05-Q64, CG05-Q69, CG05-Q71, CG05-Q74, CG05-Q82.

<a id="exr-026"></a>
**EXR-026.** **Size accounting.** Snapshot max_response_bytes when preparing the MODEL Invocation, before any remote request. Account for the full deterministic serialized response including envelope and terminal information. Reception itself MUST use finite buffering/resource protection and MAY stop before remote termination when a bound is exceeded. Best-effort interruption depends on adapter support; do not require unlimited draining just to obtain a terminal result or claim that local interruption proves remote termination.

Decision sources: CG05-Q48, CG05-Q68, CG05-Q102.

<a id="exr-027"></a>
**EXR-027.** **Known-complete size rejection.** `response_rejection_code = RESPONSE_TOO_LARGE` is permitted only with confirmed complete remote termination and a deterministic serialized response exceeding max_response_bytes. Atomically retain that code, DISPATCH_INTENT_DURABLE with no response record, and Run ending FAILED/RESPONSE_TOO_LARGE under valid authority. It is immutable; PREPARED and RESPONSE_DURABLE require null rejection code. Do not persist a truncated/oversized body, fabricate RESPONSE_DURABLE, retry the Provider or erase known completion. If another ending already won, do not rewrite it or attach this marker as though the required atomic outcome occurred.

Decision sources: CG05-Q76, CG05-Q87, CG05-Q99.

<a id="exr-028"></a>
**EXR-028.** **Interrupted reception.** Stopping a stream before confirmed remote completion cannot set RESPONSE_TOO_LARGE rejection evidence. When the execution path is lost/interrupted with committed intent and no durable response or complete rejection evidence, converge as OUTCOME_UNKNOWN with null failure_code and null rejection code unless another ending already won. Preserve possible remote effects/spend; local resource exhaustion is not proof of a complete rejected response.

Decision sources: CG05-Q67, CG05-Q99, CG05-Q101, CG05-Q102.

<a id="exr-029"></a>
**EXR-029.** **TOOL seam.** The common TOOL portion is `invocation_id: UUIDv4`, immutable owning `run_id: UUIDv4`, and `kind: TOOL`. Its action Contract MUST supply typed exact inputs, current permission/admission, completion/result evidence, required recovery data and explicit reconcile/re-execution conditions. Do not copy MODEL phases, response formats or dispatch markers onto every Tool. Without a concrete action agreement, fail closed on recovery rather than infer replay safety from its name. M1's proof consumer is a controlled exact-version local read, not a production Tool catalog, remote-idempotency subsystem or business-write Tool.

Decision sources: CG05-Q17, CG05-Q25, CG05-Q70, CG05-Q116, CG05-Q121.

<a id="exr-030"></a>
**EXR-030.** **Controlled local-read recovery.** The controlled read MUST retain immutable exact input references and prove it performs no hidden Ensure, parsing, business write or remote request. If its durable result is valid, reuse it. If unfinished and no reusable durable result exists, its explicit pure-read agreement MAY re-execute the same Invocation under fresh valid Run qualification, current permission and the same exact inputs. Required missing-dependency outcomes and completion/result evidence must be typed in that proof consumer. Do not upgrade lineage-only refs into read prerequisites or replace historical inputs with current values. A later independent Context acquisition is a new ToolInvocation; recovery of this original unfinished read is not a new acquisition. These permissions never authorize MODEL replay.

Decision sources: CG05-Q116, CG05-Q122, CG05-Q123, CG05-Q124.

<a id="exr-031"></a>
**EXR-031.** **Response failure convergence.** When needed for an OPEN Run's recovery, confirmed missing payload ends FAILED/RESPONSE_PAYLOAD_UNAVAILABLE; bad hash/length ends FAILED/RESPONSE_INTEGRITY_FAILED; an unavailable registered historical reader ends FAILED/RESPONSE_FORMAT_UNAVAILABLE; intact bytes with an available reader that violate the selected format end FAILED/RESPONSE_FORMAT_INVALID. Preserve phase, metadata, original payload when present and format key; never fetch a replacement. A known writer/reader capability absence before dispatch must prevent the call and converge as FAILED/RESPONSE_FORMAT_UNAVAILABLE. Known-complete size rejection uses EXR-027. These are Runtime failure causes; validly decoded but unacceptable consumer business output stays with its consumer. All endings still require EXR-008/009; read errors alone do not confer write authority.

Decision sources: CG05-Q53, CG05-Q64, CG05-Q69, CG05-Q74, CG05-Q75, CG05-Q76.

<a id="exr-032"></a>
**EXR-032.** **Handler and structural failures.** A missing historical consumer handler isolates the affected OPEN Run and converges through lawful coordination as FAILED/CONSUMER_UNAVAILABLE; it does not fail unrelated application startup, reinterpret the key or reopen an ended Run. In contrast, invalid persisted Run structure (negative generation, unknown enum, inconsistent ending fields) is a persistence-integrity failure: stop the affected operation without automatic repair or pretending the record is a valid business failure. Whole-store integrity rules remain Storage-owned. Caller errors `RUN_NOT_FOUND`, `INVOCATION_NOT_FOUND`, `REFERENCE_MISMATCH`, `RUN_ENDED`, `EXECUTION_NOT_CURRENT` are operation rejections, not automatic FAILED endings.

Decision sources: CG05-Q82, CG05-Q98, CG05-Q109, CG05-Q110.

<a id="exr-033"></a>
**EXR-033.** **Operation results and failure obligations.** Implementations MUST expose typed success/rejection/uncertainty results for the internal operations below. Structural/type failures and reference/read-access failures precede state-dependent mutation checks; publication's special existing-response precedence remains EXR-018. Failed CAS/conflicting state is not success, and acknowledgement loss is not rollback. No HTTP mapping is specified.

| Operation | Success / no-op projection | Rejection or unresolved distinctions |
| --- | --- | --- |
| Create Run | run_id | Invalid/unknown consumer or deadline; persistence/commit uncertainty |
| Read Run by run_id | EXR-003 record | RUN_NOT_FOUND; read access; structural integrity; storage read failure |
| Grant | EXR-005 qualification | RUN_NOT_FOUND; RUN_ENDED; owner/expected-generation conflict; overflow; consumer denial/unresolved; commit uncertainty |
| Revoke | Revocation confirmed, generation retained | RUN_NOT_FOUND; EXECUTION_NOT_CURRENT; storage/commit uncertainty |
| Establish deadline | Established exact deadline | RUN_NOT_FOUND; RUN_ENDED; different frozen deadline; invalid input; storage/commit uncertainty |
| Cancel / authorized end | Original committed Run ending | Missing Run; missing authorization or stale executor qualification; invalid reason/code; storage/commit uncertainty |
| Ownerless coordination | Committed ending or original ended outcome | Missing Run; owner/generation race; unconfirmed consumer completion; invalid Runtime failure evidence; commit uncertainty |
| Prepare MODEL | invocation_id | RUN_NOT_FOUND; RUN_ENDED; EXECUTION_NOT_CURRENT; invalid format/size; consumer denial/unresolved; commit uncertainty |
| Commit dispatch intent | Confirmed intent for original live winner | Missing/mismatched refs; no valid current authority/admission/deadline; already-consumed or uncertain sending path; storage/commit uncertainty |
| Publish / confirm response | EXR-020 immutable four-field result | EXR-018/019/021 ordering, immutable conflict, format/size failure, missing/corrupt stored bytes, storage/commit uncertainty |
| Read raw response | EXR-017 record | EXR-023 distinctions |
| Consumer reconciliation/admission | EXR-024 variants | No conversion of unresolved reads into permission or absence |

The remaining logical call shapes below complete this internal interface. Parameters named `descriptor` and consumer result/failure facts are typed by the registered consumer, not open generic JSON; they never become additional Run fields. Execution qualification has EXR-005's three fields; generation/UUID/instant types are EXR-003/COM-047. Workspace/consumer authorization and original live-path context are execution preconditions enforced by Runtime, not caller-supplied boolean assertions.

| Logical call | Input / output data |
| --- | --- |
| establish_deadline | Inputs: run_id (UUIDv4), deadline_at (nonnull UTC instant), under the consumer's authorized establishment boundary. Success: that exact deadline_at; apply EXR-010's write-once rules |
| end_run | Inputs: execution_qualification, end_reason (EXR-003 enum), failure_code (nullable string with iff-FAILED rule). Runtime validates the corresponding consumer completion/failure or time/cancellation evidence; values alone do not authorize an ending |
| coordinate_ending | Inputs: run_id (UUIDv4), expected_generation (exact integer), confirmed typed consumer-completion or Runtime-failure facts. Only the lawful Workspace Runtime derives end_reason/failure_code and performs EXR-009's ownerless CAS; this is not a public arbitrary-state setter |
| cancel_run | Input: run_id (UUIDv4), through the separately authorized Run-wide cancellation boundary; no executor token required |
| End-operation success | Exactly the immutable ending projection: run_id, execution_generation, ended_at, end_reason, failure_code, with EXR-003 types. Runtime owns ended_at. Existing ending returns the same fields; no mutable owner/status reconstruction or receipt record |
| revoke_execution | Input: execution_qualification. Success: revocation confirmed with the retained generation from that qualification; no new execution token |
| commit_dispatch_intent | Inputs: invocation_id (UUIDv4), execution_qualification, consumer-validated typed descriptor/exact refs. The association must match qualification.run_id. Success confirms this Invocation's committed intent/dispatch_generation to the original live winner; it issues no transferable serialized sending token. Actual sending still requires EXR-014 |
| read_model_invocation | Input: invocation_id (UUIDv4). Success: EXR-012's required projection and, after intent publication, the consumer-typed committed descriptor; preserve read access and missing/reference/integrity/storage distinctions. A read never recreates the live sending context |

Logical result categories do not create a universal persisted operation-error enum. Only explicitly named stable Runtime failures may populate failure_code; concrete later-consumer mappings must close before use. Action-specific TOOL methods remain governed by EXR-029/030.

Decision sources: CG05-Q1, CG05-Q8, CG05-Q44, CG05-Q83, CG05-Q93, CG05-Q98, CG05-Q112, CG05-Q113, CG05-Q114, CG05-Q118, CG05-Q120, CG05-Q129.

<a id="exr-034"></a>
**EXR-034.** **Deferred interfaces and compatibility.** The M1 definitions MUST NOT be taken as readiness for production protected calls, Tool business schemas, explicit Run-level retry/lineage, active payload purge/disposition, response_durable_at, the full late-usage subsystem or platform workflow integration. Later consumers must review both ends of their concrete interfaces. Existing Candidate Save receipt/authority and Materials Work/attempt/publication semantics remain unchanged; no replacement by AgentRun or reuse of their state enums is implied.

Decision sources: CG05-Q22, CG05-Q50, CG05-Q51, CG05-Q78, CG05-Q86, CG05-Q90, CG05-Q111, CG05-Q116.
