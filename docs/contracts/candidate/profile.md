# Candidate Profile Contract

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. This body defines only the SL-02.M1 consumed scope; future consumer scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

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
