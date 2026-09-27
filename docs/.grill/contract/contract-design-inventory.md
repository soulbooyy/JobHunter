# Contract Design Inventory — Architecture Decisions through Q187

## 1. Purpose, status, and reading rules

This is the requested inventory of objects, attributes, policies, and boundaries that need later
Contract design. It is **not** the formal contract specification, a table schema, implementation
report, or an additional business authority. Formal normative contracts will live in
`docs/contracts/`; this preparation inventory lives in `docs/design/contract/`.

Sources:

- [Decision Register](../grill-me-design-tree.md), interpreted through Q172 and current supplements;
- [Tool Actions](../harness/tool.md);
- [Context Engineering](../harness/context.md);
- [Memory](../harness/memory.md);
- [Budget](../harness/budget.md);
- [Recovery](../harness/recovery.md);
- [Storage, Retention, and Audit](../harness/storage.md);
- [Agent Evaluation and Observability](../eval/agent-evaluation.md), S35.1 and accepted Q173-Q187.

All Q/S references below refer to stable decision IDs in the register. A parent record marked
ACCEPTED may contain an obsolete clause: later scoped corrections, not the parent's label alone,
determine the current contract. Deprecated objects are listed only in the exclusions section.

### How to interpret the inventory

- **Root / version / asset / value / projection / policy / command / port / runtime** distinguish
  responsibilities. A listed concept does not automatically require a database table or new Aggregate.
- **Established semantics** are architecture commitments. Printed property names are names already
  discussed; except where explicitly minimal (notably EvidenceRef), they are not exhaustive schemas.
- **Example payload** lists are illustrative UI/source structures, not mandatory complete field lists.
- **Later design** must determine types, nullability, constraints, exact enums, identifiers, schemas,
  API shapes, validation errors, migration, and tests without reopening settled authority boundaries.
- Rebuild direction — Q4/S37.1: design fresh contracts for a new implementation. Old APIs, schemas,
  tests, fixtures and implementation status are not compatibility constraints or completion evidence.
  Legacy import/migration is not required. Future evolution of new-system immutable assets still
  follows the accepted historical-reference invariants.
- Handoff sequence — S38.1: this inventory moves with the Grill records to the independent
  `JobHunter/docs/design/` tree. First plan documentation with `to-spec`, write and review Spec,
  Architecture, Acceptance, Development and Progress; then conduct the detailed Contract Grill,
  complete Contract documents, and only then start development. No old implementation is imported.
- No Candidate/tenant ownership fields are to be added merely because this inventory is comprehensive.
- Ports/commands with descriptive labels and no accepted canonical name remain unnamed boundaries.
- A result being durable does not make it fact authority: RequirementSet, Analysis, and GroundingSet
  are durable derived assets, while EvidenceItemVersion contains saved career-fact authority.

### Controlling changes

Q56 removes ScreeningProfileSnapshot; Q75/Q79/Q98 remove persistent Assertions; Q108 makes Evidence
versions temporal with one current version; Q112 separates Candidate and Resume Fit; Q113 removes
KnowledgeConfirmation; Q114/Q118/Q119 synchronize affected current Resumes. Q139 separates lazy
interactive acquisition from eager exact headless inputs and separates Memory controls. Q146 removes
Advisor drafts and requires formal-apply impact preview/confirmation. Q147 adds transactional
derivative intents, not transactional rendering. Q148-Q149 bind target-specific ChangeProposal
confirmation without a suggestion-source Resume concept. Q150 approves actual frozen material;
Q151 replaces withdrawal controls with logical Item deletion and direct current-Resume membership
propagation. Q152 makes derivative generation demand-driven while preserving durable intent. Q153 separates
Resume-only removal from Knowledge-page global deletion. Q154 defers exact fail-fast prerequisite
matrices; Q155 serializes Session foreground Turns; Q156 preserves committed mutation results after
chat failure; Q157 makes Greeting a fixed-default editable Preparation value.

## 2. Cross-cutting contract families

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Stable identity and immutable version reference / value family | Roots versus versions; exact referenced identities; no silent reinterpretation or pointer rewind | Identifier formats, root/version ref typing, referential constraints | Q3, Q7, Q18, Q54, Q59, Q79, Q108 |
| Optimistic revision / concurrency contract | expected revision, CAS, stale-write conflict; revision is not business version history | Command-specific revision coverage, conflict payloads, atomic checks | Q42, Q54–Q55, Q73, Q91, Q118 |
| Idempotency and retry lineage / command-runtime values | Duplicate request protection; explicit retry creates new Run; immutable original result identity | Key scope/lifetime, payload mismatch, replayed command response versus new execution | Q30, Q73, Q116, Q122, Q124 |
| Provenance / lineage / source refs | Exact sources, imported text location or user action, policy/parser/model lineage where applicable | Typed provenance alternatives, deletion-safe references, validation | Q59, Q74, Q79, Q86, Q125, Q138, Q146 |
| Content normalization/hash / value-policy boundary | Semantic Job comparison, exact material hashes, input/output audit hashes; hash is not missing content | Canonical serialization, algorithm/version, scope of hashed material | Q3, Q50, Q56, Q77, Q125 |
| Compatibility / stale validation | Historical readability is not current eligibility; validate each task's actual frozen dependencies | Reusable validators versus task policy; stale reasons, atomic publish checks | Q40, Q76–Q77, Q87, Q108, Q116, Q143 |
| Validation findings / error results | Typed boundary failures, review-required, unsupported, unknown/incomplete reasons; no unvalidated input to authority | Error taxonomies, validation ownership, safe user diagnostics | Q3, Q27, Q71, Q111, Q117, Q126 |
| Sensitivity/privacy/admission policy | Eligible sources before access; post-Tool-result admission; contact excluded from models by default | Classification, grants/revocation, redaction, task scope, diagnostic minimization | Q19, Q54, Q72, Q125–Q126 |
| Bounded time/status/audit concepts | Fact occurrence versus observation versus capture; Run outcome versus business progress | Per-contract clocks, transition semantics, no generic catch-all status | Q7, Q31, Q37, Q50, Q122 |

## 3. Workspace configuration, Profile, and Preferences

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Local Workspace configuration / metadata, not Aggregate | Single-user premise; default Resume and current baseline metadata; no CandidateId/tenant hierarchy | Storage/config access, initialization, atomic pointer management | Q8, Q53, Q93, Q108 |
| CandidateProfile / root | profile_id, active/current ProfileVersion reference, optimistic revision | Canonical pointer spelling, single-user cardinality, command boundaries | Q54, Q119 |
| CandidateProfileVersion / immutable authority | Identity/display/contact; exact rendering references; permanently interpretable history | Actual accepted UI fields and validation | Q54, Q74, Q119 |
| Profile fields / example payload | Name/nickname/email/phone/location/GitHub/Portfolio are candidate fields, not frozen required schema | Display choices, privacy and model projection, optionality | Q54 |
| CandidateProfileDraft / proposed input | Parsed/manual proposed data is not authority until Save | Editor ownership, import provenance, validation and reconciliation | Q54, Q70, Q73, Q146 |
| Profile Save and propagation / Application boundary | New ProfileVersion plus all affected current ResumeVersions/GroundingSets; preserve displayed fields; no career baseline change for contact-only edits | Exact revision set, atomic affected-root update, derivative intents | Q119, Q147 |
| PreferenceSet / one global root | Stable identity, active_version_id, revision; one current complete configuration | Initialization, CAS update, version transition | Q45, Q55 |
| Current Job Pool filtering / derived local view | Latest PreferenceSetVersion governs saved Job display/re-screening immediately; frozen collection and historical QuickScreen retain own versions; no automatic collection or Job deletion | Current projection publication and version lineage; partial newly saved data filtered by latest rules | Q55, Q161 |
| PreferenceSetVersion / immutable authority | Entire configured HARD constraints; targets, cities, salary, recruitment type, work mode, blacklist; unset means unrestricted | Exact constraint types/units/operators; multiple directions in one set | Q45, Q55–Q56, S17.1 |
| Preference-to-platform search projection | Only expressible constraints map into source search; QuickScreen handles deterministic local checks | Search parameter mapping, normalization, exact version lineage | Q45, Q49 |
| Local Job list filter/sort state / UI projection | Temporary keyword/sort/view filters never update PreferenceSet | Read query boundary; distinction from collection request | Q45, S9.1 |
| Resume-dependent Skill preflight | No saved Resume yields create/import guidance before Run; missing task-required basic/career input also fails fast; empty saved state allowed | Per-feature prerequisite matrix and exact inputs deferred; no universal Profile requirement or completeness confirmation | Q88, Q93, Q154 |
| Default Resume selection / config value | default_resume_id; first Resume default; cannot remove last; default removal atomically chooses another | Selection command and deletion conflict behavior | Q93, Q100 |
| Advisor apply target / interaction value | Current instruction's explicitly named Resume else Workspace default; read exact actual target before ChangeProposal | Exact target resolution/display and revision checks; no suggestion-source inference | Q146, Q149 |

## 4. Candidate Knowledge, Evidence, and import

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| EvidenceItem / experience-level root | Stable experience identity; one current_version_id; Workspace-global; logical deletion excludes future formal use | Item identity/kind/current revision and logical removal representation | Q15, Q63, Q98, Q108, Q151 |
| EvidenceItemVersion / immutable fact authority | Exact Item/version identity; original evidence_schema_version; saved structured body; provenance/hash; temporal creation order | Version schema, fields by Evidence kind, Save-time version creation, old-version readers | Q75, Q79, Q86, Q96–Q98, Q108 |
| Education payload / example version-owned value | School, degree, major, dates, GPA/ranking, description | Actual supported fields and source-preserving layout | Q15, S15.1, Q98 |
| Employment/internship payload / example | Company, role, dates, responsibilities/achievements/technologies or existing content blocks | Preserve original bullet/list/paragraph structure without atomic fact extraction | S15.1, Q98 |
| Project payload / example | Name, role, period, description, technology stack, content[] | Structural restore, exact body/pointer semantics, no mandatory sentence splitting | S15.1, Q98 |
| Skill / Certification / Award and other Evidence payloads | Natural user-maintained experience/fact records | Supported kinds, schemas, eligibility; do not invent independent Assertion identities | Q15, S15.1, Q98 |
| EvidenceRef / minimal Value Object | evidence_item_version_id + pointer only; root empty pointer or canonical JSON Pointer to saved field/list item | Pointer syntax/validation and typed resolver; no per-ref duplicate schema/hash/span | Q79, Q86, Q98 |
| EvidenceResolver / original-schema reader Port | Interpret exact version using its own schema reader; retain old readers | Reader registry, unsupported schema outcomes, canonical projection | Q86 |
| Canonical Evidence read projection / derived value | Optional unified representation after correct original-schema resolution | Mapping lineage and no historical pointer rewriting | Q86 |
| Delete Evidence / Application command boundary | Global logical deletion only from Knowledge management; confirmed direct current-Resume membership removal, new baseline/versions/intents atomically; history immutable | Command/schema/entry authorization/revisions/idempotency; no Advisor global-delete action or semantic dependency graph | Q151, Q153 |
| EvidenceBaselineSnapshot / immutable snapshot | Exact currently selected current saved fact versions; no copy of all data and no completeness confirmation | Snapshot membership/hash/time, current baseline pointer/concurrency metadata | Q66, Q108, Q113 |
| EligibleEvidenceProjection / task read projection | Exact baseline and admitted/excluded facts; Skill/task/validity/privacy/permission; non-sensitive exclusion counts/reasons | Manifest representation, revocation and actual context coverage linkage | Q19, Q72, Q82, Q115 |
| EvidenceDraft / typed ingestion proposals | Parsed fields/body/provenance; candidate matches; not authority before Save | My Resumes/formal facts editor integration, unresolved reconciliation | Q64, Q70, Q98, Q146 |
| Reconciliation match/result / Application preparation values | Reuse current fact, new temporal version, new Item, ignore, unresolved; parser proposes, user decides | Matching confidence presentation, explicit conflict resolution, exact expected revisions | Q64, Q96, Q108 |
| UpdateCandidateKnowledge / shared Application command | Authorized changes/expected revisions, Evidence/current baseline/affected Resume versions/GroundingSets and necessary intents atomically | Request/result/confirmation binding, current membership, idempotency; deletion uses same authority consistency boundary | Q85, Q114, Q118, Q128, Q146–Q149, Q151 |
| Document Parser / source adapter | PDF/DOCX layout/text/provenance into typed parsed input | Supported formats, page/span extraction, failures and trust boundary | Q70, Q73, Q98, S15.1 |
| Resume Parser / deterministic preparation service | Restore sections, experiences, existing bullet structure; optional semantic enhancement, no compulsory LLM atomic decomposition | Schema mapping, validation, optional enhancement admission | Q73, Q98, S15.1 |
| ParsedDocument / ResumeTextArtifact / source artifact | Technical import input/intermediate, never Evidence authority; source hash/import/parser metadata | Exact retention and provenance retention must not depend on keeping raw binary forever | Q70, S15.1; earlier source-artifact decisions retained by reference |
| Import/reconciliation provenance | Source Resume/import/editor and actual text location/user confirmation | Exact final provenance around first Save; technical-artifact retention details remain open | Q63–Q64, Q70, Q73, Q98 |

## 5. Resumes, Suggestions, and formal Save

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Resume / stable root | Logical identity, current formal version, logical removal; no private Evidence store | Current pointer/revision, default configuration, removal constraints | Q63, Q93, Q100, Q114 |
| Remove experience from Resume / selection command | My Resumes removes only that Resume's membership and versions it; Evidence/baseline/other Resumes unchanged | Selection command/grounding/render dependencies; distinct from global deletion | Q153 |
| ResumeVersion / immutable formal asset | Whole selected current EvidenceItem bodies, Profile refs/display choices, ResumeClaim/content, experience order/presentation/layout; no per-Resume bullet selection or alternate body | Content/claim schema, exact whole-experience refs and publication identity; fine grounding still possible | Q63, Q71, Q108, Q114, Q118–Q119, Q163 |
| ResumeDraft / transient My Resumes UI state | Mutable unsaved content/revision and proposed edits; normal navigation Save/Discard/Cancel; crash may lose edits, no checkpoint/autosave | Page state and Save request validation, no durable draft recovery or Advisor/Chat/Preparation draft | Q70–Q73, Q113, Q146, Q166 |
| Dirty-state guard / UI boundary | Save persists, Discard abandons edits, Cancel stays; downstream only saved assets | Navigation protection and failure UX, not a Domain global dirty flag | Q113, Q146 |
| ResumeClaim / expression-support unit | Exact ResumeVersion/content location; classification and support refs; all formal factual claims resolved | Claim identity/granularity, content pointers, validation | Q71, Q74–Q75, Q115 |
| Claim Classification / controlled value contract | PROFILE_FACT, CAREER_FACT, DERIVED_SUMMARY, TARGETING_EXPRESSION, PRESENTATION_ONLY, AMBIGUOUS | Classification boundary, ambiguity resolution; no model factual-strength inflation | Q74 |
| Derived summary support / Claim value | Composition of confirmed facts and derivation rule; cannot amplify fact strength | Rule/explanation/ref representation | Q74 |
| ResumeGroundingSet / immutable durable derived asset | Exact ResumeVersion/Profile and actual EvidenceRef dependencies; GroundingPolicyVersion; mapping/status/findings; no active root pointer | Canonical maps, validation findings, dependency compatibility | Q75, Q79, Q87, Q108 |
| GroundingPolicyVersion / policy | Current valid support, deterministic compatibility, no lineage-only semantic proof | Version compatibility and affected-claim validation | Q87, Q108 |
| EnsureResumeGroundingSet / Application use case | Exact Resume/current Profile/current facts/policy; reuse/new validated Set/REVIEW_REQUIRED/UNSUPPORTED | Input/output/error schema; cannot rescue historical Resume for new formal use contrary to Q108 | Q87, Q108, Q114 |
| FinalizeResumeDraft / atomic Application command | Draft revision, resolved claims, reconciliation, expected revisions, idempotency; root creation only on success | My Resumes command contract, transactional authority + DerivedWorkItem intents | Q73, Q113–Q114, Q118–Q119, Q147 |
| ChangeProposal / non-editable operation proposal | Exact target/patch/impact; persists after generating Turn; Application confirms; unconfirmed source-Session proposals invalidated on Session deletion; old IDs cannot reactivate | Schema/lifetime/auth/result linkage and atomic Session/Proposal confirmation-delete arbitration; no editable Resume or suspended Run | Q148–Q149, Q158, Q167 |
| SuggestionCandidate / Suggestion / SuggestionSet | Proposed changes/rationale, Requirement/intent where relevant; authoritative EvidenceRef or validated Session refs and truthful actual input lineage | Output schema/durable candidate boundary; do not infer or require separate suggestion-source Resume state; formal patch targets ChangeProposal | Q41, Q138, Q146, Q149 |
| Persisted mutation result / Application outcome | Known committed changes and exact results independent of final model reply; Proposal-level idempotency prevents duplicate versions; UI separates saved/unfinished narration | Durable result/transaction/idempotency contract, recovery and display; no remote retry authority | Q156 |
| HumanChoice / explicit adoption confirmation | User confirmation binds exact Proposal target/patch/impact; actual result lineage independent of chat body retention; no authority expansion | Confirmation/idempotency representation and invalidation on replacement; final fields/lifetime deferred | Q41, Q52, Q96, Q148–Q149 |
| Advisor formal apply / Application boundary | Application executes exact confirmed Proposal without model reinterpretation; generating Turn ended; optional narration is new bounded execution; mutation result/idempotency independent | Typed confirm/apply/result contract, revisions and pending-action lifecycle | Q146, Q148–Q149, Q156, Q158 |
| Formal Resume read/render/export readiness / projection | Saved does not mean rendered/export-ready; EXPORT_NOT_READY possible | Readiness policy and derivative status visibility | Q118, Q147 |

## 6. Jobs, QuickScreen, collection, and source observations

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Job / stable source root | source_platform + source_job_id; current metadata; active_version_id; description availability; operational observation times | Canonical metadata, lifecycle distinct from read projections | Q12, Q17, Q44, Q48–Q50 |
| JobVersion / immutable source authority | Complete exact JD and canonical semantic fields; captured_at; normalized semantic hash; new version only on semantic change | Completeness/schema/normalization, exact active version transition | Q44, Q48, Q50 |
| Manual identity/admission / source contract | source_platform=manual; generated stable source ID; metadata-only allowed; no ManualJob subtype | Duplicate URL hint, validation and first complete version | Q17, Q44, Q48 |
| Transient collected candidate / adapter DTO | List metadata/source identity before admission; REJECT discarded, PASS/UNCERTAIN proceed to detail | Boundary types, validation, per-run dedup hash, no durable rejected content | Q27, Q49, S9.1 |
| Source-to-canonical mapping / adapter contract | Only validated source fields with real consumers enter Domain | Version-pinned mapping, failures, upstream changes | Q3, Q27 |
| Source ingestion admission policy | BOSS title/company/URL/JD complete before atomic Job + first version; Manual exception only at admission | Required canonical details, ingestion transaction/errors | Q44, Q48–Q49 |
| QuickScreenResult / deterministic result | Actual metadata snapshot/input hash, exact PreferenceSetVersion/QuickScreenPolicyVersion, PASS/REJECT/UNCERTAIN, reasons | Reproducible necessary inputs; persistence only where admitted, not rejected BOSS listings | Q45, Q49, Q56 |
| QuickScreenPolicyVersion / hard filter policy | All configured preferences hard; unset unrestricted; definite conflict rejects; missing data uncertain | Deterministic rule types and policy version | Q45, Q49, Q56 |
| Job candidate/filter/readiness projection | eligible/filtered/pending/error labels discussed; analysis_readiness separate from lifecycle | Final read-state vocabulary, recomputation and local filtering | Q7, Q45, Q48, S9.1 |
| CollectionRun / operational audit | Frozen PreferenceSetVersion/Collector/policy/search/usage/aggregate audit; never mid-run preference switch; user stop retains partial saved Jobs | Audit/stop/result contracts, old-rule UI notice, no rejected listing content; local filter uses newest preference | Q49, Q161 |
| Platform Safety State / durable operational state | Shared risk blocks subsequent access; ordinary workflow failure not automatically account risk; strong risk BLOCKED_REQUIRES_USER; predictable capacity can recover by policy | Scope/state/transition schema, adapter signal validation, explicit restoration and audit; no credentials | Q160 |
| PlatformAccessSafety / shared operational admission | Every recruiting access scoped by (platform, account); combined capacity, persistent risk, action admission across Collector/Executor/future Monitor; distinct from approval | Typed interface/atomic capacity/risk classification and resume policies; exact limits deferred | Q49, Q160 |
| Collection operational PolicyVersion | Independently versioned safe-access limits; no hardcoded Domain quotas, no official allowance claim | Configuration/versioning and budget reset semantics | Q49 |
| Source availability observation / append-only concept | Source, occurred/observed/verified time, verification method and status; human versus source verified | Concrete object name/schema and evidence of closure | Q50 |
| FreshnessPolicy / AvailabilityPolicy | Captured content vs last_seen_at vs last_verified_at; age gives STALE, absence not CLOSED | Policy versions, thresholds and availability/read freshness separation | Q50 |
| Freshness/availability projection | ACTIVE/STALE/CLOSED/UNKNOWN examples; Manual default UNKNOWN; CLOSED blocks new auto-application | Current policy interpretation; never delete historical assets | Q50 |
| Local refresh/collection request / Application boundary | Explicit latest-fetch request; normal browsing/preferences re-screen local assets | Request identity, scheduling/risk-lock refusal and stale views | Q45, Q49, S9.1 |
| Company aggregation / read view only | Job counts/cities/directions over flat Job pool | Query schema; no Company Aggregate | S5.1 |

## 7. Requirement parsing, independent Fit, and scoring

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| RequirementSet / immutable durable derived asset | Exact JobVersion/parser/model/prompt/schema/policy/parse-run lineage; stable identity and Requirements; no empty/non-usable Fit dependency | Usability/compatibility validation, source lineage and typed errors; diagnostics are not a usable target | Q10, Q14, Q58–Q59, Q111, Q117, Q171 |
| Requirement / Set-local assessment unit | Stable Requirement ID, normalized text, type, REQUIRED/PREFERRED/UNKNOWN, ALL_OF/ANY_OF/UNKNOWN, source span | Exact schema/grouping, unresolved logic, source grounding | Q111, Q117 |
| RequirementParserVersion / RequirementValidationPolicyVersion | One JD extraction, at most one deterministic-error repair; schema/enum/span/empty/duplicate/invariant checks | Canonical versions and findings, not structural validity = perfect semantic coverage | Q58–Q59, Q111, Q117 |
| EnsureRequirementSet / shared use case | Reuse compatible usable Set or independent parse; unusable zero-unit result fails downstream prerequisite; Fits cannot invent requirements | Request/result/dependency failure and producer/waiter ownership | Q58, Q110, Q142, Q144, Q171 |
| Parse target / durable claim / waiter relationship | Exact JobVersion plus parser/schema/prompt/policy target; one valid producer via DB unique target/claim/CAS; owner pays | Claim lifecycle/fencing, waiting references, cancellation and retry | Q142, Q144 |
| RequirementParseRun / RequirementParse AgentRun | Separate bounded semantic task, exact JD, primary + optional one repair, validated durable Set only | Link between application parse record and Harness AgentRun, failure codes | Q58, Q111, Q117, Q144 |
| CandidateJobFitAnalysis / immutable semantic asset | Exact RequirementSet, current saved baseline/admitted Evidence, actual Context lineage, assessments/gaps/risks | Exact compatibility, current result selection, input/privacy coverage | Q46, Q72, Q76, Q112, Q115 |
| ResumeJobFitAnalysis / independent immutable asset | Exact RequirementSet + saved eligible ResumeVersion + necessary grounding metadata; no outside facts | ResumeClaim/content support refs; no Candidate Fit prerequisite | Q112, Q115 |
| RequirementAssessment / per-Requirement result | MATCHED/PARTIAL/MISSING/UNKNOWN, type, support, Evidence strength, risk/explanation, incomplete reason | Scope-specific result schemas; MISSING has no fabricated positive support ref | Q46, Q82, Q115 |
| Analysis inclusion/completeness / lineage value | Actual admitted/inspected inputs and excluded reasons, all Requirements validated; not a completeness-confirmation object | Actual Frame coverage, missing/unknown promotion policy | Q72, Q82–Q83, Q113, Q115 |
| DeepFitScorePolicy / DeepFitScorePolicyVersion | Deterministic assessments-to-score/priority and score availability; valid Analysis may be unscored, never arbitrary zero or normal numeric rank | Weights/thresholds/PARTIAL/caps and availability representation deferred; independent Candidate/Resume views | Q46, Q51, Q112, Q168 |
| Original score / historical value | Original score or unavailable result and policy lineage preserved; valid unscored Analysis is not failure or old-score inheritance | Score snapshot/availability representation per Analysis | Q51, Q168 |
| ReScoreProjection / derived view | New policy score/coverage/priority without new model Analysis; unsupported if old data insufficient | Policy compatibility, comparison/ranking, non-recomputable reasons | Q51, Q112 |
| Fit target / concurrency key | Separate Candidate and exact-Resume targets; one valid RUNNING Run per target | Full key dimensions, uniqueness and idempotency | Q116 |
| Current compatible result / read projection | Latest successful still-compatible immutable Analysis; failed rerun retains old success | Stale indicator, recent failure overlay; no generic latest_deepfit | Q116 |
| DeepFitBatch / durable orchestration | Frozen selected members/task choices, known exact inputs, budget/concurrency, child IDs, status and created/cancelled/completed times | Member/child/task schemas; not Aggregate, chat, or cross-Job transaction | Q35, Q40, Q110, Q112, S22.1 |
| DeepFit child workflow / analysis request | Selection freeze first; dependency preparation; then full exact Job/Set/Resume/grounding/baseline/policy inputs | Task-specific request types; no placeholders or silent input upgrade | Q40, Q110 |
| DeepFitSelection / task selection value | User-selected Jobs and Candidate/Resume task choices for this operation, not long-lived Pursuit state | Exact selection identity/request schema and freeze boundary | Q23, Q35, Q110, Q112 |
| RequirementSet default/compatibility selection | Validated new Set may be usable default; historical refs do not change and no manual confirmation required | Exact default selection versus compatibility query; preserve last valid asset | Q14, Q59 |
| Batch progress / projection | completed/failed/cancelled/stale/outcome_unknown; independent Fit outcomes | Precise technical outcomes and retry mapping | Q40, Q112 |
| Transient Advisor result comparison | Per-Requirement comparison of available compatible Candidate/Resume results | Optional optimization hint, never durable CoverageAnalysis or score difference authority | Q112 |

## 8. Materials, Preparation, external execution, and Tracking

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| ApplicationPreparation / mutable root | Job/channel preparation with selected exact materials/editable Greeting/CAS; repeated entry defaults to unfinished instance; explicit new/reapplication has separate chain | Creation idempotency, resume/select when multiple, readiness revalidation without exact-input upgrade | Q16, Q25, Q42, Q146, Q157, Q162 |
| Preparation readiness / channel policy projection | Current formal Resume/grounding, greeting/material/validation/render/valid MaterialApproval | Policy-specific missing prerequisites and stale artifacts, never writable execution authority | Q42, Q77, Q91 |
| Adopt-and-return / narrow CAS command | Explicit produced formal Resume selection; expected Preparation revision; preserve other fields | Conflict reread/confirmation/narrow patch; no implicit Snapshot/Approval creation | Q91, Q146 |
| Greeting / Preparation-owned editable value | One fixed generic product default; no customization/model call; manual CAS edits; actual confirmed text/hash frozen by MaterialApproval and ExecutionSnapshot | Field/validation/default-copy contract and changed-text reconfirmation; no Aggregate/history/templates/Skill | Q157 |
| MaterialBundle / immutable asset | Exact current formal Resume-derived application materials and necessary lineage | Bundle composition/content identity and compatibility; no Advisor draft bypass | Q30, Q42, Q77, Q108 |
| Artifact / rendered output | Exact bytes/hash/source/render refs/availability; existing historical PDF/material remains immutable after fact deletion | Current versus historical publish, new-render eligibility, storage schema; no cascading historical rewrite | Q30, Q77, Q147, Q150–Q151 |
| RenderManifest / immutable derived asset | Exact render source/reference/hash/validation lineage; current pointer only when compatible | Renderer/version/font/layout inputs and output schema not yet frozen | Q42, Q77 |
| MaterialApproval / content authorization | Actual viewed frozen artifact/hash/sources and exact Greeting; renders ready before confirmation; changed Greeting needs reconfirmation; no equal-hash eligibility bypass | Exact binding/expiry/compatibility/schema; separate from ExecutionApproval | Q30, Q42, Q150, Q157 |
| ApplicationExecutionSnapshot / immutable execution input | Exact Job/channel/account/Resume/Profile/baseline/grounding/material/greeting/render/hash bindings | Atomic freeze with Preparation revisions/approvals; concrete channel-specific fields | Q30, Q42, Q77 |
| ExecutionApproval / single-use authorization | One exact Snapshot/Job/scope; expiration; consumed by one Attempt; partial continuation needs new scoped authorization | Consumption concurrency, cancellation/stale behavior, authorization evidence | Q30, Q36 |
| ExecutionAttempt / technical attempt | Exact Snapshot/Approval, lifecycle/times/verified steps/outcome; failed/partial/unknown distinct | Attempt transitions and read-back evidence, no silent retry | Q30–Q31 |
| ExecutionEvent / technical append-only event | Browser navigation/input/click/submit/read-back observations | Event payloads and diagnostic privacy; click does not mean APPLIED | Q31 |
| Browser Executor / channel adapter Port | Approved frozen materials plus necessary scoped live identity/availability checks; mismatch stops; no implicit Job refresh/Requirement parse/retarget/model analysis | Typed requests/readback/risk/outcome-sensitive recovery; explicit refresh/repreparation | Q30–Q31, Q36, Q160, Q164 |
| Channel verification policy | Reliable source observations to business event mapping | Required evidence for CONTACTED/MATERIALS_SENT/APPLIED and partial completion | Q31 |
| ApplicationRecord / stable real-attempt identity | One Job + channel/account + application attempt; repeat creates new record; manual reporting supported | Identity/idempotency; optional record only after real verified action or human report | Q16, Q25, Q30, Q37 |
| ApplicationEvent / append-only business event | Event kind, source/idempotency identity, happened_at/observed_at semantics, provenance, correction/retraction refs | Nonlinear/late/duplicate facts, HUMAN_REPORTED versus verified observations | Q31, Q37 |
| ApplicationProgressPolicy / versioned policy | Effective events derive current_progress; rejection/withdrawal controls automation by policy | Event precedence and correction interpretation; no manually overwritten status authority | Q37 |
| Interview event payload | Structured ApplicationEvent with round/type/schedule/mode/location/notes examples | Scheduled/completed/cancelled/feedback/next-round schema; not new Interview Aggregate | Q21 |
| Batch application / UI-orchestration record | Member Jobs, scheduling/concurrency/progress; each has independent full execution chain | Batch cancellation, never-dispatched states, no cross-Job rollback | Q36 |
| Channel risk circuit breaker / workflow integration | Shared platform/account Safety State prevents new affected access across workflows; undispatched Jobs not failed/applied | Integrate with PlatformAccessSafety, workflow-local failure versus strong risk; no separate bypass lock | Q36, Q160 |
| Human application report / Application command | Explicit real-world fact without fabricated automatic execution provenance | Report validation/correction, channel/account/attempt identity | Q17, Q25, Q30–Q31 |

## 9. Shared Harness, Skills, execution ownership, and Invocations

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Skill Contract / protected control | Skill identity/version, semantics, input requirements/projection, Tool+Memory allowlists, output schema, interaction, budget/repair/validation/context policy | Exact code registration and contract schema; progressive guidance is still control | Q120–Q121, Q126, Q138–Q139 |
| Skill metadata / core instructions / detailed guidance | Always-required core, on-demand templates/references | Trusted loading and version lineage; no dynamic plugin marketplace | Q139 |
| RequirementParse / CandidateJobFit / ResumeJobFit Skill contracts | Headless, EAGER_EXACT, bounded evaluation/repair; Fits read-only, Memory NONE | Per-Skill input/output/error contracts | Q111, Q115, Q120–Q121, Q139 |
| ResumeAdvisor Skill contract | Chat-based LAZY_TOOL, discussion/Suggestions, typed confirmed formal apply; no optimization Tool or working draft | Session source and action authorization, bounded loop and output types | Q138–Q139, Q146 |
| MemoryExtraction Skill contract | Independent headless background task proposing candidates only | Source range/admission/output/budget, no recursive trigger or business write | Q127–Q130 |
| AgentRun / durable bounded runtime record | run_id, Skill, initial scope/frozen input lineage, concurrency key, status, execution_generation, runtime_instance_id, retry_of_run_id, budget/deadline | Exhaustive fields/transitions/ownership after architecture; one task, Job-specific one exact JobVersion | Q47, S22.1, Q122, Q135 |
| AgentLoop / execution policy | Finite model→Tool→model steps within one Run, not multiple unrelated tasks | Allowed step limits and local continuation states | Q47, Q120–Q121 |
| AgentRunRuntime / owner | Claim/revoke/generation, lifecycle, cancel/timeout/startup reconciliation | Atomic ownership protocol, terminal outcomes, concurrency release | Q122, Q135 |
| ModelInvocation / durable call record | Sequence, exact ContextFrame, kind, dispatch state/intent, Provider/model request metadata, durable business response, usage certainty, time/outcome | Final schemas, ordering/idempotence and late usage handling | Q122, Q125, Q135, Q140–Q141 |
| Invocation kind / accounting category | PRIMARY, VALIDATION_REPAIR, CONTEXT_COMPACTION, REACTIVE_RETRY examples | Complete vocabulary; Memory extraction is task context, not an assumed new enum | Q135 |
| ModelInvocationRuntime / unique Provider boundary | Count/admit/reserve/intent/fence/dispatch/durable response/settle/cancel/recover/audit | Interface and transactional coordination with Budget/Gateway/Storage | Q122, Q135, Q140 |
| ModelGateway / typed adapter | Provider/model abstraction and request/response adaptation only | Supported Provider contract, typed errors, no hidden retries/fallback | Q135, Q140 |
| Dispatch intent / durable invocation state | Commit intent before remote request; intent without full response is potentially sent | Record/state schema, recovery classification, no guessed zero usage | Q122 |
| Durable response / protected payload reference | Complete business response before local validation, not HTTP secrets; RESPONSE_DURABLE boundary | Payload envelope, availability, parser recovery; invalid output not authority | Q122, Q125, Q141 |
| Execution fencing / ownership token | execution_generation plus effective Run ownership; revoked/old executors cannot publish canonical result | CAS/publication protocol and late diagnostic handling | Q122 |
| Retry lineage / new-Run request | Explicit Retry creates a new Run, not resurrection of unknown old Run | retry_of_run_id, current input validation, new budget admission | Q122, Q140 |
| Cancellation / timeout / reconciliation | Cancel locally not proof Provider stopped; release target separately from unknown spend | Typed interruption outcomes and ownership transitions | Q122, Q124 |
| Workflow checkpoint integration / LangGraph boundary | Restores workflow state, not authority to replay remote Invocation or browser effect | Coupling to Harness durable receipts/fences | Q122 |
| StreamBridge / SSE presentation | Transient deltas, disposable on disconnect/crash; reconnect reads eventual durable result | Transport/UI state, no durable partial transcript requirement | Q141 |
| Canonical result publication / Application boundary | Complete response → parse/validation/stale/fence check → accepted result commit | Atomic result and current projection updates, failures without false success | Q40, Q116, Q122 |
| Runtime/Invocation audit metadata | IDs, task/model/policy/hash/lineage, timing/status/known or unknown usage | Safe schema, immutable availability history, no sensitive ordinary logs | Q125 |

## 10. Context, Tool contracts, and acquisition

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| ChatSession / Conversation | Durable history/scope/result refs; one active foreground Turn; deletion cancels foreground and invalidates pending Proposals but preserves committed authority/audit | Atomic deletion/confirmation arbitration, non-resurrection, persistence/privacy; existing Memory forgetting separate | Q47, Q52, Q89, Q139, Q155, Q167 |
| Advisor dependency wait / Application orchestration state | Same active foreground Turn waits for independent RequirementParse without model slot/polling; deadline/cancel remain; exact result admitted; owner/waiter failure rules | State/result/resumption/deadline contract; unlike human confirmation after completed generating Turn | Q142, Q144, Q159 |
| Turn / user-facing interaction | User request and bounded execution/results; new input waits or explicitly stops previous Turn; independent auxiliary/dependency Runs permitted | Admission/wait/cancel/completion and proposal lifecycle; half-stream not formal Assistant result | Q47, Q130, Q141, Q155 |
| SessionContextRef / UserTurnRef | Exact permitted Session/Turn and actual cited text; validated, not career authority | Canonical ref shape/existence/text/scope validation, deletion unavailability | Q138, Q146 |
| BusinessContextAcquisition / mode policy | EAGER_EXACT headless Application freeze vs LAZY_TOOL interactive admitted reads | Per-Skill manifest and acquisition responsibility, not default all-data injection | Q139, Q143 |
| ContextPackage / immutable initial manifest | Run-start Skill/scope/policies, initial business refs, frozen inputs when known, capabilities/Memory allowlist | Exact reference schemas; payload may be absent initially for Advisor | Q83, Q94, Q139 |
| AdmittedRuntimeInput / append-only concept | Actual exact versions obtained by authorized read/write after current admission | Input lineage, active task binding, no initial Package rewriting | Q94, Q134, Q139, Q143 |
| ContextFrame / immutable per-invocation record | Exact messages/control/Skill/Tool schemas, Session/checkpoint, dynamic Memory, admitted Tool data, redaction/compaction/token accounting | Serialized payload/hash and traceability to actual ModelInvocation | Q83, Q125, Q139 |
| ContextStrategyPolicy / versioned runtime policy | Full Context default; model capacity, actual serialization, output/tool/control reserves/safety margin; future Retrieval separate | Limits/selection and preflight failure schema | Q80, Q121, Q123 |
| ContextAdmission / policy boundary | Current source/permission checks; mid-run protected EAGER_EXACT revocation ends frozen task, never silent scope reduction; new task for new scope | Grant/revoke/dispatch/publish fencing and privacy manifests; pre-freeze exclusions remain separate | Q72, Q126, Q139, Q172 |
| ContextBuilder / runtime service | Assemble only admitted current sources, pinned exact versions, dynamic Recall and protected control | Build interface, deterministic accounting and actual inclusion proof | Q83, Q139, Q143 |
| Protected Context classification / value-policy | Current user/control/permission/approval and required EAGER_EXACT inputs cannot be lossy | Per-Skill required protected payload, no all-business residency assumption | Q132, Q139 |
| ToolResult projection / externalized reference | Tool invocation/source ref, bounded preview, metadata/object refs; exact source can be reread | Payload availability, admissible source access, new read identity | Q132, Q136, Q139 |
| History window / micro structured state | Recent admitted messages, valid Tool pairs, goals/refs/pending state; no Session deletion | Projection schema and bounded selection, no new Domain authority | Q132 |
| ContextCheckpointSummary / derived continuity | Goal/work/decisions/constraints/unresolved questions/artifact-source refs/pending actions/next steps | Schema/validation/source coverage; excludes direct Memory, no second-order removal v1 | Q132, Q139 |
| ContextCompaction / policy-runtime | Protected classification→externalize→window→micro→bounded semantic checkpoint; trigger distinct target watermark | Exact thresholds deferred; one semantic call and one reactive retry per Run | Q132, Q135 |
| Reactive Context rescue / bounded branch | Explicit Provider size rejection only; local and total budgets; never retry unknown remote outcome | Error normalization and allowance accounting | Q135, Q140 |
| ToolRegistry / capability registry | Code-registered typed actions; membership not permission | Action identity/version lookup, no plugin market | Q120 |
| Tool Contract / Business Tool Action | <domain>.<resource?>.<action>; typed input/output, scope, pure action semantics, replay/effect/approval requirements | Final normalized catalog and argument/result fields | Q126, Q138, Q144; Tool Actions §§2–4 |
| ToolCall / ToolInvocation | Action, arguments and source lineage, Run/frame association, admission, replay class, effect state, result/outcome | Full durable record, idempotency/fencing/error propagation | Q122, Q126 |
| ToolInvocationRuntime | Action/schema/object/scope/permission and user-source checks; execution and result admission | Interfaces to typed Application Ports, permission revocation and action audit | Q126, Q138–Q144 |
| ToolResult / typed returned data | Actual exact read versions, action outcome or dependency missing; privacy readmission before Frame | Return envelope/metadata/error schemas; no hidden chat scan or parse | Q126, Q139, Q144 |
| job.requirements.read / accepted pure read action | Exact JobVersion + compatible existing Set; DEPENDENCY_MISSING/REQUIREMENT_SET_REQUIRED otherwise | Request/result types; no LLM/Run/asset creation within read | Q144 |
| Other read/list/search/update actions / catalog workload | resume.read, evidence.read/search and typed business read/write concepts | Normalize earlier example names without inventing implemented APIs; no suggest_improvement | Q120, Q126, Q138, Q144 |
| Application Ensure* dependency signal/handoff | Pure read exposes missing dependency; Application prepares separate task, owner pays, result admitted | Handoff/wait/failure schemas; no nested hidden semantic task | Q142, Q144 |
| Tool replay semantics / policy value | SAFE_REPLAY, genuinely supported IDEMPOTENT_REMOTE, OUTCOME_SENSITIVE | Per-action concrete replay proof and scoped idempotency | Q122 |
| Formal action authorization / policy-value boundary | Explicit user confirmation and exact applicable scope; generated parameters not consent | Evidence binding, expiry/revision conflict and consumption semantics still to specify | Q126, Q146 |

## 11. Long-term Memory and user management

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| LongTermMemoryEntry / non-business asset | Identity/type/scope/content/provenance/status, created time, supersession/invalidation concepts | Durable entry schema, manual versus Session source and retention | Q127, Q139 |
| LongTermMemoryType / allowed category | PREFERENCE, FEEDBACK, WORKING_STYLE, REUSABLE_AGENT_LEARNING; no career USER_FACT | Typed category definitions and policy behavior | Q127, Q129, Q139 |
| MemoryCandidate / proposed value | Candidate content/type/scope, traceable source/user evidence, admission outcome | Candidate schema, safe extraction findings, not self-validating authority | Q127–Q129 |
| MemoryWriteAdmissionPolicy | Type/scope/durability/business-owner/source/conflict/sensitivity checks | Deterministic admissibility without pretending arbitrary semantics are provable | Q127–Q129 |
| Memory admission disposition | ACCEPT_LONG_TERM_MEMORY, KEEP_SESSION_ONLY, ROUTE_TO_BUSINESS_AUTHORITY, REJECT | Exact enum/errors; business routing does not authorize a write | Q127 |
| Durable extraction source work / ranges | Completed eligible Turns; successful, failed/unknown and pending remain distinct; failed ranges do not block or automatically reenter later work; explicit retry only | Range/cursor/batch schemas, coalescing without false success/replay, restart and source checks | Q130, Q169–Q170 |
| MemoryExtractionTriggerPolicy | Debounce/idle/accumulation over eligible pending sources only; no failed-range inclusion or deleted-Session learning; no self-trigger | Actual trigger limits/dispatch source checks; explicit retry admission separate | Q130, Q169–Q170 |
| Extraction source validity / publication gate | Deleted Sessions prevent pending dispatch and late Memory publication; cancel where possible; existing accepted Memory independent; prior transmission not retractable | Atomic source-validity check/publication and necessary audit; no automatic old-payload resurrection | Q131, Q170 |
| Auto Learning control | Independent enablement for pending/extraction/automatic publication; recheck dispatch/commit | Control storage/change semantics, disabled-period no-backfill | Q139 |
| Recall / Injection control | Independent per-Frame read/injection gate; no deletion, old Package cannot override; no default disabled-period backfill | Dynamic admission and Tool lookup integration | Q137, Q139 |
| User Memory management / deterministic command family | View/Add/Edit/Delete/Clear All without extraction; collaboration types only | Revision/validation/result/provenance; independent of automatic learning/Recall | Q139 |
| Manual-edit versus extraction conflict policy | Newer corresponding manual edit/deletion beats older-source candidate; later genuine user preference may update | Matching/conflict metadata, conservative ambiguous outcome | Q145 |
| MemorySummary / derived view | Small admitted stable summary plus entry refs; not checkpoint or second fact store | Rebuild/invalidation and relevance/token bounds | Q127, Q139 |
| MemoryRetriever / lookup Port | Type/scope/relevance/Skill constrained; detailed entries on demand | Typed queries/results; no all-history chat scan | Q127 |
| Memory index/routing metadata / derived infrastructure | Rebuildable small lookup helpers, not required graph or complex vectors | Lightweight schema/rebuild version | Q127 |
| MemoryRetentionPolicy / lifecycle policy | Expiry/invalidate/supersede/delete/forget scope | Retention values, logical/physical deletion and purge coordination | Q127, Q131 |
| Forgetting/anti-resurrection constraint | Remove new-context use, invalidate derived views, prevent old-source recreation, late extractor recheck | Minimal source-range/tombstone representation; no forever raw-content requirement | Q131, Q145 |
| LongTermMemoryStore / persistence Port | Accepted entries, validity, supersession, manual-management provenance and forgetting constraints | Typed load/write/query and conflict/atomic publication interfaces | Q127, Q139, Q145 |
| MemoryCandidateExtractor / MemorySummaryBuilder / store Ports | Extraction via separate Run; deterministic admission/store; derived summary generation | Interfaces and publication boundaries, no additional business authority | Q127–Q130 |

## 12. Budget, capacity, and usage accounting

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| ExecutionBudget / owned resource envelope | Explicit operation scope/owner, total limits, settled usage, outstanding reservations | Final accounting units/schema, available=total−settled−outstanding | Q124, Q130 |
| Foreground operation budget | DeepFit parse/Fits/repairs or Advisor operation; distinct from background maintenance | Ownership sharing and lifetime, task-local allocations | Q124, Q130, Q144 |
| BackgroundMemoryBudget | Independent low-priority background owner; merged Turns not charged to last foreground Run | Allocation/renewal/amounts, pending work admission | Q130 |
| AgentRun local budget / limits | Model/Tool call count, tokens, cost, steps, deadline and applicable concurrency | Per-Skill total values, dimensions and enforcement | Q124, Q135 |
| Invocation reservation / accounting record | required_reservation, owner/Run/Invocation, atomic check+reserve before dispatch | Estimate/schema/transaction/idempotency, release-before-send conditions | Q124 |
| Usage settlement / actual cost value | Actual token/cost/call usage and certainty; release excess reservation; unknown not zero | Billing metadata/pricing version, over-reservation/overrun/reconciliation policy | Q124–Q125 |
| Unknown-cost exposure | Outstanding conservative spend after dispatched unknown outcome | Future settlement/evidence/release rules, not reset on Retry | Q122, Q124 |
| Kind-local allowance / runtime counters | Repair max one; semantic compaction max one per Run; reactive retry max one per Run; all share totals | Exact accounting and concurrent increment mechanics | Q135 |
| Budget Runtime / shared service | Atomic owner+local admission, settlement, unknown exposure, audit | Unified interfaces for foreground/background and model/Tool use | Q124, Q130 |
| Provider headroom / capacity gate | Foreground priority, Provider/rate/runtime capacity separate from money budget | Scheduling/concurrency values, no free background calls | Q130 |
| Pricing/reservation policy / versioned configuration | Selected model/input/output reservation/safety assumptions; amounts not frozen | Sources, rate changes, monetary versus other resource units | Q124 |
| Budget outcome/read projection | Exhaustion stops undispatched work and preserves successful assets; no invented Fit failure | User cost/unknown/budget-blocked status reporting | Q124 |

## 13. Storage, retention, and durable derived work

| Candidate / kind | Established semantics and discussed properties | Later design focus | Sources |
| --- | --- | --- | --- |
| Business Durable Asset storage Port | Long-lived formal assets and necessary lineage, including durable derived analyses | Referential integrity and independent business retention | Q125 |
| Harness Recovery Payload / protected storage | Exact Frame, complete business response, necessary ToolResult; not auth headers/cookies/tokens | Payload envelope/encoding/local protection/retention | Q125 |
| Harness Audit Metadata | Run/invocation/frame/Skill/model/policy refs, hashes, timing/status/usage/lineage | Minimal durable schema without raw sensitive content | Q125 |
| Operational Logs / Telemetry contract | Trace IDs, event/error category, timing/status only by default | Redaction/event schema/export policy; no business dumps/secrets | Q125 |
| Payload availability / state value | PAYLOAD_AVAILABLE/PAYLOAD_PURGED/SOURCE_UNAVAILABLE examples; honest absent history | Enum and content availability lookup, no fake reconstruction | Q125, Q136 |
| Active Recovery Dependency | Needed exact payload pinned until safe recovery boundary | Reference pin/cleanup coordination, not indefinite all-source retention | Q136 |
| Historical Source Reference | Durable lineage may outlive payload; fresh exact business reread is new ToolInvocation | Unavailable-source errors and safe continuation | Q136 |
| Recovery payload retention policy | Unfinished required payload retained; terminal payload independently cleanable; business history unaffected | Durations, purge implementation, audit persistence | Q125–Q136 |
| DerivedWorkItem / durable technical intent | PENDING for required work at atomic Save/delete; later actual demand also persists intent before dispatch; exact source/configuration, result linkage | Identity/schema/claim/retry/replay safety and idempotent compatible reuse; no all-format eager requirement | Q147, Q151–Q152 |
| Derived-work planning / Application Prepare boundary | Authority/currentness synchronized immediately; current preview/export/Preparation need drives generation; unused formats may stay ungenerated | Demand/required-work contract, source/configuration keys and safe reuse; model/platform work excluded | Q147, Q152 |
| Derived-work dispatcher/startup reconciliation | Durable pending scan; recheck source/current demand before costly work; obsolete queued current-work may end unexecuted; safe in-flight completion historical-only | Claim/obsolete disposition/retry/publish protocol; no platform/model replay | Q147, Q165 |
| Artifact current-publication validation | Check exact source/current demand before start and current refs before publication; stale completion cannot overwrite current; completed history preserved | Atomic publication/idempotency/currentness, obsolete-intent result semantics | Q42, Q147, Q165 |
| Derivative readiness / read projection | Formal Save succeeds even if export/render not ready | EXPORT_NOT_READY and other supported capabilities, failure surfacing | Q118, Q147 |
| Personal-data removal/retention boundaries | Resume logical removal, chat cleanup, Memory forgetting, payload purge and logical Evidence deletion are separate | Comprehensive physical erasure/import-export separate later capability; no cascade into historical PDFs/materials | Q52, Q100, Q125, Q131, Q151 |

## 14. Integration, validation, and design-governance contracts

| Candidate / kind | Established semantics | Later design focus | Sources |
| --- | --- | --- | --- |
| Repository / Application Ports | Typed canonical objects/commands; no fake Candidate ownership routes; adapters do not leak third-party exceptions/data types | Port signatures, transaction/unit-of-work boundaries, typed errors | Q2–Q5, Q27, Q53 |
| Collector / Executor channel adapters | Source-specific validated mapping, explicit safety constraints, disabled by default | Source identity, operation permissions, verification and fixture contracts | Q27, Q30, Q49 |
| Parser/model/prompt/schema/policy lineage | Immutable versions on assets/results where relevant | Canonical version identifiers/compatibility and migration | Q59, Q111, Q117, Q125 |
| Contract status / acceptance mapping | Normative target rules versus implementation state; Implemented / Partial / Planned / Deferred only by acceptance, not file existence | Slice acceptance evidence, exact status vocabulary from contract workflow | Q26, Q32 |
| Traceability Matrix / design artifact | Requirement/contract/slice/implementation/test/evaluation mappings; Progress only summary | Missing-link checks and acceptance-based status transitions | Q26, Q32 |
| Source research/feasibility input | Pinned upstream examples are research, never automatic Domain contract or implementation proof | Adapter mapping and tests from real scope, no claimed official quotas | Q3, Q27, Q49 |
| Formal architecture/contract review boundary | Fresh contracts by real responsibility; source-specific DTO versus canonical need; no old-code compatibility mandate | Detailed field Grill, new implementation acceptance, future historical-reference evolution | Q2–Q5, Q18, Q22, S24.2, S37.1 |
| Verification contracts / gates | Deterministic boundary tests, fail-closed input/side-effect/recovery checks, semantic evaluation appropriately scoped | Concrete tests/evals and Slice acceptance, not existence-based completion claims | Q26–Q27, Q32, Q82, Q117 |

## 15. Deferred extension inventory — not basic v1 implementation

| Future candidate | Properties/constraints already discussed | Scope |
| --- | --- | --- |
| RetrievalUnit | retrieval_unit_id, index_version, canonical EvidenceRef[], retrieval_text, projection_version; rehydrate exact authority and check scope | Q81, Q121, S24.1; post-v1 Candidate Agentic RAG |
| EvidenceChunk / SemanticChunk / SemanticAssertionProjection / AssertionProjection | Derived segment identity within projection/index; never persistent career authority | Q75, Q79, Q81, Q98 |
| Assertion/EvidenceItem/Chunk retrieval views, FTS/embedding indexes | Rebuildable from authoritative Evidence, versioned; no facts solely in Vector DB | S15.1, Q81, Q121 |
| Requirement query/retrieval/rerank/parent expansion/diversity/packing | Exact Requirement query, canonical source refs, method/rank/redaction/token/index/policy lineage; no retrieval miss = MISSING | Q72, Q81, Q121 |
| REQUIREMENT_RETRIEVAL Context strategy | Budget-triggered future bounded read-only Agentic RAG, no autonomous fact writes | Q121, S24.1 |
| Formal annotated parser-release evaluation | Semantic omission/necessity/logic assessment; not currently required architecture release Gate | Q117 |
| PursuitDecision / bookmark-follow intent | Distinct from filtering, batch selection, Preparation and application; no v1 legacy Shortlisted carry-forward | Q23; S37.1; future product decision |
| Future General Assistant / MockInterview / InterviewReview Skills | Must define their own inputs/interaction/Tool/Memory admission before implementation | Q127, Q139; examples do not add v1 features |
| Multi-account/Candidate/tenant identity, SearchProfile, comprehensive erasure | Independent future product decisions/migrations, no speculative current fields | Q53, Q55, Q100 |

## 16. Excluded or renamed concepts — do not design as current v1 authority

| Excluded / historical term | Current replacement or boundary | Sources |
| --- | --- | --- |
| Candidate Aggregate / CandidateId / tenant ownership | Single-user local configuration and independent assets | Q53 |
| Multi-platform logical Job with SourceListing hierarchy / physical merge | One platform/source identity per Job; no automatic merge | Q12–Q13 |
| Company Aggregate | Flat Job pool with optional Company read view | S5.1 |
| CollectedJobLead / CollectedJobObservation / JobListingSnapshot | Transient pre-admission DTO; no rejected BOSS content persistence | Q48–Q49, S9.1 |
| ScreeningProfileSnapshot | Exact PreferenceSetVersion; no legacy reader/migration required in the rebuild | Q56; S37.1 |
| HARD/SOFT preference split / parallel named SearchProfiles | One global hard PreferenceSetVersion, unset unrestricted | Q45, Q55 |
| EvidenceAssertion authoritative identity | Experience-level EvidenceItemVersion plus minimal EvidenceRef | Q75, Q79, Q98 |
| Resume-owned separate Candidate Knowledge | Shared Workspace Evidence | Q63 |
| KnowledgeConfirmation / CandidateKnowledge completeness Gate | Formal Save and exact saved baseline; bounded MISSING semantics | Q113 |
| User-selected parallel Evidence versions / ResumeEvidenceOverlay | One current temporal version per Item; historical versions for lineage | Q108 |
| CandidateKnowledgeSnapshot naming ambiguity | Use accepted EvidenceBaselineSnapshot for current saved facts, not a duplicate authority | Q66, Q108, Q113 |
| Version/item withdraw/invalidity product controls / Q105 | Delete EvidenceItem logically; propagate only explicit current Resume inclusion, no semantic graph | Q151 |
| Suggestion-source Resume inference/state | Actual target-specific ChangeProposal; exact consumed input audit is not inferred source-selection state | Q149 |
| Page ResumeDraft crash checkpoint / durable autosave | Unsaved My Resumes UI may be lost on crash; explicit Save remains durable | Q166 |
| Per-Resume bullet selection / alternate experience body | Whole current EvidenceItem body plus experience selection/order/layout | Q163 |
| Advisor working draft / draft autosave/restore / Q101 | ResumeDraft only in My Resumes; Advisor Suggestions plus confirmed formal apply | Q146 |
| Frozen Advisor draft material eligible for export/application | Only saved formal Resume-derived eligible materials | Q108, Q146 |
| ResumeCoverageAnalysis / Coverage score / Candidate Potential upper-bound | Independent CandidateJobFitAnalysis and ResumeJobFitAnalysis | Q112 |
| Generic latest_deepfit | Per-target latest successful compatible result | Q116 |
| Separate ResumeAdvisorSession or targeted Session compatibility | Unified ChatSession with explicit references and current validation | Q89, Q139 |
| SessionSummary / Session Compaction | ContextCheckpointSummary / Context Compaction outside Memory | Q132 |
| Greeting Aggregate / edit-version history / templates / generation Skill | One fixed default plus manually editable Preparation field, freeze actual approval/execution text | Q157 |
| Coupled Memory off-switch as sole control | Auto Learning, Recall, and user management separately | Q139 |
| resume.suggest_improvement | ResumeAdvisor Skill owns the semantic task | Q138 |
| jobs.requirementset | job.requirements.read; Application EnsureRequirementSet prepares dependencies | Q144 |
| Durable partial stream transcript requirement | Deltas are disposable presentation; complete response boundary only | Q141 |
| InterviewProcess / standalone InterviewRecord Aggregate | Structured ApplicationEvent payload currently; future examples not authority to add it | Q21 |

Historical terms may remain in the register as supersession evidence. They are not silently restored
by being mentioned here. In particular, Q101 and Q105 are SUPERSEDED and omitted from active rows.

### Historical naming aliases, not additional current objects

EvidenceVersion means EvidenceItemVersion in older prose. DeepFitAnalysis / DeepFitRun are historical
generic names: current contracts must distinguish CandidateJobFitAnalysis, ResumeJobFitAnalysis,
and their bounded task Runs. ResumeSuggestion belongs to the Suggestion output family, not a second
optimization authority. ParserVersion shorthand must resolve to the actual parser/model/prompt/
schema/validation identities. ResumeFit means the ResumeJobFit view, not Coverage.
ConversationSummary is historical compaction language; use ContextCheckpointSummary.
CareerProfile / KnowledgeScope are prospective isolation concepts, not current Workspace ownership.
Plural spellings such as EvidenceRefs, RequirementAssessments, or ContextFrames denote collections,
not separate entities.

## 17. Architecture closure and deferred detailed Contract work

Q148-Q152 resolve the former preview-binding, inferred-source/target, deletion-propagation,
actual-material-approval, and eager/on-demand derivative questions:

- ChangeProposal binds the actual target/patch/impact. Replacement requires a new preview; it is
  not a ResumeDraft. Its complete schema/lifetime remains detailed Contract work.
- Formal target is explicit in the current instruction or Workspace default. Do not introduce
  suggestion-source inference/state.
- Logical EvidenceItem deletion propagates through direct current Resume inclusion only, not a
  semantic dependency graph. Historical material stays immutable.
- MaterialApproval binds viewable actual frozen material and current eligibility remains separate.
- Only necessary requested derivatives need generation; intent always precedes execution.

Q153-Q157 additionally settle selection-only removal, one active foreground Turn per Session,
independent mutation outcome/idempotency, and Preparation-owned fixed-default Greeting. Empty saved
state is allowed; exact missing-input Gates remain explicitly deferred by Q154.

Q158-Q162 settle Application-owned confirmation after the generating Run ends, bounded machine
dependency waiting, persistent shared platform/account safety, frozen collection versus current local
Preferences, and unfinished-Preparation reentry.

Q163-Q167 settle whole-experience inclusion, execution checks without implicit refresh, skipping
obsolete derivative work, intentionally disposable page Drafts, and deleted-Session pending-Proposal
invalidation with atomic confirmation/deletion arbitration.

Q168-Q172 close the remaining listed architecture questions: valid unscored Analysis; isolated
failed/unknown Memory ranges with explicit retry; no new Memory from deleted sources; unusable
Requirement targets failing before Fit; and fail-closed mid-run protected-input revocation.

Business/Harness questions are resolved through Q172; Eval architecture is settled through Q187,
including N+1 boundary state, evaluator evidence scope, expected-answer/control isolation,
Skill-versus-workflow scope and Memory/background configuration. No additional in-scope architecture
frontier remains before the S38.1 artifact handoff. Q175 excludes release policy,
thresholds, Trial counts and default capability enablement. Final schemas, implementation, actual
evaluation or formal-document rewrite is not thereby complete. S37.1 accepts the rebuild direction;
this inventory update does not execute it or require migration from the old system.

Final properties, schema/nullability, per-feature prerequisite matrices, score-availability rules,
source-range/permission lifecycle representations, proposal/approval expiry, mutation-result representation,
source-import retention, actual Profile/Evidence fields, Fit target keys, budget prices/overruns,
runtime transition enums, and complete render/channel payloads belong to the later Contract Grill.
This inventory does not authorize arbitrary Tools, hidden parsing on read, automatic platform
refresh, unsafe retry, Candidate RAG, or new navigation.

## 18. Coverage and maintenance

Business coverage includes Jobs/import/filter/source safety, Profile/Preferences, Evidence/baselines,
Resume/editor/grounding/Suggestions, Requirement/Fit/scoring/batches, materials/preparation/execution,
and Application/Interview events. Harness coverage includes Skill/Run/Model/Tool, Context acquisition
and compaction, Memory learning/Recall/management, budget/capacity/usage, storage/recovery/audit,
stream presentation, and durable derivative work.

Product navigation, rewrite-stage planning, language/source-document authority, and excluded options
are not transformed into Domain objects merely to make a schema inventory larger. Their governing
records include Q1/Q6/Q11/Q21–Q27, Q32, S5.1/S5.3, S17.1–S17.4, S24.2, and S25.1–S30.1.

When later contracts are designed, each row should link to its actual contract, fields/invariants,
tests/evaluations, new-system evolution requirements, and acceptance status. Do not mark any row Implemented
because this file or corresponding code happens to exist. This inventory is architecture preparation
through Q187, not the subsequent exhaustive field-level Grill. Eval concepts belong to
infrastructure contracts, not new Domain Aggregates.

## 19. Agent Eval and Observability architecture-to-Contract inventory

Source: [Detailed Eval design](../eval/agent-evaluation.md). S35.1 accepts the platform/task/check
direction; Q173-Q187 are accepted. Production invariants keep their authority.
The rows list conceptual properties and questions for later Contract work, not final fields, database
tables, thresholds, or permission to begin implementation. Eval maintenance stays
in this inventory, the decision register, and the detailed Eval document. A new check on a Harness
contract is not itself a change to that module's design and does not justify rewriting its document.

| Candidate / kind | Established semantics or explicitly pending boundary | Later Contract focus | Sources |
| --- | --- | --- | --- |
| EvalTask / application adapter | Thin RequirementParse/CandidateFit/ResumeFit/Advisor entry, real Application/Harness code, no test-only Agent | Typed dataset input -> command -> actual task output, failures and Run/result correlation | S35.1, Eval §§4/6/7 |
| EvalScenario / infrastructure value | Skill, initial inputs, expected outcomes, positive/negative/boundary/regression intent; Advisor may span Turns and Application confirmation | Scenario schema, event sequencing, allowed alternative paths, deterministic human actions; no self-consent | Eval §§9/14; Q173 |
| EvalEnvironment / fixture boundary | Isolated per-Case/Trial fixture state; real production code/test DB commits, no live Workspace/platform effects | Temporary persistence, credentials, safe adapter binding, setup/teardown and per-trial isolation | Q173 |
| ScenarioFixture / immutable input artifact | Immutable reconstructible versions/current pointers/permissions/state/artifacts; stable refs/hash validation; no latest fallback | Snapshot schema, provenance, content hashes, hydration validation, immutable storage/ref handling | Q177 |
| Dataset / DatasetVersion / DatasetItem refs | Langfuse is primary dataset/version platform; Skill dev/holdout separation and case metadata | Exact timestamp/version selection, item identity/status, input/expected-output typing; schema version separately | S35.1, Eval §§5/8/10 |
| Case classification / metadata | positive, negative, boundary, regression; human-reviewed production failures can become regression cases | Controlled labels, scenario coverage, sensitive source handling, Contract-supersession retirement | Eval §§9/21 |
| Experiment configuration / manifest | Exact dataset/model/prompt/Skill/Context configuration; frozen fixture/events/expected outcomes/rubric/Runner configuration required; remote output may vary | Code/runner/evaluator/model settings, hashes, comparative compatibility and missing configuration | S35.1; Q177 |
| Trial / evaluation execution record | Repeated attempts measure stability, not best-of-N selection; proposed 1/3/5 counts not frozen | Trial identity/isolation, live versus replay classification, repair/retry distinction and interrupted outcomes | Eval §18; Q173 |
| Scenario event / Turn/Tool/confirmation projection | Observable Task/Turn/Run events; Proposal confirmation occurs outside the generating Run | MUST/MAY/MUST NOT predicates, actual action/result order and exact ref checks, admitted event projection | Q158; Eval §§14/16 |
| EvalTaskResult / observation bundle | Actual result and state evidence, not only final prose; evidence minimization required | Typed outcomes, canonical result refs, required evidence completeness, forbidden payloads | Eval §§4/6/19; Q174 |
| Domain-aware ContractCheck / evaluator function | Deterministic persisted authority/lineage/authorization/mutation checks; results published to platform | Input evidence, Domain hydration, pre/post-state diff, declared propagation, typed verdict and safe reasons | S35.1, Eval §6 |
| Generic CodeEvaluator binding | Prefer Langfuse/SDK facilities; local function execution does not imply a new framework | Callable inputs/output schema, platform versus SDK deployment, code/runtime version and errors | Eval §§5/28; platform notes |
| Requirement judgment / matching rubric | Extraction/necessity/logic/source support, UNKNOWN allowed; invalid/unusable sets fail closed | Unit alignment, multiple correct parses, duplicates, source-span rules, Precision/Recall denominator | Q117/Q171; Eval §11 |
| Fit judgment / support annotation | Four statuses scoped per independent Fit; exact Evidence or Resume support; unscoreable Analysis valid | Multi-label/partial support, semantic vs referential validity, exclusion cases, status/scoreability metrics | Q112/Q115/Q168; Eval §§12/13 |
| Advisor rubric / trajectory constraints | Selection, arguments, alternative legal trajectories, advice quality, exact confirmed target/patch/impact | Scenario-conditioned required reads, sanctioned multi-Resume reads, Session refs and confirmed fact creation | Q138/Q148/Q149/Q158; Eval §14 |
| SemanticJudge / platform evaluator | LLM judgment only for semantic/subjective quality, never runtime authorization authority | Judge prompt/model/rubric version, admitted evidence, output validity, unavailable judgments | Eval §§5/26; Q176 |
| HumanCalibrationSet / reviewed judgments | Compare human review and LLM judges; judge is not ground truth | Sampling, agreement/disagreement, adjudication, judge drift and calibration version | Eval §26 |
| EvalScore / CheckResult / metric observation | Separate hard, quality, reliability and efficiency; no compensating overall Agent score | Value types/units/denominators, missing vs failure vs unavailable, confidence and raw counts | Eval §19; Q168 |
| Metric aggregation / comparison policy | Langfuse preferred generic platform, semantics owned by project | Per-case coverage, repeated trials, skipped/errors, unsupported-match visibility, no best-of-N claims | Eval §§18/19/28 |
| Release/rollout policy / deferred, not this Grill | Eval supplies evidence; repository/CI policy, default enablement, thresholds and Trial counts explicitly not designed now | Later rollout work, not an active Contract or architecture decision to settle in this round | Q175; Eval §20 |
| Holdout governance | Separate from tuning; Q117 preserved, no mandatory annotated ParserVersion certification | Dataset use/leakage provenance; release use and required sizes deferred to rollout work | Q117, Q175; Eval §10 |
| Evaluator execution/budget owner | Agent-under-test uses business Runtime; judge uses independent Eval invocation/budget/model/rubric/observability identity, cannot alter business state/outcome | Judge credentials/data admission/cost limits/unknown usage/retry/audit; no foreground budget leakage | Q176 |
| Observability instrumentation binding | CallbackHandler + direct SDK, no generic custom Telemetry Port; no new Domain dependency | Ownership/correlation across graph and auxiliary paths, duplicate suppression, SDK compatibility | S35.1; Q174; Eval §§22/23/25 |
| Trace export / privacy policy | Self-hosting is not raw-content authorization; local recovery stays separate | Pre-export masking/allowlist across callbacks and SDK, exact refs/hash admission, payload enablement/retention | Q125; Q174; Eval §24 |
| Telemetry availability / Eval completeness | Langfuse not completion/settlement/recovery authority; outages never trigger rollback/replay; missing necessary observations = INCOMPLETE_EVIDENCE | Delivery/flush failure, bounded buffering policy, incomplete scores, production vs experiment outcomes | Q174 |
| Regression promotion / human review | Production observation -> reviewed case, no automatic Dataset truth | Sanitization/consent, source provenance, fixture reconstruction, retention and accepted labels | Eval §§9/21/24 |
| Langfuse feature/deployment admission | Platform choice accepted, feature support/worker topology must be verified for actual deployment | SDK/platform version pin, Python evaluator execution location, self-host configuration and feasibility | S35.1; Eval platform notes |
| Clean-slate Eval implementation | New thin task/Scenario/check code and tests against accepted contracts; old assets optional reference, no migration prerequisite | New fixture/rubric/metric contracts and verified acceptance; no inherited completion claims | Q4; S37.1; Eval §§7/29 |

This inventory does not imply a local Dataset database, independent Eval framework, durable Advisor
draft, mandatory annotated parser certification, or an implemented Judge integration. Q176 accepts separate Eval judge ownership; implementation and
its exact interfaces remain future work.

### Round 36 accepted architecture — detailed schemas remain deferred

| Candidate / kind | Accepted architecture semantics | Later Contract focus | Sources |
| --- | --- | --- | --- |
| ScenarioDriver / thin Eval adapter | Fixed user Turns and logical events through real Application/Harness; full workflow assertions use canonical state, no User Simulator or trace-delivery dependency | Event interfaces/checkpoints, exact-one real Proposal matching and formal confirmation; preserve Q158 | Q173/Q177/Q178 |
| Task outcome versus Evaluation result | Task outcome separate from each check; expected rejection can be correct, violations/incomplete/evaluator errors distinct; no hidden sample drops | Exact result schema, coverage and denominator formulas, applicability and retained findings | Q174/Q179 |
| Expected-behavior constraints / semantic judgment | Exact deterministic refs/permission/authorization; legitimate semantic alternatives allowed within contract/grounding/scenario | Unit matching, support alternatives, constraint representation and ambiguous-label handling | Q117/Q180 |
| Regression-case retention / thin curation | Reviewed reproducible minimal sanitized/synthetic fixture separate from original payload retention; missing executable coverage disclosed | Consistent transformations, reproduction checks, admitted storage/expiry and source lineage | S35.1/Q177/Q181 |
| Evaluation pass over existing Trial evidence | Same captured outcome may be re-evaluated without Agent/Tool/mutation replay; original results preserved, actual evidence required | Evaluation-to-Trial refs, versioned scores, available actual post-state, missing/purged evidence outcomes | Q174/Q176/Q182 |
| N+1 case / targeted execution scope | Freeze preceding N Turns and rerun only the next input for a known conversational failure; no claim of full earlier-workflow success | Historical context representation and coherent exact boundary-state hydration without historical replay | Q178/Q183 |
| Exact-one Proposal match / Scenario action boundary | Driver verifies one real Proposal satisfying scenario conditions before formal Application confirmation; none/multiple cannot authorize selection | Matching predicates/events, failure outcomes, accepted actual target/patch/impact and revision checks | Q178 |
| Platform Session/Trace association | Langfuse groups observations; JobHunter owns ChatSession/Turn and Scenario/confirmation behavior; assertions independent of trace upload | Correlation IDs and structured results, canonical evidence access, no business authority in telemetry | Q174/Q178 |

### Round 37 accepted architecture — detailed schemas remain deferred

| Candidate / kind | Accepted architecture semantics | Later Contract focus | Sources |
| --- | --- | --- | --- |
| N+1 boundary Fixture | Coherent necessary business/session/runtime state plus N prior Turns; hydrate isolated state and run only N+1, no historical call/write replay or full-workflow claim | Exact versions/refs, Proposal/source state, required artifacts, hydration validation and missing-state outcome | Q178/Q183 |
| Evaluator evidence projection | Task-scoped actual inputs/output/constraints; Resume-only Fit judging, admitted Candidate scope and distinct Advisor Session facts; separate deterministic audit access | Typed evidence inputs, source distinction, privacy/admission, availability and evaluator-specific requirements | Q174/Q176/Q184 |
| Eval input/control partition | Task data separate from evaluator reference and Scenario control; no labels/future Turns/prior scores in Agent Context; candidate text cannot alter judge rules | Consumer visibility, trusted rubric, event-to-current-input transition, projection validation and leakage checks | Q177/Q180/Q185 |
| Experiment task scope / attribution | Skill-focused and composed workflows both use real entry points; ready dependencies reused normally, actual stage failures/costs attributed without false end-to-end claims | Scope declaration, initial dependency state, Ensure reuse, stage outcomes, unexecuted-task evidence and comparison compatibility | Q173/Q186 |
| Experiment Memory/background configuration | Frozen isolated initial Memory/Recall/permissions; supported controls prevent unscripted changes; dedicated Scenarios drive real learning with separate costs | Configuration manifest, enabled capabilities/events, per-Trial isolation, background accounting and declared coverage | Q173/Q177/Q187 |
