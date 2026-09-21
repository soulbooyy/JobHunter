# Derived Work Contract — Exact Material Demand and Local Execution

> English is authoritative. Normative scope revision: **2026-09-21.S2M2-r1**. This body defines SL-02.M2 exact-version material demand, Work and local recovery. It does not define a generic job framework, invocation recovery or future follow-current subscriptions. Documentary readiness and actual execution evidence are separate in [Progress](../../progress/traceability.md#64-sl-02m2-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Materials](../applications/materials.md) · [Common](../common.md#com-043) · [Storage](storage.md#sto-029) · [Decisions](../../design/contract/sl-02-m2-grill.md)

## 1. Scope, records and results

<a id="drw-001"></a>
**DRW-001.** A RenderIntent MUST express one immutable exact resume_version_id/render_configuration_id target. EXACT_VERSION is the only M2 mode; no mode field is added. Resume Save/current-pointer movement MUST NOT advance, obsolete or silently recreate that demand. No cancel/release command or long-lived CURRENT_RESUME subscription is provided. Each accepted command creates an independent Intent; compatible execution/output MAY be shared under later clauses. Local safe recovery MUST NOT replay model calls, browser submissions or other external effects. Q17/Q19/Q23/Q24.

<a id="drw-002"></a>
**DRW-002.** The public RenderIntent read object MUST contain exactly these eight required fields:

| Field | Type/state rule |
| --- | --- |
| render_intent_id | non-null UuidV4 |
| resume_version_id | non-null exact UuidV4 |
| render_configuration_id | non-null exact UuidV4 |
| status | non-null PENDING, FULFILLED or FAILED |
| created_at | non-null UtcTimestamp |
| finished_at | UtcTimestamp; null exactly while PENDING |
| artifact_id | UuidV4; non-null exactly while FULFILLED |
| failure_code | DRW-005 enum; non-null exactly while FAILED |

FULFILLED MUST bind exactly one published Artifact; FAILED MUST retain its stable classification. Terminal states/results MUST NOT change due to later payload loss, current pointers or client reads. PENDING has all three result fields null. Internal Work/attempt/path data is not added. Q27/Q33/Q39/Q119.

<a id="drw-003"></a>
**DRW-003.** Work MUST persist the following fifteen logical execution fields; this is not a mandated physical table layout or public API:

| Field | Type/constraint |
| --- | --- |
| work_id | non-null UuidV4 |
| resume_version_id | non-null exact UuidV4 |
| render_configuration_id | non-null exact UuidV4 |
| status | non-null QUEUED, RUNNING, SUCCEEDED or FAILED |
| attempt_count | non-null exact nonnegative integer; initially 0, <= captured max_attempts |
| max_attempts | non-null exact positive integer, captured on creation |
| max_pages | non-null exact positive integer, captured on creation |
| max_png_pixels | non-null exact positive integer, captured on creation; applies to PNG |
| max_output_bytes | non-null exact positive integer, captured on creation |
| timeout_ms | non-null exact positive integer, captured on creation |
| current_attempt_id | UuidV4; non-null exactly while RUNNING |
| created_at | non-null UtcTimestamp |
| finished_at | UtcTimestamp; non-null exactly while terminal |
| artifact_id | UuidV4; non-null exactly while SUCCEEDED |
| failure_code | DRW-005 enum; non-null exactly while FAILED |

A claim MUST atomically increment attempt_count; requeue retains it and clears current_attempt_id. Pure preflight failure retains the count, so FAILED may have zero attempts. No permanent 0–3 structural bound, recovery_policy_id/version, limit-policy object, RENDERED/PUBLISHING state or public Work object is introduced. Q34/Q44/Q48/Q53/Q54/Q94/Q117.

<a id="drw-004"></a>
**DRW-004.** An Intent directly satisfied by Artifact reuse MUST have no associated Work; an execution-backed Intent MUST associate with exactly one Work for its lifetime. Multiple Intents MAY share that Work. Recovery changes its attempt, not the Intent's Work. At most one unfinished Work exists per Workspace and exact source/configuration pair. Each SUCCEEDED Work creates exactly one Artifact; each newly published Artifact has exactly one creating Work. Reuse MUST NOT fabricate a successful Work or reassign an Artifact's creator.

Intent/Work exact targets MUST agree, fulfilling Manifest targets MUST agree with Intent, and execution-backed terminal results MUST agree with Work. Required relationship contradictions are integrity errors, not GET-time repairs. No general many-to-many dependency entity is required. Q28/Q110/Q111/Q116.

<a id="drw-005"></a>
**DRW-005.** FAILED Work and Intent MUST use this closed terminal failure_code vocabulary, distinct from HTTP error codes and raw exception text:

| Code | Execution result |
| --- | --- |
| SOURCE_UNAVAILABLE | Required exact historical input is confirmed missing/corrupt; unused lineage payload is not a prerequisite |
| CONFIGURATION_UNAVAILABLE | Required execution/font support cannot be used |
| PERMISSION_DENIED | Required execution permission is no longer satisfied |
| RENDER_FAILED | Renderer explicitly reports an execution failure |
| OUTPUT_INVALID | Candidate output violates required format/integrity/conformance |
| RESOURCE_LIMIT_EXCEEDED | Applicable execution/dimension/resource limit is exceeded |
| STORAGE_FAILED | Required execution storage reads or writes fail |
| RECOVERY_EXHAUSTED | Interrupted execution cannot obtain another permitted claim |
| INTERNAL_ERROR | Contradictory persisted relationships or unexpected internal failure |

Preserve a determined primary failure when later temporary-file cleanup fails; sanitized diagnostics/deferred cleanup MUST NOT overwrite it. If the result cannot commit, no durable terminal result may be claimed. Q38/Q108/Q125.

## 2. Commands, receipts and atomic acceptance

<a id="drw-006"></a>
**DRW-006.** POST /api/v1/render-intents MUST accept exactly request_id, resume_version_id and render_configuration_id, all non-null UuidV4. request_id is the client command key; all source root/Profile/Evidence refs are derived server-side. The operation is RENDER_REQUEST, not a caller-writable field. After successful atomic acceptance, return HTTP 200 with exactly request_id, outcome = ACCEPTED, render_intent_id. This same three-field result applies even for immediate Artifact reuse; no current readiness, Work ID or Artifact ID is added. Q1/Q7/Q22/Q26.

<a id="drw-007"></a>
**DRW-007.** request_fingerprint MUST be lowercase SHA-256 over UTF8("JobHunter:SL02:Materials:1\n") followed immediately by the COM-045 encoding of ["RENDER_REQUEST", null, input], where input contains exactly admitted resume_version_id and render_configuration_id. Here \n denotes one LF byte, not two literal characters. Exclude request_id and all generated values. Preserve SAV-010 and all SL-01 prefixes/fingerprints. Different JSON key ordering/formatting MUST NOT change admitted command equality. Q5/Q76.

<a id="drw-008"></a>
**DRW-008.** The Workspace Materials receipt key MUST be (operation, request_id), independent of Candidate Save and SL-01 namespaces; identical UUID text in another namespace does not conflict. Each successful receipt MUST contain exactly request_id: UuidV4, operation: RENDER_REQUEST, request_fingerprint: Sha256Hex, schema_version: integer 1, and result_snapshot: DRW-006's original complete acceptance. All are required/non-null; inner/outer request_id MUST agree. No receipt timestamp or mutable Work status is added.

Retain successful receipts for the Workspace lifetime without TTL. The snapshot MUST reference the Intent created by that acceptance; its exact target encoded under DRW-007 MUST match the receipt fingerprint. This does not require replay to traverse the Work/Artifact chain. Same key/equal input MUST return the original committed snapshot, never reconstruct current readiness; different input conflicts. Missing later bytes MUST NOT delete the receipt or rewrite replay. Detected receipt corruption MUST NOT become a miss. Q5/Q10/Q88/Q133.

<a id="drw-009"></a>
**DRW-009.** Processing MUST enforce current local access/raw transport, closed field/type/value admission and fingerprint before receipt lookup. A matching valid receipt replays before new-generation lifecycle/source/configuration checks; it may replay after Resume removal or configuration unavailability. On a receipt miss, resolve exact Resume/root, require ACTIVE root, resolve/validate actual required historical render sources, resolve exact configuration, then check its current execution support, in that order. Missing client-supplied source/configuration IDs are INVALID_REFERENCE; detected broken required stored refs are INTERNAL_ERROR. Do not rerequire Evidence ACTIVE/current or unused body payloads.

Only if subsequent selection needs a new Work, validate the necessary current limit defaults; invalid positive-integer defaults yield 500 INTERNAL_ERROR with no committed Intent/receipt/Work, without fallback. Reuse, original replay and valid existing Work snapshots remain unaffected. Q14/Q15/Q67/Q126.

<a id="drw-010"></a>
**DRW-010.** One acceptance transaction MUST commit receipt, new Intent and exactly one disposition: bind a verified reusable Artifact and fulfill immediately; associate with compatible unfinished Work; or create new Work with captured limits and associate with it. Selection follows MAT-016's Artifact-first/Work-second/new-Work order. Committing Intent before Work creation in a later step is forbidden. Rendering is post-commit; in-memory notifications do not establish durable execution. Joining Work MUST NOT replace its captured limits. Q25/Q32/Q53/Q94/Q118.

<a id="drw-011"></a>
**DRW-011.** Concurrent same Materials key/equal fingerprint MUST converge on at most one accepted Intent and its original result; different fingerprints cannot both succeed. Resolve storage uniqueness races from committed receipt state, not fabricated lifecycle errors. Unfinished-Work uniqueness MUST be enforced atomically for its exact pair.

Joining and terminal publication/failure MUST have a defined concurrent order. A join committed first is included in terminal propagation; a terminal commit first requires the new acceptance to repeat selection, never attach PENDING demand to terminal Work. No failed Work is reopened. Uncertain commits follow DRW-017, not hidden new-key command reexecution. Q28/Q32/Q41 and inherited SAV-011 receipt semantics.

<a id="drw-012"></a>
**DRW-012.** One logical transaction event MUST use one server UtcTimestamp. New Intent and newly created Work share created_at. Immediate reuse gives Intent equal created_at/finished_at without altering Artifact.created_at. Successful publication gives Artifact.created_at and Work/newly fulfilled Intents' finished_at the same value. Failure gives Work/newly failed Intents the same finished_at. These are logical event times, not precise flush timestamps; historical values and identity chronology MUST NOT be inferred or rewritten. Q49.

## 3. Execution, fencing and recovery

<a id="drw-013"></a>
**DRW-013.** Before a claim, the Coordinator MUST check current configuration execution dependencies. If preflight establishes that they are unavailable, atomically fail QUEUED Work and every PENDING dependent Intent with CONFIGURATION_UNAVAILABLE, conditional on work_id, status = QUEUED and the observed attempt_count. Do not increment the count or create an attempt. If that condition loses a race, reread; an old preflight MUST NOT terminate a newly claimed or requeued execution.

Otherwise a claim MUST atomically require QUEUED and attempt_count < max_attempts, generate a new attempt_id, increment count and enter RUNNING. A later dependency loss fails under that RUNNING attempt's fence. Capability loss MUST NOT strand accepted Work forever in QUEUED. No claim-before-preflight requirement or revision field is introduced. Q43/Q54/Q117/Q124.

<a id="drw-014"></a>
**DRW-014.** Only the Coordinator MAY publish success after candidate validation and durable file preparation under STO-034. In one database transaction it MUST condition on current work_id, current_attempt_id and RUNNING, verify the attempt remains within its execution budget and required permissions/provenance, publish Artifact/Manifest, mark Work SUCCEEDED, and fulfill all still-PENDING associated Intents with that Artifact. Clear current_attempt_id and set terminal fields atomically. Bytes alone, internal reserved IDs or prepared paths do not establish publication.

Ordinary current-pointer movement/removal or loss of new-generation capability MUST NOT reject already lawful completed bytes merely as stale. Required execution dependencies actually lost before completion still fail explicitly. A stale/timed-out attempt MUST NOT publish or finish Intents. Q12/Q23/Q35/Q43/Q68/Q84/Q85.

<a id="drw-015"></a>
**DRW-015.** Failure of a RUNNING attempt MUST match work_id, attempt_id and RUNNING, then atomically mark Work and every PENDING associated Intent FAILED with stable failure_code/time and clear current_attempt_id. Queued preflight failure follows its separate DRW-013 condition. Do not commit Work failure and finish dependent Intents later. A reported renderer failure is terminal, not automatically retried because claims remain. Preserve primary failure against cleanup faults and reconcile uncertain terminal writes under DRW-017. Q29/Q40/Q43/Q108/Q117.

<a id="drw-016"></a>
**DRW-016.** Persisted QUEUED Work MUST be rediscoverable at startup and during operation; a queue/callback/wakeup is only an optimization. Before recovering RUNNING Work, the Coordinator MUST acquire Storage's physical-directory runtime ownership, recognize the store and establish/fence the prior publisher; PID, file existence or elapsed time alone is insufficient. Reconcile any committed terminal result first. If no terminal result exists, recover by a fresh attempt within captured max_attempts, retaining counts; if exhausted, commit RECOVERY_EXHAUSTED and dependent failures atomically under the owned recovery condition. Do not reopen terminal Work, reset counts, resume partial output or register an unpublished orphan as a successful Artifact.

A known renderer failure MUST NOT be retried while the Coordinator retains it. If a crash loses that volatile failure before reliable terminal persistence, actual unfinished stored state is interruption evidence; bounded recovery may execute again. No second authoritative failure journal is introduced. Q42/Q44/Q45/Q81/Q107/Q109.

<a id="drw-017"></a>
**DRW-017.** If acceptance or terminal commit outcome cannot be established, preserve the uncertainty and read durable receipt/result state before more execution/publication. Do not assume a transiently absent observation proves non-commit, manufacture rollback or reexecute a successful command. A confirmed terminal result is used as stored; unavailable storage remains an unknown outcome rather than guessed failure/success. Prepared files are retained when references/commit status are uncertain. Terminal-state uncertainty MUST NOT trigger duplicate rendering/publication. Q15/Q40/Q45/Q104/Q109.

<a id="drw-018"></a>
**DRW-018.** Capture only the needed max_attempts, max_pages, max_png_pixels, max_output_bytes and timeout_ms scalars on Work creation, in acceptance's transaction. They MUST remain fixed across recovery; changed defaults affect only new Work. Each attempt's monotonic elapsed-time budget starts after claim commit and covers source preparation, rendering, validation and the prepublication terminal decision, excluding queue wait. Recovery receives a fresh interval with the same captured timeout. PNG pixels count the complete assembled image; other applicable limits remain independently enforced. Do not silently grant retries different execution constraints or change configuration/output to fit limits. Q53/Q54/Q91/Q94/Q95.

<a id="drw-019"></a>
**DRW-019.** On timeout, the current attempt MUST lose publication eligibility and atomically fail Work/PENDING Intents with RESOURCE_LIMIT_EXCEEDED under the matching fence. Success checks the same budget before its terminal decision; the terminal winner is not overwritten. If the adopted execution model supports isolated termination, terminate the timed-out execution. In-process execution MUST NOT promise unsupported forcible killing.

Until renderer exit/termination is established, it still occupies execution resources and its attempt paths remain isolated; logical FAILED is not proof of physical exit. Do not start unbounded replacements or delete live-writer files because the logical result is terminal. Q83/Q85/Q86.

<a id="drw-020"></a>
**DRW-020.** The accepted initial implementation defaults are max_attempts = 3 and executor concurrency = 1. An initial HTTP body limit of 4 KiB MAY be used. These defaults may be adjusted later without changing the Contract schema or its permanent bounds. Concurrency changes MUST preserve unfinished-Work uniqueness, conditional claims, attempt fencing and atomic propagation. Q44/Q48/Q82/Q87. This scope defines no distributed lease, generic policy entity, public scheduler tuning API or external queue requirement.

## 4. HTTP, clients and evidence

<a id="drw-021"></a>
**DRW-021.** GET /api/v1/render-intents/{render_intent_id} MUST return 200 with one coherent DRW-002 snapshot after current local access checks. It MUST NOT recover, execute, retry or repair Work. Ordinary Resume removal or new-generation configuration unavailability MUST NOT hide its retained result. FULFILLED MUST NOT be returned without its published artifact_id, but it is not a claim of current byte availability. Q20/Q33/Q39.

<a id="drw-022"></a>
**DRW-022.** All six M2 operations MUST apply WSP-012 local access before business handling. POST requires compatible application/json UTF-8 and absent/identity Content-Encoding, with a finite actual-byte body limit enforced before receipt lookup; do not trust Content-Length alone. Reject malformed JSON/encoding, duplicate decoded JSON keys, unsupported transport and closed-shape violations without coercion. POST accepts no query. GET accepts no body; only content GET admits its single optional disposition. Repeated disposition, even equal, is invalid. Parsed wrong root/type/field/value and prohibited query/body use field validation; no endpoint silently strips extras. Existing M1/SL-01 parsers and budgets remain unchanged. Q87/Q120/Q131.

<a id="drw-023"></a>
**DRW-023.** Errors MUST use COM-029/039/043–046, with empty field_errors when not field-specific and at least one accurate field error for validation. Required phase ordering applies; no exhaustive all-errors response or total order among simultaneous same-phase failures is promised.

| HTTP | Trigger/code |
| --- | --- |
| 400 | BAD_REQUEST: malformed/unsupported transport or malformed/duplicate-key JSON |
| 403 | ACCESS_DENIED: current local access boundary |
| 413 | REQUEST_TOO_LARGE: configured actual-byte request limit |
| 422 | VALIDATION_ERROR: admitted parsing but invalid root/fields/types/values, prohibited query/body, invalid-format path ID, invalid/repeated disposition; supplied absent source/config ID uses INVALID_REFERENCE |
| 404 | NOT_FOUND: valid-format requested GET resource absent |
| 409 | REQUEST_CONFLICT: same command key/different input; INVALID_STATE: new demand's Resume removed; RENDER_CONFIGURATION_UNAVAILABLE: retained configuration cannot admit new generation |
| 503 | STORAGE_UNAVAILABLE: unavailable storage, with write non-commit established when rejecting a write; OUTCOME_UNKNOWN: commit not established |
| 500 | INTERNAL_ERROR: detected required metadata/reference corruption, invalid defaults when new Work is necessary, or unexpected internal failure |

Content-specific availability/integrity mappings are MAT-027. Detected internal corruption MUST NOT be mislabeled as a missing client-supplied reference. A 5xx alone MUST NOT be treated as rollback evidence. Q15/Q77/Q78/Q126/Q131.

<a id="drw-024"></a>
**DRW-024.** After timeout/disconnection/OUTCOME_UNKNOWN, clients MUST retain request_id and both exact target IDs, retry the identical command for confirmation and avoid automatic new-key duplicate demand. A rejected retry or temporary absence does not prove the earlier attempt uncommitted. Once acceptance is confirmed, query its original Intent rather than reinterpret a replay as current readiness; an explicit new generation after terminal failure uses a new command.

Client state MUST be isolated by render_intent_id. A late PENDING response MUST NOT overwrite an already observed terminal result; responses for another Intent MUST NOT replace the selected Intent's state. Download failure MUST be displayed separately from fulfillment. No public revision is added. Q5/Q10/Q104/Q119.

<a id="drw-025"></a>
**DRW-025.** Intent, terminal Work and necessary association/result records MUST be retained without first-release TTL or automatic deletion. A new command after failed execution creates a new Intent and, when required, new Work; it MUST NOT overwrite prior Work with the same compatibility key. Explicit cancel/release and public retry/history/repair/Work APIs remain absent. Receipt retention and Artifact payload semantics remain separately owned. Q24/Q92/Q110/Q120.

<a id="drw-026"></a>
**DRW-026.** Implementation conformance MUST cover complete acceptance's three branches, same-key and same-target races, lost wakeups, queued preflight versus claim/join, old-attempt fencing, success/failure fan-out, uncertain commits, restart exhaustion, live-writer cleanup and post-removal historical completion. Work uniqueness and publication guarantees MUST hold beyond concurrency 1. Tests MUST distinguish documentary approval, installed upstream capability, renderer capability evidence and actual acceptance; no design default or published requirement proves execution. See [Acceptance §4.3](../../acceptance.md#43-demand-and-safe-derivative-recovery) and MAT-030. Q32/Q41–Q45/Q81–Q86/Q107–Q109/Q117/Q124/Q128.
