# Candidate Profile Contract

> **Current applicability — 2026-09-24.S2M1S1-r1.** PRO-001–003/006–009 shared contact authority, separate Save/adoption, initialization and material joins are superseded. PRO-004/005 contact validation and PRO-006 display/null/privacy behavior survive only for Resume-owned contacts. CandidateProfileProjection is a different read-only capability index. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../../design/contract/sl-02-m1-supplement-grill.md); [current review](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. The original clauses preserve SL-02.M1 scope; the final section adds the explicitly bounded 2026-09-21.S2M2-r1 consumer interface. Other future scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../design/contract/sl-02-m1-grill.md)

## 1. Authority and saved representation

<a id="pro-001"></a>
**PRO-001.** CandidateProfile MUST be the sole authority for the three v1 identity/contact values: full_name, phone_number and email. Career facts belong to [Evidence](evidence.md); collection intent to [Preferences](preferences.md); optional Header wording to [Resume](resumes-grounding.md). No nickname, GitHub, city, homepage, gender, political-affiliation or work-years field belongs to Profile. The single Profile MUST NOT be deleted in v1; clearing all three values is a valid Save. Contact fields MUST remain model-invisible by default; display support does not authorize model admission. (Q1/Q7/Q13; BC1/BC3.)

<a id="pro-002"></a>
**PRO-002.** The complete saved shapes MUST be:

| Object | Exact fields and types |
| --- | --- |
| CandidateProfile | profile_id: UuidV4; current_profile_version_id: UuidV4; revision: Revision; created_at: UtcTimestamp; updated_at: UtcTimestamp |
| ProfileVersion | profile_version_id: UuidV4; profile_id: UuidV4; schema_version: integer 1; full_name: string or null; phone_number: string or null; email: string or null; created_at: UtcTimestamp |

Business values MUST occur only in the immutable Version. The current pointer MUST reference a Version of that root. IDs, strict fields and metadata use COM-038; publication uses SAV-004/005. No Version revision, updated_at or is_current is introduced. (Q49/Q51/Q56.)

<a id="pro-003"></a>
**PRO-003.** Fresh S2-capable initialization and explicit migration MUST create exactly one real Profile root at revision 1 and a first immutable Version with all three values null, atomically under STO-022. Profile completeness MUST NOT gate Knowledge maintenance or Resume creation. An absent mandatory root/Version after initialization MUST NOT be repaired by an ordinary read or startup. Preferences remains lazy and no Resume is automatically created. (Q49/Q51/Q93.)

## 2. Contact values and equality

<a id="pro-004"></a>
**PRO-004.** All three contact keys MUST exist; each allows explicit null. Non-null input MUST use COM-025 scalar text and COM-026 fixed outer trim. A trimmed empty string MUST fail BLANK_VALUE, never become null. Preserve admitted internal spacing, case and Unicode form. full_name MUST contain 1–100 code points and no remaining controls or line/paragraph separators. phone_number MUST contain 1–50 code points, only ASCII digits, U+0020 spaces, hyphens, parentheses and at most one plus at the beginning, and at least one ASCII digit; other formats fail INVALID_FORMAT after shared scalar/character checks. No country inference, formatting repair or multiple-number structure is supported. (Q13/Q17.)

<a id="pro-005"></a>
**PRO-005.** A non-null email MUST contain 1–254 code points, exactly one @ with nonempty sides, and no remaining COM-026 whitespace/control characters or line/paragraph separators. This is bounded contact validation, not proof of deliverability or comprehensive email-standard conformance. Invalid syntax MUST fail INVALID_FORMAT; prohibited characters follow COM-039. Saving MUST NOT send email, check reachability, lowercase or repair it. Canonical Profile equality MUST compare the three admitted nullable strings exactly; object-key order and JSON spelling MUST NOT matter. (Q17/Q57/Q97.)

## 3. Exact use, reads and editing

<a id="pro-006"></a>
**PRO-006.** Resume Header MUST obtain the three fixed values from its exact profile_version_id, never duplicate them or override them privately. Populated values MUST display; null MUST produce no placeholder or label-only content. No presentation hide control is supported. Profile publication MUST NOT update any existing ResumeVersion. First/newly switched Resume reference MUST be current at commit; an unchanged exact reference from the preceding formal ResumeVersion MAY remain historical. Resume source admission is RES-011; command ordering is SAV-003. (Q14/Q59/Q60; BC3/A1.)

<a id="pro-007"></a>
**PRO-007.** The read interfaces MUST be GET /api/v1/profile → {profile: CandidateProfile, profile_version: ProfileVersion} and GET /api/v1/profile/versions/{profile_version_id} → ProfileVersion, both 200. The current pair MUST come from one consistent snapshot with matching root/current/owner IDs; exact reads MUST NOT substitute current content. Missing requested exact IDs use SAV-014; missing mandatory internal authority uses STO-028. No Profile-history listing/picker is introduced. Save accepts and returns only SAV-001/008 shapes. (Q75/Q78.)

<a id="pro-008"></a>
**PRO-008.** Profile edits MUST use the separate Profile Save. A Resume editor changing contact values MUST NOT treat unsaved values as a private saved Header; explicit Profile publication and explicit Resume source adoption are separate actions. Failed Save preserves the editing draft; no-op/replay/publication follow SAV-004–009. This Contract grants no automatic propagation or additional AI contact permission. (BC3/A1; Q14/Q57/Q60.)

## 4. Materials exact contact projection

Scope revision **2026-09-21.S2M2-r1**. Earlier published consumer semantics remain effective within their scope. Provenance: [CG04](../../design/contract/sl-02-m2-grill.md).

<a id="pro-009"></a>
**PRO-009.** For MAT-005, Profile MUST provide the complete retained ProfileVersion identified by ResumeVersion.profile_version_id, with PRO-002/006's three-field contact/null/display semantics. Validate actual source identity and consumed fields, not currentness of the Profile root; never substitute current contacts or a private Materials copy. This internal capability adds no HTTP operation and does not weaken PRO-007 full-read behavior. Actual permission/availability remains enforced. Q1/Q14/Q67/Q69/Q74/Q96.

## 5. CandidateProfileProjection schema v1 and paired publication

Scope revision **2026-09-24.S2M1S1-r1**. The [user-approved naming amendment](../../design/contract/sl-02-m1-supplement-grill.md#cg03s1-profile-entry-naming) names the collection entries and its element ProfileIndexEntry; the schema remains v1. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="pro-010"></a>
**PRO-010.** CandidateProfileProjection schema v1 MUST describe only supported capabilities observed from EVD-016’s default-source Evidence. User intent remains PreferenceSetVersion; no desired city/salary/role, contact/Header value, proficiency score, personality label or unsupported capability upgrade is allowed. Education, skills, experience domains and demonstrated directions use the same entry shape; no fixed category taxonomy is required.

<a id="pro-011"></a>
**PRO-011.** The immutable Profile MUST contain exactly schema_version: 1, resume_version_id, extraction_key and entries. entries is an ordered array of ProfileIndexEntry objects containing exactly name: nonblank scalar string, description: nonblank scalar string, evidence_refs: nonempty array of EVD-018 EvidenceRef. name and description use Common scalar/control admission and retain admitted model text; finite output limits belong to the registered invocation configuration, not an invented proficiency taxonomy. Every ref MUST resolve inside the paired exact Evidence. Duplicate refs within one capability are invalid. This is the established business field schema: capability name, short description, evidence references. Schema version, source and generation metadata are not user-editable profile fields.

<a id="pro-012"></a>
**PRO-012.** A portrait MUST publish Profile and Evidence as one coherent immutable pair: {portrait_id: UuidV4, schema_version: 1, resume_version_id, extraction_key, profile: CandidateProfileProjection, evidence: CandidateEvidenceProjection, generation: {kind: MODEL|REUSE, run_id: UuidV4|null, reused_from_portrait_id: UuidV4|null}, created_at}. MODEL requires the owning invocation run_id with its lawful complete durable response and null reused_from; publish the pair/derivation decision under current qualification before confirming/ending that Run, never require it already ENDED; REUSE requires the prior exact portrait and null run_id. Source IDs/rules must match throughout. Only an eligible current build may attach this pair to current state. Ready means nonempty entries with valid supported refs; an empty semantic result leaves portrait unavailable, not a fabricated generic capability.

<a id="pro-013"></a>
**PRO-013.** Profile generation MUST use one schema-constrained protected model invocation over the admitted deterministic Evidence; model output is exactly {entries:[{name,description,evidence_refs:[evidence_id,...]}]}. Backend resolves these local IDs against the frozen source and expands full EvidenceRefs; the model cannot select source version/rules. Validate the complete output and semantic-support obligation. Any invalid entry, bad/missing ref, empty unusable result or detected unsupported upgrade rejects the whole candidate; do not silently prune or substitute approximate claims. Structural checks do not prove semantic support; required Eval covers that quality. No hidden second model judge is authorized.

<a id="pro-014"></a>
**PRO-014.** Each derivation attempt MUST allow at most one Provider request, zero for deterministic reuse. No automatic repair, retry or fallback model request is permitted. A complete durably stored response may recover local validation/publication without redispatch; uncertain/incomplete dispatch must remain failed/unavailable with truthful usage. Explicit refresh may create a fresh attempt after terminal failure. Missing provider configuration, admission/budget denial or source too large for protected input leaves portrait unavailable without blocking Resume Save. Reuse actual SL-03.M1/M2 runtime admission, budget and durability; do not masquerade this consumer as safe render replay or the conformance exercise format.

The registered portrait consumer MUST also supply the EXR-024 whole-Run agreement before enabling real invocation. Its durable build outcome is either an exact validated pair (published current only under SAV-023), a deterministic terminal derivation rejection with its owned reason, or an obsolete-source disposition; none may be inferred merely from durable response bytes. A valid historical pair remains successful derivation without becoming current. A durably recorded complete derivation decision (including unusable/invalid Profile or proven admission denial with no remote uncertainty) establishes COMPLETION_CONFIRMED and may end COMPLETED under EXR-009; it does not imply READY. Fresh semantic-start rejection creates no Run. Actual remote uncertainty retains OUTCOME_UNKNOWN; actual time denial retains TIMED_OUT; authorized cancellation retains CANCELLED. Runtime-owned integrity/missing-handler failures retain their existing exact EXR causes. Do not promote generic HTTP failure, stale qualification or unconfirmed storage outcome into any terminal fact.

Registration MUST freeze a positive finite execution timeout and nonnegative finite local-recovery grace in the exact execution configuration. Establish the Run deadline at accepted semantic start, before any invocation; queued portrait waiting before that start does not authorize dispatch. Persist the local-recovery latest-grant instant as that deadline plus the frozen grace, with checked arithmetic; it cannot reset across restart. Admit only deterministic processing of a response durably available before the original deadline, using fresh current qualification, source/permission checks, SAV-023 fencing and a finite execution bound no later than that latest-grant instant. A complete recorded decision is confirmed before decoding/time admission. After the bound, genuinely unfinished work converges under EXR-011 without dispatch; already-ended Runs cannot reopen. Unknown commit/read outcome remains unresolved until owned bounded reconciliation establishes truth. This is a business consumer agreement, not the EVO conformance consumer or a universal recovery default; concrete finite values, adapter format keys and all registered configuration limits require executable adoption proof.

<a id="pro-015"></a>
**PRO-015.** CurrentPortraitState MUST contain exactly default_resume_selection, source_resume_version_id: UuidV4|null, status: NO_SOURCE|EMPTY_SOURCE|QUEUED|RUNNING|READY|FAILED, build_id: UuidV4|null, portrait_id: UuidV4|null and failure_code: string|null. NO_SOURCE has null source/build/portrait; EMPTY_SOURCE has source but null build/portrait. QUEUED/RUNNING has source/build and null portrait; READY has source/build/portrait and null failure; FAILED has source/build, null portrait and a sanitized code. Failures use SOURCE_UNAVAILABLE, CONFIGURATION_UNAVAILABLE, INPUT_NOT_ADMITTED, OUTPUT_INVALID, INVOCATION_FAILED or OUTCOME_UNKNOWN; no sensitive detail. failure_code MUST be non-null if and only if status=FAILED. This is mutable current publication state, not an immutable Profile field or claim that earlier history vanished. A coherent pair is visible as current only in READY.

<a id="pro-016"></a>
**PRO-016.** The user-portrait page MUST show source attribution, read-only supported capabilities and an edit-source route when ready. Otherwise show unavailable/source state and explicit refresh; no partial-Evidence browsing workflow. Refreshing a ready source makes new use unavailable immediately; failed refresh does not restore old-as-current. GET/page reload only observes. DeepFit clicked without ready portrait returns a clear unavailable prerequisite response with no hidden dispatch/fallback. Already-frozen analysis keeps exact historical inputs. Distinguish this from empty selected-Resume optimization, which checks only that selected document under RES-024.
