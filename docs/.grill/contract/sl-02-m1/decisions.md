# SL-02.M1 Contract Grill Decision Register

> English is authoritative. This is the single decision/provenance record for this milestone, not normative Contract text or implementation evidence. Record accepted conclusions and scoped supersession, not question transcripts or unaccepted recommendations.

[Design navigation](../../README.md) · [Milestone plan](../../../plans/slices/sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) · [Contract Structure](../../../contracts/structure.md) · [Readiness ledger](../../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

## Purpose and session state

- Milestone: SL-02.M1 — Complete saved authority and atomic Save.
- User instruction: start this milestone's Contract Grill; continue five questions per round.
- Decision namespace: CG03-Qn. These are provenance locators, not published requirement IDs.
- Last answered batch: CG03-Q96–Q100 accepted, with Q98 revised to authoritative immutable Item.kind lookup and Q97 establishing Common-owned shared error vocabulary.
- Session: effective Q1–Q100 decisions and Q98 precedence clarification are published as 2026-09-21.S2M1-r1 after explicit user authorization; consumed interface review is complete. Future consumers retain separate Grill scope.
- Readiness: the eight consumed S2M1 portions are Ready; [review and ID mapping](../../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) owns evidence. Backend/frontend implementation remains Not started.
- Actual normative bodies now own the accepted definitions and IDs; this register preserves decision provenance. No implementation, frontend design, commit or placeholder bodies are created.

## Source baseline and controlling invariants

Read Product §3, Architecture §3/5/16.3, the owning Slice plan, Contract Structure/Index, Inventory §3–5, original Q15/Q54/Q63/Q66/Q96/Q98/Q163 and current upstream evidence. Follow repository AGENTS.md and Development's ownership/two-seam discipline. Inventory payload names remain examples until accepted; historical clauses retain later scoped corrections.

CG03-BC3 below controls current lineage, local expression, separate Save and DeepFit semantics, including the affected portions of BC1/BC2 and earlier decisions. CG03-BC1 controls the surviving Header-specific boundary. CG03-UI1 distinguishes local Draft preview from durable rendered materials. The following inherited architectural decisions remain effective subject to those scoped refinements:

- CandidateProfile owns identity/contact with immutable versions and root concurrency; career facts belong to shared Evidence; collection intent stays in Preferences. Contact is model-invisible by default. Concrete Profile fields are not frozen by historical examples.
- Evidence is a coherent experience/fact record, preserving paragraphs/lists; no persistent atomic Assertion decomposition. Each Item has one current saved version; historical versions do not replace current Knowledge facts; BC3 explicitly permits retained exact historical Resume lineage.
- EvidenceBaselineSnapshot freezes exact current membership without copying facts or asserting personal completeness.
- Resumes compose exact published Evidence and Profile versions with Resume-local expression/presentation. Existing historical or retired Evidence bindings remain legitimate lineage; later Knowledge/Profile publication does not change them. New ordinary member selection uses active current Evidence only; no arbitrary history picker in v1.
- Knowledge Save atomically publishes its owned version/current pointer/baseline and receipt; Profile Save publishes Profile only. Resume Save independently publishes the selected document, exact refs/current pointer and receipt. CG03-Q95 places actual material demand/durable intent in M2; once an actual consumer requires intent, it joins the owning command atomically. No implicit cross-Resume propagation or model/network/render inside a short authority transaction.
- Manual Resume Save checks exact lineage and structural validity, not semantic entailment of user wording. AI/Advisor rewrites retain explicit support constraints; their exact support representation remains pending. Lineage is not proof of truth.
- Empty saved career/Resume content is legal. First Resume becomes default; removing the last available root is prohibited. Evidence retirement changes the current baseline, retains referenced immutable history and leaves all Resumes unchanged. Independent privacy revocation/erasure is not ordinary retirement.
- New Evidence from the editor and Import uses explicit Knowledge Save first, then Resume Draft/Save. Cancel/close/failure of the second stage cannot undo committed facts. Drafts stay page-local; durable rendering remains SL-02.M2. DeepFit is one product workflow over two independent analyses, not a third analysis authority.

## Actual upstream state

The M1 local backend and M2 Preferences backend are implemented according to the current Progress and handoff evidence. Read-only code inspection agrees that the runtime targets schema 2 with explicit offline schema-1 migration; the M2 handoff §5 controls over its preserved preparation-time schema-1 description. Recorded 160-test backend evidence is inherited evidence, not a test run by this Grill.

SL-02.M1's logical upstream capability remains M1 local configuration/persistence. Extending today's physical schema must preserve the already implemented schema-2 Preferences and Entry consumers; this observation does not invent a functional dependency on Preferences configuration. Profile/Evidence/Resume bodies and implementation are not supplied by the Preferences module. Concurrent frontend/API/navigation changes in the working tree are outside this task.

## Required normative owners

| Owner under docs/contracts | Consumed portion for this milestone |
| --- | --- |
| foundation/workspace.md | Default Resume, first/last/removal and atomic configuration participation |
| candidate/profile.md | Concrete identity/contact fields, versions, exact snapshot display/privacy and explicit adoption |
| candidate/evidence.md | Typed whole records, current/history, baseline, exact references and eligibility |
| candidate/resumes-grounding.md | Resume/Draft/local expression/presentation, exact lineage, scoped AI support and removal |
| candidate/candidate-save.md | Separate Knowledge/Profile/Resume prepare/commit, revisions/idempotency, owned participants and durable results |
| applications/materials.md | Source/currentness and unavailable-output meaning required by Save; rendered delivery is SL-02.M2 |
| common.md | Actual consumed identity/date/text/reference/error conventions, preserving existing consumers |
| foundation/storage.md | Persisted representation, atomicity, privacy, retained readers and explicit evolution from current schema |

Under CG03-Q95 these are six named owner portions plus applicable Common/Storage, not a requirement to complete all eight document families. M1 consumes only manual lineage and source/currentness boundaries; actual material demand/intent is M2 and AI support is SL-07. Complete those future interfaces for their actual consumers, not as an M1 readiness gate.

## Round 1 — Content Scope, Top Presentation and Periods

<a id="cg03-q1"></a>

### CG03-Q1 — Five-field Profile and separate Resume targeting

- **Status:** PARTIALLY SUPERSEDED by CG03-Q7/BC1. The historical five-field inventory below is no longer current; Resume-specific targeting remains separate from acquisition Preferences.
- **Decision:** Profile v1 supports only name, nickname, email, phone and GitHub address. Current city, personal homepage/portfolio address, photo, birth date, gender, identity number and detailed address are outside v1. Career facts remain Evidence. Resume-specific job-seeking intention is presentation owned by that Resume/ResumeVersion, not Profile or search Preferences.
- **Boundary:** This does not remove the existing Preferences acquisition keywords/dimensions: future Collection intent and a Resume's displayed targeting statement are different concepts. Canonical Profile names, types, optionality and validation remain open. The earlier broader Profile field suggestion was not accepted; preserved Inventory examples are not an alternative supported schema.

<a id="cg03-q2"></a>

### CG03-Q2 — Six Evidence kinds and independent Top Presentation

- **Status:** PARTIALLY SUPERSEDED by CG03-Q6/Q8/BC1. Internship-only taxonomy, free Top Presentation and its blanket support obligation below are historical. Resume ownership of presentation/order and Evidence ownership of facts survive.
- **Decision:** Candidate Knowledge v1 has exactly six categories: education background, internship experience, project experience, professional skills, awards and certifications. General employment is not silently included in the accepted internship category. Canonical enum values and per-kind fields remain open. Evidence owns facts, not Resume section order/layout; order within an Evidence paragraph/list body remains meaningful content under Q3.
- **Presentation:** Each ResumeVersion may own different Top Presentation content and section order. Top Presentation sits between Profile contact information and regular Resume sections. A job-seeking intention is a v1 example, not an exhaustive whitelist: the area can carry other explicitly supported short display content. It is neither Candidate Knowledge nor Preferences authority. Pure presentation changes do not mutate shared Evidence.
- **Support boundary:** Existing factual-support and no-private-career-facts invariants still apply. The precise allowed support dependencies, item representation and propagation/deletion implications need subsequent Grill; no unreviewed special exemption or restriction is inferred from the area's position.
- **Formal owners:** Product §3, Architecture §3/5, Resume/Grounding planned scope and the owning milestone. This is an explicit scope/ownership refinement of previously generic examples; original architecture records remain preserved.

<a id="cg03-q3"></a>

### CG03-Q3 — Ordered plain-text content blocks

- **Status:** REFINED by CG03-Q25/Q26. Evidence retains semantic text/structure; Resume supports separate inline presentation. Exact serialized representation remains pending.
- **Decision:** Beyond each kind's structured fields, narrative content is an ordered block collection supporting paragraph, unordered list and ordered list. Paragraphs contain plain text; lists contain ordered plain-text items. Both block and item order are business content. v1 excludes nested lists, tables, images, arbitrary HTML and structure hidden in a Markdown string.
- **Boundary:** Blocks belong to an EvidenceItemVersion; they have no independent business identity and do not enable per-Resume bullet selection. Exact field/block/item grounding locations remain possible. Wire tags/field names, whitespace/newline/length rules and empty-content rules remain open.

<a id="cg03-q4"></a>

### CG03-Q4 — Month precision and unfilled period meaning

- **Status:** ACCEPTED WITH USER CORRECTION.
- **Decision:** Supplied experience start/end times must be precise to month, not day. Year-only precision is not supported. An unfilled start displays Unknown; an unfilled end displays Present/ongoing. Do not require a separate ongoing choice as the unaccepted earlier recommendation proposed.
- **Boundary:** This freezes user-facing semantic meaning, not whether wire omission/null/empty string is admitted. Exact canonical names, encoding, calendar/range checks and interval validation remain open. The preceding year-only and unknown-end-distinct-from-ongoing recommendation was not accepted, so there is no previously accepted rule to silently supersede.

<a id="cg03-q5"></a>

### CG03-Q5 — Mutable Resume management name

- **Status:** ACCEPTED.
- **Decision:** resume_name belongs to the mutable Resume root and is required/nonblank on creation. Duplicate names are allowed; resume_id owns identity. Rename requires concurrency admission but does not create ResumeVersion or change Evidence, grounding or material content. Management name is not automatically printed in the document; the displayed person's name comes from Profile. Export filename use belongs to the later Materials consumer.
- **Open detail:** Name bounds/canonical validation and the exact rename command/revision behavior will be defined with root/API semantics.

## Round 2 — Header Boundary, Canonical Types and Editor Structure

<a id="cg03-bc1"></a>

### CG03-BC1 — Manual Header presentation is not factual authority

- **Status:** ACCEPTED ARCHITECTURE BOUNDARY REVISION.
- **Decision:** ResumeHeaderPresentation replaces the earlier separate free Top Presentation Area. It is the top region before ordinary Evidence sections, combining default display of three exact Profile fields with per-Resume optional items from a system-defined catalog. Catalog membership is still open; the user's examples do not freeze all supported kinds.
- **Scoped exception:** User-authored optional Header text is presentation even when it contains career-like assertions. v1 performs no career-fact parsing or Evidence support check, creates no hidden Evidence dependency or expanded membership, does not consume it in Candidate Fit, and does not create/update Knowledge from it. It is stored in ResumeVersion.presentation, never Profile, Preferences or Evidence. Acquisition Preferences and Header intentions have no synchronization relationship.
- **Supersession:** Replaces CG03-Q1's five-field Profile with Q7's three fields and CG03-Q2's internship-only category with Q8's work experience. Replaces Q2's free supported Top Presentation and the original Product §3.2/3.5 / Architecture §5.1 blanket grounding obligation only for user-authored optional Header text. The previous Q6 recommendation to require support from selected Evidence was not accepted. No published normative requirement ID is changed or retired by this design revision.
- **Preserved boundary:** Profile still owns its exact identity/contact facts; Evidence sections still use whole current shared facts with their existing grounding/currentness rules. Header text cannot silently become confirmed Knowledge. AI/Advisor-generated Header admission/grounding is explicitly deferred to its real consumer. Resume Fit inclusion/exclusion and interpretation of manual Header are NOT decided by the explicit Candidate Fit exclusion; resolve that consumer boundary separately.

<a id="cg03-q6"></a>

### CG03-Q6 — ResumeHeaderPresentation mechanism

- **Status:** ACCEPTED AS USER REVISION.
- **Later scope:** BC3 replaces implicit shared Profile refresh with exact snapshots.
- **Decision:** Default Header displays name, phone and email from CandidateProfile without an independently editable copy. Each Resume may add/edit/remove/reorder predefined Optional Header Items through an Add Information action. Optional content belongs to immutable ResumeVersion.presentation; different ResumeVersions may differ. User-entered optional text follows BC1's presentation-only exception, including strings describing career experience or skills.
- **Open:** Supported item catalog, wire shape, cardinality/limits, default-field display controls, consumer visibility and version/no-op behavior. Future AI Header rules are not inferred from manual editing.

<a id="cg03-q7"></a>

### CG03-Q7 — Three canonical Profile fields

- **Status:** ACCEPTED; supersedes the field inventory portion of Q1.
- **Decision:** CandidateProfile v1 has only full_name, phone_number and email. Name is not split into first/last components; phone and email are single values, with phone represented as a string. nickname and github_url are removed from current v1 scope along with already excluded city/homepage/other fields. Root/version metadata is separate from this business field inventory. Header references these three Profile values.
- **Open:** Requiredness/nullability, precise validation and initial-object semantics.

<a id="cg03-q8"></a>

### CG03-Q8 — Six canonical Evidence kinds

- **Status:** ACCEPTED; supersedes the internship-only portion of Q2.
- **Decision:** EvidenceKind is exactly EDUCATION, WORK_EXPERIENCE, PROJECT, SKILL, AWARD, CERTIFICATION. WORK_EXPERIENCE covers internships, regular jobs, part-time work and other professional experience. A future distinction may be a work-experience field; experience_type is an example, not an adopted field. No INTERNSHIP top-level kind or OTHER catch-all exists. Kind selects a factual schema, never Resume section order.

<a id="cg03-q9"></a>

### CG03-Q9 — Explicit nullable month interval

- **Status:** ACCEPTED; completes Q4's representation.
- **Decision:** Period-bearing education/work/project records use required start_month and end_month fields. Each is a valid YYYY-MM string or null. Null start means unknown; null end means ongoing/Present. Both null means unknown start and ongoing end. v1 has no representation for ended-with-unknown-end-month and introduces no date_status field. Year-only/day dates, empty strings and display text such as Present are invalid. Do not synthesize a first day. If both ends are known, start_month <= end_month; same-month duration is valid.
- **Open:** Concrete calendar/year bounds and shared month-type clause, with per-kind validation.

<a id="cg03-q10"></a>

### CG03-Q10 — Exact narrative block shapes

- **Status:** PARTIALLY SUPERSEDED by CG03-Q25, then scoped by Q26. Evidence owns semantic text/structure and Resume owns marks; the historical exact string-based payload is not automatically re-frozen before representation Grill.
- **Decision:** content is an ordered collection of PARAGRAPH objects with exactly type/text, or UNORDERED_LIST and ORDERED_LIST objects with exactly type/items. Text and list items are plain strings. Preserve block/item order and duplicate text; never sort or deduplicate. No block/bullet business ID or separate Evidence identity exists. Fine-grained exact-version grounding locations do not create independently selectable Resume membership.
- **Semantic versus visual:** Store paragraph/list kind and ordering, not font, size, color, manual indentation or bullet icon. No arbitrary HTML/Markdown, tables, images or nested lists. Field-specific structured data remains owned by each EvidenceKind.
- **Open:** Empty content/list/item treatment, Unicode/whitespace/newline rules and bounds.

<a id="cg03-ui1"></a>

### CG03-UI1 — Structured editor and local A4 Draft preview

- **Status:** ACCEPTED PRODUCT/EDITOR STRUCTURE; no UI implementation performed.
- **Decision:** Resume Editor uses left structured editing and right live A4-paper preview, approximately equal panes. The top bar exposes back navigation, management name, save status and relevant export/actions subject to actual delivery. Header editing defaults to the Profile trio with an Add Information selector for predefined optional items. Section toolbar uses the six Q8 categories, including Work Experience rather than Internship. Prefer selecting existing Knowledge records; creating a new one uses shared Evidence authority, never a private Resume fact copy. Sections can contain multiple selected records; Resume owns section/member order. A paragraph/unordered-list/ordered-list editor matches Q10.
- **Draft boundary:** Local Header, selection, order, presentation and body edits update browser preview immediately from the same structured Draft. This needs no API request per keystroke and creates no formal versions, saved Profile/Evidence changes, durable material or export-ready state. Explicit successful Save still establishes authority; shared body/Profile edits use coordinated Save. A section/remove action changes Resume selection, not global Knowledge deletion.
- **Rendering:** Use a shared deterministic document-rendering representation/components for live preview and later PDF/print where feasible, avoiding independent competing templates. Pagination, page breaks, splitting, margins, typography and exact export fidelity remain Materials/M2 implementation/Contract work. The local draft preview is distinct from saved-version-bound durable artifacts and demanded-work publication; authority success and material readiness remain separate.
- **Exclusion:** No source-mode/Resume DSL, extra parser, source/visual round-trip or DSL recovery in v1. A future source view would be a derived representation, not another authority. This direction refines M1 editor scope while preserving M2's durable rendering/export obligation and the instruction to implement frontend only after UI design.

## Round 3 — Header Catalog, Fixed Profile Display and Section Groups

<a id="cg03-q11"></a>

### CG03-Q11 — Nine Optional Header kinds

- **Status:** ACCEPTED WITH ADDITIONS.
- **Decision:** v1 supports the six proposed kinds JOB_SEARCH_STATUS (job-seeking status), JOB_INTENTION (job-seeking intention), EXPECTED_POSITION, EXPECTED_CITY, EXPECTED_SALARY and HIGHEST_EDUCATION, plus gender, political affiliation and years of work experience. The last three canonical wire tags remain to be fixed. The catalog is system-defined; no custom kinds or custom labels in v1.
- **Values:** Values are user-written text, not derived enums/facts. Salary/city do not bind to Preferences and education/experience do not bind to Evidence. The three additions remain optional per-Resume presentation, not new Profile or Knowledge fields. CG03-BC1's no-parsing/grounding/dependency/membership/Knowledge-write/Candidate-Fit rules remain effective. Model/privacy admission for other future consumers is not inferred from display support.

<a id="cg03-q12"></a>

### CG03-Q12 — Minimal ordered Optional Header items

- **Status:** ACCEPTED. Q25/Q26 does not change Optional Header kind/value items or their plain-text rule; a prior round-five supersession label on this node was a recording error, now corrected.
- **Decision:** ResumeHeaderPresentation has an ordered optional_items array; each item has exactly kind (predefined type) and value (user text). Each kind appears at most once in a Resume. Array order is display order, with no sorting/deduplication. No independent item ID is required. An added item must have valid nonempty text to Save; remove the item when unwanted.
- **Authority:** Item kind/value/order changes are Resume presentation changes. No EvidenceRef, copied Profile values or extracted normalized fact value is stored in the item. Text limits/character/newline rules and overall presentation/version schema remain open.

<a id="cg03-q13"></a>

### CG03-Q13 — Explicit nullable Profile values

- **Status:** ACCEPTED.
- **Decision:** Profile's full_name, phone_number and email are all required keys with string-or-null values; all three values may be null. Null means not provided. Frontend clears send explicit null. Backend does not treat missing keys, empty strings or whitespace-only strings as implicit null. Profile completeness is not a gate for Knowledge maintenance or empty Resume creation.
- **Open:** String admission/canonicalization and initial root/version behavior remain separate decisions.

<a id="cg03-q14"></a>

### CG03-Q14 — Fixed Header trio, no hide controls

- **Status:** ACCEPTED USER REVISION; scoped architectural display refinement.
- **Later scope:** BC3/A1 supersedes automatic Profile propagation, while fixed fields/no-hide/null omission survive.
- **Decision:** Name, phone and email are fixed Header fields. Editor always exposes the three inputs; there is no presentation-level hide control. A populated value must be rendered; null produces no placeholder, label-only line, null/Unknown/Not Filled text. Rendering absence follows actual absent data, never a stored visibility override. Editing any of these values changes shared CandidateProfile through the existing Save boundary, not a private Resume override.
- **Supersession:** Replaces historical per-Resume Profile field-display choices for these three v1 fields in Product §3.3/Architecture §5.2 and their acceptance/interface descriptions. The immediately preceding hide-control recommendation was not accepted. This changes document display only, not model visibility/privacy admission or immutable historical Profile references.
- **Propagation:** A saved change from null to a populated value becomes visible in affected current Resumes; clearing to null omits its rendered content. Existing all-affected atomic Profile propagation still applies, without changing career Evidence baseline or historical assets.

<a id="cg03-q15"></a>

### CG03-Q15 — One section per kind, ordered whole members

- **Status:** ACCEPTED.
- **Later scope:** BC3 permits Resume-local expression and bullet organization; whole Evidence identity is lineage membership, not mandatory verbatim whole-body display.
- **Decision:** Each EvidenceKind has at most one section in a Resume; each section may select multiple records of that kind. Resume owns section order and order within the section. Adding an already-present kind selects more members into that group rather than creating another same-kind section. An EvidenceItem appears at most once in one Resume; similar content in distinct Items does not authorize merging.
- **Removal:** Removing a member or an entire section changes that Resume's membership only, never global Knowledge. Selected experiences remain whole; block/item locations are not selectable members.
- **Open:** Empty-section behavior and final section/reference wire representation remain pending.

## Round 4 — Text Admission and Education, Work and Project Fields

<a id="cg03-q16"></a>

### CG03-Q16 — Header tags and bounded display text

- **Status:** ACCEPTED.
- **Decision:** The three additions to Q11 use GENDER, POLITICAL_AFFILIATION and YEARS_OF_EXPERIENCE. Together with Q11's six existing tags they complete the nine-kind v1 catalog. Every optional value uses Common's fixed outer trim and contains 1–200 Unicode code points after trimming. Values are single-line plain text; remaining control/newline characters are rejected. Preserve case, internal spaces and wording; no implicit Unicode normalization or repair.
- **Boundary:** Do not parse gender, political affiliation, years, salary or education into facts, numeric values or another enum. Text such as New Graduate or 3 years remains presentation under BC1. This resolves Q11's pending tags and Q12's text-admission details without changing consumer/privacy permissions.

<a id="cg03-q17"></a>

### CG03-Q17 — Profile string validation without inferred identity

- **Status:** ACCEPTED.
- **Decision:** Each non-null Profile value uses Common's fixed outer trim; empty results are invalid, never converted to null. Preserve case, Unicode form and accepted formatting. full_name is nonempty single-line text of at most 100 Unicode code points; Chinese/other-language names and internal spaces are supported. phone_number is at most 50 code points, permits ASCII digits, spaces, a leading plus sign, hyphens and parentheses, and requires at least one ASCII digit. Do not infer a country code or reformat the number.
- **Email:** email is at most 254 code points, contains exactly one @ with nonempty sides, and contains no whitespace/control characters. This is bounded application validation, not complete email-standard validation or proof of deliverability. Do not lowercase or repair the value automatically.
- **Preserved:** All three required keys remain nullable under Q13; explicit null clears a value. Q14's populated-display/null-omission rule remains unchanged. Initial root/version behavior remains open.

<a id="cg03-q18"></a>

### CG03-Q18 — Education facts and a separate degree enum

- **Status:** ACCEPTED WITH USER CORRECTION.
- **Decision:** EDUCATION content fields are school_name, degree, major, start_month, end_month and content. degree is a single structured Candidate Education value: SECONDARY_VOCATIONAL, HIGH_SCHOOL, ASSOCIATE, BACHELOR, MASTER, MBA or DOCTORATE. These respectively represent secondary vocational school, high school, associate, bachelor, master, MBA and doctorate education. MBA is a distinct peer choice; no extra MBA field is introduced.
- **Ownership:** This enum records the user's education facts, not a Job's education-requirement ceiling. It neither reuses nor changes Preferences' merged education enum. Future comparison needs an explicit candidate-to-requirement level mapping owned by its actual consumer; enum names, declaration order and source codes cannot supply an implicit ordering or MBA mapping.
- **Scope:** No separate v1 GPA, rank or department fields; supplementary course/research/grade/rank facts can use content. The preceding free-text degree recommendation was not accepted. This is a correction to that proposal, not retirement of a published requirement or previously accepted degree representation.
- **Open:** Per-field requiredness/nullability, text bounds and date admission details remain pending; Q9 already owns interval meaning.

<a id="cg03-q19"></a>

### CG03-Q19 — Work-experience field inventory

- **Status:** ACCEPTED.
- **Decision:** WORK_EXPERIENCE content fields are company_name, role_title, start_month, end_month and content. v1 has no separate experience_type, department, work city or salary field. A title may mention internship or part-time work without automatic extraction into a subtype. This closes Q8's potential subtype field for v1 without narrowing the work-experience kind itself.
- **Open:** Per-field requiredness/nullability, bounds and date admission details remain pending.

<a id="cg03-q20"></a>

### CG03-Q20 — Project field inventory and one optional link

- **Status:** ACCEPTED.
- **Decision:** PROJECT content fields are project_name, role_title, project_url, start_month, end_month and content. project_url is one optional project homepage/demo/repository link, not a collection of links. v1 has no structured technology_stack; technology facts may appear in content and are not automatically converted into SKILL records.
- **Boundary:** A repository link is part of the project fact, not restoration of the removed Profile github_url field. Optional-link wire representation, URL validation/bounds and other field requiredness remain pending.

## Round 5 — Remaining Evidence Kinds, Requiredness and Rich Text

<a id="cg03-q21"></a>

### CG03-Q21 — Skill record and field inventory

- **Status:** ACCEPTED.
- **Decision:** SKILL content fields are skill_name and content. A record expresses one user-maintained skill or coherent skill group, such as Java or Backend Development. Narrative describes capability/experience. v1 adds no proficiency score, years-of-mastery field or inferred level and does not extract Skill records automatically from work/project text.
- **Membership:** A Resume selects the whole Skill record, not individual bullets. Requiredness and field bounds remain open.

<a id="cg03-q22"></a>

### CG03-Q22 — Award fields and an event month

- **Status:** ACCEPTED.
- **Decision:** AWARD content fields are award_name, awarding_organization, awarded_month and content. Level, ranking and background may use narrative; no separate v1 fields are added for them. awarded_month is YYYY-MM or null, with null meaning unknown award month, never ongoing/Present. The event meaning is distinct from Q9's interval-end meaning.
- **Open:** Name/organization requiredness, bounds and concrete calendar admission remain pending.

<a id="cg03-q23"></a>

### CG03-Q23 — Certification facts without validity management

- **Status:** ACCEPTED.
- **Decision:** CERTIFICATION content fields are certification_name, issuing_organization, issued_month and content. issued_month is YYYY-MM or null; null means unknown acquisition month. v1 adds no certificate number, verification URL, expiry field or automatically maintained validity status. Supplementary display facts may use narrative. No expiration assessment or reminder capability follows from saving the record.
- **Open:** Name/organization requiredness, bounds and concrete calendar admission remain pending.

<a id="cg03-q24"></a>

### CG03-Q24 — Education, work and project scalar requiredness

- **Status:** ACCEPTED.
- **Decision:** All defined fields of these three payloads are required keys; optional scalar values use explicit null, not omitted fields or empty strings. EDUCATION requires nonempty school_name and a valid degree; major is nullable. WORK_EXPERIENCE requires nonempty company_name and role_title. PROJECT requires nonempty project_name; role_title and project_url are nullable. Period fields retain Q9's required nullable month semantics; content follows Q25.
- **Boundary:** These constraints validate a record the user chooses to save. They do not require the user to own any education, work or project record or make empty Knowledge/Resume content illegal.

<a id="cg03-q25"></a>

### CG03-Q25 — Bounded rich-text content and document-wide typography

- **Status:** ACCEPTED USER REVISION, further scoped by CG03-Q26/BC2 and Q30. Rich editing support survives; semantic Evidence content and Resume-only inline presentation have separate owners.
- **Decision:** content is a required collection and may be empty. v1 supports paragraphs, unordered lists and ordered lists, with explicitly supported inline marks including bold, italic and links. Block order and list-item order are meaningful. Empty blocks, empty lists and empty items cannot be saved.
- **Content boundary:** No arbitrary HTML, Markdown string representation, fonts, font sizes, colors, images, tables or nested lists are stored in the body. Font family, font size, line spacing and theme color belong to Resume-level presentation and are controlled consistently for the entire Resume. Inline marks do not authorize arbitrary styling attributes or a generic editor document format.
- **Supersession:** Replaces Q3/Q10's plain-string-only text and previously exact string-based block payload. Supported block categories, order, no independent block/item business identities and whole-record selection remain effective. Exact rich-text AST and serialized mark names are deliberately deferred to representation Grill; old type/text and type/items examples cannot be used as a finalized schema. Q25's preceding single-line/trim/control handling recommendation is not accepted by this replacement answer; whitespace, line-break handling and rich-text emptiness validation need explicit follow-up.
- **Open interfaces:** Mark-only edit ownership/versioning, equality/canonicalization, safe link representation, exact grounding locations and text projection for consumers remain unresolved. Do not infer a private per-Resume Evidence body or a no-version formatting exception. Q16/Q17 Header/Profile plain-string validation is unaffected; this revision does not extend inline marks to those fields.

## Round 6 — Semantic Content versus Resume Presentation and Scalar Admission

<a id="cg03-bc2"></a>

### CG03-BC2 — Semantic Evidence and Resume-only inline presentation

- **Status:** ACCEPTED BOUNDARY CLARIFICATION under Q26/Q30.
- **Decision:** EvidenceItemVersion owns factual text, PARAGRAPH/UNORDERED_LIST/ORDERED_LIST structure, block order and list-item order. Changing these creates a shared Evidence version and follows existing atomic baseline/current-Resume propagation. Visual emphasis and inline hyperlinks authored within a Resume belong to that ResumeVersion's presentation. Pure presentation changes publish only a ResumeVersion; they do not create Evidence versions, advance EvidenceBaselineSnapshot or invalidate Candidate Fit through a format-only change.
- **Ownership:** project_url remains a structured project fact. Inline hyperlink placement, presence, display text and destination belong to Resume presentation and create no new Evidence dependency. Shared URL value rules do not create a shared business object or transfer ownership.
- **Supersession:** Resolves Q25's open mark-ownership/version branch and replaces any interpretation that stores inline marks in Evidence. The preceding Q26 recommendation to version Evidence/baseline for mark-only edits was rejected, not an accepted or published rule. Q25's rich editor capability and global typography boundary remain. This does not automatically republish Q10's old exact AST.
- **Preserved/open:** No Evidence marks overlay, format-only EvidenceVersion, private alternate career-fact body or independently selectable bullet is introduced. Exact Resume presentation representation, hyperlink display-text reconciliation with shared semantic text, and safe preservation/reset of formatting after changed Evidence remain open. Underline was conditional in the user's answer and is not yet an accepted v1 mark. Grounding/currentness for the new ResumeVersion must still be reconciled; absence of a new Evidence dependency is not a claim of unconditional GroundingSet or material reuse. No future Resume Fit or AI consumer policy is inferred.

<a id="cg03-q26"></a>

### CG03-Q26 — Separate semantic edits from visual edits

- **Status:** ACCEPTED USER REVISION; controls BC2.
- **Later scope:** BC3 extends Resume ownership to local wording/block organization and removes automatic shared-Resume propagation.
- **Decision:** Paragraph/list text, structure and ordering are shared Evidence semantic content. Bold/italic and other explicitly supported purely visual emphasis are Resume presentation; inline hyperlinks added to Resume text are also presentation. Format-only Save advances the edited ResumeVersion without changing shared Knowledge, baseline or Candidate Fit currentness. Font family/size, line spacing and theme color remain document-wide Resume presentation.
- **Boundary:** No Evidence marks overlay or format-only Evidence version. Supported marks, exact rendering representation and propagation across semantic text changes remain separate Grill decisions.

<a id="cg03-q27"></a>

### CG03-Q27 — Skill, award and certification requiredness

- **Status:** ACCEPTED.
- **Decision:** Every declared key is required. SKILL requires nonempty skill_name. AWARD requires nonempty award_name; awarding_organization and awarded_month may be null. CERTIFICATION requires nonempty certification_name; issuing_organization and issued_month may be null. Each requires content, with an empty collection permitted under Q25. Unknown organizations need not be invented to save a known award or certification.

<a id="cg03-q28"></a>

### CG03-Q28 — Common admission for short Evidence strings

- **Status:** ACCEPTED.
- **Decision:** school_name, major, company_name, role_title, project_name, skill_name, award_name, awarding_organization, certification_name and issuing_organization share fixed Common outer trim, then 1–200 Unicode code points of single-line text. Reject remaining controls/newlines. Preserve internal spacing, case and Unicode form; do not normalize names or truncate. A permitted absent scalar is explicit null; a non-null string trimmed to empty is invalid.
- **Scope:** This is short structured-field admission, not a trim rule for individual rich-text inline fragments. Body whitespace/canonicalization remains open.

<a id="cg03-q29"></a>

### CG03-Q29 — Exact month values without a moving future-date gate

- **Status:** ACCEPTED.
- **Decision:** Known month values use exactly ASCII YYYY-MM, year 0001–9999 and month 01–12. No surrounding whitespace, shortened year or automatic zero-padding. Known interval endpoints satisfy start_month <= end_month. v1 does not uniformly reject future values based on the current system month, or infer expected/completed states merely from future dates.
- **Null semantics:** Unknown start, ongoing end, unknown award month and unknown acquisition month retain their different field-owned meanings from Q9/Q22/Q23.

<a id="cg03-q30"></a>

### CG03-Q30 — Shared URL values, distinct fact and presentation owners

- **Status:** ACCEPTED WITH OWNERSHIP CLARIFICATION.
- **Decision:** project_url and inline hyperlink destinations reuse the existing URL value validation of MAE-004: fixed Common trim; at most 8192 code points; valid absolute HTTP(S) URL; no embedded credentials, invalid whitespace/control characters or silently repaired input. Non-HTTP(S) schemes including javascript/data/file/mailto and relative references are rejected. Preserve admitted spelling; saving does not fetch the URL or test reachability.
- **Ownership:** project_url belongs to EvidenceItemVersion. A Resume inline hyperlink's presence, location, display text and destination belong to Resume presentation and add no Evidence dependency. Reuse only URL value rules, not Manual Entry identity, command/revision, waiting-page or application semantics. The future representation is expressed in each actual owner; sharing validation does not combine both into one business object. Existing published MAE behavior is unchanged.

## Architecture Supersession — Independent Knowledge and Resume Documents

<a id="cg03-bc3"></a>

### CG03-BC3 — Exact lineage, Resume-local expression and unified DeepFit

- **Status:** ACCEPTED ARCHITECTURE SUPERSESSION; writeback authorized after A1–A5. This is not a local formatting-migration fix. No published SL-01 requirement ID is retired or repurposed.
- **Authority:** Candidate Knowledge/Evidence is the sole confirmed career-fact authority. Each Item retains immutable versions and one current version; Baseline snapshots current active Knowledge. ResumeVersion composes exact published Evidence versions, an exact Profile version, local expression and presentation. Resume is a document authority, not a Knowledge subclass or competing confirmed-fact store.
- **No synchronization:** Publishing or retiring Evidence changes Knowledge/current baseline only. Profile publication changes Profile only. Neither operation automatically changes any Resume, creates ResumeVersion, replaces source refs, clears wording/marks/links, invalidates unchanged Resume materials or cancels their work merely because a source current pointer changed. Existing older/retired Evidence refs remain valid lineage for Resume use, including Resume Fit/material/Preparation subject to their own actual permissions and readiness. Historical audit, Analysis and material references are preserved.
- **Editing:** Existing structured fact fields and factual source body are edited through Candidate Knowledge, not Resume-local overrides. Resume owns its own wording, paragraph/list/bullet organization, inline emphasis/hyperlinks, Header, section/member order and global presentation. User wording may differ from or lack support in current Knowledge; v1 manual Save performs no automatic factual verification and never promotes that wording to Knowledge. Resume-only changes advance only that ResumeVersion, not Evidence, baseline, other Resumes or Candidate Fit currentness.
- **Creation:** Selecting an existing active Evidence captures its exact current version into the Draft. Creating a new fact from Resume editing first opens a formal Evidence form and successfully saves it to Knowledge; only then can the Draft refer to V1. Fact Save failure cannot be bypassed with a private fact. Committed facts survive later Resume cancellation/failure. The two stages are separate commands, not one implied database transaction.
- **Adoption:** Adopting a newer source is an explicit mutation creating a new ResumeVersion. v1 performs no implicit refresh, fuzzy cross-version matching or automatic relocation/migration of presentation. The exact explicit-adoption command remains Contract work.
- **Analysis:** Candidate Fit consumes exact RequirementSet + exact admitted current EvidenceBaselineSnapshot. Resume Fit consumes exact RequirementSet + the specified ResumeVersion's admitted expression; source metadata cannot supply unexpressed facts. Opposite assessments are legitimate in either direction. A Resume MATCHED is support in the document, not confirmation of a Knowledge fact.
- **DeepFit:** DeepFit(Job, Resume) is the sole product Fit entry and an Application workflow. Both sides share one exact RequirementSet, retain independent tasks/results/history/failure/retry and show per-Requirement source provenance side by side. No DeepFitAnalysis, CoverageAnalysis, combined semantic task, score-gap authority or required score ordering is introduced. Existing safety, privacy, capacity, exact-frame, scoring and independent outcome rules survive.

| Superseded earlier mechanism | Current controlling replacement |
| --- | --- |
| Current Resume must use only current Evidence; historical facts prohibit new Resume use | Exact published lineage stays valid after newer versions/retirement; ordinary new selection is active-current-only under A3 |
| Shared wording/body, no local bullet expression (affected original Q63/Q96–Q98/Q108/Q163 and CG03 portions) | Shared source facts plus independent Resume-local wording/structure; no automatic Knowledge write-back |
| All-affected Profile/Evidence/Resume/grounding transaction (affected Q114/Q118–Q119) | Separate owned Knowledge/Profile and Resume commands; atomicity retained within each real command |
| Evidence deletion rewrites referencing Resumes (affected Q151/Q153) | Retire current Knowledge membership, advance baseline, retain referenced versions, leave Resumes unchanged |
| Blanket semantic-support/current-fact gate for manual formal Resume | Exact lineage/structural validation; separate AI support policy under A2 |
| Independent Candidate/Resume user entry selection (Q112/S22.1 product portions) | Unified DeepFit product workflow; independent internal analysis semantics survive |
| SL-04 single Evidence+Resume+Grounding transaction | Explicit two-stage Import under A5; product choice, not technical impossibility |

Original architecture/Harness records, Inventory and prior handoffs remain preserved; their affected clauses are interpreted through this supersession, not silently erased.

<a id="cg03-a1"></a>

### CG03-A1 — Profile snapshots

- **Status:** ACCEPTED. Resume binds exact ProfileVersion. Editing Profile never automatically advances existing Resumes; explicit adoption creates a new ResumeVersion. The three fixed non-hideable fields render values from the bound version, with null omitted. Privacy/model-admission rules remain independent.

<a id="cg03-a2"></a>

### CG03-A2 — Manual lineage versus AI support

- **Status:** ACCEPTED. Manual Save validates source existence, ownership and structure without automatic factual entailment. Traceable lineage is not a claim that the entire document is fact-verified. AI/Advisor-generated rewrites retain explicit support constraints and target one Resume. New/corrected facts use an explicit Knowledge flow. Grounding object retention/name/schema/Ensure reuse is deliberately reopened; no old universal semantic gate survives by retaining its name.

<a id="cg03-a3"></a>

### CG03-A3 — New selection and retained membership

- **Status:** ACCEPTED. The ordinary v1 picker offers active Items and captures the current version at selection. Existing saved members may retain older versions even after retirement. No arbitrary historical-version picker is introduced; explicit newer-version adoption is a Resume mutation. Precise selection-to-Save race checks remain Contract work without restoring continuous current-only membership.

<a id="cg03-a4"></a>

### CG03-A4 — One DeepFit entry, independent sides

- **Status:** ACCEPTED. Product entry requires a Job and Resume, uses one exact RequirementSet and separately frozen baseline/Resume inputs. A failed/oversized/unavailable side does not invalidate the other's success; show both statuses and retry within DeepFit. Internal Candidate capability does not require Resume; internal implementations can develop independently. Product integration acceptance requires both capabilities and orchestration, not two standalone buttons.

<a id="cg03-a5"></a>

### CG03-A5 — Two-stage Import as a product choice

- **Status:** ACCEPTED WITH RATIONALE CORRECTION. First confirm and save Candidate Knowledge; then decide how the Resume uses/expresses it and save the Resume separately. Stage-one committed facts survive stage-two cancel, browser closure and failed Resume Save. Atomic Evidence+Resume creation could technically preserve authority if refs bind simultaneously published versions; v1 chooses two stages for a consistent mental model, not because the database or authority model forbids a combined transaction. This explicitly supersedes SL-04's old one-transaction Evidence+Resume+Grounding flow.

<a id="cg03-q31"></a>

### CG03-Q31 — Link text follows Resume-local expression

- **Status:** ACCEPTED USER REVISION under BC3. Inline hyperlink range, target and display text belong to Resume mutation. They can use local wording rather than verbatim Evidence text, without Knowledge write-back. The preceding recommendation to route every linked-text change through Evidence was not accepted.

<a id="cg03-q32"></a>

### CG03-Q32 — Evidence semantic AST

- **Status:** ACCEPTED. Evidence content uses ordered PARAGRAPH objects with exactly type/text, or UNORDERED_LIST/ORDERED_LIST objects with exactly type/items; text/items are plain source strings. No marks, presentation links, fonts or independent block/item IDs. Preserve order/duplicates; content may be empty. Resume-local AST is separately owned and is not the same mutable content. Detailed whitespace/bounds remain pending.

<a id="cg03-q33"></a>

### CG03-Q33 — Knowledge changes leave Resume documents unchanged

- **Status:** ACCEPTED USER REPLACEMENT under BC3. Evidence updates never clear or migrate Resume wording, structure, marks, hyperlinks or presentation. Explicit source adoption creates a new ResumeVersion; no v1 fuzzy matching or automatic presentation relocation. The preceding clear-all-inline-formatting recommendation was not accepted and is not an implemented behavior to migrate.

<a id="cg03-q34"></a>

### CG03-Q34 — Resume editing layers

- **Status:** ACCEPTED. Local expression supports PARAGRAPH, UNORDERED_LIST and ORDERED_LIST; inline presentation supports BOLD, ITALIC, UNDERLINE and LINK, including combined emphasis on links. No nested lists, strikethrough, highlight, sub/superscript, inline code or per-span font/size/color. Global font/size/spacing/theme remains Resume-wide. Exact local AST and mark serialization remain Contract work.

<a id="cg03-q35"></a>

### CG03-Q35 — Draft-only empty sections

- **Status:** ACCEPTED. Draft may contain empty section placeholders; formal ResumeVersion cannot. Frontend omits empty sections before submission; backend rejects submitted empty-member sections instead of silently repairing them. All sections may be absent (empty collection), without deleting shared Evidence or Header content.

## Round 8 — Initial Expression, Membership Admission and Local Rich Text

<a id="cg03-q36"></a>

### CG03-Q36 — One-time local expression initialization

- **Status:** ACCEPTED. First inclusion uses the selected exact EvidenceItemVersion.content to initialize Resume-local content once, retaining paragraph/list/item order and initially adding no inline marks. Subsequent local editing belongs to that Resume and does not follow later source changes. Structured company/school/role/date fields remain supplied by the bound exact source, never copied into independently editable Resume-private factual authority.
- **Writeback:** Product §3.2–3.3; Architecture §5.1; Acceptance §4.1; planned resumes-grounding owner and SL-02.M1.

<a id="cg03-q37"></a>

### CG03-Q37 — Newly published membership freshness

- **Status:** ACCEPTED. A newly added member must bind the still-current version of an active EvidenceItem when Resume Save commits. A source update or retirement after selection rejects the entire Save; do not silently substitute current, omit the member or discard Draft edits. A member already present in the preceding formal ResumeVersion may retain its unchanged exact historical binding after source update/retirement. This is admission of new membership, not continuous current-only eligibility of saved documents.
- **Open boundary:** Explicit changed-source adoption races and precise revision/base classification belong to the remaining command Contract. This decision does not authorize arbitrary historical additions.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.2.

<a id="cg03-q38"></a>

### CG03-Q38 — Source adoption and expression reset are separate

- **Status:** ACCEPTED WITH USER CLARIFICATION. Explicitly adopting A3 updates the exact source reference and source-provided structured facts in the Draft while retaining local wording, marks and links. Ask whether the user also wants to replace the local expression from A3; only a separate explicit choice replaces it. Retention is not a claim that A3 supports the retained wording. No automatic grounding, merge or fuzzy alignment. Successful Resume Save publishes the chosen changes as a new ResumeVersion; Knowledge remains unchanged.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.2.

<a id="cg03-q39"></a>

### CG03-Q39 — Empty member body is legal

- **Status:** ACCEPTED. ResumeEvidenceMember.content is present and may be an empty array. The member still exists with exact lineage and its source-provided structured facts; empty content causes neither Evidence-body fallback nor source/member deletion. Nonempty AST cannot contain empty blocks, lists or items. This is distinct from Q35's rejected empty-member sections.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1.

<a id="cg03-q40"></a>

### CG03-Q40 — Ordered text runs with inline marks

- **Status:** ACCEPTED WITH USER CLARIFICATIONS. Resume-local PARAGRAPH owns ordered runs; UNORDERED_LIST/ORDERED_LIST owns ordered items, each owning ordered runs. Runs use text and marks; emphasis marks use type, and LINK uses type plus url, following the accepted example. The four mark kinds are BOLD, ITALIC, UNDERLINE and LINK; they can coexist on one run with at most one LINK. Lists remain block types, never inline marks. Blocks/items/runs have no business IDs. Evidence retains its separate plain semantic AST.
- **Canonicalization principle:** Adjacent runs with equivalent marks must coalesce so formatting segmentation alone is not a meaningful representation difference. Exact mark comparison/order, merge procedure, whitespace, empty runs and limits remain the next Grill frontier; no unaccepted algorithm or capacities are frozen here.
- **Writeback:** Product §3.3; Architecture §5.2; Contract Structure and SL-02.M1 scope. Exact representation/admission proof follows the remaining decisions.

## Round 9 — Body Canonicalization, Capacity and Adoption Freshness

<a id="cg03-q41"></a>

### CG03-Q41 — Canonical marks and adjacent runs

- **Status:** ACCEPTED. marks is required, using an empty array for unformatted text. Sort marks in BOLD, ITALIC, UNDERLINE, LINK order; duplicate kinds, including duplicate LINK, are invalid rather than silently deduplicated. LINK.url follows shared URL validation without additional equivalence rewriting of host case/trailing slash. Within one paragraph or list item, adjacent runs with identical canonical marks coalesce by concatenating text. Do not merge across paragraphs/items/blocks or across intervening differently formatted runs. Mark ordering and equivalent adjacent run segmentation do not create a meaningful content difference.
- **Open boundary:** Raw admission/validation order remains to be specified; merging is not an implicit license to repair invalid runs.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1; planned resumes-grounding scope.

<a id="cg03-q42"></a>

### CG03-Q42 — Evidence source-body whitespace

- **Status:** ACCEPTED. For each Evidence paragraph.text/list item, reject Common control characters and line/paragraph separators (including Tab/CR/LF) before applying Common's fixed outer trim. Trimmed text must be nonempty. Preserve internal ordinary spaces and repeated spaces; do not normalize Unicode. Separate blocks/items encode paragraph/list boundaries; visual wrapping belongs to rendering. No v1 manual soft break within a paragraph/item. The editor can construct semantic blocks from editing actions; the backend does not guess/split illegal strings.
- **Writeback:** Product §3.1; Acceptance §4.1; planned evidence scope. Short-field rules do not silently define body admission.

<a id="cg03-q43"></a>

### CG03-Q43 — Local whitespace preservation without invisible formatting

- **Status:** ACCEPTED WITH USER REFINEMENT. Reject empty-string runs and empty runs arrays. Do not trim individual runs: retain legitimate leading/trailing/internal spaces and word separation around marks. A run consisting only of ordinary U+0020 spaces is permitted only with marks = []; runs containing actual non-whitespace text may carry marks. Thus BOLD/LINK applied only to ordinary spaces is invalid. Join paragraph/item run text and apply Common trim only as a nonempty check, never as replacement text. Reject controls and line/paragraph separators, including CR/LF/Tab. Member content = [] remains legal; empty/non-content blocks do not.
- **Open boundary:** Treatment of runs consisting solely of other permitted Unicode whitespace and detailed pre-merge admission order remain to be made explicit; ordinary-space handling is not silently generalized into a new whitespace algorithm.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1. This narrows Q43's original unqualified whitespace-only-run recommendation.

<a id="cg03-q44"></a>

### CG03-Q44 — Per-body capacity limits

- **Status:** ACCEPTED. Apply separately to each Evidence content and each Resume member's local content: at most 100 blocks, 100 items per list block, 10,000 Unicode code points per paragraph/item, and 50,000 text code points summed across that content. Resume paragraphs/items permit at most 256 canonical runs each. Text counts concatenate runs, exclude marks metadata, and do not replace LINK.url's existing 8192-code-point limit. Any excess rejects the complete Save without truncating/splitting. These capacities do not promise model-context admission or a PDF page count.
- **Open boundary:** Whole-Resume membership/content capacity, raw pre-canonicalization node budgets and HTTP byte limits remain separate forthcoming decisions. Canonical run count alone is not a raw request cost bound.
- **Writeback:** Product §3.1/3.3; Acceptance §4.1; evidence/resumes-grounding planned scopes and SL-02.M1.

<a id="cg03-q45"></a>

### CG03-Q45 — Freshness when replacing an existing source binding

- **Status:** ACCEPTED. Explicitly replacing a member's Evidence reference must target the still-current version of an active Item at commit. If A3 is chosen but A4 is published or the Item is retired before Save, reject the complete Save and retain Draft edits; do not silently choose A4 or restore A2. The user can explicitly select an admissible current source or cancel the reference change and retain the already-published A2 binding. Editing local wording while keeping A2 unchanged does not require A2 to remain current. This resolves Q37's changed-source race branch without restoring continuous current-only eligibility.
- **Open boundary:** Exact expected-revision/base representation, conflict payload and replay order remain command Contract work; Profile initialization/adoption has its own boundary.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.2; candidate-save interface planning.

## Round 10 — Raw Admission, Immutable Evidence Kind and Initial Profile

<a id="cg03-q46"></a>

### CG03-Q46 — Fixed allowed-whitespace rule for local runs

- **Status:** ACCEPTED. Extend Q43's ordinary-space rule to Common's fixed whitespace set after excluding prohibited controls and line/paragraph separators. A run consisting entirely of these permitted whitespace characters is legal only with marks = []; a run containing non-whitespace text can have marks. Preserve NBSP, ideographic space and other permitted characters exactly, without converting them to U+0020 or inheriting a moving Unicode classification. The joined paragraph/item must still pass the nonempty check. This explicitly resolves Q43's broader-whitespace branch.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1; planned resumes-grounding scope.

<a id="cg03-q47"></a>

### CG03-Q47 — Validate raw runs before canonical merging

- **Status:** ACCEPTED. Validate each submitted run before canonical merge. Empty runs, invalid characters, duplicate marks and marked whitespace-only runs reject the input even if concatenation with a neighbor would conceal the violation. Only admitted runs proceed to mark ordering and adjacent-equivalent merge; then enforce the 256 canonical-run limit. Do not repair by deleting runs, clearing marks or merging invalid input. Segmentation equivalence applies to independently admitted representations. The editor emits valid structure; the server independently validates it.
- **Open boundary:** Raw node and whole-request budgets remain separate pending limits; this ordering does not permit unbounded pre-merge requests.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1; resumes-grounding/candidate-save admission seam.

<a id="cg03-q48"></a>

### CG03-Q48 — Evidence kind is permanent per Item

- **Status:** ACCEPTED. EvidenceKind is fixed for the lifetime of an EvidenceItem. Editing changes only that kind's fields/content; changing PROJECT into WORK_EXPERIENCE is not an update. Correct a wrong kind by explicitly creating a new Item and, when desired, retiring the old one. Do not convert fields, migrate Resume membership or replace historical references automatically. No OTHER kind or generic conversion API is added.
- **Ownership refinement:** Q50 fixes EvidenceItem as the sole kind authority; immutable version content is interpreted through its owning Item.
- **Writeback:** Product §3.1; Architecture §3.1/5.1; Acceptance §4.1–4.2; planned evidence scope.

<a id="cg03-q49"></a>

### CG03-Q49 — Initial empty Profile snapshot

- **Status:** ACCEPTED. Fresh initialization of storage supporting SL-02 creates the sole Profile root and its first immutable ProfileVersion, with full_name, phone_number and email all null. It means no contact values have been provided, not an identity confirmation. A first Resume can bind this real version without fictitious IDs or mandatory contact entry. Later changes use separate Profile Save. Do not create a Resume automatically. Existing older storage gains this capability only through explicit migration; ordinary startup must not silently recreate missing required records.
- **Boundary:** Preferences retains its independently defined lazy creation. Q49 defines no Candidate aggregate, baseline initialization, final schema number or new normative requirement ID. The detailed atomic initialization/migration representation remains Storage work.
- **Writeback:** Product §3.1/3.3; Architecture §5.1; Acceptance §4.1; Profile/Workspace/Storage planning and SL-02.M1.

<a id="cg03-q50"></a>

### CG03-Q50 — Item-owned discriminator and version business content

- **Status:** ACCEPTED USER REVISION. EvidenceItem alone owns permanent kind. EvidenceItemVersion business content consists of type-specific fields and shared semantic content; the owning Item.kind uniquely selects the legal fields schema. API responses may project kind from the owner for discriminated/self-contained representations, but it is not an independently mutable/version-owned authority. No second authoritative kind is introduced into Version content.
- **Shape:** fields contains only that kind's approved structured facts; content uses the same Evidence semantic AST for all six kinds. Reject unrelated/unknown/cross-kind fields rather than combining all kinds into a broadly nullable schema. Version identity/ownership/timestamps and exact API write/read envelope rules remain forthcoming. Resume-local content stays outside this fact payload.
- **Writeback:** Product §3.1; Architecture §3.1/5.1; Acceptance §4.1; planned evidence and candidate-save scopes.

## Round 11 — Saved Roots, Versions, Members and Baseline Ownership

<a id="cg03-q51"></a>

### CG03-Q51 — Profile root and immutable snapshot fields

- **Status:** ACCEPTED. CandidateProfile fields: profile_id, current_profile_version_id, revision, created_at, updated_at. ProfileVersion fields: profile_version_id, profile_id, schema_version, full_name, phone_number, email, created_at. Root owns identity/current/concurrency; business contact values exist only in Version. Initialization sets root revision = 1 and points to the initial all-null Version. Version has neither updated_at nor is_current. schema_version starts at 1 and selects content structure, not user edit count. v1 cannot delete the Profile root; clearing contact means saving all-null content.
- **Open boundary:** ID representation/generation, publication/no-op timestamps, complete read/Save envelopes and concurrency results remain subsequent decisions. These are saved-object fields, not accepted write payloads.
- **Writeback:** Product §3.1/3.3; Architecture §3.1/5.1; Acceptance §4.1; profile/candidate-save scope.

<a id="cg03-q52"></a>

### CG03-Q52 — Evidence roots and immutable version fields

- **Status:** ACCEPTED. EvidenceItem fields: evidence_item_id, kind, status, current_evidence_item_version_id, revision, created_at, updated_at. status is ACTIVE or RETIRED. EvidenceItemVersion fields: evidence_item_version_id, evidence_item_id, schema_version, fields, content, created_at. Root creation publishes its first Version atomically, with no empty root. Retirement retains the current pointer as the last published version; RETIRED excludes it from current Baselines. Version schema_version starts at 1 and, with the owning Item.kind, selects its reader. Version has no independent authoritative kind/status/revision/is_current; any API kind is owner-derived under Q50.
- **Open boundary:** Retirement command/repeat results, restore capability, ID format and publication time/revision rules remain pending; the two status values do not by themselves authorize a restore operation.
- **Writeback:** Product §3.1/3.4; Architecture §3.1/5.2–5.3; Acceptance §4.1–4.2; evidence/storage/candidate-save scope.

<a id="cg03-q53"></a>

### CG03-Q53 — Resume root and management name

- **Status:** ACCEPTED. Resume fields: resume_id, resume_name, status, current_resume_version_id, revision, created_at, updated_at. status is ACTIVE or REMOVED; removal is logical and preserves immutable versions/required history. Root creation atomically publishes the first ResumeVersion. resume_name is root management metadata, not document body or version content. Common outer trim yields 1–120 code points; reject controls/line/paragraph separators, allow duplicates and add no automatic suffix. Rename requires revision admission but creates no ResumeVersion. Existing default/last-root rules remain effective.
- **Open boundary:** Exact name-validation ordering, mutation/no-op/time/revision results, removal/recovery commands and full ResumeVersion structure remain pending.
- **Writeback:** Product §3.3–3.4; Architecture §5.2–5.3; Acceptance §4.1–4.2; Resume/Workspace/candidate-save scope.

<a id="cg03-q54"></a>

### CG03-Q54 — Ordered sections and exact member references

- **Status:** ACCEPTED. ResumeSection fields are kind and members. ResumeEvidenceMember fields are evidence_item_id, evidence_item_version_id and content (Resume-local AST). Preserve section/member array order. At most one section per kind and one membership per EvidenceItem across the document. Referenced Version belongs to the referenced Item; section.kind agrees with every member Item.kind. Section kind is grouping/validation, not a second fact-kind authority. No section_id/member_id/position/sort_order; classification, Item identity and array order are sufficient. Local content is not authoritative Evidence source content.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1–4.2; resumes-grounding scope.

<a id="cg03-q55"></a>

### CG03-Q55 — Initial exact Baseline and domain-owned current pointer

- **Status:** ACCEPTED WITH OWNERSHIP CORRECTION. Initialize a real empty EvidenceBaselineSnapshot and persist exactly one current_evidence_baseline_snapshot_id pointer in SL-02-capable storage. Evidence/Baseline domain owns that pointer's normative meaning and changes. Physical placement in a Workspace singleton/config row is an implementation choice and grants Workspace no Candidate Knowledge authority; this supersedes the proposal that Workspace configuration normatively owns the pointer.
- **Shape:** Snapshot fields: evidence_baseline_snapshot_id, schema_version, members, created_at. schema_version starts at 1; initial members = []. Each member contains evidence_item_id and evidence_item_version_id. A Snapshot includes all then-ACTIVE Items, once each, bound to their exact current versions. Membership is an unordered business set, serialized deterministically by evidence_item_id; this order has no presentation or temporal meaning. Do not copy kind/fields/content or assert personal completeness.
- **Evolution:** Real Knowledge changes publish a new Snapshot/current pointer. Profile edits, Resume edits and reads do not advance it. Retiring the last active Item publishes another empty Snapshot rather than clearing the pointer. Older storage uses explicit migration; ordinary startup does not repair a missing Snapshot/pointer. No Candidate aggregate is introduced.
- **Open boundary:** ID generation, times, exact pointer concurrency/storage representation and complete command protocol remain pending. Q55 separately authorizes baseline initialization; it was not implied by Q49's Profile initialization.
- **Writeback:** Product §3.1/3.4; Architecture §3.1/5.1–5.3; Acceptance §4.1–4.2; evidence/candidate-save/storage scopes. Contract Structure removes mandatory Workspace placement.

## Round 12 — IDs, Publication, Resume Envelope and Profile Freshness

<a id="cg03-q56"></a>

### CG03-Q56 — Server-generated opaque UUIDv4 identities

- **Status:** ACCEPTED. profile_id, profile_version_id, evidence_item_id, evidence_item_version_id, evidence_baseline_snapshot_id, resume_id and resume_version_id use server-generated Common UuidV4 (lowercase, hyphenated). Clients reference existing identities but cannot choose new formal business IDs. IDs encode no time/order/type/name/content and are not content hashes. Retire/remove does not permit reuse. Publishing the same content at a different time can produce a new version identity. request_id is a distinct command-idempotency identity, whose protocol remains pending.
- **Writeback:** Architecture §3.2; Acceptance §4.1; applicable Profile/Evidence/Resume/Common/Storage consumption. Existing Common scalar meaning is reused, not changed for SL-01.

<a id="cg03-q57"></a>

### CG03-Q57 — Revision before canonical equality and publication

- **Status:** ACCEPTED. For ordinary new commands, check the root revision before canonical equality and only then decide a valid no-op, content publication or lifecycle change. Matching content does not bypass stale revision. All new roots start at revision 1; real root changes advance by one. Reuse Common's revision range: at maximum revision, valid no-op may succeed but real mutation is rejected without overflow. Compare each owner's canonical content, never JSON bytes or UI dirty state. A→B→A publishes a fresh Version rather than reactivating historical identity. Receipt replay ordering and repeated lifecycle requests are separate remaining command decisions.

| Actual change | Publication effect |
| --- | --- |
| Profile content | New ProfileVersion, root revision +1 |
| Evidence content | New EvidenceItemVersion, root revision +1, new Baseline/current pointer |
| Resume document | New ResumeVersion, root revision +1 |
| Resume name | Root revision +1, no ResumeVersion |
| First Evidence retirement | Root revision +1, new Baseline, no new fact Version |
| First Resume removal | Root revision +1, retain immutable history |
| Valid canonical no-op with matching revision | No new Version, root revision or Baseline |

- **Writeback:** Product §3.2–3.4; Architecture §5.2; Acceptance §4.1–4.2; candidate-save and its owned root interfaces.

<a id="cg03-q58"></a>

### CG03-Q58 — One scoped publication time

- **Status:** ACCEPTED WITH SCOPE CLARIFICATION. A real commit uses one publication_time: max(system now, old updated_at of roots actually modified, previous current Baseline.created_at only when that commit truly advances Baseline). Ignore absent old-root values for creation. Profile-only and Resume-only commands do not consult Baseline time. Assign that time to modified-root updated_at, all newly published Versions/Snapshots created_at and new-root created_at/updated_at; existing-root created_at stays fixed. Immutable objects have no updated_at. No-op, reads and successful replay refresh no business times. Common UTC millisecond representation applies.
- **Limits:** No global logical clock or publication sequence. Equal timestamps are legal; timestamps and UUIDv4 provide no strict total historical order. Non-regression is scoped to the objects being advanced, not unrelated records.
- **Writeback:** Architecture §5.2; Acceptance §4.1; candidate-save/storage publication representation.

<a id="cg03-q59"></a>

### CG03-Q59 — ResumeVersion envelope without copied Profile or Baseline

- **Status:** ACCEPTED WITH HEADER CLARIFICATION. ResumeVersion fields are resume_version_id, resume_id, schema_version, profile_version_id, header_presentation, sections, document_presentation and created_at. schema_version starts at 1. profile_version_id supplies the exact fixed Header trio; header_presentation stores optional_items and only explicitly supported pure presentation settings, never full_name/phone_number/email values. No copied Profile values exist elsewhere in the Version either. Existing Q12 optional-item shape/order remains controlling; this does not authorize arbitrary extra Header fields.
- **Composition:** sections uses Q54 exact Item/Version refs and local content. document_presentation owns whole-document typography/theme; its internal fields remain pending. No root resume_name/status/revision/current pointer, whole evidence_baseline_snapshot_id or mandatory general grounding_set_id belongs in this manual Version. Resume selects exact lineage, not a sub-snapshot of an entire Baseline; AI support waits for its real consumer.
- **Writeback:** Product §3.3; Architecture §5.1–5.2; Acceptance §4.1; resumes-grounding/profile/evidence interface scopes.

<a id="cg03-q60"></a>

### CG03-Q60 — Profile freshness only for a new or switched reference

- **Status:** ACCEPTED WITH EXPLICIT HISTORICAL-REFERENCE EXCEPTION. First Resume publication or an explicit switch of profile_version_id requires that selected ProfileVersion still be current at commit. A reference already present in the preceding formal ResumeVersion and left unchanged receives no renewed current-only check. Thus a document can retain historical P2 while editing wording/presentation after Profile publishes P3. New/switch adoption racing Profile publication rejects the complete Resume Save and retains Draft; no silent latest substitution. The user may explicitly reselect current or cancel a switch to retain the preceding published reference.
- **Open boundary:** Exact revision/base read/write envelopes, error priority and replay protocol remain pending; this adds no arbitrary historical Profile picker or automatic propagation.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.2; profile/resumes-grounding/candidate-save admission seam.

## Round 13 — Document Settings, Aggregate Capacity and M1 Commands

<a id="cg03-q61"></a>

### CG03-Q61 — Explicit document-wide typography and theme

- **Status:** ACCEPTED USER REPLACEMENT. ResumeVersion.document_presentation contains exactly the four v1 settings below, explicitly saved rather than defaulted on read. Draft defaults initialize editable state, not missing formal fields.

| Field | Accepted rule | New Draft default |
| --- | --- | --- |
| font_family | SOURCE_HAN_SANS, HEITI, SONGTI, KAITI | SOURCE_HAN_SANS |
| font_size_pt | Global body size 12–20 pt in 0.5-pt steps | 12 |
| line_spacing_pt | Full body line-box height 14–30 pt; at least font_size_pt + 2 | 18 |
| theme_color | Six-digit #RRGGBB; uppercase canonical hex letters | #1F2937 |

- **Rendering boundary:** Fonts are logical enums, not OS font names/files. Renderer owns actual Web/PDF font and fallback mapping. UI label is line spacing; line_spacing_pt is the full line-box height, not extra whitespace added to font size. A4 is fixed; margins, relative heading sizes and section spacing remain unified-template settings. No per-span typography/color; the four accepted inline marks survive. Real document_presentation changes publish a ResumeVersion only, without Profile/Evidence/Baseline mutation.
- **Open boundary:** The line_spacing_pt step/precision, exact numeric/color boundary admission and Renderer asset/configuration mapping remain pending. The proposed percentage line-height field and generic two-family/9–14-pt alternatives were not accepted.
- **Writeback:** Product §3.3; Architecture §5.2/5.4; Acceptance §4.1/4.3; resumes-grounding/material interface and SL-02.M1.

<a id="cg03-q62"></a>

### CG03-Q62 — Whole-Resume defensive limits

- **Status:** ACCEPTED WITH COUNTING CLARIFICATION. At most 100 Evidence members per Resume; at most 200,000 Unicode code points summed from all Resume-local member.content run.text values. Each member still obeys Q44. Profile, Optional Header, Evidence structured fields and URL targets do not enter this sum; their own limits apply. Existing six-section/nine-Header-kind constraints are unchanged. Reject the whole Save without truncation, member removal or font shrinking. These are storage-validity limits, not page-count or model-admission guarantees.
- **Open boundary:** HTTP body bytes and raw pre-canonicalization AST node budgets remain required separate limits.
- **Writeback:** Product §3.3; Acceptance §4.1; resumes-grounding and eventual HTTP admission scope.

<a id="cg03-q63"></a>

### CG03-Q63 — Per-Item Knowledge commands in M1

- **Status:** ACCEPTED. M1 exposes single EvidenceItem create/update/retire, each atomically committing the Item change, necessary Version, new Baseline/current pointer and required durable intent. The Snapshot still contains all ACTIVE Items' exact current versions, not just the changed Item. No generic multi-Item Save/delete or whole-library replacement interface is delivered in M1.
- **Later consumer:** SL-04 multi-fact Import requiring a wholly atomic confirmation stage needs an explicit batch Contract extension. Multiple independently committed single-Item commands cannot be represented as one rollback-capable stage. This does not revoke BC3/A5's two stages or durability between them.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; SL-02.M1 and SL-04.M1 plans; candidate-save/Import ownership seam.

<a id="cg03-q64"></a>

### CG03-Q64 — One-way lifecycle with readable history

- **Status:** ACCEPTED WITH READABILITY CLARIFICATION. v1 supports only ACTIVE→RETIRED for EvidenceItem and ACTIVE→REMOVED for Resume. No restore; recreating current availability uses a new identity. Retired Evidence rejects content updates; removed Resume rejects document updates/rename; ordinary Save cannot reactivate either. Objects and immutable Versions remain readable for historical lineage under applicable permissions/availability. No-write is not no-read. Any future restore capability requires explicit new Grill.
- **Repeat behavior:** A new retire/remove request whose current revision matches an already-target-state root succeeds as a no-op, changing no revision, Baseline or business time. Stale revision conflicts. Same-request replay is governed separately by the forthcoming receipt protocol. Last-available-Resume removal prohibition and atomic default replacement remain effective.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; evidence/resumes-grounding/candidate-save/storage reader boundaries.

<a id="cg03-q65"></a>

### CG03-Q65 — Complete content replacement rather than generic PATCH

- **Status:** ACCEPTED. M1 content Saves replace complete business content atomically; no generic PATCH/operation-list API. Missing required fields are invalid, never preserve-old-value instructions. Valid null clears a nullable value; an empty array explicitly empties that collection. Submitted section/member/block/run order fully replaces its previous order; no hidden merge. Revision conflicts preserve Draft, not a server-side merge into newer state.

| Content operation | Complete business payload |
| --- | --- |
| Profile Save | full_name, phone_number, email |
| Evidence Create | kind, fields, content |
| Evidence Update | fields, content; no kind change |
| Resume document Save | profile_version_id, header_presentation, sections, document_presentation |

- **Boundary:** New Resume creation also supplies resume_name. Existing root rename, retire/remove and default selection are explicit separate operations. Writes cannot directly set generated IDs, current pointers, version metadata or publication times. This defines business payloads, not final HTTP envelopes/routes/revision/request_id fields or result schemas.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; candidate-save and owning domain command scopes.

## Round 14 — Scalar Admission, Command Surface and Confirmed Default Replacement

<a id="cg03-q66"></a>

### CG03-Q66 — Numeric values and canonical picker color

- **Status:** ACCEPTED WITH UI CLARIFICATION. line_spacing_pt uses 0.5-pt steps, retaining Q61's 14–30 range and minimum font_size_pt + 2. Both point-valued fields use JSON numeric value semantics: 12, 12.0 and 1.2e1 are equivalent; strings, booleans and null are invalid. Reject off-grid/out-of-range values without rounding or clamping. font_family exactly matches its enum, without case or whitespace repair. theme_color exactly matches ASCII #[0-9A-Fa-f]{6}, canonicalized to uppercase without trim; shorthand, alpha suffixes and named colors are invalid.
- **UI:** Use a Color Picker/palette and submit the selected canonical Hex value. Backend admission remains authoritative. The four Q61 Draft defaults remain unchanged; no frontend implementation is introduced.
- **Writeback:** Product §3.3; Architecture §5.2; Acceptance §4.1; planned resumes-grounding scope.

<a id="cg03-q67"></a>

### CG03-Q67 — Explicit HTTP mutation operations

- **Status:** ACCEPTED. The following M1 mutation routes use POST and return 200 on success. A path identity is not repeated in the body. Existing-root commands use revision for the expected root revision; Evidence/Resume creation does not send a fabricated initial revision.

| Operation | Route |
| --- | --- |
| Profile Save | /api/v1/profile/save |
| Evidence Create | /api/v1/evidence-items |
| Evidence Update | /api/v1/evidence-items/{evidence_item_id}/save |
| Evidence Retire | /api/v1/evidence-items/{evidence_item_id}/retire |
| Resume Create | /api/v1/resumes |
| Resume document Save | /api/v1/resumes/{resume_id}/save |
| Resume Rename | /api/v1/resumes/{resume_id}/rename |
| Resume Remove | /api/v1/resumes/{resume_id}/remove |
| Set default Resume | /api/v1/workspace/default-resume/set |

- **Open boundary:** Complete request/result schemas, reads, media/body admission and the separate default-pointer concurrency representation remain pending. These are accepted routes for later normative publication, not implemented endpoints.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned candidate-save/domain/workspace interfaces and SL-02.M1.

<a id="cg03-q68"></a>

### CG03-Q68 — Success receipts for every user mutation

- **Status:** ACCEPTED. Every M1 user mutation above carries a client-generated request_id separate from business identity. Retries of the same operation retain it. Successful commands, including successful no-ops, durably retain a receipt atomically with any business changes. Replay returns the original confirmed result without executing again or reverting current pointers/state to that historical result. Reusing a successful key for a different operation, target, expected revision or canonical content produces REQUEST_CONFLICT.
- **Admission distinction:** Successful receipt replay is distinct from an ordinary new command; the latter still checks revision before canonical equality/no-op. Current content equality alone cannot prove that an interrupted request succeeded.
- **Open boundary:** Exact key representation/namespace, retention, fingerprint encoding, result shape and failure/processing precedence remain pending. Existing M1/M2 protocols do not silently supply these missing S2 definitions.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; planned candidate-save/storage interfaces.

<a id="cg03-q69"></a>

### CG03-Q69 — Per-Item concurrency and complete Baseline publication

- **Status:** ACCEPTED. Evidence update/retire uses the target Item revision, without a client expected Baseline ID or global Knowledge revision. Different-Item writes do not conflict solely because another Item advanced the Baseline; each successful command atomically derives the complete latest ACTIVE/current set and advances the domain-owned pointer without dropping other committed changes. Concurrent same-Item changes still obey root revision admission. Evidence creation follows Q67 without an invented preexisting Item revision.
- **Boundary:** No client-maintained Candidate aggregate concurrency gate. Storage locking/constraints must implement the accepted atomic behavior; a client-observed old Snapshot is not a replacement source for current Knowledge.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned evidence/candidate-save/storage seam.

<a id="cg03-q70"></a>

### CG03-Q70 — Adjacent replacement confirmed before default removal

- **Status:** ACCEPTED USER REPLACEMENT. Removing the default Resume does not require the user to manually choose a replacement. Frontend selects the next ACTIVE Resume in the canonical Resume list order; if no next item exists, it selects the previous ACTIVE item. The confirmation dialog explicitly displays the exact Resume that will become default. After confirmation, remove submits that exact replacement_resume_id.
- **Commit:** Backend atomically removes the target and switches the default pointer to the submitted replacement. If the replacement is no longer ACTIVE, the default pointer has changed or another concurrency precondition fails, reject the whole operation without choosing another replacement. Removing the last ACTIVE Resume remains forbidden. Non-default removal does not itself change the default; default selection does not publish a ResumeVersion or adopt newer Profile/Evidence sources.
- **Open boundary:** Canonical list ordering/read snapshot, default-pointer concurrency fields and complete remove/no-op/replay validation order remain pending. The earlier recommendation for manual replacement selection was not accepted; no accepted historical decision is being silently rewritten.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; planned workspace/resumes-grounding/candidate-save scopes.

## Round 15 — Stable List Order, Small Selection State and Replay-Safe Reads

<a id="cg03-q71"></a>

### CG03-Q71 — Canonical ACTIVE Resume ordering

- **Status:** ACCEPTED. Order ACTIVE Resume roots by created_at ascending, then canonical resume_id string ascending for equal timestamps. UUID tie-breaking is deterministic, not actual creation chronology. Rename, document Save and default selection do not reorder entries; mark the default without pinning it above others.
- **Confirmation:** Q70 adjacency uses the list read when opening the confirmation dialog. After confirmation, newly created entries do not cause replacement recomputation or invalidate the confirmed exact replacement by themselves; the originally displayed ID remains the target if its availability and other concurrency preconditions still hold.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; planned Resume list/Workspace interface.

<a id="cg03-q72"></a>

### CG03-Q72 — Small independently revisioned default selection

- **Status:** ACCEPTED WITH SCOPE CLARIFICATION. DefaultResumeSelection is a small Workspace-owned Contract selection state with default_resume_id (UuidV4 or null) and revision, not a heavyweight Domain Aggregate or generic Workspace configuration framework. Initialize null/revision 1. First successful Resume creation atomically selects it and increments this revision. Real switches, including replacement on default removal, increment once; same-target selection with matching revision is a no-op. Stale revision conflicts even when the current ID matches, detecting A→B→A.
- **Isolation:** Ordinary Resume content edits, renames and non-default changes do not advance selection revision. No selection-history version family is introduced. This selection is separate from the Evidence/Baseline-owned current pointer; physical storage placement is not new authority. Exact command precondition fields, overflow behavior and storage evolution remain to be specified.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; planned workspace/candidate-save/storage scope.

<a id="cg03-q73"></a>

### CG03-Q73 — SL-02 command-family receipts

- **Status:** ACCEPTED WITH SCOPE CLARIFICATION. The nine SL-02.M1 user mutations share one SL-02 command-family request_id namespace per Workspace; clients generate Common UUIDv4 keys. A successfully used key cannot be reused for another operation, target or canonical request. This is a scoped namespace, not a Universal Idempotency Framework. Published Manual Entry and Preferences namespaces remain independent and unchanged.
- **Retention:** Retain success receipts for the Workspace lifetime, with no v1 TTL and no deletion on business-object retirement/removal or later publication. Restart preserves exact successful replay and duplicate-create protection. Fingerprint encoding, receipt/result representation and physical constraints remain pending.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned candidate-save/storage interface.

<a id="cg03-q74"></a>

### CG03-Q74 — Pure admission before receipt, state checks after replay

- **Later scoped correction:** CG03-Q98 permits Evidence Update to read the target Item's immutable kind before type-specific admission/canonicalization and receipt lookup. Revision/lifecycle/freshness admission still follows receipt miss.

- **Status:** ACCEPTED. Process request parsing, structural/value validation and canonicalization first; then look up the successful receipt. A matching fingerprint returns the original result, a mismatching successful key returns REQUEST_CONFLICT. Only when no receipt exists do current revision/lifecycle/source-freshness and other state preconditions govern new execution, followed by atomic business/receipt commit.
- **Boundary:** The initial phase checks the request itself, not whether its referenced source is still current or a root has since retired. A committed-but-lost Resume Save can replay after later Evidence publication without repeating freshness admission. An explicitly failed, uncommitted command has no success receipt. Unknown outcomes retain the original request/key for verification rather than using a new key to execute again. Exact transport/error precedence and persisted receipt schema remain pending.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; planned candidate-save recovery/admission scope.

<a id="cg03-q75"></a>

### CG03-Q75 — Consistent current root/version reads

- **Status:** ACCEPTED. The following GET operations succeed with 200 and return a consistent root/current-Version pair from one read snapshot. The returned Version ID equals the root current pointer; never mix pre-write root with post-write Version.

| Route | Result fields |
| --- | --- |
| /api/v1/profile | profile, profile_version |
| /api/v1/evidence-items/{evidence_item_id} | evidence_item, evidence_item_version |
| /api/v1/resumes/{resume_id} | resume, resume_version |

- **Historical availability:** Exact-root reads allow RETIRED Evidence and REMOVED Resume, retaining their status and last current Version without restoring write eligibility. A nonexistent Evidence/Resume ID returns 404. Resume references remain exact; no latest Profile/Evidence substitution. Historical-Version, Baseline and list operations remain separate pending definitions, as do full HTTP admission and failure representations.
- **Writeback:** Architecture §5.2; Acceptance §4.1–4.2; planned profile/evidence/resumes-grounding/storage readers.

## Round 16 — Removal Preconditions, Retained Readers and Raw Admission

<a id="cg03-q76"></a>

### CG03-Q76 — Separate Resume and default-selection preconditions

- **Status:** ACCEPTED WITH ORDER CLARIFICATION. Set-default body contains request_id, revision (expected DefaultResumeSelection revision), and default_resume_id (target ACTIVE Resume). Remove body contains request_id, revision (target Resume), default_resume_selection with its required revision, and required replacement_resume_id (UuidV4 or null). Path identity is not repeated.
- **New execution order:** After request-only admission and a receipt miss, check target Resume revision. If it matches and the root is already REMOVED, succeed as a no-op without checking current default revision or replacement state. Otherwise check DefaultResumeSelection revision, determine default/non-default semantics and atomically remove with any default replacement. Even non-default removal checks the selection token, preventing a confirmation-time non-default from silently being deleted after another page makes it default.
- **ACTIVE path:** Default removal requires a different ACTIVE replacement; non-default removal requires replacement_resume_id = null. Replacement semantic checks apply only on this ACTIVE path; syntax/type admission still applies before receipt/no-op. Replacement rename/document change alone does not conflict and no replacement root revision is required. Last-ACTIVE removal remains forbidden. Any required revision increment beyond Common's maximum fails the whole command; a valid no-op needs no increment.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; Workspace/Resume/Save/Storage planned interface.

<a id="cg03-q77"></a>

### CG03-Q77 — Consistent full ACTIVE Resume list and selection

- **Status:** ACCEPTED WITH CAPACITY FOLLOW-UP. GET /api/v1/resumes returns 200 with resumes (complete ACTIVE Resume roots in Q71 order, without document bodies) and default_resume_selection (the Q72 object) from one consistent read snapshot. Default identity is a field, never list reordering. No pagination, filtering or sorting parameters in v1. Before first creation return [] and null/revision 1 without creating a Resume.
- **Open boundary:** A numerical Resume-count capacity must be decided in a later capacity Grill to bound this full-list design. No quota, counting population or pagination is inferred here.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; planned Resume/Workspace read seam.

<a id="cg03-q78"></a>

### CG03-Q78 — Exact immutable and current Baseline readers

- **Status:** ACCEPTED. These GET operations succeed with 200:

| Route | Result |
| --- | --- |
| /api/v1/profile/versions/{profile_version_id} | ProfileVersion |
| /api/v1/evidence-items/versions/{evidence_item_version_id} | kind and evidence_item_version |
| /api/v1/resumes/versions/{resume_version_id} | ResumeVersion |
| /api/v1/evidence-baselines/current | Current EvidenceBaselineSnapshot |
| /api/v1/evidence-baselines/{evidence_baseline_snapshot_id} | Exact EvidenceBaselineSnapshot |

- **Reference meaning:** Evidence kind is derived from the owning Item, not another Version authority. Missing requested exact IDs return 404, never current substitution. Retirement/removal alone does not disable retained reads. Current Baseline always returns a real Snapshot, including an empty one, not null. M1 adds no historical-version lists, history sorting or history picker.
- **Writeback:** Architecture §5.2; Acceptance §4.1–4.2; planned Profile/Evidence/Resume/Storage reader interfaces.

<a id="cg03-q79"></a>

### CG03-Q79 — Strict S2 JSON transport boundary

- **Status:** ACCEPTED. POST accepts application/json and compatible charset=utf-8 parameters with actual UTF-8 body; Content-Encoding is absent or identity. Reject malformed JSON, duplicate object keys, non-object request roots and unknown fields without stripping/coercion. Required omission differs from explicit null; only owner-declared nullable fields admit null. Strings/booleans are not numbers. The currently defined GET operations accept no query/body; POST accepts no extra query.
- **Errors:** Reuse Common ContractError/FieldError representation, without echoing raw input or user-supplied unknown keys. Complete classifications, nested-path adoption and HTTP mappings remain pending except Q80's accepted byte-excess mapping. Existing SL-01 consumers are unchanged.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned Common/candidate-save/domain HTTP scopes.

<a id="cg03-q80"></a>

### CG03-Q80 — Pre-canonicalization byte and structural budgets

- **Status:** ACCEPTED WITH ERROR-DISTINCTION CLARIFICATION.

| POST scope | Maximum UTF-8 body bytes |
| --- | --- |
| Resume Create/document Save | 8 MiB (8,388,608) |
| Evidence Create/Update | 1 MiB (1,048,576) |
| Profile Save, Resume Rename, Evidence Retire, Resume Remove, Set Default | 64 KiB (65,536) |

- **Raw structure:** At most 100,000 raw JSON value nodes per request: every object, array and scalar counts once, including the root; object keys do not add nodes. At most 32 nested object/array containers, counting the root as depth 1. Enforce before canonicalization; do not merge runs, deduplicate, drop nodes or truncate to admit an oversized request. Count bytes during reading rather than trusting Content-Length, and constrain depth during parsing. These bounds apply together with field/body/document limits; individually valid values do not guarantee a valid combined request.
- **Failure:** Body-byte excess maps to 413 REQUEST_TOO_LARGE. Node/depth excess requires a separate explicit structural-complexity validation code, still to be selected; do not classify it as byte excess or ordinary business-field capacity. Failure admits no partial mutation.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned Common/HTTP/candidate-save scope.

## Round 17 — Capacity, Error Paths and Historical Command Results

<a id="cg03-q81"></a>

### CG03-Q81 — ACTIVE Resume capacity

- **Status:** ACCEPTED. A Workspace admits at most 100 ACTIVE Resume roots. Removed roots, immutable versions and receipts do not consume ACTIVE slots and are not deleted by this policy. Creation checks capacity atomically so concurrent creates cannot exceed it. At capacity, existing edit/rename/default/removal remains available; removal frees a slot. Successful replay precedes capacity checks and consumes no new slot. A new over-capacity creation returns 409 CAPACITY_EXCEEDED with no root, Version or success receipt committed. This quota is independent of Q62's 100 members per document.
- **Writeback:** Product §3.4; Architecture §5.3; Acceptance §4.2; planned resumes-grounding/candidate-save/Common error scope.

<a id="cg03-q82"></a>

### CG03-Q82 — Structural complexity is not request byte size

- **Status:** ACCEPTED. Raw node/depth excess produces 422 VALIDATION_ERROR with field_errors containing field = $ and code = STRUCTURE_TOO_COMPLEX. Either limit uses this classification; no full traversal or collection of other field errors is promised after rejection. Byte excess remains 413 REQUEST_TOO_LARGE with field_errors = []. Common owns the shared FieldError code representation when S2 normative scope is published; S2 HTTP owns limits/triggers. Prior M1/M2 behavior is unchanged.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned Common/candidate-save HTTP scope.

<a id="cg03-q83"></a>

### CG03-Q83 — S2 nested error paths

- **Status:** ACCEPTED. S2 explicitly adopts the small COM-034-style nested-path grammar: $ or dot-separated known canonical names with optional nonnegative array indices. No full JSONPath. Array indices refer to submitted arrays before canonicalization/merge/sorting. Missing fields use the expected path; unknown keys use UNKNOWN_FIELD at the nearest known parent without echoing the supplied key. Cross-field combinations locate their common known parent. Clients do not depend on field-error order. This extends consumption to S2 without changing M1's original top-level path convention.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned Common and owning field-admission scopes.

<a id="cg03-q84"></a>

### CG03-Q84 — Remaining complete write bodies and first-create concurrency

- **Status:** ACCEPTED WITH CONCURRENT-CREATE CLARIFICATION. No generic payload wrapper. Every listed field is present; owner-declared nullable values remain valid. Q76 owns the two other command bodies.

| Operation | Body fields |
| --- | --- |
| Profile Save | request_id, revision, full_name, phone_number, email |
| Evidence Create | request_id, kind, fields, content |
| Evidence Update | request_id, revision, fields, content |
| Evidence Retire | request_id, revision |
| Resume Create | request_id, resume_name, profile_version_id, header_presentation, sections, document_presentation |
| Resume document Save | request_id, revision, profile_version_id, header_presentation, sections, document_presentation |
| Resume Rename | request_id, revision, resume_name |

- **Identity/metadata:** Existing object identity comes from path; singleton Profile needs no profile_id in the request. Create has no root revision or default-selection token. Clients do not supply new business IDs, publication timestamps/current pointers or saved-object schema_version.
- **Concurrent initial creation:** The first successful transaction establishing an ACTIVE Resume also establishes default null→that Resume and selection revision 1→2. Another concurrently prepared Create can also succeed: at its commit it observes the established default and leaves it unchanged. Its earlier observation of null does not create a selection-revision conflict. Normal capacity, source admission and other applicable conditions still apply; this is not unconditional creation success.
- **Writeback:** Product §3.2/3.4; Architecture §5.2/5.3; Acceptance §4.1–4.2; planned candidate-save/domain/workspace requests.

<a id="cg03-q85"></a>

### CG03-Q85 — Frozen successful command results

- **Status:** ACCEPTED WITH HISTORICAL-RESULT CLARIFICATIONS. Every successful result includes request_id and outcome, plus the fields below. Outcomes are CREATED, UPDATED, RETIRED, REMOVED and UNCHANGED; content/name/default changes use UPDATED, first lifecycle changes use their specific outcome and valid no-ops use UNCHANGED.

| Operation | Additional result fields |
| --- | --- |
| Profile Save | profile, profile_version |
| Evidence Create/Update/Retire | evidence_item, evidence_item_version, evidence_baseline_snapshot_id |
| Resume Create/Remove | resume, resume_version, default_resume_selection |
| Resume document Save/Rename | resume, resume_version |
| Set Default | default_resume_selection |

- **Version meaning:** Return the command-time current Version even when rename/retire/remove/no-op publishes no Version. Results describe the completed command, not a later latest-state read. Replay returns the original result/outcome, never REPLAYED, and never rewinds authority.
- **Replay reconstruction:** Persist enough command-result history to reproduce mutable root/selection values plus exact immutable refs. Do not re-read today's mutable root to assemble a historical result. Rename at revision 4/name Backend Resume must replay that result after a later revision 5/name AI Backend Resume. These snapshots are command-result history, not another business authority. Exact receipt fields/encoding are the next Grill boundary.
- **Evidence no-op:** Return the current Baseline ID at this command's successful completion without creating a Baseline. If it was B10, replay remains B10 after another command publishes B11.
- **Default selection:** Resume Create/Remove and Set Default results freeze the selection at completion. Creating the first R1 returns R1/revision 2; replay still returns that selection after a later switch to R2/revision 3. Current state requires a separate GET; never mix today's selection with an old command result.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1–4.2; planned candidate-save/storage/result interfaces.

## Round 18 — Receipt Representation, Deterministic Fingerprints and Recovery

<a id="cg03-q86"></a>

### CG03-Q86 — Candidate command receipt representation

- **Status:** ACCEPTED. CandidateCommandReceipt contains request_id, command_type, request_fingerprint, schema_version (initially 1), outcome and result_snapshot. command_type is PROFILE_SAVE, EVIDENCE_CREATE, EVIDENCE_UPDATE, EVIDENCE_RETIRE, RESUME_CREATE, RESUME_SAVE, RESUME_RENAME, RESUME_REMOVE or DEFAULT_RESUME_SET.

| Operation | result_snapshot fields |
| --- | --- |
| Profile Save | profile (complete root snapshot), profile_version_id |
| Evidence operations | evidence_item (complete root snapshot), evidence_item_version_id, evidence_baseline_snapshot_id |
| Resume Create/Remove | resume (complete root snapshot), resume_version_id, default_resume_selection (complete command-time snapshot) |
| Resume Save/Rename | resume (complete root snapshot), resume_version_id |
| Set Default | default_resume_selection (complete command-time snapshot) |

- **Reconstruction:** Mutable values come only from stored result snapshots. Resolve immutable content using the exact retained IDs. Each stored root current pointer agrees with the corresponding result Version ID. Do not copy complete immutable bodies or raw request bodies into receipts, add business revision/lifecycle, use receipts to edit facts, or treat them as a current-state query authority. This is command-result history within the scoped SL-02 namespace.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned candidate-save/storage representation.

<a id="cg03-q87"></a>

### CG03-Q87 — Complete typed fingerprint encoding

- **Status:** ACCEPTED WITH USER COMPLETIONS. request_fingerprint is Common Sha256Hex of the bytes below. The outer value is exactly the three-element array [command_type, target_id, input], not an implicit concatenation or object. target_id is the canonical path object ID, or null where none exists. input is the canonical request body with request_id excluded. Include every caller precondition/replacement/content field, but no generated IDs/timestamps/post-commit Baseline or selection state.

```text
fingerprint = SHA-256(UTF8("JobHunter:SL02:Command:1\n") + encode([command_type, target_id, input]))
```

The prefix notation \n denotes one LF byte. There is no indentation, extra whitespace or separator beyond the encoding below; the outer encoding begins with ASCII a3:.

| Value | Exact encoding |
| --- | --- |
| null | ASCII n |
| false / true | ASCII b0 / b1 |
| string | ASCII s + UTF-8 byte length + ASCII : + exact UTF-8 bytes |
| number | ASCII d + canonical decimal ASCII byte length + ASCII : + canonical decimal bytes |
| array | ASCII a + element count + ASCII : + concatenated ordered element encodings |
| object | ASCII o + field count + ASCII : + encoded key/value pairs, keys sorted by Unicode code point |

- **Numbers/counts:** Lengths/counts use ASCII decimal integers without leading zeros. Numeric values use ordinary decimal without exponent, redundant leading zeros or trailing fractional zeros; -0 encodes as 0. NaN/Infinity are invalid inputs and never enter fingerprinting. Boolean is distinct from number. This complete codec does not admit booleans into numeric fields, zero into positive-only fields or any otherwise invalid command input.
- **Equality:** Apply accepted field/mark/run/color canonicalization first. JSON spelling/key order and admitted equivalent representations do not change the fingerprint. Preserve meaningful array order and string content. This encoding is only for SL-02; existing fingerprint protocols remain unchanged.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned candidate-save fingerprint and Common scalar consumption.

<a id="cg03-q88"></a>

### CG03-Q88 — Request-only Evidence Update schema admission

- **Superseded by CG03-Q98:** The request-only six-schema union and later Item-kind comparison are replaced by authoritative immutable Item.kind lookup before field validation. The following text preserves the earlier decision, not the current algorithm.

- **Status:** ACCEPTED. Before receipt lookup, Evidence Update.fields must completely satisfy one of the six accepted field schemas and canonicalize under it. The legal shapes are distinguished by school_name/company_name/project_name/skill_name/award_name/certification_name. A receipt miss then requires this admitted shape to agree with the actual immutable EvidenceItem.kind. Valid PROJECT-shaped fields cannot update a WORK_EXPERIENCE Item.
- **Authority:** Choosing a validation branch is not another kind authority or permission to convert an Item. No additional kind input is added to Update; no current business-content read is needed merely to canonicalize replay input. Malformed/incomplete/mixed shapes still fail declared schema admission; detailed ambiguous-invalid-branch error priority remains part of final validation reconciliation.
- **Writeback:** Architecture §5.2; Acceptance §4.1; planned Evidence/candidate-save admission.

<a id="cg03-q89"></a>

### CG03-Q89 — Lifecycle and reference failure classification

- **Later scoped correction:** Q98 replaces Update alternate-schema/Item-kind mismatch with validation directly against the authoritative target kind. Its discriminator read precedes receipt; a missing target at that discriminator lookup returns 404 before receipt, even for a key previously used elsewhere (Q98 clarification). Other reference/lifecycle classes remain effective.

- **Status:** ACCEPTED. Apply these after a receipt miss where state admission is required, in the previously accepted check order:

| Trigger | Classification |
| --- | --- |
| Command path root absent, or GET exact ID absent | 404 NOT_FOUND |
| Update retired Evidence; edit/rename removed Resume; choose inactive default/replacement | 409 INVALID_STATE |
| Newly introduced/switched Resume source no longer current, or newly adopted Evidence retired | 409 SOURCE_CONFLICT |
| Remove the final ACTIVE Resume | 409 LAST_RESUME_REQUIRED |
| Request-body reference absent/wrong owner; section kind disagrees with Item; Update field shape disagrees with Item.kind | 422 VALIDATION_ERROR with INVALID_REFERENCE at the corresponding path |

- **Exceptions:** Valid unchanged historical bindings do not trigger SOURCE_CONFLICT; matching-revision repeated retire/remove follows its existing no-op rule. REVISION_CONFLICT, REQUEST_CONFLICT, REVISION_EXHAUSTED and CAPACITY_EXCEEDED remain separate. Requested bad references do not redefine missing/corrupt persisted lineage as ordinary input error. Common will own representations when normative scope is published; actual triggers remain with their owners.
- **Writeback:** Architecture §5.2/5.3; Acceptance §4.1–4.2; planned Common/domain/HTTP errors.

<a id="cg03-q90"></a>

### CG03-Q90 — Honest uncertain-write recovery

- **Status:** ACCEPTED. Success includes a confirmed historical replay. Contract rejection or 503 STORAGE_UNAVAILABLE with established non-commit is a definite rejection/non-commit. Timeout, connection loss, 503 OUTCOME_UNKNOWN and other 5xx lacking non-commit proof are pending verification.
- **Client:** Retain the original request_id and complete original request, suspend replacing that pending operation with different input, and resend the identical command when the user retries verification. Do not infer success from similar current content/list names, create with a fresh key or present an unknown outcome as definite rollback/failure. A separate latest-state GET after confirmed success may fail without undoing that success. OUTCOME_UNKNOWN belongs to the command outcome, never Profile/Evidence/Resume lifecycle.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; planned candidate-save/client/storage recovery seam.

## Round 19 — Evidence Browsing, Schema 3 and Material Milestone Boundary

<a id="cg03-q91"></a>

### CG03-Q91 — ACTIVE Evidence list with exact current projection

- **Status:** ACCEPTED WITH EXACT-ID CLARIFICATION. GET /api/v1/evidence-items returns 200 with evidence_items. Each entry contains evidence_item (complete root), current_evidence_item_version_id (explicit read projection equal to the root pointer), and fields (that exact current Version's structured fields). All ACTIVE entries/fields/pointers come from one consistent read snapshot. Do not separately duplicate kind/status/revision outside the root; projected ID/fields have no independent authority or persistence.
- **Browsing:** Order by created_at ascending then canonical evidence_item_id ascending. No pagination/search/filter/sort parameters in v1; UI may group by Item.kind. Exclude content from the list; use existing complete readers for details/editing/source inclusion. Empty Knowledge returns [] without creation. The explicit ID identifies the source of the returned fields; a later detail read still obeys exact-source/freshness semantics.
- **Writeback:** Product §3.1; Architecture §5.2; Acceptance §4.1; planned Evidence reader scope.

<a id="cg03-q92"></a>

### CG03-Q92 — ACTIVE Knowledge capacity

- **Status:** ACCEPTED. At most 1,000 ACTIVE EvidenceItems per Workspace. New creation checks capacity atomically; concurrent creates cannot exceed it and excess returns 409 CAPACITY_EXCEEDED. Retired Items, historical Versions/Baselines and receipts do not consume ACTIVE slots and are not erased. At capacity, update/retire/read remains possible; retirement frees a slot and success replay consumes none. This is a stored-current-object limit, not Resume membership or guaranteed whole-Knowledge model admission.
- **Writeback:** Product §3.1; Architecture §5.2; Acceptance §4.1; Evidence/Save/Storage planned scopes.

<a id="cg03-q93"></a>

### CG03-Q93 — Planned schema-3 initialization and explicit migration

- **Status:** ACCEPTED. S2 targets storage schema 3; actual current runtime remains schema 2 until implementation. Add a new migration without rewriting published schema-1/2 history. Preserve database/application identity, Entry/Preferences rows and receipts. Use the existing explicit offline migration entry and physical-directory exclusive lock; runtime cannot concurrently use that directory. Commit schema, initial records and migration metadata atomically, never recognize a partial target as complete.
- **Initial state:** Fresh schema-3 storage or explicit upgrade publishes the real empty Profile/version, empty Baseline/domain current pointer and null/revision-1 default selection. No Resume is auto-created; Preferences stays lazy. Normal startup recognizes supported complete storage but does not migrate/repair missing records. Schema 1 follows the retained migration chain rather than bypassing or modifying prior migrations.
- **Writeback:** Architecture §5.1/13; Acceptance §4.1/10; planned Storage and SL-02.M1 migration scope.

<a id="cg03-q94"></a>

### CG03-Q94 — Relational identity and lineage, JSON internal content

- **Status:** ACCEPTED WITH OWNERSHIP CLARIFICATION. Relational columns/tables carry identity, lifecycle, concurrency, lineage and exact references. Keep root metadata/current pointers and immutable-version identity/owner/schema/source refs/time explicit. References requiring FK/existence/same-owner/lineage guarantees cannot live only inside JSON; enforce necessary integrity with actual database constraints, with concrete SQL left to implementation.
- **Internal structures:** JSON may represent type-specific Evidence fields/content, Resume-local AST, Header and document presentation. Resume/Baseline membership may use internal relation rows and ordering columns without creating business IDs. Historical command snapshots may retain JSON representation, but required exact reference integrity still has relational support. JSON is not an authority shortcut: Application canonicalization exclusively determines business equality, not serialized bytes/key order/whitespace. Database constraints do not replace Domain/Application value admission. No cascade may destroy retained lineage through ordinary retire/remove.
- **Writeback:** Architecture §13; Acceptance §10; planned Storage representation.

<a id="cg03-q95"></a>

### CG03-Q95 — Material demand and durable intent move to SL-02.M2

- **Status:** ACCEPTED MILESTONE-SCOPE SUPERSESSION. Replaces the plan that M1 first delivers durable demanded intent for M2 to reuse. M1 delivers formal owned Saves, exact Resume/Profile/Evidence readers, retained history/source-currentness boundaries and local Draft A4 preview. Save success is not durable preview/PDF/export readiness. Actual render demand, renderer configuration, durable intent/work and output/readiness/recovery are defined and delivered together in M2, not speculative M1 fields or queues.
- **Preserved atomicity:** When M2 introduces an actual existing material demand that requires updating on Save, extend that Save's transaction to include the required durable intent. A lossy post-commit notification is not a substitute. Rendering remains post-commit; source current-pointer movement alone never implicitly changes a bound Resume or demands a rerender.
- **Contract/readiness:** foundation/derived-work.md is no longer an M1 required normative portion. M1 retains only applications/materials.md's exact-source/currentness and Save-not-output-ready boundary. M2 consumes materials/derived-work and the necessary candidate-save/Storage extension. Import/Advisor reuse M1 authority and result protocols; material intent is conditional on actual M2 demand/integration. Preparation obtains durable demand from M2, not M1.
- **History:** Earlier Grill statements about M1 required intent are scoped by this decision, not erased. This changes milestone delivery, not the general rule that genuinely required intent and authority commit atomically. It creates no new milestone or normative ID and grants no readiness.
- **Writeback:** Product §3.5; Architecture §5.2/5.4/16.3; Acceptance §4.3; global/SL-02/SL-04/SL-07/SL-10 plans; Contract Structure and scope-readiness ledger.

## Round 20 — Admission, Shared Errors and Storage Integrity

<a id="cg03-q96"></a>

### CG03-Q96 — Existing local access and HTTP admission boundary

- **Status:** ACCEPTED. S2 retains Workspace loopback and configured exact Host/Origin admission before business handling; rejection is 403 ACCESS_DENIED. Current development host/port defaults are not new S2 constants. Invalid encoding, unsupported media type/Content-Encoding, malformed JSON and duplicate decoded keys return 400 BAD_REQUEST. Parseable wrong root/type/field/value or prohibited query/GET body returns 422 VALIDATION_ERROR. Existing byte excess remains 413 REQUEST_TOO_LARGE; node/depth excess remains 422 VALIDATION_ERROR with STRUCTURE_TOO_COMPLEX at $. No total ordering of simultaneously invalid admission conditions is promised; preserve required access, validation/canonicalization, receipt and mutable-state phases, as scoped by Q98.
- **Writeback:** Architecture §5.2; Acceptance §4.1; Workspace/Common/candidate-save consumed interfaces.

<a id="cg03-q97"></a>

### CG03-Q97 — Single shared FieldError vocabulary and owner-specific triggers

- **Status:** ACCEPTED WITH LONG-TERM OWNERSHIP PRINCIPLE. common.md is the single normative owner of stable FieldError.code vocabulary and shared error representation. Evidence/Profile/Resume and other consuming Contracts reference that vocabulary and define when their fields/operations trigger it; they do not duplicate or independently redefine the codes. This is an enduring cross-contract boundary, not an S2-only convenience. New shared vocabulary is added through Common with explicitly scoped consumer applicability, preserving published consumers' semantics.

| Condition in the consumed S2 scope | FieldError.code |
| --- | --- |
| Required key missing | REQUIRED |
| Wrong type or disallowed null | INVALID_TYPE |
| Undeclared key | UNKNOWN_FIELD |
| Blank under the field's established check | BLANK_VALUE |
| Text exceeds its length bound | TOO_LONG |
| Prohibited characters | INVALID_CHARACTERS |
| Invalid enum/month/email/phone/URL/color format | INVALID_FORMAT |
| Numeric range, half-point grid or collection-count violation | OUT_OF_RANGE |
| Invalid month interval, line-spacing/size combination, duplicate section/member/mark | INVALID_FORMAT at the common parent or corresponding collection |
| Raw JSON node/depth excess under Q82 | STRUCTURE_TOO_COMPLEX at $ |

- **Classification:** Missing/type failures are not additionally reinterpreted as format failures. Return at least one accurate field error; neither exhaustive enumeration nor error-array ordering is promised. Existing nested paths, permitted null/empty values, character checks, canonicalization and INVALID_REFERENCE triggers remain unchanged.
- **Writeback:** Architecture §5.2/16.1; Acceptance §4.1; Contract Structure Common and consuming-owner boundaries. Normative vocabulary additions remain part of the upcoming reviewed Common scope, not copies in domain documents.

<a id="cg03-q98"></a>

### CG03-Q98 — Authoritative immutable kind selects Evidence Update schema

- **Status:** ACCEPTED USER REVISION; SUPERSEDES CG03-Q88 and the affected request-only wording of Q74. Evidence Update does not infer its schema from six payload keys and does not add kind to the request body.
- **Order:** Admit the common request envelope, request_id/revision syntax, object-shaped fields and basic shared content structure; read the target EvidenceItem's permanent immutable kind using the path identity; validate fields and shared semantic content under the authoritative schema; canonicalize and fingerprint; inspect receipt; only on receipt miss perform revision/lifecycle and remaining mutable-state admission, followed by atomic execution.
- **Meaning:** Reading kind obtains the sole schema discriminator, not mutable business eligibility. It does not reject merely because the retained Item is RETIRED, require its current Version's content for schema inference, or compare revision before replay. A WORK_EXPERIENCE update missing company_name produces REQUIRED at fields.company_name. Fields belonging to another kind are checked as invalid input under the actual target schema, not admitted as an alternate union and later classified as a kind-conversion reference error. Evidence Create continues using its declared creation kind.
- **Accepted precedence clarification:** If the target is absent during immutable-kind resolution, return 404 NOT_FOUND before fingerprint/receipt processing, even if request_id was previously used for a different target; do not prefer REQUEST_CONFLICT. This narrowly scopes the general Q68/Q74/Q89/Q99 used-key/missing-target ordering. Successful Update targets remain retained, so ordinary retirement cannot break their replay. An actually detected corrupt persisted receipt/reference remains Q100 integrity failure.
- **History/replay:** Permanent kind and retained Item identity make schema selection stable after content changes/retirement. Successful historical replay still precedes mutable revision/lifecycle admission. Ordinary missing path targets retain Q89 NOT_FOUND; broken persisted references retain Q100 integrity handling, never schema guessing or business reexecution.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; Evidence/candidate-save planned interfaces and current progress records.

<a id="cg03-q99"></a>

### CG03-Q99 — Concurrent receipt arbitration and retry evidence

- **Status:** ACCEPTED. Concurrent equal request_id/fingerprint commands produce at most one successful business mutation; another request returns the original result once its committed receipt can be established. A successfully claimed key with a different fingerprint yields 409 REQUEST_CONFLICT; both conflicting inputs cannot succeed. A database uniqueness race is an internal signal, not automatically REVISION_CONFLICT; safely finish the competing transaction before classifying using committed receipt state.
- **Recovery:** Processing is bounded. If the outcome cannot be established, use the existing proven-non-commit versus OUTCOME_UNKNOWN distinction. Do not secretly rerun the business command; limited recovery of transaction completion requires the previously accepted safe storage semantics. A rejection of a retry does not prove an earlier uncertain attempt never committed, and does not authorize a new-key duplicate creation.
- **Writeback:** Product §3.2; Architecture §5.2; Acceptance §4.1; candidate-save/Storage interface.

<a id="cg03-q100"></a>

### CG03-Q100 — Broken stored lineage is an integrity failure

- **Status:** ACCEPTED. An ordinarily absent requested object is 404 NOT_FOUND. A persisted root, Resume, Baseline or receipt referencing a missing/wrong-owner object is an internal integrity fault. Affected reads return 500 INTERNAL_ERROR, never a partial list, omitted member, substituted current Version or fabricated empty authority. Failure to reconstruct a historical receipt result never authorizes reexecution.
- **Writes/startup:** Stop affected writes and safely roll back; uncertain commit remains OUTCOME_UNKNOWN. Record necessary internal diagnostics without exposing raw content/database details in HTTP errors. Missing mandatory initial records or incomplete storage detected during startup causes startup failure without repair. No exhaustive historical-body scan on every startup is required.
- **Writeback:** Architecture §5.2/13; Acceptance §4.1/10; Storage and exact-reader interfaces.

## Decision tree and current frontier

The identified SL-02.M1 decision frontier is closed after Q100 and the Q98 clarification. The user explicitly authorized the next publication step. Actual normative bodies, stable IDs and reviewed consumed interfaces are now in [Progress §6.3](../../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence); the [development handoff](../../../development/handoff/sl-02-m1-handoff.md) supports a new backend task.

M2 material demand/intent, SL-07 AI support, SL-04 Import batch and SL-05/SL-06 DeepFit remain their own future scope, not M1 gates. Concrete implementation choices cannot reopen superseded automatic propagation, infer schemas from payload keys or create private Knowledge. Surface any genuinely new semantic conflict for a targeted decision. Ready Contracts do not mean implemented UI/backend or runtime acceptance.

## Verification and later writeback

Each accepted batch records conclusions here and updates its actual owners as they become concrete. Naming follows existing Common; published IDs must not be reused or silently change meaning. Normative completion requires decision-to-document traceability and cross-document interface consistency, plus actual scope ledger/handoff updates. Documentary readiness remains separate from implementation and runtime acceptance. Existing user instruction defers frontend implementation until UI design; this Grill defines necessary product/data obligations without implementing UI.

Round-two writeback verification: independent read-only review confirmed the scoped manual Header grounding exception, three-field Profile/work-experience supersession and local-versus-durable preview split across current owners. No accidental Resume Fit or AI admission policy was found; those consumers and Q11–Q15 remain open. All edited-document local links/anchors and the existing 105 normative IDs resolve; diff whitespace checks pass. This is document review, not Contract readiness or runtime proof.

Round-four verification: Q16/Q17 text decisions are recorded here and referenced by Acceptance; Q18–Q20 inventories and the independent Candidate Education boundary are reconciled with Product, Architecture and the milestone plan. Preferences' published enum and normative bodies are unchanged. No unaccepted requiredness, future education mapping or consumer policy was promoted into the current definitions. All seven edited files' local links/anchors resolve; the Contract checker reports 105 unique requirements and git diff --check passes. These checks establish scoped document consistency, not runtime proof or M1 readiness.

Round-five verification: Q21–Q24 map to the six-kind inventories and record-level admission in Product/Acceptance; Q25 maps to Product/Architecture, editor capabilities, Contract Structure and the owning plan. A read-only boundary audit identified mark-only version effects as unresolved; the round-five owners stated that limitation rather than applying either prior rule implicitly. Q3/Q10 history is retained with scoped supersession, and Header/Profile plain text remains unchanged. All eight edited documents' local links/anchors resolve; the existing 105 normative IDs and diff whitespace checks pass. No runtime or readiness evidence is claimed.

Round-six verification: Q26/BC2 separates Evidence semantic content and per-Resume inline presentation across Product, Architecture, Acceptance, Contract Structure and the milestone plan; Q27–Q30 records scalar/month/URL admission with distinct business owners. Independent read-only review identified unresolved link-label, attachment/propagation and grounding/material interfaces; they remain open rather than implicit decisions. Q12's erroneous supersession label was corrected by its exact node, and Q10's historical wire schema remains subject to representation Grill. All eight edited documents' local links/anchors resolve, the checker reports 105 existing normative requirements, and diff whitespace checks pass. No implementation, new normative IDs or readiness claims are introduced.

BC3 writeback verification: Decision-to-Document Traceability maps BC3/A1–A5 and Q31–Q35 to current Product/Architecture, Contract planning, Slice plans and Acceptance/Eval owners in the [BC3 traceability map](../../../progress/traceability.md#22-later-architecture-supersession-cg03-bc3). Cross-Document Semantic Consistency review reconciled separate Knowledge/Profile/Resume commands, retained historical bindings, manual lineage versus AI support, unchanged document materials, two-stage Import durability and unified DeepFit with independent analysis outcomes. A read-only review identified and resolved residual manual-grounding, cross-Resume transaction and integration-dependency wording. The 21 edited documents pass local link/anchor checks; 21 protected historical/normative files retain their pre-writeback hashes; all 24 milestone IDs and the existing 105 normative requirements remain unchanged. Contract link/ID checks and diff whitespace checks pass. These are documentation checks, not runtime proof or scope readiness; detailed SL-02.M1 Grill remains paused and its unreviewed normative scope remains Pending.

Round-eight verification: CG03-Q36–Q40 maps to Product §3.2–3.3, Architecture §5.1–5.2, Acceptance §4.1–4.2, Contract Structure and the owning SL-02.M1 plan. Review distinguishes one-time local initialization from factual ownership, new membership admission from retained historical bindings, and explicit source adoption from separately chosen body replacement. Empty member content remains distinct from an empty-member section; list kinds remain blocks, not marks. Only the adjacent-equivalent-run merge principle is accepted; exact canonicalization, whitespace, capacities and changed-source adoption races remain pending. Local links/anchors and 105 existing normative IDs resolve, protected normative/provenance files remain unchanged and diff whitespace checks pass. These are documentation checks, not runtime evidence or scope readiness.

Round-nine verification: Decision-to-Document Traceability maps CG03-Q41–Q45 to Product §3.1/3.3, Architecture §5.2, Acceptance §4.1–4.2, the planned evidence/resumes-grounding scopes and SL-02.M1. Cross-Document Semantic Consistency review confirms distinct source/local whitespace, ordinary-space-only marks restrictions, canonical mark ordering/container-local merge, the five capacity limits and current-at-commit replacement-source checks without restricting unchanged historical bindings. Independent read-only review found no semantic mismatches; broader Unicode-whitespace handling and pre-merge validation order remain explicitly unresolved. Local links/anchors, the 105 existing normative IDs and diff whitespace checks pass; protected normative/provenance files are unchanged. No runtime tests, new normative IDs, readiness claims or implementation are introduced.

Round-ten verification: CG03-Q46–Q50 maps fixed-set whitespace and raw-validity-before-merge to Product §3.3/Architecture §5.2/Acceptance §4.1; permanent Item-owned kind and typed version business content to Product §3.1/Architecture §3.1/5.1/Acceptance §4.1–4.2; initial empty Profile to Product §3.1/3.3, Architecture §5.1 and Acceptance §4.1. Profile/evidence/Resume scope planning, SL-02.M1 and the current traceability frontier agree. Kind projection is not a second Version authority; Profile initialization introduces neither automatic Resume creation nor baseline initialization and does not alter Preferences lazy creation. Local links/anchors, 105 existing normative IDs and diff whitespace checks pass; protected normative/provenance files remain unchanged. Complete object/command schemas and Storage evolution remain pending; no runtime proof or readiness is claimed.

Round-eleven verification: Decision-to-Document Traceability maps CG03-Q51–Q55 saved-object fields and lifecycle boundaries to Product §3.1/3.3–3.4, Architecture §3.1/5.1–5.3, Acceptance §4.1–4.2 and the owning planned Contract/Slice scopes. Author comparison checked the accepted field lists; independent read-only review checked cross-document semantics. Evidence/Baseline exclusively owns the current-baseline pointer; current owners no longer mandate Workspace placement. Only accepted initial Profile revision/schema values are frozen; ID generation, publication/no-op timing and restore operations are not inferred. Local links/anchors, 105 existing normative IDs and diff whitespace checks pass; protected normative/provenance files are unchanged. Full ResumeVersion/command/storage scope remains Pending, with no implementation or runtime proof.

Round-twelve verification: CG03-Q56–Q60 maps identities to Architecture §3.2, publication/no-op/timestamps to Product §3.2 and Architecture §5.2, and the Resume envelope/Profile freshness to Product §3.3/Architecture §5.2, with future proof in Acceptance §4.1–4.2. Author traceability and independent read-only semantic review confirm that only advancing objects contribute old timestamps, unchanged historical Profile refs remain exempt from current-only checks, and neither Header nor another ResumeVersion field copies contact values. All-root revision initialization, fresh A→B→A identities and unchanged no-op state agree across owners; lifecycle repeats and receipt replay remain pending. Local links/anchors, 105 normative IDs and diff whitespace checks pass; protected normative/provenance files remain unchanged. No implementation, new normative IDs or scope readiness is claimed.

Round-thirteen verification: CG03-Q61–Q65 maps the exact document settings and local-run aggregate limits to Product §3.3/Architecture §5.2/Acceptance §4.1; single-Item/full-replacement commands to Product §3.2/Architecture §5.2/Acceptance §4.1 and SL-02/SL-04 planning; one-way lifecycle with historical reads/repeat no-op to Product §3.4/Architecture §5.3/Acceptance §4.2. Independent read-only review confirmed user-specified fonts/point ranges/full line-box semantics and did not infer a line-spacing step. Current owners distinguish history reads from prohibited edits and do not promise batch rollback through separate commits. Local links/anchors, 105 existing normative IDs and diff whitespace checks pass; protected normative/provenance files remain unchanged. Residual scalar/read/HTTP/default/idempotency/storage interfaces and raw budgets remain Pending; no runtime proof, implementation or readiness is claimed.

Round-fourteen verification: Decision-to-Document Traceability maps CG03-Q66 scalar/Color Picker admission to P3.3/A5.2/V4.1; Q67 routes, Q68 all-mutation success receipts and Q69 per-Item Baseline concurrency to P3.2/A5.2/V4.1 and planned owner interfaces; Q70 confirmed adjacent replacement to P3.4/A5.3/V4.2 and Workspace/Resume/Save planning. Independent read-only semantic review found no actionable mismatch. Canonical list order, default concurrency representation, receipt namespace/retention/fingerprint and complete validation precedence remain open; Q64 repeated-removal no-op and historical readability survive. The earlier manual-replacement recommendation is not treated as accepted history. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The checker reports 105 existing normative requirements and git diff --check passes. No new normative IDs, implementation, runtime proof or scope readiness is claimed.

Round-fifteen verification: Decision-to-Document Traceability maps CG03-Q71/Q72 stable ACTIVE ordering and small revisioned default selection to P3.4/A5.3/V4.2; Q73/Q74 scoped lifetime receipts and pure-admission/replay/state-check precedence to P3.2/A5.2/V4.1; Q75 consistent current pairs and inactive-root reads to A5.2/V4.1–4.2. Independent read-only review found no actionable mismatch and confirmed that neither a heavyweight Workspace aggregate/configuration framework nor universal idempotency framework was introduced. Full remove/default preconditions, exact-history projections and raw caps remain pending. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The Contract checker reports 105 existing normative requirements and diff whitespace checks pass. No implementation, runtime proof, new normative IDs or readiness claim is introduced.

Round-sixteen verification: Decision-to-Document Traceability maps CG03-Q76/Q77 two-token removal/no-op and full list/selection snapshots to P3.4/A5.3/V4.2; Q78 retained exact readers to A5.2/V4.1–4.2; Q79/Q80 strict S2 transport and pre-canonicalization limits to A5.2/V4.1 and planned shared/HTTP owners. Independent read-only review found no actionable mismatch, confirmed that removed-root no-op bypasses only later state checks, and checked exact byte conversions/node/depth counting. Resume-count capacity and a separate structural-complexity code remain open; prior normative bodies are unchanged. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The checker reports 105 existing normative requirements and diff whitespace checks pass. No implementation, runtime proof, new normative IDs or scope readiness is claimed.

Round-seventeen verification: Decision-to-Document Traceability maps CG03-Q81 capacity and Q84 concurrent first creation to P3.4/A5.3/V4.2; Q82/Q83 complexity and submitted-index error paths to A5.2/V4.1; Q84/Q85 complete requests and frozen successful results to P3.2/A5.2/V4.1 and planned candidate-save/storage. Independent read-only review confirmed the accepted semantics and identified one stale pending-request/result sentence in Architecture, which was narrowed to the remaining interfaces. Rename/root, no-op Baseline and default-selection replay preserve command-time values without creating another authority; exact receipt fields/fingerprints remain pending. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The checker reports 105 existing normative requirements and diff whitespace checks pass. No implementation, runtime proof, new normative IDs or scope readiness is claimed.

Round-eighteen verification: Decision-to-Document Traceability maps CG03-Q86/Q87 receipt/typed tuple encoding and Q88 pure Evidence schema admission to A5.2/V4.1; Q89 lifecycle/reference errors to A5.2–5.3/V4.1–4.2; Q90 original-request recovery to P3.2/A5.2/V4.1 and planned candidate-save/storage/Common scopes. Independent read-only review found no actionable mismatch, checked the one-LF prefix/fixed a3 tuple/boolean and negative-zero rules, and confirmed that codec completeness does not widen command field admission. Historical result snapshots and retained-source/no-op exceptions remain intact; physical storage/final admission and actual Evidence-list/material consumers remain open. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The checker reports 105 existing normative requirements and diff whitespace checks pass. No implementation, runtime proof, new normative IDs or scope readiness is claimed.

Round-nineteen verification: Decision-to-Document Traceability maps CG03-Q91/Q92 list/current projection and ACTIVE capacity to P3.1/A5.2/V4.1; Q93/Q94 schema evolution and relational/JSON boundaries to A13/V4.1/V10; Q95 milestone-scope supersession to P3.5/A5.4/A16.3/V4.3 and global/SL-02/SL-04/SL-07/SL-10 plans, Contract Structure and scope-readiness records. Independent read-only review found the accepted semantics consistent; two stale Acceptance references to still-unfrozen request/result and receipt representations were corrected to the remaining normative/implementation proof. Actual demanded intent retains atomic Save ownership when M2 introduces its consumer; no speculative M1 intent gate remains. All 21 cumulative edited documents pass local link/anchor checks; 21 protected historical/normative files and 24 milestone IDs remain unchanged. The Contract checker reports 105 existing normative requirements and diff whitespace checks pass. No migration, implementation, runtime proof, new normative IDs or scope readiness is claimed.

Round-twenty verification: Decision-to-Document Traceability maps CG03-Q96/Q97 access and field admission to A5.2/V4.1, enduring Common vocabulary ownership to A16.1 and Contract Structure, Q98 authoritative-kind schema selection to P3.2/A5.2/V4.1 and Evidence/candidate-save planning, and Q99/Q100 receipt races/integrity to P3.2/A5.2/A13/V4.1/V10. Independent read-only review confirmed these accepted semantics and identified stale Acceptance pure-admission wording and a missing Pending frontier entry; both were corrected. Q88 is explicitly superseded and Q74/Q89 scoped without changing retained historical replay or moving mutable checks before receipt. The user subsequently accepted missing-target 404 before receipt even for a previously used key; this narrow Q98 exception is reconciled across current owners. Local links/anchors, protected historical/normative hashes, 24 milestone IDs, 105 existing requirement IDs and diff whitespace checks pass. No new normative IDs, runtime proof, implementation, commit or readiness is claimed.

Normative publication verification: after explicit user authorization, the eight consumed owners publish 73 new stable requirements under 2026-09-21.S2M1-r1, for 178 total. The per-batch effective-decision mapping and owner/consumer semantic review are recorded in Progress §6.3. Profile/Evidence/Resume/Materials and Common/Workspace/Save/Storage were independently reviewed; first-inclusion initialization strength, explicit set-default receipt precedence and schema3 startup applicability were corrected. Shared documents preserve their published prefixes and the prior Entry/Preferences bodies remain unchanged. No consumed semantic question remains open. Backend-first handoff is available; no S2 implementation, runtime proof, migration or commit is claimed.
