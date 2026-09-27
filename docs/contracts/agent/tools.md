# Tools Contract — Typed Action Admission

> **Current applicability — 2026-09-24.S2M1S1-r1.** Existing typed admission and conformance read/model formats survive; TOL-015 does not expose generic file/database/web access. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../../design/contract/sl-02-m1-supplement-grill.md); [current review](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> Normative scope revision: **2026-09-24.S3M2-r1**. English is authoritative. This defines required behavior, not implemented or executed acceptance. Earlier scoped consumers remain unchanged.

[Decision register](../../archived/sl-03-m2-grill.md) · [Contract index](../index.md)

This internal boundary consumes COM-049. Its execution authority and action-recovery interfaces depend on the replacement Execution Runtime Contract, so TOL-001–015 are not implementation-ready until that interface is reconciled. It is not a public generic Tool HTTP API or a complete business action catalog.

<a id="tol-001"></a>
**TOL-001.** **Static registry.** Register a finite static set of exact action keys. Each item MUST supply an unambiguous Provider function name, owned typed input validator/projection protocol, allowed resource-scope/permission checks, typed result protocol and finite bounds, handler, completion-evidence reader and reexecution_classification. The classification is ALLOWED_BY_ACTION_PROTOCOL with its exact agreement, or NOT_REEXECUTABLE; absent recovery agreement defaults to the latter. Do not require a recovery protocol for one-shot actions. Conflicting names/keys disable the affected capability rather than choose a winner. No plugin loader, arbitrary shell/SQL/HTTP or model-autonomous browser is introduced.

Decision sources: [CG06-Q3](../../archived/sl-03-m2-grill.md#cg06-q3), [CG06-Q9](../../archived/sl-03-m2-grill.md#cg06-q9), [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q57](../../archived/sl-03-m2-grill.md#cg06-q57), [CG06-Q179](../../archived/sl-03-m2-grill.md#cg06-q179), [CG06-Q198](../../archived/sl-03-m2-grill.md#cg06-q198).

<a id="tol-002"></a>
**TOL-002.** **Projection versus authority.** Provider-visible schema is a controlled projection of the owned typed action protocol. It MUST accurately express supported constraints without contradicting or weakening that protocol. Runtime validation remains authoritative for every argument, exact reference, permission and eligibility condition, including those unavailable in Provider schema. Schema-valid output is not admission. Freeze the exact exposed action/projection basis in Frame provenance; a later registration with the same name cannot reinterpret historical arguments. Compatible implementation fixes need not freeze source hashes. The current production projection uses ordinary DeepSeek Chat Completions without Beta strict mode.

Decision sources: [CG06-Q10](../../archived/sl-03-m2-grill.md#cg06-q10), [CG06-Q43](../../archived/sl-03-m2-grill.md#cg06-q43), [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q60](../../archived/sl-03-m2-grill.md#cg06-q60), [CG06-Q100](../../archived/sl-03-m2-grill.md#cg06-q100), [CG06-Q179](../../archived/sl-03-m2-grill.md#cg06-q179), [CG06-Q198](../../archived/sl-03-m2-grill.md#cg06-q198), [CG06-Q207](../../archived/sl-03-m2-grill.md#cg06-q207).

<a id="tol-003"></a>
**TOL-003.** **Effective capability intersection.** Expose and execute only the intersection of registration, Skill action allowlist, Package/acquisition scope and current permission, plus any actual action approval requirement. An exposed definition does not preauthorize later execution. Model/Tool text, checkpoints and generated IDs cannot enlarge scope. Exact source eligibility need not mean latest; it follows its owner. Static configuration is not a mutable permission grant.

Decision sources: [CG06-Q3](../../archived/sl-03-m2-grill.md#cg06-q3), [CG06-Q10](../../archived/sl-03-m2-grill.md#cg06-q10), [CG06-Q30](../../archived/sl-03-m2-grill.md#cg06-q30), [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q135](../../archived/sl-03-m2-grill.md#cg06-q135), [CG06-Q205](../../archived/sl-03-m2-grill.md#cg06-q205), [CG06-Q215](../../archived/sl-03-m2-grill.md#cg06-q215).

<a id="tol-004"></a>
**TOL-004.** **Single-request execution boundary.** ToolInvocationRuntime executes one request explicitly selected by Skill/Application. Skill owns multi-request selection/order/failure policy; Runtime MUST NOT universally execute all returned requests or implement first-error-stop. Current semantic Runs allow at most one active MODEL/TOOL; each selected Tool receives independent current qualification, permission, deadline and action-protocol checks. Tool/semantic-step bounds belong to the Skill; there is no M2 Operation Tool-count wallet. Necessary invocation audit is not a business write by a pure read.

Decision sources: [CG06-Q8](../../archived/sl-03-m2-grill.md#cg06-q8), [CG06-Q59](../../archived/sl-03-m2-grill.md#cg06-q59), [CG06-Q144](../../archived/sl-03-m2-grill.md#cg06-q144), [CG06-Q164](../../archived/sl-03-m2-grill.md#cg06-q164), [CG06-Q180](../../archived/sl-03-m2-grill.md#cg06-q180).

<a id="tol-005"></a>
**TOL-005.** **Model-origin request locator.** The internal model-origin selection input is execution_qualification plus producing_model_invocation_id and tool_call_index (nonnegative exact zero-based position in the immutable terminal tool_calls list). Derive action and raw arguments from the durable response and its exposed Frame definition, not caller duplicates. The producing MODEL MUST belong to the same Run. Provider tool-call id is correlation, not local identity. Shared operation_id grants no cross-Run permission. Application-origin typed actions retain a separate entry; they cannot claim a nonexistent model request.

Decision sources: [CG06-Q58](../../archived/sl-03-m2-grill.md#cg06-q58), [CG06-Q61](../../archived/sl-03-m2-grill.md#cg06-q61), [CG06-Q109](../../archived/sl-03-m2-grill.md#cg06-q109), [CG06-Q141](../../archived/sl-03-m2-grill.md#cg06-q141), [CG06-Q142](../../archived/sl-03-m2-grill.md#cg06-q142), [CG06-Q143](../../archived/sl-03-m2-grill.md#cg06-q143), [CG06-Q177](../../archived/sl-03-m2-grill.md#cg06-q177).

<a id="tol-006"></a>
**TOL-006.** **Unique association and confirmation.** At most one TOOL Invocation may associate with (producing_model_invocation_id, tool_call_index). Publish the association and creation atomically under current admission and seriality; Runtime allocates invocation_id. No argument/hash-based deduplication merges distinct requests. With historical read eligibility and structural integrity, an existing valid association returns its original invocation_id read-only before fresh execution admission. Confirmation never calls a handler or grants replay. Unknown commit is not absence; do not create a replacement. Definite initial rejection leaves no Tool Invocation or RejectedTool record.

Decision sources: [CG06-Q26](../../archived/sl-03-m2-grill.md#cg06-q26), [CG06-Q61](../../archived/sl-03-m2-grill.md#cg06-q61), [CG06-Q142](../../archived/sl-03-m2-grill.md#cg06-q142), [CG06-Q144](../../archived/sl-03-m2-grill.md#cg06-q144), [CG06-Q178](../../archived/sl-03-m2-grill.md#cg06-q178).

<a id="tol-007"></a>
**TOL-007.** **Argument validation.** After complete response durability, parse the selected raw arguments under finite byte/depth/node bounds into the owned closed input type. Reject duplicate keys, unknown fields, nonobject roots, invalid Unicode, type coercion, truncation or automatic repair. Check object existence/ownership/exact scope and current permission. A missing/incompatible exposed definition or invalid request yields a typed action-admission rejection. Any later model-based correction is a separately admitted consumer-defined invocation, never a hidden Tool/parser call.

Decision sources: [CG06-Q39](../../archived/sl-03-m2-grill.md#cg06-q39), [CG06-Q43](../../archived/sl-03-m2-grill.md#cg06-q43), [CG06-Q60](../../archived/sl-03-m2-grill.md#cg06-q60), [CG06-Q65](../../archived/sl-03-m2-grill.md#cg06-q65), [CG06-Q143](../../archived/sl-03-m2-grill.md#cg06-q143).

<a id="tol-008"></a>
**TOL-008.** **Action completion and representation.** Represent action completion independently from result encoding/returned-content admission. A reliably completed action remains completed if projection/schema/encoding or Context admission fails; a single overall FAILED must not imply the effect did not happen. Before invoking a handler, its agreement MUST define how actual completion evidence is retained/read, how definite failure differs from unknown action outcome, and which result is available. Do not copy MODEL PREPARED/intent/response phases onto all Tools. Result schema and size failures cannot authorize handler reexecution.

Decision sources: [CG06-Q62](../../archived/sl-03-m2-grill.md#cg06-q62), [CG06-Q63](../../archived/sl-03-m2-grill.md#cg06-q63), [CG06-Q64](../../archived/sl-03-m2-grill.md#cg06-q64), [CG06-Q65](../../archived/sl-03-m2-grill.md#cg06-q65).

<a id="tol-009"></a>
**TOL-009.** **Result readers.** Read an existing Tool result through its action-owned exact evidence protocol. Historical reading does not execute the handler; new Frame inclusion independently rechecks scope/privacy/permission. Define finite result/projection limits and rejection behavior without silent truncation of a claimed complete result. Caller-provided arbitrary text cannot replace evidence. A complete action without an admissible model representation may force its consumer to stop while preserving action truth.

Decision sources: [CG06-Q47](../../archived/sl-03-m2-grill.md#cg06-q47), [CG06-Q62](../../archived/sl-03-m2-grill.md#cg06-q62), [CG06-Q64](../../archived/sl-03-m2-grill.md#cg06-q64), [CG06-Q65](../../archived/sl-03-m2-grill.md#cg06-q65), [CG06-Q194](../../archived/sl-03-m2-grill.md#cg06-q194).

<a id="tol-010"></a>
**TOL-010.** **Recovery and reexecution.** Only ALLOWED_BY_ACTION_PROTOCOL permits recovery reexecution, under that agreement's current permission/source/qualification/deadline checks and explicit denial mappings. NOT_REEXECUTABLE or unknown remote effect never becomes replayable merely from missing local output. Existing completion evidence takes precedence over unnecessary reexecution. Model retry semantics, generic HTTP idempotency or graph checkpoints do not establish action replay safety. Whole-Run ending remains the actual consumer's decision under the replacement Runtime agreement.

Decision sources: [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q62](../../archived/sl-03-m2-grill.md#cg06-q62), [CG06-Q63](../../archived/sl-03-m2-grill.md#cg06-q63), [CG06-Q78](../../archived/sl-03-m2-grill.md#cg06-q78), [CG06-Q180](../../archived/sl-03-m2-grill.md#cg06-q180).

<a id="tol-011"></a>
**TOL-011.** **Current read action.** The conformance wrapper reuses controlled.response-read.v1 without changing its historical meaning: typed input is exactly source_invocation_id; it names one retained immutable MODEL response. Read verified actual bytes through the existing repository and retain completion evidence under the TOOL invocation_id. The model-visible result projection is exactly {source_sha256: SHA-256, source_byte_length: positive exact integer}; map those values from existing LocalRead result_sha256 and result_byte_length respectively. This adds a projection, not a rename of historical action evidence. Encode the Tool content as compact UTF-8 JSON with fixed source_sha256 then source_byte_length order; integer spelling is unsigned base-10 without leading zeros, with EXR-049 string escaping. DeepSeekResponseReadProjection:v1 has function name controlled_response_read and description "Read the SHA-256 and byte length of the one authorized exact response." Its parameters value is exactly the JSON object below. Runtime additionally validates canonical UUIDv4, exact target, current permission and all owned action requirements; schema does not grant access. The transport deterministically wraps the Frame definition as {type: function, function: {name, description, parameters}} with no strict-mode field.

```json
{"type":"object","properties":{"source_invocation_id":{"type":"string","pattern":"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"}},"required":["source_invocation_id"],"additionalProperties":false}
```

 The target is separate from the producing MODEL request and may be in the explicitly authorized fixture source Run. Before execution, require target equality with Package's sole allowed exact source; reject any other model-supplied invocation_id. The action does not return source body, parse business semantics, Ensure dependencies or access the network. Reexecution is allowed only through the preserved exact local-read agreement; previous completed digest/length is readable without rereading a body merely to recognize completion.

Decision sources: [CG06-Q45](../../archived/sl-03-m2-grill.md#cg06-q45), [CG06-Q46](../../archived/sl-03-m2-grill.md#cg06-q46), [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q62](../../archived/sl-03-m2-grill.md#cg06-q62), [CG06-Q177](../../archived/sl-03-m2-grill.md#cg06-q177), [CG06-Q194](../../archived/sl-03-m2-grill.md#cg06-q194), [CG06-Q215](../../archived/sl-03-m2-grill.md#cg06-q215).

<a id="tol-012"></a>
**TOL-012.** **Error distinctions.** Internal Tool outcomes MUST distinguish request/source not found or invalid locator, wrong Run/kind, TOOL_NOT_ALLOWED, TOOL_ARGUMENTS_INVALID, TOOL_PROTOCOL_UNAVAILABLE, SOURCE_UNAVAILABLE, PERMISSION_DENIED, execution not current/Run ended/deadline denial, serial conflict, storage unavailability and persistence integrity. Existing result representation/admission failures remain distinct from action failure/unknown completion. These categories do not themselves set Run failure_code. A consumer must supply actual recovery/ending mappings before being enabled; no generic RECOVERY_NOT_ADMITTED fallback is restored.

Decision sources: [CG06-Q56](../../archived/sl-03-m2-grill.md#cg06-q56), [CG06-Q60](../../archived/sl-03-m2-grill.md#cg06-q60), [CG06-Q63](../../archived/sl-03-m2-grill.md#cg06-q63), [CG06-Q64](../../archived/sl-03-m2-grill.md#cg06-q64), [CG06-Q144](../../archived/sl-03-m2-grill.md#cg06-q144), [CG06-Q178](../../archived/sl-03-m2-grill.md#cg06-q178), [CG06-Q179](../../archived/sl-03-m2-grill.md#cg06-q179), [CG06-Q196](../../archived/sl-03-m2-grill.md#cg06-q196).

<a id="tol-013"></a>
**TOL-013.** **Executable candidate admission.** For the current DeepSeek profile, only a complete durable tool_calls terminal result with structurally admissible requests yields executable Tool candidates. Other finish reasons or ambiguous duplicate Provider Tool-call IDs yield no executable set, even if the terminal response remains durably valid evidence. Do not rename IDs, merge requests or substitute local indexes as Provider reply IDs. This is the current support profile, not a claimed universal Provider rule.

Decision sources: [CG06-Q58](../../archived/sl-03-m2-grill.md#cg06-q58), [CG06-Q98](../../archived/sl-03-m2-grill.md#cg06-q98), [CG06-Q102](../../archived/sl-03-m2-grill.md#cg06-q102), [CG06-Q103](../../archived/sl-03-m2-grill.md#cg06-q103), [CG06-Q112](../../archived/sl-03-m2-grill.md#cg06-q112), [CG06-Q113](../../archived/sl-03-m2-grill.md#cg06-q113), [CG06-Q196](../../archived/sl-03-m2-grill.md#cg06-q196).

<a id="tol-014"></a>
**TOL-014.** **DeepSeek continuation.** For current DeepSeek Chat Completions, retaining an assistant turn with N tool_calls requires N lawful admitted corresponding Tool results before the next MODEL continuation. The selected action/result protocol defines truthful replies; M2 adds no synthetic denial-result protocol. Skill may execute only part and terminate this continuation path. It MUST NOT delete unexecuted calls, rewrite the original assistant turn into a subset, fabricate results or let the adapter execute remaining Tools. Preserve ordered requests, exact Provider ids and required reasoning history. Future Provider partial-continuation protocols require their own adapter agreement.

Decision sources: [CG06-Q59](../../archived/sl-03-m2-grill.md#cg06-q59), [CG06-Q97](../../archived/sl-03-m2-grill.md#cg06-q97), [CG06-Q105](../../archived/sl-03-m2-grill.md#cg06-q105), [CG06-Q128](../../archived/sl-03-m2-grill.md#cg06-q128), [CG06-Q195](../../archived/sl-03-m2-grill.md#cg06-q195), [CG06-Q196](../../archived/sl-03-m2-grill.md#cg06-q196).

## Supplement: frozen Evidence retrieval consumer boundary

Scope revision **2026-09-24.S2M1S1-r1**. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="tol-015"></a>
**TOL-015.** DeepFit Evidence reads MUST be typed, read-only and scoped to the run’s frozen exact projection and permitted EVD-018 references. Support block reads and expansion to the corresponding entry or broader permitted projection coverage; return source-preserving admitted text/fields and exact provenance, with explicit missing/denied/unavailable outcomes. Enforce EVD-019 privacy on every result, before model visibility. No latest/other-Resume substitution, URL fetch, hidden derivation, Save, vector index or generic RAG fallback is authorized. Record actual selected and acquired inputs/coverage; EVD-021 governs negative conclusions. The future Fit consumer Contract still owns its concrete Tool request/result schema, orchestration and scoring; this interface alone does not make SL-05 implementation-ready.
