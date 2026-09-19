# ManualApplicationEntry Contract

> English is authoritative. Normative scope revision: **2026-09-19.M1-r1**. Consumer: SL-01.M1. This document owns the independent mutable entry, its commands, HTTP interface and browser-only effect. Formal Job/JobVersion semantics remain with the planned `jobs/jobs-screening.md`. See [scope readiness](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger) for actual review state.

[Index](../index.md) · [Common](../common.md) · [Workspace](../foundation/workspace.md) · [Storage](../foundation/storage.md) · [Decision register](../../design/contract/sl-01-m1-grill.md)

## 1. Record and admission

<a id="mae-001"></a>
**MAE-001.** `ManualApplicationEntry` MUST remain outside the formal Job family. Its only business purpose is maintaining user-provided company/role/application destinations and explicitly navigating to one. It MUST NOT produce a JobVersion, accept JD, participate in Requirements/Fits/targeted Advisor/Preparation/automatic Execution/Application History, or turn navigation into an application fact, approval consumption or implicit collection.

<a id="mae-002"></a>
**MAE-002.** A complete entry MUST contain exactly these seven required non-null fields. Common owns the referenced scalar types.

| Field | Type | Authority |
| --- | --- | --- |
| `manual_application_entry_id` | `UuidV4` | Backend-generated; stable and immutable |
| `company_name` | `UnicodeText`, MAE-003 | User through whole-record Save |
| `role_title` | `UnicodeText`, MAE-003 | User through whole-record Save |
| `application_url` | `UnicodeText`, MAE-004 | User through whole-record Save |
| `revision` | `Revision` | Backend; starts at 1 |
| `created_at` | `UtcTimestamp` | Backend; immutable creation time |
| `updated_at` | `UtcTimestamp` | Backend; MAE-006 |

There is no entry `status`, `workspace_id`, `schema_version`, business-version ID, `request_id`, click count or last-opened time. Request identity belongs to the create command/receipt.

<a id="mae-003"></a>
**MAE-003.** Company/role inputs MUST be valid scalar text, pass COM-026 outer trim, then contain 1–200 code points on one line with no remaining control or line/paragraph separator characters. Internal spacing, case, punctuation and Unicode representation MUST be preserved. Invalid/oversized input MUST be rejected, not truncated or repaired.

<a id="mae-004"></a>
**MAE-004.** `application_url` MUST be scalar text trimmed by COM-026, nonempty and at most 8192 code points. It MUST be an absolute HTTP(S) URL with an explicit `http://` or `https://` authority delimiter, a nonempty valid host and no userinfo/embedded credentials. Scheme comparison is case-insensitive; original spelling is preserved. Remaining controls, COM-026 whitespace, backslashes, userinfo delimiters in the authority and non-HTTP(S) schemes MUST be rejected. Validity means a [valid absolute-URL-with-fragment string under this pinned WHATWG snapshot](https://url.spec.whatwg.org/commit-snapshots/8e14777cfa145b08a9fb735fe580ec0c366564c3/#url-writing): parsing with no base MUST produce neither failure nor validation errors. A parser that silently repairs malformed input is insufficient. Each literal `%` MUST be followed by two ASCII hexadecimal digits. An explicit port MUST be nonempty decimal in `0..65535`. Unicode host/path input is allowed under the pinned definition; no network/DNS check is performed. Localhost/IP destinations are not forbidden merely for lacking a public domain.

The stored/returned value MUST be the trimmed admitted input, not the parser's serialized/punycode/trailing-slash-normalized form. Path/query/fragment, escaping and case MUST NOT be rewritten. Saving MUST NOT fetch the address, check page availability, infer a scheme or guess another destination. Browser transport encoding and later site redirects do not rewrite the saved record.

<a id="mae-005"></a>
**MAE-005.** The backend MUST generate an entry UUIDv4 without business meaning and prevent reuse of an identity retained in create receipts. Equal company/role/URL values and equal fingerprints MUST NOT block intentional creation or merge records. M1 requires no duplicate-warning feature. A distinct intentional creation MUST use a new frontend-generated `request_id`; a retry MUST reuse the original request identity/content.

<a id="mae-006"></a>
**MAE-006.** Successful creation MUST set revision 1 and equal creation/modification times. An actual committed content change MUST increment revision by one and set `updated_at = max(current_UTC_millisecond_time, prior_updated_at)` in the same transaction. `created_at` MUST stay fixed. Equal effective content MUST leave revision and both timestamps unchanged. Opening MUST leave all fields unchanged. Same-millisecond times are permitted; revision orders this record's changes. Implementations MUST NOT introduce a logical clock or fabricate millisecond increments to order records. Cross-record chronology during clock rollback is not guaranteed.

## 2. Commands and reads

The field sets below are complete logical interfaces. MAE-015 maps identity to an HTTP path where appropriate. Admission uses COM-031 and MAE-003/004 before execution; syntactically invalid payloads cannot acquire a receipt merely because they contain an existing request ID.

<a id="mae-007"></a>
**MAE-007.** `CreateManualApplicationEntry` MUST accept `request_id`, `company_name`, `role_title`, `application_url`, and return only `{manual_application_entry_id}` on success. Under atomic storage admission:

1. No receipt for this admitted request: generate a new identity and atomically persist the entry and its receipt.
2. Receipt with a different admitted-content fingerprint: reject `REQUEST_CONFLICT` without mutation.
3. Same fingerprint, original entry still exists: return its original identity, even if its mutable content has subsequently changed. The current content is obtained by a separate read.
4. Same fingerprint, original entry deleted: return `ORIGINAL_ENTRY_DELETED`; do not recreate it.

Concurrent repetitions MUST converge on one receipt/original identity. Only successful creation writes a receipt. The receipt is not an original-content snapshot, and replay MUST NOT update the entry or its timestamps.

<a id="mae-008"></a>
**MAE-008.** The create receipt MUST contain exactly `request_id: UuidV4`, `request_fingerprint: Sha256Hex`, `manual_application_entry_id: UuidV4`. Compute the fingerprint from this exact byte sequence, excluding request ID, generated identity, revision and timestamps:

```text
UTF8("ManualApplicationEntryCreate:v1") || 0x00 ||
u32be(len(UTF8(company_name)))    || UTF8(company_name) ||
u32be(len(UTF8(role_title)))      || UTF8(role_title)   ||
u32be(len(UTF8(application_url))) || UTF8(application_url)
```

Values are the admitted post-trim strings. `len` means bytes; each prefix is four unsigned big-endian bytes. SHA-256 is emitted as lowercase hexadecimal. Storage retains receipts under STO-010 independently of business deletion; it MUST NOT retain the three original business strings in them.

<a id="mae-009"></a>
**MAE-009.** `GetManualApplicationEntry` MUST accept an entry ID and return a complete entry or `NOT_FOUND`. `ListManualApplicationEntries` MUST return `{items: ManualApplicationEntry[]}`, including every current entry and no formal Job, sorted by `updated_at` descending and entry ID lexicographically ascending on ties. Empty means `items: []`. M1 MUST NOT silently truncate, paginate or accept search/filter/custom-sort parameters. Each read MUST satisfy STO-009 consistency; later writes do not invalidate the fact that a returned revision was observed.

<a id="mae-010"></a>
**MAE-010.** `UpdateManualApplicationEntry` MUST accept ID, expected `revision` and all three business fields, and return the complete saved entry. There is no partial update. The operation MUST validate input first, then check existence, then expected revision, then exact equality of the three admitted strings. Missing returns `NOT_FOUND`; stale revision returns `REVISION_CONFLICT`, including equal-content stale submissions. A valid equal-content save returns the original record unchanged. A real change at maximum revision returns `REVISION_EXHAUSTED`. Otherwise apply MAE-006 atomically. Update MUST NOT recreate a deleted entry.

<a id="mae-011"></a>
**MAE-011.** `DeleteManualApplicationEntry` MUST accept ID and expected revision. After validation, it MUST check existence, then revision, and atomically physically remove the business row. Success returns `{manual_application_entry_id}`. Missing returns `NOT_FOUND`; stale revision returns `REVISION_CONFLICT`. It MUST NOT retain a hidden entry, recycle-bin row or edit/version history, or delete/clear its create receipt. Deliberate re-addition is a new creation. Retrying an already completed deletion returns `NOT_FOUND`.

<a id="mae-012"></a>
**MAE-012.** `ResolveManualApplicationEntryUrl` MUST accept ID and expected revision and return exactly `{application_url}` from one consistent saved record. Validate existence before revision; reject missing/stale targets using `NOT_FOUND`/`REVISION_CONFLICT`. It MUST NOT fall back to a stale cached/unsaved address, update any record or hold a transaction across browser interaction. A change/deletion after successful resolution does not recall the resolved navigation; this is not an Execution lease.

## 3. Browser and client semantics

<a id="mae-013"></a>
**MAE-013.** An explicit click MUST request a neutral waiting browsing context through user activation, then asynchronously resolve ID/revision under MAE-012 when the context is available. Only a successful resolution permits navigation of that waiting context to the returned URL. Failed resolution MUST cause no external navigation; the waiting context closes or shows failure. A blocked/closed waiting context MUST be reported without automatically opening another; a new click rechecks the entry. Failure reporting MUST describe only observable inability to complete handoff, not infer a particular popup-blocker cause from a null handle alone.

Before external content gains control, it MUST NOT retain a usable opener relationship and MUST NOT receive referrer information. Implementations MAY use waiting-page self-resolution/self-navigation or same-origin coordination; this Contract does not mandate a particular `window.open` feature string or opener API sequence. Success text MUST mean only that the validated external navigation has actually been initiated. Creating a waiting page is not success. UI MUST NOT say “successfully opened”, “loaded” or “applied”. The product requests a new tab, subject to browser presentation settings. No automatic background retry, application event or click persistence is allowed.

<a id="mae-014"></a>
**MAE-014.** Client recovery MUST distinguish known command rejection from uncertain commit. Timeout, connection loss, `OUTCOME_UNKNOWN` and an otherwise ambiguous write 5xx require verification. A valid 4xx Contract rejection is definite rejection of the current operation, not proof that an earlier replayed creation never existed. `STORAGE_UNAVAILABLE` for a mutation denotes confirmed non-commit under STO-008; an unrecognized/malformed response is not proof of rollback.

For uncertain create, the current page MUST retain the exact submitted request/content in memory and use it for an explicit verify/retry action without a fresh request ID. For update/delete it MUST read current state without automatically resubmitting at a fresh revision. Current reads MUST NOT be described as reconstructing all intervening history or overwrite dirty editor content. M1 MUST NOT introduce a persisted command queue or promise refresh/browser-restart recovery. After losing page state, prompt list inspection; do not automatically recreate.

## 4. HTTP interface

<a id="mae-015"></a>
**MAE-015.** The local API MUST use JSON at `/api/v1/manual-application-entries`. All listed success responses are HTTP 200 with the exact result object below, without an additional `data`/`success` envelope. Path identity MUST NOT be repeated in the body. GET operations take no body/query options; command objects reject extra fields.

| Operation | Method / path suffix | Request body | Result type |
| --- | --- | --- | --- |
| Create | `POST` base | `request_id`, `company_name`, `role_title`, `application_url` | `ManualApplicationEntryIdentity`: entry ID only |
| List | `GET` base | None | `ManualApplicationEntryList`: `items` of complete entries |
| Read | `GET /{manual_application_entry_id}` | None | `ManualApplicationEntry` |
| Update | `PUT /{manual_application_entry_id}` | `revision`, all three business fields | `ManualApplicationEntry` |
| Delete | `POST /{manual_application_entry_id}/delete` | `revision` | `ManualApplicationEntryIdentity` |
| Resolve | `POST /{manual_application_entry_id}/resolve-url` | `revision` | `ManualApplicationEntryUrl`: `application_url` only |

<a id="mae-016"></a>
**MAE-016.** Owned operation failures MUST emit COM-029 `ContractError` with this mapping; field details use COM-030. Known pre-commit rejections MUST leave business data and receipts unchanged. A response-construction/delivery failure after commit MUST NOT be reported as proof of non-commit: return the authoritative success when recoverable, otherwise require verification under MAE-014/STO-008. A generic exception handler MUST NOT certify rollback merely because code raised. Error handling itself MUST NOT introduce further mutations.

| Code | HTTP | Meaning / recovery |
| --- | --- | --- |
| `BAD_REQUEST` | 400 | Unparseable JSON or malformed transport request; correct request |
| `VALIDATION_ERROR` | 422 | Body/path/query field admission failure; correct fields |
| `NOT_FOUND` | 404 | Ordinary target read/mutation/resolution absent |
| `REVISION_CONFLICT` | 409 | Stale caller revision; inspect current record without overwriting edits |
| `REQUEST_CONFLICT` | 409 | Admitted create content differs under the same request key |
| `ORIGINAL_ENTRY_DELETED` | 409 | Matching create replay identifies a physically deleted original; no resurrection |
| `REVISION_EXHAUSTED` | 409 | Real change would exceed revision range; valid no-op remains possible |
| `STORAGE_UNAVAILABLE` | 503 | Storage failed; mutation non-commit is confirmed |
| `OUTCOME_UNKNOWN` | 503 | Mutation commit cannot be determined; MAE-014 applies |
| `INTERNAL_ERROR` | 500 | Unexpected error; an uncertain mutation instead follows STO-008/MAE-014 |

Runtime Host/Origin rejection is owned separately by WSP-006. `OUTCOME_UNKNOWN` MUST NOT be added to the Entry field set or any Entry state machine.

<a id="mae-017"></a>
**MAE-017.** Explicit Save MUST validate/persist all three business fields atomically before they become saved authority. Unsaved edits MUST NOT change the list's saved data or navigation target. A known failed Save MUST preserve current editor input and the prior stored row; an uncertain Save follows MAE-014 without claiming the row is unchanged. There is no per-field autosave, immutable entry history or crash-recoverable draft promise. UI caches/optimistic presentation MUST NOT be represented as durable success.

<a id="mae-018"></a>
**MAE-018.** Server, generated client and frontend validation MUST preserve Common/Entry semantics rather than inherit incompatible coercion, extra-field stripping, URL normalization, character counting or retry behavior. The server remains authoritative. The browser boundary MUST satisfy WSP-006 and Storage privacy; ordinary navigation MUST NOT require the automated browser Executor or live recruiting-account integration.

## 5. Required conformance examples

These illustrate the cited rules; [Acceptance](../../acceptance.md#31-sl-01m1-contract-conformance) owns the required proof plan.

| Input / event | Required result |
| --- | --- |
| Missing `role_title` versus `role_title: null` | `REQUIRED` versus `INVALID_TYPE` |
| `" Acme "` versus `"Acme"`; `"ACME"` versus `"Acme"` | Equal effective text in the first case only |
| One supplementary Unicode character | Counts as one code point, not two UTF-16 units |
| Outer `U+0085` versus `U+FEFF` | First is trimmed; second is preserved, not silently treated as trim whitespace |
| `https://example.test/apply?q=one%20two#step` | Exact post-trim spelling saved and returned |
| `HTTP://Example.test:80/./apply`, `http://localhost`, `http://[::1]/` | Valid input spelling preserved; serialization equality is not a validation rule |
| `example.test`, `javascript:alert(1)`, `https://u:p@example.test/` | Rejected without repair or fetch |
| `https:////example.test`, `http://127.1/`, `https://example.test:/`, `/bad%zz` in a URL path | Invalid authority/IP/port/percent syntax rejected, not repaired |
| Valid URL longer than 2083, at most 8192 code points | Not rejected by an unrelated library default |
| Same request after edit / after deletion | Original identity / `ORIGINAL_ENTRY_DELETED`; no additional entry |
| Stale revision with equal fields | `REVISION_CONFLICT` |
| No-op at maximum revision | Original record unchanged |
| Failed or blocked waiting page | No external navigation, no automatic replacement, no business state change |

No requirements are retired in this initial scope. Provenance: CG01-BC1, Q11–Q18, Q20–Q23, Q27–Q37, Q39–Q45. Physical schema/commit/retention definitions are owned by Storage, not duplicated here.
