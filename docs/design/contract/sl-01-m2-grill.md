# SL-01.M2 Contract Grill Decision Register

> English is authoritative. This register records conclusions and the open decision tree, not question transcripts or unaccepted recommendations. It is not a normative Contract, a readiness declaration or implementation evidence.

[Contract design navigation](README.md) · [Milestone plan](../../plans/slices/sl-01-workspace-jobs-preferences.md#sl-01m2-collection-preferences-and-immutable-versions) · [Contract Structure](../../contracts/structure.md) · [Scope readiness ledger](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

## Purpose and Authority

Maintain one working decision record for SL-01.M2. Record accepted conclusions, rationale, precise scope, supersession and formal writeback destinations here; do not create per-module decision files. Product and Architecture own behavior and responsibilities, Contracts own detailed norms, the Implementation Plan owns delivery scope, Acceptance owns proof, and Progress owns actual readiness and evidence.

Use `CG02-Qn` for this milestone's interview decisions, independently of `CG01` and the original Architecture Q/S locators. These are decision locators, not normative requirement IDs. Preserve the original design sources and historical handoffs. Reuse Common conventions; do not copy M1-only schemas or limits into M2 without an actual consumer decision.

## Current Baseline and Precedence

[CG02-BC1](#cg02-bc1) and [CG02-S1](#cg02-s1) control over conflicting earlier decisions. Preferences express future acquisition intent; Collection consumes an exact immutable PreferenceSetVersion; Job Pool view filters independently query saved Jobs. Current Preferences are not a continuing Job eligibility gate. SL-01.M2 delivers configuration/version/read/save/concurrency, not QuickScreen.

All six dimensions require an explicit legal user choice and successful Save before configured status. A dimension may permit an explicit no-constraint choice under its own Contract; missing/unfilled values and an all-empty object cannot silently express unrestricted configuration. Keywords require at least one valid term; the other five dimensions permit an explicit UNLIMITED choice, mutually exclusive with concrete effective values. Q16–Q20 settle dimension representations; Q26–Q30 settle the HTTP operations, success objects and publication times. Work mode remains deferred.

The single global authority, revision-first Save, canonical no-op, frozen collection inputs, no implicit collection restart, retained saved Jobs, no Candidate/Requirement-based acquisition screening and independent ManualApplicationEntry remain effective. UI implementation still waits for UI design. M1's published Contracts and backend are unaffected.

## Q6 Rewrite Plan

1. Record CG02-Q6–Q10, CG02-BC1 and CG02-S1; mark the replaced portions of Q1/Q2/Q3/Q5 explicitly. The unaccepted title-keyword recommendation is rejected, not invented as a previously accepted decision.
2. Rewrite Product/Architecture around future acquisition intent, source planning/admission, and independent Job Pool queries. Remove current-Preference re-screening and downstream QuickScreen gates while retaining real Job/source/dependency/permission eligibility.
3. Narrow SL-01.M2 to complete explicit configuration, immutable versions, Save/read/concurrency and persistence. SL-08.M2 owns the real source consumer and admission integration. Keep 12 Slices and 24 milestone IDs.
4. Reconcile Contract Structure/catalog/consumer mapping, Acceptance, current traceability and navigation. Keep jobs-screening as the formal Job/admission/local-query definition destination and collection as source workflow/mapping owner; no new parallel query authority document.
5. Check residual obsolete gates, Markdown references, stable normative IDs, source preservation and Pending readiness. Do not create code, frontend or prematurely complete field schemas, enum catalogs, migration or source mappings.

**Execution status:** Completed for the accepted architecture/scope revision. Read-only cross-document review found no surviving current-Preference gate or active versioning-deferral/empty-PASS rule. Clarifications scoped the M1 navigation label and retained mandatory metadata-supported admission checks. Mechanical checks confirmed resolved local Markdown links, unchanged 69 published M1 requirement IDs, four Ready/63 Pending scope rows, 12 Slices/24 milestone IDs and 28 Contract destinations. Original sources, M1 norms/runtime and unrelated API documentation were compared with the incoming snapshot. This is writeback evidence, not normative M2 readiness or runtime acceptance.

## Writeback Destinations

| Owner | Current responsibility |
| --- | --- |
| `docs/contracts/candidate/preferences.md` | Six-dimensional future collection intent; explicit configuration; immutable PreferenceSetVersion; canonical Save/read/concurrency |
| `docs/contracts/jobs/collection.md` | Exact-version source query/admission mapping, workflow and adapter behavior at SL-08.M2 |
| `docs/contracts/jobs/jobs-screening.md` | Formal Job authority/admission and independent local Job Pool query semantics at their actual consumers; no M2 QuickScreen |
| `docs/contracts/common.md` | Shared identity/immutable-reference conventions, error representation/vocabulary and the small M2 nested-path grammar; preserve M1 error behavior |
| `docs/contracts/foundation/storage.md` | Atomic Preference version/current/revision persistence, retained exact references and explicit evolution from M1 storage |
| Plans, Acceptance and Progress | Revised scope/dependencies, proof, traceability and actual readiness under their existing owners |

The published M1 STO-003/005/006/011 rules still apply to M1 storage. Q39 accepts explicit offline evolution from schema 1 to schema 2 and fresh schema-2 initialization; new consumed Storage clauses must express that scope without silently upgrading, replacing an existing database or weakening Entry guarantees. Existing M1 binaries are not promised schema-2 compatibility.

## Session State

- Current milestone: **SL-01.M2 — Collection Preferences and immutable versions**.
- Last answered batch: **CG02-Q36–Q40**, accepted with Q38/Q40 corrections: binary fingerprint, six-field receipts, business configuration independent of JSON serialization, explicit schema evolution and precise error mapping.
- Current controlling architecture revision: **CG02-BC1**.
- Current batch: none. The accepted decision frontier is closed through Q40; no unanswered recommendation has been adopted.
- Current normative readiness: the four consumed M2 scopes are Ready at 2026-09-20.M2-r1 under the actual bodies and Progress 6.2 review. This register is still provenance, not normative authority or implementation evidence.
- Next activity: backend implementation using the M2 handoff and actual normative IDs. UI implementation waits for UI design; no new Grill round is needed unless a concrete new conflict is discovered.

## Accepted Dimension Inventory

| Dimension | Accepted expression | Still open |
| --- | --- | --- |
| Target job keywords | `target_job_keywords`: nonempty string array, at most 20 unique terms, each 1–100 code points after fixed trim; no UNLIMITED | Source query composition stays Collection work |
| Work cities | `accepted_cities`: UNLIMITED or LIMITED with 1–50 unique city strings, each 1–100 code points after fixed trim | Source city mapping/ambiguity stays Collection work |
| Salary | `minimum_salary`: UNLIMITED or LIMITED with exact JSON integer value in [1, 300000], CNY pre-tax monthly base salary | No remaining dimension decision; source consumption stays Collection work |
| Recruitment types | `recruitment_types`: UNLIMITED or LIMITED with 1–4 unique enum members, canonical order CAMPUS, INTERNSHIP, EXPERIENCED, PART_TIME | Source mapping/overlap stays Collection work |
| Excluded companies | `excluded_companies`: UNLIMITED or LIMITED with 1–200 unique names, each 1–200 code points after fixed trim | Source name mapping stays Collection work |
| Required education ceiling | `max_required_education`: UNLIMITED or LIMITED with one member of the six-level ordered education enum | Source qualification mapping/ambiguity stays Collection work |

`job_search_keywords` is a retired proposed canonical name under CG02-Q12; acquisition semantics remain unchanged. `minimum_monthly_base_salary_cny` was not adopted. Value types, no-constraint encodings and limits are defined by CG02-Q16–Q20, not inferred from the short field names.

## Accepted Identity and Publication Inventory

| Object | Field | Adopted role/type |
| --- | --- | --- |
| PreferenceSet | `preference_set_id` | System-generated stable UuidV4 |
| PreferenceSet | `current_preference_set_version_id` | Explicit reference to the current immutable version |
| PreferenceSet | `revision` | Common Revision; initial 1, +1 per real changed publication; no-op unchanged |
| PreferenceSet | `created_at` | System-generated Common UTC timestamp |
| PreferenceSet | `updated_at` | System-generated Common UTC timestamp; no-op unchanged |
| PreferenceSetVersion | `preference_set_version_id` | System-generated immutable-version UuidV4 |
| PreferenceSetVersion | `preference_set_id` | Reference to the owning stable root |
| PreferenceSetVersion | `created_at` | System-generated Common UTC timestamp |
| PreferenceSetVersion | `configuration` | Complete object with exactly the six accepted dimension fields; shared configuration definition |

No `is_current` field is stored on an immutable version. Root and first version are created together only by the first complete valid successful Save; root absence means initial configuration has not completed. CG02-Q21 adopts these as the complete root/version business object fields; Q26–Q30 settle HTTP envelopes and publication time behavior, and Q37–Q39 settle the receipt fields and storage representation/evolution direction. Root does not duplicate configuration; versions have no updated_at or revision. UUIDv4 has no temporal ordering semantics; M2 adds no historical sequence field or strict historical ordering guarantee.

## Round 1 — Scope, Configuration State, Save and Screening

<a id="cg02-q1"></a>

### CG02-Q1 — Five hard-preference dimensions

- **Status:** `PARTIALLY SUPERSEDED` by CG02-Q6/Q9/BC1/S1: six collection-intent dimensions now apply; work-mode deferral survives.
- **Decision:** First release supports role directions, work cities, salary requirements, recruitment type and company blacklist. Work mode is `DEFERRED` because a stable consumable source representation has not been established. This freezes dimension scope only, not matching, normalization, salary calculation or company identity logic.
- **Rationale and provenance:** The user reports source research using [BossHunter](https://github.com/shengjidaguai-china/BossHunter) and [boss-zhipin-scraper](https://github.com/eatmoreduck/boss-zhipin-scraper). This records the user's rationale, not certification of current live BOSS behavior or a pinned adapter mapping. Recruitment-type meaning still needs an explicit decision.
- **Formal writeback:** Product 4.2 and Architecture 4.2; detailed representation remains pending in Preferences and Jobs-screening.

<a id="cg02-q2"></a>

### CG02-Q2 — Configuration state independent of version history

- **Status:** `SUPERSEDED` by CG02-BC1 and CG02-S1. The historical decision below is not the current versioning or initialization rule.
- **Decision:** Distinguish never-configured Preferences from a successful explicit Save with no restrictions. Do not silently create a configured default. M2 does not require PreferenceSetVersion as the only representation. Whether immutable history/version objects are needed is deferred to a real lineage consumer; this decision does not forbid later versioning or settle the persistence schema.
- **Scoped supersession:** Replaces the mandatory PreferenceSetVersion/current-version-pointer and change-creates-history representation in Q45/Q55/Q56 and the corresponding representation assumptions in Q49/Q161. The single global authority, hard intent, concurrency, deterministic inputs, frozen collection versus current filtering, and exclusion of ScreeningProfileSnapshot remain effective. Formal Job/JobVersion and other immutable authorities are unaffected.
- **Formal writeback:** Product 4.2–4.3, Architecture 3.1/4.2, Contract Structure, SL-01.M2, Acceptance 3 and the current scope ledger. Original architecture records, Inventory and historical handoffs remain preserved.

<a id="cg02-q3"></a>

### CG02-Q3 — Explicit whole-configuration Save and canonical no-op

- **Status:** `PARTIALLY SUPERSEDED`: explicit Save, canonical equality and revision-preserving no-op survive. CG02-BC1/S1 replace the non-versioned-state option with complete immutable Preference versions for real changes.
- **Decision:** Editing is not authority. Successful explicit Save publishes the effective Preference state. Determine content equality using the Preference Contract's canonical comparison, never frontend dirty-state comparison. Equal content under that comparison is a successful no-op with no revision increment and no new history. A real change publishes new effective state; CG02-Q2 means this does not mandate an immutable version object.
- **Open detail:** Array ordering, unset/empty equivalence, trim and domain-specific name normalization. Their answers must agree across Save, persistence and screening.
- **Formal writeback:** Preferences Save/comparison clauses remain to be authored with the actual representation.

<a id="cg02-q4"></a>

### CG02-Q4 — Revision admission precedes no-op comparison

- **Status:** `ACCEPTED`
- **Decision:** Ordinary Save validates the caller's expected revision before content equality. A stale revision conflicts even when submitted content equals current content; no last-writer-wins, automatic merge or overwrite. Same-request uncertain-outcome recovery is a separate unresolved protocol, not implicitly settled by this rule.
- **Formal writeback:** Preferences command/atomic admission and applicable Storage scope remain pending.

<a id="cg02-q5"></a>

### CG02-Q5 — Complete screening explanations and unconfigured exclusion

- **Status:** `PARTIALLY SUPERSEDED` by CG02-BC1/S1. No M2 or continuing formal-Job QuickScreen/result contract remains; the all-empty unrestricted state and its PASS meaning are retired. Configuration distinction and truthful uncertainty survive only within the newly assigned owners; future admission result representation remains open.
- **Decision:** For configured Preferences, evaluate every configured dimension and retain each result/reason. Any definite conflict yields REJECT; otherwise any undecidable configured dimension yields UNCERTAIN; otherwise PASS. A saved unrestricted configuration yields PASS without claiming career suitability. Unconfigured Preferences must not be presented as completed screening or conflated with missing source metadata.
- **Distinct situations:** `NO_PREFERENCES_CONFIGURED` versus `PREFERENCES_CONFIGURED_BUT_NO_RESTRICTIONS`. Their response placement/type and the invocation admission shape remain open; they are not assumed to be additional QuickScreen outcome enum members.
- **Boundary:** Explainable return values do not authorize durable storage of rejected source content. Formal Collection access/admission remains a later consumer obligation.
- **Formal writeback:** Product/Architecture screening meaning and Acceptance scenarios; exact Jobs-screening input/output and errors remain pending.

## Round 2 — Acquisition Intent and Boundary Revision

<a id="cg02-bc1"></a>

### CG02-BC1 — Preferences, Collection and Job Pool queries are distinct

- **Status:** `ACCEPTED`
- **Decision:** Preferences are durable user intent for future Collection. Collection consumes one exact immutable PreferenceSetVersion and owns source query/admission mapping with the formal Job admission owner. Once admitted, Jobs are not continually eligible/ineligible under current Preferences. JobPoolViewFilter is independent browsing/query state, not an authority object or fixed payload selected here.
- **Effects:** Preference changes affect future Collection only; no retrospective removal, preference-conflict marker, implicit view exclusion or history rewrite for saved Jobs. Active collection retains its original exact version, and explicit stop still preserves saved results without restart. View filters do not Save Preferences, create versions, change future Collection, delete/mutate Jobs or produce QuickScreenResult.
- **Scope:** Remove the pure QuickScreen component and its Contract requirement from SL-01.M2. M2 delivers configuration, immutable version semantics, read/Save/concurrency and storage. SL-08.M2 implements source projection and necessary deterministic candidate admission. This is a responsibility transfer, not deletion of safeguards for actual Collection.
- **Single owners:** preferences defines user intent; collection defines source consumption; jobs-screening retains formal Job identity/admission/local-query semantics. Source pushdown versus local admission, query count/concurrency/deduplication and platform taxonomy are not Preferences ownership. No new JobPoolViewFilter document or Company entity is implied.
- **Supersedes:** Q45/Q55/Q56/Q161 and related Q49/Q110 clauses only where they impose current-Preference re-screening, persistent QuickScreen authority/results or a downstream QuickScreen eligibility gate. CG02-Q2's versioning deferral and CG02-Q5's M2 screening/result architecture are replaced. Frozen-run identity, complete formal Job admission, no rejected-content store, resource/safety permissions and original exact Job history survive.
- **Rationale:** Future acquisition intent cannot retroactively redefine why an already-saved Job exists. A pure component without a current consumer is not retained solely for the old plan.
- **Formal writeback:** Product/Architecture, global and SL-01/08 plans, Contract Structure, Acceptance, active traceability and navigation. Original Q/S records and historical handoffs remain source-time evidence.

<a id="cg02-q6"></a>

### CG02-Q6 — User-owned collection search terms

- **Status:** `PARTIALLY SUPERSEDED` by CG02-Q12 for the canonical name only: use `target_job_keywords`. Acquisition meaning and all owner boundaries remain accepted.
- **Decision:** Canonical field name `job_search_keywords`. Values express terms around which future Collection should search; they are neither semantic job-category IDs nor a literal title eligibility predicate. A source result such as Java developer returned for a backend search is not rejected solely for lacking the original term in its title.
- **Exclusions:** First release does not automatically expand user terms into synonyms or model-generated terms. Keyword composition/OR behavior, query count, deduplication, normalization and source encoding are not frozen here. Any later semantic query expansion is a separate enhancement.
- **Supersession:** Rejects the unadopted title-keyword recommendation. Architectural consequences are defined in CG02-BC1 rather than silently changing Q5.
- **Formal writeback:** Preferences planned scope and Product acquisition meaning; actual source consumption remains collection-owned.

<a id="cg02-q7"></a>

### CG02-Q7 — City-level acquisition intent

- **Status:** `ACCEPTED`
- **Decision:** Accepted work locations are city-level alternatives, without inferred neighbouring cities, districts, business areas or commute-distance rules. Ambiguous/missing source city is not guessed. City identity, names, codes and aliases remain to be defined; source search codes are not automatically Domain identity.
- **Owner split:** Preferences expresses the acceptable cities; Collection handles source projection and candidate admission. Existing Job Pool city filters are independent queries.

<a id="cg02-q8"></a>

### CG02-Q8 — Salary intent and future admission policy

- **Status:** `ACCEPTED`
- **Decision:** Salary intent is a minimum CNY pre-tax monthly base salary. Do not automatically convert annual/day rates or include bonuses, equity or extra salary months. Amount representation and explicit no-limit choice remain open.
- **Future Collection admission decision:** For a comparable interval, lower bound at/above the threshold satisfies it; upper bound below it conflicts; an interval spanning the threshold is uncertain. Missing, negotiated or incomparable pay stays uncertain. With a 15,000 threshold: 16,000–20,000 satisfies; 10,000–14,000 conflicts; 12,000–18,000 is uncertain. These examples select no user default.
- **Ownership:** The interval comparison is deferred to the Collection/Job admission policy's normative scope, not a Preferences predicate or M2 QuickScreen implementation. Source amount extraction remains adapter work.

<a id="cg02-q9"></a>

### CG02-Q9 — Acquisition job types and required-education ceiling

- **Status:** `ACCEPTED`
- **Decision:** Multi-select acquisition job types are `CAMPUS`, `INTERNSHIP`, `EXPERIENCED`, `PART_TIME`. They are user-facing acquisition categories, not a claim of one mutually exclusive source field. Unrestricted is not a persisted enum member; its explicit representation remains open under CG02-S1. Mapping/query/source classification and necessary deterministic admission belong to Collection/adapters.
- **Additional dimension:** `max_required_education` expresses the maximum education requirement acceptable on a Job, not the Candidate's own highest education. `MASTER` means master's degree and below. Full enum/order, missing or ambiguous source interpretation and explicit unrestricted representation remain open.
- **Supersession:** Extends CG02-Q1 from five to six dimensions. Replaces the unadopted recommendation to restrict recruitment type to campus/experienced only. Work mode remains deferred.

<a id="cg02-q10"></a>

### CG02-Q10 — Explicit company-name exclusions

- **Status:** `ACCEPTED`
- **Decision:** Company exclusions use full equality of source display names after the normalization still to be defined. No implicit substring/fuzzy match, legal-suffix stripping or group/affiliate expansion. Users may explicitly name multiple aliases. Missing source company is uncertain rather than guessed.
- **Ownership:** Preferences records exclusions; Collection applies candidate admission. No Company authority, Job Pool filtering side effect or automatic change to saved Jobs is introduced.

<a id="cg02-s1"></a>

### CG02-S1 — Complete explicit configuration and immutable publication

- **Status:** `ACCEPTED`, refined by CG02-Q11/Q15: five dimensions permit explicit UNLIMITED, keywords require values, and first publication uses lazy atomic root/version creation.
- **Decision:** Every one of the six dimensions requires a legal explicit user selection before successful Save establishes configured Preferences. Incomplete configuration cannot start formal acquisition. Missing/unfilled values and an all-empty object are not an accepted unrestricted version. A legal explicit no-constraint/no-exclusion choice is allowed only as defined for that dimension; city and recruitment type permit such a choice, while the remaining exact options/encodings still require Grill.
- **Publication:** Collection consumes a complete user-confirmed immutable PreferenceSetVersion. Real canonical changes create a new version; the accepted revision-first and canonical no-op rules remain effective. No-op creates neither a version nor a revision increment. Initial representation, atomic root/current/version structure, history retention and retry behavior remain open.
- **Supersedes:** CG02-Q2's saved-empty/unrestricted and versioning-deferral design, the corresponding CG02-Q3 wording, and CG02-Q5's all-empty PASS scenario. It preserves the distinction between unfinished configuration and an explicit unrestricted choice; it does not reintroduce QuickScreen or impose a personal default.

## Round 3 — Explicit Inputs, Canonical Fields and Lazy Publication

<a id="cg02-q11"></a>

### CG02-Q11 — Six explicit inputs and mutually exclusive no-constraint choices

- **Status:** `ACCEPTED`
- **Decision:** All six dimensions require explicit valid choices before a complete Save can configure Preferences and authorize future Collection. Keywords require at least one valid term and have no UNLIMITED option. Cities, salary, recruitment types, company exclusions and required-education ceiling each offer an independent explicit UNLIMITED checkbox; exclusions interpret it as excluding no companies. Missing/unfilled/blank/empty input is not an implicit unrestricted choice.
- **UI obligation:** Keyword/city/company entry uses one text value plus Add and removable Chips/Tags, not comma-delimited strings. Salary uses a single decimal integer input in CNY/month. Recruitment types use multi-select buttons. Education is a single-select upper-bound dropdown. UNLIMITED disables the associated controls; optional restoration of unsaved local draft values remains frontend implementation choice. This records future UI requirements, not permission to implement UI now.
- **Authority:** UNLIMITED and concrete values cannot both be effective in a successfully saved dimension. Backend validation is authoritative and applies to the complete Save; any invalid field rejects it atomically without a new version. Structured field_errors identify the affected area; optional element/Chip location requires its later error representation and does not silently extend COM-029.
- **Salary input:** The frontend accepts ordinary decimal integer input, rejecting k notation, commas, currency signs, fractions and ranges. CG02-Q17 subsequently fixes [1, 300000] and exact JSON integer-value semantics at the backend; the UI writing restriction is not a raw-number lexical restriction on HTTP input.
- **Formal writeback:** Product interaction/validation constraints; Preferences detailed choice/value and error representation remains pending.

<a id="cg02-q12"></a>

### CG02-Q12 — Canonical dimension names and concise UI labels

- **Status:** `ACCEPTED`
- **Decision:** Use `target_job_keywords`, `accepted_cities`, `minimum_salary`, `recruitment_types`, `excluded_companies`, `max_required_education`. `minimum_salary`'s normative description fixes CNY pre-tax monthly base salary; units are not guessed from the field's shorter name. `max_required_education` remains explicitly Job-facing, not Candidate highest education.
- **Scoped supersession:** `target_job_keywords` replaces CG02-Q6's `job_search_keywords` name while preserving its meaning. The recommended `minimum_monthly_base_salary_cny` name was not adopted. No duplicate names or API aliases are introduced.
- **UI clarification:** Concise labels may use Target job keywords, Minimum salary and Highest education, with visible helper text/tooltip explaining monthly base salary and Job-required-education ceiling. Labels do not change canonical meaning; the earlier longer education-label recommendation is refined, not a new Candidate field.

<a id="cg02-q13"></a>

### CG02-Q13 — Unordered multivalue intent and canonical equality

- **Status:** `ACCEPTED`
- **Decision:** Concrete keyword/city/recruitment-type/company collections are unordered sets with no priority. Backend applies each field's agreed normalization, removes equivalent duplicates and produces deterministic canonical ordering. Valid inputs differing only in ordering or duplicate occurrences are a canonical no-op and create no version or revision increment. Frontend duplicate prevention is not the only enforcement point.
- **Boundary:** Save canonicalization does not select source query OR/composition, execution order or acquired-result deduplication. Exact comparison/sort rules and validation-limit interaction remain open.

<a id="cg02-q14"></a>

### CG02-Q14 — Exact search-term normalization

- **Status:** `ACCEPTED`
- **Decision:** Search terms use Common's fixed outer-whitespace trim and legal Unicode scalar text. Reject blank-after-trim and forbidden controls/line separators; terms are single-line. Do not case-fold, normalize Unicode/width, merge internal whitespace or substitute synonyms. After trim, Java and java, different internal spacing, and full-/half-width characters remain distinct terms. Source interpretation does not redefine saved Preference equality.
- **Remaining detail:** Item length/count and deterministic ordering; city/company normalization are separately owned field decisions.

<a id="cg02-q15"></a>

### CG02-Q15 — Stable identity and lazy atomic first publication

- **Status:** `ACCEPTED`
- **Decision:** Adopt the root/version identity fields in the inventory, system-generated Common UuidV4 identities and Common Revision on the root. The current pointer lives on PreferenceSet; immutable versions do not store is_current.
- **Initialization:** Workspace initialization creates no Preference root. First complete valid successful Save creates root, first immutable version and current reference in one transaction. Failure leaves no empty root or partial initialization. Root absence means the user has not completed first Preferences configuration.
- **Remaining detail:** Exact first-save command/precondition/race behavior, initial revision, timestamps, complete response, retained history and retry protocol. This does not yet select a migration or weaken M1 storage recognition.

## Round 4 — Choice Representation, Numeric Semantics and Canonical Values

<a id="cg02-q16"></a>

### CG02-Q16 — Explicit discriminated choice objects

- **Status:** `ACCEPTED`
- **Decision:** Each of the five no-constraint-capable fields is exactly either `{"mode":"UNLIMITED"}` or `{"mode":"LIMITED","value":...}`. UNLIMITED forbids value, including null/empty values. LIMITED requires the field's valid concrete scalar or nonempty collection. Missing/unknown mode and extra fields reject; no inferred mode. Keywords remain a nonempty plain array.
- **Types:** LIMITED value is a string array for cities/companies, integer salary value, recruitment-type array or one education enum member, respectively. UNLIMITED is a choice mode and never a recruitment/education member. Complete configuration requires all six canonical fields.
- **Ownership:** Saved intent representation only; this creates no Collection query/admission behavior. Exact FieldError addressing remains open.

<a id="cg02-q17"></a>

### CG02-Q17 — Salary uses exact JSON integer-value semantics

- **Status:** `ACCEPTED`
- **Decision:** LIMITED salary is a JSON number whose exact mathematical value is an integer in the inclusive range [1, 300000]. Equivalent spellings such as 15000, 15000.0 and 1.5e4 are admitted; lexical exponent/decimal-point spelling alone is not a rejection. Strings, booleans, null, non-integral values and out-of-range values reject. Admission must not round an invalid precise fraction into an accepted integer. The frontend still restricts ordinary user input to integer form.
- **Supersession/clarification:** Rejects the unadopted Q17 raw-number lexical restriction and clarifies CG02-Q11's plain-digit rule as frontend input. The earlier suggested maximum is now adopted. Reuses Common's exact-integrality principle, not Revision's domain range; M1 Revision remains unchanged.
- **Canonical output:** Salary remains an integer value; output serialization and error details will be reconciled with the complete API boundary. Currency, tax and monthly-base meaning remain the field's normative description, not optional caller-controlled qualifiers.

<a id="cg02-q18"></a>

### CG02-Q18 — Six ordered required-education levels

- **Status:** `ACCEPTED`
- **Decision:** Ordered lowest to highest: JUNIOR_HIGH_OR_BELOW, UPPER_SECONDARY, ASSOCIATE, BACHELOR, MASTER, DOCTORATE. UPPER_SECONDARY groups high school and secondary vocational/technical school as one JobHunter level. An upper bound includes its own level and every lower level. UNLIMITED remains outside this enum.
- **Boundary:** This is deliberate Domain normalization of the source distinctions discussed in research, not a claim that source search codes form the same ordering. Unknown, unrestricted-source, foreign or complex qualification mapping belongs to future Collection admission. This is not a Candidate education record.

<a id="cg02-q19"></a>

### CG02-Q19 — City and company text preserves explicit names

- **Status:** `ACCEPTED`
- **Decision:** Use the same fixed Common outer trim and scalar/control/single-line legality boundary as accepted keyword text. Reject blank-after-trim, invalid Unicode and prohibited controls/line separators. Do not case-fold, normalize Unicode/width, merge internal spaces, strip city/legal suffixes, infer aliases or merge affiliates. 深圳 and 深圳市 therefore remain distinct saved terms. A comma is part of an explicitly added item, not a list separator.
- **Boundary:** Source translation/unsupported or ambiguous names remain Collection work; the adapter does not retroactively rewrite saved Preference equality.

<a id="cg02-q20"></a>

### CG02-Q20 — Collection bounds and deterministic ordering

- **Status:** `ACCEPTED`
- **Limits:** After deduplication, at most 20 keywords, 50 cities, 200 excluded companies and 4 recruitment types. Trimmed text item limits are 100 code points for keywords/cities and 200 for companies. Keywords and LIMITED collection values require at least one item. Invalid/excess input rejects rather than truncates.
- **Order of admission:** Validate every submitted item for type/scalar/character legality, trim and length; no invalid item is hidden by deduplication. Deduplicate by the field's canonical value, check resulting set capacity, then sort. Text sets sort lexicographically by Unicode code points, independent of locale. Recruitment types sort in their already-declared enum order: CAMPUS, INTERNSHIP, EXPERIENCED, PART_TIME, not lexical order.
- **Boundary:** Canonical ordering does not assign search priority or source execution order. Whole-request byte/raw-item transport budgets are separate unresolved boundary protections and are not silently selected by these canonical-count limits.

## Round 5 — Saved Objects, Publication, Replay and History

<a id="cg02-q21"></a>

### CG02-Q21 — Complete root and immutable-version objects

- **Status:** `ACCEPTED`
- **Decision:** PreferenceSet has preference_set_id, current_preference_set_version_id, revision, created_at and updated_at. PreferenceSetVersion has preference_set_version_id, preference_set_id, created_at and configuration. Configuration contains exactly the six canonical dimension fields and shares its definition with Save input. Root does not duplicate six-dimensional content; versions have no updated_at/revision/is_current.
- **Time ownership:** Timestamps are system-generated Common UTC representations, not caller-writable. Clock/publication timestamp selection and HTTP envelopes remain open.

<a id="cg02-q22"></a>

### CG02-Q22 — Revision publication and competing first saves

- **Status:** `ACCEPTED`
- **Decision:** First successful Save creates root/version/current atomically at revision 1. A subsequent real canonical change checks current revision, creates a new version, switches the pointer and increments revision by one. A canonical no-op changes neither version, revision nor modification time. At Common's maximum revision, a valid no-op succeeds while a real increment is rejected; never wrap or overflow.
- **Race:** Different first-save requests compete on root absence; only one creates the singleton. The loser receives a concurrent-configuration conflict even for identical content, not an automatic overwrite/no-op. Replay of the same logical request follows Q23 separately.

<a id="cg02-q23"></a>

### CG02-Q23 — Durable identity for logical Save retries

- **Status:** `ACCEPTED`
- **Decision:** Every logical Save carries a client-generated request_id. Persist enough successful outcome information in a receipt to recognize the same request across retries. Matching request ID, canonical configuration and concurrency precondition returns the original success; differing content or precondition under the same ID conflicts. After input admission, a known successful receipt is resolved before treating the request as an ordinary stale revision.
- **Effects:** Replay creates no new version, changes no revision and never switches current back to an older saved result. A new logical Save uses a new request ID. Known failed requests do not fabricate successful receipts. The replay result may identify a version no longer current; it is evidence of that request, not a fresh current-state read.
- **Open detail:** Request representation, deterministic fingerprint, exact success/result fields, receipt retention/storage, error precedence and uncertain-outcome recovery. Successful no-op also needs replay-consistent outcome handling without changing business state.

<a id="cg02-q24"></a>

### CG02-Q24 — Retained immutable Preference history

- **Status:** `ACCEPTED`
- **Decision:** Retain every successfully published complete PreferenceSetVersion for the Workspace lifetime, without automatic expiry or single-version deletion in v1. Only real changes add history; no-op does not. Exact content is retained, including former terms/exclusions, not replaced by a digest.
- **Boundary:** Reading history does not activate it. No rollback feature is introduced. Receipt retention is independently decided; version history alone does not prove the outcome of every Save request.

<a id="cg02-q25"></a>

### CG02-Q25 — Normal read of unconfigured Preferences

- **Status:** `ACCEPTED`
- **Decision:** Reading current Preferences before first successful Save is a normal successful result expressing NOT_CONFIGURED, not 404, corruption or an implicit default. Repeated reads create no root/version and mutate nothing. Configured reads return real current saved data. Exact endpoint/envelope is pending; lookup of a nonexistent exact version is a distinct later-defined case.

## Round 6 — HTTP Operations, Publication Time and Receipts

<a id="cg02-q26"></a>

### CG02-Q26 — Complete Save command and concurrency precondition

- **Status:** `ACCEPTED`
- **Decision:** POST /api/v1/preferences/save accepts exactly three required fields: client-generated Common UuidV4 request_id, revision, and complete six-dimensional configuration. Explicit revision null means the root must not exist; later saves require a positive Common Revision. Missing revision and zero are not first-save aliases. Root-present/null and root-absent/numeric combinations conflict, subject to successful-receipt replay precedence under Q23.
- **Boundary:** Caller cannot supply root/version IDs or timestamps. Save replaces the whole configuration; no partial PATCH is introduced.

<a id="cg02-q27"></a>

### CG02-Q27 — Current and exact-version reads

- **Status:** `ACCEPTED`
- **Decision:** GET /api/v1/preferences returns 200 with exactly status NOT_CONFIGURED when root is absent. Once configured, it returns status CONFIGURED, preference_set containing the complete root, and current_preference_set_version containing the complete referenced version. Root and version come from one consistent read; mixed snapshots are invalid.
- **Exact read:** GET /api/v1/preferences/versions/{preference_set_version_id} returns the complete immutable version with 200, or 404 when that exact version does not exist. It never substitutes current. No history-list, delete or restore endpoint is introduced.

<a id="cg02-q28"></a>

### CG02-Q28 — Replay-stable successful Save result

- **Status:** `ACCEPTED`
- **Decision:** Successful Save returns 200 and exactly preference_set_id, preference_set_version_id, revision and outcome. Outcome is CREATED for first publication, UPDATED for a real changed publication, or UNCHANGED for a canonical no-op. Result revision is the root revision at that successful Save.
- **Replay:** Return the original result for a matching successful request even if current subsequently advanced. This is a request outcome, not a fresh current read. A later current-read failure does not undo or reclassify the successful Save.

<a id="cg02-q29"></a>

### CG02-Q29 — Publication timestamps without historical total ordering

- **Status:** `ACCEPTED WITH CORRECTION`
- **Decision:** One real publication uses one system-generated Common UTC millisecond timestamp. First creation sets root.created_at, root.updated_at and version.created_at to that same time. Later changes use max(now, root.updated_at) for both the new version.created_at and root.updated_at; root.created_at remains unchanged. No-op and replay refresh no business timestamps.
- **Ordering boundary:** UUIDv4 carries no temporal order. M2 does not promise a strict total order of all historic versions from created_at or UUIDv4, including multiple publications within one millisecond or a clock rollback. Current pointer identifies only the current version; revision orders root modifications. No historical-list/sort consumer exists in M2, so no sequence field is added. A future strict-order consumer must explicitly introduce publication sequence/revision lineage.
- **Correction:** Rejects the prior recommendation's claim that version ID expresses version order. That claim was not an accepted rule and is not adopted into any normative Contract.

<a id="cg02-q30"></a>

### CG02-Q30 — Lifetime successful Save receipts

- **Status:** `ACCEPTED`
- **Decision:** Retain receipts for all successful Saves, including UNCHANGED, for the Workspace lifetime without automatic expiry or cleanup in v1. Persist a real publication and its success receipt in one transaction. A successful no-op persists its receipt without adding a version or changing root revision/timestamps.
- **Authority:** Store enough request identity and result information to recognize and reconstruct original success. The immutable version remains the sole owner of complete configuration content; receipts do not create another configuration authority. Known failed requests are not successful receipts. Exact fingerprint and storage representation remain open.

## Round 7 — Input Admission, Error Paths and Recovery

<a id="cg02-q31"></a>

### CG02-Q31 — Strict M2 request admission

- **Status:** `ACCEPTED WITH REFINEMENT`
- **Decision:** M2 JSON command bodies must actually be UTF-8. Accept application/json with compatible charset=utf-8 parameters using media-type parsing, not byte-for-byte header equality. Reject a non-identity Content-Encoding; absent encoding and identity are permitted. Malformed JSON, invalid body encoding and duplicate member names within one JSON object produce 400 BAD_REQUEST; never resolve duplicates by last-value-wins. Parseable inputs with invalid shape, types, fields or values produce 422 VALIDATION_ERROR.
- **Validation:** Reject unknown fields without stripping, missing required fields without defaults, and invalid types without coercion. Missing fields use REQUIRED; explicit null uses INVALID_TYPE except Save's explicitly nullable revision precondition. Preserve exact admitted JSON numeric-value semantics without lexical integer restrictions. Both GET endpoints accept neither body nor query parameters; exact-version path identity uses Common UuidV4.
- **Compatibility:** These are consumed M2 rules, not retroactive changes to M1 input behavior.

<a id="cg02-q32"></a>

### CG02-Q32 — Minimal nested field-error path grammar

- **Status:** `ACCEPTED WITH REFINEMENT`
- **Decision:** Reuse ContractError and the two-field FieldError object. M2 field locations use the small grammar below, not full JSONPath. Names denote only known canonical fields; array indices refer to the submitted array before deduplication/sorting.

```text
path    = "$" | segment ("." segment)*
segment = name ("[" index "]")?
name    = [a-z][a-z0-9_]*
index   = "0" | [1-9][0-9]*
```

- **Locations:** Examples are revision, configuration.minimum_salary.value and configuration.accepted_cities.value[1]. Missing fields use their expected path. Unknown fields use UNKNOWN_FIELD at the nearest known parent object (or $ at the document root), without echoing the supplied key. No wildcard, quoted-key, recursive-descent, slice or filter syntax exists.
- **Reporting:** Return at least one accurate field error on field validation failure; multiple errors are permitted without an ordering promise. Do not include submitted values, SQL or internal exceptions. Non-field-specific errors retain an empty field_errors array.
- **Shared ownership:** Common owns public error representation and the scoped path grammar. Preserve M1's top-level field paths; explicitly add the M2-consumed grammar during normative writeback rather than silently rewriting an existing requirement's core meaning.

<a id="cg02-q33"></a>

### CG02-Q33 — Uncertain Save result and explicit retry

- **Status:** `ACCEPTED`
- **Decision:** Timeout, connection loss, ambiguous write 5xx and responses that establish neither valid success nor definite rejection require verification. Keep the original logical request's request_id, precondition and complete configuration for explicit retry; do not silently allocate a new ID or replace its revision with current. A committed request replays its receipt; an uncommitted request still faces its original precondition.
- **Evidence:** Current content equality does not prove that request succeeded; different current content does not prove failure. A definite Contract 4xx rejects the current request but does not establish non-commit of an earlier uncertain request. STORAGE_UNAVAILABLE (503) requires confirmed non-commit; uncertain commit uses OUTCOME_UNKNOWN (503). OUTCOME_UNKNOWN is a command outcome, never PreferenceSet state. No durable browser retry queue or unsaved-draft crash recovery is introduced.

<a id="cg02-q34"></a>

### CG02-Q34 — Admission, replay and publication precedence

- **Status:** `ACCEPTED`
- **Decision:** Check request boundaries and fully validate/canonicalize input; resolve an existing successful request receipt next; matching canonical content/precondition replays original success and a mismatch conflicts. Without a receipt, check root-absence or current-revision precondition, then canonical equality, then atomically commit the corresponding creation/change/no-op outcome and receipt. Acknowledge success only after confirmed commit.
- **Concurrency:** Invalid inputs cannot bypass admission via a known request ID. A new stale request conflicts even for equal content. Concurrent same-ID requests cannot publish twice; matching requests converge on one original success. Database races/recovery do not relax this order or authorize hidden business-command reexecution.

<a id="cg02-q35"></a>

### CG02-Q35 — Bounded transport and raw arrays

- **Status:** `ACCEPTED`
- **Decision:** Save accepts at most 1,048,576 actual JSON body bytes, including whitespace and escape spelling; excess returns 413 REQUEST_TOO_LARGE. Each multivalue input array accepts at most 1,000 submitted items before deduplication; excess returns 422 VALIDATION_ERROR with OUT_OF_RANGE at that array. After these admission bounds, validate every item, deduplicate, check Q20 canonical capacities and sort. Never truncate or partially accept.
- **Scope:** Order/duplicate-only no-op semantics apply to requests that pass these input boundaries. These limits are not substitutes for canonical business-set capacities.
- **Cross-Contract ownership:** Common owns shared error representation/vocabulary, including REQUEST_TOO_LARGE and OUTCOME_UNKNOWN when added for M2 consumption. Preferences owns their operation-specific triggers and HTTP mappings, not a duplicate error structure. OUTCOME_UNKNOWN already has M1 Entry/Storage trigger semantics; promotion to shared vocabulary must preserve those consumers. This decision does not publish new normative IDs or rewrite existing M1 clauses yet.

## Round 8 — Fingerprints, Durable Representation and Schema Evolution

<a id="cg02-q36"></a>

### CG02-Q36 — Exact Save fingerprint bytes

- **Status:** `ACCEPTED`
- **Decision:** request_fingerprint is Common Sha256Hex of the binary concatenation below. Input has already passed authoritative validation and canonicalization. u32be is exactly four unsigned big-endian bytes; string lengths count UTF-8 bytes, not characters. Decimal revision text has no leading zero, exponent, sign or fraction; this canonical encoding does not restrict admitted JSON numeric spelling.

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

- **Value encoding:** LIMITED cities, recruitment types and excluded companies use A with their canonical ordering. LIMITED salary uses u32be of its exact integer value. LIMITED education uses S of its canonical enum. The six fields have exactly the displayed order.
- **Exclusions:** request_id is the lookup key and is not hashed. Generated identities/timestamps, raw JSON bytes, whitespace, key order and original numeric spelling do not participate. Canonically equivalent admitted requests have the same fingerprint. M1's fingerprint format is unchanged.

<a id="cg02-q37"></a>

### CG02-Q37 — Minimal successful receipt fields

- **Status:** `ACCEPTED`
- **Decision:** PreferenceSaveReceipt has exactly request_id (Common UuidV4), request_fingerprint (Common Sha256Hex), preference_set_id, preference_set_version_id, result_revision (Common Revision) and outcome (CREATED/UPDATED/UNCHANGED). Replay maps result_revision to the response revision. Receipt does not duplicate configuration, original revision precondition or timestamps; the precondition already participates in fingerprint identity.
- **Constraints:** request_id is unique in the Workspace's Preferences Save namespace, independently of Entry create request IDs. Neither fingerprint nor version reference is unique: different logical requests may have equal content, and multiple no-op receipts may refer to the same version. Retention/atomicity follow Q30.

<a id="cg02-q38"></a>

### CG02-Q38 — Business storage independent of JSON serialization

- **Status:** `ACCEPTED WITH REFINEMENT`
- **Decision:** Add preference_sets, preference_set_versions and preference_save_receipts. Root persists its five accepted fields plus a storage-only constrained singleton key; this technical key is not an API/business-object field. Version persists its four accepted fields, with configuration represented as JSON TEXT. No city/keyword child tables are needed for M2's actual consumers.
- **Canonical meaning:** Persist canonical business configuration, not a normative byte-level JSON serialization. Application canonicalization determines business equality and Q36 fingerprint input. JSON TEXT key order, whitespace and serialization spelling do not determine equality or fingerprints. Database JSON is a persistence representation and does not replace authoritative validation.
- **Integrity:** Database constraints, such as composite foreign keys, enforce version ownership, current-version membership in the same root, and receipt/root/version consistency. Concrete SQL form is an implementation choice; temporary cyclic references may be deferred until transaction commit. No content/digest uniqueness: A → B → A is a new real publication, not reuse of a historical version. No historical sequence is added. Storage owns concrete types/checks and schema recognition obligations.

<a id="cg02-q39"></a>

### CG02-Q39 — Explicit offline schema-1 to schema-2 evolution

- **Status:** `ACCEPTED`
- **Decision:** M2 uses application schema_version 2. An explicit offline migration command operates after the backend stops, obtains the same exclusive directory ownership, and starts no business listener. Only completely recognized schema 1 may upgrade; foreign, corrupt and unsupported stores fail. New schema, product version and Alembic metadata advance in one real transaction. Preserve all M1 entries and create receipts, including receipts for deleted entries, with their original identities, content and fingerprints. Migration creates no Preference root/version.
- **Startup:** Normal M2 startup encountering schema 1 reports an upgrade requirement and never silently upgrades. Eligible fresh empty storage initializes complete schema 2. A migration command seeing complete schema 2 may report no upgrade required. No automatic downgrade is provided; unchanged M1 binaries reject schema 2. Existing schema-1 definitions/migrations must not be retroactively rewritten into schema 2.
- **Uncertainty:** An uncertain migration result is not proof of rollback; re-recognize actual storage state. Normative closure is now recorded in STO-017–019; successful CLI output layout remains implementation choice. Command spelling is an implementation choice.

<a id="cg02-q40"></a>

### CG02-Q40 — Precise operation and choice-validation errors

- **Status:** `ACCEPTED WITH CORRECTION`
- **Decision:** REVISION_CONFLICT (409) covers root existence/revision precondition mismatch; REQUEST_CONFLICT (409) covers same request ID with different canonical content/precondition; REVISION_EXHAUSTED (409) covers a real increment beyond the maximum; NOT_FOUND (404) covers an absent well-formed exact version ID; INTERNAL_ERROR (500) covers an unclassified internal failure with sanitized details. A generic 500 does not establish non-commit and follows Q33 verification.
- **Validation:** Unknown mode/recruitment/education enum uses INVALID_FORMAT. Empty sets and count/numeric range violations use OUT_OF_RANGE. LIMITED missing value uses REQUIRED. UNLIMITED carrying value uses INVALID_FORMAT at the choice parent, e.g. configuration.accepted_cities. Wrong types are not coerced.
- **Correction:** Rejects the proposed UNKNOWN_FIELD classification for UNLIMITED + value: value is known but incompatible with that mode. This recommendation was not an accepted rule. Truly unknown keys still follow Q32. No INVALID_COMBINATION or FORBIDDEN_FIELD code is introduced solely for this case.
- **Ownership:** Common owns shared error representation/vocabulary; Preferences owns its triggers, paths and HTTP mapping. Adding shared vocabulary preserves M1 meanings and uses explicit new normative clauses rather than reusing published IDs with altered core semantics.

## Current Open Decision Tree

| Frontier locator | Open decision | Dependent detail |
| --- | --- | --- |
| None | Decisions through Q40 are accepted and written to reviewed consumed Contracts | Concrete SQL/CLI/test organization remains implementation choice; future Collection/query work is outside M2 |

This table records pending decision topics only. It does not preserve question transcripts or adopt proposed answers.

## Remaining Detailed Work

Dimension representations/canonical equality are settled through Q20; saved objects/publication/history through Q25; HTTP success/read boundaries, timestamps and retention through Q30; strict admission/error paths/retry precedence and raw transport budgets through Q35; fingerprint/receipt/business storage representation, explicit schema evolution direction and operation errors through Q40. Normative closure now supplies migration diagnostics/recognition, scoped Common/Workspace/Storage applicability and proof/readiness mapping. Concrete SQL choices do not reopen accepted business semantics. Platform query/admission mappings and Job Pool query/UI schemas remain in later consumer scopes.

### Normative writeback and reviewed closure

The completed [Preferences Contract](../../contracts/candidate/preferences.md) owns PRF-001–023. Actual shared additions are [COM-033–037](../../contracts/common.md#com-033), [WSP-007](../../contracts/foundation/workspace.md#wsp-007) and [STO-014–020](../../contracts/foundation/storage.md#sto-014), all at 2026-09-20.M2-r1. [Progress 6.2](../../progress/traceability.md#62-sl-01m2-reviewed-scope-and-interface-evidence) records scope/interface evidence; [Acceptance 3.2](../../acceptance.md#32-sl-01m2-contract-conformance) maps future proof; [handoff](../../development/handoff/sl-01-m2-handoff.md) directs backend-first implementation.

| Accepted decision group | Actual normative destination |
| --- | --- |
| Q1–Q10, BC1/S1 effective scope; Q11–Q14 and Q16–Q20 values/UI | PRF-001–006/022; COM-033/035 |
| Q15, Q21–Q22, Q24–Q25, Q29 saved authority/history/time | PRF-007–011/018; COM-037; WSP-007 |
| Q23, Q26–Q28, Q30, Q33–Q34 Save/read/receipt/recovery | PRF-012/014–019/021; STO-020 |
| Q31–Q32, Q35, Q40 boundary/errors | PRF-016/020; COM-033–036; WSP-007 |
| Q36–Q39 fingerprint/representation/evolution | PRF-013/014/023; STO-014–020 |

Authoring closure applies inherited local/privacy guarantees to the actual M2 consumer, supplies explicit scoped supersession and schema-2 recognition/CLI diagnostic semantics without inventing a new business resource. No further material user decision was found by read-only gap review. Independent consistency review passed after restoring Q11's precise future UI input details in PRF-022. The rejected Q29 UUID ordering and Q40 UNKNOWN_FIELD recommendation are not adopted. The original 69 M1 definition bodies remain intact; 36 new IDs are added. This is documentary readiness, not code or executed acceptance.

### Preserved source observations

For the education vocabulary frontier, both referenced repositories list separate source-search choices for junior-high-or-below, secondary vocational/technical school, high school, associate, bachelor, master and doctorate. They do not supply JobHunter's required-education-ceiling ordering, and their unrestricted search parameters differ. See [BossHunter's mapping](https://github.com/shengjidaguai-china/BossHunter/blob/main/src/bosshunter/collection/platforms/boss.py) and [scraper's mapping](https://github.com/eatmoreduck/boss-zhipin-scraper/blob/master/scripts/boss_cdp_raw.py). Platform codes are not adopted as Domain enums or rank values; CG02-Q18 now adopts the explicit six-level grouping/order as a product decision. No live account was accessed.

Read-only inspection of the user-named repositories found separate recruitment and employment-form concepts in [BossHunter configuration](https://github.com/shengjidaguai-china/BossHunter/blob/main/config.example.yaml) and its [BOSS adapter](https://github.com/shengjidaguai-china/BossHunter/blob/main/src/bosshunter/collection/platforms/boss.py). The adapter's heuristic campus detection includes some internship terms; this is not proof that internship and campus recruitment are the same canonical category. The [scraper's list mapping](https://github.com/eatmoreduck/boss-zhipin-scraper/blob/master/scripts/boss_cdp_raw.py) exposes role/salary/location/company data but does not itself establish a universally available explicit recruitment category. No live platform session was accessed. These moving-branch observations inform questions only; they are not pinned adoption evidence, normative mapping or verified current BOSS guarantees.
