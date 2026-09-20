# Candidate Commands, HTTP and Atomic Save Contract

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. This body defines only the SL-02.M1 consumed scope; future consumer scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../design/contract/sl-02-m1-grill.md)

## 1. Complete write interfaces

<a id="sav-001"></a>
**SAV-001.** SL-02.M1 MUST expose exactly the following nine POST operations under /api/v1; all successful commands return 200. Body field sets are closed and complete, with no generic payload wrapper. Existing target identity comes only from path; no client-chosen new business ID, timestamp, schema_version or current pointer is accepted. revision is COM-028; request_id is client-generated UuidV4. Other values use their normative field owner.

| command_type | Route after /api/v1 | Exact body fields |
| --- | --- | --- |
| PROFILE_SAVE | /profile/save | request_id, revision, full_name, phone_number, email |
| EVIDENCE_CREATE | /evidence-items | request_id, kind, fields, content |
| EVIDENCE_UPDATE | /evidence-items/{evidence_item_id}/save | request_id, revision, fields, content |
| EVIDENCE_RETIRE | /evidence-items/{evidence_item_id}/retire | request_id, revision |
| RESUME_CREATE | /resumes | request_id, resume_name, profile_version_id, header_presentation, sections, document_presentation |
| RESUME_SAVE | /resumes/{resume_id}/save | request_id, revision, profile_version_id, header_presentation, sections, document_presentation |
| RESUME_RENAME | /resumes/{resume_id}/rename | request_id, revision, resume_name |
| RESUME_REMOVE | /resumes/{resume_id}/remove | request_id, revision, default_resume_selection: {revision}, replacement_resume_id: UuidV4 or null |
| DEFAULT_RESUME_SET | /workspace/default-resume/set | request_id, revision, default_resume_id: UuidV4 |

For remove, revision is target Resume revision and nested revision is selection revision. Set-default revision is selection revision. Create has no expected root/default token. Content Saves MUST replace complete owned content, not PATCH or preserve omissions. (Q65/Q67/Q76/Q84.)

<a id="sav-002"></a>
**SAV-002.** All nine operations MUST share one per-Workspace SL-02 command-family request_id namespace, independent of Manual Entry and Preferences namespaces. Success, including no-op, MUST atomically persist a receipt with the command's owned changes. Retain it for Workspace lifetime without TTL or deletion on retirement/removal. Matching successful replay MUST return the original result without reexecution or rewinding current state; a successfully used key with a different admitted operation/target/revision/content MUST fail REQUEST_CONFLICT, subject to SAV-003 admission precedence. Explicit proven-uncommitted rejection creates no success receipt. This MUST NOT become a universal idempotency framework. (Q68/Q73/Q74.)

## 2. Admission and atomic publication

<a id="sav-003"></a>
**SAV-003.** Processing MUST enforce local access and raw admission, then field validation/canonicalization and fingerprint before receipt; only receipt miss proceeds to mutable revision/lifecycle/freshness/capacity and execution. Exception: EVIDENCE_UPDATE MUST first admit the common envelope (request_id/revision, object fields and basic shared content structure), read the target's permanent Item.kind, validate fields/content under that authoritative schema, then canonicalize/fingerprint and inspect receipt. This read MUST NOT admit current status/revision or infer schema from six payload keys; no kind input is added. At this lookup an absent target MUST return 404 NOT_FOUND before receipt even for a key already used elsewhere. Retained retired Items still supply kind for successful historical replay. Actually detected corrupt persisted references use STO-028. (Q74/Q88 superseded by Q98 and its accepted precedence clarification.)

<a id="sav-004"></a>
**SAV-004.** On receipt miss, ordinary existing-root mutation MUST check revision before canonical equality. Stale revision MUST conflict even for equal content. New roots start revision 1; each real root change increments once. At maximum revision a valid no-op MAY succeed but any required increment MUST fail REVISION_EXHAUSTED without overflow or partial changes. A→B→A MUST publish a fresh immutable Version, never reactivate an old ID. Application equality follows PRO/EVD/RES, not JSON bytes/UI state.

| Change | Owned publication |
| --- | --- |
| Profile content | new ProfileVersion, root pointer/revision/time |
| Evidence create/content change | new Item when creating, new Version, root pointer/revision/time, complete new Baseline/pointer |
| Resume create/document change | new root when creating, new Version, root pointer/revision/time; first-create selection under WSP-010 |
| Resume rename | root name/revision/time only |
| First Evidence retire | root status/revision/time and complete new Baseline; no fact Version |
| First Resume remove | root status/revision/time and necessary default switch; no document Version |
| Matching valid canonical no-op | no business Version/Baseline/revision/time change; success receipt still committed |

Receipt/results are part of each successful command. No cross-Resume propagation or Profile/Evidence change follows from local Resume expression. (Q57/Q64/Q68/Q69.)

<a id="sav-005"></a>
**SAV-005.** Each real publication MUST use one publication_time = max(current UTC millisecond time, previous updated_at of roots actually modified, previous current Baseline.created_at only if this command advances Baseline). Ignore absent prior-root values during creation. Assign it to modified roots' updated_at, new roots' created_at/updated_at and all new Versions/Snapshots' created_at; preserve old root created_at. Profile-only/Resume-only commands MUST NOT consult Baseline time. Read/no-op/replay MUST NOT refresh business times. No logical clock/sequence or strict history order from timestamps/UUID is implied. (Q58.)

<a id="sav-006"></a>
**SAV-006.** The Application MUST prepare outside and commit in a short storage transaction with all actual participants: owned root/Version/Baseline/selection and receipt. Freshness/revision/capacity/Baseline complete-set checks MUST be protected at commit, not merely trusted from preflight. No model/network/render operation occurs inside the authority transaction. A failure MUST leave no partial publication; already committed independent Knowledge saves survive later Resume failure/cancel. M1 MUST NOT create speculative material demand/intent; M2 adds necessary actual demand intent to the owning Save transaction when consumed, never replaces it with a lossy post-commit notification. M1 exposes no generic multi-Item transaction or Import batch. (BC3/A5; Q63/Q69/Q93–Q95.)

<a id="sav-007"></a>
**SAV-007.** Remove/default admission MUST follow WSP-010/011. For RESUME_REMOVE after admitted receipt miss: check target revision; if matching and already REMOVED, return successful UNCHANGED without checking present selection revision or replacement eligibility; otherwise check selection revision even for a non-default target, then ACTIVE/default/last/replacement rules and required revision increments. Replacement syntax is still validated before receipt/no-op. Repeated EVIDENCE_RETIRE at matching revision is likewise UNCHANGED; retired content edits and removed document/name edits fail INVALID_STATE. Fresh Resume sources follow RES-011 only on new execution; replay does not recheck currentness. (Q64/Q76.)

## 3. Results, receipts and exact fingerprints

<a id="sav-008"></a>
**SAV-008.** Every success MUST contain request_id, outcome and exactly the following additional fields. outcome is CREATED for create, UPDATED for actual content/name/default changes, RETIRED/REMOVED for first respective lifecycle change, or UNCHANGED for valid no-op; replay keeps the original value, never REPLAYED.

| Commands | Additional result fields |
| --- | --- |
| PROFILE_SAVE | profile: CandidateProfile, profile_version: ProfileVersion |
| EVIDENCE_CREATE/UPDATE/RETIRE | evidence_item: EvidenceItem, evidence_item_version: EvidenceItemVersion, evidence_baseline_snapshot_id: UuidV4 |
| RESUME_CREATE/REMOVE | resume: Resume, resume_version: ResumeVersion, default_resume_selection: DefaultResumeSelection |
| RESUME_SAVE/RENAME | resume: Resume, resume_version: ResumeVersion |
| DEFAULT_RESUME_SET | default_resume_selection: DefaultResumeSelection |

Returned Version is command-time current even when no Version was created. Evidence no-op MUST capture the current Baseline at successful completion; selection results MUST capture completion-time selection. Replay after later changes MUST preserve those historical root/name/revision/Baseline/selection values, never blend in current values. These results do not prove today's current state. (Q85.)

<a id="sav-009"></a>
**SAV-009.** CandidateCommandReceipt MUST contain exactly request_id: UuidV4, command_type: one of SAV-001's nine tags, request_fingerprint: Sha256Hex, schema_version: integer 1, outcome: SAV-008 outcome, and result_snapshot with:

| Commands | Exact result_snapshot fields |
| --- | --- |
| PROFILE_SAVE | profile: complete root snapshot, profile_version_id: UuidV4 |
| EVIDENCE_CREATE/UPDATE/RETIRE | evidence_item: complete root snapshot, evidence_item_version_id: UuidV4, evidence_baseline_snapshot_id: UuidV4 |
| RESUME_CREATE/REMOVE | resume: complete root snapshot, resume_version_id: UuidV4, default_resume_selection: complete selection snapshot |
| RESUME_SAVE/RENAME | resume: complete root snapshot, resume_version_id: UuidV4 |
| DEFAULT_RESUME_SET | default_resume_selection: complete selection snapshot |

Stored root pointers MUST equal the stored result Version IDs. Reconstruct mutable values only from snapshots and immutable bodies only from exact retained references, never today's mutable root/selection. Do not copy raw request/complete immutable bodies into receipts or add receipt business revision/lifecycle. Receipt is command-result history, not editable business/current-state authority. (Q86.)

<a id="sav-010"></a>
**SAV-010.** request_fingerprint MUST be lowercase SHA-256 over UTF8("JobHunter:SL02:Command:1\n") followed immediately by encode([command_type, target_id, input]). In that prefix notation \n is exactly one LF byte; no other separator/indentation exists. Outer value is the exact three-element array, starting a3:. target_id is the canonical path ID, or null for no path identity (Profile/Create/default). input is the canonical complete body excluding request_id; include caller revisions/replacement and content, exclude generated IDs/time/result Baseline/selection.

| Value | Encoding |
| --- | --- |
| null | ASCII n |
| false / true | ASCII b0 / b1 |
| string | ASCII s + UTF-8 byte length + ASCII : + exact UTF-8 bytes |
| number | ASCII d + decimal ASCII byte length + ASCII : + canonical decimal ASCII |
| array | ASCII a + element count + ASCII : + ordered concatenated encoded elements |
| object | ASCII o + field count + ASCII : + concatenated encoded key/value pairs, keys sorted by Unicode code point |

Counts MUST be unpadded ASCII decimal integers. Numbers MUST use exact plain decimal without exponent, redundant leading zeros or trailing fractional zeros; -0 becomes 0. NaN/Infinity are invalid input, never fingerprintable admitted commands. Boolean encoding does not admit bool into numeric fields. Apply field/mark/run/color canonicalization first; preserve meaningful order/text. This protocol MUST NOT change SL-01 fingerprints. (Q87.)

<a id="sav-011"></a>
**SAV-011.** Concurrent same-key/same-fingerprint commands MUST yield at most one successful business mutation and converge on its original committed result when established. Different fingerprints cannot both succeed under that key. Storage uniqueness races MUST be safely resolved using committed receipt state, not exposed as fabricated revision conflicts. Recovery MUST be bounded and follow STO-027; no hidden business-command reexecution is authorized. Failure to establish commit outcome uses OUTCOME_UNKNOWN, not guessed rollback/success. (Q99.)

## 4. HTTP admission and errors

<a id="sav-012"></a>
**SAV-012.** S2 MUST apply WSP-008 access before business handling. POST accepts parsed application/json with compatible charset=utf-8 and actual UTF-8 body; Content-Encoding may be absent or identity only. Reject malformed encoding/JSON, duplicate decoded member names in any object, unsupported transport, non-object roots, unknown/missing fields or coercion. GET routes accept no query/body; POST accepts no query. Compatible media parameters do not require byte-identical header spelling. Read routes are PRO-007, EVD-013/014 and RES-014; all valid reads return 200. Existing SL-01 parsers/consumers are unchanged. (Q79/Q96.)

<a id="sav-013"></a>
**SAV-013.** Raw POST body admission MUST enforce: 8,388,608 bytes for Resume Create/Save; 1,048,576 for Evidence Create/Update; 65,536 for the remaining five commands. Count actual incoming bytes, not trusted Content-Length. Every request MUST have <=100,000 raw JSON value nodes (each object/array/scalar counts once including root; keys do not count) and <=32 nested object/array containers with root at depth 1. Enforce bytes while reading and depth while parsing, before canonicalization. Do not merge/deduplicate/drop/truncate input to evade budgets. Byte excess is 413 REQUEST_TOO_LARGE with []; node/depth excess is 422 VALIDATION_ERROR with STRUCTURE_TOO_COMPLEX at $, without full traversal/all-errors guarantees. Business capacities still apply separately. (Q80/Q82.)

<a id="sav-014"></a>
**SAV-014.** Errors MUST use COM-029/039/040. Non-field-specific errors use empty field_errors; input validation returns at least one accurate field error. Required phases and explicit command order apply, without a total order among all simultaneous admission failures.

| HTTP | code and trigger |
| --- | --- |
| 400 | BAD_REQUEST: malformed/unsupported encoding/media/Content-Encoding or malformed/duplicate-key JSON |
| 403 | ACCESS_DENIED: Workspace Host/Origin rejection |
| 413 | REQUEST_TOO_LARGE: raw body-byte bound |
| 422 | VALIDATION_ERROR: parseable wrong root/type/field/value, prohibited query/GET body, structural budget, supplied missing/wrong-owner refs or section/Item-kind disagreement |
| 404 | NOT_FOUND: missing path/read target; early Update target absence follows SAV-003 |
| 409 | REQUEST_CONFLICT: successfully used key with different admitted fingerprint |
| 409 | REVISION_CONFLICT: expected mutable revision mismatch |
| 409 | REVISION_EXHAUSTED: required increment beyond Common range |
| 409 | INVALID_STATE: retired content edit, removed document/name edit, inactive default/replacement |
| 409 | SOURCE_CONFLICT: newly introduced/switched source not current or new Evidence source inactive |
| 409 | LAST_RESUME_REQUIRED: removal of last ACTIVE Resume |
| 409 | CAPACITY_EXCEEDED: new ACTIVE Resume/Evidence exceeds root cap |
| 503 | STORAGE_UNAVAILABLE: storage unavailable with established non-commit for a write |
| 503 | OUTCOME_UNKNOWN: write commit cannot be established |
| 500 | INTERNAL_ERROR: sanitized internal failure, including broken stored lineage; no rollback implication |

Supplied reference failures use INVALID_REFERENCE at the corresponding path; unknown enums/formats and incompatible combinations use INVALID_FORMAT; numeric/grid/count limits OUT_OF_RANGE, text lengths TOO_LONG, blank text BLANK_VALUE and prohibited characters INVALID_CHARACTERS. Duplicate sections/members/marks and invalid month/line-height combinations use INVALID_FORMAT at the common parent/collection. Invalid Update fields are validated directly under authoritative kind, not an alternate-schema INVALID_REFERENCE. Retained historical bindings and matching lifecycle no-ops preserve their exceptions. Known internal corruption MUST NOT be misclassified as a client's missing reference. (Q89/Q96/Q97/Q98/Q100.)

## 5. Client outcomes and boundaries

<a id="sav-015"></a>
**SAV-015.** Clients MUST distinguish confirmed success (including historical replay), definite Contract rejection/proven non-commit, and uncertain outcome. Timeout, connection loss, OUTCOME_UNKNOWN or other 5xx without non-commit proof MUST remain pending verification, not a root status. Retain the complete original request/key and prevent replacing that pending operation with different intent; explicit user retry resends identical input. Do not infer success from equal current content, create a new-key duplicate or promise rollback. A rejected retry does not prove an earlier uncertain attempt uncommitted. A latest GET failure after confirmed success MUST NOT undo that success. Current state needs a separate read. (Q90/Q99.)

<a id="sav-016"></a>
**SAV-016.** M1 manual Save MUST require no model/network/Agent invocation or semantic grounding. Imported facts and Advisor mutations MUST later consume explicitly extended Contracts rather than being silently represented as nine-command batch support. Actual demand/rendering/recovery remains M2; successful source Save does not establish material or application success. Old Entry/Preferences operations and receipt namespaces MUST remain independent. (BC3/A5; Q63/Q73/Q95.)
