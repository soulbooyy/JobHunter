# Common Contract — Shared Expression and M1 Types

> **Current applicability — 2026-09-24.S2M1S1-r1.** COM-038’s server-generated-ID rule gains the logical-ID exception below; COM-038’s schema-1 literals for ResumeVersion/CandidateCommandReceipt and COM-043’s schema-1 Artifact/RenderManifest literals are superseded by RES-018/SAV-020/MAT-032 for the new schema-2 objects; existing scalar, privacy, error and value-encoder definitions retain their meanings. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../design/contract/sl-02-m1-supplement-grill.md); [current review](../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> English is authoritative. Normative scope revision: **2026-09-19.M1-r1**. Scope: conventions and types actually consumed by SL-01.M1. Later additions below publish only their stated consumer scopes; other formal-asset, invocation and immutable-reference schemas remain unassigned. Readiness and review evidence belong to [Progress](../progress/traceability.md#6-contract-normative-scope-readiness-ledger), not this header.

[Index](index.md) · [Decision provenance](../design/contract/sl-01-m1-grill.md) · [Entry](jobs/manual-application-entries.md) · [Workspace](foundation/workspace.md) · [Storage](foundation/storage.md)

## 1. Naming and normative expression

The following rules implement CG01-Q1. Examples illustrate naming only; they do not add fields to other objects.

<a id="com-001"></a>
**COM-001.** Type/object names MUST use `PascalCase`, such as `ManualApplicationEntry`.

<a id="com-002"></a>
**COM-002.** Canonical Contract fields MUST use `snake_case`.

<a id="com-003"></a>
**COM-003.** Canonical serialized enum values MUST use `UPPER_SNAKE_CASE`.

<a id="com-004"></a>
**COM-004.** Stable logical business identities MUST use `*_id` names.

<a id="com-005"></a>
**COM-005.** Immutable business-version identities MUST use object-specific `*_version_id`, not bare `version_id`.

<a id="com-006"></a>
**COM-006.** `revision` MUST mean mutable-object/persistence-row optimistic concurrency, not immutable business versioning.

<a id="com-007"></a>
**COM-007.** `schema_version` MUST mean serialized/persisted structure evolution, not a business or policy version. Storage's explicit mapping to SQLite metadata is defined by STO-005.

<a id="com-008"></a>
**COM-008.** Policy versions MUST use meaningful `*_policy_version` names. Bare `policy_version` MAY be used only where exactly one policy is unambiguous.

<a id="com-009"></a>
**COM-009.** Contracts MUST NOT use an ambiguous bare `version` field in place of a business version, schema version, policy version or concurrency revision.

<a id="com-010"></a>
**COM-010.** References SHOULD use the target's canonical identity name. Generic `target_id`/`source_id` names MAY be used only by genuinely generic structures, not as synonyms for a known object identity.

<a id="com-011"></a>
**COM-011.** Collection names MUST use concept plurals, such as `reason_codes`; they MUST NOT add redundant type suffixes such as `*_id_list`.

<a id="com-012"></a>
**COM-012.** Boolean names MUST express positive predicates, preferably `is_*`, `has_*`, `can_*` or `requires_*`; they MUST NOT use double negatives or inverted state meanings.

<a id="com-013"></a>
**COM-013.** State-like alternatives SHOULD use an enum rather than combinations of Booleans. Independent concerns MUST NOT be collapsed into a universal lifecycle merely to follow this convention.

<a id="com-014"></a>
**COM-014.** Timestamp fields MUST use `*_at` names.

<a id="com-015"></a>
**COM-015.** Date-only fields MUST use `*_date` and MUST remain distinct from timestamp values.

<a id="com-016"></a>
**COM-016.** Duration/timeout fields MUST carry explicit units in their names, such as `duration_ms` or `ttl_seconds`.

<a id="com-017"></a>
**COM-017.** `UtcTimestamp` MUST serialize a valid RFC 3339 UTC instant as `YYYY-MM-DDTHH:mm:ss.sssZ`, with exactly three fractional digits and `Z`. M1 system-clock values use millisecond precision; finer precision is discarded. Offsets, local time and varying fractional precision MUST NOT appear in emitted canonical values. This type does not make Entry timestamps caller-writable.

<a id="com-018"></a>
**COM-018.** One business concept MUST have one canonical name across Contracts; synonymous field names MUST NOT silently create duplicate concepts.

<a id="com-019"></a>
**COM-019.** Internal code MAY follow language naming conventions, but adapters MUST explicitly preserve canonical names and meanings at Contract boundaries.

<a id="com-020"></a>
**COM-020.** Normative clauses MUST use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` for requirement strength. Explanatory prose SHOULD avoid incidental uppercase use of these keywords.

<a id="com-021"></a>
**COM-021.** Requirements MUST have stable owner-prefixed IDs. Moving a clause or renaming a heading MUST NOT change its ID. Current owners are `COM` (Common), `WSP` (Workspace), `MAE` (ManualApplicationEntry) and `STO` (Storage).

<a id="com-022"></a>
**COM-022.** Published requirement IDs MUST NOT be reused; retired IDs remain reserved.

<a id="com-023"></a>
**COM-023.** Replacement of a requirement's core semantics MUST record explicit supersession and a new ID rather than repurpose the old one. Editorial clarification that preserves meaning does not itself require a new ID.

<a id="com-024"></a>
**COM-024.** Common MUST be the sole definition owner of these conventions. Other Contracts MUST reference them; Structure owns organization only. Examples MUST NOT impose fields on unrelated objects. Mutable records SHOULD carry creation/modification timestamps when actual consumers need them; immutable/version/event records MUST NOT mechanically acquire `updated_at`.

## 2. M1 scalar representations

<a id="com-025"></a>
**COM-025.** `UnicodeText` MUST be a JSON string of Unicode scalar values; unpaired surrogates MUST be rejected. Length MUST count Unicode code points, not UTF-8 bytes, UTF-16 code units or grapheme clusters. No implicit normalization, case folding or width conversion is part of this type.

<a id="com-026"></a>
**COM-026.** `trim_outer_whitespace` MUST remove only leading/trailing members of this fixed set: `U+0009–U+000D`, `U+0020`, `U+0085`, `U+00A0`, `U+1680`, `U+2000–U+200A`, `U+2028`, `U+2029`, `U+202F`, `U+205F`, `U+3000`. It MUST NOT inherit a moving Unicode release or language defaults. Control characters mean `U+0000–U+001F` and `U+007F–U+009F`; line/paragraph separators additionally mean `U+2028`/`U+2029`. Whether a field permits them is owned by that field's Contract. `U+FEFF` is not in the trim set.

<a id="com-027"></a>
**COM-027.** `UuidV4` MUST be a lowercase, hyphenated 36-character string matching `^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`. Boundary validation MUST reject rather than rewrite uppercase, whitespace or other UUID versions. M1 uses this type for entry IDs and create request IDs; future identity families are not selected by this rule.

<a id="com-028"></a>
**COM-028.** `Revision` MUST be a JSON number with an exact integer value from `1` through `9007199254740991`. JSON strings, Booleans, null and non-integral numbers MUST NOT be coerced and produce `INVALID_TYPE`; an integer value outside the range produces `OUT_OF_RANGE`. Consistent with [JSON Schema integer semantics](https://json-schema.org/understanding-json-schema/reference/numeric#integer), `1`, `1.0` and `1e0` represent the same admitted integer value; exponent spelling alone is not another type. Admission MUST NOT round a fractional or out-of-range input into an allowed integer. Implementations MUST prevent overflow/wraparound. Meaning and increment conditions belong to the mutable object's owner.

<a id="com-029"></a>
**COM-029.** `ContractError` MUST have exactly the following fields. It MUST NOT carry submitted values, raw exception objects, SQL or stack traces. Programs MUST use codes rather than parse message wording.

| Field | Type | Meaning |
| --- | --- | --- |
| `code` | Nonempty enum string defined by the operation owner | Service/startup outcome |
| `message` | Nonempty string | Human-readable sanitized explanation; wording is not stable protocol |
| `field_errors` | Array of `FieldError` | Empty array when not field-specific |

`FieldError` has exactly `field` and `code`. `field` is a canonical top-level field name; `$` denotes a whole-document error or an unrecognized field without echoing its supplied key. `code` is from COM-030. Consumers do not depend on field-error order; repeated identical `(field, code)` pairs are unnecessary.

<a id="com-030"></a>
**COM-030.** M1 validation MUST distinguish the following codes. A required field's absence is `REQUIRED`; explicit null for its string/integer type is `INVALID_TYPE`. Detection proceeds from missing/type/scalar legality to field-specific validation; a validator MUST NOT misclassify missing or null as blank text.

| Code | Meaning |
| --- | --- |
| `REQUIRED` | Required field absent |
| `UNKNOWN_FIELD` | Field not accepted by this operation, including a forbidden system field |
| `INVALID_TYPE` | Wrong JSON type, including explicit null |
| `BLANK_VALUE` | Empty after the specified trim |
| `TOO_LONG` | Exceeds the owning field's code-point limit |
| `INVALID_CHARACTERS` | Invalid Unicode or forbidden characters |
| `INVALID_FORMAT` | UUID/URL format invalid |
| `OUT_OF_RANGE` | Integer revision outside the admitted range |

<a id="com-031"></a>
**COM-031.** M1 request objects MUST reject unknown fields, missing required fields and wrong types rather than ignore, default or coerce them. Every request/result field listed by the M1 Contracts is required and non-null unless its owning definition says otherwise. Root values other than an object are validation errors at `$`. Omitted fields, explicit null and empty arrays MUST NOT be treated as interchangeable. This is the consumed M1 convention, not an automatic schema for future modules.

<a id="com-032"></a>
**COM-032.** `Sha256Hex` MUST be exactly 64 lowercase hexadecimal characters. The operation owner defines input bytes; a digest alone MUST NOT be treated as recoverable original content or proof of anonymity.

## 3. Ownership and evolution

No requirement has been retired or superseded in this initial scope revision. New consumer scopes add their own reviewed clauses without implying completion of all Common responsibilities. Provenance: CG01-Q1, Q16, Q20–Q21, Q27, Q30–Q32, Q36–Q37. Storage layout, command outcomes and business field applicability remain with their respective owners.

## 4. M2 consumed shared representations

Scope revision **2026-09-20.M2-r1**. COM-001–032 remain the published M1 baseline. The following clauses add the actual M2 consumer; they do not broaden M1 transport behavior or rename existing fields.

<a id="com-033"></a>
**COM-033.** M2 MUST consume COM-001–028 conventions and scalar semantics, COM-032 Sha256Hex and the ContractError/FieldError object shapes of COM-029, with only the scoped path extension in COM-034. Every declared M2 field MUST be present and non-null unless its owner explicitly allows otherwise. Unknown fields, wrong types and missing fields MUST be rejected, not stripped/coerced/defaulted. A non-object request root is INVALID_TYPE at $. Save's explicit nullable revision is an operation precondition, not a change to the Revision scalar. Boundary JSON integer admission MUST preserve exact numeric values without rounding into validity.

<a id="com-034"></a>
**COM-034.** For M2 only, COM-029's top-level-only field restriction is superseded by this grammar. All other COM-029 shape/sanitization/order rules remain effective; M1 continues its original top-level field or $ representation.

```text
path    = "$" | segment ("." segment)*
segment = name ("[" index "]")?
name    = [a-z][a-z0-9_]*
index   = "0" | [1-9][0-9]*
```

Names MUST identify known canonical fields. Indices MUST identify submitted arrays before normalization/deduplication/sorting. Missing fields use the expected path; unknown keys MUST use UNKNOWN_FIELD at the nearest known parent object, or $ for document-root extras, without echoing the key. No wildcard, quoted key, slice, recursive descent or predicate exists. Owner-defined incompatible combinations use their own validation classification rather than pretending a known field is unknown.

<a id="com-035"></a>
**COM-035.** M2 MUST reuse COM-030's REQUIRED, UNKNOWN_FIELD, INVALID_TYPE, BLANK_VALUE, TOO_LONG and INVALID_CHARACTERS meanings and missing/type/scalar-before-value classification. For M2, INVALID_FORMAT additionally covers invalid declared enums and owner-defined invalid object combinations; OUT_OF_RANGE additionally covers owner-defined numeric and collection-size bounds. These extensions do not alter M1 triggers. Known but mode-incompatible value is INVALID_FORMAT at its choice parent. No INVALID_COMBINATION/FORBIDDEN_FIELD code is introduced.

<a id="com-036"></a>
**COM-036.** The shared error vocabulary below MUST use the sole COM-029 representation. Consumers MUST define their own applicable triggers, HTTP/CLI mapping and evidence; vocabulary membership alone authorizes no operation, retry or state mutation. Existing Entry/Storage mappings remain unchanged, including their existing OUTCOME_UNKNOWN semantics.

| Code | Shared meaning |
| --- | --- |
| BAD_REQUEST | Request transport/serialization cannot be admitted |
| ACCESS_DENIED | Local access boundary rejects the caller |
| REQUEST_TOO_LARGE | Owning request byte bound exceeded |
| VALIDATION_ERROR | Input fails declared schema/value admission |
| NOT_FOUND | Requested exact resource absent |
| REVISION_CONFLICT | Mutable authority precondition not satisfied |
| REQUEST_CONFLICT | Reused request identity conflicts with original input |
| REVISION_EXHAUSTED | Required increment exceeds admitted revision range |
| STORAGE_UNAVAILABLE | Storage unavailable; write non-commit established when used to reject a write |
| OUTCOME_UNKNOWN | Command commit outcome not established; not a persisted business state |
| INTERNAL_ERROR | Sanitized unclassified failure, with no implication of rollback |

Programs MUST NOT infer commit status from HTTP class or human message alone. Owner-defined startup diagnostics and M1-only outcomes remain owned by their current Contracts; this table does not remove them.

<a id="com-037"></a>
**COM-037.** The M2 consumer MUST use distinct UuidV4 root and immutable-version identity fields and exact retained references, never bare version identifiers, current substitutions or timestamp/UUID ordering inference. A successful exact reference resolves the requested immutable content or reports failure; a pointer selects current without changing historical identity. Common supplies naming/representation only; Preferences owns field membership and retention semantics, Storage owns same-owner/reference enforcement. This does not complete other asset or invocation identity families.

## 5. SL-02.M1 shared scope

Scope revision **2026-09-21.S2M1-r1**. Existing COM-001–037 and SL-01 consumer semantics remain unchanged.

<a id="com-038"></a>
**COM-038.** S2 MUST consume COM-001–028 naming/scalar conventions, COM-029 error object shape and COM-032 digest representation. Every field set declared in the S2 bodies is closed: all listed keys MUST exist and be non-null unless explicitly nullable; unknown keys, omitted keys, invalid scalar text and wrong types MUST fail without coercion, stripping or read-time defaults. Non-object request roots use INVALID_TYPE at $. All S2 business root/Version/Baseline IDs MUST be server-generated UuidV4, immutable and never reused; client-generated request_id is separate. UUIDs/timestamps MUST NOT imply strict history order. S2 serialized Version/Baseline/receipt schema_version is integer 1, unrelated to database schema 3. Future owner prefixes extend COM-021: PRO (Profile), EVD (Evidence/Baseline), RES (Resume), SAV (Candidate Save), MAT (Materials boundary). PRF remains Preferences. (Q49–Q60/Q79/Q84.)

<a id="com-039"></a>
**COM-039.** Common MUST be the sole normative owner of shared ContractError/FieldError representation and stable FieldError.code vocabulary. Consuming Contracts MUST reference it and define field/operation triggers, never duplicate or independently redefine shared codes. New shared codes MUST state consumer applicability without silently changing existing protocols. For S2, adopt COM-034's nested known-name/submitted-index grammar, extending only COM-029's M1 top-level restriction. Missing fields use expected paths, unknown keys the nearest known parent without echo, combinations their common parent. S2 consumes COM-030/035 meanings plus STRUCTURE_TOO_COMPLEX (raw structural admission bound) and INVALID_REFERENCE (supplied identity/owner relationship invalid). INVALID_FORMAT covers declared format/enum/combination constraints; OUT_OF_RANGE covers numeric range/grid and collection-count bounds. Required/type failures precede value classification; return at least one accurate field error without exhaustive enumeration or stable ordering. Domain text/character/format triggers remain domain-owned. (Q82/Q83/Q89/Q97.)

<a id="com-040"></a>
**COM-040.** S2 MUST consume COM-036 shared top-level error vocabulary and additionally use INVALID_STATE (target lifecycle forbids the operation), SOURCE_CONFLICT (new source admission no longer valid/current), LAST_RESUME_REQUIRED (operation would remove the last ACTIVE Resume) and CAPACITY_EXCEEDED (current-object capacity exhausted). These codes use only COM-029 representation; SAV-014 owns S2 HTTP triggers. Vocabulary alone MUST NOT authorize a lifecycle change, retry, alternate authority or error-priority rule. (Q81/Q89/Q92/Q97.)

<a id="com-041"></a>
**COM-041.** S2 Month MUST be a string of exactly ASCII YYYY-MM with year 0001–9999 and month 01–12. It MUST NOT accept surrounding whitespace, shortened years, day precision, year-only values, display text or automatic padding. It MUST NOT use a system-date-dependent future limit. Field owners define null/interval/event meaning; supplied invalid month syntax/range is INVALID_FORMAT. (Q9/Q29/Q97.)

<a id="com-042"></a>
**COM-042.** S2 HttpUrl MUST reuse the complete value-validation/canonicalization definition of MAE-004, including its pinned URL standard, fixed trim, 8192-code-point bound, strict absolute HTTP(S), credentials/character/percent/port checks, no repair and preserved admitted spelling. This clause promotes reuse of the value rule only: project_url remains Evidence fact authority and LINK.url remains Resume presentation; neither becomes a ManualApplicationEntry or application fact. Saving MUST NOT fetch/resolve reachability or introduce hidden dependencies. Existing MAE-004 is unchanged. (Q30.)

## 6. SL-02.M2 shared expression

Scope revision **2026-09-21.S2M2-r1**. Earlier published consumer scopes remain effective unless an applicability extension below explicitly says otherwise. Provenance: [CG04](../design/contract/sl-02-m2-grill.md).

<a id="com-043"></a>
**COM-043.** SL-02.M2 MUST consume COM-001–028, COM-029/032 and COM-038/039's closed-field and validation conventions; MAT-012 owns the four required logical font-role mappings. The additional owner prefix is DRW (Derived Work). Artifact, RenderIntent, Work and attempt identities MUST be distinct server-generated UuidV4 values; shipped RenderConfiguration identities are fixed application-assigned UuidV4 values. request_id remains client-generated in its own command namespace. Serialized RenderConfiguration, RenderManifest, Artifact and Materials receipt schema_version MUST be integer 1; this does not select a database migration version. No other object acquires a schema_version, revision or timestamp field merely by analogy. Q1–Q16, Q33/Q48/Q75/Q88/Q127.

<a id="com-044"></a>
**COM-044.** For SL-02.M2, COM-036/040's shared top-level vocabulary additionally contains the following codes, with sole COM-029 representation. Materials/Derived Work own triggers and HTTP mappings, not another error envelope. Existing consumers' code applicability is unchanged.

| Code | Shared meaning |
| --- | --- |
| RENDER_CONFIGURATION_UNAVAILABLE | A retained configuration cannot currently admit new generation |
| ARTIFACT_UNAVAILABLE | Published Artifact metadata exists but its payload is missing |
| ARTIFACT_INTEGRITY_FAILED | Available payload bytes disagree with the Artifact's immutable integrity metadata |

Terminal Work/Intent classifications are the distinct owner-defined enum in DRW-005; vocabulary membership MUST NOT create retry, repair or state-transition authority. Q38/Q77/Q78/Q131.

<a id="com-045"></a>
**COM-045.** The shared deterministic value encoder consumed by SAV-010 and DRW-007 MUST use the following exact bytes. This consolidates the already published SAV-010 encoder without changing any old prefix, input canonicalization, fingerprint or namespace.

| Admitted value | Encoding |
| --- | --- |
| null | ASCII n |
| false / true | ASCII b0 / b1 |
| string | ASCII s + UTF-8 byte length + ASCII : + exact UTF-8 bytes |
| number | ASCII d + canonical decimal ASCII byte length + ASCII : + canonical decimal ASCII |
| array | ASCII a + element count + ASCII : + ordered concatenated encoded elements |
| object | ASCII o + field count + ASCII : + encoded key/value pairs, keys sorted by Unicode code point |

Counts MUST be unpadded ASCII decimal integers. Numbers MUST use exact plain decimal without exponent, redundant leading zeros or trailing fractional zeros; -0 becomes 0. NaN/Infinity are not admitted values. Boolean encoding MUST NOT admit Boolean values into numeric fields. Consumers canonicalize their own business fields before encoding, preserving meaningful order/text. Q76; preserved CG03-Q87.

<a id="com-046"></a>
**COM-046.** SL-02.M2 HTTP validation MUST use COM-039 paths/reasons. Path UUID errors identify the operation's canonical path field (render_intent_id, render_configuration_id or artifact_id); disposition errors identify disposition. Prohibited query/body or unrecognized parameters use the nearest declared parent, or $, without echoing arbitrary names. Repeated disposition, invalid enum/UUID and incompatible shapes use INVALID_FORMAT; absence/type/unknown fields retain REQUIRED/INVALID_TYPE/UNKNOWN_FIELD. Supplied missing references use INVALID_REFERENCE at their body field. Positive/nonnegative integer fields MUST be admitted exactly without Boolean/string coercion, fractional rounding or overflow; malformed types use INVALID_TYPE and owner-bound violations OUT_OF_RANGE. No success object may be repaired with read-time defaults. Q54/Q75/Q87/Q131.

## SL-03.M1 scoped identity and expression

Revision **2026-09-23.S3M1-r1**. [Decision source](../design/contract/sl-03-m1-grill.md); [Runtime owner](agent/execution-runtime.md). Prior scoped consumer rules remain unchanged.

<a id="com-047"></a>
**COM-047.** **Runtime scalars and closed shapes.** The internal SL-03.M1 projections MUST reuse Common UUIDv4, Sha256Hex, UTC instant and exact integer expression. Execution generation is an exact integer in 0–9007199254740991; generation zero is not execution authority. Positive byte limits/lengths reject booleans, fractions and nonfinite/coerced values; no arbitrary permanent MiB ceiling is added. Registered code keys are nonempty exact case-sensitive strings, not normalized user text. Listed logical fields are required, including explicit null where allowed; do not silently accept extra fields or insert revision/schema_version/updated_at into every object. Common conventions do not impose Entry timestamp ordering on AgentRun.

Decision sources: CG05-Q3, CG05-Q4, CG05-Q12, CG05-Q21, CG05-Q43, CG05-Q46, CG05-Q97, CG05-Q107, CG05-Q119, CG05-Q120.

<a id="com-048"></a>
**COM-048.** **Runtime requirement and error scope.** `EXR` identifies Execution Runtime requirements and `EVO` identifies scoped evaluation/evidence requirements. Internal operation errors, persisted Runtime failure_code and consumer business outcomes MUST remain distinct. EXR-032's caller errors do not automatically fail a Run. M1 provides no new public HTTP envelope/status mapping, universal business error registry or generic recovery-denial code. Reuse existing Common HTTP rules only when a later actual HTTP consumer is defined.

Decision sources: CG05-Q1, CG05-Q53, CG05-Q98, CG05-Q105, CG05-Q111, CG05-Q120.


## SL-03.M2 protected semantic scope

> Normative scope revision: **2026-09-24.S3M2-r1**. English is authoritative. This defines required behavior, not implemented or executed acceptance. Earlier scoped consumers remain unchanged.

[Decision register](../design/contract/sl-03-m2-grill.md) · [Contract index](index.md)



<a id="com-049"></a>
**COM-049.** **M2 internal expression.** SL-03.M2 MUST reuse COM-017 UTC milliseconds, COM-025 Unicode scalar strings without implicit normalization, COM-027 UUIDv4, COM-032 Sha256Hex and COM-047 exact keys/closed logical shapes. Budget's signed-64-bit nonnegative integer range does not enlarge M1 execution_generation. Byte limits are positive finite exact integers. Owner-defined optional values use explicit null only where declared; no coercion of Boolean/string/fraction into integer, silent trimming, duplicate-key acceptance, default repair or unknown properties. Internal error outcomes remain distinct from persisted failure_code and business outcomes under COM-048; no public HTTP envelope is introduced. New requirement prefixes are CTX (Context), TOL (Tools) and BUD (Budget). COM-045 is reused for semantic-start fingerprints and the typed Context encodings; it MUST NOT replace the separate fixed-order DeepSeek terminal JSON format. Each owner defines finite technical parsing/size bounds in its controlled configuration; this does not create a universal business-input schema.

Decision sources: [CG06-Q11](../design/contract/sl-03-m2-grill.md#cg06-q11), [CG06-Q21](../design/contract/sl-03-m2-grill.md#cg06-q21), [CG06-Q31](../design/contract/sl-03-m2-grill.md#cg06-q31), [CG06-Q39](../design/contract/sl-03-m2-grill.md#cg06-q39), [CG06-Q41](../design/contract/sl-03-m2-grill.md#cg06-q41), [CG06-Q42](../design/contract/sl-03-m2-grill.md#cg06-q42), [CG06-Q43](../design/contract/sl-03-m2-grill.md#cg06-q43), [CG06-Q116](../design/contract/sl-03-m2-grill.md#cg06-q116), [CG06-Q129](../design/contract/sl-03-m2-grill.md#cg06-q129), [CG06-Q137](../design/contract/sl-03-m2-grill.md#cg06-q137), [CG06-Q138](../design/contract/sl-03-m2-grill.md#cg06-q138), [CG06-Q139](../design/contract/sl-03-m2-grill.md#cg06-q139), [CG06-Q162](../design/contract/sl-03-m2-grill.md#cg06-q162), [CG06-Q172](../design/contract/sl-03-m2-grill.md#cg06-q172), [CG06-Q182](../design/contract/sl-03-m2-grill.md#cg06-q182).

## Supplement: independent document identity and protocol applicability

Scope revision **2026-09-24.S2M1S1-r1**. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="com-050"></a>
**COM-050.** Resume entry_id and block_id MUST use canonical UuidV4 values, assigned by the editor/import draft before Save and preserved by the backend. These are logical identities contained in a Resume, not independent writable business roots. Resume, ResumeVersion, projection and build identities remain server-generated. The exact EvidenceRef is owned by EVD-018; it is not an unqualified UUID or a character offset.

<a id="com-051"></a>
**COM-051.** This coordinated development replacement MUST reject obsolete Candidate request fields/operations; it MUST NOT adapt or replay legacy Candidate payload formats. New commands use SAV-018–025. Existing Manual Entry, Preferences, Materials demand and controlled.model.v1/controlled.read.v1 protocol meanings are unchanged. STO-054–058 defines the explicit development reset, not a compatibility migration. New-model success receipts and immutable history remain required.
