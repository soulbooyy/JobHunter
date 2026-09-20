# Resume Composition and Manual Lineage Contract

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. This body defines only the SL-02.M1 consumed scope; future consumer scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../design/contract/sl-02-m1-grill.md)

## 1. Document authority and saved shapes

<a id="res-001"></a>
**RES-001.** Resume MUST compose exact Profile/Evidence lineage with its own local expression and presentation. It MUST NOT become a second Candidate Knowledge authority. Manual wording, Header text, formatting and inline links MUST NOT be parsed into facts, automatically grounded or used to expand Evidence membership. Structural/lineage validation is not semantic support: user wording may be unsupported by Knowledge. AI/Advisor support and Fit analysis remain separately owned future scopes; no generic grounding_set_id is required by manual Save. Source updates/retirement MUST NOT implicitly publish a ResumeVersion or clear/rewrite local expression/presentation. (BC1/BC3; Q26/Q31–Q40/Q59.)

<a id="res-002"></a>
**RES-002.** The saved shapes MUST be exactly:

| Object | Fields |
| --- | --- |
| Resume | resume_id: UuidV4; resume_name: string; status: ACTIVE or REMOVED; current_resume_version_id: UuidV4; revision: Revision; created_at: UtcTimestamp; updated_at: UtcTimestamp |
| ResumeVersion | resume_version_id: UuidV4; resume_id: UuidV4; schema_version: integer 1; profile_version_id: UuidV4; header_presentation: ResumeHeaderPresentation; sections: ResumeSection[]; document_presentation: DocumentPresentation; created_at: UtcTimestamp |

Current Version MUST belong to its root. No copied Profile contact, whole Baseline ID, management name/status/revision/current pointer or mandatory general GroundingSet belongs to Version content. root creation MUST include its first Version; saved IDs/fields use COM-038. (Q53/Q59.)

<a id="res-003"></a>
**RES-003.** resume_name MUST use COM-025/026 trim, then 1–120 code points without remaining controls or line/paragraph separators. Duplicate names are legal; identity is resume_id. Rename MUST change only root metadata under SAV-004, not publish a Version, automatically suffix the name or print it as candidate name. Export filename selection is future Materials scope. Lifecycle MUST be ACTIVE→REMOVED only, with no restore; removed roots/history remain readable but content/name edits are forbidden. At most 100 ACTIVE roots are allowed; creation enforces capacity atomically, while removal frees a slot and history/receipts remain retained outside the count. The last ACTIVE Resume MUST NOT be removed. (Q5/Q53/Q64/Q81.)

## 2. Header and sections

<a id="res-004"></a>
**RES-004.** ResumeHeaderPresentation MUST contain exactly optional_items: array of {kind, value}. kind MUST be one of JOB_SEARCH_STATUS, JOB_INTENTION, EXPECTED_POSITION, EXPECTED_CITY, EXPECTED_SALARY, HIGHEST_EDUCATION, GENDER, POLITICAL_AFFILIATION, YEARS_OF_EXPERIENCE; at most one item per kind. Array order is presentation order; duplicates MUST be rejected, not deduplicated. value MUST use fixed Common trim, then 1–200 code points of single-line plain text without remaining controls/line/paragraph separators. No custom kind/label/item ID, extracted fact/ref, rich marks or copied Profile value is admitted. Empty optional_items is legal. These user texts MUST NOT synchronize with Preferences/Knowledge, create hidden Evidence dependencies or enter Candidate Fit authority. Fixed name/phone/email display follows PRO-006. (Q6/Q11–Q16; BC1/BC3.)

<a id="res-005"></a>
**RES-005.** ResumeSection MUST contain exactly kind: EvidenceKind and members: ResumeEvidenceMember[]. ResumeEvidenceMember MUST contain exactly evidence_item_id: UuidV4, evidence_item_version_id: UuidV4 and content: ResumeLocalContent. sections MAY be []; each included formal section MUST have at least one member, and each kind may occur once. Each Item may appear at most once across the Resume. Its exact Version MUST belong to that Item and its kind MUST match the section. Preserve section/member order; no section_id/member_id/position/sort_order exists. A member's content MAY be [] without source fallback or membership removal. (Q15/Q35/Q39/Q54.)

## 3. Local AST and canonical form

<a id="res-006"></a>
**RES-006.** ResumeLocalContent MUST be an ordered array of these exact structures:

| Node | Exact fields |
| --- | --- |
| Paragraph | type: PARAGRAPH; runs: ResumeTextRun[] |
| List | type: UNORDERED_LIST or ORDERED_LIST; items: array of {runs: ResumeTextRun[]} |
| ResumeTextRun | text: string; marks: InlineMark[] |
| Emphasis InlineMark | type: BOLD, ITALIC or UNDERLINE |
| Link InlineMark | type: LINK; url: HttpUrl under COM-042 |

Lists and runs arrays MUST be nonempty. Blocks/items/runs have no business IDs. List styles belong to block type, not marks. A run MAY combine all four marks but MUST NOT repeat a mark type, including LINK. No nested lists, arbitrary HTML/Markdown, images/tables, strike/highlight/subscript/superscript/inline-code or per-span font/size/color is supported. Literal markup-looking characters remain plain text. (Q34/Q40/Q41.)

<a id="res-007"></a>
**RES-007.** Before merging, each raw run MUST be valid COM-025 scalar text, nonempty, and contain no COM-026 controls or U+2028/U+2029, including no CR/LF/tab. Individual runs MUST NOT be trimmed. A run entirely composed of the allowed members of COM-026's fixed whitespace set (excluding prohibited controls/separators) MUST have marks=[]. Preserve those characters exactly, including NBSP/ideographic spaces. The concatenated paragraph/item text MUST pass a Common-trim nonblank check without replacing its text. Invalid raw runs or duplicate marks MUST fail even if later merging could conceal them; do not drop runs or clear marks to repair input. (Q43/Q46/Q47.)

<a id="res-008"></a>
**RES-008.** After raw admission, canonicalization MUST validate/canonicalize LINK.url under COM-042, order marks as BOLD, ITALIC, UNDERLINE, LINK, and merge adjacent runs with identical canonical mark arrays by concatenating text. Merge only within the same paragraph/item; never cross another mark set or a block/item boundary. URL spelling equality is the admitted exact value, not extra host-case/slash normalization. Valid segmentation or mark-order differences alone MUST NOT publish a new Version. (Q40/Q41/Q47/Q57.)

<a id="res-009"></a>
**RES-009.** Each local content MUST have at most 100 blocks, 100 items per list, 10,000 code points per paragraph/item, 50,000 summed text code points, and 256 canonical runs per paragraph/item after merging. Across the document, at most 100 members and 200,000 code points summed from all member.content run.text are allowed. Profile, Header, source structured fields and URL targets do not enter that sum and retain their own bounds. Text limits count retained local text including spaces. Reject excess without truncation/splitting/removing members/font shrinking. Raw request budgets are additional SAV-013 constraints, not satisfied by merging. (Q44/Q62/Q80.)

## 4. Source selection and document settings

<a id="res-010"></a>
**RES-010.** First inclusion of selected Evidence in a Draft MUST initialize local content once from its exact source EvidenceContent: paragraph text becomes one unmarked run; each list item becomes one unmarked run while preserving block/list order. This initializes the Draft only; later edits, including content=[], remain legal and the backend MUST NOT require submitted local content to equal the source. Thereafter local text belongs to Resume and MUST NOT follow source updates. Structured company/school/role/dates/project_url remain provided by the bound exact EvidenceVersion, never private fact overrides. Explicit adoption of a newer source MUST preserve existing local wording/marks/links by default; the UI MUST ask whether to separately replace expression from the new source and do so only on explicit choice. Preservation MUST NOT claim semantic support by the new source. No fuzzy alignment, automatic merge or grounding is performed. (Q36/Q38; BC3.)

<a id="res-011"></a>
**RES-011.** At commit, a new member or switched Evidence reference MUST resolve to the current Version of an ACTIVE Item. Compare against the immediately preceding formal ResumeVersion under root revision admission. An unchanged Item+Version binding already present there MAY remain historical or retired. First/newly switched ProfileVersion MUST likewise be current; unchanged prior Profile binding MAY remain historical. Any race on new/switch admission MUST reject the entire Save without latest substitution or silent reversion. The user MAY cancel a proposed adoption and explicitly retain the previously published binding. New facts created in the editor MUST first commit to Knowledge under EVD-012. (Q37/Q45/Q60; BC3.)

<a id="res-012"></a>
**RES-012.** DocumentPresentation MUST contain exactly the following explicit fields. Defaults initialize a new local Draft, not missing saved fields:

| Field | Valid value | Draft default |
| --- | --- | --- |
| font_family | SOURCE_HAN_SANS, HEITI, SONGTI, KAITI | SOURCE_HAN_SANS |
| font_size_pt | JSON number 12–20 inclusive, multiples of 0.5 | 12 |
| line_spacing_pt | JSON number 14–30 inclusive, multiples of 0.5, >= font_size_pt+2 | 18 |
| theme_color | exact ASCII #[0-9A-Fa-f]{6}, canonical uppercase | #1F2937 |

Numeric values MUST be admitted exactly, treating 12/12.0/1.2e1 equivalently, without coercion/rounding/clamping; string/bool/null is INVALID_TYPE, range/grid violations OUT_OF_RANGE. Color MUST NOT be trimmed or repaired. line_spacing_pt is the entire line-box height, not added leading. Font enums are logical choices, not OS paths; actual renderer mapping/fallback is a renderer responsibility. A4 is fixed; margins, relative headings and section spacing belong to the uniform template. UI MUST use a Color Picker; no per-span typography/color is added. (Q61/Q66.)

<a id="res-013"></a>
**RES-013.** Canonical Resume document equality MUST compare exact profile_version_id, canonical Header/order, sections/order/member exact refs/local content and the four document settings. It MUST exclude management name/root state and external current pointers; JSON spelling/key order is not equality. A change to local expression/presentation/source binding MUST publish only this Resume's new Version under SAV-004; Knowledge/Profile/Baseline/other Resumes remain unchanged. Save success MUST NOT establish PDF/export readiness (MAT-001). (Q26/Q57/Q59/Q94/Q95.)

## 5. Read surface and editor obligations

<a id="res-014"></a>
**RES-014.** GET /api/v1/resumes/{resume_id} MUST return 200 {resume: Resume, resume_version: ResumeVersion} from a single consistent root/current snapshot, including REMOVED roots. GET /api/v1/resumes/versions/{resume_version_id} MUST return the exact retained ResumeVersion with 200, never substitute current. GET /api/v1/resumes MUST return {resumes: complete ACTIVE Resume roots, default_resume_selection: DefaultResumeSelection} from one consistent snapshot, ordered created_at ASC then canonical resume_id ASC, without document bodies or default pinning/reordering. Empty means [] plus initial null/revision-1 selection. No pagination/filter/sort/query/history listing is supported. Missing requested IDs and corrupt internal lineage follow SAV-014/STO-028. (Q71/Q75/Q77/Q78.)

<a id="res-015"></a>
**RES-015.** The frontend MUST provide structured left editing and right live local A4 Draft preview, fixed Profile Header fields, predefined optional Header items, six section categories and semantic paragraph/list editing with the supported local marks. Empty draft section placeholders MAY exist, but the client MUST omit them before formal submission; the backend MUST reject submitted empty sections. Preview updates MUST remain page-local without per-keystroke Save or authority/material publication. Dirty navigation MUST offer Save/Discard/Cancel; failed Save retains the Draft. No autosave/crash-recovery/Resume DSL/source mode is promised. Selecting existing Knowledge or explicitly saving a new fact precedes local expression; cancelling Resume editing MUST NOT undo a prior successful fact Save. Frontend implementation awaits UI design; this does not postpone server admission obligations. (Q5/Q35; UI1/BC3.)
