# Evidence and Baseline Contract

> **Current Entry-scoped amendment — 2026-09-24.S2M1S1-r2.** Accepted [Q42–Q46](../../.grill/contract/sl-02-m1-supplement/decisions.md#cg03s1-q42) replaces the earlier whole-source-only reuse/input policy with Entry-scoped generation, exact baseline reuse and explicit full refresh. The amended clauses and additions below control that scope; original source/privacy/transaction/Runtime guarantees survive. [Reviewed scope](../../progress/traceability.md#entry-incremental-review) separates Contract readiness from implementation.

> **Current applicability — 2026-09-24.S2M1S1-r1.** EVD-001/002/006–015 independent fact authority, Baseline, CRUD, retirement and material joins are historical. The six kind values and EVD-003–005 field/value semantics are reused by Resume entries; ownership is now RES-018. EVD-016–023 defines the new read-only projection. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../../.grill/contract/sl-02-m1-supplement/decisions.md); [current review](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. The original clauses preserve SL-02.M1 scope; the final section adds the explicitly bounded 2026-09-21.S2M2-r1 consumer interface. Other future scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../.grill/contract/sl-02-m1/decisions.md)

## 1. Item authority and immutable versions

<a id="evd-001"></a>
**EVD-001.** EvidenceItem MUST own one permanent EvidenceKind: EDUCATION, WORK_EXPERIENCE, PROJECT, SKILL, AWARD or CERTIFICATION. WORK_EXPERIENCE includes internship, regular and part-time professional experience without a separate v1 experience_type. No OTHER or kind-conversion command exists. Correcting kind requires a new identity and optional explicit retirement of the old Item, not hidden reference migration. Kind MUST NOT be independently owned by a Version or Resume section; an API kind projection MUST derive from the retained Item. (Q8/Q48/Q50.)

<a id="evd-002"></a>
**EVD-002.** Saved objects MUST have exactly these fields:

| Object | Exact fields and types |
| --- | --- |
| EvidenceItem | evidence_item_id: UuidV4; kind: EvidenceKind; status: ACTIVE or RETIRED; current_evidence_item_version_id: UuidV4; revision: Revision; created_at: UtcTimestamp; updated_at: UtcTimestamp |
| EvidenceItemVersion | evidence_item_version_id: UuidV4; evidence_item_id: UuidV4; schema_version: integer 1; fields: kind-specific object; content: EvidenceContent; created_at: UtcTimestamp |

Creation MUST publish root plus first Version atomically. The current pointer MUST belong to the Item. Retirement MUST keep the last current pointer and all retained history; it does not create a fact Version. Version content is fields plus content; no version-owned kind/status/revision/is_current/updated_at exists. (Q50/Q52/Q56.)

## 2. Structured fact schemas

<a id="evd-003"></a>
**EVD-003.** fields MUST contain exactly the keys of the owning Item.kind below. All keys are required; ? means explicit null is allowed, never omitted or an empty-string substitute. S is the short text type in EVD-004; Month is COM-041. content is a sibling of fields, never repeated inside it.

| Kind | Complete fields |
| --- | --- |
| EDUCATION | school_name: S; degree: CandidateEducation; major: S?; start_month: Month?; end_month: Month? |
| WORK_EXPERIENCE | company_name: S; role_title: S; start_month: Month?; end_month: Month? |
| PROJECT | project_name: S; role_title: S?; project_url: HttpUrl?; start_month: Month?; end_month: Month? |
| SKILL | skill_name: S |
| AWARD | award_name: S; awarding_organization: S?; awarded_month: Month? |
| CERTIFICATION | certification_name: S; issuing_organization: S?; issued_month: Month? |

CandidateEducation MUST be exactly SECONDARY_VOCATIONAL, HIGH_SCHOOL, ASSOCIATE, BACHELOR, MASTER, MBA or DOCTORATE. MBA is a peer choice, not an extra field. This enum MUST NOT be substituted with Preferences education or treated as ordered by enum/source-code position; future requirement-level comparisons need their own explicit mapping. No GPA/rank/department, work city/salary/subtype, structured technology_stack, proficiency score, certificate number/expiry/verification URL is admitted. Supplementary facts MAY use content. (Q18–Q24/Q27/Q50.)

<a id="evd-004"></a>
**EVD-004.** Each non-null S MUST use COM-025/026 outer trim and then contain 1–200 code points, without remaining controls or line/paragraph separators. Internal spacing/case/Unicode form MUST remain unchanged. Null is legal only where EVD-003 permits it; non-null blank text is BLANK_VALUE. project_url MUST use COM-042 HttpUrl, with no fetch or inferred availability. Project URL is an Evidence fact; a Resume inline link is presentation, despite sharing value validation. (Q24/Q27/Q28/Q30.)

<a id="evd-005"></a>
**EVD-005.** Period start_month=null MUST mean unknown start; end_month=null MUST mean ongoing/Present. Both null is legal; ended-with-unknown-end is not represented in v1. Where both values exist, start_month MUST be <= end_month; equality is valid. awarded_month/issued_month=null MUST mean unknown event month, never ongoing. Month values MUST follow COM-041 without a moving current-date/future-date gate. No date_status or fabricated day is permitted. (Q4/Q9/Q22/Q23/Q29.)

## 3. Plain semantic body and equality

<a id="evd-006"></a>
**EVD-006.** EvidenceContent MUST be an ordered array, including [], of these exact shapes:

| type | Exact fields |
| --- | --- |
| PARAGRAPH | type; text: string |
| UNORDERED_LIST | type; items: string[] |
| ORDERED_LIST | type; items: string[] |

Each string MUST reject COM-026 controls and U+2028/U+2029 before fixed outer trim, then remain nonempty. Preserve internal spaces, duplicate text, block order and item order; do not parse HTML/Markdown or silently split illegal text. Lists MUST contain at least one item. No inline marks, nested lists, manual soft breaks, tables, images, fonts, colors or business IDs exist in EvidenceContent. Characters resembling markup are plain text, not executable/rendered markup. (Q3/Q10 as refined by Q26/Q32/Q42; BC3.)

<a id="evd-007"></a>
**EVD-007.** Each content MUST admit at most 100 blocks, 100 items per list, 10,000 code points per canonical paragraph/item and 50,000 code points across that content. Empty content is valid; empty blocks/items/lists are not. Admission MUST reject the whole command without truncating/splitting. These are stored-content bounds, not model or page-count guarantees. (Q25/Q39/Q44.)

<a id="evd-008"></a>
**EVD-008.** Evidence canonical equality MUST compare the complete admitted kind-specific fields and ordered semantic content, preserving null distinctions, text and order. It MUST NOT compare JSON bytes, UI dirty state or inferred semantic similarity. All six kinds share EVD-006, not a broadly nullable cross-kind structure. Update schema selection MUST use the authoritative immutable Item.kind under SAV-003, never guess from payload keys; missing WORK_EXPERIENCE company_name is REQUIRED at fields.company_name. (Q50/Q57/Q94/Q98.)

## 4. Baseline, lifecycle and consumers

<a id="evd-009"></a>
**EVD-009.** EvidenceBaselineSnapshot MUST contain exactly evidence_baseline_snapshot_id: UuidV4, schema_version: integer 1, members: array of {evidence_item_id: UuidV4, evidence_item_version_id: UuidV4}, and created_at: UtcTimestamp. It MUST freeze every then-ACTIVE Item once with its exact current Version. Membership is an unordered business set serialized by canonical evidence_item_id ascending, not presentation order; do not copy kind/fields/content or assert personal completeness. Evidence/Baseline MUST own exactly one durable current_evidence_baseline_snapshot_id pointer. Its physical placement in a Workspace/config row MUST NOT transfer authority. (Q55.)

<a id="evd-010"></a>
**EVD-010.** Initialization MUST publish a real empty Snapshot/current pointer. Actual Evidence create/update/retire MUST atomically publish the complete latest ACTIVE/current set and advance that pointer; retire of the last active Item publishes another empty Snapshot. Different-Item concurrent commands MUST preserve each other's committed facts, without a caller Baseline/global-Knowledge token. Same-Item writes use root revision. Profile/Resume changes and no-ops MUST NOT publish a Baseline; successful Evidence no-op returns the then-current ID under SAV-008. (Q55/Q57/Q63/Q69/Q85.)

<a id="evd-011"></a>
**EVD-011.** v1 lifecycle MUST be ACTIVE→RETIRED only. Retired content cannot be edited or restored; a matching-revision repeated retire is a successful no-op after receipt admission. Retirement MUST remove the Item from future Baselines while preserving root and immutable lineage for old Resume/Analysis reads; it MUST NOT change Resumes, local expressions, marks, links or their source references. Usage information is not authority for cascading changes. At most 1,000 ACTIVE Items may exist; creation MUST enforce capacity atomically and reject excess via SAV-014. Retired/history/receipts do not count or expire due to this cap. At capacity update/retire/read/replay remain available. (BC3; Q64/Q92.)

<a id="evd-012"></a>
**EVD-012.** New Evidence created from the Resume editor MUST first complete a separate Knowledge Save before inclusion in its Draft; later cancellation/failure of Resume Save MUST NOT roll back confirmed facts. Choosing an existing source initializes local expression once under RES-010, never creates a private fact copy. Import multi-fact confirmation, AI support, Candidate Fit and semantic extraction remain future consumer scopes; M1 provides single-Item commands only. (BC3/A5; Q36/Q63/Q95.)

## 5. Exact and list reads

<a id="evd-013"></a>
**EVD-013.** Read routes MUST return 200 with these complete representations:

| GET route | Result |
| --- | --- |
| /api/v1/evidence-items/{evidence_item_id} | {evidence_item: EvidenceItem, evidence_item_version: EvidenceItemVersion} |
| /api/v1/evidence-items/versions/{evidence_item_version_id} | {kind: owning Item.kind, evidence_item_version: EvidenceItemVersion} |
| /api/v1/evidence-baselines/current | current EvidenceBaselineSnapshot |
| /api/v1/evidence-baselines/{evidence_baseline_snapshot_id} | exact EvidenceBaselineSnapshot |

Root/current pairs MUST come from one consistent snapshot; exact readers MUST preserve the requested identity and remain usable after ordinary retirement. Missing requested IDs use SAV-014; broken persisted lineage uses STO-028. No history listing/sorting/picker or implicit creation exists. (Q75/Q78.)

<a id="evd-014"></a>
**EVD-014.** GET /api/v1/evidence-items MUST return {evidence_items: [{evidence_item, current_evidence_item_version_id, fields}]} with all ACTIVE roots ordered by created_at ASC then canonical evidence_item_id ASC. Each root is complete; the explicit sibling current ID MUST equal its pointer, and fields MUST project that exact Version. All entries/projections MUST come from one read snapshot. Do not separately repeat kind/status/revision or return full content. Projection has no independent persistence/authority. Empty means []; no pagination/query/search/filter/sort parameters exist. Detail/source inclusion uses exact/full readers, with later Save freshness still required. (Q91.)

## 6. Materials exact structured-source projection

Scope revision **2026-09-21.S2M2-r1**. Earlier published consumer semantics remain effective within their scope. Provenance: [CG04](../../.grill/contract/sl-02-m2/decisions.md).

<a id="evd-015"></a>
**EVD-015.** For each Resume member consumed by MAT-005, Evidence MUST provide exactly evidence_item_id, evidence_item_version_id, Item-owned kind and the corresponding complete EVD-003 fields shape, retaining the requested version's Item ownership and the consumer's member order. It MUST validate that actual structured input without substituting current/ACTIVE versions or requiring unused Evidence.content to parse/pass full body validation. This projection has no business ID, separate persisted authority or public endpoint. EVD-013's full exact HTTP reader and existing Save continue complete owned validation; the new internal projection MUST NOT weaken those consumers. Retired/historical refs remain usable for admitted exact demand; contradictory ownership is not a valid source. Q6/Q14/Q67/Q69/Q74/Q96.

## 7. Deterministic CandidateEvidenceProjection

Scope revision **2026-09-24.S2M1S1-r1**. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="evd-016"></a>
**EVD-016.** CandidateEvidenceProjection MUST be deterministically derived from one exact saved ResumeVersion schema 2, using registered immutable extraction rules. It MUST NOT accept user writes, model splitting, rewritten text, summaries or inference as Evidence. The original Resume remains authority. No union of other Resumes, past defaults, Memory or chat assertions is allowed. Evidence units may exist internally before Profile succeeds; this does not publish a usable partial portrait.

<a id="evd-017"></a>
**EVD-017.** The projection MUST contain exactly schema_version: integer 1, resume_version_id: UuidV4, extraction_key: string, entries: EntryEvidenceUnit[] and blocks: BlockEvidenceUnit[]. Both arrays may be empty and preserve the source order described below. extraction_key is an immutable registered parser/admission-rule identifier matching ^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$; changed rules get a new key. Entry units contain exactly evidence_id, entry_id, kind, fields and content, preserving the complete saved entry and its canonical AST. Block units contain exactly evidence_id, entry_id, block_id and text; text is the exact concatenation of that paragraph/listItem’s run.text, without trimming/normalizing, and parent entry resolves in this projection. Iterate Resume section/member/block/list-item order; identical text in different IDs stays distinct. Every valid paragraph or listItem yields one block; its nested editor paragraph is not another unit. Structured entries without body still yield an entry unit.

<a id="evd-018"></a>
**EVD-018.** An entry evidence_id MUST be "entry/" + canonical entry_id; a block evidence_id MUST be "block/" + canonical entry_id + "/" + canonical block_id. EvidenceRef MUST contain exactly resume_version_id: UuidV4, extraction_key and evidence_id. The full triple is identity: stable logical IDs can continue across versions but do not overwrite older Evidence. Source location is the exact version plus entry_id and nullable block_id (null for entry); character offsets/array indices may aid display but cannot be authoritative. Repeat projection with the same source/rules MUST reproduce the same identities/text.

<a id="evd-019"></a>
**EVD-019.** Retained source and model-visible projection MUST be distinct. Preserve complete original fields/AST/link targets for source display/provenance. Model admission excludes all contacts and Header, structured project_url and hidden LINK.url targets; visible run text and admitted structured career fields remain. Omit excluded fields rather than invent null facts. No URL fetch or inferred repository abilities is authorized. Apply privacy/permission checks before Frame construction and Tool results; excluded content cannot reappear through logging, summaries or fallback.

<a id="evd-020"></a>
**EVD-020.** A frozen consumer MUST resolve EvidenceRefs only inside its selected exact projection and verify parent/version/rule identity. Unknown or mismatched refs fail; never substitute current or search another Resume. Controlled retrieval may read specific blocks, expand to their complete admitted entry context, then inspect more permitted evidence. The portrait page may expose source attribution for a ready pair, but no standalone partial-Evidence interface or independent evidence-history archive is added.

<a id="evd-021"></a>
**EVD-021.** Profile is an index, not a completeness certificate. Missing Profile entries or retrieval misses MUST NOT establish absence. DeepFit must broaden inspection when needed; incomplete access, failed reads or capacity/budget limits produce UNKNOWN, not a definitive gap. A sufficiently inspected negative is only “this source Resume does not express the capability”, never “the candidate lacks it”. Record actual inspected references/coverage in the consumer’s result evidence; a reference alone does not prove content was seen. Future Fit Contract owns assessment/coverage serialization and scoring.

<a id="evd-022"></a>
**EVD-022.** Usable portrait source means at least one valid structured career entry; contacts/Header alone or sections=[] are empty. Deterministic projection of an empty source is legal, but MUST NOT dispatch semantic derivation or establish ready portrait. Non-default sources can be read for direct optimization without publishing global Evidence. Normal reads never create projections, dispatch models or alter default selection.

<a id="evd-023"></a>
**EVD-023.** Automatic whole-pair semantic reuse MUST first derive the target version's exact Evidence and establish all Entry-level equivalence under EVD-024 with a compatible PRO-018 baseline. Rebind every Profile ref into the new exact version and record REUSE provenance; never label it a fresh model result. Excluded-only/contact/Header/presentation changes may qualify. Changed career text/fields invalidate reuse of their owning Entry, not unchanged other Entries; those updates use PRO-019 incremental rebuilding. An unchanged exact-version historical pair may instead reattach under PRO-018 without rewriting it. Explicit full refresh bypasses reuse. Historical Evidence and analysis refs remain unchanged.

## 8. Deterministic Entry diff

Scope revision **2026-09-24.S2M1S1-r2**; accepted CG03S1-Q42/Q43/Q45/Q46.

<a id="evd-024"></a>
**EVD-024.** Compare baseline and target within one Resume using logical entry_id and parent-scoped block_id, not the version-dependent EvidenceRef triple, text similarity or array positions. Entry comparison includes kind, all admitted structured background fields, current ordered Block identities/original text and semantic paragraph/list structure. A new/deleted/changed Block, local semantic order change or admitted Entry-background change makes the whole surviving Entry dirty; an added Entry is dirty, an absent Entry is removed, and exact equal Entries are reusable. Copied equal text with new logical IDs is new content. Keep null/empty distinctions and original text; a hash may accelerate equality only with exact canonical content/rule verification. Apply EVD-019 exclusions before semantic comparison: typography/marks, contacts/Header, hidden link targets and project_url alone do not dirty an Entry. Global Entry/section order and presentation labels do not supply career facts; assembly follows target Entry order without unrelated reanalysis. Structured-only Entries compare their admitted fields and empty body. The complete diff MUST partition every target Entry into dirty or unchanged and identify removed baseline Entries. There is no cross-Entry dependency closure or persistent global capability cache. Actual source loss/corruption fails rather than being classified as an unchanged or absent Entry.
