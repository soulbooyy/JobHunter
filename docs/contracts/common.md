# Common Contract — Shared Expression and M1 Types

> English is authoritative. Normative scope revision: **2026-09-19.M1-r1**. Scope: conventions and types actually consumed by SL-01.M1. Additional formal-asset, invocation and immutable-reference schemas remain unassigned. Readiness and review evidence belong to [Progress](../progress/traceability.md#6-contract-normative-scope-readiness-ledger), not this header.

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
