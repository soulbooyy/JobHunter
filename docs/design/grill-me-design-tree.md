# Grill-Me Design Tree Decision Register

## Purpose and Authority

This file preserves decisions reached during the JobHunter architecture Grill-Me session.
The accepted delivery direction is a clean-slate documentation and code rebuild (Q4/S37.1),
not an incremental refactor constrained by the old implementation. This register is a recovery aid
for context compaction, handoff, and later sessions, not a new source of product, architecture,
engineering, contract, acceptance, or implementation authority.

Formal authority will reside in the following documents in the new repository once written and
reviewed. They are not supplied by this artifact-only transfer:

- `docs/spec.md`
- `docs/architecture.md`
- `docs/acceptance.md`
- `docs/development.md`
- `docs/contracts/*`
- `docs/progress.md`

This register records conclusions only. It does not authorize implementation or changes to the
formal documents. Supersession is recorded before cleanup. On an explicit user cleanup request,
wholly superseded records may be removed; replacement records retain their IDs and relationships.
Partially valid records remain, with later corrections taking precedence over their historical clauses.

## Status Vocabulary

- `ACCEPTED`: adopted for the new design and ready to be written into the indicated formal documents.
- `OPEN`: still requires a product or architecture decision.
- `DEFERRED`: intentionally postponed until a named dependency or later design slice.
- `SUPERSEDED`: replaced by a later decision; retained until explicitly requested cleanup.
  A superseded clause does not by itself make the entire surrounding accepted record obsolete.
- `REJECTED`: considered and explicitly excluded from the current design.

## Session State

- Last answered batch: Q183-Q187; Eval architecture direction recorded as S35.1
- Answers persisted through: Q187; all questions in the recorded architecture frontier are accepted
- Q188-Q192 rebuild-execution suggestions received one unified user direction, recorded in S38.1;
  the previous recommendations were not accepted as a bundle. No further architecture questions
  remain before the requested artifact handoff.
- Latest supplement: S37.1 replaces incremental refactoring with a complete documentation and code
  rebuild. Old APIs, schemas, tests and completion claims do not constrain the new baseline.
  This update changes design records only; it deletes no code or data.
- Repository handoff — S38.1: move the nine Grill records from the old job-hunter/docs/design tree
  into the independent JobHunter/docs/design tree. Do not transfer old code, formal documents or
  runtime data. Use the user's new documentation-first sequence in Q22.
- Updated: 2026-09-18 HKT
- Architecture frontier: Q173-Q187 settle Eval isolation, observability, independent judges, exact
  fixtures, N+1/Scenario driving and boundary state, check completeness, valid alternatives,
  regression retention, re-evaluation, evaluator evidence scope, answer/control isolation,
  Skill-versus-workflow experiments, and controlled Memory/background activity.
  No additional in-scope architecture question remains. S38.1 closes this phase with an artifact
  handoff and an explicit documentation-first plan; it does not start development.
  Q175 excludes rollout/release policy, thresholds, Trial counts, and default enablement.
  Detailed Contract design remains a separate follow-up Grill.
- Detailed Eval record: [Agent Evaluation and Observability](eval/agent-evaluation.md). The register
  keeps key decisions only; evaluator metrics, examples, platform notes, and proposed code layout
  live in that module. Contract candidates are synchronized without freezing their final fields.
- Detailed Harness module records: [Memory](harness/memory.md), [Recovery](harness/recovery.md),
  [Budget](harness/budget.md), [Context](harness/context.md), [Storage](harness/storage.md),
  [Tool Actions](harness/tool.md).
  They preserve architecture designs, not final field schemas or a new
  class of formal authority. Q127 adds collaboration-only Long-term Memory to v1, not career-fact
  Memory, General Assistant, interview Skills, or Candidate Evidence Agentic RAG.
- Latest subsystem correction: Q168 permits valid analyses without a defensible total score.
  Q169 isolates failed/unknown Memory batches from later learning; Q170 blocks new learning from
  deleted Session sources. Q171 rejects unusable Requirement targets before Fit. Q172 terminates
  protected exact tasks on mid-run input-permission revocation rather than shrinking their scope.
  Earlier authority, immutable lineage, runtime budgets/recovery and explicit action boundaries remain.
- Contract inventory: [Contract Design Inventory](contract/contract-design-inventory.md) collects
  currently valid objects, known attribute semantics, invariants, and sources; it is not final schemas.
  Q101 and Q105 were explicitly superseded by Q146 and Q151 respectively and removed in the
  latest requested cleanup. Their replacements and exclusions from active inventory remain.
- Memory module filename is memory.md, renamed by the user; design references are synchronized.
- Module maintenance: update existing Harness files only when an accepted decision actually changes
  that module's responsibilities, runtime behavior, authority, storage, or permission boundary.
  Eval Grill normally changes only this register, eval/agent-evaluation.md, and the Contract inventory;
  merely evaluating a Harness invariant is not a module-design change. New Harness files still
  require an explicit request (S27.1).
- Interview scope: this entire Grill settles architectural contracts, responsibilities, authority,
  and invariants only. Exhaustive field/schema definitions and detailed state-transition tables
  belong to a separate follow-up Grill after these boundaries stabilize (S24.2).
- v1 scope: Agentic RAG is a documented post-v1 extension, not part of v1 implementation or further
  detailed questioning in this Grill (Q121/S24.1).
- Current precedence: Q113 removes KnowledgeConfirmation everywhere; Q114 automatically synchronizes
  affected current Resumes; Q115 scopes the shared four assessment states; Q116 serializes each Fit
  target; Q117 defers formal offline ParserVersion release evaluation.
- Latest explicit cleanup: After Q172, removed wholly SUPERSEDED Q101/Q105 and the now-empty
  Round 21 heading, retaining Q146/Q151 as replacements. Partially valid records, REJECTED alternatives,
  DEFERRED work, decision IDs, and replacement links remain unchanged. Earlier Q138-Q142 cleanup
  removed Q78/Q84 and explicitly replaced clauses; prior Q65/Q68/Q69/Q92/Q95/Q99/Q102/Q103/Q104/Q106/Q107
  removal remains. No renumbering or formal-doc edits.

## Round 1 — Design Authority and Canonical-Contract Principles

### Q1 — Product and documentation target

- **Status:** `ACCEPTED`
- **Decision:** Rewrite the documentation around the complete JobHunter capability chain: Job
  import/collection, QuickScreen, user selection, DeepFit, resume improvement, application
  preparation, submission, and progress tracking. The product is a non-linear workspace organized
  by user tasks, not one mandatory pipeline. DeepFit and Resume Advisor are independently callable
  Use Cases when their own prerequisites are satisfied.
- **Rationale:** The left navigation and the independently callable Use Cases describe the intended
  product more accurately than a single start-to-finish workflow diagram.
- **Formal writeback:** `spec.md`, `architecture.md`, `acceptance.md`

### Q2 — Dedicated data-contract authority

- **Status:** `ACCEPTED`
- **Decision:** Add a normative `docs/contracts/` area defining important interfaces, entities,
  identity, versioning, authority, lineage, privacy, and cross-domain references. Product and
  architecture documents reference these contracts instead of duplicating field definitions.
- **Rationale:** The current contract is distributed across prose, Domain code, API schemas,
  persistence models, frontend validators, and tests, making internal fields and boundaries hard to
  control.
- **Formal writeback:** `architecture.md`, `contracts/*`, `development.md`

### Q3 — Canonical data-model principle

- **Status:** `ACCEPTED`
- **Decision:** Use minimal, stable JobHunter canonical contracts. Source-specific payloads remain at
  validated adapter and source-snapshot boundaries unless a concrete JobHunter consumer justifies a
  canonical field.
- **Deferred detail:** Exact Job and Candidate fields will be decided during the relevant BOSS
  Collector, Resume Parser, Candidate Profile UI, and contract reviews. BossHunter and
  boss-zhipin-scraper are research inputs, not automatic Domain authority.
- **Rationale:** Avoid a source-shaped Domain and large collections of speculative nullable fields.
- **Formal writeback:** `architecture.md`, `contracts/*`

### Q4 — Clean-slate documentation and code rebuild

- **Status:** `ACCEPTED`; revised by the user's post-Q187 direction (S37.1).
- **Decision:** Rewrite JobHunter's formal documentation and implement its code anew from the
  effective Grill decisions and subsequent detailed contracts. Do not adapt the old implementation
  incrementally or preserve its structure as a constraint.
- **Legacy boundary:** Old APIs, SQLite schemas/history, modules, tests and Eval assets impose no
  mandatory backward-compatibility, migration or dual-running obligation. They may serve as reference,
  but their behavior and test expectations cannot override the new contracts.
- **Preserved design:** Accepted business scope, authority, immutable history, exact references,
  confirmation, privacy, safety and test-first/Eval principles still govern the new implementation.
  Historical readers and version evolution for assets created under the new contracts are distinct
  from migrating the old implementation.
- **Progress:** Establish implementation status against the new contracts and verified acceptance
  evidence. Old completion claims do not automatically count as implemented capabilities.
- **Execution boundary:** This decision update deletes or overwrites no existing code, formal
  documents, databases, personal data or Git history. Later destructive replacement needs concrete
  authorized targets; optional old-data import is separate scope, not an assumed requirement.
- **Formal writeback:** All formal documents, `contracts/*`, and the new implementation plan.

## Round 2 — Information Architecture, State Boundaries, and Core Identities

### Q5 — Contract-document split strategy

- **Status:** `ACCEPTED`
- **Decision:** Split contracts by real domain/authority boundaries, but do not freeze the final file
  count before each domain is reviewed. Exact decomposition remains incremental.
- **Rationale:** Navigation categories are not Domain boundaries, and premature file splitting can
  create duplication. Refined by Q11.
- **Formal writeback:** `architecture.md`, `contracts/*`, `development.md`

### Q6 — Navigation versus Domain ownership

- **Status:** `ACCEPTED`
- **Decision:** The primary navigation represents user task organization only. A Domain object may
  serve several navigation areas, and one navigation area may compose several Domains through read
  models and Application Use Cases.
- **Rationale:** UI information architecture and Domain ownership solve different problems and must
  not be forced into a one-to-one mapping.
- **Formal writeback:** `spec.md`, `architecture.md`

### Q7 — Separate evolution mechanisms instead of one lifecycle

- **Status:** `ACCEPTED`
- **Decision:** Split Opportunity eligibility, material readiness, and application progress rather
  than extending one Job lifecycle. Evidence, DeepFit, Retrieval, AgentRun, ResumeVersion, and other
  objects must each be reviewed to determine whether they need a state machine, immutable versions,
  append-only events/decisions, a versioned policy, a run status, or only a derived projection.
- **Rationale:** These objects have different ownership and evolution semantics. A universal state
  machine would manufacture transitions and duplicate authority.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q8 — Candidate asset boundaries

- **Status:** `ACCEPTED`
- **Decision:** Separate Candidate information conceptually into CandidateProfile, PreferenceSet,
  EvidenceItemVersion, ResumeVersion, and task-specific ScreeningProfileSnapshot/projections.
  Candidate-facing navigation may group targets and preferences, education and experience, skills
  and achievements, resumes, and application/interview history without making that UI tree one
  Domain aggregate.
- **Deferred detail:** Do not freeze exact fields until the BOSS Collector, Resume Parser, Candidate
  Profile UI, and related contract designs provide concrete consumers.
- **Rationale:** Preferences, career facts, resume expression, and application history have
  different authority and privacy semantics.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`

### Q10 — Requirement as a reusable analysis asset

- **Status:** `ACCEPTED`
- **Decision:** Promote requirement parsing to an independently callable, rerunnable, versioned Use
  Case. A RequirementSet is a derived analysis asset bound to an exact JobVersion and reusable by
  QuickScreen, DeepFit, Resume Advisor, and other downstream consumers.
- **Rationale:** Requirement parsing must not remain a hidden side effect of QuickScreen, and parser
  evolution must not rewrite historical downstream lineage.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 3 — Documentation Topology and Domain Contract Direction

### Q11 — Top-level document categories

- **Status:** `ACCEPTED`
- **Decision:** Keep six top-level documentation categories: `spec.md` for product scope,
  `architecture.md` for system design and authority, `acceptance.md` for completion gates,
  `development.md` for delivery rules, `contracts/` for concrete business/data boundaries, and
  `progress.md` for current implementation state. Complexity goes inside `contracts/`. Add ADRs
  later only when a decision genuinely needs durable rationale; do not create more overview
  categories.
- **Rationale:** These six ownership categories are sufficient and make duplication easier to
  detect.
- **Formal writeback:** `architecture.md`, `development.md`, `contracts/*`

### Q12 — Current Job identity scope

- **Status:** `ACCEPTED`
- **Decision:** Do not implement cross-platform Job merging or multi-SourceListing
  canonicalization now. One reliable platform identity maps to one Job. Content changes for the same
  `(source_platform, source_job_id)` produce JobVersions. Similar listings from different platforms
  remain independent Jobs. Revisit cross-platform aggregation only as a separate Slice when real
  data proves the need.
- **Rationale:** BOSS collection is the near-term primary need; cross-platform aggregation adds
  identity, canonicalization, merge, and lineage complexity without current business value.
- **Supersedes:** Q9's cross-platform logical-Job and multi-listing model.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `development.md`

### Q13 — Historical physical merge after duplicate confirmation

- **Status:** `REJECTED`
- **Decision:** Exclude physical or logical cross-platform Job merge behavior from the current
  design.
- **Rationale:** Q12 removes cross-platform aggregation from scope, so reparenting or aliasing
  historical Jobs has no current consumer. Reconsider only with the future aggregation Slice.
- **Controlled by:** Q12.
- **Formal writeback:** `spec.md` non-goals/deferred scope, `contracts/*`

### Q14 — RequirementSet activation

- **Status:** `ACCEPTED`
- **Decision:** Separate RequirementSet creation from activation. A new parse result becomes the
  current default only after validation. Version 1 may automatically activate a successfully
  validated set; manual confirmation is not required. Historical consumers retain their exact
  RequirementSet references.
- **Rationale:** Separate activation protects the last valid set and preserves downstream lineage
  while avoiding unnecessary user friction in the initial deterministic workflow.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q15 — Career facts under Evidence

- **Status:** `ACCEPTED`
- **Decision:** Initially represent education, employment, internships, projects, skills,
  certifications, awards, portfolios, and similar Candidate career facts as typed Evidence. Promote
  a category to an independent Aggregate only after it develops independent business behavior or a
  real lifecycle.
- **Rationale:** A shared Evidence authority supplies versioning, provenance, sensitivity,
  confirmation, eligibility, and grounding without premature aggregate proliferation.
- **Deferred detail:** Exact Evidence taxonomy and typed payload fields await Candidate/Resume
  contract and parser design.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`

### Q16 — Candidate assets, preparation, and application records

- **Status:** `ACCEPTED`
- **Decision:** CandidateProfile, PreferenceSet, Evidence, and ResumeVersion are long-lived Candidate
  assets independent of a particular submission. `ApplicationPreparation` is one Job-specific,
  channel-aware preparation instance that references existing Candidate assets and owns or links
  Job-specific greeting, material, render, and readiness information. Create `ApplicationRecord`
  only after real external contact/submission or an explicit human report of an application.
- **Rationale:** Resume/data maintenance, submission preparation, and real-world application history
  are separate authority boundaries.
- **Greeting refinement — Q157:** Preparation owns one editable Greeting field initialized from
  fixed generic product text, without personalization/model invocation, independent root/version
  history, template library, or Skill. Edits use Preparation CAS. MaterialApproval freezes actual
  viewed text/hash and edits require reconfirmation; ExecutionSnapshot freezes actual send text.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 4 — Manual Jobs, Evolution Review, Model Visibility, and Product Entry Points

### Q17 — Manual Job identity and incomplete JD

- **Status:** `ACCEPTED`
- **Decision:** Manual Job is a lightweight custom-application supplement, not the primary collector.
  The user supplies URL, company, title, and optional JD. Each creation receives an independent
  `manual` source identity and is stored as an ordinary Job/JobVersion. Do not automatically merge
  it with existing Jobs; the same URL may produce only a non-blocking duplicate hint. A missing JD
  still permits recording and Tracking, but Requirement parsing and DeepFit require the user to add
  a job description first.
- **Rationale:** Manual applications need low-friction record keeping without importing speculative
  identity or deduplication complexity.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q18 — Minimal evolution-mechanism review rule

- **Status:** `ACCEPTED`
- **Decision:** For every object, select the smallest mechanism matching its real semantics. Prefer
  immutable versions, append-only events/decisions, and derived projections. Introduce a state
  machine only for genuine long-lived stages with legal transitions. Use run status only for bounded
  computation and policy versions only for historical explainability. Do not build a generic
  Lifecycle Framework.
- **Rationale:** A shared framework would create ceremony without proving shared behavior or
  ownership.
- **Formal writeback:** `architecture.md`, `development.md`, `contracts/*`, `acceptance.md`

### Q19 — Candidate model-visibility boundary

- **Status:** `ACCEPTED`
- **Decision:** Candidate data reaches a model only through task-level projection, sensitivity and
  privacy admission, redaction, and ContextPackage/ContextFrame construction. Freeze the mechanism
  and minimum-visibility default now; define exact allowlists separately when DeepFit, Resume
  Advisor, and other Harness Skills are implemented. EvidenceItemVersion is the confirmed career
  fact layer, while ResumeVersion is a selection and expression of facts. DeepFit normally consumes
  RequirementSet plus relevant Evidence, not an entire Resume. Resume Advisor/Suggestion consumes
  both the edited ResumeVersion and relevant Evidence. Contact details, identity numbers, family
  information, and raw source documents are model-invisible by default. Tool results pass through
  the same admission. Model visibility and UI/API visibility are separate contracts.
- **Rationale:** Local storage is not model authorization, and Resume expression must not replace
  Evidence authority.
- **Deferred detail:** Skill-specific field allowlists and redaction rules.
- **Input-scope correction — Q112:** CandidateJobFit uses admitted current baseline Evidence;
  ResumeJobFit uses only the exact Resume's admitted content. The historical generic DeepFit input
  description above is not a shared input contract for both independent tasks.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q21 — Interview representation

- **Status:** `ACCEPTED`
- **Decision:** Do not introduce an InterviewProcess Aggregate initially. Represent interviews as
  structured, append-only ApplicationEvents, including at least `INTERVIEW_SCHEDULED`,
  `INTERVIEW_COMPLETED`, `INTERVIEW_CANCELLED`, `INTERVIEW_FEEDBACK_RECORDED`, and
  `NEXT_ROUND_CONFIRMED`. Events may contain round, round type, schedule, mode/location, and notes.
  Derive `Interviewing` from events. Promote Interview to an Aggregate only when scheduling,
  multi-round constraints, preparation tasks, reminders, participants/meetings, or a review Agent
  creates independent business behavior.
- **Rationale:** Current Tracking needs an auditable timeline, not a speculative interview state
  machine.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q22 — Documentation-first rebuild sequence

- **Status:** `ACCEPTED`
- **Decision — S38.1:** In the new repository, first use the user-selected `to-spec` skill to design
  the documentation-writing plan. Then write `spec.md`, `architecture.md`, `acceptance.md`,
  `development.md` and `progress.md`, and review them for correctness and consistency. Only after
  that review conduct the separate detailed Contract Grill, complete the Contract documents, and
  then begin formal development. The artifact handoff does not execute these later stages.
- **Detail boundary:** The first five documents describe the accepted architecture without pretending
  that exhaustive fields/interfaces are already frozen. The later Contract Grill resolves those
  details; reconcile affected references before implementation rather than silently contradicting
  the reviewed documents. Implementation slices remain later planning, not a new architecture round.
- **Rebuild boundary — S37.1:** Old documents/code are reference, not compatibility constraints or
  proof of completion. Re-establish Progress for the new implementation; detailed Contract work
  does not reopen settled architecture merely to fit legacy code.
- **Replaces:** The earlier fixed D0-D6/two-pass ordering that put detailed Contract review before
  architecture/acceptance/development documentation. The user's new sequence takes precedence.
- **Completion criterion:** Any JobHunter capability must reveal why it exists, its data
  prerequisites, authority owner, Harness involvement, persistence semantics, acceptance proof, and
  current implementation status.
- **Formal writeback:** `development.md`, `progress.md`, all formal documents during their assigned
  stages

## Round 5 — Pursuit, Advisor, Preparation, Contract Status, and Research Inputs

### Q23 — Shortlisted versus DeepFitSelection

- **Status:** `ACCEPTED`
- **Decision:** `Shortlisted` means a long-lived user `PursuitDecision`: the Job is worth continued
  attention or later action. It is not a QuickScreen pass, a DeepFitSelection, an
  ApplicationPreparation, or an external application. Do not extend this capability now and do not
  add a bookmark entry point, saved list, or new UI around it. DeepFitSelection is a one-run input;
  ApplicationPreparation means real preparation has begun. Under S37.1, do not carry old Shortlisted
  behavior into v1 solely for code compatibility. Pursuit/bookmark UX and any PursuitDecision
  contract remain a separate future design, not a required legacy feature.
- **Rationale:** Long-term Job collection is not required for the current product loop. Expanding it
  now would blur screening, analysis selection, preparation, and application facts again.
- **Deferred detail:** Future Job-pool UX and the relationship between bookmark/follow behavior and
  `PursuitDecision`.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `progress.md`

### Q24 — Resume Advisor without mandatory DeepFit

- **Status:** `ACCEPTED`
- **Decision:** DeepFitAnalysis is not a Resume Advisor prerequisite. Resume Advisor uses exact
  JobVersion, RequirementSet, ResumeVersion, and relevant Evidence as authoritative input and
  independently produces resume-expression coverage, grounding, and suggestions. A DeepFitAnalysis
  may be reused only when compatible with the current JobVersion, RequirementSet, and Candidate
  Evidence. It adds confirmed matches, risks, and Evidence conclusions but cannot gate resume
  improvement. Complete Candidate Fit plus `MISSING`/`UNKNOWN` and whole-Job fit judgments remain
  exclusively owned by DeepFit.
- **Rationale:** Resume expression can be analyzed and improved from Requirements, the edited
  Resume, and Evidence without first paying for a complete Candidate Fit analysis.
- **Rebuild impact — S37.1:** Do not preserve the old implementation's mandatory DeepFit-lineage
  dependency or build a compatibility reader/migration for it. Implement the effective independent
  Fit and Advisor contracts; their own exact-input lineage remains required.
- **Refined by:** Q58. Job-targeted Resume Advisor obtains RequirementSet through the same shared
  `EnsureRequirementSet` Use Case as DeepFit rather than depending on a prior DeepFit run.
- **Further refined by:** Q65. DeepFit now includes a Resume-presented primary view as well as a
  Candidate-Knowledge potential view; Resume Advisor still owns the generation of grounded resume
  changes and remains independently callable.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `progress.md`

### Q25 — Mutable preparation and frozen execution snapshot

- **Status:** `ACCEPTED`
- **Decision:** `ApplicationPreparation` is a mutable pre-submission draft, not a versioned Aggregate
  that records every edit. The user may freely change the selected ResumeVersion, greeting, and
  other Job-specific material. Adopting DeepFit or Resume Advisor output updates current preparation
  content without preserving changes that have no external business significance. Clicking
  "confirm and begin application" freezes the exact JobVersion, ResumeVersion, greeting/material,
  render, and other execution inputs into an immutable `ApplicationExecutionSnapshot` or
  `ExecutionAttempt`. Browser Executor may execute only that snapshot. A verified external action
  or explicit human report then creates an ApplicationRecord referencing the frozen attempt. A
  later application to the same Job creates a new Preparation/Attempt and never overwrites the
  earlier application history.
- **Rationale:** The audit boundary is what was actually authorized and used externally, not every
  reversible draft choice made before authorization.
- **Refines:** Q16's separation of Candidate assets, preparation, and real applications.
- **Deferred detail:** Final naming and identity constraints for `ApplicationExecutionSnapshot`
  versus `ExecutionAttempt` belong to the Application/Execution contract review.
- **Greeting refinement — Q157:** Preparation owns one editable Greeting field initialized from
  fixed generic product text, without personalization/model invocation, independent root/version
  history, template library, or Skill. Edits use Preparation CAS. MaterialApproval freezes actual
  viewed text/hash and edits require reconfirmation; ExecutionSnapshot freezes actual send text.
- **Reentry — Q162:** Apply entry defaults to resuming an unfinished Preparation for that Job/
  channel, preserving selections and manual Greeting. Revalidate eligibility/readiness/approvals
  without silently replacing exact inputs. Refresh/retry is creation-idempotent; explicit new
  preparation and later real reapplication create separate chains; multiple candidates need user choice.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q26 — Normative contracts versus current implementation

- **Status:** `ACCEPTED`
- **Decision:** `contracts/*.md` contains normative target contracts: business/data rules, authority,
  identity, versioning, interfaces, validation and invariants. Future evolution must keep new-system
  historical references interpretable; S37.1 removes mandatory old-code/schema interpretation and
  migration from the initial rebuild. Contracts exclude transient API availability, test counts and
  implementation progress. `progress.md` tracks implementation and gaps against the new baseline,
  without inheriting old completion claims. Important
  contract requirements receive stable IDs such as `JOB-ID-001` or `APP-RECORD-002`. A lightweight
  Traceability Matrix maps `Contract ID → implementation → test → status`, while Progress references
  those IDs with `Implemented / Partial / Planned / Deferred`.
- **Rationale:** Contract describes what the system must be; Progress describes how much of it exists
  now. Stable IDs preserve traceability without contaminating normative documents with volatile
  state.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`,
  `progress.md`

### Q27 — BossHunter and boss-zhipin-scraper authority

- **Status:** `ACCEPTED`
- **Decision:** Treat BossHunter and `boss-zhipin-scraper` as research and implementation inputs, not
  upstream JobHunter specifications. BossHunter informs BOSS acquisition flow, filtering, field
  coverage, risk controls, and application UX. `boss-zhipin-scraper` informs BOSS payloads, source
  identity, extraction, pagination, throttling, authentication, and risk behavior and may later be a
  reused third-party dependency. Any reused module remains behind a JobHunter-owned Adapter/Port:
  raw output is runtime-validated into an adapter DTO before canonical Job/JobVersion creation;
  third-party field names, state, and temporary tokens cannot enter Domain. Before detailed Job Contract
  review, pin the studied commits, record license and maintenance status, inventory fields, and map
  `raw source field → adapter field → canonical field`. A field needs a real JobHunter consumer to
  enter Canonical Contract and receives no model visibility merely because a dependency exposes it.
- **Rationale:** External repositories provide evidence about the source and useful implementation
  patterns, while JobHunter product needs and real validated data remain canonical authority.
- **Formal writeback:** `spec.md`, `architecture.md`, `development.md`, `contracts/*`, `progress.md`

## Round 5 Batch Supplements

### S5.1 — Flat Job pool with optional Company view

- **Status:** `ACCEPTED`
- **Decision:** The Job pool defaults to a flat Job list with city, industry, recruitment type,
  update time, keyword, and other filters. It may switch to a Company aggregation read model whose
  rows summarize Job count, main cities, and role directions. Selecting a Company returns to the
  ordinary Job list with a company filter. Company view does not create Company Domain authority or
  a Company Aggregate.
- **Rationale:** Company is a useful browsing dimension, but a conventional company dropdown does
  not scale and the current business has no independent Company lifecycle.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`

### S5.3 — DeepFit and Resume Advisor product placement

- **Status:** `ACCEPTED`
- **Decision:** DeepFit is a Job-side batch analysis capability inside the Job pool, not primary
  navigation. The user filters Jobs, enters DeepFit selection mode, and starts one independent
  DeepFitRun per explicitly selected Job. QuickScreen remains the background deterministic hard
  filter. Resume Advisor is a Resume-side capability with both an independent entry point and a
  contextual entry from ApplicationPreparation. The contextual entry passes JobVersion,
  RequirementSet, ResumeVersion, relevant Evidence, and optional compatible DeepFitAnalysis to the
  same underlying Resume Advisor Use Case. Do not build separate Advisor implementations per entry
  point.
- **Rationale:** Product entry points should reflect whether a capability analyzes Jobs or edits
  resume expression while Application uses one shared business capability underneath.
- **Deferred detail:** Resume Advisor UI form, including preview/chat layout, conversation history,
  suggestion diff, and version switching, awaits Resume Advisor Contract and UI/UX review.
- **Refined by:** S17.2-S17.3 fix the five navigation entries and route both Advisor modes to
  求职助手. Job-targeted entry comes only from a specific Job's preparation; General entry comes
  from Resume-side actions or the Assistant navigation. Preparation has no top-level navigation.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 6 — Hard Filtering, Execution Authority, Events, and Traceability

### Q30 — Snapshot, authorization, attempt, and real application

- **Status:** `ACCEPTED`
- **Decision:** The user selects one or more Jobs in the Job pool and enters application preparation.
  Each selected Job's preparation permits adjustment of ResumeVersion, greeting, and other
  materials. Completion freezes exact JobVersion, channel/account, ResumeVersion,
  greeting/material, RenderManifest, and hashes into an immutable
  `ApplicationExecutionSnapshot`. The Snapshot answers what will be submitted and grants no
  authority. An explicit "confirm and begin application" action creates a scope-bound, expiring,
  single-use `ExecutionApproval`. Browser Executor consumes it to create one `ExecutionAttempt`
  recording run status, timing, verified steps, and technical outcome. One Approval can be consumed
  by at most one Attempt. `PARTIAL` continuation requires a new narrower Approval;
  `OUTCOME_UNKNOWN` cannot automatically retry and requires external-state confirmation.
  MaterialApproval accepts content but is not execution authority. A manual external application
  creates a human-reported ApplicationRecord without fabricated Snapshot, Approval, or Attempt.
- **Rationale:** Frozen input, user authorization, bounded execution, and real-world application
  facts have different authority and failure semantics.
- **Execution check boundary — Q164:** Necessary live identity/availability checks stay within
  authorization and PlatformAccessSafety, not implicit JobVersion refresh, Requirement parsing or
  Snapshot replacement. Clear execution-relevant mismatch stops further actions for explicit
  refresh/repreparation; no added LLM Job-analysis step.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q31 — ExecutionEvent versus ApplicationEvent

- **Status:** `ACCEPTED`
- **Decision:** Strictly separate technical `ExecutionEvent` values from business
  `ApplicationEvent` values. Browser Executor records actions and observations such as opening a
  page, clicking communication, entering a greeting, submitting, and reading page state. None
  directly advances Application progress. Application Service creates a business event only after a
  channel-specific reliable read-back proves the real outcome. For BOSS, the first verified greeting
  normally produces `CONTACTED`; later verified material sending, formal application, or reply
  produces distinct `MATERIALS_SENT`, `APPLIED`, or `REPLIED` events according to versioned channel
  policy. Explicit failure yields a failed Attempt and no success event. An action with an
  unverifiable final outcome yields `OUTCOME_UNKNOWN`, no success event, and no automatic retry.
  Manual external actions create `HUMAN_REPORTED` ApplicationEvents and do not invent Executor
  history.
- **Rationale:** ExecutionEvent answers what the system did and observed; ApplicationEvent answers
  what was reliably established in the external business process.
- **Research dependency:** Before formal writeback of BossHunter-specific verification details,
  inspect and pin the referenced BossHunter commit. The accepted JobHunter invariant does not depend
  on that repository: only platform read-back or explicit human report may establish the business
  fact.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`,
  `development.md`

### Q32 — Traceability Matrix under Progress

- **Status:** `ACCEPTED`
- **Decision:** Maintain the lightweight current-state matrix at
  `docs/progress/traceability.md`, inside the Progress document category rather than as a seventh
  top-level authority or inside normative Contracts. Contracts define stable IDs and requirements;
  the Matrix references each ID and maps it to implementation, tests, and one of `Implemented`,
  `Partial`, `Planned`, or `Deferred` without copying contract prose. Each implementation Slice must
  update affected rows. Later extend `./scripts/check` to verify ID uniqueness, valid Matrix
  references, and required mappings. File existence cannot automatically establish `Implemented`;
  Slice acceptance remains authoritative for status. `progress.md` remains a concise summary of the
  current Slice, overall state, major blockers, and next step.
- **Rationale:** Detailed traceability needs room to grow without making either normative contracts
  or the rolling summary volatile and unreadable.
- **Formal writeback:** `development.md`, `contracts/*`, `progress.md`,
  `docs/progress/traceability.md`

## Round 7 — Collection Filtering, Requirements, Batches, and Application History

### Q35 — Durable headless DeepFitBatch

- **Status:** `ACCEPTED`
- **Decision:** Keep a lightweight durable `DeepFitBatch` orchestration record. It is a background
  run record, not a chat Session or business Aggregate. The user filters and selects Jobs, then the
  system freezes batch membership and creates one independent DeepFitRun/AgentRun per Job. DeepFit
  is headless, workflow-triggered, and fully automatic; it requires no user messages or HITL
  conversation. The Batch records selected JobVersion members, batch budget and concurrency policy,
  child run IDs, overall run status, and created/cancelled/completed timestamps for progress,
  cancellation, recovery, and cost audit. Child failures do not roll back other analyses, and each
  DeepFitAnalysis remains independent business authority.
- **Rationale:** Batch control needs durability and observability, while fit semantics, context,
  budgets, and failures must remain isolated per Job.
- **Refined by:** S12.1. Each DeepFit child also binds the exact Resume/Evidence scope selected for
  that analysis; batch membership alone does not select Candidate Knowledge implicitly.
- **Further refined by:** Q63 and Q65. Evidence is Workspace-global, while every child freezes the
  selected ResumeVersion and exact CandidateKnowledgeSnapshot needed for the two DeepFit views.
- **Refined by Q110-Q112:** A Job child prepares shared RequirementSet dependencies, then schedules
  independently selected Candidate Fit and Resume Fit tasks with isolated outcomes. One Job does not
  imply one shared semantic AgentRun for both analyses.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q36 — Batch application UX with per-Job business isolation

- **Status:** `ACCEPTED`
- **Decision:** Batch application is only a UI/orchestration operation. The user may select multiple
  Jobs, enter preparation once, and confirm a batch, but the business layer creates an independent
  `ApplicationPreparation → ApplicationExecutionSnapshot → ExecutionApproval → ExecutionAttempt →
  optional ApplicationRecord` chain for every Job. Each Job independently selects or inherits
  Resume/greeting/material, performs stale checks, authorizes, executes, fails, cancels, and audits.
  A bulk confirmation may create multiple approvals, but every approval binds one exact
  Snapshot/Job and remains single-use. The batch controls membership, presentation, scheduling,
  concurrency, and progress only; it is not a transaction boundary. A CAPTCHA, platform-risk, or
  account anomaly may trip a channel-level circuit breaker and halt later dispatches. Undispatched
  Jobs remain `not_started`, `pending`, or `cancelled_before_execution`; they cannot be marked failed
  or applied.
- **Rationale:** Batch UX must not become batch business consistency. Every real external action has
  independent frozen input, authority, outcome, and history.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q37 — Event-sourced ApplicationRecord progress

- **Status:** `ACCEPTED`
- **Decision:** One stable ApplicationRecord identity represents one real application attempt for one
  Job and one channel/account. Reapplying to the same Job/channel creates a new record. Each record
  owns append-only ApplicationEvents such as `CONTACTED`, `REPLIED`, `MATERIALS_SENT`, `APPLIED`,
  interview events, `REJECTED`, `OFFER_RECEIVED`, and `WITHDRAWN`; channels need not share one linear
  sequence. External facts deduplicate by source/idempotency identity. Late events retain both fact
  occurrence time and system observation time. Corrections append `EVENT_CORRECTED` or
  `EVENT_RETRACTED` rather than deleting history. Versioned ApplicationProgressPolicy derives
  `current_progress` for reads/UI and decides whether terminal events stop later automatic actions;
  the projection is not independently writable authority.
- **Rationale:** Real channels produce non-linear, delayed, duplicate, and corrected observations;
  an overwrite-only status cannot preserve or explain them.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 7 Batch Supplement

### S7.1 — Shared Harness with Skill-specific interaction policy

- **Status:** `ACCEPTED`
- **Decision:** DeepFit and Resume Advisor share one Agent Harness infrastructure—Runtime, Context,
  Tool Registry, Model Gateway, Budget, Cancellation, and Audit—but have separate static Skill
  contracts for context, allowed tools, budgets, output schemas, and interaction policy. DeepFit is
  a non-conversational automatic analysis Skill. Resume Advisor is currently the principal Skill
  allowed to expose natural-language, potentially multi-turn resume optimization. Research existing
  open-source resume-optimization/tailoring Skills for prompt, workflow, JD targeting, rewrite, and
  interaction patterns, but treat them only as research/implementation input. JobHunter's Evidence
  grounding, no-fabrication rule, Context admission, HumanChoice, and lineage remain authoritative.
- **Rationale:** Shared execution infrastructure does not imply shared product interaction or weaken
  business-specific contracts.
- **Deferred detail:** Specific Resume Advisor research projects, pinned versions, UI conversation
  model, and multi-turn persistence await its Contract and UI/UX review.
- **Refined by Q120-Q121:** RequirementParse, CandidateJobFit, ResumeJobFit, and ResumeAdvisor have
  separate Skill Contracts on one Harness. Registered Tools are not automatically exposed; actual
  actions require Skill, Context-strategy, and runtime admission. Agentic retrieval is post-v1.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 8 — Uncertain Collection, Pre-Version Jobs, Frozen Analysis, and Mutable Preparation

### Q40 — Frozen DeepFit child input and stale rejection

- **Status:** `ACCEPTED`
- **Decision:** DeepFitBatch freezes every child request's exact JobVersion, RequirementSet,
  QuickScreenResult, Context/Evidence versions, PolicyVersion, and budget. It never silently replaces
  those inputs. Immediately before dispatch, revalidate that QuickScreen remains non-REJECT, the
  JobVersion/RequirementSet remain applicable, and Context/authorization remain valid. Stale input
  ends the child as `STALE_INPUT` before model invocation and is not an analysis failure. UI creates
  a new batch member from current inputs rather than editing the original Batch. If a model call has
  occurred and final T2 validation finds stale Evidence or other authority, preserve invocation,
  usage, and audit but do not persist a new DeepFitAnalysis. Batch summaries distinguish completed,
  failed, cancelled, stale, and outcome-unknown children.
- **Rationale:** Queue delay and concurrent mutation must not cause an analysis to run against an
  unrecorded mixture of old and new authority.
- **Refined by:** Q62 and S12.1. The frozen input uses exact Resume-scoped EvidenceVersion and
  Assertion references; a later active Evidence version makes an undispatched child stale rather
  than silently upgrading it.
- **Supersession note:** Q63 replaces Resume-scoped ownership with an exact Workspace
  CandidateKnowledgeSnapshot; the exact-reference and stale-input rules remain accepted.

- **Current correction — Q108/Q110/Q112:** Batch creation freezes known selected inputs, not a
  placeholder RequirementSet. Freeze the complete per-analysis request only after dependency
  preparation. Current-fact changes are revalidated for the affected task; no historical-version
  Overlay or silent input upgrade is permitted. The two Fit tasks remain independent.
- **Mid-run revocation — Q172:** If authorization for a protected EAGER_EXACT input is revoked
  after freeze, end the affected task fail-closed rather than silently reducing scope. No later
  Frame/repair/Tool consumes revoked input or publishes valid current Analysis. A requested new
  admitted scope needs a new task. Initial exclusions retain existing UNKNOWN semantics; prior
  transmission cannot be undone and necessary usage/recovery/audit stays truthful.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q41 — Resume Advisor conversation has no mutation authority

- **Status:** `ACCEPTED`
- **Decision:** Advisor messages express intent and may include user-stated Session facts; discussion
  alone cannot mutate Candidate Knowledge or an immutable ResumeVersion. Q138 suggestions distinguish
  saved EvidenceRef from verified SessionContextRef/UserTurnRef, with requirement/intent and rationale.
  Explicit Save promotes relevant Session facts through the controlled Application path and creates
  formal facts/Resume grounding, never an in-place overwrite. Fit remains saved-authority-only.
- **Rationale:** Advisor optimizes the expression of confirmed facts; conversation is not a hidden
  Candidate Knowledge or Resume write boundary.
- **Deferred detail:** Conversation retention, deletion, redaction, instruction lineage/hash, and
  EvidenceDraft interaction await Resume Advisor and privacy contract review.
- **Refined by:** Q85 introduces a mutable Advisor working draft and explicit promotion into
  Candidate Knowledge. S17.3 retains Suggestion/HumanChoice/new-version and grounding boundaries.
  Q108 resolves the draft boundary: formal Save is required before export/application; editing alone
  does not give model-generated facts authority.
- **Current correction — Q128:** Chat text/model parameters alone still cannot mutate facts.
  After the user explicitly confirms a proposed fact addition/correction, an actually authorized
  typed Tool may invoke Application's UpdateCandidateKnowledge and its atomic Resume propagation.
  A separate manual Draft-page visit is not the only permitted route. Q108 prohibits temporary-draft
  export/application without formal Save.
- **Scoped supersession — Q133/Q134:** Unsaved user-stated facts may immediately inform Session-local
  discussion and proposed wording; they need not first become EvidenceDraft/authority. Formal Fit
  and persisted business facts still require saved inputs. Explicit, unambiguous Save intent can
  authorize the controlled write without a redundant second confirmation. Append actual committed
  inputs to new Frames after admission; never rewrite historical outputs.
- **Scoped supersession — Q146:** Advisor has discussion and Suggestions, not ResumeDraft or a
  persistent working draft. Draft belongs only to My Resumes page CRUD. Formal apply resolves a
  user-specified Resume or Workspace default, previews concrete shared-fact/current-Resume impact,
  receives one confirmation, and immediately commits through UpdateCandidateKnowledge. Earlier
  draft/promotion clauses in this record are historical only; no extra draft Save follows.
- **Formal proposal refinement — Q148-Q149:** Only the actual apply target is selected: current
  instruction's explicit Resume, otherwise Workspace default. Read its exact version and generate
  its own before/after ChangeProposal; do not infer a suggestion-source Resume or transplant another
  Resume's patch. Preview target/version/default status, fact changes, and affected current Resumes.
  One confirmation binds that complete Proposal; target/patch changes or revision conflicts require
  a new preview. Ordinary exact input lineage remains, not an extra source-selection concept.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q42 — Concurrent mutable ApplicationPreparation

- **Status:** `ACCEPTED`
- **Decision:** ApplicationPreparation is a mutable root with optimistic concurrency and derived
  readiness, not immutable edit history. It stores the current preparation ID/revision, selected
  ResumeVersion, current greeting/material references, current RenderManifest, and update time.
  Every mutation supplies expected revision and fails explicitly on stale write. Replaced selections
  are not recorded as preparation history, while independently immutable ResumeVersions,
  MaterialBundles, RenderManifests, artifacts, and their audit remain. Channel policy derives
  readiness from current Resume, greeting, materials, validation, render, and valid
  MaterialApproval. Async render/output becomes current only if it still matches the relevant
  preparation revision and references; stale output retains artifact/audit but cannot advance the
  current pointer. ApplicationExecutionSnapshot creation atomically revalidates revision,
  references, approvals, and hashes before freezing. Later Preparation edits cannot mutate a frozen
  Snapshot.
- **Rationale:** Draft editing needs concurrency safety and consistent current references, while only
  actual immutable assets and external execution inputs require durable historical identity.
- **Material confirmation refinement — Q150:** Confirm actual displayed frozen artifact/hash and
  source lineage, not just Resume identity/version. Required rendering precedes confirmation; new
  selected material requires compatibility validation. Equal hashes cannot bypass current fact
  eligibility. Historical artifacts and execution Snapshots are never replaced in place.
- **Greeting refinement — Q157:** Preparation owns one editable Greeting field initialized from
  fixed generic product text, without personalization/model invocation, independent root/version
  history, template library, or Skill. Edits use Preparation CAS. MaterialApproval freezes actual
  viewed text/hash and edits require reconfirmation; ExecutionSnapshot freezes actual send text.
- **Reentry — Q162:** Apply entry defaults to resuming an unfinished Preparation for that Job/
  channel, preserving selections and manual Greeting. Revalidate eligibility/readiness/approvals
  without silently replacing exact inputs. Refresh/retry is creation-idempotent; explicit new
  preparation and later real reapplication create separate chains; multiple candidates need user choice.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 9 — Job Materialization, Preferences, DeepFit Scoring, and Advisor Sessions

### Q44 — Unified complete-JobVersion rule

- **Status:** `ACCEPTED`
- **Decision:** Job is a stable source identity and may exist before JobVersion; JobVersion is an
  immutable canonical snapshot complete enough for semantic analysis and downstream binding. For a
  Manual source, create Job from a system-generated stable manual source ID plus current metadata.
  Without JD, keep the Job, expose `description_availability`, and allow Job-pool display, Tracking,
  and human-reported applications, but do not create JobVersion. Supplying a JD or sufficiently
  complete verified details creates the first JobVersion. BOSS and Manual sources use the same
  completeness principle: RequirementSet, DeepFit, and Job-targeted Resume Advisor require a valid
  JobVersion with complete JD.
- **Rationale:** A single semantic contract avoids source-specific meanings of JobVersion while
  allowing lightweight manual record keeping.
- **Scope resolved by:** Q48. Automatic BOSS collection requires complete details/JD at persistence;
  explicitly supported Manual sources may persist metadata-only Job roots without JobVersion.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q45 — Every configured Preference is hard

- **Status:** `ACCEPTED`
- **Decision:** PreferenceSet does not distinguish HARD and SOFT. Every explicitly configured Job
  preference is a hard requirement. Before first automatic collection, the user configures required
  dimensions such as target role direction, city, salary, recruitment type, work mode, and company
  blacklist. An unset dimension means no restriction; the system invents no default preference.
  PreferenceSet both derives BOSS-expressible search parameters and drives local deterministic
  QuickScreen against list metadata. Only a confirmed conflict yields REJECT; missing source data
  remains UNCERTAIN. The system reuses the current PreferenceSet across collections. An explicit
  user change creates a new PreferenceSetVersion and recomputes local visibility and related
  QuickScreen results. Temporary Job-pool keywords, sorting, and view filters never mutate
  PreferenceSet.
- **Rationale:** A configured preference is an enforceable acquisition constraint, while ad hoc
  exploration belongs to local view state.
- **Rejects:** The HARD/SOFT criterion model proposed in Q45's recommendation.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q46 — Policy-derived DeepFit score

- **Status:** `ACCEPTED`
- **Decision:** The model produces evidence-grounded RequirementAssessments rather than authoritative
  total scores. Assessments include requirement type, `MATCHED / PARTIAL / MISSING / UNKNOWN`,
  Evidence strength and references, risks, and explanation. Versioned `DeepFitScorePolicy`
  deterministically aggregates stable dimensions such as core responsibilities, hard requirements,
  transferable capabilities, and bonus/domain context, then derives score, coverage, and priority
  with hard-gap caps, unknown counts, and risks. `UNKNOWN` is not `MISSING` and cannot be naively
  assigned a fixed low score. Critical missing requirements cannot be offset by many minor matches.
  The 0-100 score is sorting/UI summary only; Fit authority remains RequirementAssessments,
  Evidence, hard gaps, risks, and coverage.
- **Rationale:** Deterministic policy preserves explainability, reproducibility, and recalibration
  without granting the model an opaque ranking authority.
- **Deferred detail:** Dimension weights, PARTIAL treatment, caps, thresholds, and priority bands
  await real Job data and user ranking feedback and are versioned rather than frozen now.
- **Current correction — Q112:** Candidate Fit and Resume Fit have independent assessments and
  scores. There is no capability-times-expression score, durable Resume Coverage score, score gap,
  or guaranteed ordering between them. Any assessment-completeness metric must not reintroduce
  the removed Resume-versus-Knowledge coverage ratio. Numerical tuning remains deferred.
- **Score availability — Q168:** Valid assessments/reasons/lineage may be persisted without a
  comparable total score or normal score ranking when deterministic ScorePolicy cannot justify one.
  Unavailable is not zero, failed Analysis, or permission to label an old result's score as this
  result. Score availability thresholds/representation remain later Contract work.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q47 — ResumeAdvisorSession, Turn, AgentRun, and AgentLoop

- **Status:** `ACCEPTED`
- **Decision:** The unified ChatSession is durable product interaction state, not a waiting Agent
  process. It preserves current Resume/Job scope, admitted conversation history/summary, accepted
  Suggestions, and produced ResumeVersions. Each new user request creates one Turn and one bounded
  AgentRun with its own ContextFrame, budget, deadline, tool calls, hooks, audit, and outcome. A
  bounded `LLM → Tool → LLM → ... → final response` AgentLoop may occur inside that Run, which ends
  after the response and never waits for the next user message. A later Run reconstructs context
  from Session state through Memory/History Projection and Context admission, using current explicit
  ResumeVersion, JobVersion/JD/RequirementSet, relevant Evidence, accepted Suggestions, bounded
  recent conversation, and summary. Scope changes are explicit, never silent. Chat messages remain
  interaction context and do not become Evidence or Preference authority.
- **Rationale:** Session supplies semantic continuity while each Run remains bounded, auditable,
  cancellable, and independently reconstructable.
- **Cross-skill rule:** DeepFit normally uses no Session (`one Job → one AgentRun → one bounded
  loop`); Resume Advisor uses `one Session → many Turns → many AgentRuns` through the shared Harness.
- **Current refinement:** Q83 assigns one immutable Frame per ModelInvocation; Q89-Q90 use one
  ChatSession without Session compatibility or a separate Job-targeted Session type. Q139 uses
  explicit business references and LAZY_TOOL acquisition, not eager business-body injection.
  Durable history, bounded Runs, current validation, and explicit scope remain.
- **Foreground serialization — Q155:** At most one active foreground Turn per ChatSession.
  New input waits or explicitly stops the current Turn before starting; different Sessions and
  independent dependency/auxiliary/background AgentRuns can run in parallel. Two user Turns cannot
  concurrently advance the same Session Context/business state.
- **Wait distinction — Q158-Q159:** Proposal generation/display ends that Turn/Run; pending human
  confirmation is Application state and exact command validation, not a live Agent. Advisor's
  independent RequirementParse dependency wait keeps the same foreground Turn active, releases
  model/Provider execution capacity, and retains deadline/cancel and Q142 owner/waiter semantics.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 9 Batch Supplement

### S9.1 — Persistent local Job dataset and explicit refresh

- **Status:** `ACCEPTED`
- **Decision:** JobHunter maintains a persistent local Job dataset rather than visiting BOSS whenever
  the Job pool opens. BOSS access happens after initial Preference setup or an explicit "fetch latest
  Jobs" action. Collector derives platform search conditions from Preference, obtains list metadata,
  and QuickScreens transient adapter DTOs. REJECT candidates are skipped and not persisted in the
  local Job dataset. PASS/UNCERTAIN candidates fetch detail and full JD; only successfully completed
  candidates become persistent Job/JobVersion data. Daily browsing and Preference changes operate
  against local data first; Preference changes never delete Jobs already admitted. Another BOSS
  request occurs only when the user explicitly refreshes. The Job pool displays freshness such as
  `fetched_at / last_fetched_at` so the user knows when platform data was obtained.
- **Rationale:** Local persistence makes normal browsing immediate and reduces repeated platform
  traffic, detail requests, and account-risk exposure. Explicit refresh keeps external access under
  user control.
- **Supersedes:** Q28/Q38 filtered-view persistence for rejected BOSS candidates, Q39/Q43 persistent
  pre-version BOSS Jobs, and Q33's durable filtered observation.
- **Preserves:** Only confirmed REJECT stops detail acquisition; PASS and UNCERTAIN continue. Jobs
  already admitted remain durable even if a later PreferenceSet filters them from the current view.
- **Scope resolved by:** Q48. The complete-details admission rule applies to automatic BOSS
  collection; Manual Job may persist metadata-only under the shared Job Contract.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 10 — Source Admission, Collection Safety, Freshness, Rescoring, and Chat Persistence

### Q48 — Source-specific admission under one Job Contract

- **Status:** `ACCEPTED`
- **Decision:** The local Job dataset may contain a Job without JobVersion only for a source whose
  ingestion policy explicitly supports it, initially Manual. Job always represents stable source
  identity; JobVersion always represents an immutable canonical snapshot complete enough for
  Requirement parsing, DeepFit, and Job-targeted Resume Advisor. BOSS persists `Job + first
  JobVersion` atomically only after detail/JD validation and cannot create a metadata-only durable
  Job. Manual may persist a Job root with empty `active_version_id` for Tracking or human-reported
  Application, then create its first JobVersion when the user supplies JD. Both use one Job Contract;
  source changes admission policy, not JobVersion meaning. `analysis_readiness` is a derived read
  projection, not Job lifecycle state.
- **Rationale:** The product retains low-friction Manual tracking without weakening the quality and
  completeness guarantees of automatically collected BOSS Jobs.
- **Resolves:** Q44 and S9.1's Manual scope ambiguity.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q49 — Two-stage BOSS collection and platform safety guard

- **Status:** `ACCEPTED`
- **Decision:** Automatic BOSS collection uses two stages. Search/list metadata is QuickScreened
  against exact PreferenceSetVersion. REJECT stops without detail access, Job creation, or durable
  rejected-listing content. PASS/UNCERTAIN consumes detail access; only a complete validated result
  meeting required BOSS fields such as title, company, URL, and JD atomically creates Job plus first
  JobVersion. Collection safety is measured primarily in platform page access, separately tracking
  search/list access, detail attempts, and shared platform access—not the number of Jobs saved.
  Platform risk signals such as CAPTCHA, verification, rate limit, access denial, account restriction,
  or login loss override all remaining budgets and immediately stop the CollectionRun. Consecutive
  page/load/parse failures also stop at a versioned threshold. Never increase concurrency, switch
  tabs/accounts, bypass controls, or silently resume after cooldown; another external access requires
  an explicit later user action.
- **Collection audit:** CollectionRun records PreferenceSetVersion, Collector/PolicyVersion, a search
  parameter summary, search/detail/global access usage, scanned/PASS/UNCERTAIN/REJECT aggregates,
  rejection-reason aggregates, failures, duration, risk event, and final stop reason. It is run/audit
  data, not Job authority, and does not retain rejected title/company/URL/JD. A temporary stable hash
  may support within-run deduplication but cannot recover the Job later. User-visible failures explain
  the stop, retained completed data, and need for manual retry after cooldown.
- **Rationale:** Page access and platform risk—not saved result count—represent the real safety cost.
  Aggregate audit preserves operational explainability without building a rejected-Job database.
- **Operational research reference:** BossHunter values mentioned during the Grill-Me session—60
  search pages/day, 150 detail attempts/day, 500 shared accesses/day, delay multiplier 1.5, three
  consecutive failures, and a 5–10 minute risk cooldown—are research candidates only. Pin and inspect
  the exact upstream commit before formal citation. They are not BOSS official limits, Domain
  invariants, or frozen JobHunter defaults.
- **Shared safety refinement — Q160:** All recruiting workflows use persistent PlatformAccessSafety
  by (platform, account), aggregating access and risk. Ordinary page/selector/browser failures may
  stop their workflow but are not automatically account risk. Predictable capacity may recover by
  policy; strong risk is BLOCKED_REQUIRES_USER with explicit user restoration, no cooldown-only
  recovery or bypass. Safety admission never grants execution approval. Earlier undifferentiated
  cooldown/risk wording does not override this distinction or imply automatic stopped-Run restart.
- **Preference/cancellation refinement — Q161:** A Run retains its frozen PreferenceSetVersion.
  Updated Preferences immediately govern current local re-filtering and future Runs, not this Run's
  rules. User stop retains committed Jobs as partial results; no automatic recollection or deletion.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q50 — Freshness and availability are separate projections

- **Status:** `ACCEPTED`
- **Decision:** `JobVersion.captured_at` records when canonical content was obtained;
  `Job.last_seen_at` records the last reliable source listing observation;
  `Job.last_verified_at` records the last direct detail/availability verification. Versioned
  FreshnessPolicy and AvailabilityPolicy derive `ACTIVE / STALE / CLOSED / UNKNOWN`; these outcomes
  are not inferred merely from timestamps stored as state. A refresh with semantically unchanged
  canonical content updates operational timestamps without creating JobVersion. A normalized/hash
  semantic change in JD, responsibilities, requirements, salary, or other canonical content creates
  a new immutable JobVersion and advances the active pointer. Age can produce STALE but not CLOSED.
  Absence from one search result is only CollectionRun observation, not closure. CLOSED requires a
  stronger verified source observation such as explicit removal or stopped recruitment. Closure
  never deletes Job or downstream history and prevents new automatic application. Manual Job
  availability defaults to UNKNOWN and user reports remain distinguishable from source verification.
- **Rationale:** Content history, observation recency, and source availability answer different
  questions and need different proof strength.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q51 — Original DeepFit score and explicit rescoring

- **Status:** `ACCEPTED`
- **Decision:** RequirementAssessments and Evidence grounding are authoritative DeepFit semantics;
  score, coverage, and priority are policy-derived. Every DeepFitAnalysis permanently retains its
  original score and original DeepFitScorePolicyVersion. A new Policy may deterministically produce
  an explicit ReScoreProjection from old assessments without model invocation or new
  DeepFitAnalysis. Job-pool comparison defaults to one common PolicyVersion; mixed analyses may be
  normalized by generating projections under one newer Policy. If required new dimensions are absent
  from old assessments, rescoring is unavailable rather than guessed. New semantic judgment requires
  a new DeepFitRun/Analysis.
- **Rationale:** Historical explanation and reproducibility coexist with later ranking-policy
  improvement without mutating model-derived evidence assessments.
- **Current correction — Q112:** Preserve original and rescored results separately for each
  independent analysis type and its exact inputs; neither score is derived from the other.
- **Score availability — Q168:** Valid assessments/reasons/lineage may be persisted without a
  comparable total score or normal score ranking when deterministic ScorePolicy cannot justify one.
  Unavailable is not zero, failed Analysis, or permission to label an old result's score as this
  result. Score availability thresholds/representation remain later Contract work.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q52 — Local chat persistence without frozen compaction design

- **Status:** `ACCEPTED`
- **Decision:** ResumeAdvisorSession persists local cross-Turn conversation state, including
  Message/Turn history, AgentRun references, Suggestion/HumanChoice references, and explicit current
  scope, but chat content is not Candidate Evidence, Preference, or other business-fact authority.
  Accepted Suggestions, HumanChoices, ResumeVersions, and Evidence lineage remain independently
  valid if the user deletes or cleans conversation content; new personal claims in chat never become
  Evidence automatically.
- **Rationale:** Multi-turn product continuity needs durable local session data, while business
  artifacts must not depend on retaining sensitive conversational prose.
- **Deferred context design:** Do not yet freeze recent-message selection, ConversationSummary,
  structured state, multi-layer compaction, artifact rehydration, token budgeting, summary updates,
  or whether summarization invokes a model. Harness Context Engineering will own how Session history
  becomes a later AgentRun's admitted ContextFrame. ConversationSummary is a possible derived
  representation, not a fixed ResumeAdvisorSession business contract.
- **Scope resolved by Q127:** Session persistence remains non-authoritative, but v1 now explicitly
  includes SessionSummary/recent-window compaction and separately admitted cross-session collaboration
  Memory. The prior session-only recommendation is not adopted. Detailed summary algorithms remain
  open; see [Memory module](harness/memory.md).
- **Compaction ownership correction — Q132:** Complete Session history remains durable. Context
  Engineering owns Context Compaction and ContextCheckpointSummary, not SessionSummary or a Memory
  layer. Its semantic invocation is auxiliary inside the current Run; see [Context](harness/context.md).
- **Session deletion — Q167:** Unconfirmed originating Proposals become ineligible, e.g.
  INVALIDATED_BY_SESSION_DELETE; old IDs/restored pages cannot confirm them. Cancel active foreground
  work. Confirmation/deletion atomically checks current Session/Proposal state and only one competing
  outcome succeeds. Already committed mutation results/formal assets remain; new modification needs
  a new Proposal in a valid context.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 11 — Candidate Roots, Preference Authority, Evidence Assertions, and RAG

### Q53 — No Candidate aggregate in the single-user local workspace

- **Status:** `ACCEPTED`
- **Decision:** JobHunter v1 is a single-user, local-first personal Job workspace and does not add a
  unified Candidate Aggregate, CandidateId, tenant scope, Candidate foreign keys on every table, or
  `/candidates/{candidate_id}` APIs. CandidateProfile, PreferenceSet, EvidenceItem, Resume, and
  ApplicationRecord remain independently identified/versioned long-lived assets. Their common
  ownership is implicit in the one-Workspace/one-Candidate product boundary. Add explicit ownership
  only through a later migration if accounts, multiple Candidates, Workspace import/export, or
  multi-tenancy becomes real scope.
- **Rationale:** v1 models the actual personal workspace rather than prebuilding a hypothetical
  multi-tenant root.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`

### Q54 — Versioned narrow CandidateProfile

- **Status:** `ACCEPTED`
- **Decision:** CandidateProfile is a stable root with `profile_id`, active version pointer, and
  optimistic-concurrency revision. Immutable CandidateProfileVersion owns identity, display, and
  contact authority. A change creates a new version and advances the pointer; old versions remain.
  ApplicationExecutionSnapshot may bind exact ProfileVersion or its rendered artifact so later
  contact changes cannot alter history. Profile answers only "who I am and how to contact me".
  Education, employment, projects, skills, and certificates belong to Evidence; role, city, salary,
  and work-mode intent belong to PreferenceSet. Contact data may enter local rendering but is
  model-invisible by default. Parsed Profile proposals require user confirmation before creating a
  new ProfileVersion. Immutable versions preserve business history; root revision only prevents
  concurrent-write loss.
- **Rationale:** Identity/contact, career facts, and job-seeking intent have different authority,
  privacy, and evolution semantics.
- **Deferred detail:** Exact name, nickname, phone, email, location, GitHub, Portfolio, and similar
  fields await Candidate Profile Contract/UI review.
- **Resolved by Q119:** Profile Save atomically propagates the new ProfileVersion into new current
  versions of referencing Resumes and their grounding while preserving field-display choices.
  Contact-only edits do not change career Evidence or its baseline; historical materials remain exact.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q55 — One global versioned PreferenceSet

- **Status:** `ACCEPTED`
- **Decision:** v1 has one global PreferenceSet root with stable identity, active version pointer,
  and optimistic-concurrency revision. Immutable PreferenceSetVersion contains the complete current
  hard constraints for automatic collection and QuickScreen. It may include multiple role
  directions in one version. Any explicit change creates a new version and triggers local
  re-screening. Every CollectionRun and QuickScreenResult references the exact version. Do not add
  named SearchProfiles, per-city/channel Preference sets, or automatic selection among configurations
  in v1. Add a SearchProfile layer only if genuinely parallel long-lived searches later require it.
- **Rationale:** One explicit active configuration keeps collection and screening reproducible and
  avoids an unneeded configuration-selection problem.
- **In-flight boundary — Q161:** CollectionRun keeps frozen Preferences; the Job Pool immediately
  uses the latest version for current filtering. Changes do not restart collection. User stop
  prevents subsequent accesses and retains all successfully saved Jobs, including those now unmatched.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q56 — Remove ScreeningProfileSnapshot from the target contract

- **Status:** `ACCEPTED`
- **Decision:** QuickScreen uses Job/source metadata, exact PreferenceSetVersion, and exact
  QuickScreenPolicyVersion. PreferenceSetVersion is already the immutable, traceable Candidate-side
  screening authority, so do not duplicate it as ScreeningProfileSnapshot. CandidateProfile,
  Evidence, Resume, and skill facts do not participate in QuickScreen eligibility. If a future
  low-cost stage needs a Candidate capability summary, introduce and review an explicit task
  projection rather than reviving an ambiguous snapshot. Under S37.1, the new implementation needs
  no legacy ScreeningProfileSnapshot reader or old-data migration. Two overlapping active
  screening authorities remain forbidden.
- **Rationale:** Removing the duplicate input prevents pointer drift and restores QuickScreen to a
  pure hard-preference gate.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `progress.md`

## Round 11 Batch Supplement

## Round 12 — Requirement Ownership, Evidence Completeness, and Resume-Scoped Knowledge

### Q58 — Shared on-demand RequirementSet generation

- **Status:** `ACCEPTED`
- **Decision:** Define Requirement generation as an independent Application Use Case such as
  `EnsureRequirementSet`, shared by DeepFit and Job-targeted Resume Advisor rather than owned by
  either. It receives exact JobVersion, RequirementParserVersion, and
  RequirementValidationPolicyVersion, reuses an existing compatible RequirementSet, or starts an
  independent auditable RequirementParseRun. The run parses `JobVersion.jd`, performs
  schema-constrained semantic extraction, and deterministically validates the result. General
  Resume Advisor work without a specific Job does not require RequirementSet.
- **Rationale:** Requirement parsing is a reusable semantic capability serving every consumer that
  needs structured JD semantics; Resume Advisor must remain independent of a previous DeepFit run.
- **Refines:** S11.1 and Q24.
- **Parser implementation resolved — Q111:** Shared EnsureRequirementSet invokes a bounded
  RequirementParse AgentRun: one LLM extraction plus at most one validation-guided repair.
  Deterministic code validates rather than interprets JD semantics. The shared Use Case remains
  available to Job-targeted Advisor without requiring Candidate Fit or Resume Fit to have run.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q59 — Immutable durable RequirementSet identity

- **Status:** `ACCEPTED`
- **Decision:** Every successfully parsed RequirementSet is an immutable durable derived asset with
  stable `requirement_set_id`, exact JobVersion, parser/model/prompt/schema/validation-policy
  versions, ParseRun, creation time, and Requirement identities. Any relevant parser or policy
  change creates a new Set rather than modifying an old one. A newer compatible Set may become the
  current default, while DeepFitAnalysis, ResumeSuggestion, ContextPackage, and other historical
  consumers permanently retain their exact Set reference. Old Requirement IDs never acquire new
  semantics through pointer movement.
- **Rationale:** Rebuildability describes provenance from JD; it does not remove identity,
  persistence, lineage, or immutable historical interpretation.
- **Refines:** Q10, Q14, Q34's surviving projection semantics, and S11.1.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 12 Batch Supplement

## Round 13 — Workspace Evidence, Resume Presentation, and Confirmed Baselines

### Q63 — Workspace Evidence authority and Resume selection/expression

- **Status:** `ACCEPTED`
- **Decision:** Career-fact authority is one Workspace-level Candidate Knowledge base, not owned or
  copied by individual Resume roots. One real education, employment, project, skill, certificate, or
  achievement is represented by one EvidenceItem lineage with immutable versions and version-local
  Assertions. A ResumeVersion is an immutable selection and expression snapshot containing exact
  EvidenceVersion/Assertion references, grounded ResumeClaims, wording, layout, and presentation.
  Different Resumes may select and emphasize different facts without creating private fact stores.
  CandidateProfile and the single PreferenceSet also remain Workspace-global. Candidate UI separates
  Resume management from Candidate Knowledge management; Resume provenance may be used as a filter
  but never as Evidence ownership. A future genuinely isolated career identity requires an explicit
  CareerProfile/KnowledgeScope rather than overloading Resume.
- **Import consequence:** First and later Resume imports create Resume plus imported ResumeVersion,
  then editable Profile/Evidence Drafts. Only explicit confirmation creates or updates Workspace
  Profile/Evidence authority. A later Resume import reconciles its Drafts against that shared
  authority. Updating Evidence never mutates an existing ResumeVersion; later ResumeVersions may
  choose new facts or newer Evidence versions.
- **Rationale:** Facts should not diverge merely because the same person maintains role-targeted
  Resume presentations. Resume remains expression; Evidence remains fact authority.
- **Supersedes:** S12.1's Resume-owned isolated Evidence stores and the Resume-ownership clause of
  Q61. Q65 supersedes Q63's initial suggestion that DeepFit's sole primary view is Candidate-level
  Fit; the Workspace Evidence ownership decision remains controlling.
- **Supersession note:** Q70-Q71 replace only the import sequence above: upload creates a mutable
  ResumeDraft, and no formal ResumeVersion exists until every factual claim is resolved and the save
  transaction succeeds. Workspace Evidence ownership remains controlling.
- **Selection refinement — Q163:** v1 Resume inclusion is whole EvidenceItem experience body from
  its current version, plus experience selection/order/layout. No independent per-Resume bullet
  selection mapping or alternate fact text. Fine EvidenceRef grounding and Profile display/privacy
  rules remain; they do not imply independently selectable career-body fragments.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q64 — Human-governed Evidence reconciliation across Resume imports

- **Status:** `ACCEPTED`
- **Decision:** EvidenceDrafts extracted from a second or later Resume are matched against Workspace
  Candidate Knowledge only as reconciliation candidates. The parser/matcher has no merge authority.
  Human Confirmation chooses among linking the Resume to an existing exact EvidenceVersion,
  creating a new immutable version of an existing EvidenceItem for confirmed additions/corrections,
  creating a new EvidenceItem, ignoring the Draft,
  or leaving it unresolved. Ambiguous/conflicting facts remain separate or unresolved by default;
  they are never automatically overwritten or merged. One EvidenceVersion may ground several
  ResumeVersions, but a later Evidence update never moves any old Resume, DeepFit, ContextPackage, or
  ResumeClaim reference. Each Resume adopts a newer EvidenceVersion only explicitly in a new
  immutable expression/grounding result.
- **Rationale:** Shared authority eliminates duplicate fact stores, while human-governed
  reconciliation prevents a parser from corrupting an existing career history.
- **Current body-edit rule — Q96-Q97:** Every formally saved body-text change versions affected
  Evidence; only presentation-only edits are exempt. Human reconciliation and immutable history remain.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`


### Q66 — Immutable snapshots of saved current Evidence

- **Status:** `ACCEPTED`
- **Decision:** EvidenceBaselineSnapshot freezes the exact current saved EvidenceItemVersion set
  without copying all Evidence data. A new Resume omitting an old fact does not delete that fact.
  Unsaved Draft work does not change the baseline; formal Save or explicit removal/invalidity changes
  the current set atomically. Historical snapshots remain immutable.
- **Rationale:** Exact snapshots make historical analysis inputs reproducible without a second fact
  store or mutable completeness boolean.
- **Current rules:** Q108 requires one current version per EvidenceItem, not free historical-version
  selection; body-text saves use Q96-Q97 and restoring old text creates a new temporal version.
  Q113 removes the separate completeness confirmation mechanism. Save establishes authority;
  no KnowledgeConfirmation object or UNCONFIRMED Gate survives.
- **Cleanup:** Only the explicitly superseded confirmation clauses were removed; baseline identity
  and exact-history semantics remain accepted.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 14 — Dual-Axis DeepFit, Draft Admission, and Context Completeness



### Q70 — Mutable ResumeDraft before atomic formal save

- **Status:** `ACCEPTED`
- **Decision:** Upload does not immediately create a formal ResumeVersion. It creates or updates a
  mutable ResumeDraft containing parsed resume content plus CandidateProfileDraft and EvidenceDraft
  proposals. The user reviews, edits, supplements, and reconciles these Drafts. Only Save creates an
  immutable ResumeVersion and initial ResumeGroundingSet, creates/reuses confirmed
  EvidenceItemVersions, advances Candidate Knowledge baseline, and records the corresponding
  grounding. Later Evidence changes never mutate the ResumeVersion. The same ResumeVersion may have
  a newer immutable GroundingSet against a later Candidate Knowledge baseline when its text is
  unchanged; a content, claim, structure, or layout change creates a new ResumeVersion.
- **Rationale:** Saving is the authority boundary: draft content remains flexible, while every formal
  Resume starts with stable content and auditable grounding.
- **Supersedes:** Q63 and Q67 only where they said upload immediately creates an imported formal
  ResumeVersion. It preserves Workspace Evidence ownership and Q67's post-save authority/retention
  separation.
- **Open contract detail:** Transaction boundaries, conflict handling, retry/idempotency, and partial
  failure behavior for the multi-asset Save command require the next round.
- **Current correction — Q108:** New formal Resume inputs must reference current facts. When a
  referenced Evidence version is no longer current, creating only a replacement GroundingSet for
  the old ResumeVersion cannot restore formal eligibility; create a current-fact ResumeVersion.
- **Draft durability — Q166:** Unsaved My Resumes ResumeDraft is temporary UI state; crash loss
  is accepted and no recovery checkpoint/autosave is promised. Normal navigation still requires
  Save / Discard / Cancel. Successful Save and Harness/business durability remain unchanged.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q71 — Formal Resume admission requires complete factual grounding

- **Status:** `ACCEPTED`
- **Decision:** Unresolved factual claims may exist only in mutable ResumeDraft. Before Save, every
  statement a recruiter would understand as a Candidate career fact must either ground to confirmed
  CandidateProfile/Evidence, create or reconcile confirmed Evidence, be corrected, or be explicitly
  removed. Any unresolved factual claim blocks formal save and therefore blocks DeepFit,
  ResumeAdvisor, export, preparation, and application. Successful Save atomically creates immutable
  ResumeVersion plus GroundingSet with complete factual grounding. Identity/contact, target heading,
  structural, and layout content are validated under their own authorities and do not require
  Evidence grounding.
- **Rationale:** This removes partial-grounding states from formal Resumes and ensures every asset
  eligible for AI optimization or real submission is factual, auditable, and safe by construction.
- **Supersedes:** Q61 and Q63 where they allowed an imported formal ResumeVersion before Evidence
  confirmation, and Q67's equivalent import sequence.

- **Current correction — Q108:** The independent draft-export/application exemption is withdrawn.
  Advisor work must be explicitly adopted and formally saved before export or formal downstream use;
  a user-confirmed fact may be created in that Save without third-party proof or a second confirmation.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q72 — Baseline, eligibility, and model visibility are three boundaries

- **Status:** `ACCEPTED`
- **Decision:** EvidenceBaselineSnapshot freezes all active confirmed Workspace Candidate Knowledge
  and binds KnowledgeConfirmation. EligibleEvidenceProjection applies exact Skill/task scope,
  validity, sensitivity/privacy, and user-authorization policies and records admitted/excluded
  Evidence plus non-sensitive exclusion reasons. ContextPackage then records the content actually
  provided to one AgentRun after Full Context or retrieval, rerank, parent expansion, redaction, and
  token packing. Full Context means all admitted eligible Evidence, never all locally stored data.
  A potentially supporting fact excluded by admission yields `UNKNOWN`, `NOT_ADMITTED`, or an
  equivalent non-negative conclusion. Retrieval miss, truncation, budget loss, or index fault yields
  `NO_EVIDENCE_RETRIEVED`/`UNKNOWN`. Strong `MISSING` is permitted only when the baseline is confirmed,
  relevant evidence was not excluded, and versioned completeness policy says the admitted Context
  was sufficiently examined. It still means no support in current confirmed and task-admitted
  Candidate Knowledge, not real-world incapability.
- **Audit requirement:** CandidateJobFitAnalysis retains exact baseline, confirmation, admission
  policy, EligibleEvidenceProjection, non-sensitive exclusion counts/categories, ContextPackage,
  retrieval/index versions, truncation/completeness facts, and final assessments. Sensitive excluded
  content never enters model Context, ordinary logs, or model output.
- **Rationale:** Candidate Knowledge completeness, permission to use a fact, and actual model
  visibility provide different proof strengths and cannot share one boolean.
- **Refines:** Q19, Q60, Q66, and S11.1.
- **Further refined by:** S15.1 makes Full Context the v1 default when every admitted Evidence item
  fits; retrieval completeness and miss rules apply only when the versioned Context strategy selects
  Retrieval Mode.
- **Further refined by:** Q82 fixes the exact validation gates required before Full Context may
  produce bounded strong `MISSING`; mode selection alone is never sufficient proof.
- **Current correction — Q113/Q115:** Baseline contains saved current facts, not a separate
  completeness assertion. Keep baseline / eligibility / actual Context distinct and preserve privacy,
  truncation, and output-validation checks. No KnowledgeConfirmation reference or Gate remains;
  MISSING is bounded by the particular analysis's saved inputs and sufficiently inspected scope.
- **Mid-run revocation — Q172:** If authorization for a protected EAGER_EXACT input is revoked
  after freeze, end the affected task fail-closed rather than silently reducing scope. No later
  Frame/repair/Tool consumes revoked input or publishes valid current Analysis. A requested new
  admitted scope needs a new task. Initial exclusions retain existing UNKNOWN semantics; prior
  transmission cannot be undone and necessary usage/recovery/audit stays truthful.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 15 — Atomic Resume Finalization and Experience-Level Evidence

### Q73 — Atomic FinalizeResumeDraft command

- **Status:** `ACCEPTED`
- **Decision:** `FinalizeResumeDraft` is one atomic Application Command. Parsing, deterministic
  Resume processing, optional LLM Evidence enhancement, preview, and user editing occur before Save.
  Save revalidates exact Draft revision, resolved claims/reconciliation, expected Profile/Evidence
  revisions, and idempotency key, then commits all non-rebuildable authority changes in one local DB
  transaction: ProfileVersion, Evidence roots/versions, BaselineSnapshot, KnowledgeConfirmation,
  Resume root/version, GroundingSet, and active pointers. Any failure rolls back the entire commit.
  New Resume root appears only on successful Finalize; an existing Resume advances only after commit.
  Rendering, embeddings, FTS/vector indexes, previews, and caches are post-commit rebuildable work.
- **Rationale:** Prepare may retry and post-commit derivatives may rebuild, but authority must never be
  left half-created or internally inconsistent.
- **Resolves:** Q70's transaction, conflict, retry, and partial-failure question.

- **Refined by:** Q78. KnowledgeConfirmation participates in the atomic commit only when the user
  explicitly confirms completeness for the exact new baseline; ordinary Resume save creates the
  baseline without automatically asserting Workspace-wide completeness.
- **Current correction — Q108:** Atomic authority Save again advances affected EvidenceItem
  current_version_id together with the new current-fact baseline and formal Resume. Preserve CAS,
  idempotency, and post-commit derivatives; no free historical-version selection is supported.
- **Current correction — Q113/Q114:** KnowledgeConfirmation is removed from the command and
  transaction. An Evidence Save also creates and advances immutable versions of every affected
  current Resume in the same formal save flow. These propagated Resume changes reuse the newly
  saved EvidenceVersion and must not recursively create further Evidence versions.
- **Resolved by Q118-Q119:** The local authority transaction includes every affected current Resume
  and its GroundingSet, not only the Resume initiating Save. Any authority write failure rolls back
  all changes. Revisions guard concurrent edits; rendering/index/cache work remains post-commit.
- **Durable derivatives — Q147:** Register necessary DerivedWorkItem(PENDING) intents in the
  same short SQLite authority transaction, after Prepare determines required work. Actual render/
  preview/index/cache execution stays post-commit and safely idempotent; stale outputs cannot
  overwrite current artifacts. Intent persistence closes the commit-before-scheduling crash window.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q74 — Claim classification and user-confirmed fact authority

- **Status:** `ACCEPTED`
- **Decision:** Resume content is classified as `PROFILE_FACT`, `CAREER_FACT`, `DERIVED_SUMMARY`,
  `TARGETING_EXPRESSION`, `PRESENTATION_ONLY`, or `AMBIGUOUS`. Profile facts reference exact
  CandidateProfileVersion fields. Career facts—including dates, quantities, rank, scope, outcomes,
  and proficiency—reference exact EvidenceItemVersion field/index/span locations. Derived summaries
  reference their composing Evidence and derivation rule without amplifying strength. Targeting
  describes user intent, and presentation changes no factual meaning. Ambiguous content blocks Save
  until resolved. Parser/model may propose classification but has no fact authority. Contrary to the
  earlier recommendation, explicit user input may create or amend Candidate Knowledge: Finalize
  creates a `USER_CONFIRMED` Evidence authority and grounding when no fact exists, and forces an
  explicit choice when it conflicts with current authority.
- **Rationale:** Grounding prevents Resume and Candidate Knowledge from becoming competing fact
  stores; it does not demand third-party proof or deny the user authority over their own facts.
- **Refines:** Q15, Q41, Q70, and Q71.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q75 — Immutable ResumeGroundingSet without persistent Assertions

- **Status:** `ACCEPTED`
- **Decision:** ResumeGroundingSet is an immutable durable derived asset binding exact ResumeVersion,
  CandidateProfileVersion, actual Evidence dependencies, and GroundingPolicyVersion. It maps ResumeClaims
  to Profile fields or canonical EvidenceRef (exact EvidenceItemVersion plus pointer); v1 does not
  persist EvidenceAssertion. One ResumeVersion may have many Sets.
  Historical consumers freeze exact Set; a new Use Case resolves a compatible Set by exact inputs,
  reusing it or creating another without modifying ResumeVersion or old Sets. There is no mutable
  active GroundingSet pointer. Future semantic assertion projections, if any, remain derived and have
  identity only within their retrieval/index version.
- **Rationale:** Grounding can evolve with Candidate Knowledge without making every bullet a Domain
  entity or allowing historical Resume semantics to drift.
- **Supersedes:** Q62 and Q57's persistent Assertion contract; refines Q68's support references.
- **Refined by:** Q79. Canonical grounding uses the minimal
  `(evidence_item_version_id, pointer)` EvidenceRef; schema, provenance, hash, and source-span data
  remain owned by the referenced EvidenceItemVersion rather than duplicated into each Ref.
- **Current compatibility — Q87:** Validate actual dependencies, not membership of the entire
  baseline. Immutability, exact historical references, and no mutable active Set pointer remain.
- **Current-use qualification — Q108:** Historical Sets remain immutable, but non-current career-fact
  references cannot authorize new formal use. A new current-fact ResumeVersion is required when its
  referenced Evidence changed; unrelated Evidence still does not invalidate actual-dependency grounding.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q76 — Exact-baseline fail-closed CandidateJobFit compatibility

- **Status:** `ACCEPTED`
- **Decision:** v1 CandidateJobFitAnalysis binds an exact EvidenceBaselineSnapshot. Any confirmed
  semantic baseline change makes the old Analysis historical/stale for current Candidate Potential,
  even if the change appears unrelated to a Job. Old Analysis remains viewable and labelled as based
  on older Candidate Knowledge; a current result requires a new run. Do not infer requirement-level
  impact in v1. Future evaluated dependency/impact analysis may support incremental work, but still
  creates a new Analysis identity and never reinterprets the old one under the new baseline.
- **Rationale:** Conservative invalidation avoids missing newly relevant Evidence or silently
  attributing an old semantic judgment to unseen authority.
- **Refines:** Q69.
- **Refined by:** Q97 defines any formally saved factual body-text change as an Evidence/baseline
  change; there is no semantic-equivalence exception for wording edits. Pure presentation changes
  preserve the baseline and current CandidateJobFit compatibility.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q77 — Current-authority validation for every new application

- **Status:** `ACCEPTED`
- **Decision:** Immutable old ResumeVersions, GroundingSets, and Applications remain auditable but do
  not automatically qualify for a new application. Preparation/readiness validates every factual
  claim against current CandidateProfileVersion, current confirmed EvidenceBaselineSnapshot, and a
  compatible GroundingSet. A semantically valid Evidence version update may create a new GroundingSet
  without changing Resume text. Withdrawn, invalid, or corrected Evidence cannot support new action;
  if the Resume text no longer holds, the user must create a corrected ResumeVersion. Execution
  Snapshot freezes exact ResumeVersion, GroundingSet, ProfileVersion, baseline, and hashes. Later fact
  changes never rewrite history but may invalidate an undispatched Approval under stale policy.
  Historical application corrections remain append-only rather than destructive.
- **Rationale:** Historical truth describes what was sent; current readiness must prevent known-stale
  or unsupported facts from being sent again.
- **Refines:** Q30, Q37, Q42, Q70, and Q75.
- **Refined by:** Q87 makes current grounding validation dependency-aware. Do not infer that any
  unrelated baseline change invalidates GroundingSet. Snapshot/audit references and CandidateJobFit's
  whole-baseline compatibility remain distinct from GroundingSet compatibility.

- **Current correction — Q108:** Even a still-readable old EvidenceVersion is historical-only once
  no longer current. Referenced fact changes require a current-fact ResumeVersion before a new
  application; re-grounding the old Resume alone is insufficient. Unrelated facts do not invalidate
  the Resume's actual dependencies. Completed application history remains untouched.
- **Current correction — Q113/Q114:** Current-authority validation consumes saved baseline and
  Resume inputs without a completeness-confirmation Gate. Affected Resume roots automatically
  advance during fact Save; historical snapshots and already selected exact inputs are not rewritten.
- **Deletion refinement — Q151:** Delete Evidence means logical removal of an EvidenceItem, with
  affected current Resumes determined only by explicit Item inclusion. Confirm the listed impact,
  then atomically update baseline, directly affected current Resume versions/pointers and necessary
  derived intents. No per-version withdrawal UI, sentence/Claim dependency graph, or old-version
  fallback. Historical assets stay immutable; new formal work consumes current eligible inputs.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 15 Batch Supplement

### S15.1 — Experience-level Candidate Knowledge and Full-Context-first DeepFit

- **Status:** `ACCEPTED`
- **Decision:** v1 Candidate Knowledge authority is the user-maintainable experience-level
  EvidenceItemVersion: one education, employment/internship, project, skill, certificate, award, or
  similar coherent record with typed scalar/list fields such as dates, responsibilities,
  achievements, and technologies. Do not persist a first-class EvidenceAssertion for every bullet.
  Fine grounding uses `EvidenceRef(exact evidence_item_version_id, field_path, optional item_index,
  optional source_span)`. Deterministic Document/Resume parsing extracts layout, headings, contact,
  dates, roles, projects, and bullets into typed Drafts; an LLM is optional semantic enhancement for
  complex descriptions, never the from-scratch ingestion owner. Human review plus
  FinalizeResumeDraft creates authority.
- **Context strategy:** v1 is Full Context First. After confirmed Baseline and task admission, if all
  eligible Evidence fits the versioned budget, ContextPackage includes all of it with exact
  RequirementSet and the selected Resume/Grounding inputs. CandidateJobFit evaluates Requirements
  against EvidenceRefs; ResumeCoverage evaluates expression. This avoids retrieval miss at current
  personal-workspace scale. Only when eligible Evidence exceeds budget does Context Builder select
  Requirement-level Retrieval. It may derive semantic chunks/assertion projections, embeddings, FTS,
  hybrid recall, fusion, rerank, parent expansion, diversity, and token packing from authoritative
  EvidenceItemVersions. Every such artifact is rebuildable infrastructure and maps back to canonical
  EvidenceRefs; no index or projection becomes fact authority.
- **Requirement asymmetry:** On-demand RequirementSet semantic decomposition remains because
  Requirements are the direct DeepFit assessment and scoring units, even though Candidate Knowledge
  remains experience-level. JD parsing therefore stays as decided in Q58-Q59.
- **MISSING rule:** In Full Context, a confirmed baseline plus complete admission and inclusion of all
  eligible Evidence permits bounded `MISSING` when no support exists. Retrieval completeness, top-k,
  and miss semantics apply only in Retrieval Mode. Q72's baseline → eligibility → Context separation
  remains mandatory in both modes.
- **Rationale:** The design matches the scale and UI of one person's career history, preserves precise
  grounding without premature Domain atoms, and defers RAG complexity until Context size creates a
  measured need.
- **Supersedes:** Q57, Q62, S11.1's Candidate-side Assertion/RAG-first design, and Q60's assertion-based
  ingestion/default-retrieval assumptions. It refines Q68, Q72, and Q75 without changing their core
  authority or two-axis boundaries.
- **Deferred detail:** EvidenceRef canonical syntax, Context-mode selection policy, derived retrieval
  projection mapping, Full Context completeness validation, and thresholds require the next round.
- **Current corrections — Q108/Q111/Q112:** Full-Context-first and experience-level Evidence remain.
  Requirement parsing is LLM extraction with deterministic validation. CandidateJobFit receives
  admitted current-baseline Evidence; ResumeJobFit receives the selected formal Resume, not the
  whole baseline or a ResumeCoverage dependency. Downstream tasks consume the exact RequirementSet,
  not full JD re-interpretation. The old shared two-axis/coverage clauses no longer apply.
- **v1 scope correction — Q121/S24.1:** Full Context remains the v1 Fit path. Requirement-level
  bounded Agentic RAG is a retained post-v1 extension, not a required v1 overflow implementation.
  Its detailed retrieval design is outside this Grill; v1 overflow behavior remains to be settled.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 16 — Completeness Authority, Canonical EvidenceRefs, and Context Strategy

### Q79 — Minimal version-scoped EvidenceRef

- **Status:** `ACCEPTED`
- **Decision:** v1 EvidenceRef is a value object containing only exact
  `evidence_item_version_id + pointer`. Pointer is a canonical JSON Pointer or equivalent controlled
  path to a field/list item, such as `/responsibilities/1`; an explicit root pointer references the
  whole EvidenceItemVersion. The immutable EvidenceVersion already owns schema version, provenance,
  and hashes, so each Ref does not duplicate schema, index, value hash, or source span. A newer
  EvidenceVersion never redirects or migrates an old Ref. Boundary validation must resolve every Ref
  before persisting GroundingSet, DeepFitAnalysis, ResumeClaim, or Suggestion.
- **Rationale:** Exact version freezes the fact snapshot and pointer selects its internal part,
  providing precise grounding without creating another entity or redundant metadata.
- **Resolves:** S15.1's EvidenceRef syntax question and refines Q75.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q80 — Harness-owned initial Context strategy and runtime supervision

- **Status:** `ACCEPTED`
- **Decision:** Full Context versus Retrieval is selected by shared Agent Harness Context Engineering,
  not DeepFit or the model. Before the first model call, a versioned ContextStrategyPolicy uses model
  limit, actual serialized input, system/tool/output reserves, and safety margin to build the initial
  ContextPackage. During a bounded AgentLoop, Harness Hooks supervise token, deadline, tool-result,
  and step budgets and, before later model calls, apply policy-governed Context management or
  terminate. The model never owns the final decision. Exact compaction/summarization mechanics remain
  deferred to the Harness Context Engineering phase.
- **Rationale:** Initial packing and runtime growth are distinct control points but both require
  deterministic policy, budget enforcement, and audit outside model discretion.
- **Refines:** Q47, Q72, and S15.1.
- **Refined by Q121:** ContextStrategyPolicy also constrains Tool visibility: Full-Context Fit
  exposes no Evidence Tools. Candidate Agentic retrieval is deferred beyond v1; Resume Fit uses
  Full Context without an autonomous Tool loop.
- **Resolved at architecture level — Q132:** Classify protected exact inputs, externalize Tool
  results, trim history windows, and perform deterministic micro-compaction before a bounded semantic
  checkpoint. Trigger/target hysteresis and one Provider-size rescue are required; values/schemas
  remain deferred. Protected authority cannot be summarized to bypass Q123.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q81 — Retrieval projections must rehydrate canonical Evidence authority

- **Status:** `ACCEPTED`
- **Decision:** SemanticChunk, AssertionProjection, embedding, and FTS records are rebuildable
  retrieval derivatives, never final grounding targets. A RetrievalUnit minimally records its ID,
  index version, canonical EvidenceRefs, retrieval text, and projection version. After retrieval,
  Context Builder reloads exact EvidenceItemVersion authority and verifies frozen-baseline membership,
  eligibility, pointer resolution, and non-staleness before admitting content. Failed candidates are
  discarded with non-sensitive reasons. Model output and durable analysis cite canonical EvidenceRef,
  never chunk ID alone. Indexes may be deleted/rebuilt without breaking historical business assets.
- **Rationale:** Retrieval locates candidates; only the canonical Evidence Store determines what the
  facts are and whether they belong in the exact run.
- **Resolves:** S15.1's derived-projection mapping question.

- **Current correction — Q108/Q112:** Historical-version Overlay admission is removed. Rehydrate
  only facts authorized by the specific frozen task input; Candidate Fit's scope is its current
  confirmed baseline, and Resume Fit cannot acquire unexpressed Candidate facts through retrieval.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q82 — Validated bounded MISSING in Full Context

- **Status:** `ACCEPTED`
- **Decision:** `FULL_CONTEXT` alone never proves `MISSING`. Strong `MISSING` requires an exact
  saved BaselineSnapshot; complete admission with no possibly
  supporting Evidence excluded by privacy, sensitivity, validity, Skill scope, or authorization;
  inclusion of every eligible Evidence item without truncation; complete one-to-one coverage of the
  RequirementSet in model output; and successful schema/EvidenceRef validation. Any failed Gate
  degrades to `UNKNOWN` or an explicit incomplete reason. The meaning remains bounded to no support
  found in current saved task-usable Candidate Knowledge, not real-world incapability.
- **Acceptance implication:** ContextPackage carries an Evidence manifest/inclusion proof; every
  Requirement has exactly one validated Assessment; positive support refs resolve; `MISSING` records
  its basis and inspected scope. v1 need not run a second model pass for every negative, but false
  negatives, omitted Requirements, and grounding require evaluation Hard Gates. If reliability is
  insufficient, UI language degrades to “no supporting evidence found in current materials.”
- **Rationale:** Full inclusion removes retrieval loss but not model omission or schema failure, so
  promotion still requires deterministic validation and measured semantic reliability.
- **Refines:** Q60, Q72, and S15.1.
- **Current refinement — Q83/Q113/Q115:** Evaluate actual inclusion against the assessment-producing
  Frame. No separate completeness-confirmation Gate exists. Saved scope, admission, inspection,
  validation, and lineage still apply; insufficient inspection is UNKNOWN. Candidate and Resume
  MISSING retain their distinct bounded meanings. Q117 does not require offline annotated
  ParserVersion release approval in v1.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 17 — Context Frames, Confirmed DeepFit, Advisor Workspace, and Dependency Grounding

### Q83 — Frozen task ContextPackage and per-invocation ContextFrame

- **Status:** `ACCEPTED`
- **Decision:** AgentRun creation freezes a task-level ContextPackage specifying admitted Job,
  Requirement, Evidence, Resume/Grounding inputs, and Context Strategy. Every ModelInvocation binds
  its own immutable ContextFrame recording the exact messages, readmitted ToolResults,
  compaction/redaction outputs, and token accounting actually sent to that model call. Tool results,
  compression, and clipping create later Frames without editing prior ones. Full Context
  completeness is evaluated against the Frame that actually produces RequirementAssessments.
- **Rationale:** A bounded loop may have several different model inputs; one task package cannot
  prove what each invocation saw. Q80/Q52 still defer the detailed compaction implementation.
- **Refines:** Q47, Q72, Q80, and Q82; per-call actual visibility is now recorded by ContextFrame.
- **Retention clarified by Q125:** Exact Frame/response payload is durable for required recovery,
  not automatically permanent. Protected payload retention is separate from lightweight audit and
  business history; purged exact input must never be reconstructed from current data as historical fact.
- **Compaction refinement — Q132:** Validate and durably publish a checkpoint before a new Frame
  uses it; preserve prior recoverable sources. Reinject exact admitted source versions and constraints,
  not latest versions or paraphrases. Earlier Frames remain historical, never rewritten.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q85 — Shared Candidate Knowledge writes and a separate Advisor working draft

- **Status:** `ACCEPTED`
- **Decision:** All formal Candidate Knowledge writes go through UpdateCandidateKnowledge, atomically
  creating EvidenceVersions, advancing active pointers, and creating a BaselineSnapshot, with
  KnowledgeConfirmation only after explicit user confirmation. Both 我的简历 (current Resume-related
  facts) and 求职资料库 (all facts) are formal fact-editing entry points into this shared authority
  path. Formal Resume-page changes are treated as fact-material edits. ResumeAdvisor Workspace alone
  offers a temporary working draft based on a saved ResumeVersion, allowing suggestion adoption and
  user CRUD without automatically writing Candidate Knowledge or changing its baseline/DeepFit.
  The user may freeze/export that work for one application, or explicitly choose 保存到求职资料 to
  reconcile and promote facts through UpdateCandidateKnowledge.
- **Rationale:** The product distinguishes formal fact maintenance from temporary job-specific
  expression while preserving one Candidate Knowledge write path.
- **Supersedes:** The earlier product assumption that 我的简历 itself offers an independent
  expression-only edit path. Q73's atomic formal-save rules remain relevant; Advisor working-draft
  changes are separate from that command.

- **Current correction — Q108:** Working drafts remain editable and non-authoritative, but their
  independent freeze/export/application route is removed. Explicit adoption and formal Save now
  advances EvidenceItem.current_version_id, snapshots current facts, and creates the formal Resume
  atomically. Save is not automatic whole-Knowledge completeness confirmation.
- **Current correction — Q113/Q114:** Formal Save itself confirms facts; no separate completeness
  confirmation exists. Both formal editing pages handle Save / Discard / Cancel locally, while
  shared authority writes synchronize current versions of all affected formal Resumes. Advisor
  working drafts retain the separate explicit formal-adoption boundary from Q108.
- **Additional formal entry path — Q128:** A confirmed fact edit may also reach the same Application
  write command via a specifically authorized chat Tool. This does not make unconfirmed chat or
  Memory authoritative and does not grant business mutation to Fit or MemoryExtraction Skills.
- **Scoped supersession — Q146:** Advisor has discussion and Suggestions, not ResumeDraft or a
  persistent working draft. Draft belongs only to My Resumes page CRUD. Formal apply resolves a
  user-specified Resume or Workspace default, previews concrete shared-fact/current-Resume impact,
  receives one confirmation, and immediately commits through UpdateCandidateKnowledge. Earlier
  draft/promotion clauses in this record are historical only; no extra draft Save follows.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q86 — Historical EvidenceRef resolution by original schema reader

- **Status:** `ACCEPTED`
- **Decision:** EvidenceRef remains exact evidence_item_version_id plus pointer. Resolution reads
  evidence_schema_version from the immutable EvidenceItemVersion and invokes its corresponding
  reader. Breaking schema changes affect new writes and never rewrite old version payloads. Old
  readers are retained indefinitely by default. A common read projection may be built after
  resolution, but historical pointers are first interpreted against their original schema.
- **Rationale:** Minimal references remain auditable across schema changes without duplicated
  metadata or destructive migrations of historical facts.
- **Refines:** Q79 and compatibility requirements under Q26.
- **Formal writeback:** `architecture.md`, `contracts/*`, `development.md`, `acceptance.md`

### Q87 — Dependency-aware EnsureResumeGroundingSet

- **Status:** `ACCEPTED`
- **Decision:** A GroundingSet's compatibility identity does not bind the entire EvidenceBaseline.
  EnsureResumeGroundingSet receives exact ResumeVersion, current Profile/Candidate Knowledge
  authority, and exact GroundingPolicyVersion, and checks the facts that this Resume actually uses.
  Reuse a Set when its exact EvidenceRefs resolve and their support remains valid under current
  authority; unrelated Evidence changes do not invalidate it. When a referenced EvidenceVersion is
  replaced, check only affected Claims. Proven deterministic lineage, pointer mapping, and unchanged
  factual support may create a new immutable Set. Version ancestry alone is insufficient. Semantic
  change, ambiguous mapping, or weakened support yields REVIEW_REQUIRED; explicitly absent current
  support yields UNSUPPORTED and blocks new formal application. Re-grounding cannot edit Resume
  wording or Candidate Knowledge. Human review may produce a new Set; an incorrect Claim requires
  corrected Resume content and a new ResumeVersion. Preparation, DeepFit, and Advisor share this
  Use Case rather than implementing separate compatibility rules.
- **Rationale:** Whole-baseline identity belongs to whole-knowledge analysis and completeness
  confirmation. Resume grounding depends only on facts its Claims actually reference.
- **Supersedes:** Q75's whole-baseline compatibility requirement and corresponding interpretations
  of Q77. Q76 remains unchanged for CandidateJobFitAnalysis. Exact historical references survive.

- **Current correction — Q108:** Actual-dependency checks remain, but a non-current referenced
  EvidenceVersion cannot be reused for new formal business or rescued by re-grounding the same old
  ResumeVersion. First create a new ResumeVersion using current facts. Only unrelated Evidence
  changes leave a current-fact Resume's grounding compatible; no historical fact Overlay is allowed.
- **Current correction — Q114:** Referenced Evidence updates create new affected current
  ResumeVersions automatically in the formal Save flow, not via a separate manual Resume-refresh
  operation. EnsureResumeGroundingSet still validates exact inputs; it does not mutate old versions.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 17 Product Supplements

### S17.1 — User-configured acquisition scope and separately evaluated quality scope

- **Status:** `ACCEPTED`
- **Decision:** Product scope does not prescribe AI Agent/LLM, Backend, Full-stack, Shenzhen, or a
  target-company set as initial supported targets or evaluation priorities. Acquisition and
  QuickScreen follow user Preferences; unset dimensions impose no restriction. Acceptance/evaluation
  work later defines the tested scope and defensible quality claims.
- **Rationale:** Personal search scope belongs to the user, while demonstrated quality must come
  from evaluation rather than a hard-coded product persona.
- **Refines:** Q1, Q45, and Q55. Role/city examples elsewhere are illustrative, not product limits.
- **Formal writeback:** `spec.md`, `acceptance.md`, `contracts/*`

### S17.2 — Five navigation entries and contextual application preparation

- **Status:** `ACCEPTED`
- **Decision:** Left navigation is 我的简历, 求职资料库, 岗位池, 求职助手, 我的投递.
  ApplicationPreparation is a flow page reached after selecting Jobs in 岗位池 and clicking 投递;
  it has no top-level navigation. 我的投递 exposes 前往投递, which routes to the Job pool for selection.
  Preparation, material selection, readiness, MaterialApproval, Snapshot, and ExecutionApproval retain
  their existing business boundaries. 求职助手 is a conversational page initially exposing only
  Resume optimization; mock interviews and other capabilities require later independent design.
  A chat-product interaction reference does not import job search, email, or unrelated capabilities.
- **Rationale:** Navigation reflects user tasks and contextual entry, while business authority remains
  independent of menu structure.
- **Supersedes:** Q1's original navigation illustration wherever it implies a top-level 投递准备 or
  separate 求职进展 entry. Refines Q6, Q30, Q42, and S5.3; no new conclusion about detailed tracking
  layout is inferred solely from removal of a navigation entry.
- **Formal writeback:** `spec.md` navigation, preparation flow and chapter review;
  `architecture.md`, `acceptance.md`

### S17.3 — One Assistant page with General and Job-targeted ResumeAdvisor modes

- **Status:** `ACCEPTED`
- **Decision:** One ResumeAdvisor Skill and 求职助手 page support ordinary and preparation-originated
  conversations through the unified ChatSession. Preparation entry creates a new chat with explicit
  Job/Preparation/selected Resume references; General entry uses default or explicit saved Resume
  context without silently turning a job-family request into a concrete Job scope.
- **Acquisition — Q139:** Entry references are not injected business bodies. Advisor primarily uses
  LAZY_TOOL to read exact Resume, requirements, and Evidence as needed; each result is admitted and
  recorded in later Frames. No special targeted Session/Agent implementation is introduced.
- **Continuity:** Q93 selection priority, exact input provenance, current validation, user choice,
  and the controlled formal-save path remain. Q91 governs explicit return to Preparation.
- **Rationale:** Entry context changes the intended task, not the underlying Skill or authority.
- **Refines:** S5.3, Q24, Q41, Q47, Q52, Q58, and Q85; Q88-Q94 settle defaults and unified Sessions.
- **Current correction — Q108/Q112:** Both entry modes share the formal-save-only Advisor outcome.
  Compatible CandidateJobFitAnalysis or ResumeJobFitAnalysis may optionally enhance advice; neither
  is a mandatory prerequisite, and no ResumeCoverageAnalysis or draft-to-application bypass exists.
- **Formal writeback:** `spec.md` navigation, prerequisites, REQ-RESUME-006, preparation flow and
  chapter review; `architecture.md`, `contracts/*`, `acceptance.md`

### S17.4 — Shared Harness and bounded Assistant capability scope

- **Status:** `ACCEPTED`
- **Decision:** DeepFit and ResumeAdvisor share Agent Harness infrastructure and use distinct Skill
  Contracts for inputs, allowed tools, outputs, budgets, and interaction. DeepFit remains headless
  inside the Job pool. Only Resume optimization is initially exposed as a chat Skill in 求职助手;
  that restriction neither removes DeepFit Skill nor creates a general-purpose Agent that
  automatically dispatches every job-search capability.
- **Rationale:** UI capability availability and runtime reuse answer separate product/design questions.
- **Refines:** S7.1, Q35, Q47, and S17.3.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 18 — Default Resume, Unified Chat, and User-Confirmed Formal Save

### Q88 — Default Resume and explicit Tool-assisted selection

- **Status:** `ACCEPTED`
- **Decision:** Resume-dependent Assistant Skills default to the Resume configured in 我的简历.
  Missing default Resume fails business preflight with fixed import/set-default guidance before
  AgentRun creation or model invocation. The user need not select a Resume each time. An explicit
  request for another saved Resume may use the active Skill's declared Resume Tool to query/read it,
  consistent with progressive capability disclosure. The default is an initial scope, not a permanent
  binding; every Turn/AgentRun records exact versions actually used, with no silent switching. v1
  accepts only formal Resumes in 我的简历; ad hoc chat PDF/DOCX upload/optimization is out of scope.
- **Rationale:** A default reduces repeated setup while explicit requests and exact input records
  preserve user control and explainability.
- **Supersedes:** Q88's recommendation to require manual selection before every new optimization.
- **Open detail:** Priority among preparation-selected, continued-chat, explicitly requested, and
  default Resumes, and Run-time resolution versus frozen ContextPackage, require Q93-Q94.
- **Resolved by:** Q93 fixes selection precedence and guarantees a default whenever a Resume exists;
  Q94 fixes immutable runtime input admission. Preflight fail-fast now applies when no Resume has
  ever been created, not to an independently missing default among existing Resumes.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q89 — Unified ChatSession with structured initial preparation context

- **Status:** `ACCEPTED`
- **Decision:** Use one ChatSession/Conversation model without a Job-targeted Session object or
  Session compatibility mechanism. Each 简历优化 entry from ApplicationPreparation starts a new chat
  and places explicit Job/Requirement/Preparation references in structured initial context.
  Under Q139 this does not imply those business payloads have entered the initial Frame;
  typed lazy reads supply the needed exact content after admission.
  General and targeted chats differ only in whether they start with Job context. Existing chats are
  continued through recent conversations; another preparation entry always creates another chat.
  Each Turn/AgentRun records actual exact JobVersion, ResumeVersion, Evidence, and other inputs.
  Restoring a chat reruns current admission, grounding, stale, and permission validation.
- **Rationale:** Ordinary chat continuity plus explicit per-run inputs provides sufficient isolation
  without a new business Session type or compatibility state machine.
- **Supersedes:** Q47/S17.3 interpretations requiring mode-specific Session identity and the Q89
  recommendation for compatible-Session discovery at preparation entry. Q52 retention boundaries
  survive for the unified chat model.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q91 — Explicit optimistic-concurrency return to ApplicationPreparation

- **Status:** `ACCEPTED`
- **Decision:** Producing an optimized Resume result and applying it to Preparation are independent.
  Only 采用并返回投递准备 attempts the update. CAS checks expected Preparation revision; success
  patches only adopted Resume/Grounding references and recomputes rendering, readiness, and approval
  compatibility without overwriting Greeting or unrelated edits. Conflict preserves the optimized
  result, reloads current Preparation, and asks whether to apply it there. Explicit confirmation
  permits a Resume-only patch against the new revision, still subject to CAS. Frozen execution
  Snapshots remain immutable. Return neither grants ExecutionApproval nor starts external execution.
- **Rationale:** Material adoption must preserve concurrent changes and keep execution authorization
  separate from content selection.

- **Refines:** Q30, Q42, and S17.3.
- **Current correction — Q108:** Adopt-and-return selects an eligible formally saved ResumeVersion.
  Independent temporary Advisor materials are no longer a selectable alternative. CAS, narrow
  patching, and separate execution approval remain unchanged.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`


## Round 19 — Resume Precedence, Runtime Inputs, Frozen Materials, and Text-Based Fact Updates

### Q93 — Explicit Resume precedence and Workspace default invariant

- **Status:** `ACCEPTED`
- **Decision:** Resolve the editing Resume in this order: this Turn's explicitly requested saved
  Resume, the ChatSession's explicitly adopted editing Resume, the originating Preparation's selected
  ResumeVersion, then Workspace default. New ordinary chats use the default; preparation entry uses
  the selected Resume. Later default changes never silently move an existing chat's editing object.
  User-directed switches must resolve ambiguity and every Turn/Run records the actual exact
  ResumeVersion without rewriting prior Turns. The first Resume automatically becomes default.
  With multiple Resumes the user may switch default. Deleting the last Resume is prohibited; deleting
  the default must atomically select another existing Resume, either explicitly or automatically.
  Consequently only the never-created-any-Resume case requires the no-Resume Skill preflight failure.
- **Rationale:** Default choice, preparation material, chat editing object, and immutable run input
  are separate scopes, with explicit current user intent taking precedence.
- **Supersedes:** Q88's possible existing-Resume-without-default state and overly broad missing-default
  failure condition. Skill Tools and the saved-Resume-only scope remain accepted.
- **Scoped formal-apply rule — Q146:** For an Advisor command to apply changes, use the explicitly
  specified target Resume, otherwise Workspace default, and show it in the concrete impact preview.
  This supersedes treating prior Chat/Preparation selection alone as implicit apply-target authority.
  Existing discussion/read context, pinned references, default invariants, and no-silent-switch rules
  remain; suggestions must not be relabeled as based on a different target.
- **Formal proposal refinement — Q148-Q149:** Only the actual apply target is selected: current
  instruction's explicit Resume, otherwise Workspace default. Read its exact version and generate
  its own before/after ChangeProposal; do not infer a suggestion-source Resume or transplant another
  Resume's patch. Preview target/version/default status, fact changes, and affected current Resumes.
  One confirmation binds that complete Proposal; target/patch changes or revision conflicts require
  a new preview. Ordinary exact input lineage remains, not an extra source-selection concept.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q94 — Append-only admitted runtime inputs after initial ContextPackage

- **Status:** `ACCEPTED`
- **Decision:** The immutable initial ContextPackage contains only inputs already resolved at Run
  creation, task scope, and allowed Tool capabilities. A Skill Tool may later resolve another exact
  ResumeVersion. After permission, privacy admission, and version validation, record that version as
  a new immutable runtime input and include its admitted content/references in the next ContextFrame.
  Never edit the initial Package or earlier Frames. Querying/comparing another Resume does not switch
  the editing object without explicit user intent. Suggestions, working drafts, and other outputs
  bind the actual editing baseline, not merely the starting default. Apply this same trace to other
  Tools: initial Package → ToolCall/Result → admitted runtime input → Frame → Invocation → result.
- **Rationale:** Progressive Tool access and frozen initial context coexist through append-only input
  provenance rather than mutable packages or a Session compatibility framework.
- **Refines:** Q83, Q88, and Q93.
- **Extended by Q134:** The same append-only mechanism admits actual committed business-write
  results during an authorized Advisor task, not just lookup results. Initial Context and old
  suggestions stay immutable; unrelated concurrent edits and independent Fit inputs are not upgraded.
- **Scoped supersession — Q146:** Advisor has discussion and Suggestions, not ResumeDraft or a
  persistent working draft. Draft belongs only to My Resumes page CRUD. Formal apply resolves a
  user-specified Resume or Workspace default, previews concrete shared-fact/current-Resume impact,
  receives one confirmation, and immediately commits through UpdateCandidateKnowledge. Earlier
  draft/promotion clauses in this record are historical only; no extra draft Save follows.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`


### Q96 — One fact-change preview and atomic formal Save

- **Status:** `ACCEPTED`
- **Decision:** Saving an optimized Resume first previews new facts, changed facts, unresolved
  conflicts, and the formal ResumeVersion to be created. One explicit user confirmation supplies
  USER_CONFIRMED authority; do not add another factual confirmation. Omitted older Evidence remains
  unless explicitly removed. Every change to formal Resume body text is treated as a corresponding
  Candidate Knowledge fact-content change and creates a new version of the affected EvidenceItem;
  do not classify wording-only edits as semantically unchanged. Only experience/section ordering,
  layout, fonts, spacing, pagination, and other purely presentational edits leave Evidence unchanged.
  Ambiguous ownership and content conflicts are resolved in that same preview. Commit relevant
  Profile/Evidence, BaselineSnapshot, ResumeVersion, and GroundingSet atomically. A revision conflict
  after confirmation is a concurrency conflict, not a demand to prove the user's facts again.
- **Rationale:** A mechanical body-text versus presentation distinction keeps formal Resume and
  knowledge content synchronized without model judgment about semantic equivalence.
- **Supersedes:** Q96's proposed wording-only exemption and Q64's equivalent body-edit treatment.
- **Scoped refinement — Q133:** An unambiguous conversational instruction specifying facts to save
  already supplies explicit confirmation; do not demand a redundant second approval simply because
  the entry point is chat. The editor's fact-change preview, ambiguity/conflict resolution, atomicity,
  and revision checks remain; ordinary discussion is not a Save.
- **Scoped formal-apply refinement — Q146:** A request to apply Advisor changes triggers a concrete
  modification/shared-fact impact preview and one explicit confirmation, then immediate formal
  commit. This replaces the no-additional-preview interpretation for Advisor Resume application;
  ordinary fact discussion still does not trigger Save prompts or compulsory confirmation.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q97 — Body-text changes invalidate the baseline; presentation changes do not

- **Status:** `ACCEPTED`
- **Decision:** Formal Resume body-text changes always version the affected Evidence and create a
  new EvidenceBaselineSnapshot. Old KnowledgeConfirmation never automatically extends to that
  baseline; CandidateJobFitAnalysis/DeepFit based on the prior baseline becomes historical/stale.
  Pure presentation edits reuse Evidence, Baseline, and KnowledgeConfirmation and do not invalidate
  CandidateJobFit. Do not use semantic analysis to decide whether a textual rewrite counts as a
  fact change. This applies to formal Save, not ordinary Advisor draft edits. Q108 removes temporary-material export/application.
- **Rationale:** Deterministic change classification makes invalidation predictable and avoids
  treating unreviewed rewritten fact content as the previously confirmed knowledge baseline.
- **Supersedes:** Q97's proposed wording-only baseline reuse; refines Q66, Q73, Q76, and Q96.
- **Current correction — Q113/Q114:** Remove KnowledgeConfirmation and its carry-forward rules.
  Only an actual user change to current fact content versions Evidence. Propagating an already saved
  EvidenceVersion into affected Resumes creates ResumeVersions, not another EvidenceVersion or
  another baseline. Pure presentation edits still leave Candidate Knowledge unchanged.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 20 — Source Structure, Baseline-Owned Selection, and Historical Resume Validity

### Q98 — Experience authority with source-preserving internal structure

- **Status:** `ACCEPTED`
- **Decision:** EvidenceItem authority remains at experience level: a project, employment, education,
  or another coherent career record. Its version contains business-form fields and preserves source
  bullets/lists/paragraphs as far as possible, for example a Project's name, dates, technologies, and
  content blocks. Ingestion restores sections, records, fields, and existing structural boundaries;
  it does not decompose a bullet or paragraph into atomic facts or Assertions. A source paragraph
  remains one block when it has no finer structure. EvidenceRefs may address an entire version,
  field, or persisted bullet via pointers such as empty root, /content, or /content/1, but may not
  claim finer persisted structure that does not exist. A saved body-text change versions the whole
  affected EvidenceItem. Optional finer semantic segments belong only to Context/derived projections.
- **Rationale:** Stable experience authority and precise references coexist without requiring
  semantic atomization during import. Reference granularity does not dictate entity granularity.
- **Refines:** S15.1, Q79, Q96, and Q97. Exact typed schemas remain subject to the contract review;
  the example fields are not a complete frozen inventory.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`


### Q100 — Logical Resume removal preserves shared facts and historical lineage

- **Status:** `ACCEPTED`
- **Decision:** Delete Resume logically removes it from current selectable Resumes without cascading
  into Profile, Evidence, or historical artifacts. Keep at least one formal available Resume. Removing
  the default atomically selects another existing Resume and never leaves a missing default. Removed
  Resumes are unavailable for new chats, preparation, or applications, but exact versions referenced
  by past preparations, Snapshots, chats, materials, and GroundingSets remain readable/auditable.
  Continuing an old chat using a removed Resume requires explicit selection of an available Resume;
  never switch silently. Resume deletion neither deletes Workspace Evidence nor rolls back current
  baseline. Physical personal-data erasure is a separate deferred capability.
- **Rationale:** Resume provenance is not Evidence ownership; ordinary list removal must preserve
  completed application history and independently confirmed facts.
- **Refines:** Q63, Q93, and Q95.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 22 — Current Facts, Bounded Requirement Parsing, and Independent Fit Analyses

### Q108 — One current fact version, temporal history, and formal-save-only Resume use

- **Status:** `ACCEPTED`
- **Decision:** Each EvidenceItem owns exactly one `current_version_id`, representing its latest
  explicitly confirmed saved fact state. EvidenceItemVersion is immutable temporal history, not a
  parallel fact variant. Earlier versions remain for lineage, historical Resumes/analyses, and
  completed applications, but are not inputs to new formal business. Restoring V1 text after V2
  creates V3; neither content deduplication nor user selection rewinds the current pointer.
  EvidenceBaselineSnapshot freezes the current Evidence versions at that time, rather than selecting
  arbitrary historical versions. Formal fact changes advance the affected Item pointers and create
  a new baseline; the user cannot independently switch a baseline member back to an old version.
- **Resume boundary:** A formal ResumeVersion is a subset of current Candidate Knowledge plus
  presentation. Resumes may select different experiences and layouts, but new formal versions use
  the current version of every selected Item. Historical ResumeVersions keep their exact refs.
  If a referenced fact is no longer current, create a new current-fact ResumeVersion before new
  DeepFit or application; an old version's readability or lack of withdrawal is insufficient.
  Unrelated Evidence changes do not change which fact versions that Resume actually references.
- **Advisor boundary:** Free editing and autosave remain confined to a non-authoritative working
  draft. It cannot independently freeze into an application material or be exported/applied.
  The user either discards the work and uses an otherwise eligible original Resume, or explicitly
  adopts and saves. Changed body text versions the affected Evidence, advances current pointers,
  snapshots the baseline, and atomically creates a formal ResumeVersion before downstream use.
  Unchanged facts are reused; pure presentation edits do not version Evidence. Rendered artifacts
  from an eligible saved Resume still exist; the removed path is a draft bypass around formal Save.
- **Preserved invariants:** User confirmation supplies fact authority without third-party proof or
  a second factual-confirmation round. Save previews real changes/conflicts and preserves source
  provenance. Expected revisions/CAS and atomic fact-pointer/baseline/Resume writes remain required.
  Workspace baseline metadata does not create a Candidate Aggregate. KnowledgeConfirmation remains
  separate and does not automatically carry forward after a changed baseline. Privacy admission,
  canonical EvidenceRefs, explicit withdrawal, and separate execution authorization remain required.
- **Rationale:** One current fact state removes selectable fact branches, cross-version Overlay,
  and independent temporary-material eligibility while retaining full historical auditability.
- **Supersedes:** Q99's baseline-only selection authority; Q103 ResumeEvidenceOverlay; Q104's free
  historical-version selection; Q106's historical-version admission for new formal tasks; Q107's
  historical-version editing as an alternative formal-current branch; Q92/Q95 independent draft
  export/application; and Q102's temporary-material assessment branch. Those complete replaced
  records were removed in this requested cleanup.
- **Scoped corrections:** Q40/Q66/Q73/Q85 restore per-Item current pointers and temporal snapshots.
  Q70/Q71/Q75/Q77/Q87 no longer permit old formal Resume eligibility through historical-version reuse
  or GroundingSet-only rebinding. Q91 adopts a formally saved Resume; Q101 retains durable drafts
  but not independent freeze/export. Q105 withdrawal remains distinct from being historical, but
  both prevent that old version from serving as a new formal input.
- **Further refinement:** Q112 separately removes any score upper-bound or coverage relationship
  between Candidate Fit and Resume Fit, even though both now operate within current facts.
- **Current correction — Q113/Q114:** Remove the separate KnowledgeConfirmation mechanism.
  Save confirms facts and automatically advances all affected current ResumeVersions to the saved
  current Evidence, preserving each Resume's selection/order/presentation. Historical versions stay
  immutable; no separate user-triggered refresh step or recursive fact-version creation is needed.
- **Scoped supersession — Q146:** Advisor has discussion and Suggestions, not ResumeDraft or a
  persistent working draft. Draft belongs only to My Resumes page CRUD. Formal apply resolves a
  user-specified Resume or Workspace default, previews concrete shared-fact/current-Resume impact,
  receives one confirmation, and immediately commits through UpdateCandidateKnowledge. Earlier
  draft/promotion clauses in this record are historical only; no extra draft Save follows.
- **Deletion refinement — Q151:** Delete Evidence means logical removal of an EvidenceItem, with
  affected current Resumes determined only by explicit Item inclusion. Confirm the listed impact,
  then atomically update baseline, directly affected current Resume versions/pointers and necessary
  derived intents. No per-version withdrawal UI, sentence/Claim dependency graph, or old-version
  fallback. Historical assets stay immutable; new formal work consumes current eligible inputs.
- **Selection refinement — Q163:** v1 Resume inclusion is whole EvidenceItem experience body from
  its current version, plus experience selection/order/layout. No independent per-Resume bullet
  selection mapping or alternate fact text. Fine EvidenceRef grounding and Profile display/privacy
  rules remain; they do not imply independently selectable career-body fragments.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q109 — Historical Overlay isolation branch no longer needed

- **Status:** `REJECTED`
- **Decision:** Do not design separate model-input isolation for Baseline versus historical Resume
  Overlay. Q108 removes the parallel-version/Overlay premise, so this question requires no answer.
  Ordinary task-scoped privacy and model-input isolation still apply.
- **Rationale:** A removed data branch must not leave behind a second Context mechanism.
- **Resolved by:** Q108; independent analysis task boundaries are specified by Q112 and S22.1.
- **Formal writeback:** `architecture.md`, `contracts/*`

### Q110 — Freeze Batch selection before dependency resolution, then freeze complete analysis inputs

- **Status:** `ACCEPTED`
- **Decision:** Collection persists the exact JD only; no RequirementSet is generated on ingestion.
  DeepFitBatch first freezes the user's known selected inputs, including exact JobVersion,
  selected ResumeVersion, confirmed baseline, and budget where applicable to the requested task.
  A child without a compatible RequirementSet enters dependency preparation through the shared
  EnsureRequirementSet Use Case, with grounding/admission preparation as required. It does not
  start CandidateJobFit semantic analysis with unresolved or placeholder dependencies.
  After all dependencies resolve, create one complete immutable analysis request binding the
  exact resolved inputs and policies, then dispatch. Never silently substitute newer selected inputs.
- **Failure and reuse:** Incompatible required-input changes during preparation end the affected
  child under stale-input rules. A successfully generated immutable RequirementSet remains a
  durable independent asset and may be reused later even if another dependency or the child fails.
- **Rationale:** A user's selected target can be frozen before all lazily computed dependencies exist;
  a model analysis must nevertheless execute only against a fully resolved exact request.
- **Refines:** Q40's assumption that every complete dependency is available at Batch creation.
- **Same-batch correction:** Q111 replaces this answer's deterministic-first Requirement semantic
  parser with LLM extraction and deterministic validation. Only this parser mechanism is replaced;
  the two freeze points, stale handling, and durable dependency reuse remain accepted.
- **Further refinement:** Q112 makes Candidate Fit and Resume Fit independent selected tasks.
  Candidate baseline confirmation remains required for Candidate Fit; the Resume-only entry Gate
  is a remaining boundary, not permission to silently inherit every Candidate-task prerequisite.
- **Current correction — Q113:** Freeze the exact current saved baseline for Candidate Fit, without
  KnowledgeConfirmation. Two-phase selection/dependency/request freezing remains; neither task
  reads page dirty state or acquires an extra Workspace-completeness Gate.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q111 — Bounded LLM Requirement parsing and a sole structured requirements input

- **Status:** `ACCEPTED`
- **Decision:** An independent RequirementParse AgentRun receives the full exact JobVersion JD and
  extracts Requirements under a fixed schema/prompt/policy. Requirements include normalized text,
  necessity (`REQUIRED / PREFERRED / UNKNOWN`), logic (`ALL_OF / ANY_OF / UNKNOWN`), and source spans.
  LLM performs semantic interpretation; deterministic code validates schema, enums, source spans,
  duplicates, empty values, completeness constraints, and Domain invariants, then persists an
  immutable RequirementSet bound to exact JobVersion and parser/model/prompt/schema/policy versions.
- **Bounded failure:** Normally allow one ModelInvocation. A failed deterministic validation permits
  at most one repair using the original JD, initial structured output, and explicit validation
  errors, followed by the same validation. Continued failure stops the affected Job's analysis:
  no untrusted Set and no formal score based on partial parsing. Return an explicit cause such as
  `JD_SOURCE_INVALID`, `REQUIREMENT_PARSE_FAILED`, or `REQUIREMENT_VALIDATION_FAILED`, with safe
  diagnostics and an actionable check/correct/refetch path. Other Batch Jobs continue independently.
- **Consumer boundary:** Once validated, exact RequirementSet is the only Job-requirements input
  to CandidateJobFit, ResumeJobFit, and Job-targeted ResumeAdvisor; they do not reread full JD or
  reinterpret requirements independently. JobVersion JD remains the retained original source;
  the immutable derived Set is the reusable structured consumer contract, not a mutable JD replacement.
  EnsureRequirementSet remains shared with Advisor as established in Q58.
- **Rationale:** One bounded interpretation per compatible JobVersion avoids duplicated semantic
  parsing and makes downstream assessment units stable and auditable.
- **Supersedes:** Q110's deterministic-first semantic parser; earlier downstream full-JD-plus-Set
  input assumptions; and deterministic code as the owner of JD semantic decomposition. Retains
  Q14 activation safety, Q58 shared ownership, and Q59 immutable durable lineage.
- **Open validation detail:** Deterministic structural validation alone does not settle how parser
  semantic omission/fabrication quality is evaluated. Quality/evaluation acceptance remains to be
  specified without reintroducing downstream JD interpretation.
- **Validation scope resolved — Q117:** Mandatory runtime checks concern schema/source/structural
  validity, not a proof of zero semantic omissions. Ambiguous necessity/logic may remain UNKNOWN.
  Actual-JD tests and manual checks guide iteration; a formal annotated ParserVersion release Gate
  is deferred, not required in the v1 architecture.
- **Usable dependency Gate — Q171:** No usable Requirement means fail fast before downstream
  Fit. An empty/non-assessable result cannot become a usable compatible target merely by passing
  JSON/schema checks. Surface input/dependency failure; no downstream invented requirements,
  zero-item perfect match, or extra retry allowance beyond the existing bounded parser policy.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q112 — Independent CandidateJobFitAnalysis and ResumeJobFitAnalysis

- **Status:** `ACCEPTED`
- **Decision:** DeepFit offers two independent analysis capabilities. CandidateJobFitAnalysis uses
  exact RequirementSet plus the current confirmed EvidenceBaselineSnapshot and admitted Candidate
  facts to evaluate the person against the Job. ResumeJobFitAnalysis uses exact RequirementSet plus
  an exact eligible formal ResumeVersion to evaluate that Resume alone against the Job. Each has
  independent durable identity, execution, failure, retry, and history. Resume Fit never requires
  an existing Candidate Fit result, and neither model task consumes the other as a prerequisite.
- **Batch UX:** The second-level task selection page offers Candidate Fit and Resume Fit separately
  for each Job. A task without a compatible saved result defaults selected; one with a compatible
  saved result defaults unselected. Explicitly selecting a rerun produces a new immutable Analysis
  as the current result, retaining previous results rather than overwriting their content.
  Failure of either analysis does not block or roll back the other.
- **Removed model:** Do not create ResumeCoverageAnalysis, a durable coverage score, a score
  difference, or a Candidate-Potential-greater-than-or-equal-to-Resume-Presented invariant.
  Facts omitted from a Resume may reflect normal editorial selection; a coverage ratio has no
  stable product authority. The independent results have no mandatory numerical ordering.
- **Advisor reuse:** When both compatible results exist, Advisor may derive a transient
  Requirement-level comparison, e.g. Candidate MATCHED versus Resume NOT_PRESENT, as an optimization
  hint. Do not persist a new CoverageAnalysis or turn such a comparison into an additional Fit Gate.
- **Rationale:** Person-to-Job and Resume-to-Job are independently useful questions, not successive
  levels of one score calculation.
- **Supersedes:** Q65's primary-presented/secondary-potential product dependency, Q68's joint dual-axis
  semantic assessment, Q69's CandidateJobFit-to-ResumeCoverage asset graph, and Q102's coverage/material
  scoring assumptions. These fully replaced records were removed. Refines Q46/Q51 scoring scope;
  deterministic policy-derived scores and exact-input historical audit remain valid.
- **Open boundary:** Resume-only prerequisite completeness and its assessment vocabulary need their
  own contract; no conclusion here treats absence from Resume as absence of real Candidate capability.
- **Current corrections — Q113/Q115/Q116:** Candidate Fit uses current saved baseline without
  KnowledgeConfirmation; Resume Fit uses its exact saved eligible Resume. Both use MATCHED / PARTIAL /
  MISSING / UNKNOWN, always interpreted within their own scope (replace the NOT_PRESENT example
  above with Resume-scoped MISSING). Targets execute serially per target and in parallel across
  targets; current display selects the latest successful compatible result, not latest user-intent
  arbitration between competing concurrent Runs.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### S22.1 — One bounded semantic task per AgentRun and one exact Job per Job-specific run

- **Status:** `ACCEPTED`
- **Decision:** An AgentRun serves one bounded semantic task. A Job-specific AgentRun binds one exact
  JobVersion; unrelated JDs never share a Run. Application-layer DeepFitBatch orchestrates isolated
  per-Job workflows and separately requested analysis runs. Multiple ModelInvocations inside a Run
  are consecutive steps of that same task (bounded loop, Tool use, or bounded repair), not a container
  for independent Jobs or independent Candidate Fit and Resume Fit tasks.
- **Rationale:** Task identity, Context isolation, budget, failure, and audit should align.
- **Refines:** Q35, Q47, Q83, Q94, Q110, and Q112; RequirementParse is an independent dependency run.
- **Runtime-maintenance refinement — Q132:** Semantic Context Compaction normally remains a Harness
  auxiliary Invocation in the current task's Run, sharing budget/fencing/recovery; it is not a separate
  business task. Independent background MemoryExtraction still requires its own AgentRun.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 23 — Saved Authority, Automatic Resume Synchronization, and Scoped Fit Results

### Q113 — Save confirms facts; remove KnowledgeConfirmation

- **Status:** `ACCEPTED`
- **Decision:** Delete the independent KnowledgeConfirmation mechanism, whole-Knowledge completeness
  confirmation workflow, and every Fit prerequisite based on it. Successful user Save establishes
  fact authority. Unsaved changes in 我的简历 or 求职资料库 remain page-local dirty drafts outside
  Candidate Knowledge. Leaving a dirty formal editing page requires Save / Discard / Cancel:
  Save persists the relevant Profile/Evidence/Resume versions, advances applicable current pointers
  and snapshots changed current Evidence; Discard abandons edits and leaves; Cancel stays editing.
  A failed Save must not be treated as a successful authority update.
- **Consumer boundary:** Application/Domain and downstream Skills consume exact saved authority,
  never page dirty state or uncommitted edits. CandidateJobFit runs on the current saved baseline;
  ResumeJobFit runs on its exact saved eligible ResumeVersion. Neither requires a further claim that
  Workspace Knowledge is complete. Existing fact validation, concurrency, grounding, admission, and
  stale-input checks remain distinct from the removed confirmation mechanism.
- **MISSING scope:** Candidate MISSING means no supporting fact found in current saved Candidate
  Knowledge, not that the person lacks the capability in reality. Q115 retains UNKNOWN for incomplete
  or unreliable inspection. Save confirms entered facts, not omniscience about the person's life.
- **Rationale:** Editor navigation owns dirty-work handling; business workflows see only saved inputs.
  A second completeness-confirmation workflow adds no desired product authority.
- **Supersedes:** Q78 and Q84 in full; all KnowledgeConfirmation creation, references, UNCONFIRMED
  completeness state, and completeness-confirmation Gates in Q66/Q72/Q73/Q77/Q82/Q85/Q97/Q108-Q112
  and other earlier clauses. Baseline snapshots, admission, model visibility, and audit remain.
- **Scope note:** Mentions of future Skills such as mock interviews describe the saved-input boundary,
  not permission to implement capabilities beyond the current product scope. Advisor drafts retain
  Q108's explicit formal-adoption requirement.
- **Draft durability — Q166:** Unsaved My Resumes ResumeDraft is temporary UI state; crash loss
  is accepted and no recovery checkpoint/autosave is promised. Normal navigation still requires
  Save / Discard / Cancel. Successful Save and Harness/business durability remain unchanged.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q114 — Automatically version every affected current Resume when facts are saved

- **Status:** `ACCEPTED`
- **Decision:** Saving a fact change E1/V1 → E1/V2 advances E1.current_version_id, creates the new
  current EvidenceBaselineSnapshot, and in the same formal save flow finds all current formal
  Resume roots using E1. Each gets a new immutable ResumeVersion using E1/V2 while preserving
  its experience selection, order, and presentation. Resumes not referencing E1 are unaffected.
  Previous ResumeVersions retain E1/V1 for historical analysis/chat/application/audit, but cease
  to be those roots' current formal versions.
- **Invariant:** Every available Resume root's current ResumeVersion references only current
  versions of its selected EvidenceItems. Do not leave a normally saved current Resume pending a
  separate manual update-to-current-facts operation.
- **No feedback loop:** Propagation reuses E1/V2. Synchronizing its content into a Resume does not
  create E1/V3 or another fact change; only a genuine subsequent user edit to fact text creates the
  next EvidenceItemVersion. New Resume snapshots do not rewrite already frozen historical inputs.
- **Rationale:** Synchronize formal current views at Save while preserving immutable history, rather
  than making users repair a persistent current-Resume/current-fact mismatch.
- **Supersedes:** Any Q108 or subsequent interpretation requiring users to manually refresh an old
  current Resume after shared facts change; rejects Q114's proposed separate manual refresh workflow.
  Narrows Q96/Q97 body-change versioning so automatic reuse of current facts is not a new fact edit.
- **Remaining boundaries:** The implementation-level all-affected-roots commit/concurrency boundary
  and analogous Profile-change propagation are not independently specified by this answer.
- **Remaining boundaries resolved — Q118-Q119:** All affected current Resume authority updates
  commit atomically with facts and baseline; Profile changes use the same propagation principle
  without changing career Evidence. No user-managed synchronization state is introduced.
- **Deletion refinement — Q151:** Delete Evidence means logical removal of an EvidenceItem, with
  affected current Resumes determined only by explicit Item inclusion. Confirm the listed impact,
  then atomically update baseline, directly affected current Resume versions/pointers and necessary
  derived intents. No per-version withdrawal UI, sentence/Claim dependency graph, or old-version
  fallback. Historical assets stay immutable; new formal work consumes current eligible inputs.
- **Selection refinement — Q163:** v1 Resume inclusion is whole EvidenceItem experience body from
  its current version, plus experience selection/order/layout. No independent per-Resume bullet
  selection mapping or alternate fact text. Fine EvidenceRef grounding and Profile display/privacy
  rules remain; they do not imply independently selectable career-body fragments.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q115 — Shared four states with strictly separate Candidate and Resume scopes

- **Status:** `ACCEPTED`
- **Decision:** Both Fit types use MATCHED / PARTIAL / MISSING / UNKNOWN. Candidate MISSING means
  no Requirement-supporting fact found in current saved Candidate Knowledge. Resume MISSING means
  no supporting expression found after complete inspection of the exact Resume's admitted content.
  Neither state implies the other or proves real-world incapability. UNKNOWN records the reason
  a reliable decision cannot be made, including privacy exclusion, truncation, incomplete inputs,
  or unverifiable model results; incomplete inspection cannot become MISSING.
- **Resume inputs and citations:** Resume Fit sees exact RequirementSet plus exact ResumeVersion
  and necessary grounding metadata only. Grounding validates already expressed facts; it cannot
  supply unexpressed Candidate Evidence to improve Resume Fit. MATCHED/PARTIAL retain exact
  ResumeVersion and ResumeClaim/content-pointer support. MISSING has no positive support citation:
  retain exact Requirement, ResumeVersion, and analysis/Context lineage proving the inspected scope.
  UNKNOWN additionally records its uncertainty reason.
- **Rationale:** Shared vocabulary simplifies the UI while the analysis type and exact input scope
  prevent capability and Resume presentation from being conflated.
- **Supersedes:** The proposed Resume-specific NOT_PRESENT status from Q115 and that example in
  Q112. Removes any automatic conversion between Candidate-scoped and Resume-scoped negatives.
  Refines Q72/Q82 admission/completeness handling under Q113's saved-authority model.
- **Score availability — Q168:** Valid assessments/reasons/lineage may be persisted without a
  comparable total score or normal score ranking when deterministic ScorePolicy cannot justify one.
  Unavailable is not zero, failed Analysis, or permission to label an old result's score as this
  result. Score availability thresholds/representation remain later Contract work.
- **Formal writeback:** `spec.md`, `contracts/*`, `acceptance.md`

### Q116 — Serialize each Fit target and retain the latest successful compatible result

- **Status:** `ACCEPTED`
- **Decision:** Manage Candidate Fit and Resume Fit results separately, never via a generic
  latest_deepfit. Resume targets distinguish actual exact ResumeVersions (e.g. R1/V3 versus R2/V1).
  Allow parallel work across different targets but only one effective RUNNING analysis per target.
  UI disables repeat execution until success, failure, cancellation, or timeout; backend idempotency,
  a unique running constraint, or CAS enforces the same invariant despite multiple tabs, retried
  requests, or other concurrent clients.
- **Result selection:** A rerun creates a new immutable Analysis. On successful compatible completion
  it becomes that target's current displayed result; older analyses remain historical. Failed reruns
  do not remove a previously successful still-compatible result, and UI may show both that result
  and the latest failure. Stale-input outputs cannot become current.
- **Rationale:** Serial execution within a target avoids competing-current-intent arbitration while
  preserving independent targets, audit, retries, and useful previous results.
- **Rejects:** Q116's proposed latest-explicit-intent arbitration across overlapping valid same-target
  Runs. The system prevents that overlap rather than defining which competing completion wins.
- **Refines:** Q112's task selection, rerun, and independent-result contract. Multiple-client
  robustness does not expand the single-user local product into a multi-tenant system.
- **Recovery refinement — Q122:** The shared Harness, not Fit-specific code, reconciles abandoned
  execution, releases slots for ended Runs, and fences late writers. Outcome-unknown remote model
  calls require explicit Retry into a new Run; slot release does not imply remote work stopped.
- **Score availability — Q168:** Valid assessments/reasons/lineage may be persisted without a
  comparable total score or normal score ranking when deterministic ScorePolicy cannot justify one.
  Unavailable is not zero, failed Analysis, or permission to label an old result's score as this
  result. Score availability thresholds/representation remain later Contract work.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q117 — Mandatory bounded runtime validation; formal parser-release evaluation deferred

- **Status:** `ACCEPTED`
- **Decision:** Preserve Q111's independent exact-JD LLM extraction, fixed schema/prompt/policy,
  deterministic validation, at most one bounded repair, immutable RequirementSet lineage, and sole
  structured-requirements input for downstream tasks. Validators check schema, required fields,
  enums, source spans, emptiness, duplicates, and explicitly verifiable structural constraints.
  Structural validity is not proof of zero semantic omission. Necessity and ALL_OF/ANY_OF logic
  may remain UNKNOWN when uncertain instead of being guessed.
- **Failure:** A second invalid output fails closed for the affected Job; do not persist an untrusted
  Set, score partial requirements, or let downstream tasks supplement requirements from full JD.
  Successfully parsed compatible Sets are durably reusable.
- **Quality process:** Use real JD tests, manual inspection, and development iteration to detect
  omitted requirements and necessity/logic mistakes and improve prompt/schema/validation/model
  choices. v1 does not mandate an offline human-annotated ParserVersion publication Gate. Formal
  annotated evaluation datasets, numeric thresholds, or parser release certification are deferred
  until a demonstrated need, not runtime architecture dependencies.
- **Rationale:** Require structurally valid, bounded-failure, traceable execution without prematurely
  building a formal semantic-evaluation release process.
- **Rejects:** Q117's recommendation that an annotated ParserVersion release evaluation is mandatory
  in v1. This does not remove deterministic tests or general repository verification requirements.
- **Resolves:** Q111's remaining parser-quality process question; refines Q82 only where it might
  otherwise be read as mandating this particular parser-release mechanism.
- **Usable dependency Gate — Q171:** No usable Requirement means fail fast before downstream
  Fit. An empty/non-assessable result cannot become a usable compatible target merely by passing
  JSON/schema checks. Surface input/dependency failure; no downstream invented requirements,
  zero-item perfect match, or extra retry allowance beyond the existing bounded parser policy.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 24 — Atomic Propagation, Shared Skill Contracts, and Durable Harness Recovery

### Q118 — Atomically save facts and every affected current Resume

- **Status:** `ACCEPTED`
- **Decision:** One local database transaction commits the changed EvidenceVersion/current pointer,
  new baseline, every affected current ResumeVersion/current pointer, and corresponding GroundingSets.
  Validate revisions and reconciliation first. Any authority write failure rolls back the whole Save;
  the editor retains the user's changes and must not leave as if Save succeeded. There is no
  successfully saved authority state with some current Resumes waiting for asynchronous synchronization.
- **Concurrency and derivatives:** Revisions protect against concurrent fact/Resume edits. Propagation
  reuses the saved EvidenceVersion and never recursively extracts or versions facts again. PDF render,
  indexes, and caches run after commit; derivative failure does not undo facts, but required unavailable
  materials prevent application readiness. UI may show which Resumes will change without requiring
  separate repeated confirmation for each Resume.
- **Historical boundary:** Do not automatically rewrite analyses, chat Turns, Preparation-selected
  exact references, or frozen execution Snapshots. Their compatibility and explicit-adoption rules
  remain distinct from current Resume root propagation.
- **Rationale:** Current facts and all affected current Resume authorities must become visible together,
  while rebuildable derivatives and historical selections retain independent lifecycles.
- **Source:** User accepted the complete Q118 recommendation.
- **Resolves:** Q114's all-affected-root atomicity and concurrency boundary; extends Q73.
- **Durable derivatives — Q147:** Register necessary DerivedWorkItem(PENDING) intents in the
  same short SQLite authority transaction, after Prepare determines required work. Actual render/
  preview/index/cache execution stays post-commit and safely idempotent; stale outputs cannot
  overwrite current artifacts. Intent persistence closes the commit-before-scheduling crash window.
- **Deletion refinement — Q151:** Delete Evidence means logical removal of an EvidenceItem, with
  affected current Resumes determined only by explicit Item inclusion. Confirm the listed impact,
  then atomically update baseline, directly affected current Resume versions/pointers and necessary
  derived intents. No per-version withdrawal UI, sentence/Claim dependency graph, or old-version
  fallback. Historical assets stay immutable; new formal work consumes current eligible inputs.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q119 — Propagate Profile changes without changing career Evidence

- **Status:** `ACCEPTED`
- **Decision:** Profile Save advances its current immutable CandidateProfileVersion and atomically
  creates new current ResumeVersions/GroundingSets for Resumes referencing it. Preserve each Resume's
  displayed-field choices, experience selection, and presentation; updating a contact does not add
  fields the Resume previously chose not to display. Historical Resumes and completed applications
  retain their original exact Profile/material references.
- **Analysis boundary:** Profile changes alone do not create EvidenceItemVersions or alter the career
  EvidenceBaselineSnapshot. Candidate Fit is not invalidated by contact-only edits outside its inputs.
  Resume Fit, render, and application materials follow their own exact-input compatibility rules;
  an old result must not silently be relabeled as evaluating a new ResumeVersion.
- **Rationale:** Current identity/contact content must stay synchronized just as career facts do,
  without conflating Profile authority with career Evidence authority.
- **Source:** User accepted the complete Q119 recommendation and explicitly required automatic sync.
- **Refines:** Q54, Q114, and Q118.
- **Durable derivatives — Q147:** Register necessary DerivedWorkItem(PENDING) intents in the
  same short SQLite authority transaction, after Prepare determines required work. Actual render/
  preview/index/cache execution stays post-commit and safely idempotent; stale outputs cannot
  overwrite current artifacts. Intent persistence closes the commit-before-scheduling crash window.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q120 — One Harness with Skill-scoped action-level Tool authority

- **Status:** `ACCEPTED`
- **Decision:** RequirementParse, CandidateJobFit, ResumeJobFit, and ResumeAdvisor use independent
  Skill Contracts on one shared Agent Harness Runtime. Each declares input requirements, Context
  projection, output schema, budget, validation, interaction policy, and allowed Tools/actions.
  ToolRegistry defines available system capabilities; registration never grants a Run permission.
  Exposed actions must satisfy ToolRegistry intersected with Skill allowlist and runtime
  admission/permission, further narrowed by ContextStrategy under Q121. Prefer action-level grants
  such as resume.read, evidence.read, and jobs.detail rather than every action of a Tool.
- **Ownership:** Parsing and Fit Skills are headless; Advisor receives Turns through ChatSession.
  Harness owns execution machinery: AgentLoop, ModelInvocation, ContextFrame, Tool admission, budget,
  cancellation, and audit. It does not own Candidate Knowledge, Resume, Preparation, or application
  business mutation authority. Application owns EnsureRequirementSet, dependency preparation, exact
  input freezing, batch scheduling, and validated business-result persistence. Fit cannot launch
  another Fit, advance application, or change formal facts on its own.
- **v1 scope:** Use explicit code registration of Skills and Tools; no dynamic plugin marketplace,
  general workflow editor, or universal career Agent.
- **Rationale:** Skill defines this task's permissions, Tools define capabilities, Harness executes
  safely, and Application controls business workflows and authority.
- **Refines:** S7.1, S17.4, Q47, Q83, Q94, and S22.1. Action examples are illustrative, not a final
  exhaustive Tool catalog or field schema.
- **Extended by Q126-Q127:** Tools are typed/scoped Business Actions with pre-call validation and
  post-result admission, never generic terminal/resource access. MemoryExtraction is an additional
  independent headless Skill/Run; only its admitted candidates may reach the dedicated Memory store.
- **Refined by Q128/Q132:** A user-confirmed fact-change Tool delegates to Application under actual
  Skill/runtime permission; the model cannot assert its own authorization. Context maintenance may
  use auxiliary Invocations within the current Run without becoming a new Skill/task by default.
- **Clarified by Q138/Q139:** ResumeAdvisor itself performs optimization; do not duplicate the
  semantic task as suggest_improvement. Skill is protected Control Context with progressive guidance;
  Business Tool actions are scoped capabilities, not prompt-wide implicit data access.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q121 — Full-Context Fit by default; retrieval Tools only in a deferred mode

- **Status:** `ACCEPTED`
- **Decision:** Application orchestrates three independent Skills. EnsureRequirementSet reuses a
  compatible exact-JobVersion Set or invokes RequirementParse separately: one complete-JD extraction,
  at most one validation-triggered bounded repair, then immutable persistence. Candidate Fit and
  Resume Fit share that exact Set and never independently parse JD.
- **Resume Fit:** Use Full Context with exact RequirementSet and ResumeVersion. One structured
  evaluation and at most one deterministic-validation-error repair; no autonomous Tool loop.
- **Candidate Full Context:** ContextStrategyPolicy selects FULL_CONTEXT when the complete admitted
  current Candidate Knowledge fits the real Context budget. Application/Context Builder supplies the
  exact RequirementSet and all admitted Evidence. One structured evaluation and at most one repair;
  do not expose Evidence Tools to the model.
- **Extension boundary:** Only genuinely over-budget Candidate Knowledge calls for a future
  REQUIREMENT_RETRIEVAL mode with bounded Agentic RAG. That mode may expose read-only evidence.search,
  evidence.read, and optionally evidence.get_item for model-directed Requirement queries under step,
  token, deadline, admission-scope, and privacy limits. Effective actions are the intersection of
  ToolRegistry, Skill allowlist, ContextStrategy, and runtime admission/permission.
- **No business writes:** DeepFit Tools remain read-only: no Evidence/Resume writes, baseline
  mutation, Preparation editing, or external application. Application persists validated immutable
  analyses. Registering a reading capability as a Tool does not expose it in every mode.
- **Rationale:** Small saved inputs need bounded structured evaluation, not automatic autonomous
  retrieval; larger-data capability can later reuse the same permission-controlled Harness.
- **Supersedes/narrows:** Earlier assumptions that a complete Retrieval Mode is a required v1 fallback
  when Full Context exceeds budget. Full Context remains v1; S24.1 defers Agentic RAG design details
  and implementation. Exact v1 over-budget behavior remains open rather than silently truncating.
- **v1 overflow resolved by Q123:** If the complete serialized task input and required reserves do
  not fit, stop before invocation; no silent truncation, model switch, or unavailable Retrieval fallback.
- **Acquisition and dependencies — Q139/Q142:** These v1 headless Skills use EAGER_EXACT inputs,
  unlike Advisor's LAZY_TOOL. EnsureRequirementSet uses database-backed single-flight for a common
  exact parse target; owner pays and waiters reuse, with no automatic ownership transfer on failure.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q122 — Shared durable-boundary recovery, ownership, replay safety, and fencing

- **Status:** `ACCEPTED`
- **Decision:** Harness Runtime recovers only from durable boundaries, not arbitrary code positions.
  Persist and commit dispatch intent before a remote Invocation; persist a complete durable response
  before subsequent parse/validation/business-result processing. Before dispatch, frozen-input
  validation can permit safe continuation. A recorded dispatch intent without durable response is
  outcome-unknown for model/outcome-sensitive remote calls, even if the crash might have preceded
  the network send: do not silently replay. End the old Run, release its effective target slot, and
  require explicit user Retry into a new AgentRun. A complete durable response permits continuation
  of local processing without another model call.
- **Ownership and fencing:** A Run has execution ownership and an execution_generation fencing token.
  Every canonical-state-affecting submission must confirm an active valid Run and matching generation.
  Timeout, cancellation, recovery, or ownership revocation invalidates the former generation; late
  coroutines cannot commit current results. Local cancellation does not prove remote execution stopped,
  and unknown usage must not be recorded as zero.
- **Startup reconciliation:** Runtime examines unfinished Runs owned by prior runtime instances and
  their durable Invocation states. It safely claims/resumes eligible local work or ends interrupted/
  outcome-unknown Runs and releases concurrency slots. Explicit Retry creates a new Run with retry
  lineage; it never revives an outcome-unknown Run as RUNNING.
- **Replay ownership:** LangGraph Checkpoint restores workflow state; Harness Invocation Runtime
  decides model/Tool replay safety. Tool Contracts declare replay semantics, such as SAFE_REPLAY for
  local reads, IDEMPOTENT_REMOTE where remote idempotency is actually reliable, and OUTCOME_SENSITIVE
  for model or external actions whose unknown outcomes must not be blindly repeated. A checkpoint
  or generic Tool label does not grant business authorization or override existing application/
  Browser Executor approval and unknown-outcome rules.
- **Rationale:** Persisted intent/response boundaries expose ambiguity instead of causing duplicate
  remote work; execution fencing prevents old owners from publishing after cancellation or takeover.
  This is common Harness capability, not Fit-only recovery.
- **Refines:** Q116 concurrency recovery, Q83/Q94 invocation lineage, and S22.1 bounded tasks.
  Atomic canonical publication and normal Domain stale checks remain necessary alongside fencing.
- **Field-scope note:** run_id, execution_generation, runtime_instance_id, retry_of_run_id, and the
  conceptual AgentRun/Invocation/ContextFrame diagram illustrate required semantics, not a frozen
  exhaustive field list or finalized transition table. See S24.2.
- **Detailed design:** [Harness Recovery](harness/recovery.md) preserves the full Q122 boundary,
  conceptual object map, and Q125 four-layer retention integration. [Harness Budget](harness/budget.md)
  specifies why releasing an interrupted target does not release unknown-cost exposure.
- **Local mutation result — Q156:** Recover confirmed Proposal application from persisted mutation
  result. A committed fact update is not undone or made unknown by a subsequent failed model reply.
  The same Proposal cannot create duplicate versions; remote model Retry still obeys this record.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### S24.1 — Defer Agentic RAG implementation and detailed design until after basic v1

- **Status:** `DEFERRED`
- **Decision:** Retain Q121's permission-limited Requirement-level Agentic RAG extension in the
  architectural direction, but do not implement it or continue detailed RAG grilling for v1.
  Revisit after the basic v1 implementation. This is not authority to omit Evidence silently or
  claim a nonexistent retrieval fallback is available.
- **Rationale:** Complete the small-data Full-Context product before expanding retrieval complexity.
- **Refines:** S15.1, Q80, and Q121; canonical Evidence authority/admission remain unchanged.
- **Formal writeback:** `architecture.md`, `contracts/*`, `progress.md`

### S24.2 — Architectural-contract Grill now; exhaustive field design in a separate later Grill

- **Status:** `ACCEPTED`
- **Decision:** This entire Grill settles architectural contracts, responsibilities, authority,
  dependencies, failure/recovery semantics, and core invariants. Important fields already mentioned
  illustrate those commitments but do not imply a complete implementation schema. Do not expand
  this interview into exhaustive field/type/enum/table definitions or detailed transition matrices.
- **Follow-up boundary:** After this architecture Grill concludes, a separate Grill must derive
  detailed contracts from the final boundaries. Review AgentRun identity/Skill/inputs/concurrency/
  ownership/retry/budget; ModelInvocation ordering/Context/dispatch/provider metadata/durable response/
  usage certainty; ToolInvocation actions/argument lineage/replay/side effects/result; ContextFrame
  exact messages/ToolResult/compaction/redaction/token accounting; and Runtime claim/revoke/fencing/
  reconciliation/cancel/retry transitions. This list is a future review agenda, not new frozen fields.
- **Rationale:** Settle architecture before enumerating schemas, while ensuring eventual detailed
  contracts cannot stop at vague AgentRun/Runtime labels.
- **Supersedes:** Any interpretation of the earlier Grill plan or Q122's conceptual diagram requiring
  field-by-field finalization during this current interview. Does not launch a new thread automatically.
- **Formal writeback:** `development.md`, `contracts/*`, `progress.md`

## Round 25 — Context Capacity, Budget Reservation, Payload Privacy, and Harness Memory

### Q123 — Fail visibly before dispatch when v1 Full Context cannot fit

- **Status:** `ACCEPTED`
- **Decision:** Check actual serialized complete inputs, system/instruction overhead, output reserve,
  and safety margin before invocation. If the task cannot fit, stop it with a clear capacity reason.
  Do not silently trim Evidence, generate a formal score/MISSING from omitted inputs, switch models,
  or enter unimplemented Retrieval. Resume Fit also requires the check despite normally small inputs.
  One oversized Candidate task does not block an independently feasible Resume task.
- **User path:** Where an already supported larger-context configuration exists, the user may select
  it explicitly and retry. Do not require deletion of real facts to accommodate the limit.
- **Rationale:** Full Context must describe actual complete admitted inputs, not hide a capacity loss.
- **Source:** User accepted the complete Q123 recommendation.
- **Resolves:** Q121/S24.1 v1 overflow behavior; Retrieval remains deferred.
- **Detailed design:** [Harness Budget — Context capacity](harness/budget.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q124 — Shared ExecutionBudget, local Run limits, and atomic Invocation reservations

- **Status:** `ACCEPTED`
- **Decision:** Application owns one operation-level ExecutionBudget; AgentRuns retain local
  call/step/token/deadline limits. Before each charged or limited Invocation, Harness atomically
  checks and reserves against total budget minus settled usage minus outstanding reservations.
  Parsing, both Fits, repair, and future Retrieval Invocations count actual work; reused exact
  RequirementSets do not create duplicate parse charges. Settlement uses actual usage and releases
  excess reservation; higher-than-reserved cost requires a policy still to be defined.
- **Unknown outcomes:** Dispatched timeout/crash cannot count as zero usage or immediately release
  all exposure. Explicit new-Run Retry needs fresh admission. Exhaustion stops undispatched work,
  never rolls back already durable independent results.
- **Rationale:** Per-Run limits alone cannot stop concurrent tasks from overspending a shared balance.
- **Deferred:** Amounts, thresholds, allocation ratios, concrete schema, and overrun/reconciliation
  details; no complex billing system.
- **Detailed design:** [Harness Budget](harness/budget.md).
- **Ownership extended — Q130/Q132:** One Budget Runtime serves separate foreground operation and
  BackgroundMemoryBudget owners, with foreground-priority capacity/headroom admission. Current-Run
  compaction charges that Run's budget, not background Memory. The atomic reservation/settlement and
  unknown-exposure rules remain unchanged; see [Budget](harness/budget.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q125 — Four storage layers with explicit payload availability

- **Status:** `ACCEPTED`
- **Decision:** Separate Business Durable Assets, protected Harness Recovery Payload, lightweight
  durable Harness Audit Metadata, and minimal Operational Logs/Telemetry. Preserve recovery-needed
  exact ContextFrames, complete business responses, and necessary ToolResults until the unfinished
  recovery boundary ends; completed payloads follow independent retention. Do not store HTTP secrets
  or print sensitive business contents in ordinary logs. Keep identities/lineage/hashes/known-or-unknown
  usage/timing/status metadata without pretending those replace complete deleted payloads.
- **Cleanup:** Payload purge never deletes formal Analysis/Resume/Evidence/application history.
  Explicit availability distinguishes available from purged payload; never recreate old input from
  current assets and claim it is the historical exact Frame.
- **Rationale:** Recovery durability, auditability, and business permanence are different obligations.
- **Deferred:** Retention periods, concrete availability fields, and physical storage choices.
- **Detailed design:** [Harness Storage, Retention, and Audit](harness/storage.md).
- **Refines:** Q83/Q94/Q122 exact-input persistence without requiring indefinite raw-payload retention.
- **Retention resolved — Q136:** Active Recovery Dependencies stay pinned until their safe recovery
  boundary ends. Historical source references may outlive payloads; new permitted exact-business
  reads are new ToolInvocations, not reconstructed old results. Report unavailable necessary sources
  without guessing or automatically replaying external accesses.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q126 — Typed scoped Business Tools, never a generic execution surface

- **Status:** `ACCEPTED`
- **Decision:** v1 exposes typed Business Tool Actions through controlled Ports, not Bash/Shell,
  arbitrary SQL, files, or HTTP. Before every call, validate action permission, argument schema,
  object references, resource scope, Run authority, and runtime policy; model-supplied IDs/paths/URLs
  do not grant permission. Readmit ToolResult for sensitivity/privacy/Context before the next Frame.
  JD, Resume, webpage, quoted/chat content, and ToolResult instructions cannot expand Tool authority.
- **External effects:** Collection, Browser execution, application and other external effects stay
  in their explicitly authorized Application workflows and replay/safety policies, not a universal
  model Tool. Examples do not add email or other unimplemented capabilities to v1.
- **Rationale:** Skill grants possible actions; Harness authorizes the particular call; Application
  retains business authority. Tools are controlled capabilities, not a general-purpose terminal.
- **Refines:** Q19/Q120/Q121; no external implementation claims were independently verified here.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q127 — Collaboration Memory with independent extraction and deterministic admission

- **Status:** `ACCEPTED`
- **Decision:** Keep Business Authority, durable Session Memory, Harness Long-term Memory, and
  derived Memory retrieval distinct. Context Engineering/Compaction is an independent subsystem.
  Career/search/Resume/application facts remain in business objects. Long-term Memory admits only
  PREFERENCE, FEEDBACK, WORKING_STYLE, and REUSABLE_AGENT_LEARNING, not USER_FACT.
- **Automatic path:** Independent headless MemoryExtraction proposes candidates from eligible durable
  user-facing Turns; MemoryWriteAdmissionPolicy accepts, keeps Session-local, routes to business, or
  rejects. It has separate background budget/failure/recovery ownership. Main chat does not silently
  write long-term entries; Q129 requires supported user sources rather than assistant inference.
- **Read and management:** A small derived MemorySummary plus on-demand entries passes Skill/privacy
  admission. Fits/RequirementParse receive none. Q139 separates Auto Learning, Recall, and explicit
  user View/Add/Edit/Delete/Clear All without extraction. User management still cannot store career
  facts as Memory; future Skill examples do not expand v1.
- **Lifecycle and scope:** Minimal provenance/supersession/invalidation/removal, non-resurrecting
  forgetting, no all-chat automatic scanning/vectorization, complex consolidation, or Memory graph.
- **Authority:** Business facts, execution permissions, and interaction priority are separate rules
  (Q128). Session statements may support natural conversation (Q133/Q138), never implicit business
  Save. Context checkpoints do not directly copy Long-term Memory (Q139).
- **Rationale:** Reusable collaboration information improves interaction without another fact store.
- **Refinements/cleanup:** Q128-Q139 replace the original six-layer placement and single priority
  chain; only those obsolete clauses are removed. The Memory capability itself remains accepted.
  Candidate Agentic RAG stays deferred, and exhaustive fields await the later Grill.
- **Detailed design:** [Harness Memory](harness/memory.md); [Context](harness/context.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### S25.1 — Detailed per-module Harness design records

- **Status:** `ACCEPTED`
- **Decision:** Preserve important Harness module designs in separate files under
  `docs/design/harness/`, initially `memory.md` (requested spelling), `recovery.md`, and
  `budget.md`. They contain the complete accepted architectural design, not only condensed Q entries.
  The Decision Register retains short decisions, supersession relationships, and links.
- **Authority boundary:** These are detailed design records inside the existing design work area,
  not new final Sources of Truth or permission to edit formal documents outside the agreed stages.
  Clearly label accepted boundaries, genuinely open architecture choices, and deferred field details.
- **Rationale:** Module-level recovery after handoff needs more detail than the compact Decision
  Register while preserving the six formal document categories and S24.2's architecture-only scope.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 26 — Confirmed Fact Tools, Durable Memory Work, and Independent Context Engineering

### Q128 — Separate fact, permission, and interaction rules; controlled confirmed fact writes

- **Status:** `ACCEPTED`
- **Decision:** Saved Business Authority governs facts. Skill allowlist, runtime policy, and required
  approval govern actions. Interaction style follows current explicit user instruction, then admitted
  Long-term Memory, then derived conversation summary/checkpoint. A one-off override does not update
  Memory; an explicit durable preference becomes a candidate for Memory admission.
- **Fact-write path:** Q133 permits Session-local discussion without immediate Save prompts.
  When the user explicitly and unambiguously specifies a Save, an authorized Skill/Run may directly
  call a typed action such as
  candidate_knowledge.update_evidence, delegating to UpdateCandidateKnowledge. The command creates
  the new EvidenceVersion/current pointer/baseline and synchronizes affected current Resumes through
  the accepted atomic save path. Model arguments do not supply authorization. No preference waives
  fact-conflict handling, MaterialApproval, ExecutionApproval, or runtime permissions.
- **Rationale:** Memory changes how to collaborate; business sources establish facts; policy controls
  action. Explicit user confirmation can authorize a typed business write, not arbitrary model mutation.
- **Scoped supersession:** Refines Q41/Q85's draft/page-only interpretations; their prohibition on
  implicit model/chat authority remains. Fit remains read-only and MemoryExtraction cannot confirm
  facts. Refines Q127's one-chain authority shorthand.
- **Detailed design:** [Memory](harness/memory.md).
- **Scoped supersession — Q133:** Do not interrupt new/conflicting Session assertions merely to
  request a formal update. Discuss them naturally as Session information. Enter the write path on
  explicit Save/change intent or an authoritative business prerequisite; clear Save intent itself
  is confirmation, with clarification only for unresolved target/content/conflict. No duplicate
  confirmation is required. Current runtime permission and Application validation still apply.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q129 — Conservative user-sourced automatic Long-term Memory admission

- **Status:** `ACCEPTED`
- **Decision:** v1 automatic long-term acceptance prioritizes explicit traceable durable user
  expression/correction. Source evidence and scope matter; the extractor's type label alone is
  insufficient. Clear “in future, show a diff” can be accepted without another per-entry popup.
  One-off instructions stay Session-local. Repeated behavior, assistant guesses/suggestions, and
  generated summaries alone do not establish a durable user preference. Weak/ambiguous candidates
  take KEEP_SESSION_ONLY / REJECT instead of default persistence.
- **Rationale:** Limited automatic memory must not become an inferred, self-reinforcing user profile.
- **Source:** User accepted the complete Q129 recommendation.
- **Refines:** Q127 MemoryWriteAdmissionPolicy, including REUSABLE_AGENT_LEARNING; the category remains
  but its admission requires the same supported-source discipline.
- **Detailed design:** [Memory](harness/memory.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q130 — Durable pending extraction and separate low-priority background budget ownership

- **Status:** `ACCEPTED`
- **Decision:** With Auto Learning enabled, new completed durable user-facing Turns create
  persisted pending source ranges. Coalescing/debounce/idle/accumulated-range Trigger Policy schedules
  independent MemoryExtraction Runs; timers are not work authority. Progress advances only after
  successful extraction processing. Do not depend on a Session-ended event, invoke after every Turn
  unconditionally, or backfill all pre-enablement chats. Background outputs never retrigger extraction.
- **Sources/failure:** Minimize input to relevant user messages, necessary assistant responses, and
  explicit correction/confirmation evidence, not full Tool/Evidence/web/transcript dumps. Extraction
  has independent Context, Skill, recovery, and budget. Failure/insufficient budget/unknown outcome
  never changes foreground success or authorizes endless retry. Disabling/pausing stops new automatic
  extraction Runs without deleting stored entries.
- **Budget extension:** Shared Harness Budget Runtime has multiple scopes/owners. DeepFit operations
  and Advisor Turns own foreground envelopes; merged multi-Turn extraction charges BackgroundMemoryBudget,
  never the final foreground Turn. Shared atomic reservation/settlement and conservative unknown-usage
  handling apply to both. Background dispatch also requires Provider headroom, protected foreground
  capacity, and runtime concurrency. Budget permits spending; capacity decides whether now is suitable.
  Foreground work takes priority. Budget shortage may leave work pending or record non-execution under
  later policy; no complex scheduler is required.
- **Rationale:** Durable work survives restart; maintenance has an honest cost owner and cannot starve
  the user or silently spend an unrelated operation's budget.
- **Deferred:** Trigger values, cursor schema, concrete amounts/headroom percentages, and scheduling
  policy details. Future Skill examples do not expand current product scope.
- **Refines:** Q124 without replacing its accounting mechanism; Q127's trigger/budget frontier.
- **Detailed design:** [Memory](harness/memory.md), [Budget](harness/budget.md).
- **Refined by Q139:** Auto Learning controls scheduling/automatic publication; Recall independently
  controls model-visible Memory on each Frame. Explicit validated user management is separate.
  Retained entries remain and reenablement does not default to disabled-period extraction.
- **Range isolation — Q169:** Failed/unknown extraction batches do not block newer source work
  or silently reenter automatic coalesced batches. Only explicit Retry reprocesses their old range.
  Keep success/failure/pending distinct; a prefix cursor example cannot imply false successful
  advancement. Undispatched budget/capacity waiting remains pending.
- **Source deletion — Q170:** Deleted Sessions cannot start new extraction or publish late
  candidates; recheck sources at dispatch/publication and cancel where possible. Existing Memory
  remains independent; already transmitted content/unknown usage cannot be erased by local deletion.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q131 — Deliberate forgetting must prevent source-driven resurrection

- **Status:** `ACCEPTED`
- **Decision:** Forgotten/invalid entries stop entering new Context and their summaries/indexes stop
  presenting them as valid. Old source Turns must not recreate deliberately forgotten memory; pending
  extractors recheck forgetting before commit. Minimal anti-recreation/source-range constraints may
  remain without retaining deleted raw content forever. Later explicit user permission may establish
  new memory. Chat deletion and Memory deletion are distinct, explained operations; neither removes
  formal business assets. Already transmitted remote input cannot be retracted by local deletion;
  historical recovery payload follows its own explicit retention policy.
- **Rationale:** Forgetting is a future extraction/rebuild constraint, not temporary UI hiding.
- **Source:** User accepted the complete Q131 recommendation.
- **Deferred:** Marker representation, logical/physical deletion choice, and exact retention values.
- **Detailed design:** [Memory](harness/memory.md), [Storage](harness/storage.md).
- **Background learning boundary — Q170:** Source Session deletion also prevents new automatic
  extraction/publication from its pending or in-flight ranges, with source checks before dispatch
  and publication. Existing accepted Memory retains its independent lifecycle; preserve truthful
  remote usage/recovery/audit and do not claim already-sent data was retracted.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q132 — Context Compaction outside Memory; deterministic stages and bounded auxiliary calls

- **Status:** `ACCEPTED`
- **Decision:** ChatSession/Turn preserves durable history; separate Context Engineering reduces
  model-visible transient/history content. Classify protected exact business/user/Skill/permission
  inputs first. Apply ToolResult externalization, history-window trimming, and structured/micro
  compaction without LLM calls. Only if still over target allow bounded semantic compaction into
  ContextCheckpointSummary. Trigger and target watermark are distinct (hysteresis); numerical
  thresholds remain unfrozen. Preserve durable source refs and do not delete Session history.
- **Exactness:** Lossy operations cannot replace exact Resume, admitted analysis Evidence,
  RequirementSet, current user instruction, permission/approval, or other required business state.
  Reinject exact sources rather than newer versions or summaries. If protected Full-Context Fit
  inputs alone exceed budget, Q123 still fails closed; Compaction is not Retrieval.
- **Ownership/publication:** Semantic compaction normally is an auxiliary ModelInvocation inside the
  current AgentRun, sharing budget, generation, deadline, audit, and Q122 recovery. Keep old sources
  recoverable; generate candidate, validate required structure/goal/refs/state, durably publish,
  then use in a new Frame. Failed/unknown work never publishes an untrusted checkpoint or silently
  repeats a model call. Background MemoryExtraction remains a separate Run and budget owner.
- **Reactive rescue:** An explicit Provider Context-size rejection permits more aggressive
  compaction of eligible transient content and at most one admitted retry; another rejection fails
  closed. This exception does not cover timeout or unknown outcome. Total auxiliary/repair/rescue
  allowances are fixed per Run by Q135, jointly constrained by total budget.
- **Scoped supersession:** Removes Q127's Memory L2 Session Compaction and the SessionSummary name.
  Corrected source layers are Business Authority, Session Memory, Long-term Memory, and derived Memory
  retrieval, with independent Context Engineering. Rejects Q132's recommendation to make ordinary
  compaction a separate AgentRun; refines S22.1 to permit same-task runtime maintenance.
- **Rationale:** Keep the durable past, cross-session collaboration, and next-invocation Context
  separate; reduce cheap transient material before paid semantic maintenance without distorting facts.
- **Detailed design:** [Context Engineering](harness/context.md); updated [Memory](harness/memory.md),
  [Budget](harness/budget.md), [Recovery](harness/recovery.md).
- **Resolved by Q135/Q136:** Semantic compaction and reactive retry each have at most one allowance
  across the entire Run, jointly constrained by Run totals and enforced by ModelInvocationRuntime.
  A checkpoint reference pins only still-needed Active Recovery Dependencies, not terminal historical
  payload forever. Unavailable historical content must be handled explicitly.
- **Context acquisition — Q139:** Protect required EAGER_EXACT headless inputs, not all business
  data in every interactive Frame. Old LAZY_TOOL results can be externalized and read again at exact
  versions. Direct Long-term Memory blocks are not checkpoint source material.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### S26.1 — Dedicated Context and Storage records, with synchronized module ownership

- **Status:** `ACCEPTED`
- **Decision:** Record the complete Q132 Context Compaction module in context.md; extract Q125's
  reaffirmed four-layer storage/retention design into storage.md. Storage is broader than logs,
  so log.md would misname its scope. Memory no longer owns Compaction; Recovery links to Storage
  while retaining its replay/durability boundaries. Budget incorporates Q130's separate owners and
  Q132's same-Run auxiliary cost. Keep all five module records consistent without changing formal docs.
- **Clarification:** The user's final reference to “Q131 budget changes” refers to the budget
  expansion supplied under Q130; Q131 itself confirms forgetting semantics. Both are preserved.
- **Rationale:** Full module designs need clear homes, not contradictory copies in adjacent modules.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

## Round 27 — Conversational Facts, Unified Model Execution, and Live Admission

### Q133 — Natural Session assertions; explicit Save is the business boundary

- **Status:** `ACCEPTED`
- **Decision:** Current user career statements may immediately support Advisor discussion, proposed
  wording, and questions even when absent from or inconsistent with saved Evidence. Do not interrupt
  every such statement to request a formal update. Session information stays distinct from saved
  Business Authority and does not automatically become Long-term Memory.
- **Save boundary:** Explicit unambiguous intent specifying facts to save is itself confirmation.
  An authorized Skill may directly use the typed business Tool and Application UpdateCandidateKnowledge;
  no redundant second confirmation is required. Resolve genuinely ambiguous targets/content/conflicts,
  and enforce permission, validation, reconciliation, revision checks, and atomic fact/baseline/current
  Resume propagation. Model parameters never supply authority by themselves.
- **Scope:** Candidate Fit uses saved current knowledge only; Resume Fit uses exact saved Resume.
  A one-off Job direction or response-style request stays Session-local; explicit durable collaboration
  instructions can become Memory candidates, while saved search preferences still belong to PreferenceSet.
  Formal operations cannot use conversational assertions as already saved facts.
- **Rationale:** Conversation can use what the user just said; formal business operations use what
  the user explicitly saved. Natural interaction does not require a second career-fact store.
- **Scoped supersession:** Replaces Q128's immediate-confirmation-on-statement wording and Q41's
  blanket ban on discussing unsaved assertions. Preserves Q108's formal-save prerequisite for actual
  Resume export/application. External product analogies are user design inputs, not verified claims.
- **Detailed design:** [Memory](harness/memory.md), [Context](harness/context.md).
- **Scoped formal-apply refinement — Q146:** A request to apply Advisor changes triggers a concrete
  modification/shared-fact impact preview and one explicit confirmation, then immediate formal
  commit. This replaces the no-additional-preview interpretation for Advisor Resume application;
  ordinary fact discussion still does not trigger Save prompts or compulsory confirmation.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q134 — Continue from actual committed exact inputs without rewriting initial Context

- **Status:** `ACCEPTED`
- **Decision:** After an explicitly authorized Application business write in an Advisor task, append
  the actual committed exact references as immutable admitted runtime inputs. Recheck privacy,
  permission, grounding, and scope before the next ContextFrame. New suggestions/working drafts
  bind their real updated editing baseline, while initial ContextPackage, earlier Frames, and prior
  outputs remain unchanged.
- **Limits:** The same Run can continue the same task within its remaining budget. Do not guess new
  version IDs, silently adopt unrelated concurrent edits, reset limits, or change other Fit Runs'
  frozen inputs; those Runs retain fail-closed compatibility checks.
- **Source:** User accepted the complete Q134 recommendation.
- **Refines:** Q83/Q94 append-only input lineage and Q128/Q133 controlled writes.
- **Detailed design:** [Context](harness/context.md), [Memory](harness/memory.md),
  [Recovery](harness/recovery.md).
- **Proposal-flow refinement — Q158:** The Proposal-generating Run ends before user confirmation.
  Application confirms/commits independently and any subsequent conversation uses new bounded
  execution. Generic append-only post-write input handling does not keep or revive that old Run.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q135 — Unique ModelInvocationRuntime and cumulative Run-wide invocation limits

- **Status:** `ACCEPTED`
- **Decision:** Every real Provider call passes through ModelInvocationRuntime, including primary
  work, RequirementParse, Fits, repair, semantic compaction, reactive retry, and MemoryExtraction.
  It owns budget admission/reservation, invocation counting, dispatch intent, fencing, durable response,
  settlement, timeout/cancel/recovery, and audit. ModelGateway only adapts Provider/model transport;
  AgentRunRuntime owns bounded Run lifecycle and ToolInvocationRuntime owns Tool admission/replay.
- **Limits:** Skill validation repair remains at most once. Semantic compaction is at most once
  per entire AgentRun; reactive Context-size rescue retry is at most once per entire AgentRun.
  Allowances never reset with loop steps. Every call also consumes total Run model-call/token/cost/
  deadline/step budgets; both local allowance and total budget must permit dispatch.
- **Failure:** Reactive rescue only follows explicit Provider context_length_exceeded/prompt_too_long,
  never timeout/disconnection/OUTCOME_UNKNOWN. Protected Full Context overflow fails without lossy
  fact summarization. Deterministic compaction does not create a model invocation.
- **Rationale:** Auxiliary work cannot evade accounting or recovery through a separate model path.
  Invocation kind examples describe architecture, not exhaustive schema or fixed total budget values.
  External framework comparisons do not establish independently verified implementation facts.
- **Resolves:** Q132's cumulative allowance frontier while preserving Q122/Q124/Q130.
- **Detailed design:** [Budget](harness/budget.md), [Recovery](harness/recovery.md),
  [Context](harness/context.md); extraction integration in [Memory](harness/memory.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### Q136 — Active recovery dependencies versus expiring historical source references

- **Status:** `ACCEPTED`
- **Decision:** Payload required by running/recoverable work remains an Active Recovery Dependency
  until its safe recovery boundary ends and cannot be purged. A terminal checkpoint's Historical
  Source Reference does not require indefinite source retention. Preserve minimal metadata/hash/
  lineage and explicit PAYLOAD_PURGED/SOURCE_UNAVAILABLE or equivalent availability after cleanup.
- **Continuation:** Check availability and permission. A surviving exact business version may be
  obtained through a new controlled ToolInvocation, honestly recorded as a new read. Never pretend
  it is the old ToolResult, substitute current content for historical exact input, or guess missing
  source text from a checkpoint. Necessary unavailable sources stop reliable continuation or require
  user input; no automatic platform revisit, external request replay, or side effect restoration.
- **Rationale:** Lineage is an explanation of provenance, not a promise of permanent readability.
- **Resolves:** Q125/Q132 checkpoint-reference retention frontier.
- **Detailed design:** [Storage](harness/storage.md), [Context](harness/context.md),
  [Recovery](harness/recovery.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q137 — Memory disablement effects, separated into independent controls by Q139

- **Status:** `ACCEPTED`
- **Retained behavior:** Check current permission for every new Frame and automatic extraction
  publication. Initial Package admission is not permanent permission. Retain stored entries;
  forgetting/deletion, Session continuity, Business Authority, and already transmitted content have
  separate lifecycles. No default disabled-period history backfill on reenabling.
- **Current control model — Q139:** Auto Learning off stops new automatic extraction/publication
  but does not stop Recall. Recall off excludes Memory from the next Frame but does not itself
  disable learning or delete entries. Explicit user management is a third independent capability.
- **Scoped supersession:** Q139 replaces the single coupled off-switch, not the retention,
  per-use admission, non-backfill, or no-retroactive-retraction rules; this partial record remains.
- **Detailed design:** [Memory](harness/memory.md), [Context](harness/context.md),
  [Storage](harness/storage.md), [Recovery](harness/recovery.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### S27.1 — Automatically synchronize existing Harness modules; new files require explicit request

- **Status:** `ACCEPTED`
- **Decision:** Whenever an accepted answer changes an existing Harness module, update its detailed
  design automatically along with the Decision Register, including scoped supersession and dependent
  modules. Do not wait for the user to name each file. Create a new Harness module design file only
  when explicitly requested; Q135 runtime responsibilities therefore live in the existing records.
- **Boundary:** Continue architecture-only, five-question sequential Grill batches. No permission
  to modify formal documents, implement code, freeze exhaustive fields, or remove unmarked decisions.
- **Rationale:** Complete module records must stay consistent with the decisions they elaborate.
- **Eval maintenance clarification (user correction after Q177):** Eval Grill normally updates only
  this register (questions/answers), eval/agent-evaluation.md (detailed Eval architecture), and the
  Contract inventory (future Contract objects/properties). Do not copy Eval coverage, fixtures,
  check outcomes, or pending Eval questions into Harness modules. Change a module only when an
  accepted decision actually alters its design, not merely because the module is being tested.
- **Formal writeback:** Design workflow only; not a new product or implementation authority.

## Round 28 — Skill-centric Lazy Context, Independent Memory Controls, and Parse Ownership

### Q138 — Advisor owns optimization; Session facts use verifiable conversational references

- **Status:** `ACCEPTED`
- **Decision:** ResumeAdvisor is the semantic optimization Skill; do not introduce a redundant
  suggest_improvement Tool. Tools provide typed controlled actions such as resume.read,
  evidence.read/search, and candidate_knowledge.update_evidence.
- **Source boundary:** Saved facts use EvidenceRef. Newly user-stated Session facts may immediately
  support discussion, Suggestion, and working draft using SessionContextRef/UserTurnRef to the exact
  authorized Session/Turn and cited text. They are not Evidence and cannot enter Candidate/Resume Fit
  as formal facts. Context Engineering explicitly admits relevant Session information; Tools never
  silently inspect the full chat to discover intent.
- **Validation/save:** Where passed to an action, ToolInvocationRuntime verifies Session membership,
  actual cited text, and scope. Model-invented references are invalid. Explicit unambiguous adoption/
  Save uses the controlled Application path to create facts/versions/formal Resume and grounding;
  without Save there is no automatic Memory or business promotion.
- **Refines:** Q120's illustrative optimization action, Q133/Q134, and Advisor suggestion grounding;
  no third-party framework behavior is claimed as independently verified.
- **Detailed design:** [Context](harness/context.md), [Memory](harness/memory.md),
  [Recovery](harness/recovery.md).
- **Scoped supersession — Q146:** Advisor has discussion and Suggestions, not ResumeDraft or a
  persistent working draft. Draft belongs only to My Resumes page CRUD. Formal apply resolves a
  user-specified Resume or Workspace default, previews concrete shared-fact/current-Resume impact,
  receives one confirmation, and immediately commits through UpdateCandidateKnowledge. Earlier
  draft/promotion clauses in this record are historical only; no extra draft Save follows.
- **Formal proposal refinement — Q148-Q149:** Only the actual apply target is selected: current
  instruction's explicit Resume, otherwise Workspace default. Read its exact version and generate
  its own before/after ChangeProposal; do not infer a suggestion-source Resume or transplant another
  Resume's patch. Preview target/version/default status, fact changes, and affected current Resumes.
  One confirmation binds that complete Proposal; target/patch changes or revision conflicts require
  a new preview. Ordinary exact input lineage remains, not an extra source-selection concept.
- **Formal writeback:** `architecture.md`, `contracts/*`, `spec.md`, `acceptance.md`

### Q139 — Context sources are not default injection; Skill-centric acquisition and independent Memory

- **Status:** `ACCEPTED`
- **Decision:** Distinguish Control/Instruction, Session, dynamic Long-term Memory, business Tool
  capabilities, Business Authority, and runtime/Tool sources. Skill's core semantics/permissions/
  output contract are protected Control Context; detailed guidance/templates/references may be
  progressively disclosed without becoming Tools or Memory.
- **Acquisition:** Interactive Advisor primarily uses LAZY_TOOL: initial control, current/recent
  Session, admitted recalled Memory, and Tool definitions; business bodies are read as needed,
  action-validated, and readmitted into later Frames. Business Tools do not scan Session history.
  Preparation entry supplies explicit business references/intent, not an eager full JD/Resume/Evidence
  dump or separate Agent type. Existing selection priority and no-silent-switch rules remain.
- **Exact exception:** RequirementParse, CandidateJobFit, and ResumeJobFit use EAGER_EXACT:
  Application freezes the necessary exact JD or RequirementSet/Resume/baseline/Evidence before Run
  creation. These headless inputs are protected; v1 Fits have no autonomous Evidence Tool loop.
  Future Candidate Agentic RAG remains deferred, not implicitly enabled by interactive lazy reads.
- **Package/Frame:** Immutable ContextPackage is Run-start scope/policy/frozen-input/capability
  manifest, not all eventual payload. Tool reads and authorized writes append actual admitted
  exact runtime inputs. Each immutable ContextFrame records one ModelInvocation's actual input.
- **Memory controls:** Auto Learning controls automatic pending work/extraction/publication; Recall
  independently controls each Frame's Memory reads/injection. Turning either off does not delete
  entries or imply the other is off. User View/Add/Edit/Delete/Clear All runs through deterministic
  validation without extraction, limited to collaboration categories, never career/search facts.
  Existing no-backfill, forgetting/non-resurrection, privacy, and Skill allowlists remain.
- **Compaction:** Exclude direct Long-term Memory blocks from semantic checkpoint sources; recall
  dynamically per Frame. Legacy direct mixtures are removed or rebuilt from permitted Session/runtime
  sources. v1 defers indirect second-order influence via real assistant responses. Old LAZY_TOOL
  results may externalize; later exact rereads are new ToolInvocations. Protected EAGER_EXACT inputs
  cannot be summarized to evade overflow. Compaction still leaves durable Session history intact.
- **Scoped supersession:** Replaces default business-body injection for all Skills and Q137's coupled
  Memory switch. Refines S17.3/Q89 entry payload interpretation and Q132 protected-input classification.
  This changes acquisition, not authority, explicit Save, runtime permission, or business approval.
- **Detailed design:** Complete design in [Context](harness/context.md), synchronized with
  [Memory](harness/memory.md), [Budget](harness/budget.md), [Recovery](harness/recovery.md),
  [Storage](harness/storage.md). No new module file or future Skill implementation is introduced.
- **Refined by Q143/Q144/Q146:** Lazy reads pin resolved exact versions; job.requirements.read is
  a pure read that reports missing dependency for Application EnsureRequirementSet. Advisor has no
  working draft; formal application uses a concrete shared-impact preview and one confirmation.
  Session references are conversational provenance, not an implicit write authorization.
- **Mid-run revocation — Q172:** If authorization for a protected EAGER_EXACT input is revoked
  after freeze, end the affected task fail-closed rather than silently reducing scope. No later
  Frame/repair/Tool consumes revoked input or publishes valid current Analysis. A requested new
  admitted scope needs a new task. Initial exclusions retain existing UNKNOWN semantics; prior
  transmission cannot be undone and necessary usage/recovery/audit stays truthful.
- **Formal writeback:** `architecture.md`, `contracts/*`, `spec.md`, `acceptance.md`

### Q140 — Gateway and SDK have no transparent retry or fallback authority

- **Status:** `ACCEPTED`
- **Decision:** Gateway/SDK adapters cannot hide extra Provider requests or choose automatic model/
  Provider fallback. Every permitted resend is a real ModelInvocation through Runtime allowance,
  budget/reservation, durable dispatch, recovery, and audit. Bounded validation repair and explicit
  size-rejection rescue retain their accepted limits.
- **Failure:** Timeout, disconnection, and uncertain remote execution remain OUTCOME_UNKNOWN with
  explicit new-Run Retry. Proven pre-dispatch local preparation can safely continue. Explicit user
  selection of a supported alternative configuration starts a new Run without erasing old history.
- **Source:** User accepted the complete Q140 recommendation.
- **Refines:** Q122/Q135's unique execution boundary, including adapter behavior.
- **Detailed design:** [Recovery](harness/recovery.md), [Budget](harness/budget.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q141 — Streaming deltas are disposable UI state, not durable results

- **Status:** `ACCEPTED`
- **Decision:** StreamBridge/SSE can display deltas, but only a complete Provider response persisted
  by ModelInvocationRuntime as RESPONSE_DURABLE proceeds to parse/validation and formal Assistant
  Turn, Suggestion, or adoptable result. Half-streams need not persist and may disappear on refresh
  or recovery. They never form a formal Suggestion or extraction source, and cannot be spliced to Retry.
- **Failure/reconnect:** Apply existing known-failure/unknown-outcome semantics to interrupted calls.
  Frontend disconnection alone does not stop a healthy Backend call; reconnect may read its eventual
  completed formal result. Model text saying "saved" is not Application commit evidence.
- **Rejects:** Q141's recommendation to retain incomplete text as a persistent chat fragment.
  Q122 outcome/usage audit survives independently of discarded deltas.
- **Detailed design:** [Recovery](harness/recovery.md), [Storage](harness/storage.md),
  [Memory](harness/memory.md), [Context](harness/context.md).
- **Business outcome refinement — Q156:** A formal Application commit made before a later chat
  failure remains successful. UI separates saved modification from unfinished reply; persisted
  mutation result, not streaming text or final narration, drives recovery and Proposal idempotency.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q142 — Durable single-flight Requirement parsing with owner-only cost

- **Status:** `ACCEPTED`
- **Decision:** EnsureRequirementSet enforces one valid RequirementParse AgentRun for an exact
  JobVersion + parser/schema/prompt/policy compatibility target using database atomic claim,
  unique active-target constraint, or CAS. Process-local singleflight is optional optimization.
  The winning operation owns the producer and pays its actual parse/repair from its ExecutionBudget.
  Many waiters reuse one completed immutable Set without duplicate parse charges.
- **Cancellation/failure:** Waiter cancellation affects only its wait. Owner-operation cancellation,
  parse failure, or OUTCOME_UNKNOWN returns dependency-unavailable to waiters, with no automatic Run/
  budget takeover or silent reparse. Explicit user Retry rechecks compatible durable results, then
  competes for new ownership only if necessary. Unknown exposure remains with the original owner.
- **Rationale:** Persistent concurrency control prevents duplicate producers while keeping budget,
  cancellation, and isolated semantic-task boundaries explicit.
- **Refines:** Q58/Q110/Q121 dependency preparation, Q124 budget ownership, Q122 recovery.
- **Detailed design:** [Budget](harness/budget.md), [Recovery](harness/recovery.md).
- **Advisor integration — Q144:** A missing job.requirements.read result delegates preparation to
  Application, not hidden parsing inside the read. The same owner/waiter budget and failure rules
  serve Advisor without requiring prior DeepFit.
- **Usable dependency Gate — Q171:** No usable Requirement means fail fast before downstream
  Fit. An empty/non-assessable result cannot become a usable compatible target merely by passing
  JSON/schema checks. Surface input/dependency failure; no downstream invented requirements,
  zero-item perfect match, or extra retry allowance beyond the existing bounded parser policy.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### S28.1 — Explicit-obsolescence cleanup and cross-module Context rewrite

- **Status:** `ACCEPTED`
- **Decision:** Remove wholly marked SUPERSEDED Q78/Q84, preserving Q113 as their replacement.
  Prune explicitly superseded clauses in partially valid records without deleting their surviving
  decisions, IDs, or replacement relationships. REJECTED alternatives and DEFERRED work are not
  automatically obsolete records. No renumbering.
- **Synchronization:** Apply Q139 acquisition throughout Context and existing Harness modules, not
  only as an appended exception. Independent Memory controls replace coupled-switch wording.
  New module files still require explicit user request; formal project documents remain untouched.
- **Formal writeback:** Design-record maintenance only.

## Round 29 — Pure Tool Reads, Explicit Formal Application, and Durable Derivative Intent

### Q143 — Pin exact versions after lazy resolution

- **Status:** `ACCEPTED`
- **Decision:** First read of a permitted unresolved root records its actual exact version; subsequent
  reads of the same task object within a Run use that version, not silently latest. Preserve already
  fixed Chat/Preparation inputs. An authorized current-task Application write may explicitly append
  its committed new versions under Q134; unrelated concurrent page changes do not upgrade the Run.
- **Mutation boundary:** Saved mutations check revisions/compatibility; old-version readability is
  not current business eligibility. New outputs bind actual inputs; querying another Resume is not
  implicit editing-target selection.
- **Source:** User accepted the complete Q143 recommendation.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q144 — Pure job.requirements.read and Application-owned Ensure orchestration

- **Status:** `ACCEPTED`
- **Decision:** Model-facing action names use <domain>.<resource?>.<action>, preferably explicit
  read/list/search/update verbs rather than Aggregate names. Replace jobs.requirementset with
  job.requirements.read. It reads an existing compatible RequirementSet for an exact JobVersion or
  returns DEPENDENCY_MISSING / REQUIREMENT_SET_REQUIRED; it cannot hide parsing, a model call,
  another AgentRun, or durable asset creation.
- **Dependency:** Application's shared EnsureRequirementSet reuses or single-flight-produces the Set
  through a separate RequirementParse AgentRun. ModelInvocationRuntime, owner budget, at most one
  repair, recovery, and audit apply. Successful exact Set is admitted into the Advisor's next Frame.
  Owner pays; waiters do not duplicate charges. Advisor waits without absorbing the parse task.
- **Failure/scope:** No prior manual DeepFit is required. Parsing failure is explicit dependency
  failure; Advisor cannot invent another formal RequirementSet from JD. read remains read, writes
  are explicit, and Ensure* orchestration belongs to Application.
- **Detailed design:** Newly authorized [Tool Actions](harness/tool.md); synchronized
  [Context](harness/context.md), [Budget](harness/budget.md), [Recovery](harness/recovery.md).
- **Bounded wait — Q159:** Application drives dependency readiness; Advisor retains its active
  foreground Turn without a model/Provider slot or model polling. Overall deadline/cancel applies;
  success admits the exact Set, failure ends waiting without inline parsing or ownership takeover.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q145 — User Memory management outranks older-source extraction

- **Status:** `ACCEPTED`
- **Decision:** Automatic publication rechecks current entries, manual edits, deletion, and
  supersession. Candidates clearly based on sources older than a corresponding user management
  change cannot overwrite it. Ambiguous old recurrence versus new preference is conservatively
  rejected rather than prompting constantly.
- **Continuity:** A genuinely later explicit durable user instruction may still update Memory via
  admission; manual management is not permanent locking. Memory Runtime, not the extractor's
  self-declared freshness, enforces these rules and no-resurrection constraints.
- **Source:** User accepted the complete Q145 recommendation.
- **Detailed design:** [Memory](harness/memory.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q146 — Page-only ResumeDraft; Advisor Suggestions and confirmed immediate formal apply

- **Status:** `ACCEPTED`
- **Decision:** ResumeDraft exists only in My Resumes, the sole manual Resume CRUD page. Unsaved page
  edits require Save / Discard / Cancel before leaving. Advisor, ChatSession, and Preparation do not
  own ResumeDraft or another persistent working draft; downstream flows consume saved ResumeVersion.
- **Advisor:** Session-stated facts can immediately inform discussion/Suggestion without entering
  Knowledge. To apply to Resume, determine the user-specified target or Workspace default when absent.
  Show actual modifications and explicitly explain shared Candidate Knowledge/other current Resume
  impact, then obtain one confirmation. This authorizes typed Application UpdateCandidateKnowledge:
  version changed facts, advance current pointers/baseline, and atomically create affected current
  ResumeVersions/GroundingSets. There is no subsequent draft Save or per-Resume repeated confirmation.
- **Preparation:** Display/select final rendered formal Resume, never edit its body. Optimization
  opens ordinary chat with Preparation/Job/selected Resume refs and lazy business reads. Returning
  a new formal version remains an explicit Q91 revision/CAS adoption, preserving concurrent fields
  and immutable execution Snapshots.
- **Supersedes:** Q101 in full; Advisor working-draft clauses of Q41/Q85/Q94/Q108/Q138/Q139;
  implicit prior-context apply-target precedence under Q93; Q133's no-preview interpretation for
  formal Advisor application. Ordinary conversational use, exact reads, and business invariants remain.
- **Resolves:** The deleted-Session/pending-Advisor-draft branch is removed, not solved by inventing
  a recoverable draft. Formal results survive chat deletion independently; unsaved statements remain
  Session context.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Memory](harness/memory.md), [Storage](harness/storage.md).
- **Formal proposal refinement — Q148-Q149:** Only the actual apply target is selected: current
  instruction's explicit Resume, otherwise Workspace default. Read its exact version and generate
  its own before/after ChangeProposal; do not infer a suggestion-source Resume or transplant another
  Resume's patch. Preview target/version/default status, fact changes, and affected current Resumes.
  One confirmation binds that complete Proposal; target/patch changes or revision conflicts require
  a new preview. Ordinary exact input lineage remains, not an extra source-selection concept.
- **Refinements — Q153/Q156:** My Resumes experience removal changes that Resume's selection,
  not shared Evidence. A committed formal Advisor mutation remains successful even if later model
  narration fails; reconcile persisted mutation result and never apply one confirmed Proposal twice.
- **Draft durability — Q166:** Unsaved My Resumes ResumeDraft is temporary UI state; crash loss
  is accepted and no recovery checkpoint/autosave is promised. Normal navigation still requires
  Save / Discard / Cancel. Successful Save and Harness/business durability remain unchanged.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q147 — Atomic authority plus durable derived-work intent; post-commit execution

- **Status:** `ACCEPTED`
- **Prepare:** Validate/reconcile/check revisions, determine all affected Resumes and necessary
  derived tasks before committing.
- **Finalize:** One short SQLite transaction commits authority versions/current pointers, baseline,
  all affected ResumeVersions/GroundingSets, and DerivedWorkItem(PENDING) intents. A crash immediately
  after commit cannot lose knowledge of required derived work.
- **Post-commit:** Render/preview/index/cache execute asynchronously with startup discovery,
  explicit replay safety and idempotence. Failure preserves saved authority but affects readiness,
  e.g. EXPORT_NOT_READY. Publication validates exact source versions/hashes/current state; stale
  completion may retain history but never overwrite a current artifact.
- **Scope:** Lightweight durable SQLite work records, no MQ. This replay permission does not extend
  to model calls, recruiting-platform access, email, or browser application; outcome-sensitive work
  remains under Q122 dispatch/unknown/explicit-retry rules.
- **Refines:** Q73/Q118/Q119 without moving expensive computations into the authority transaction.
- **Detailed design:** [Recovery](harness/recovery.md), [Storage](harness/storage.md),
  [Tool Actions](harness/tool.md).
- **Generation demand — Q152:** Authority and derivative-currentness metadata synchronize at Save,
  but not every format must be eagerly rendered. Register necessary requested work durably; later
  preview/export/Preparation demand also persists intent before execution. Compatible exact-source/
  configuration tasks may be idempotently reused. This does not authorize new model/platform work.
- **Obsolete-work refinement — Q165:** Recheck exact source/current references/demand before
  expensive derivative execution; obsolete queued current-artifact tasks may end as no longer needed.
  In-flight safe work may finish but cannot publish current; completed history remains. No extension
  to model/platform replay or retry.
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`, `development.md`

### S29.1 — Dedicated Tool action design record

- **Status:** `ACCEPTED`
- **Decision:** Explicitly create harness/tool.md for naming, action purity, typed admission,
  Session-source validation, replay/permission boundaries, and Application dependency preparation.
  Existing module synchronization continues; this authorization does not create other Harness files.
- **Formal writeback:** Design maintenance; later normative rules enter architecture/contracts.

### S29.2 — Current contract-design inventory

- **Status:** `ACCEPTED`
- **Decision:** Collect all valid decision-register and Harness architectural objects and mentioned
  property semantics into design/contract/contract-design-inventory.md, grouped by ownership with
  source references, unresolved details, and explicit superseded/deferred exclusions.
- **Boundary:** This is a later-design checklist, not frozen schemas, generated tables, a new
  Candidate aggregate, or implementation status. Read current corrections before interpreting older
  accepted records; illustrative names never imply exhaustive required database fields.
- **Formal writeback:** Design planning only; formal contracts remain in docs/contracts.

## Round 30 — Target-Specific Changes, Logical Experience Deletion, and On-Demand Derivatives

### Q148 — Non-editable ChangeProposal binds preview and confirmation

- **Status:** `ACCEPTED`
- **Decision:** A concrete non-editable proposed operation separates Suggestion from formal commit,
  without creating an Advisor ResumeDraft. It displays actual target, before/after changes,
  shared Evidence impact, and affected current Resumes. One confirmation authorizes exactly that
  displayed change; model-generated write arguments cannot append unconfirmed mutations.
- **Replacement/concurrency:** Revised requested changes produce a new preview, not reuse of old
  authorization. Revalidate required revisions before commit; preserve suggestions and expose
  conflicts rather than overwrite. The proposal is not independently editable/exportable/applicable
  as a Resume or recruiter-facing material.
- **Source:** User accepted the complete Q148 recommendation; Q149 names it ChangeProposal and
  fixes target-specific construction. Detailed fields/lifetime remain for the later Contract Grill.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Storage](harness/storage.md), [Recovery](harness/recovery.md).
- **Wait distinction — Q158-Q159:** Proposal generation/display ends that Turn/Run; pending human
  confirmation is Application state and exact command validation, not a live Agent. Advisor's
  independent RequirementParse dependency wait keeps the same foreground Turn active, releases
  model/Provider execution capacity, and retains deadline/cancel and Q142 owner/waiter semantics.
- **Session deletion — Q167:** Unconfirmed originating Proposals become ineligible, e.g.
  INVALIDATED_BY_SESSION_DELETE; old IDs/restored pages cannot confirm them. Cancel active foreground
  work. Confirmation/deletion atomically checks current Session/Proposal state and only one competing
  outcome succeeds. Already committed mutation results/formal assets remain; new modification needs
  a new Proposal in a valid context.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q149 — Actual target only; rebuild its exact before/after patch

- **Status:** `ACCEPTED`
- **Decision:** Do not introduce/infer/track a suggestion-source Resume across conversation.
  The actual modification target is the Resume explicitly specified in the current instruction,
  otherwise Workspace default. Before ChangeProposal, read that target's exact ResumeVersion and
  validate applicability, then produce its own before/after patch.
- **Preview:** Prominently identify actual Resume name/id/version and default selection, concrete
  changes, Candidate Knowledge impact, and other affected current Resumes. The user confirms
  target + patch + impact, not a story about the original source of a suggestion.
- **Safety:** Never transplant a patch by swapping resume_id or copy unrequested experiences.
  An explicit target change invalidates the Proposal; reread and regenerate for the new exact
  target before one final confirmation. Submission checks target/Evidence revisions; concurrent
  changes regenerate the preview, never automatically overwrite.
- **Supersedes:** Q149's recommendation to infer/display differing suggestion-source and target
  Resumes. This removes extra selection state, not truthful exact invocation/input provenance.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Memory](harness/memory.md), [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q150 — MaterialApproval binds actual viewed frozen material

- **Status:** `ACCEPTED`
- **Decision:** Required render artifacts must exist and be viewable before material confirmation.
  MaterialApproval binds actual frozen material artifact/hash and necessary sources, not merely a
  Resume root/name/version. Rerendering cannot replace an approved artifact in place.
- **Compatibility:** Adopting another ResumeVersion or material requires approval compatibility
  validation, not assumed inheritance. Even identical hashes cannot bypass current fact eligibility.
  Frozen execution Snapshots stay immutable; MaterialApproval remains separate from ExecutionApproval.
- **Source:** User accepted the complete Q150 recommendation.
- **Detailed design:** [Tool Actions](harness/tool.md), [Storage](harness/storage.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q151 — Delete Evidence logically and propagate only explicit current inclusion

- **Status:** `ACCEPTED`
- **Decision:** Product action is Delete Evidence / Delete Experience, not separate withdraw or
  invalidate controls. Logically delete the EvidenceItem; immutable history stays for lineage.
  Determine impact solely by whether each current ResumeVersion explicitly contains that Item.
  Do not add sentence/Claim-level or semantic dependency graphs or model-based summary inspection.
- **Confirmation/transaction:** Show which current formal Resumes will change. The confirmed
  deletion covers removing that experience and its associated body from those Resumes. In one
  authority transaction logically delete the Item, create the new current baseline, create/advance
  every directly affected current ResumeVersion and required grounding, and register necessary Q147
  derivative intents. Any authority failure rolls back the entire operation.
- **Limits:** Resumes not containing the Item are untouched. No historical-version fallback or
  model-generated substitute. Existing EvidenceVersions, historical ResumeVersions/analyses, completed
  applications, and already rendered PDF/MaterialArtifacts remain immutable; deletion never edits them.
- **Future use:** New Candidate/Resume Fit, formal Resume Save, render, and application use current
  eligible Knowledge/Resume versions. Historical readability/download is not new-use eligibility.
- **Supersedes:** Q105's version/item withdrawal/invalidity operation family and Q151's proposed
  semantic/composite-Claim removal analysis. Preserves Q108 temporal history and Q114/Q118 atomic
  current-Resume synchronization, now using explicit membership for deletion.
- **Detailed design:** [Tool Actions](harness/tool.md), [Storage](harness/storage.md),
  [Recovery](harness/recovery.md), [Context](harness/context.md).
- **Entry restriction — Q153:** Only Candidate Knowledge management (求职资料库) initiates global
  Evidence deletion. My Resumes removes the experience from that Resume's selection only; it does
  not mutate Evidence/baseline/other Resumes. A generic Advisor write Tool is not another delete entry.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q152 — Strong authority synchronization; demand-driven derivative generation

- **Status:** `ACCEPTED`
- **Decision:** Save synchronizes all affected current Resume authority and artifact-currentness
  metadata, not every possible rendered format. Register required requested derived work durably;
  current page preview, explicit export, or Preparation material needs determine real demand.
  Artifacts not yet needed may remain ungenerated.
- **Recovery/reuse:** Later generation requests also persist intent before execution. Reuse compatible
  exact-source/configuration work idempotently; stale/missing output cannot appear current. Model
  calls, platform collection, and external application are never automatic derivative work.
- **Source:** User accepted the complete Q152 recommendation; refines Q147 without weakening
  all-affected-authority transactionality or durable work intent.
- **Detailed design:** [Recovery](harness/recovery.md), [Storage](harness/storage.md),
  [Tool Actions](harness/tool.md).
- **Obsolete-work refinement — Q165:** Recheck exact source/current references/demand before
  expensive derivative execution; obsolete queued current-artifact tasks may end as no longer needed.
  In-flight safe work may finish but cannot publish current; completed history remains. No extension
  to model/platform replay or retry.
- **Formal writeback:** `architecture.md`, `contracts/*`, `spec.md`, `acceptance.md`

### S30.1 — Correct Memory filename and maintain the contract inventory

- **Status:** `ACCEPTED`
- **Decision:** The user renamed the Memory module to memory.md. Preserve that file and synchronize
  all design links and naming notes; do not recreate the misspelled file. Update existing Harness
  modules and the contract inventory with Q148-Q152, including ChangeProposal, actual-material
  approval, logical Evidence deletion, and demand-driven derived work.
- **Scope:** No new module file, formal-document edit, implementation, or history cleanup is requested.
  Q105 is marked replaced and excluded from current contract candidates; no decision renumbering.
- **Formal writeback:** Design-record maintenance only.

## Round 31 — Selection-Only Removal, Foreground Serialization, and Minimal Greeting

### Q153 — My Resumes removes selection; only Knowledge management deletes Evidence

- **Status:** `ACCEPTED`
- **Decision:** My Resumes can only remove an experience from the current Resume's selection,
  creating its new ResumeVersion without deleting shared Evidence, changing baseline, or affecting
  other Resumes/Candidate Fit. Global Evidence deletion is available only from Candidate Knowledge
  management (求职资料库), using Q151's impact confirmation and atomic direct-membership propagation.
- **Boundary:** Do not interpret deleting an experience block from one Resume as global fact deletion,
  or expose Advisor as a second global-delete entry through a generic update capability.
- **Refines:** Q100, Q146, Q151; no new page or authority.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Storage](harness/storage.md), [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q154 — Allow empty saved state; fail fast on missing task prerequisites

- **Status:** `ACCEPTED`
- **Decision:** Do not prevent users deleting their facts merely to preserve downstream readiness,
  fabricate placeholder facts, or retain a deleted experience invisibly. Saved empty Knowledge/
  Resume state is distinct from readiness for a particular capability.
- **Gate:** Operations such as Resume Fit fail fast before model execution when their required
  basic information or career content is absent. This is an input prerequisite, not a restored
  KnowledgeConfirmation mechanism or a claim of real-world incapability.
- **Deferred:** The exact functions requiring each input and their required Profile/Evidence/Resume
  fields belong to later Contract design. Do not freeze an all-feature matrix, universal Profile/
  contact requirement, or mandatory experience count from this answer.
- **Source:** User accepted the principle and explicitly deferred per-function prerequisites.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q155 — One active foreground Turn per Session

- **Status:** `ACCEPTED`
- **Decision:** A ChatSession permits at most one active foreground Turn. New input waits or
  explicitly stops the current Turn before starting another; two user Turns never concurrently
  advance the same Session Context or business state.
- **Scope:** Different Sessions may execute concurrently. Independent dependency/auxiliary/
  background AgentRuns supporting the current Turn may also run; they are not extra user Turns.
  Enforce the constraint in backend runtime admission, not only frontend controls.
- **Preserves:** Bounded Run lifecycle, cancellation/fencing, per-operation budgets, and explicit
  exact runtime input records. Does not define a long-lived Agent waiting for user messages.
- **Detailed design:** [Context](harness/context.md), [Recovery](harness/recovery.md),
  [Memory](harness/memory.md), [Budget](harness/budget.md).
- **Wait distinction — Q158-Q159:** Proposal generation/display ends that Turn/Run; pending human
  confirmation is Application state and exact command validation, not a live Agent. Advisor's
  independent RequirementParse dependency wait keeps the same foreground Turn active, releases
  model/Provider execution capacity, and retains deadline/cancel and Q142 owner/waiter semantics.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q156 — Persisted mutation success is independent of later chat generation

- **Status:** `ACCEPTED`
- **Decision:** Once Application commit succeeds, the formal modification is final business fact,
  not rolled back by subsequent model reply failure. UI reports that formal changes succeeded but
  the following reply is unfinished rather than suggesting Save failed.
- **Recovery/idempotency:** Persisted mutation result is authoritative for whether the confirmed
  Proposal applied. Recovery and retry recognize that same Proposal idempotently; no duplicate
  EvidenceItemVersion or ResumeVersion creation.
- **Limits:** Model Retry still follows Q122; do not silently replay unknown remote calls. Any new
  formal modification needs a new confirmed ChangeProposal. Assistant wording/streaming is not
  commit evidence, and incomplete narration cannot overwrite known business success.
- **Detailed design:** [Recovery](harness/recovery.md), [Tool Actions](harness/tool.md),
  [Storage](harness/storage.md), [Context](harness/context.md), [Memory](harness/memory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q157 — Preparation-owned Greeting with one fixed generic default

- **Status:** `ACCEPTED`
- **Decision:** Greeting is a Job-level editable field of ApplicationPreparation, not a separate
  Aggregate, edit-version history, template library, reuse subsystem, or generation Skill.
  Creation uses one product-built-in generic text, e.g. “您好，我对这个岗位很感兴趣，希望有机会进一步沟通，谢谢！”.
  This is illustrative wording, not a mandatory final copy string.
- **No automatic customization:** Do not personalize by Job/company/Resume/Candidate Knowledge,
  invoke a model, or let Memory silently customize the initial message. Users may edit it manually
  under Preparation revision/CAS; each edit does not create an independent business version.
- **Confirmation/execution:** MaterialApproval freezes the actual viewed and confirmed exact Greeting
  and necessary hash. Later edits require reconfirmation; old approval does not cover new text.
  ExecutionSnapshot freezes the exact intended send text independently, unaffected by later
  Preparation changes.
- **Refines:** Q16/Q25/Q30/Q42 Greeting references; freezes minimal v1 ownership without adding
  personalized generation, cross-Job reuse, or template management.
- **Detailed design:** [Tool Actions](harness/tool.md), [Storage](harness/storage.md),
  [Context](harness/context.md), [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 32 — Application Confirmation, Bounded Dependencies, and Shared Platform Safety

### Q158 — Proposal generation ends the Turn; Application handles confirmation

- **Status:** `ACCEPTED`
- **Decision:** Generating and showing ChangeProposal completes that foreground Turn/AgentRun.
  Pending Proposal is persisted Application interaction state, not a suspended Agent waiting for a
  future user message. It does not monopolize the Session; discussion or abandonment remains possible.
- **Confirmation:** Explicit confirmation validates and executes the exact Proposal's Application
  command without another model interpretation of consent or patch. Revision conflicts require a
  new preview, not overwrite. Existing Proposal idempotency and mutation result rules apply.
- **Continuation:** If further conversation is needed, use a new bounded Turn/AgentRun consuming
  the actual mutation result; do not revive the old Run simply to await user approval.
- **Source:** User accepted the complete Q158 recommendation.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md),
  [Recovery](harness/recovery.md), [Storage](harness/storage.md), [Memory](harness/memory.md).
- **Session deletion — Q167:** Unconfirmed originating Proposals become ineligible, e.g.
  INVALIDATED_BY_SESSION_DELETE; old IDs/restored pages cannot confirm them. Cancel active foreground
  work. Confirmation/deletion atomically checks current Session/Proposal state and only one competing
  outcome succeeds. Already committed mutation results/formal assets remain; new modification needs
  a new Proposal in a valid context.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q159 — Advisor dependency wait remains active but bounded

- **Status:** `ACCEPTED`
- **Decision:** Waiting for independent RequirementParse keeps the same foreground Turn active
  in dependency-wait, without occupying model/Provider invocation execution capacity. Its overall
  deadline/cancel remains in force. UI exposes dependency preparation rather than model read polling.
- **Result:** Application admits the successful exact RequirementSet into the next Frame and
  resumes the task. Timeout/cancel/failure ends waiting explicitly, never infinite extension.
  Q142 owner/waiter cancellation applies; no takeover or Advisor-generated substitute requirements.
- **Distinction:** This is a machine dependency that can finish without new user input, unlike
  Q158's pending human confirmation after a completed generating Turn.
- **Source:** User accepted the complete Q159 recommendation.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md),
  [Recovery](harness/recovery.md), [Budget](harness/budget.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q160 — Shared persistent PlatformAccessSafety by platform and account

- **Status:** `ACCEPTED`
- **Decision:** Collector, Browser Executor, and any future Monitor/platform workflow share
  PlatformAccessSafety before every real access, scoped by (platform, account). Check combined
  capacity, current durable Safety State, and action permission; workflows cannot each assume a
  private quota or ignore another workflow's risk signal.
- **Risk:** CAPTCHA, account anomaly/restriction, security verification, explicit platform rate-limit
  and other classified risks update shared persistent state and block subsequent affected accesses.
  Ordinary page/selector/browser workflow failure is not automatically platform/account risk.
- **Recovery:** Predictable capacity may recover by policy. Strong risks default to
  BLOCKED_REQUIRES_USER: user handles the issue then explicitly resumes; never automatic bypass,
  account switching, or cooldown-only strong-risk recovery.
- **Authority:** CollectionRun, ExecutionAttempt, budgets/lifecycles/recovery remain independent.
  Access admission is not ExecutionApproval, material approval, or another workflow's authority.
  Future Monitor is covered if implemented, not introduced as a mandatory new v1 capability.
- **Reference provenance:** User reports BossHunter shares PlatformAccessGuard/page budgets/persistent
  safety lock across collection/send/monitor with tests. Treat this as supplied research rationale,
  not independently verified upstream behavior or a source of frozen numeric/platform limits.
- **Refines:** Q36/Q49 platform risk and admission boundaries. No new Harness module is authorized.
- **Detailed integration:** [Tool Actions](harness/tool.md), [Recovery](harness/recovery.md),
  [Budget](harness/budget.md), [Storage](harness/storage.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `spec.md`, `acceptance.md`

### Q161 — Frozen collection Preferences; latest local filtering; retained partial results

- **Status:** `ACCEPTED`
- **Decision:** CollectionRun freezes exact PreferenceSetVersion at start and never silently
  switches rules mid-run. New Preferences immediately become current Job Pool filtering authority
  and apply to future Runs, without launching another collection or restarting the current one.
- **User control:** Display that the active Run still uses old Preferences and allow explicit stop.
  Stop prevents subsequent accesses and ends with retained partial results; successfully saved Jobs
  are not rolled back or deleted and are filtered locally under the latest Preferences.
- **History:** A Job no longer matching current Preferences stays stored for possible future
  matching. Run and QuickScreen audit retain actual exact versions; current display never relabels
  an old result as having used the new rules.
- **Refines:** Q49/Q55 and S9.1; distinguishes execution consistency from current user intent.
- **Detailed integration:** [Recovery](harness/recovery.md), [Storage](harness/storage.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q162 — Resume unfinished Preparation on repeated Apply entry

- **Status:** `ACCEPTED`
- **Decision:** Prefer resuming an existing unfinished Preparation for the same Job/channel,
  preserving selected materials and manual Greeting. Explicit new-preparation intent starts a
  separate chain instead of silently replacing existing preparation.
- **Validation/idempotency:** Reentry checks current eligibility/readiness/approval compatibility
  without silently upgrading exact inputs. Refresh/repeated clicks/network retry must not create
  duplicates. If several recoverable preparations exist, the user selects explicitly.
- **History:** Reapplication after a completed real application creates a new Preparation/Attempt.
  Existing applications and frozen execution inputs remain unchanged.
- **Source:** User accepted the complete Q162 recommendation.
- **Detailed integration:** [Context](harness/context.md), [Storage](harness/storage.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 33 — Whole Experience Presentation, Disposable Drafts, and Pending-Action Revocation

### Q163 — Whole-experience inclusion without per-Resume bullet selection

- **Status:** `ACCEPTED`
- **Decision:** v1 selects complete experiences. A selected EvidenceItem contributes its current
  version's complete experience body; different Resumes may select different experiences, order,
  and layout, not independently select/hide bullets or retain alternate career-fact text.
- **Propagation:** Editing factual body still updates shared Evidence and affected current Resumes.
  Fine field/pointer grounding remains possible without introducing a presentation selection graph.
  Existing Profile displayed-field/privacy choices are not expanded by whole-experience inclusion.
- **Source:** User accepted the complete Q163 recommendation, including the no-per-Resume-bullet
  selection limitation; refines earlier Q63 fragment-selection wording after Assertion removal.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q164 — Execution live checks do not refresh Job authority

- **Status:** `ACCEPTED`
- **Decision:** Executor may perform necessary live target-identity/availability checks within
  current execution authorization and PlatformAccessSafety. These checks cannot silently advance
  JobVersion, generate RequirementSet, replace frozen Snapshot/materials, or add model Job analysis.
- **Mismatch:** Clearly detected closure, target mismatch or execution-relevant change stops
  subsequent actions with an explanation. Explicit user refresh/repreparation is the separate path.
  Do not infer successful external outcome or add arbitrary platform access.
- **Source:** User accepted the complete Q164 recommendation; refines Q30/Q50/S9.1/Q160 boundaries.
- **Detailed integration:** [Tool Actions](harness/tool.md), [Recovery](harness/recovery.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `spec.md`, `acceptance.md`

### Q165 — Skip obsolete queued current-artifact work before execution

- **Status:** `ACCEPTED`
- **Decision:** Before expensive safe derived computation starts, recheck exact source, current
  references and actual demand. Queued current-artifact work that is no longer needed may end
  without computation; durable intent does not require rendering every intermediate version.
- **History:** Already running safe computation may finish, but stale output cannot publish current.
  Completed artifacts/PDF/audit remain historical and unchanged.
- **Scope:** Only rebuildable derived work. Do not extend this permission to model invocation,
  platform access, external side effects or their automatic retry/replay.
- **Source:** User accepted the complete Q165 recommendation; refines Q147/Q152.
- **Detailed design:** [Recovery](harness/recovery.md), [Storage](harness/storage.md),
  [Tool Actions](harness/tool.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q166 — Unsaved editor ResumeDraft may be lost on crash

- **Status:** `ACCEPTED`
- **Decision:** A sudden crash need not preserve unsaved My Resumes ResumeDraft. It is transient UI
  state with no local recovery checkpoint/autosave guarantee. Normal navigation still uses
  Save / Discard / Cancel; only successful Save creates durable formal facts/Resume.
- **Rejects:** Q166's proposed lightweight editor recovery checkpoint. Does not revive Advisor
  drafts or weaken formal Save, Harness recovery, or durable pending-work guarantees.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md),
  [Recovery](harness/recovery.md), [Storage](harness/storage.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q167 — Session deletion invalidates pending Proposals atomically against confirmation

- **Status:** `ACCEPTED`
- **Decision:** Deleting ChatSession makes all still-unconfirmed originating ChangeProposals
  ineligible, with INVALIDATED_BY_SESSION_DELETE or an equivalent terminal state. Refresh/recovery/
  possession of an old Proposal ID cannot make them confirmable again.
- **Race:** Application checks current Session/Proposal state at the same atomic boundary for
  concurrent confirmation and deletion. Either the Proposal legally commits first or deletion
  invalidates it first; only one competing result succeeds, not both incompatible acknowledgements.
- **Preservation:** Mutation results and formal Evidence/Resume/assets already committed remain
  unchanged under Q156. Historical formal Resumes, completed applications, necessary mutation
  results and audit lineage survive chat deletion.
- **Execution:** Cancel/terminate active foreground work using existing fencing/cancellation rules.
  A further desired change needs a newly generated and confirmed Proposal in valid context, not
  reactivation of a deleted-Session pending action.
- **Detailed design:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Recovery](harness/recovery.md), [Storage](harness/storage.md), [Memory](harness/memory.md).
- **Background learning boundary — Q170:** Source Session deletion also prevents new automatic
  extraction/publication from its pending or in-flight ranges, with source checks before dispatch
  and publication. Existing accepted Memory retains its independent lifecycle; preserve truthful
  remote usage/recovery/audit and do not claim already-sent data was retracted.
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

## Round 34 — Unscored Analysis, Isolated Memory Failures, and Exact-Input Revocation

### Q168 — Valid assessments may exist without a comparable total score

- **Status:** `ACCEPTED`
- **Decision:** A valid durable Analysis may retain per-Requirement states, references, reasons and
  full lineage even when the evidence cannot justify a comparable aggregate. Deterministic
  ScorePolicy decides score availability; the model cannot invent a numeric substitute.
- **Presentation:** Unavailable score is not zero and does not enter ordinary numeric ranking.
  Do not conflate unscored valid analysis with failed execution or label a prior result's score as
  belonging to this Analysis. Original result/policy lineage and explicit rescoring rules remain.
- **Deferred:** Conditions, thresholds and concrete availability representation belong to the
  later Contract/ScorePolicy design, not this architecture decision.
- **Source:** User accepted the complete Q168 recommendation.
- **Detailed integration:** [Context](harness/context.md), [Storage](harness/storage.md),
  [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q169 — Failed Memory batches neither block nor silently replay into later batches

- **Status:** `ACCEPTED`
- **Decision:** Failed or outcome-unknown MemoryExtraction batches are independent from later
  batches. New eligible Turns can proceed; old failed ranges are not silently folded into new
  automatic work. Only explicit Retry processes an old failed/unknown range again.
- **Progress:** Preserve successful, failed/unknown, and pending processing distinctly. Do not mark
  failure successful to advance a cursor or force a single success-prefix cursor to block newer work.
  Undispatched capacity/budget waiting remains pending, not failed.
- **Recovery:** Explicit retry creates new bounded execution under source admission, budget and
  Q122 recovery rules. No infinite background retry or change to foreground task success.
- **Detailed design:** [Memory](harness/memory.md), [Recovery](harness/recovery.md),
  [Budget](harness/budget.md), [Storage](harness/storage.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

### Q170 — Deleted Session sources cannot produce new automatic Memory

- **Status:** `ACCEPTED`
- **Decision:** Do not dispatch pending automatic extraction from deleted source Sessions.
  Cancel in-flight extraction where possible and recheck source validity before publication;
  late candidates from a deleted source cannot be accepted as new long-term Memory.
- **Separation:** Previously accepted Memory is not automatically removed by deleting the chat,
  continuing Q131's independent management/forgetting semantics.
- **Remote boundary:** Already sent content cannot be retracted. Usage, unknown outcomes and
  necessary audit/recovery remain truthful; deletion is neither a refund nor proof of zero usage.
- **Source:** User accepted the complete Q170 recommendation.
- **Detailed design:** [Memory](harness/memory.md), [Recovery](harness/recovery.md),
  [Storage](harness/storage.md), [Budget](harness/budget.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q171 — No usable Requirement means no downstream Fit

- **Status:** `ACCEPTED`
- **Decision:** If JD parsing yields no usable Requirement assessment units, fail fast with an
  explicit input/dependency-not-analyzable outcome before Candidate/Resume Fit. A structurally
  valid empty result is not a usable compatible RequirementSet dependency.
- **Limits:** No zero-item perfect/default match or downstream invented requirements. Guide the
  user to supplement/correct/refetch JD as appropriate. Existing parser validation/repair bounds
  remain; no unlimited retry or extra semantic fallback is added.
- **Distinction:** Q168 concerns usable assessment targets with insufficient scoring information;
  this decision concerns the absence of a usable assessment target.
- **Detailed integration:** [Tool Actions](harness/tool.md), [Context](harness/context.md),
  [Storage](harness/storage.md), [Contract Inventory](contract/contract-design-inventory.md).
- **Formal writeback:** `spec.md`, `architecture.md`, `contracts/*`, `acceptance.md`

### Q172 — Mid-run protected-input revocation ends the frozen task

- **Status:** `ACCEPTED`
- **Decision:** Permission revocation affecting a protected EAGER_EXACT input after freeze makes
  the task fail closed. Do not silently remove that input and continue the same analysis or use it
  in later ContextFrames, repair or Tool calls. No valid new current Analysis is published.
- **New scope:** If the user still wants analysis, create a new task with newly admitted exact
  inputs. Prior ContextFrames/initial Package remain immutable historical records, not permission
  to continue using revoked data.
- **Boundary:** Exclusion before initial freeze retains the established UNKNOWN/completeness
  semantics. Already transmitted content cannot be undone; necessary usage/recovery/audit is
  preserved under protected retention, not dumped into ordinary logs.
- **Source:** User accepted the complete Q172 recommendation.
- **Detailed design:** [Context](harness/context.md), [Tool Actions](harness/tool.md),
  [Recovery](harness/recovery.md), [Storage](harness/storage.md), [Budget](harness/budget.md).
- **Formal writeback:** `architecture.md`, `contracts/*`, `acceptance.md`

## Round 35 — Agent Evaluation Platform and Execution Boundaries

### S35.1 — Langfuse-heavy Eval with real JobHunter task semantics

- **Status:** `ACCEPTED` architectural direction; Q173-Q177 integration decisions are accepted.
- **Decision:** Use LangGraph execution with self-hosted Langfuse for datasets/versioning, experiments,
  generic evaluators, scores/comparison, and observability. JobHunter keeps real Application/Harness
  task adapters, domain-aware deterministic state/lineage/authorization checks, and all production
  invariant enforcement. Do not build a parallel general Eval platform or test-only Agent.
- **Coverage:** Evaluate outcome, trajectory, Tools, Context, grounding, authorization/safety,
  reliability, and efficiency separately. Hard violations cannot be hidden by aggregate quality.
  RequirementParse, independent Candidate/Resume Fit, and Advisor have distinct evaluation semantics.
  Harness correctness primarily uses deterministic tests, not LLM judging.
- **Continuity:** Saved authority, Session facts, confirmed Proposal fan-out, actual Invocation
  boundaries, and Q168/Q172 retain their existing meaning. The new design does not automatically
  replace Q117's deferred parser-release certification or authorize trace export of private content.
- **Maintenance:** Detailed proposal in [Eval](eval/agent-evaluation.md); architecture-level objects
  and unresolved Contract work in [Inventory](contract/contract-design-inventory.md). Proposed trial
  counts/metrics/code layout are not final thresholds/schemas. S37.1 requires new Eval code against
  the effective contracts; old assets impose no migration/reuse duty. This update deletes no files.
- **Formal writeback:** `architecture.md`, `acceptance.md`, `development.md`, relevant
  `spec.md` quality/scope claims and `contracts/*`, after open decisions are settled.

### Q173 — Isolated real-path Eval execution

- **Status:** `ACCEPTED`
- **Decision:** Each Case/Trial uses isolated reconstructible business state, the real Application/
  Domain/Repository/Harness, controlled external adapters, and explicit Scenario human/events.
  Actual test DB commits are allowed; live Workspace mutations and recruiting side effects are not.
  Isolate Trials; distinguish deterministic replay evidence from live-model behavior.
- **Detailed design:** [Eval §4](eval/agent-evaluation.md#4-end-to-end-experiment-architecture).

### Q174 — Derived observability, canonical execution, and incomplete evidence

- **Status:** `ACCEPTED`
- **Decision:** Langfuse is not authority for production success, Invocation completion, usage
  settlement, or recovery. Local Domain/Application/Run/Invocation/Recovery state remains canonical.
  Outage, failed callback upload, or missing spans never rolls back commit or authorizes replay.
- **Evidence/privacy:** Missing observations required by a check yield INCOMPLETE_EVIDENCE, not
  proof of no violation. Callback and SDK share pre-export masking/redaction. Canonical Run/Model/
  Tool Invocation IDs correlate all paths, including auxiliary calls, without duplicate counts/cost.
- **Detailed design:** [Eval §§22–25](eval/agent-evaluation.md#22-observability-integration).

### Q175 — Evidence categories; rollout policy outside this Grill

- **Status:** `ACCEPTED`
- **Decision:** Authorization/permission/authority violations, illegal writes and silent replay
  are unacceptable correctness/safety failures (Hard Gates). Quality, stability, cost and latency
  are separate Quality Targets, not automatic whole-product release failure. Absolute target
  attainment and regression against an approved comparison baseline are independent judgments.
- **Scope:** Preserve Q117's real-JD tests/manual checks/traceable reports without mandatory
  annotated ParserVersion certification. Defer thresholds, Trial counts, default enablement and
  repository/CI release policy to later rollout work; do not continue grilling those policies now.
- **Detailed design:** [Eval §20](eval/agent-evaluation.md#20-hard-gates-quality-evidence-and-deferred-release-policy--q175).

### Q176 — Judge execution belongs to independent Eval Infrastructure

- **Status:** `ACCEPTED`
- **Decision:** Business model calls retain AgentRun/ModelInvocationRuntime budget, fencing and
  recovery. Judges evaluate existing outputs/trajectories under independent Eval execution,
  invocation categories, costs/budgets, model configs, Prompt/Rubric versions and observability labels.
  Judge costs/failures do not become business costs/failures; results cannot mutate Domain state,
  direct business decisions or change original Run outcome.
- **Checks:** Deterministic authorization, permission, exact-version, mutation and observable
  authority-leakage checks remain preferred. Do not claim platform judge calls automatically have
  the business Runtime's reservation/fencing guarantees.
- **Detailed design:** [Eval §26](eval/agent-evaluation.md#26-human-calibration).

### Q177 — Reconstructible fixtures and complete experiment inputs

- **Status:** `ACCEPTED`
- **Decision:** Exact Dataset version is necessary, not sufficient. Bind immutable Business Fixture,
  Scenario Events/Expected Outcomes, and exact Skill/Prompt/Context/Model/Evaluator-Rubric/Runner
  config. Rebuild each isolated Trial from the Fixture, using stable refs/hash validation, never
  current/latest Workspace root lookup. Missing/mismatched/unrecoverable inputs explicitly fail as
  non-reproducible; concurrency/permission/confirmation changes are frozen Scenario Events.
- **Boundary:** Fixture payload versus immutable artifact storage remains deferred. Thin hydration/
  config/hash/event code is allowed, not another Dataset Framework. Reproducible inputs/config/
  scoring conditions do not promise identical remote-LLM output.
- **Detailed design:** [Eval §5](eval/agent-evaluation.md#5-langfuse-platform-responsibilities).

## Round 36 — Scenario Driving, Judgments, and Reusable Evaluation Evidence

### Q178 — Fixed-input N+1 and thin deterministic Scenario orchestration

- **Status:** `ACCEPTED`
- **Decision:** Comparable multi-turn Eval uses fixed user inputs, no generative User Simulator in
  v1 regression. Prefer N+1 for known localized conversation failures: freeze N prior Turns and
  run only the target next input. Full Proposal/confirmation/refusal/revocation/concurrency/CAS/DB
  scenarios use a thin JobHunter Driver reading Langfuse DatasetItem fixtures and authored Turns.
- **Execution:** Drive real Application/Harness/LangGraph at logical checkpoints, not sleeps.
  Confirm only an actual uniquely matching Proposal through Application; never inject DB success,
  fabricate consent, or help missing preconditions. Q158's generating Turn ends before confirmation.
- **Ownership:** Assertions use canonical results/structured events/state, not observability-trace
  arrival. Langfuse manages Dataset/Experiment/platform Session/Trace/Score/Judge; JobHunter drives
  scenarios. NiceEval inspires send/Turn/events, exact-one matching and isolation, not a dependency.
  Future generative exploration is separate and not mixed into comparable regression.
- **Detailed design:** [Eval §4](eval/agent-evaluation.md#4-end-to-end-experiment-architecture).

### Q179 — Independent task outcomes and per-check conclusions

- **Status:** `ACCEPTED`
- **Decision:** Task outcome and evaluation conclusions are separate. Expected rejection can be correct
  behavior; proven violations, INCOMPLETE_EVIDENCE and evaluator errors remain distinct. A failed
  judge does not erase valid deterministic findings. Report coverage and unfinished checks; never
  silently omit failures/unassessable samples, count missing evidence as pass, or score Q168 absence
  as zero. Final types/formulae are later Contract work.
- **Detailed design:** [Eval §19](eval/agent-evaluation.md#19-four-groups-of-results-not-one-agent-score).

### Q180 — Expected output constrains valid behavior, not one answer

- **Status:** `ACCEPTED`
- **Decision:** Exact IDs/versions/enums/permission/authorization stay strict. Requirements, support
  and advice admit semantically equivalent or equally valid alternatives satisfying business
  contract, grounding and Scenario constraints. Reviewed meaning/coverage/support and allowed-path
  constraints replace unique text/sequence matching; ambiguous expectations are not model self-certification.
- **Detailed design:** [Eval §5](eval/agent-evaluation.md#5-langfuse-platform-responsibilities).

### Q181 — Regression intent can outlive original sensitive payload

- **Status:** `ACCEPTED`
- **Decision:** Preserve reviewed minimal sanitized/synthetic fixtures and expectations, checking
  consistent references and retained failure behavior after transformation. Original production
  Trace/Context/Response follows independent retention; source lineage is not permanent readability.
  If no admissible reproducible fixture survives, disclose missing executable coverage. No raw-data
  retention exception or new product approval Aggregate.
- **Detailed design:** [Eval §21](eval/agent-evaluation.md#21-production-evaluation-feedback-loop).

### Q182 — Re-evaluate captured outcomes without replaying execution

- **Status:** `ACCEPTED`
- **Decision:** New evaluator/rubric/judge passes may assess the same exact Trial when required
  admitted evidence remains. Preserve old scores and actual output with explicit new evaluator
  versions. Do not rerun Agent/Tools/mutations; keep judge costs separate. Domain checks need
  retained actual post-state/mutation evidence, not reconstructed initial state.
- **Unavailable:** Purged/missing evidence means unavailable/incomplete evaluation, not silent
  fresh execution. Intentional re-execution is a new Trial with its own frozen inputs/accounting.
- **Detailed design:** [Eval §31](eval/agent-evaluation.md#31-re-evaluation-of-captured-trial-results--q182).

## Round 37 — Evaluation Input Boundaries and Experiment Scope

### Q183 — Restore coherent N+1 state without replaying history

- **Status:** `ACCEPTED`
- **Question:** Does an N+1 fixture need the exact business/runtime state required by the next Turn,
  not just N prior messages?
- **Decision:** Freeze necessary refs/versions/session/Proposal/source state at the boundary;
  restore coherently, execute only N+1, fail as non-reproducible when dependencies are absent. Do
  not replay old calls/writes or claim a next-turn test proves the full historical workflow.
- **Source:** User accepted the complete recommendation for this question.
- **Detailed design:** [Eval frontier](eval/agent-evaluation.md#30-governing-principles-and-current-grill-frontier).

### Q184 — Provide task-scoped evidence to evaluators

- **Status:** `ACCEPTED`
- **Question:** Should judges receive relevant assessed inputs/output and expected constraints, not
  a whole Workspace/fixture/trace dump?
- **Decision:** Yes. Resume Fit judging cannot supplement its assessed Resume from Candidate
  Knowledge. Deterministic state checks may read needed admitted state separately; absent required
  evidence is incomplete evaluation, not permission to broaden model-visible data.
- **Source:** User accepted the complete recommendation for this question.
- **Detailed design:** [Eval frontier](eval/agent-evaluation.md#30-governing-principles-and-current-grill-frontier).

### Q185 — Isolate expected answers and Scenario control from the Agent

- **Status:** `ACCEPTED`
- **Question:** Must expected labels, future user Turns, confirmation scripts, judge instructions and
  previous Trial scores remain outside the Agent-under-test's Context/Tools?
- **Decision:** Yes; expose only current/past inputs and admitted business data. Application
  drives hidden Scenario events. Judge rubric is control, candidate outputs/Tool content are
  untrusted evidence and cannot rewrite scoring rules.
- **Source:** User accepted the complete recommendation for this question.
- **Detailed design:** [Eval frontier](eval/agent-evaluation.md#30-governing-principles-and-current-grill-frontier).

### Q186 — Distinguish Skill-focused from composed-workflow experiments

- **Status:** `ACCEPTED`
- **Question:** Should a Fit benchmark with a ready RequirementSet be labelled separately from an
  end-to-end workflow including parsing/dependency preparation?
- **Decision:** Yes; both use real paths. Declare fixture/dependency scope, attribute failure
  to the actual executed stage, and do not claim unexecuted Fit quality or compare partial-path
  cost as full-workflow cost. No test-only bypass of Ensure or validation.
- **Source:** User accepted the complete recommendation for this question.
- **Detailed design:** [Eval frontier](eval/agent-evaluation.md#30-governing-principles-and-current-grill-frontier).

### Q187 — Freeze Memory configuration and control background activity

- **Status:** `ACCEPTED`
- **Question:** Should ordinary comparable Advisor scenarios prevent unscripted background learning
  from changing context, while Memory-specific scenarios explicitly exercise it?
- **Decision:** Use isolated frozen Memory/Recall configuration and supported Auto Learning
  controls. Explicitly enable/drive learning only in scenarios testing it; record its separate
  cost/evidence and prevent cross-Trial contamination. Disabled learning does not test extraction.
- **Source:** User accepted the complete recommendation for this question.
- **Detailed design:** [Eval frontier](eval/agent-evaluation.md#30-governing-principles-and-current-grill-frontier).

## Post-Grill Direction Supplement

### S37.1 — Rebuild all documentation and code from the accepted design

- **Status:** `ACCEPTED`; explicit user direction after Q187, not an unanswered Grill question.
- **Decision:** Rewrite the formal documents and implement JobHunter anew. Effective Grill decisions
  and subsequent detailed contracts define the new system; adapting the old implementation is no
  longer the delivery strategy.
- **Replacements:** Q4's preservation-first method is replaced. Q22's sequence now produces new
  documents. Remove Q23's compatibility-only Shortlisted retention, Q24's old DeepFit-lineage
  migration, Q26's initial legacy-contract obligations and Q56's old screening reader requirement.
  Related records are updated in place. Eval and Contract inventory follow the same direction;
  old code/tests/fixtures need no mandatory mapped successor.
- **Unchanged:** Effective scope, business/runtime invariants, new-system immutable history,
  exact versions, human confirmation, privacy, safety, TDD and Eval evidence remain required.
  Rebuilding does not mean weaker safeguards.
- **Boundary:** This action updates design records only. It deletes no code, formal documents,
  databases, personal data or Git history. Optional import from the old system requires a separately
  scoped design; no migration or backward-compatibility capability is assumed.
- **Next stage:** Rewrite the formal baseline, complete the separate detailed Contract Grill, then
  implement and verify new slices. Do not inherit old implementation status.

### S38.1 — Independent repository and documentation-first handoff

- **Status:** `ACCEPTED`; unified user response to the proposed Q188-Q192 execution questions.
- **Destination:** `/Users/soulboy/projects/JobHunter/docs/design/`; user-provided new GitHub remote:
  `https://github.com/soulbooyy/JobHunter.git`. This is a separate repository, not an old-repository
  rebuild branch. Do not accept the prior same-repository recommendation by implication.
- **Transfer scope:** Move the decision register, six Harness design modules, detailed Eval design
  and Contract inventory, preserving their relative layout. Old application code, formal documents,
  database/runtime files and Git history are outside this transfer. No remote push is requested.
- **Sequence:** `to-spec` documentation plan → Spec / Architecture / Acceptance / Development /
  Progress → user review → detailed Contract Grill → Contract documents → formal development.
  Q22 is replaced in place to reflect this ordering. No formal document is authored during the move.
- **No inferred decisions:** The previously suggested first implementation slice and verification
  bootstrap are not separately approved; resolve them in the documentation/development planning
  stage. Detailed runtime storage placement is not decided by the artifact destination.
- **Authority:** These records are the accepted design input for the new documentation process,
  not a claim that formal specifications, field contracts or implementation are already complete.
  Prior repository-internal references describe planned documents and do not import old authority.
