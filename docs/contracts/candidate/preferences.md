# Preferences Contract — Collection Intent and Immutable Versions

> English is authoritative. Normative scope revision: **2026-09-20.M2-r1**. Scope: SL-01.M2 configuration, persistence-facing objects, read/Save and recovery. This does not complete Collection/source admission or Job Pool queries. Readiness and implementation are separate in [Progress](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger).

[Index](../index.md) · [Common](../common.md) · [Workspace](../foundation/workspace.md) · [Storage](../foundation/storage.md) · [Decisions](../../design/contract/sl-01-m2-grill.md)

## 1. Authority and configuration

<a id="prf-001"></a>
**PRF-001.** One global PreferenceSet MUST express user-confirmed intent for future automatic Collection. It MUST NOT continuously screen, hide, delete or disqualify saved formal Jobs or gate their Fit/Preparation eligibility. A Collection consumer MUST freeze a complete exact PreferenceSetVersion; later Save MUST NOT alter a running consumer's input or start/restart collection. Job Pool query filters MUST remain independent, with no Preference writes. M2 MUST NOT supply QuickScreen or source query/admission logic. ManualApplicationEntry remains independent.

<a id="prf-002"></a>
**PRF-002.** PreferenceConfiguration MUST contain exactly the six required fields below. Missing, null, blank and empty collections MUST NOT imply an unrestricted choice. Five fields use exactly `{mode: UNLIMITED}` or `{mode: LIMITED, value: ...}`; these are object descriptions, not literal unquoted JSON. Mode/value are case-sensitive. UNLIMITED forbids value even when null or empty. LIMITED requires a valid concrete value. Keywords have no UNLIMITED form. Only complete valid successful Save establishes configured state.

| Field | Required representation | Meaning |
| --- | --- | --- |
| target_job_keywords | Nonempty array of strings | User-maintained search terms for future Collection; not a literal Job-title eligibility predicate |
| accepted_cities | Choice; LIMITED value is nonempty string array | Accepted work cities; no inferred neighboring city/district/commuting region |
| minimum_salary | Choice; LIMITED value is integer | Minimum CNY pre-tax monthly base pay, excluding bonus, equity, extra salary months and annual/daily conversion |
| recruitment_types | Choice; LIMITED value is nonempty enum array | Desired campus/internship/experienced/part-time opportunities; source categories need not be mutually exclusive |
| excluded_companies | Choice; LIMITED value is nonempty string array | Company display names to exclude; future name comparison uses the defined canonical full name, not substring/fuzzy/group inference |
| max_required_education | Choice; LIMITED value is one enum | Upper bound on the Job's required education, not the candidate's own attainment |

<a id="prf-003"></a>
**PRF-003.** Keyword, city and company items MUST use Common UnicodeText, fixed outer whitespace trim and code-point length. Validate scalar legality, then trim; reject blank results and any remaining Common control/line/paragraph separator. Do not case-fold, Unicode-normalize, width-convert, collapse internal spaces, strip company suffixes, resolve aliases, split commas or infer synonyms. Commas inside an item remain literal. Source/platform interpretation remains outside this Contract; Collection MUST NOT reject a returned title solely because it lacks a submitted search term, or silently expand user terms into synonyms in v1.

<a id="prf-004"></a>
**PRF-004.** The four multivalue fields MUST be unordered sets. Validate every submitted item before deduplication; one invalid item rejects the entire Save. Deduplicate by exact canonical value, check canonical capacities, then sort text lexicographically by Unicode code points and recruitment types by PRF-006's declared order. Locale/UTF-16 sorting MUST NOT substitute for code-point order. Order/duplicate-only changes in admitted requests MUST NOT create a version or increment revision. Raw input admission limits in PRF-016 apply before these rules.

| Field | Maximum canonical item count | Each trimmed text item's code-point length |
| --- | --- | --- |
| target_job_keywords | 20 | 1–100 |
| accepted_cities LIMITED value | 50 | 1–100 |
| excluded_companies LIMITED value | 200 | 1–200 |
| recruitment_types LIMITED value | 4 | Exact enum only |

Keywords and every LIMITED set MUST contain at least one canonical item; no truncation is allowed.

<a id="prf-005"></a>
**PRF-005.** LIMITED minimum_salary MUST be a JSON number with exact integer value in inclusive range 1–300000. Strings, Booleans, null and fractional values produce INVALID_TYPE; out-of-range integer values produce OUT_OF_RANGE. No rounding/coercion is permitted. `15000`, `15000.0` and `1.5e4` are equivalent admitted values. The UI integer-entry convention does not restrict JSON number spelling. Salary comparison against source ranges and uncertain/incomparable source salaries belong to future Collection admission, not M2.

<a id="prf-006"></a>
**PRF-006.** RecruitmentType MUST have exactly CAMPUS, INTERNSHIP, EXPERIENCED, PART_TIME, in that canonical serialization order. RequiredEducation MUST have exactly the following ascending order: JUNIOR_HIGH_OR_BELOW, UPPER_SECONDARY, ASSOCIATE, BACHELOR, MASTER, DOCTORATE. UPPER_SECONDARY groups high school and secondary vocational/technical education. UNLIMITED is a choice mode, not a member of either enum. Platform parameter mappings, absent/foreign/complex source education interpretation and recruitment parsing remain Collection/adapter responsibilities.

## 2. Saved objects and publication

<a id="prf-007"></a>
**PRF-007.** The following business objects MUST have exactly these required, non-null fields. Configuration is shared with PRF-002. IDs use Common UuidV4; revision uses Common Revision; timestamps use Common UtcTimestamp. IDs/times are generated by the system, not caller-writable.

| Object | Fields |
| --- | --- |
| PreferenceSet | preference_set_id, current_preference_set_version_id, revision, created_at, updated_at |
| PreferenceSetVersion | preference_set_version_id, preference_set_id, created_at, configuration |

Root MUST NOT duplicate configuration. Versions MUST NOT have revision, updated_at or is_current. Current pointer MUST reference a version owned by that root. Version identity/content/ownership/time are immutable after publication.

<a id="prf-008"></a>
**PRF-008.** PreferenceSet MUST use lazy creation. Workspace initialization creates no root/version. First complete valid Save with satisfied root-absence precondition MUST create root, first version, current pointer and successful receipt atomically at revision 1. Failure MUST NOT leave an empty root or partial publication. Root absence means NOT_CONFIGURED; there is no clear/reset/unconfigure operation in M2. Different first-save request IDs compete on absence; the loser conflicts even for identical content.

<a id="prf-009"></a>
**PRF-009.** Ordinary later Save MUST admit current root revision before comparing canonical configuration. A real change creates a new immutable version, advances current and increments revision by exactly one atomically. Canonical equality is UNCHANGED and modifies no business object. At maximum Common Revision, an admitted no-op succeeds and a real change produces REVISION_EXHAUSTED; never wrap. A → B → A publishes a new A version. These rules do not override successful request replay in PRF-012.

<a id="prf-010"></a>
**PRF-010.** First publication MUST use one system UTC millisecond time for root.created_at, root.updated_at and version.created_at. A later real publication MUST use max(now, previous root.updated_at) for root.updated_at and new version.created_at, preserving root.created_at. No-op/replay MUST NOT refresh business timestamps. UUIDv4 has no temporal order; neither it nor created_at promises a strict total order of history. Current pointer selects current; revision orders root modifications. No historical sequence field is introduced.

<a id="prf-011"></a>
**PRF-011.** Every published version MUST retain complete immutable content for the Workspace lifetime, without expiry, single-version deletion or replacement by a digest. Reads MUST NOT activate history. M2 introduces no history listing, historical restore, named search profiles or alternate persistent Preference roots. Saved content/history is private; retention does not authorize model/provider transmission.

## 3. Save identity, fingerprint and receipts

<a id="prf-012"></a>
**PRF-012.** Every logical Save MUST carry a client-generated request_id. After request boundary and complete canonical input validation, resolve a successful receipt before ordinary existence/revision/equality admission. Same request ID plus same canonical content and original precondition MUST return the original successful result. A differing fingerprint MUST produce REQUEST_CONFLICT. Replay MUST NOT create another version/receipt, advance revision or restore an old current pointer. Concurrent matching requests MUST converge on one success; differing same-ID requests cannot both succeed. New logical saves use new IDs. Invalid payloads cannot bypass validation by reusing a successful ID.

<a id="prf-013"></a>
**PRF-013.** request_fingerprint MUST be Sha256Hex of the exact bytes below. `||` concatenates bytes; u32be is four unsigned big-endian bytes. S length is UTF-8 byte length. A encodes the validated canonical array order, including its count. Revision decimal is canonical unsigned decimal without leading zeros, exponent or decimal point; admitted JSON spelling is not restricted.

```text
S(text) = u32be(byte_length(UTF8(text))) || UTF8(text)
A(strings) = u32be(count(strings)) || S(strings[0]) || ...
R(null) = 0x00
R(revision) = 0x01 || S(decimal_integer(revision))
C(UNLIMITED) = 0x00
C(LIMITED, value) = 0x01 || encode(value)
bytes = UTF8("PreferenceSetSave:v1") || 0x00 || R(request.revision)
     || A(configuration.target_job_keywords)
     || C(configuration.accepted_cities)
     || C(configuration.minimum_salary)
     || C(configuration.recruitment_types)
     || C(configuration.excluded_companies)
     || C(configuration.max_required_education)
```

LIMITED city/type/company values use A; salary uses u32be; education uses S of its enum. Field order is exactly as shown. request_id, generated IDs/timestamps, raw JSON bytes, object key order and numeric spelling MUST NOT participate. JSON TEXT serialization MUST NOT determine business equality or fingerprint identity. M1's distinct fingerprint stays unchanged.

<a id="prf-014"></a>
**PRF-014.** PreferenceSaveReceipt MUST contain exactly request_id, request_fingerprint, preference_set_id, preference_set_version_id, result_revision and outcome. The IDs use UuidV4, digest Sha256Hex, result_revision Common Revision and outcome CREATED/UPDATED/UNCHANGED. It MUST reproduce PRF-019's original success; result_revision maps to response revision. Receipt identity is unique only within the Workspace's Preferences Save namespace, independently of Entry create requests. Content/fingerprint/version references MUST NOT be unique. Receipt MUST NOT duplicate configuration, original precondition or timestamps. The precondition is hashed; original configuration is available through its retained version. Persist every successful receipt, including no-op, atomically with its outcome and retain it for Workspace lifetime. Known failed commands MUST NOT acquire success receipts.

## 4. HTTP and error boundary

<a id="prf-015"></a>
**PRF-015.** M2 MUST provide only the following Preferences operations, using the Common/Workspace local access boundary. All success responses are HTTP 200 with the exact result object specified below, without another envelope. GET operations accept no body or query parameters; neither modifies state. There is no PATCH, delete/reset/history-list/restore operation.

| Method and path | Request/result owner |
| --- | --- |
| POST /api/v1/preferences/save | PRF-017 / PRF-019 |
| GET /api/v1/preferences | PRF-018 current read |
| GET /api/v1/preferences/versions/{preference_set_version_id} | PRF-018 exact read |

<a id="prf-016"></a>
**PRF-016.** Save transport MUST be UTF-8 JSON. Media-type parsing MUST accept application/json and compatible charset=utf-8, not require byte-identical header spelling; non-UTF-8 charset and non-JSON transport are BAD_REQUEST. Absent Content-Encoding or identity is allowed; other encodings are rejected as BAD_REQUEST. Invalid body encoding, malformed JSON and duplicate decoded member names within any object MUST produce BAD_REQUEST; no last-value-wins. Parseable wrong object/type/field/value inputs produce VALIDATION_ERROR under Common M2 admission. GET body/query admission errors produce VALIDATION_ERROR.

Save MUST admit at most 1,048,576 actual body bytes, including JSON whitespace/escape spelling. Exceeding that bound produces REQUEST_TOO_LARGE; this applies while receiving, not only to declared Content-Length. Each multivalue input array MUST admit at most 1,000 raw items before deduplication, otherwise OUT_OF_RANGE at that array. Limits MUST reject rather than truncate/partially save. Implementations MUST NOT buffer an unbounded body before enforcing the byte limit.

<a id="prf-017"></a>
**PRF-017.** Save request MUST contain exactly request_id, revision and configuration, all required. request_id uses UuidV4. Explicit revision null means the root must not exist; otherwise revision uses Common Revision. Missing/zero MUST NOT alias null. Root-present/null and root-absent/numeric are REVISION_CONFLICT, after PRF-012 replay handling. configuration uses PRF-002–006. Caller-supplied saved IDs, timestamps and other extras are rejected. Input admission/canonicalization precedes receipt matching, then ordinary precondition, then equality, then atomic outcome/receipt commit; success MUST NOT be acknowledged before confirmed commit.

<a id="prf-018"></a>
**PRF-018.** Current read MUST return exactly `{status: NOT_CONFIGURED}` before first successful Save, or exactly status CONFIGURED, preference_set (PRF-007 root) and current_preference_set_version (PRF-007 version). The root and referenced version MUST come from one consistent committed observation; missing/broken stored authority MUST NOT become an unconfigured/default response. Exact read MUST validate its path ID as UuidV4 and return the complete specified PreferenceSetVersion; a well-formed missing ID is NOT_FOUND, never a substitution of current. Neither result reserves current against subsequent Save.

<a id="prf-019"></a>
**PRF-019.** Save success MUST contain exactly preference_set_id, preference_set_version_id, revision and outcome. CREATED denotes first publication, UPDATED a real changed publication and UNCHANGED a canonical no-op. IDs/revision describe this original successful request, not necessarily the latest root. Replay returns the same original result even after current advances. A caller needing current state MUST read current separately; failure of that read MUST NOT undo/reclassify the saved outcome.

<a id="prf-020"></a>
**PRF-020.** Errors MUST use Common ContractError, shared vocabulary and the M2 path grammar, without a parallel Preferences error shape. Operations MUST use these mappings:

| HTTP | Code and trigger |
| --- | --- |
| 400 | BAD_REQUEST — malformed/unsupported transport or malformed/duplicate-key JSON |
| 403 | ACCESS_DENIED — Workspace Host/Origin rejection, before business handling |
| 413 | REQUEST_TOO_LARGE — Save body exceeds byte bound |
| 422 | VALIDATION_ERROR — admitted JSON/path/query/body fails schema or value validation |
| 404 | NOT_FOUND — well-formed exact version ID absent |
| 409 | REVISION_CONFLICT — ordinary root-presence/revision precondition fails |
| 409 | REQUEST_CONFLICT — existing request ID differs in canonical input/precondition |
| 409 | REVISION_EXHAUSTED — real modification requires increment beyond maximum |
| 503 | STORAGE_UNAVAILABLE — storage failure with confirmed non-commit of Save, or unavailable read |
| 503 | OUTCOME_UNKNOWN — commit outcome cannot be established |
| 500 | INTERNAL_ERROR — unclassified internal failure; does not prove rollback |

Unknown mode/type/education enum uses INVALID_FORMAT; empty sets or numeric/count bounds use OUT_OF_RANGE; LIMITED without value uses REQUIRED. UNLIMITED with value uses INVALID_FORMAT at the choice parent (e.g. configuration.accepted_cities), not UNKNOWN_FIELD. Truly unknown keys use UNKNOWN_FIELD at the nearest known parent. Invalid nested items use original submitted indices. Invalid scalar/control text follows INVALID_CHARACTERS; blank/length/UUID/type errors follow Common. Field validation failure MUST provide at least one accurate field error; ordering/all-errors enumeration is not promised. Other errors use empty field_errors when not field-specific.

## 5. Caller recovery, UI and interface agreement

<a id="prf-021"></a>
**PRF-021.** Timeout, connection loss, ambiguous write 5xx and responses establishing neither valid success nor definite rejection MUST require verification. Preserve the original request ID, precondition and complete configuration for explicit retry, without silently changing ID/revision or resubmitting as a new logical Save. Current equality is not evidence that the request succeeded; different current content is not evidence it failed. A definite 4xx rejects that request but does not establish non-commit of an earlier uncertain request. OUTCOME_UNKNOWN MUST NOT become persisted Preference state. M2 introduces no durable browser retry queue or unsaved-draft crash recovery. Confirmed commit followed by response failure remains success or requires verification, never invented rollback. Storage completion recovery is bounded by STO-008; no invisible command reexecution.

<a id="prf-022"></a>
**PRF-022.** The eventual Preferences UI MUST use item input plus Add/removable chips for keywords/cities/companies; a plain decimal-digit integer entry for salary (no k notation, grouping commas, currency signs, fractions or ranges); recruitment multiselect buttons; education single-select dropdown. Five independent UNLIMITED checkboxes disable/inactivate their concrete controls; keywords require at least one item. Inactive unsaved draft retention is an implementation choice, not saved authority. Labels/help MUST distinguish Job education ceiling from candidate education and explain salary units. Save MUST validate authoritatively on the backend and fail atomically for any invalid input. Editing is not saved authority; success/replay MUST NOT be presented as proof that the returned version is still current. UI design/implementation remains later work; backend Contract readiness does not claim delivered UI.

<a id="prf-023"></a>
**PRF-023.** Application-owned canonicalization MUST be shared by equality, fingerprint generation, Save validation and persistence admission. Database JSON is only representation; key order/whitespace MUST NOT affect equality. DTO/OpenAPI/generated-client schemas MUST reflect exact choice, integer-value, null-precondition and error-path rules without becoming another authority. Storage owns physical schema/constraints/transactions/evolution under STO-014–020; Common owns shared representations under COM-033–037; Workspace owns local runtime applicability under WSP-007. Collection source mapping/admission and Job Pool query details MUST remain outside this consumed scope.

## 6. Provenance and evolution

CG02-BC1/S1 and accepted CG02-Q1–Q40 control as qualified by their recorded supersession. PRF-001 supersedes the historical M2 QuickScreen/current-Preference eligibility proposal, not any published Job Contract. Q12's target_job_keywords replaces the earlier proposed job_search_keywords name; Q29 rejects UUID ordering; Q38 rejects JSON byte equality; Q40 rejects UNKNOWN_FIELD for incompatible known value. No earlier PRF IDs existed or are reused. Required proof is mapped in [Acceptance](../../acceptance.md#32-sl-01m2-contract-conformance).
