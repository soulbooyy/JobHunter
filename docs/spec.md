# JobHunter Product Specification

> English is the authoritative documentation language. This document defines intended product behavior; it does not report implemented features or passed tests.

## 1. Purpose, scope, and document authority

JobHunter is a single-user, local-first personal job-search workspace. It helps its user maintain career facts and resumes, acquire and screen Jobs, assess fit, improve resumes, prepare and authorize applications, and track real application outcomes. These are independently accessible tasks with their own prerequisites, not a mandatory sequence that every Job must traverse.

This specification owns product behavior; [Architecture](architecture.md), [Contracts](contracts/index.md), [Acceptance](acceptance.md), and the [other documentation owners](index.md#formal-document-owners) own their respective responsibilities.

**Sources:** Q1–Q6, Q11, Q22, Q26, Q32, Q53, S24.2, S37.1, S38.1; Q/S references identify provenance in the [Decision Register](design/grill-me-design-tree.md).

## 2. Workspace and task organization

### 2.1 Independent capabilities

The workspace supports independent ManualApplicationEntry maintenance, formal Job collection under saved acquisition Preferences, explicit task selection, unified DeepFit backed by independent Candidate Fit and Resume Fit, conversational resume improvement, application preparation, authorized external execution, and application tracking. The user can enter a capability when that capability's own prerequisites hold. A completed Fit is not required before using Resume Advisor or beginning preparation.

Profile, search Preferences, shared career Evidence, Resumes, and application history have distinct authority. A navigation entry may combine them without creating another owner. The single-user boundary does not introduce a unified Candidate Aggregate, Candidate identity layer, or tenant system.

**Sources:** Q1, Q6, Q8, Q16, Q24, Q53, Q112, S17.4.

### 2.2 Five navigation entries

The English names below describe the five accepted entries; they do not decide a new UI-localization policy or rename the labels accepted in S17.2.

| Entry | User task and boundary |
| --- | --- |
| My Resumes | Import, create, manually edit, organize, select a default, and remove formal Resumes; the only manual Resume CRUD surface |
| Candidate Knowledge | Maintain shared career facts and their saved current versions; the only entry for global Evidence/experience deletion |
| Job Pool | Browse and filter formal local Jobs, explicitly collect or refresh, select a Job and Resume for DeepFit, or begin preparation; a separate button opens the user-maintained ManualApplicationEntry view |
| Job Assistant | Conduct ordinary or preparation-originated resume-optimization conversations through the same ResumeAdvisor capability |
| My Applications | Review real application history and progress; its application entry routes to Job Pool for Job selection |

DeepFit is inside Job Pool, not a separate navigation entry. Preparation is a contextual flow after selecting Jobs and choosing to apply, not a top-level page. Job Assistant initially exposes conversational resume optimization only.

Job Pool defaults to a flat Job list. It may offer a Company aggregation view that summarizes related Jobs and returns to the ordinary list with a company filter. This browsing view creates no independent Company authority. Local filters and sorting are view choices, distinct from saved search Preferences.

ManualApplicationEntry records appear only in their separate view within Job Pool, never mixed into the formal Job list or Company projection. They provide a manual application shortcut without another top-level navigation entry.

A one-run Fit selection, Collection admission, beginning preparation, and a real application are different actions. Long-lived pursuit/bookmark intent remains deferred; that exclusion does not exclude the explicitly accepted ManualApplicationEntry capability. See [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1).

**Sources:** Q6, Q23, Q146, Q153, S5.1, S5.3, S17.1–S17.4; S37.1 removes compatibility-only retention of old Shortlisted behavior.

## 3. Candidate Knowledge and Resumes

The SL-02.M1 normative definitions are [Profile](contracts/candidate/profile.md), [Evidence/Baseline](contracts/candidate/evidence.md), [Resume](contracts/candidate/resumes-grounding.md) and [Candidate Save](contracts/candidate/candidate-save.md). The [reviewed scope](progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) separates documentary readiness from implementation; these product rules do not claim available S2 endpoints.

### 3.1 What the user saves

CandidateProfile owns only full_name, phone_number and email in v1 under [CG03-Q7/BC1](design/contract/sl-02-m1-grill.md#cg03-bc1). Name is not split; phone and email are single values. Nickname, GitHub, city, homepage/portfolio, photo, birth date, gender, identity number and detailed address are outside Profile v1. Candidate Knowledge has six Evidence kinds: EDUCATION, WORK_EXPERIENCE, PROJECT, SKILL, AWARD and CERTIFICATION. Work experience includes internships, regular and part-time work; v1 has no separate experience subtype field under CG03-Q19. Future Collection intent belongs to Preferences; Resume Header intentions are independently maintained presentation with no synchronization to acquisition settings.

[CG03-Q48/Q50](design/contract/sl-02-m1-grill.md#cg03-q48) makes EvidenceItem the sole owner of its permanent kind. Each EvidenceItemVersion owns type-specific fields plus the shared Evidence semantic content; Item.kind determines the fields schema. API kind is an optional projection of that owner, never a second Version authority. Reject unknown/cross-kind fields instead of a universal nullable payload. Correct a wrong kind by explicitly creating a new Item and optionally retiring the old one, without automatic field conversion or Resume-reference migration.

[CG03-Q49](design/contract/sl-02-m1-grill.md#cg03-q49) initializes the sole Profile root and a real immutable all-null contact version in fresh SL-02-capable storage. This expresses missing contact values, not identity confirmation, and creates no Resume. Existing older storage uses explicit migration; startup does not repair missing required Profile records. Preferences remains lazily created under its own Contract. [CG03-Q51](design/contract/sl-02-m1-grill.md#cg03-q51) separates Profile root identity/current pointer/revision/timestamps from immutable contact versions; initial root revision and content schema_version are 1. There is no Profile-root deletion in v1; saving null contact values clears content without deleting identity.

CG03-Q52 assigns EvidenceItem ACTIVE/RETIRED status, permanent kind, current pointer, revision and root timestamps; immutable Versions own fields/content and their metadata. Root creation includes its first Version. Retirement retains the last published current pointer while excluding the Item from current Baselines. Each EvidenceItem has one current saved fact version. Older versions preserve exact lineage for saved Resumes and analyses; ordinary new selection uses active current versions, while existing Resume bindings remain valid after newer publication or retirement. For an ACTIVE Item, explicitly saving text equal to an earlier version creates a new version when it differs from current content; this is not lifecycle restoration. [CG03-Q55](design/contract/sl-02-m1-grill.md#cg03-q55) initializes a real empty EvidenceBaselineSnapshot and one durable current pointer. Evidence/Baseline domain owns that pointer; physical storage in a Workspace/config row is optional and creates no Workspace fact authority. Each immutable Snapshot references every then-ACTIVE Item's exact current version once, with unordered membership serialized by Item ID and no copied facts or completeness claim. Real Knowledge changes advance it; Profile/Resume edits and reads do not. Initial schema_version is 1. Explicit migration extends older storage, while normal startup does not repair missing snapshots/pointers.

Evidence preserves coherent experience-level structure without persistent atomic Assertions. [CG03-Q9–Q10](design/contract/sl-02-m1-grill.md#cg03-q9) defines required nullable start_month/end_month on period-bearing records: YYYY-MM or null, unknown start, ongoing end, known start <= known end, same-month allowed; year-only/day dates and ended-with-unknown-end-month are unsupported. Under [CG03-Q25/Q26/BC2](design/contract/sl-02-m1-grill.md#cg03-bc2), required content may be empty; Evidence stores factual text and ordered paragraph/unordered-list/ordered-list structure. Empty blocks/lists/items are invalid. Per-Resume bold/italic emphasis and inline hyperlinks belong to ResumeVersion presentation, not Evidence. Font family/size, line spacing and theme color are controlled at Resume level. Arbitrary HTML/Markdown string representation, images, tables and nested lists remain excluded. CG03-Q32 fixes the Evidence semantic block payload; Q40 defines Resume-local runs/marks separately; Q41–Q44 defines canonical marks/merge, distinct source/local whitespace and per-body capacities, with final admission now in EVD-006–008 and RES-006–009. Blocks/items have no independent business identity; exact-version grounding can still address them.

[CG03-Q18–Q20](design/contract/sl-02-m1-grill.md#cg03-q18) defines education as school/degree/major plus period and narrative, work as company/role plus period and narrative, and projects as name/role/one optional project link plus period and narrative. Education uses seven distinct Candidate values: SECONDARY_VOCATIONAL, HIGH_SCHOOL, ASSOCIATE, BACHELOR, MASTER, MBA and DOCTORATE. MBA remains an independent choice. This records actual education, separate from Preferences' Job-requirement ceiling; future comparison requires an explicit mapping, never enum order. No separate work subtype or project technology-stack field is added; project repository links do not restore Profile GitHub. Scalar requiredness is settled by Q24/Q27 below; body/presentation representations are now defined by the Evidence and Resume normative bodies.

[CG03-Q21–Q24](design/contract/sl-02-m1-grill.md#cg03-q21) completes the field inventories: Skill has a name and narrative; Award has a name, awarding organization, event month and narrative; Certification has a name, issuing organization, acquisition month and narrative. Null award/acquisition month means unknown, not ongoing. There is no automatic proficiency scoring or certificate-expiry management. Education requires school/degree with nullable major; work requires company/role; project requires its name with nullable role/link. These are record-level requirements, not a minimum Evidence-count gate.

[CG03-Q27–Q30](design/contract/sl-02-m1-grill.md#cg03-q27) requires Skill/Award/Certification names, permits explicit null award/certificate organizations and event months, and defines bounded single-line short fields plus exact calendar months without a system-clock-based future-date gate. Structured project_url is an Evidence fact; Resume inline hyperlinks are presentation. They share the existing HTTP(S) URL value validation and do not trigger fetching or reachability checks.

[CG03-Q42/Q44](design/contract/sl-02-m1-grill.md#cg03-q42) defines source-body admission: reject controls/line separators before Common fixed outer trim, reject empty resulting paragraphs/items, preserve internal spaces and avoid Unicode normalization. Blocks/items express breaks; no manual soft line breaks or backend string splitting. Each Evidence body permits at most 100 blocks, 100 items per list, 10,000 text code points per paragraph/item and 50,000 in total. Over-limit input fails Save without truncation; these are content limits, not model-context or page-count guarantees.

**Sources:** Q15, Q54, Q63, Q66, Q75, Q79, Q98, Q108, S15.1. Q75/Q98 replace persistent-Assertion interpretations of earlier records.

CG03-Q91 defines GET /api/v1/evidence-items as a consistent ACTIVE list of complete roots, an explicit current_evidence_item_version_id equal to each root pointer, and that exact Version's fields projection. Do not separately duplicate kind/status/revision, persist another projection authority or include all content bodies. Order by created_at then canonical Item ID ascending, with no v1 pagination/filter/search/sort parameters. Q92 limits ACTIVE Items to 1,000, atomically rejects excess new creation with 409 CAPACITY_EXCEEDED, retains history outside the count and permits update/retire/read and successful replay at capacity. This does not guarantee model admission.

### 3.2 Import, review, and Save

[CG03-BC3/A5](design/contract/sl-02-m1-grill.md#cg03-bc3) supersedes the previous jointly published fact/Resume flow. Uploading a resume produces temporary parsed content and proposed facts, not saved authority. Parsing preserves coherent experiences; matching and optional model assistance cannot auto-merge conflicts, and omission does not delete Knowledge.

Import has two explicit stages: first the user reviews/reconciles and saves Candidate Knowledge; then the user builds/reviews Resume-local expression and saves the Resume. Committed stage-one facts survive stage-two cancellation, browser closure or failure. This is a deliberate product model shared with manual editing, not a claim that simultaneously publishing Evidence and a referencing Resume in one transaction is technically invalid. User fact confirmation needs no third-party proof, extra KnowledgeConfirmation or completeness declaration.

From Resume Editor, selecting existing Evidence captures an exact active current version into the Draft. Under [CG03-Q36–Q37](design/contract/sl-02-m1-grill.md#cg03-q36), its source body initializes local expression once, preserving structure/order without initial inline marks; company/school/role/date facts remain supplied by the exact source. A new member must still reference an active Item's current version when Save commits. Intervening update/retirement rejects the whole Save while preserving the Draft, without silent replacement or omission. Previously published members may retain their unchanged historical references. New experience creation opens a formal Knowledge form and must successfully save Evidence before adding its reference to the Resume Draft. Failure cannot fall back to a private fact; later discarding the Resume does not undo the fact Save. Existing factual source fields/body are edited in Candidate Knowledge through Edit Original Information, not silently overwritten from Resume expression.

[CG03-Q57](design/contract/sl-02-m1-grill.md#cg03-q57) applies revision-before-canonical-equality admission to ordinary new Profile/Evidence/Resume commands: stale revisions conflict even for identical content. Valid no-ops create no version/revision/Baseline; real content changes create fresh versions, including A→B→A without historical reactivation. Root-only rename/lifecycle changes retain their separate version effects. CG03-Q63 delivers only per-Item Evidence create/update/retire in M1, each atomically publishing its required Item/Version/complete Baseline/current-pointer/intent changes. Future Import needing atomic multi-fact confirmation requires an explicit batch Contract, not several independently committed commands presented as rollback-capable. CG03-Q65 content Save replaces complete Profile fields, Evidence fields/content, or Resume Profile-ref/Header/sections/document settings. Missing fields do not preserve old values; valid null/empty collections have explicit clearing meaning, and ordered arrays replace fully without hidden merge. Generated identity/version metadata/current pointers are not client content writes. New Resume supplies its name; rename/lifecycle/default changes have separate operations. CG03-Q68 gives every M1 user mutation a request_id and atomic durable success receipt, including no-ops. Same-request replay returns the original outcome without reexecution or restoring old current state; reuse for a different operation/target/revision/canonical content conflicts. An ordinary new command retains revision-before-equality admission. Matching current content alone is not proof of an interrupted commit. Q73 scopes UUIDv4 request keys/lifetime receipts to the nine SL-02 commands, independently of existing Entry/Preferences protocols. Q74 validates/canonicalizes before receipt lookup, then admits mutable current state only for new execution. Q98 scopes this rule for Evidence Update: read the target Item's immutable authoritative kind after envelope admission to choose field validation; do not infer kind from payload or check revision/lifecycle before replay. A target missing during this kind lookup returns 404 before receipt processing, including a key previously used for another target. Successful replay survives later source publication/retirement without rerunning freshness checks. Explicit uncommitted failures have no success receipt; unknown outcomes retain the original request/key. Q99 requires concurrent equal requests to converge on the original success; a rejection of a retry does not establish that an earlier uncertain attempt failed and does not justify duplicate creation with a new key. Manual Resume Save validates structure and exact source lineage, not semantic factual support for user wording. Unsupported user expression remains document content, never confirmed Knowledge. AI/Advisor-generated rewrites retain explicit support constraints. Leaving a dirty Resume page offers Save/Discard/Cancel; failed Save retains the draft and is not success. Page-local drafts have no crash-recovery/autosave promise; successful separate fact/document commits remain durable.

CG03-Q84 fixes explicit complete command bodies in the decision register, with no generic payload wrapper or client-supplied new business IDs/publication metadata. CG03-Q85 results retain request_id, outcome and operation-specific command-time root/version/selection/Baseline values. Replay reconstructs the original result without consulting mutable current state: later rename cannot alter an old name/revision result; Evidence no-op retains its completion-time Baseline ID; Resume Create retains its completion-time default selection. Result snapshots are command history, not a second business authority. A separate GET supplies current state. CG03-Q90 separates definite rejection/established non-commit from uncertain writes: timeout, connection loss, OUTCOME_UNKNOWN or other 5xx without non-commit proof retain the original request/key for explicit identical retry. Similar current content is not success evidence; do not replace the pending operation with changed input or a fresh-key create. A later GET failure cannot undo confirmed command success. Uncertainty is not a business lifecycle status.

**Sources:** Original Q64/Q70–Q74/Q98/Q108/Q113/Q118/Q146/Q166, scoped by CG03-BC3/A2/A5. No second confirmation object is introduced.

### 3.3 Whole experiences and shared edits

[CG03-BC3](design/contract/sl-02-m1-grill.md#cg03-bc3) replaces mandatory shared whole-body expression with composition over exact Evidence lineage. Candidate Knowledge owns structured facts and source narrative. Resume owns its local wording, paragraph/list/bullet organization and presentation. Local expressions may differ across Resumes and may omit source facts; none automatically updates Knowledge. A Resume is not a subclass or continuously synchronized subset of current Knowledge.

Each saved member binds an exact published EvidenceItemVersion. Later Knowledge edits advance its current version and baseline only; retirement removes it from future baselines but retains referenced history. Existing Resumes remain valid documents with unchanged sources, wording, formatting and hyperlinks. The ordinary add-member picker uses active current Evidence; v1 has no arbitrary history picker. Under CG03-Q38, explicitly adopting a newer source updates the Draft reference and source-provided structured facts, retaining local wording/marks/links. Ask whether the user also wants to replace that expression from the adopted source; replacement requires its own explicit choice. Retained wording is not automatically verified against the new source. Successful Save creates a new ResumeVersion; no automatic grounding, merge, fuzzy matching or presentation migration. CG03-Q45 requires the replacement source to remain active/current at commit. Intervening publication/retirement rejects the whole Save without changing the Draft to another source; the user may explicitly cancel adoption and retain the previously published binding. Unchanged old bindings do not gain a freshness gate.

Resume binds an exact ProfileVersion as well. Profile changes never automatically advance existing Resumes; explicit contact-source adoption creates a new ResumeVersion. The bound full_name/phone_number/email fields have no hide controls or private overrides: populated values render and null renders no placeholder. Profile completeness is not a universal prerequisite; Q49's initial all-null version supplies a real exact reference before the user enters contact values. [CG03-Q60](design/contract/sl-02-m1-grill.md#cg03-q60) checks current-at-commit only for a newly introduced or switched Profile reference. An unchanged reference from the preceding formal ResumeVersion may remain historical. A raced first/switch binding rejects the whole Save, retains Draft and never substitutes latest; users explicitly reselect or cancel adoption.

[CG03-Q59](design/contract/sl-02-m1-grill.md#cg03-q59) fixes the ResumeVersion envelope: resume_version_id, resume_id, schema_version (initially 1), profile_version_id, header_presentation, sections, document_presentation and created_at. Header stores optional items and explicitly supported presentation only; neither Header nor another Version field copies the fixed Profile values. Sections bind selected exact Evidence lineage without a whole-Baseline reference; no mandatory general grounding_set_id or root management metadata is introduced. [CG03-Q61](design/contract/sl-02-m1-grill.md#cg03-q61) requires four explicit settings: font_family = SOURCE_HAN_SANS/HEITI/SONGTI/KAITI (Draft default SOURCE_HAN_SANS), font_size_pt = 12–20 in 0.5-pt steps (default 12), line_spacing_pt = 14–30 and at least font_size_pt + 2 (default 18), and six-digit theme_color with uppercase canonical hex (default #1F2937). line_spacing_pt is the complete line-box height, not added leading. Read never fills missing settings. Renderer maps logical fonts/fallbacks; A4 is fixed and margins/relative heading sizes/section spacing stay template-controlled. [CG03-Q66](design/contract/sl-02-m1-grill.md#cg03-q66) additionally fixes 0.5-pt line-spacing steps and JSON numeric value semantics for both point fields; reject strings/booleans/null and off-grid values without rounding/clamping. Font enums match exactly. Color is exactly ASCII #[0-9A-Fa-f]{6} without trim, canonicalized uppercase; no shorthand/alpha/named colors. The UI uses a Color Picker/palette and submits canonical Hex; backend validation remains authoritative.

ResumeHeaderPresentation retains the nine Q11/Q16 Optional Header kinds, unique ordered kind/value items and bounded user text. Optional Header remains presentation, independent of Preferences and Knowledge. Resume-local paragraphs/lists support BOLD, ITALIC, UNDERLINE and LINK; link display wording may differ from source narrative, without creating Evidence dependencies or writing facts back. No nested lists, arbitrary HTML/Markdown representation, images/tables, strikethrough/highlight/subscripts/inline code or per-span font/size/color. Font, size, spacing and theme are Resume-wide.

[CG03-Q39–Q40](design/contract/sl-02-m1-grill.md#cg03-q39) allows a member's required local content to be empty without removing membership or falling back to Evidence body. Nonempty content cannot contain empty blocks/lists/items. Local paragraphs contain ordered text runs; list blocks contain ordered items with runs. Runs carry the four supported inline marks, including at most one LINK; ordered/unordered lists are block types, not marks. Blocks/items/runs have no business IDs. [CG03-Q41–Q44](design/contract/sl-02-m1-grill.md#cg03-q41) requires marks arrays, rejects duplicate mark kinds, orders BOLD/ITALIC/UNDERLINE/LINK and merges adjacent identical canonical marks only within a paragraph/item. Shared URL validation introduces no additional URL-equivalence rewriting. Local text is not trimmed; empty runs/arrays are rejected, runs consisting only of permitted Common fixed-set whitespace require no marks under CG03-Q46, and each joined paragraph/item must pass a Common-trim nonempty check without replacing the original text. Controls/line separators are invalid. Each local member body permits 100 blocks, 100 items per list, 10,000 text code points per paragraph/item, 50,000 total text code points and 256 canonical runs per paragraph/item. LINK URLs keep their existing separate limit. CG03-Q46 preserves permitted NBSP/ideographic and other fixed-set whitespace without character conversion. CG03-Q47 validates each raw run before merging: invalid text, duplicate marks or marked whitespace-only runs cannot become valid through concatenation. Only valid runs proceed to canonicalization and the 256-run check; the server never repairs invalid runs. [CG03-Q62](design/contract/sl-02-m1-grill.md#cg03-q62) additionally limits the document to 100 members and 200,000 code points summed only from local run.text. Profile/Header/structured source fields/URL targets have independent limits and are not counted again. Excess rejects Save without truncation/removal/font shrinking; this is storage validity, not a page/model-capacity promise. Raw-node and transport budgets are defined by SAV-012/013.

[CG03-Q53/Q54](design/contract/sl-02-m1-grill.md#cg03-q53) fixes Resume root identity/name/ACTIVE-or-REMOVED status/current pointer/revision/timestamps, with first Version published at creation. resume_name is management-only: Common-trimmed length 1–120 code points, no controls/line separators, duplicates allowed without suffixes; concurrency-checked rename does not create ResumeVersion. Sections contain kind and ordered members; each member contains evidence_item_id, evidence_item_version_id and local content. The Version must belong to the Item and the section kind must agree with the Item-owned kind. No separate section/member ID or stored position field is introduced. Resume owns section/member order. At most one section per Evidence kind and one membership per Item remain; membership is whole Item lineage, not mandatory verbatim rendering of its bullets. Draft may have empty section placeholders; frontend omits them before Save and backend rejects submitted empty sections. Formal sections may be an empty collection.

The editor retains structured editing beside local live A4 preview, with six-kind Add Experience controls offering Select from Knowledge or Create Fact. Preview reads local draft state without per-keystroke writes, formal authority or material-readiness claims. Saving local expression/presentation affects only this Resume, never other Resumes or baseline. Durable saved-source preview/PDF is SL-02.M2; reuse the rendering basis where feasible. No source DSL is required and this writeback does not implement frontend.

**Sources:** CG03-BC3/A1–A3/Q31–Q35 supersedes affected Q96–Q98/Q108/Q114/Q118–Q119/Q163 and CG03-BC1/BC2; surviving Header/editor rules retain their earlier locators.

### 3.4 Defaults, removal, and empty states

The first formal Resume becomes the Workspace default. With multiple Resumes, the user can switch the default. [CG03-Q70](design/contract/sl-02-m1-grill.md#cg03-q70) makes frontend choose the next ACTIVE Resume in canonical list order, or the previous ACTIVE item when no next exists, and clearly display that exact replacement in the confirmation dialog. No manual replacement choice is required. The confirmed remove command sends replacement_resume_id; backend atomically removes the target and switches the default. If the replacement is no longer ACTIVE, the default changed or another concurrency precondition fails, the whole operation fails without automatic reselection. [CG03-Q71](design/contract/sl-02-m1-grill.md#cg03-q71) orders ACTIVE roots by created_at ascending then canonical resume_id string ascending; equal-time UUID order is deterministic, not temporal. Rename/document edits/default switching do not reorder or pin the default. Confirmation uses the list at dialog opening; later insertion alone does not replace or invalidate the confirmed target. [CG03-Q72](design/contract/sl-02-m1-grill.md#cg03-q72) defines the small Workspace DefaultResumeSelection state: nullable default_resume_id plus independent revision, initially null/1. First creation and real default changes increment once; matching-revision same-target choice is no-op, while stale revision conflicts even after A→B→A. Ordinary Resume edits/renames/non-default changes do not advance selection revision. This creates neither a Domain Aggregate/configuration framework nor a selection-history version family. CG03-Q76 checks target Resume revision after a receipt miss, then returns successful no-op for an already REMOVED matching root before checking current default/replacement state. ACTIVE removal checks selection revision even for a non-default target; default removal requires the confirmed different ACTIVE replacement, non-default removal requires null. Replacement rename/document edits alone do not conflict. Any required revision overflow fails atomically; a valid no-op still succeeds. CG03-Q77 returns complete ACTIVE roots and default selection together from one consistent GET /api/v1/resumes snapshot, without document bodies, pagination or filters. CG03-Q81 caps ACTIVE Resume roots at 100; removed roots/history/receipts do not consume slots or get erased. Check new creation capacity atomically, return 409 CAPACITY_EXCEEDED without partial writes, and allow existing edits/removal at capacity. Successful replay consumes no new slot. CG03-Q84 allows concurrent initial Creates to succeed: the first successful transaction establishes default null→new Resume and selection 1→2; a later commit preserves that default rather than rejecting its stale initial null observation. Other admission rules still apply. Non-default removal leaves the default unchanged; default selection does not create a ResumeVersion or adopt newer sources. Removing the last ACTIVE Resume is prohibited. Root status becomes REMOVED while exact versions/history remain retained. Retiring the final ACTIVE EvidenceItem instead produces another empty Baseline; the domain-owned current-baseline pointer remains non-null. A workspace that has never created a Resume can still exist; resume-dependent Assistant work then provides import/create guidance before model execution.

Deleting a Resume removes it from current selection without deleting shared Evidence or historical materials. Continuing a chat that used a removed Resume requires explicit reselection rather than a silent default switch.

Removing an experience in My Resumes changes only that Resume's selection. Global Delete/Retire Evidence is available through Candidate Knowledge. It may show referencing Resumes as impact information, but removes only current Knowledge membership and advances the baseline. Referenced immutable versions remain available for existing Resume/Analysis lineage; no Resume is updated or stripped of a member. Ordinary retirement is not privacy revocation or comprehensive erasure. Resumes that do not include the Item are unaffected.

Logical deletion preserves historical facts, Resumes, analyses, PDFs, and completed applications. Historical readability or download availability does not authorize new formal use. Ordinary removal is not comprehensive physical personal-data erasure.

Empty saved Knowledge or Resume content is permitted. Retired facts must not silently remain in current Knowledge; exact historical lineage remains retained under EVD-011. The product must not invent placeholders to keep a task ready. A task missing its required inputs fails before model execution with an appropriate prerequisite explanation. Exact per-function required inputs remain Contract work; there is no universal contact/Profile requirement or mandatory experience count in this specification.

**Sources:** Q88, Q93, Q100, Q108, Q151, Q153–Q154. The prohibition on deleting the last Resume concerns its available root, not a requirement to keep career content in it.

[CG03-Q64](design/contract/sl-02-m1-grill.md#cg03-q64) makes retire/remove one-way in v1. Retired Evidence cannot be updated; removed Resume cannot be edited/renamed. Objects and versions remain available for historical lineage reads under applicable access rules. Ordinary Save never restores availability; future restore requires an explicit new capability. A new repeated retire/remove with matching current revision is a successful no-op; stale revision conflicts, while same-request replay has its separate protocol.

### 3.5 Current use, grounding, and generated materials

Exact lineage establishes which saved sources a Resume selected, not proof that its user-authored expression is factually supported. Under BC3/A2 manual Save has no automatic semantic-support gate. AI-generated rewrites retain a separate support policy. The former universal ResumeGroundingSet/current-fact gate must not be retained implicitly; its replacement role/name/representation remains Contract work.

A newer or retired Evidence source does not make an unchanged bound Resume stale/corrupt or inherently ineligible for Resume Fit, rendering/export or Preparation. These consumers still enforce their own exact-version, permission, availability and readiness rules. Profile changes likewise do not invalidate unchanged Resume materials. Explicitly changing the Resume creates a new document version; old materials/results cannot be relabeled as evaluating or rendering it.

Candidate Fit binds the admitted complete current Knowledge baseline, so real Knowledge changes affect its current compatibility. Resume expression, formatting, Header and ordering changes do not advance that baseline. Resume Fit binds the exact document and never supplements missing expression from Knowledge; differing Candidate/Resume outcomes in either direction are valid.

CG03-Q95 places actual render demand, configuration, durable intent and rendered-output delivery in SL-02.M2. M1 supplies exact saved sources/currentness and local Draft preview; Save does not promise PDF/export readiness or create speculative render work. When an actual M2 demand requires updating on Save, the necessary intent joins that transaction, never a lossy post-commit notification. Demanded rendering remains post-commit, exact-source-bound and independently recoverable. Necessary durable intent commits with the command that actually changes the relevant authority; Knowledge/Profile current-pointer movement alone creates no Resume rerender/invalidation obligation. Keep compatible output and work for unchanged documents. A genuine superseded Resume demand cannot publish as current, and render failure leaves committed facts/documents intact.

**Sources:** CG03-BC3/A1–A4 supersedes affected Q75–Q77/Q87/Q108/Q114/Q118–Q119/Q151/Q153 current-fact and propagation clauses; Q147/Q150/Q152/Q165 demand/recovery discipline remains.

SL-02.M2 now scopes this demand to an explicit exact saved ResumeVersion and immutable rendering configuration. It supports a multi-page A4 PDF or one long PNG assembled from the same complete A4 pages. It does not introduce follow-current subscriptions, cancellation or MaterialBundle. A successful demand receipt confirms acceptance, while its separate result reports fulfillment or stable failure; readable Artifact metadata and actual downloadable bytes are distinct. Ordinary newer Save/removal does not revoke already accepted exact demand, and old output cannot be relabeled as the new version. New generation still requires an ACTIVE owning Resume and actually needed historical sources, without readmitting Evidence as ACTIVE/current. No unused Evidence expression becomes a rendering prerequisite. The conditional future Save-plus-intent invariant above remains intact; this M2 exact-only consumer adds no intent to Candidate Save. See [Materials](contracts/applications/materials.md#mat-004) and [CG04](design/contract/sl-02-m2-grill.md).

## 4. Jobs, Preferences, and collection

### 4.1 Job identity and manual entry

One reliable platform source identity identifies one Job. Semantic changes to that source's content create immutable JobVersions. Similar listings from different sources remain separate; v1 performs no cross-platform or historical Job merging.

ManualApplicationEntry is an independent mutable record outside the formal Job family. It saves only a company, role title and user-provided application URL as business content. The user can repeatedly edit it through explicit whole-record Save, physically delete it and click its action to request a new browser tab at the saved URL. A neutral waiting page resolves the displayed revision before external navigation; only navigation initiation is reported. It has no JobVersion or immutable content-version history. Saved entries require all three business values; removal physically deletes the entry while minimum create receipts remain for replay protection. Exact fields, validation and operation semantics are owned by the [Entry Contract](contracts/jobs/manual-application-entries.md).

An entry is not a Requirements, DeepFit/Candidate Fit, Resume Fit, Job-targeted Advisor, Preparation, automatic Execution or Application History target. Browser opening does not create a Job, collect its content, convert the entry into a Job, or establish any application fact. Formal consumers continue to require their own eligible Job/JobVersion inputs.

Formal BOSS collection admits only validated complete details/JD, creating a Job and its first immutable JobVersion together. There is no Manual root-only exception in the formal Job family. Complete canonical JD and exact immutable content snapshots remain required.

**Sources:** Q12–Q13, Q17, Q44, Q48–Q49, S9.1, with later [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1) replacing the Manual Job path while retaining formal Job completeness/version/history invariants.

<a id="42-preferences-and-deterministic-quickscreen"></a>
### 4.2 Preferences as future collection intent

One global PreferenceSet owns durable user intent for future automatic acquisition. The six dimensions are job search keywords, accepted work cities, minimum salary, recruitment types, excluded companies and maximum required education. Work mode remains deferred. No personal target defaults or soft weights are invented.

Before first formal acquisition, the user must explicitly choose a legal value for each dimension and successfully Save one complete immutable PreferenceSetVersion. Missing/unfilled dimensions or an all-empty object cannot represent valid unrestricted configuration. Keywords require at least one valid term; each of the other five dimensions permits an explicit UNLIMITED choice, mutually exclusive with its concrete effective values. The five fields use explicit UNLIMITED/LIMITED mode objects under CG02-Q16; missing, empty or simultaneously active concrete/unlimited values reject. Unfinished configuration and explicit no-constraint choices remain distinguishable. This requires complete user choices, not a restrictive predicate in every dimension.

`target_job_keywords` contains user-maintained terms for source searches, not terms that every returned Job title must contain. A Java developer returned for a backend search cannot be rejected merely because its title omits the search term. First release does not automatically expand terms into synonyms or model-generated queries. Preferences does not own query composition, OR execution, search count, deduplication or source encoding.

City intent is city-level, without inferred neighbouring cities, districts or commute distances. Salary intent is a minimum CNY pre-tax monthly base amount, without automatic annual/day-rate, bonus/equity or extra-month conversion. Recruitment types support multi-selection of CAMPUS, INTERNSHIP, EXPERIENCED and PART_TIME; unrestricted is not a persisted type enum member. These are user acquisition categories, not a claim of one mutually exclusive source field. Company exclusions use complete display-name equality after fixed outer trim without case/Unicode/width or suffix/alias conversion, without implicit fuzzy/substring/affiliate matching. `max_required_education` limits a Job's required education; MASTER means master's and below, not the Candidate's own credential. CG02-Q18 defines six ordered education levels, grouping high school and secondary vocational/technical school into UPPER_SECONDARY; source qualification mapping remains later Collection work.

The canonical dimension fields are `target_job_keywords`, `accepted_cities`, `minimum_salary`, `recruitment_types`, `excluded_companies` and `max_required_education` under [CG02-Q11–Q15](design/contract/sl-01-m2-grill.md#cg02-q11). Keyword/city/company controls add one structured item at a time and display removable Chips; there is no comma-string parser. The other five dimensions have explicit UNLIMITED checkboxes that disable their concrete controls. Salary UI accepts ordinary integer input in CNY/month; the backend accepts exact JSON integer values in [1, 300000], including equivalent decimal/exponent spellings, without coercing strings or rounding invalid fractions; recruitment types are multi-select and education is single-select. Short UI labels use explanatory text to distinguish monthly base pay and Job-required education from Candidate credentials. Any invalid field makes the complete Save fail atomically; backend validation cannot be replaced by UI checks. Inactive unsaved drafts are not authoritative constraints.

Only successful explicit Save publishes authority. Ordinary Save checks revision before canonical comparison; stale revision conflicts even for equal content. A current-revision canonical no-op creates neither a version nor a revision increment. A real change publishes a new immutable PreferenceSetVersion. Keyword/city/type/company values are unordered sets; backend field-specific normalization/deduplication and deterministic ordering establish equality, so order/duplicate-only differences are no-ops. Keywords use fixed Common outer trim without case/Unicode/width/internal-space or synonym conversion. Cities/companies use the same fixed trim and preserve other text. Text sets use Unicode code-point order; recruitment types use their declared enum order. CG02-Q20 fixes item/canonical-set limits; complete request/error/retry representation remains Contract work. PreferenceSet is lazily created with its first immutable version and current pointer in the first successful complete Save; Workspace initialization creates none, and failed first Save leaves no root. First publication starts revision at 1; real changes increment it, while maximum revision still permits a valid no-op. Successful immutable versions retain complete content for the Workspace lifetime, without automatic expiry, single-version deletion or rollback. Reading current Preferences before first Save succeeds as NOT_CONFIGURED and creates nothing. Each logical Save has a request identity for durable successful replay, which returns its original result without restoring an old current pointer. Successful request receipts, including no-op receipts, are retained for the Workspace lifetime and committed atomically with their outcomes. Current reads return a consistent root/version pair; exact-version reads never substitute current. Save success distinguishes CREATED, UPDATED and UNCHANGED and replays the original result. The actual [Preferences Contract](contracts/candidate/preferences.md) now owns these operations and their detailed error/receipt interfaces. No named SearchProfiles or parallel long-lived configurations are introduced.

**Sources:** Q45/Q55/Q56/Q161 and S17.1 as explicitly revised by [CG02-BC1](design/contract/sl-01-m2-grill.md#cg02-bc1), [CG02-Q6–Q10](design/contract/sl-01-m2-grill.md#cg02-q6) and [CG02-S1](design/contract/sl-01-m2-grill.md#cg02-s1). The former M2 QuickScreen, current-Preference re-screening and CG02-Q2 versioning deferral are superseded.

### 4.3 Local browsing and explicit collection

Collection consumes one exact complete user-confirmed PreferenceSetVersion. It determines source-capable query pushdown and necessary deterministic candidate admission under the Collection/Job Contracts. Unsupported query parameters do not permit silently inventing user intent. Search-result title mismatch alone is not an admission conflict. Source mapping and admission policy are not owned or implemented by M2 Preferences.

Before fetching details, Collection applies its defined deterministic admission checks wherever available list metadata supports them; confirmed rejection prevents detail access and creates no formal Job. Missing or incomparable source information cannot masquerade as a confirmed conflict or satisfaction. Complete validated detail/JD remains necessary for formal Job admission. Rejected listing content is not retained as a recoverable dataset; audit retains admitted operational usage/reasons/failures/risk/stop information. Collection does not parse Requirements. The accepted salary interval comparisons in CG02-Q8 belong to future Collection admission policy, not a Preferences predicate or a standalone QuickScreen.

Normal Job Pool browsing uses saved local data. Initial acquisition after complete configuration and explicit collection/refresh are platform-access entries; merely opening the pool or saving Preferences does not fetch the platform. Every active CollectionRun keeps its original exact PreferenceSetVersion; later saves affect future Runs only. Explicit stop prevents subsequent accesses, preserves committed partial Jobs and causes no automatic restart.

Changing Preferences must not delete or hide existing formal Jobs, add preference-conflict status, change their authority or rewrite their acquisition history. Current Preferences are not a continuing eligibility invariant for RequirementParse, Fit, Preparation, Execution or Application History; those consumers retain their actual source, content, material, permission and safety requirements.

JobPoolViewFilter is independent browsing/query state over existing Jobs. Company/role query, city, batch, industry and update-time filters are examples, not a finalized schema. View filters do not modify Preferences, create PreferenceSetVersion, affect future Collection, delete or mutate Jobs, or generate QuickScreenResult. They may remain frontend state or be carried as backend query parameters; persistence and concrete fields belong to the later query/UI Contract under jobs-screening. No new Company authority or query document is introduced.

**Sources:** Q49/Q161 and S9.1, with [CG02-BC1](design/contract/sl-01-m2-grill.md#cg02-bc1) superseding current-Preference formal-Job filtering while preserving exact collection provenance, complete admission, stop and retention boundaries.

### 4.4 Freshness and availability

The pool distinguishes when content was captured, when a source listing was last reliably observed, and when availability was directly verified. Unchanged content can update observations without creating a new JobVersion. Semantic change creates a new version without rewriting old consumers.

Old data can be stale without being closed. Absence from one search result is not closure. Reliable source evidence of closure blocks new automatic application but retains the Job and history. These freshness/availability meanings apply to formal Jobs, not ManualApplicationEntry. User reports remain distinguishable from direct source verification; formal content eligibility, material readiness and application progress remain separate concerns. [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1) replaces the former Manual Job UNKNOWN rule.

**Sources:** Q7, Q44, Q48, Q50.

## 5. Requirements and independent Fit analyses

### 5.1 Shared on-demand requirements

Requirement parsing is an independent, reusable capability for an exact complete formal JobVersion. ManualApplicationEntry is ineligible for parsing and both Fits. Fit and Job-targeted Advisor share dependency preparation: reuse a compatible RequirementSet or obtain one through an independent RequirementParse task. Neither requires the user to run another Fit first. General Advisor work without a concrete Job requires no RequirementSet.

Parsing interprets the full exact JD through a bounded model extraction and deterministic validation. One validation-guided repair is allowed at most; continued failure stops the affected work with a clear dependency explanation and a check/correct/refetch path. It cannot save an untrusted result or let downstream tasks score partial or invented requirements. Structural validity is not a guarantee of zero semantic omissions; uncertainty must remain visible rather than guessed away.

A validated Set can become the current default while past consumers retain their exact Set. It remains reusable even if downstream work fails. The two Fits and Job-targeted Advisor use that exact Set as their sole Job-requirements input; they do not reread JD to invent a different interpretation. A structurally valid result with no usable assessment targets fails before Fit, rather than yielding a perfect empty-set score.

Concurrent consumers can share a single compatible parse producer. Reuse does not duplicate parsing charges. Cancelling a waiter does not cancel the producer; producer failure or cancellation exposes unavailable dependency rather than silently transferring ownership or reparsing for another waiter.

**Sources:** Q10, Q14, Q58–Q59, Q110–Q111, Q117, Q142, Q144, Q159, Q171.

### 5.2 What each Fit answers

DeepFit(Job, Resume) is one product entry over two independent internal capabilities under CG03-BC3/A4:

| Capability | Question and admitted inputs | Meaning of its result |
| --- | --- | --- |
| Candidate Fit | How do current saved Candidate facts support this Job's Requirements? Uses exact RequirementSet and the exact current saved Evidence baseline with admitted facts | A bounded assessment of saved Knowledge against the Job, not a statement about every capability the person possesses |
| Resume Fit | How does this exact eligible formal Resume support this Job's Requirements? Uses exact RequirementSet, admitted Resume-local expression, and necessary exact lineage metadata | An assessment of what that Resume expresses; grounding cannot supply facts absent from the Resume to improve the result |

Each has independent execution, result identity, failure, explicit retry, and history. Neither consumes the other as a prerequisite. Both can exist without a numerical ordering between them. There is no durable ResumeCoverageAnalysis, coverage ratio, capability-times-expression formula, or score-gap authority.

The user selects a Job and Resume for DeepFit, not separate Candidate/Resume actions. Both sides consume one exact RequirementSet and separately frozen baseline/document inputs. Display assessments side by side for each Requirement with their own source versions and explanations. One side may succeed while the other fails, is oversized or is unavailable; preserve that success and offer side-specific retry inside DeepFit. Internal Candidate execution needs no Resume, while this product entry does. Exact reuse/rerun selection controls remain Contract work; do not silently pair incompatible RequirementSets.

**Sources:** Q19, Q24, Q35, Q112, Q115, S5.3, S22.1. CG03-BC3/A4 supersedes separate product entry selection from Q112/S22.1; independent analysis identities, scopes and outcomes survive.

### 5.3 Assessment meanings and scores

The accepted assessment vocabulary has the following user-visible meanings. This table explains existing semantics; detailed output representation remains Contract work.

| Meaning | Product interpretation |
| --- | --- |
| MATCHED | The inspected task-specific content supports the Requirement, with support references |
| PARTIAL | The inspected task-specific content supports only part of the Requirement, with references and explanation |
| MISSING | Candidate Fit found no supporting fact in its saved admitted Knowledge scope; Resume Fit found no supporting expression after complete inspection of its exact admitted Resume content |
| UNKNOWN | A reliable determination cannot be made, including relevant privacy exclusion, incomplete inspection, truncation, insufficient inputs, or unverifiable output |

A Candidate negative does not imply a Resume negative or vice versa, and neither proves real-world incapability. Full Context is not sufficient proof of inspection: all necessary Requirements, admitted content, support references, and output must be checked against the actual assessment-producing model input. Incomplete inspection must not become MISSING. Claims about missing support must remain bounded to the inspected materials and their demonstrated reliability.

Models produce grounded assessments. A versioned deterministic ScorePolicy derives any total score for ranking/display. Critical hard gaps cannot be cancelled by many minor matches; UNKNOWN is not mechanically converted to a fixed low score. Scores do not replace reasons, risks, and support.

A valid analysis can have no defensible comparable total score. Show it as unscored with its assessments and reasons, not as zero, failure, an inherited score, or an ordinary numeric ranking entry. Preserve the original result and its score policy, including an originally unavailable score. Explicit rescoring can derive a separate comparison under a common policy without new semantic analysis. If required dimensions are unavailable, do not guess them. Weights, thresholds, and exact score-availability representation remain deferred.

**Sources:** Q46, Q51, Q72, Q82–Q83, Q112–Q115, Q168. Q115 removes the older Resume-specific NOT_PRESENT interpretation; Q168 distinguishes unscored analysis from Q171's unusable target.

### 5.4 Execution, compatibility, and failures

Selection freezes the known requested inputs. Missing dependencies are prepared before the complete per-analysis request is frozen. Before dispatch, revalidate source/dependency compatibility, task-specific eligibility (current baseline for Candidate, exact saved lineage for Resume), and permissions. Inputs never silently follow newer versions during preparation or execution; incompatible changes stop the affected task and require a new request against current inputs. Failed final validation after a model call preserves actual usage and audit without publishing an invalid formal analysis.

Different targets may execute concurrently. For one target, only one effective analysis can be active, including across tabs or repeated requests. The displayed current result is the latest successful compatible analysis. A failed rerun preserves an older still-compatible success and exposes the failure separately. Stale output cannot become current.

v1 Fit uses complete admitted inputs, one structured evaluation, and at most one validation-guided repair per independent task, subject to overall limits. There is no autonomous Evidence retrieval loop. If the complete input plus required reserves cannot fit, stop before the model call with a capacity explanation. Do not truncate facts, summarize protected inputs into a supposedly complete analysis, automatically switch models, or use deferred RAG. An already-supported larger-context configuration may be selected explicitly for a new attempt; the user need not delete genuine facts. An independently feasible Resume Fit may continue even if Candidate Fit is oversized.

Failures, cancellation, stale inputs, insufficient budget, and uncertain execution are not negative Fit evidence. Independent completed results and successfully parsed Requirements remain available. Budget exhaustion distinguishes work not run from work completed.

If permission for protected exact input is revoked after freezing, end that affected task. Do not shrink its scope and continue, use revoked data in later calls, or publish a new current analysis. A newly admitted scope requires a new task. Initial privacy exclusions instead retain the established UNKNOWN semantics.

**Sources:** Q35, Q40, Q76, Q108, Q110, Q113, Q116, Q121–Q124, Q135, Q168, Q172, S22.1, S24.1; see the design records for [Context](design/harness/context.md) and [Budget](design/harness/budget.md).

## 6. Job Assistant and Resume Advisor

### 6.1 Entry, context, and discussion

One ResumeAdvisor capability supports ordinary and preparation-originated conversations in Job Assistant. Each entry from Preparation starts a new ordinary chat with explicit Preparation, Job, and selected Resume references. Existing chats continue through conversation history; there is no compatible-targeted-Session discovery or separate Advisor implementation.

General optimization uses a formal saved Resume and does not infer a concrete Job from a job-family request. Without any formal Resume, preflight provides import/create guidance before execution. Ad hoc chat-file optimization is outside v1. Compatible Candidate Fit or Resume Fit results may inform advice, but neither is mandatory. Comparing their per-Requirement findings is an optimization hint, not a new persisted coverage result.

Discussion/read context uses this precedence: the current explicit Resume request, the Session's explicitly adopted Resume, the originating Preparation's selected Resume, then Workspace default. Changing the default does not silently retarget an existing conversation. Reading or comparing another Resume alone is not an editing-target switch.

Advisor reads authorized business information when needed. Entry references do not mean full Resume, Knowledge, JD, or application history has already been sent to the model. Actual exact reads remain recorded and pinned within the task; concurrent unrelated edits do not silently replace them.

The user can discuss new career facts immediately, including possible corrections to saved facts, without repeated Save prompts. Suggestions distinguish saved factual support from actual user statements in this Session. Conversation alone does not save Evidence, edit Preferences, create Memory, or make unsaved statements eligible for formal Fit. A model cannot invent a source or user confirmation.

**Sources:** Q24, Q41, Q47, Q52, Q58, Q85, Q88–Q89, Q93–Q94, Q128, Q133, Q138–Q139, Q143, S17.3. Q146 removes earlier Advisor working-draft clauses, including those in Q85.

### 6.2 Applying a change to a formal Resume

Advisor produces discussion and Suggestions, not an editable persistent ResumeDraft. A Suggestion cannot be independently exported or submitted as application material. Manual Resume CRUD remains in My Resumes.

Formal apply uses a separate target rule: the Resume explicitly specified in the current instruction, otherwise the Workspace default. Prior discussion or Preparation selection does not authorize an implicit apply target. The preview must make the actual target and default selection clear.

Before presenting a ChangeProposal, read and validate that target's exact version and build its own before/after changes. Do not infer a separate suggestion-source Resume, transplant another Resume's patch by changing its identity, or copy experiences the user did not request.

The non-editable preview shows the actual target/version and concrete supported local expression/presentation change. One confirmation authorizes that operation through Resume Save; it does not authorize Knowledge edits or updates to other Resumes. New/corrected facts require an explicit Knowledge flow first. AI rewrites retain factual-support constraints even though manual wording is not automatically verified. There is no second Advisor draft Save. Revised content, target changes, or revision conflicts require a fresh preview; previous confirmation cannot authorize different changes.

Generating and displaying the Proposal ends that foreground Turn and Run. Pending confirmation is durable interaction state and leaves the Session free for further discussion or abandonment. Application validates and applies the exact confirmed operation without a model reinterpreting consent. Any later conversation uses new bounded execution.

The authoritative mutation result determines whether the change was saved. If later narration fails, the UI reports saved changes and an unfinished reply. Retrying or recovering the same confirmed Proposal cannot create duplicate fact or Resume versions. Streamed claims of success are not proof of commit.

**Sources:** Q96, Q108, Q113–Q114, Q118–Q119, Q128, Q133, Q146, Q148–Q149, Q156, Q158. Q149 controls apply target; Q158 controls the wait boundary over earlier same-Run continuation assumptions.

### 6.3 Conversation progress, waiting, and deletion

A Session has at most one active foreground Turn. New input waits or follows an explicit stop of that Turn. Different Sessions and independent supporting tasks may execute concurrently.

Waiting for a missing RequirementSet is visible dependency preparation inside the same active foreground Turn, bounded by its deadline and cancellation. It is not a model polling loop or a live wait for user confirmation. Dependency failure ends waiting explicitly; Advisor cannot substitute its own JD interpretation or silently take over the parser.

Deleting a Session cancels active foreground work and invalidates still-unconfirmed originating Proposals. Old IDs, restored pages, or recovery cannot reactivate them. Concurrent deletion and confirmation permit only the outcome that wins the atomic eligibility check. Already committed facts, Resumes, applications, and necessary result history survive. A new desired change requires a new Proposal in a valid context.

**Sources:** Q47, Q52, Q122, Q142, Q144, Q155–Q159, Q167.

## 7. Application preparation and materials

### 7.1 Entry and editable preparation

Selecting one or more eligible formal Jobs in Job Pool opens preparation. ManualApplicationEntry browser navigation does not enter this flow. Each Job/channel has an independent preparation instance. Reentry defaults to resuming an unfinished instance, preserving selected materials and manual Greeting while rechecking eligibility, readiness, and approval compatibility. It does not silently upgrade selected exact inputs. Repeated clicks or request retries do not duplicate creation; if several resumable instances exist, the user chooses explicitly. Explicit new preparation or a later reapplication starts a separate chain.

Preparation selects and displays rendered formal Resumes; it does not edit Resume body text or own an Advisor draft. Concurrent edits must detect conflicts instead of overwriting another change. The product need not keep immutable history of every reversible Preparation edit, while referenced formal assets and execution snapshots retain their history.

Optimization opens the same Job Assistant capability. Returning a newly saved Resume is a separate explicit adopt-and-return action. It updates only the selected Resume reference and related lineage/material readiness, preserving Greeting and unrelated edits. A conflict preserves the saved result, reloads current Preparation, and requires explicit readoption. Saving in Advisor does not silently update Preparation or authorize execution.

**Sources:** Q16, Q25, Q30, Q36, Q42, Q91, Q108, Q118, Q146, Q162.

### 7.2 Greeting and material confirmation

Each Preparation begins with one fixed generic Greeting that the user can edit manually. The default is not personalized from Job, company, Resume, Knowledge, or Memory and requires no model call. Greeting has no independent template library or version-history feature.

Required rendered materials must exist and actually be viewable before material confirmation. MaterialApproval binds the displayed frozen artifact, its exact sources, and actual Greeting, not merely a Resume's name or version. Rerendering cannot replace an approved artifact in place. Changing selected material requires compatibility checks; changing Greeting requires reconfirmation. Identical visible bytes do not bypass exact source, permission or approval checks. Older/retired Evidence or an older bound Profile alone does not invalidate the selected Resume under BC3.

Readiness reflects required current, eligible, validated, rendered, and confirmed materials. A missing or failed required render blocks readiness without undoing saved career facts. Detailed channel prerequisites and material formats remain Contract work.

**Sources:** Q42, Q77, Q108, Q118, Q150, Q152, Q157.

## 8. External execution and application tracking

### 8.1 Frozen material is not execution authorization

An immutable ExecutionSnapshot records the exact intended Job, channel/account, Resume, Greeting, and materials. It answers what will be sent, not whether sending is authorized. MaterialApproval confirms content; a separate explicit, scoped, expiring, single-use ExecutionApproval authorizes external execution. At most one execution Attempt can consume that approval.

Executor uses only the approved frozen inputs. Necessary live target-identity or availability checks remain within the authorization and shared platform safety boundary. They do not silently refresh JobVersion, parse requirements, replace the snapshot, or add model Job analysis. Clear closure, target mismatch, or execution-relevant change stops further actions and explains the need for explicit refresh/repreparation.

Partial continuation needs new narrower authorization. An unverifiable external outcome creates no success event and cannot automatically retry; external-state confirmation is needed. A click, submission gesture, or technical completion alone is not proof of a real application.

**Sources:** Q25, Q30–Q31, Q77, Q150, Q157, Q164.

### 8.2 Batch behavior and shared platform safety

A batch groups interaction and scheduling, not business success or atomicity. Each Job has its own Preparation, snapshot, approval, execution Attempt, and any resulting application record. Bulk confirmation may create separate exact approvals. One task's failure does not rewrite another's outcome. Members not dispatched cannot be shown as failed or applied.

Before every platform access, Collector and Browser Executor share persistent capacity and risk controls for the platform/account. A risk detected by one workflow can block subsequent affected access by the other. This does not share their business authorizations, budgets, or outcomes.

Ordinary page, selector, or browser failure is not automatically account risk. Predictable capacity can recover under policy. Strong risks such as security verification or account restriction require user handling and explicit restoration; they cannot be bypassed through cooldown alone, account/tab switching, or increased concurrency. Restoring safety is not new ExecutionApproval or automatic restart of a stopped operation. Explain the stop and retained completed work.

Platform limits and delays quoted in research are not official guarantees or frozen product defaults. A future Monitor must use the same safety boundary if implemented; this does not add monitoring to v1 scope.

**Sources:** Q36, Q49, Q160–Q161, Q164. Q160 replaces undifferentiated cooldown-based strong-risk recovery in earlier clauses.

### 8.3 Real application history

Technical ExecutionEvents describe actions and observations. ApplicationEvents represent real business facts established through reliable channel read-back or explicit human report. Contact, material sending, formal application, and replies remain distinguishable; no universal channel sequence is implied. Human reporting for a formal Job creates human-reported history without fabricating browser execution, approvals, or snapshots. It does not require prior automated execution. ManualApplicationEntry cannot be its target, and opening an entry URL establishes no application fact ([CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1)).

One ApplicationRecord represents one real application attempt for a Job/channel/account. Reapplication creates a new record. Events are append-only and deduplicated; delayed events retain occurrence and observation distinctions. Corrections and retractions append new events rather than erasing history.

Displayed progress is derived from events under a versioned policy, not another independently editable status. Interviews are initially recorded as structured application events—scheduling, completion, cancellation, feedback, and next-round confirmation—without a separate Interview Aggregate or implied interview-assistant capability.

**Sources:** Q7, Q16–Q17, Q21, Q30–Q31, Q37, Q44, Q48.

## 9. Privacy, controlled execution, and honest recovery

### 9.1 Model visibility and permission

Local availability does not grant model access. Tasks receive only admitted inputs under their scope, privacy, sensitivity, and authorization rules. Contact details, identity numbers, family information, and raw source documents are model-invisible by default, even when they may be displayed or rendered locally. Tool results receive the same admission checks.

Advisor uses typed, permitted business actions. It is not a general Shell, SQL, file, HTTP, or browser agent. A registered capability, generated ID, source document, JD, webpage, Tool result, or Memory entry cannot expand permissions or establish consent. Reads do not conceal platform fetches, parsing, or formal mutations. Formal fact changes and external execution retain their distinct confirmation boundaries.

Saved scope, admitted scope, and what a model actually saw are separate. References alone are not proof of content inspection. Revocation and future-use restrictions apply even when immutable historical records remain readable. Content already sent to a Provider cannot be retracted by local deletion or a switch change.

**Sources:** Q19, Q54, Q72, Q82–Q83, Q94, Q120–Q121, Q126, Q128, Q138–Q139, Q143–Q144, Q172; [Tool Actions](design/harness/tool.md).

### 9.2 Bounded work and recoverable outcomes

Every model task is bounded by its applicable budget, call/step limits, and deadline. Primary work, permitted repair, Context maintenance, and background learning cannot hide additional Provider calls. SDK retry or model fallback cannot silently bypass those controls. Numeric budgets and policies remain later design details.

An interrupted remote call without a complete durable response has uncertain outcome and possible cost. It must not silently replay, count as zero usage, or turn into business success. Explicit Retry starts new bounded work with fresh admission, preserving the prior uncertainty. Releasing a task slot or cancelling local work does not prove the remote call stopped or was refunded.

If a complete response is durably available, local processing can recover without a new model call. If a formal result already committed, recovery preserves it without duplicate assets. Safe regeneration of derived previews is distinct from replaying model calls, platform collection, or external actions.

Partial streamed text is temporary presentation, not a durable Suggestion, completed Turn, Memory source, or proof of Save. It may disappear after refresh and cannot be joined to a Retry's output. Frontend disconnection does not itself cancel a healthy backend; reconnection can retrieve its completed result.

**Sources:** Q116, Q122, Q124–Q125, Q135, Q140–Q142, Q147, Q152, Q156, Q165; [Recovery](design/harness/recovery.md), [Budget](design/harness/budget.md), [Storage](design/harness/storage.md).

### 9.3 Conversation context and retention

Conversation continuity does not mean every past message is sent on every model call. Context Engineering can select and compact eligible history while keeping complete durable Session history. A summary cannot replace protected exact analysis inputs, user authorization, or current task constraints. Context compaction neither creates Long-term Memory nor changes saved business facts.

Formal business history, Session content, collaboration Memory, protected recovery payload, and minimal audit/logging have different purposes and retention. Ordinary logs must not contain secrets or complete sensitive Resume/Evidence/prompt/response payloads. Cleaning payload or chat does not erase independent business history. If exact historical invocation content is unavailable, the product must not imply it can reconstruct it from current facts or a summary. A necessary unavailable source prevents reliable continuation or requires user input; it does not authorize automatic platform revisits or external replay. Exact retention periods and cleanup interfaces remain deferred.

**Sources:** Q47, Q52, Q83, Q125, Q127, Q131–Q132, Q136, Q139, Q141; [Context](design/harness/context.md), [Storage](design/harness/storage.md).

## 10. Collaboration Memory

### 10.1 Scope and authority

Long-term Memory supports cross-session collaboration preferences, feedback, working style, and reusable collaboration learning. It is not another career-fact, search-preference, or application store. Business facts stay with their formal owners; Session-local assertions remain conversational until explicitly saved through their proper workflow.

Current explicit instructions override remembered interaction style for that interaction. A one-off request does not automatically become a durable preference. Neither remembered style nor a request to avoid repetitive confirmation bypasses factual reconciliation, material confirmation, execution approval, or action permissions.

RequirementParse and both Fits receive no Long-term Memory, including through summaries or Tools. Advisor may use admitted collaboration preferences, feedback, and working style. Storing reusable learning does not implicitly authorize Advisor to read that category or introduce a General Assistant/interview Skill.

**Sources:** Q127–Q129, Q133, Q138–Q139; [Memory](design/harness/memory.md), sections 3, 4, and 9.

### 10.2 Three independent user controls

| Control | Effect and boundary |
| --- | --- |
| Auto Learning | Controls automatic extraction and publication from eligible new conversation sources; disabling it blocks new learning and late publication under stale permission |
| Recall | Controls whether stored Memory can be read or injected into each subsequent model input, including derived summaries; disabling it takes effect from the next input without deleting entries |
| View/Add/Edit/Delete/Clear All | Explicit management with deterministic validation, independent of both switches and without an extraction model call |

Learning off does not turn Recall off, and Recall off does not disable learning. Neither switch deletes Session continuity or disables ordinary authorized business reads. Reenabling learning does not automatically backfill earlier or disabled-period conversations. New chats do not scan all old Sessions or inherit old temporary Job scopes and Resume selections.

Direct Memory blocks are excluded from Context checkpoints so that Recall controls future admission. v1 does not promise to remove indirect influence already present in actual assistant history or retract earlier transmissions.

**Sources:** Q131–Q132, Q137, Q139, Q145; [Memory](design/harness/memory.md), sections 6, 8, 10, and 13. Q139 controls over earlier combined-switch wording.

### 10.3 Learning, failure, and forgetting

Automatic learning uses eligible completed durable user-facing Turns and independently scheduled background extraction. Sources are minimized to relevant user expression and necessary conversational context, not full Tool, Evidence, webpage, or transcript dumps by default. It does not run unconditionally after every Turn or depend on a reliable Session-ended event. Incomplete streams and extraction output do not recursively trigger learning. It proposes candidates; admission decides whether traceable explicit durable user expression or correction supports them. Assistant guesses, summaries, or repeated behavior alone cannot establish a durable preference. Clear eligible durable expressions need no extra confirmation popup for every Memory entry.

Background extraction has its own budget and yields to foreground capacity. Failure or insufficient budget does not undo a successful user task or charge an arbitrary last conversation Turn. Failed or uncertain source ranges require explicit Retry and do not block later eligible ranges or get silently absorbed into a new batch.

Forgetting stops future admission and removes the entry from valid derived summaries/indexes. Old sources and late extraction cannot automatically recreate it. Older automatic candidates cannot overwrite newer corresponding manual changes. A genuinely later durable user instruction may establish new Memory; manual management is not a permanent topic lock.

Session deletion and Memory forgetting are distinct. Deleting a source Session prevents new extraction or publication from its pending/in-flight ranges but does not delete previously accepted Memory. Already committed business facts remain. Cancellation where possible and truthful usage/audit remain necessary; deletion cannot retract remote transmission or establish zero cost.

**Sources:** Q127–Q131, Q139, Q141, Q145, Q155–Q156, Q169–Q170; [Memory](design/harness/memory.md), sections 6, 7, and 13–15.

## 11. Quality and evidence boundaries

Product quality claims must identify the capability and input scope actually evaluated. User-configured search scope does not establish demonstrated quality for every occupation, city, or source. Structural parsing checks, resolvable citations, and complete input inclusion do not by themselves prove semantic correctness or zero omissions.

[Acceptance](acceptance.md) defines required future evidence for the real task path and its boundaries. Permission bypass, unconfirmed mutation, wrong-target writes, hidden replay, or Candidate-to-Resume evidence leakage cannot be compensated by a good average quality score. Semantic quality, reliability, cost, and latency are separate concerns. Valid unscored analysis and correct business refusal must not be mislabeled as failure or zero quality merely because no numeric score was produced.

Evaluators and observations assess outcomes; they do not decide whether a fact committed, whether execution was authorized, or whether an application happened. Missing evaluation evidence is not a pass. Exact inputs do not guarantee identical remote-model output, and repeated trials do not justify hiding failed attempts behind a best result.

The Architecture and Acceptance drafts own Eval responsibilities and required evidence mapping; concrete Eval interfaces remain Contract work. This document defines no trial count, numerical acceptance threshold, automatic enablement or release policy. Formal annotated ParserVersion certification remains deferred; real-JD tests, manual inspection, and traceable quality work remain required. No implementation or Eval results are asserted by this specification.

**Sources:** Q82, Q117, Q168, Q173–Q180, Q184–Q186, S17.1, S35.1; [Agent Evaluation](design/eval/agent-evaluation.md), especially sections 18–20.

## 12. Non-goals and pending detail

### 12.1 Excluded or deferred product scope

The following are not v1 requirements established by this specification:

- Multiple Candidates, tenants, a unified Candidate Aggregate, or speculative ownership fields: Q53.
- Cross-platform canonical merging or historical Job merge operations: Q12 controls; Q13 is rejected.
- Bookmark/pursuit UX retained merely for compatibility: Q23, S37.1. The explicitly accepted ManualApplicationEntry in section 4.1 is separate current scope ([CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1)).
- Named SearchProfiles and parallel saved search configurations: Q55.
- Competing private Knowledge fact stores, arbitrary historical-version pickers, persistent atomic Assertions or independent bullet-level Evidence identities. BC3 supersedes the old ban on retained historical Resume bindings and alternate local expression; Q109's rejected Overlay-isolation mechanism is not reinstated.
- Knowledge completeness confirmation, persisted Resume coverage scoring, a joint Fit score, or a mandatory Fit-before-Advisor pipeline: Q24, Q56, Q112–Q113.
- Advisor working drafts, temporary draft export/application, ad hoc chat-file optimization, or implicit application targets inferred from past discussion: Q88, Q108, Q146, Q148–Q149.
- Personalized/generated Greeting, Greeting templates, or a general agent that autonomously performs every job-search capability: Q157, S17.4.
- General Assistant, mock-interview/review Skills, an independent Interview Aggregate, or a required platform Monitor inferred from future examples: Q21, Q127, Q139, Q160, S17.2.
- Candidate Evidence Agentic RAG or silent retrieval fallback for oversized v1 Fit: Q121, Q123, S24.1. Permitted Advisor reads and lightweight collaboration-Memory lookup do not un-defer that work.
- Career USER_FACT Memory, unrestricted historical-chat search, complex Memory graphs/consolidation, automatic historical backfill, or removal of indirect Memory influence from actual assistant messages: Q127–Q132, Q139; Memory design sections 8 and 15.
- Comprehensive physical personal-data erasure, an unsaved ResumeDraft crash-recovery guarantee, old-system import, mandatory legacy migration, or compatibility with old implementation behavior: Q4, Q100, Q131, Q166, S37.1.
- Mandatory offline annotated parser release certification or invented numerical rollout/release gates: Q117, Q175.

These exclusions do not remove accepted immutable history, current-use validation, privacy, explicit authorization, or the requirement to verify actual implementation later.

### 12.2 Details reserved for later work

| Pending matter | Owning follow-up and preserved boundary |
| --- | --- |
| Exact inputs and per-capability prerequisites beyond reviewed Profile/Evidence scope | Future consumer Contract Grill; preserve empty saved states, complete JobVersion admission, and fail-fast task prerequisites without a universal completeness Gate: Q3, Q15, Q44, Q48, Q54, Q154 |
| Identity/reference syntax, schemas, fields/types/enums, API payloads, errors, transitions, and migration/evolution details | Contract Grill after main-document review; preserve accepted authority, exact history, compatibility, and concurrency without treating the inventory as normative: Q2, Q22, Q26, S24.2 |
| Fit target keys, scoring weights/thresholds, score availability, and comparison representation | Contract/ScorePolicy design; preserve independent analyses, serialized targets, bounded negatives, and valid unscored outcomes: Q46, Q51, Q112, Q115–Q116, Q168 |
| Concrete Proposal/approval representation, lifetime details, channel readiness, render formats, and reliable read-back criteria | Related Contract and channel design; preserve exact preview/consent, actual viewed materials, separate execution authorization, and honest unknown outcomes: Q27, Q30–Q31, Q42, Q148–Q150, Q157, Q164 |
| Full Tool catalog, model admission/redaction details, capacity and budget values, Context/Memory policies, retention periods and cleanup coordination | Architecture boundaries followed by Contract/policy work; preserve least privilege, independent Memory controls, no hidden retries, and honest payload availability: Q19, Q123–Q125, Q132, Q135–Q145, Q169–Q172 |
| Source/adapter verification and actual upstream capabilities | Research before related detailed Contracts; pin commits and inspect licenses, maintenance, and source-to-canonical mapping. Examples are not verified platform guarantees: Q3, Q27, Q31, Q49 |
| Demonstrated quality scope, Trial counts, release thresholds, and default enablement | Acceptance defines evidence; later rollout-policy work resolves policy, without reinstating parser certification: Q117, Q173–Q187, S17.1 |

These are remaining expressions, policies, or explicitly deferred capabilities, not an invitation to reopen the settled Architecture Grill. [Architecture](architecture.md) explains supporting mechanisms and high-level Contract boundaries; [Contract Structure](contracts/structure.md) maintains the planned document organization; [Acceptance](acceptance.md) defines required future proof, and [Development](development.md) defines delivery discipline. [Implementation Plan](plans/implementation-plan.md) owns delivery planning, and [Progress](progress.md) records actual review, readiness and implementation state.

**Sources:** Q22, S24.2, S37.1, S38.1; English document-authoring spec, Further Notes B–E.
