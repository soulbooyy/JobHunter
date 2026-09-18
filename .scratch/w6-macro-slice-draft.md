# W6 Macro Slice Draft for Contract Structure Review

> English is authoritative. This is a provisional W6 working draft, not the finalized `docs/implementation-plan.md`, a new normative authority, a completed Contract, or an implementation report. All Slice groupings and order below are proposals. W6 finalization, W7 joint review and user review remain pending.

## 1. Purpose, inputs and present boundary

The user requested a macro Slice draft first so another conversation can review Contract document structure against real prospective consumers. That structure-only discussion may occur within W6 before W7; it does not start the later field/interface-detail Contract Grill or authorize development. After structure review, Architecture retains document/family ownership, W6 binds this plan to the agreed document boundaries, and W7 reviews the complete baseline before the per-Slice detailed Contract/development cycles.

This draft follows the [English authoring spec](document-authoring-spec.en.md), [revised W5 entry](w5-progress-handoff.md#w6-entry-and-concrete-handoff) and actual [Product](../docs/spec.md), [Architecture](../docs/architecture.md), [Acceptance](../docs/acceptance.md), [Development](../docs/development.md) and [Progress](../docs/progress.md). It uses the 179-record [source matrix](../docs/progress/traceability.md), the [Decision Register](../docs/design/grill-me-design-tree.md), relevant Harness verification/ownership sections and Eval boundaries. Later controlling corrections apply inside older ACCEPTED records.

The existing repository still has no code, executable tests, normative Contract bodies, accepted actual Slice schedule or implemented capability. This draft makes no new stack/version/deployment, channel quota, scoring threshold, default enablement or release-policy choice. Its first Slice is a proposal derived from current capability dependencies, not acceptance of old suggestions under S38.1. W1–W5 remain authored drafts awaiting joint review.

The companion [Contract structure discussion prompt](contract-structure-grill-prompt.md) asks the other conversation to produce a structure proposal and reconcile it with Architecture, not to finalize schemas or create nominally complete Contract files. No conversation is created or messaged automatically by this deliverable.

## 2. Planning rules and recommended progression

Use bounded observable capabilities as delivery units. One Slice may need several families, and one family may grow across Slices. “Required Contract scope” means complete normative definitions for the relevant behavior and all necessary interfaces before that Slice's development; it does not mean the entire family or all system Contracts must be complete. Shared definitions have one owner and explicit consumers.

SL-01 through SL-12 are provisional planning identifiers, not Contract IDs, chronology guarantees or implementation statuses. Keep them stable while reviewing this draft; if splitting/merging becomes necessary, retain an explicit old-to-new mapping. No ID turns a proposed ordering into a settled architecture decision.

| Proposed Slice | Capability | Upstream implementation prerequisite |
| --- | --- | --- |
| SL-01 | [Local Workspace, Manual Jobs and Preferences](#sl-01-local-workspace-manual-jobs-and-preferences) | None |
| SL-02 | [Saved Knowledge, formal Resumes and safe materials](#sl-02-saved-knowledge-formal-resumes-and-safe-materials) | SL-01 |
| SL-03 | [Shared controlled execution with RequirementParse](#sl-03-shared-controlled-execution-with-requirementparse) | SL-01 |
| SL-04 | [Resume import into reviewed Draft and shared Save](#sl-04-resume-import-into-reviewed-draft-and-shared-save) | SL-02; SL-03 only if a model-assisted import path is selected |
| SL-05 | [Independent Candidate Fit](#sl-05-independent-candidate-fit) | SL-02, SL-03 |
| SL-06 | [Independent Resume Fit](#sl-06-independent-resume-fit) | SL-02, SL-03 |
| SL-07 | [Advisor discussion, exact Proposals and confirmed changes](#sl-07-advisor-discussion-exact-proposals-and-confirmed-changes) | SL-02, SL-03 |
| SL-08 | [BOSS collection and shared platform safety](#sl-08-boss-collection-and-shared-platform-safety) | SL-01, SL-03 |
| SL-09 | [Human-reported applications and event-derived progress](#sl-09-human-reported-applications-and-event-derived-progress) | SL-01 |
| SL-10 | [Preparation, viewed-material confirmation and adopt-back](#sl-10-preparation-viewed-material-confirmation-and-adopt-back) | SL-01, SL-02, SL-07 |
| SL-11 | [Explicit authorized execution and independent batch outcomes](#sl-11-explicit-authorized-execution-and-independent-batch-outcomes) | SL-10, SL-09; SL-08 shared platform-safety component and SL-03 outcome-sensitive recovery scope |
| SL-12 | [Collaboration Memory with independent controls and forgetting](#sl-12-collaboration-memory-with-independent-controls-and-forgetting) | SL-03, SL-07 |

A reasonable starting proposal is SL-01, then SL-02 for trusted career assets and SL-03 for the first controlled semantic capability. SL-09 can start after SL-01; it need not wait for models, Resumes or execution. Once their dependencies are ready, SL-04, SL-05, SL-06, SL-07 and SL-08 can be planned independently. SL-12 can follow SL-07 in parallel with the Preparation/execution branch. SL-10 and SL-11 complete that branch.

These are scheduling relationships, not a required user journey. Candidate Fit and Resume Fit never depend on each other. Advisor and Preparation do not require a successful Fit. Manual application reports do not require a Resume, JD, approval or browser history. SL-10's dependency on SL-07 supports the optimize/adopt-back integration; users can prepare without running Advisor. SL-11 reuses shared safety from SL-08 without requiring a successful collection. If a shared component must be delivered earlier, adjust the delivery grouping openly without weakening its invariant.

Research is a separate prerequisite to concrete source/platform/format claims. Contract structure can identify the owner and needed research without pretending that research or field design is complete. A structure proposal may expose cycles; report whether they are actual implementation dependencies, shared Contract agreements, optional paths or merely reciprocal references before imposing an order.

## 3. Contract family reference vocabulary and matrix

F01–F11 below are shorthand for the current rows of [Architecture 16.2](../docs/architecture.md#162-candidate-families-and-cross-family-references), in that order. They are local planning aliases, not new normative requirement IDs, final filenames, services or a mandate for eleven files. Architecture remains the source of responsibility boundaries. The structure review must map these aliases and each Slice's required scope to proposed document names/paths or stable structural locators; no normative field Contract is implied by a locator.

| Draft alias | Existing candidate responsibility family |
| --- | --- |
| F01 | Shared identity, exact references, concurrency, provenance, and admission |
| F02 | Workspace, Profile, and Preferences |
| F03 | Evidence, import, and baseline |
| F04 | Resume, grounding, Suggestion, and Proposal |
| F05 | Jobs, collection, source observations, and platform safety |
| F06 | Requirements, independent Fits, scoring, and batches |
| F07 | Materials, Preparation, execution, and application history |
| F08 | Harness, Skill, Run, Invocation, and Tools |
| F09 | Context, Session, and collaboration Memory |
| F10 | Budget, recovery, storage, and safe derived work |
| F11 | Eval and observability |

R means the Slice directly needs an identified scope from that family; it does not mean a full-family rewrite or that anything is already frozen. C means a conditional dependency if the optional model-assisted import path is selected, not a new mandatory feature or an accepted implementation choice. — means no additional direct scope identified here; necessary inherited scope from upstream capabilities still applies.

| Slice | F01 | F02 | F03 | F04 | F05 | F06 | F07 | F08 | F09 | F10 | F11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SL-01 | R | R | — | — | R | — | — | — | — | R | — |
| SL-02 | R | R | R | R | — | — | R | — | — | R | — |
| SL-03 | R | — | — | — | R | R | — | R | R | R | R |
| SL-04 | R | R | R | R | — | — | R | C | C | R | C |
| SL-05 | R | — | R | — | R | R | — | R | R | R | R |
| SL-06 | R | — | R | R | R | R | — | R | R | R | R |
| SL-07 | R | R | R | R | R | R | — | R | R | R | R |
| SL-08 | R | R | — | — | R | — | — | — | — | R | R |
| SL-09 | R | — | — | — | R | — | R | — | — | R | — |
| SL-10 | R | R | R | R | R | — | R | — | R | R | R |
| SL-11 | R | — | — | R | R | — | R | — | — | R | R |
| SL-12 | R | — | R | R | — | — | — | R | R | R | R |

This matrix is intentionally many-to-many. F01/common vocabulary and F10/durability are introduced only to the extent their current consumers require; they are not an up-front universal framework project. F11 is delivered with the first applicable semantic/workflow consumer, not postponed until after all product code.

## 4. Proposed Slice content

### SL-01 Local Workspace, Manual Jobs and Preferences

**Goal and business value:** Provide a useful local Job Pool and explicit search intent without requiring model calls or recruiting-site access.

**Scope:** Workspace/navigation responsibilities for delivered entry points; Manual Job roots including no-JD cases, complete immutable JobVersions, local browsing and Company read view, global hard Preferences, deterministic metadata-only QuickScreen, explicit observation/current-history distinctions. Introduce local identity/reference/persistence and privacy requirements only for these consumers.

**Out of Scope:** BOSS access, Requirement parsing, Fit, Resume editing, application execution and new bookmark/search-profile features. Undelivered entry points cannot appear implemented.

**Upstream dependencies:** No earlier Slice. Consumer-required local persistence/runtime setup and test tooling must be chosen during actual implementation preparation; this draft chooses no stack or bootstrap.

**Already-decided capabilities and provenance:** Q1, Q6–Q8, Q12–Q13, Q17, Q44–Q45, Q48, Q50, Q53, Q55–Q56, Q110, S5.1, S17.1–S17.3, S9.1. Actual behavior/mechanism owners: [P2](../docs/spec.md#2-workspace-and-task-organization); [P4](../docs/spec.md#4-jobs-preferences-and-collection); [A3](../docs/architecture.md#3-authority-identity-and-evolution); [A4](../docs/architecture.md#4-jobs-screening-collection-and-platform-access). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F05, F10.

**Required Contract scope before development:** F01: exact Job identity/version/reference and revision meanings, specific admission and history; F02: Workspace and global Preferences responsibility, with Profile/default Resume details left to SL-02; F05: Manual admission, metadata screening and observation scope; F10: durable local state, privacy and diagnostic/history separation needed here. Resolve actual consumer inputs and missing-input behavior before development; invent no universal lifecycle.

**Test / Eval categories:** Local persistence and source-identity checks, Manual root versus complete-version admission, metadata-only screening, uncertainty, latest local Preferences without remote fetch, read-view consistency and minimal diagnostics. Required proof destinations: [V3](../docs/acceptance.md#3-workspace-jobs-screening-and-collection); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not existing tests or results.

**Completion conditions:** A user can maintain local Manual Jobs and Preferences through the real boundary, with honest missing JD/unknown availability and persistent exact history. Screening neither calls a model nor acquires Candidate/Requirement authority. Required deterministic evidence and mappings exist. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-02 Saved Knowledge, formal Resumes and safe materials

**Goal and business value:** Establish trustworthy reusable career facts and formal Resumes before analyses, import automation or Advisor writes consume them.

**Scope:** Profile and manual Knowledge/Resume maintenance; page-local Draft/Save; whole current experiences; exact grounding; atomic all-affected propagation and logical deletion; default/last-Resume rules and permitted empty content. Deliver the demanded preview/export path with durable intent, exact source eligibility, safe derivative recovery and honest material readiness, without eagerly rendering all formats.

**Out of Scope:** File ingestion/reconciliation UI (SL-04), Advisor-generated Proposals (SL-07), Preparation/material approval (SL-10), private Resume career facts, KnowledgeConfirmation, persistent Assertions and draft crash recovery.

**Upstream dependencies:** SL-01 Workspace and local authority conventions. Rendering/grounding research and actual formats required for the selected scope remain Contract/implementation preparation; no mandatory model step is assumed.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q66, Q70–Q77, Q79, Q86–Q89, Q93, Q96–Q98, Q100, Q108, Q113–Q114, Q118–Q119, Q146–Q147, Q151–Q154, Q163, Q165–Q166. Actual behavior/mechanism owners: [P3](../docs/spec.md#3-candidate-knowledge-and-resumes); [A3](../docs/architecture.md#3-authority-identity-and-evolution); [A5](../docs/architecture.md#5-fact-maintenance-formal-resumes-and-derived-work). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F07, F10.

**Required Contract scope before development:** F01/F02: revision/exact-history and Profile/default behavior; F03/F04: fact/Resume/grounding ownership, full Save impact, conflict/idempotency, removal and current eligibility; F07: demanded rendered artifacts and readiness, excluding approvals/execution; F10: the same transaction's necessary durable intents, post-commit work, stale publication and historical retention. Resolve both sides of the Save/propagation/material boundary before any successful formal Save is claimed.

**Test / Eval categories:** All-affected rollback and races, direct-membership deletion, current versus historical grounding, contact versus career/presentation changes, empty states/default selection, navigation Save/Discard/Cancel, committed Save versus render failure, crash recovery and obsolete derivative publication. Required proof destinations: [V4](../docs/acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts); [V9.3](../docs/acceptance.md#93-streams-presentation-and-safe-work); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not existing tests or results.

**Completion conditions:** The actual manual maintenance and demanded material paths preserve all shared authority together; no affected current Resume waits for asynchronous fact synchronization. Unavailable derivatives block only the operations that require them. Required positive, failure, concurrency and recovery evidence exists. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-03 Shared controlled execution with RequirementParse

**Goal and business value:** Deliver the first reusable semantic capability through the real protected execution path, making later Skills consumers of one verified runtime rather than separate ad hoc integrations.

**Scope:** Application Ensure and pure requirement reads for exact complete Jobs; durable single-flight parsing, compatible reuse, owner-only charging, bounded repair and usable-target checks. Introduce the shared Run/Model/Tool admission, exact Context, budget/reservation, response/recovery/fencing, cancellation, protected-input revocation and privacy/audit substrate required by this task, plus its real-path Eval/observability support.

**Out of Scope:** Candidate/Resume Fit judgments, interactive Advisor/Session compaction, Memory learning, autonomous RAG, hidden SDK retries, whole-system generic framework work, fixed rollout thresholds or mandatory annotated parser certification.

**Upstream dependencies:** SL-01 complete JobVersion and canonical persistence. Verify selected LangGraph/Langfuse/provider SDK, masking/callback and judge capabilities before the relevant detailed integration claims; no new external research result is asserted here. Candidate Knowledge is not a parser prerequisite.

**Already-decided capabilities and provenance:** Q10, Q14, Q58–Q59, Q83, Q110–Q111, Q117, Q120–Q126, Q132, Q135–Q136, Q140–Q144, Q159, Q171–Q187, S7.1, S22.1, S24.1, S35.1. Actual behavior/mechanism owners: [P5.1](../docs/spec.md#51-shared-on-demand-requirements); [P9](../docs/spec.md#9-privacy-controlled-execution-and-honest-recovery); [P11](../docs/spec.md#11-quality-and-evidence-boundaries); [A6.1](../docs/architecture.md#61-independent-dependency-preparation); [A9](../docs/architecture.md#9-shared-harness-skills-and-controlled-actions); [A10](../docs/architecture.md#10-context-engineering); [A11](../docs/architecture.md#11-budgets-and-resource-admission); [A12](../docs/architecture.md#12-durable-execution-and-recovery); [A13](../docs/architecture.md#13-storage-retention-and-audit); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F05, F06, F08, F09, F10, F11.

**Required Contract scope before development:** F01/F05: exact Job source and task admission; F06: parse/Set validity, compatibility and shared producer/waiter scope; F08/F09/F10: the complete actual invocation, input, count/cost, durable dispatch/response, unknown outcome and settlement/recovery interfaces this path uses; F11: isolated real-path trials, exact fixtures/configuration, independent scoped judging, evidence completeness, regression retention, actual-output re-evaluation and redacted telemetry. Interactive and background-specific extensions can remain pending, but no parser safety mechanism can.

**Test / Eval categories:** Bounded parse success/repair/failure and unusable targets; concurrent Ensure/waiter cancellation/owner failure; exact admitted inputs/capacity/revocation; hidden retry prevention, atomic budget/race/fault-injection and unknown usage; real-JD/manual semantic review; isolated replay/live trials, alternative valid outputs, independent judge and telemetry-failure evidence. Required proof destinations: [V5.1](../docs/acceptance.md#51-dependency-preparation-and-bounded-parsing); [V8](../docs/acceptance.md#8-harness-tools-and-actual-context); [V9](../docs/acceptance.md#9-budget-durable-execution-and-recovery); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V12](../docs/acceptance.md#12-eval-execution-and-evidence-integrity); [V13](../docs/acceptance.md#13-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Completion conditions:** Compatible validated Requirements are reusable without duplicate producer cost or invented downstream requirements. Crash/unknown/cancel paths neither replay unsafe calls nor lose local authority/evidence. The real task's deterministic and semantic checks execute with explicit limits; other Harness features are not declared complete merely because this path works. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-04 Resume import into reviewed Draft and shared Save

**Goal and business value:** Bring existing resumes into the workspace without turning a parser's interpretation into unreviewed formal facts.

**Scope:** Upload and structural import, preserving sections/whole experiences; proposed Profile/Evidence changes; human reconciliation, conflict resolution and completeness of factual support; use SL-02's atomic Save, eligibility and demanded material path.

**Out of Scope:** Immediate formalization on upload, automatic conflict merges, omission-as-deletion, permanent bullet/Assertion graphs, a second fact-confirmation object, or a new mandatory semantic-enhancement Skill.

**Upstream dependencies:** SL-02's formal authority command and Draft/material behavior. If the eventual design uses an optional business-model step, SL-03's admitted invocation/Context/Eval scope is additionally required; this draft does not choose that option or model. Source-document parsing and retention details await focused work.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q70–Q75, Q98, Q108, Q113–Q114, Q118–Q119, Q146, Q163, Q166. Actual behavior/mechanism owners: [P3.2](../docs/spec.md#32-import-review-and-save); [A5.1](../docs/architecture.md#51-preparation-before-authority); [A5.2](../docs/architecture.md#52-one-atomic-authority-change). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F07, F10; F08, F09, F11 conditionally, as described above.

**Required Contract scope before development:** F01/F02/F03/F04: imported-source and Draft/reconciliation responsibilities, support resolution and exact Save reuse; F07/F10: source-document/material handling, privacy and disposal versus saved authority. Only if a model step is selected, complete the relevant F08/F09/F11 interfaces before using it. No raw source document becomes model-visible by default.

**Test / Eval categories:** Structure preservation, conflicting matches, absent experiences, user-authorized facts, unresolved-support Save refusal, atomic rollback, navigation/crash distinction and no source-document leakage; semantic checks only for model behavior actually introduced. Required proof destinations: [V4.1](../docs/acceptance.md#41-authority-import-and-atomic-save); [V4.3](../docs/acceptance.md#43-demand-and-safe-derivative-recovery); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V13.1](../docs/acceptance.md#131-capability-specific-review). These are future obligations, not existing tests or results.

**Completion conditions:** Import produces reviewable temporary proposals, and only the shared valid Save path creates formal versions. Skipping an old experience does not delete it. Evidence describes the selected parsing path honestly, without claiming optional model work ran. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-05 Independent Candidate Fit

**Goal and business value:** Assess the user's admitted saved Knowledge against one Job's reusable Requirements, with bounded conclusions and defensible score availability.

**Scope:** Independent CandidateJobFit selection/Run/result; two-stage freeze and actual complete admitted baseline; task-scoped assessment meanings, deterministic score/rescore policy, valid unscored results; target serialization/latest compatible success, history and multi-Job task orchestration.

**Out of Scope:** Resume Fit as a prerequisite, coupled dual-axis analysis, score ordering/gaps, capability claims beyond inspected saved facts, automatic RAG/model switching or silent trimming.

**Upstream dependencies:** SL-02 current Evidence baseline, not possession of a formal Resume; SL-03 RequirementSet reuse/Ensure, shared runtime and task evidence. SL-06 and Advisor are not prerequisites.

**Already-decided capabilities and provenance:** Q19, Q35, Q46, Q51, Q72, Q82–Q83, Q110–Q117, Q123, Q135, Q142, Q168, Q171–Q172, Q184, Q186, S22.1. Actual behavior/mechanism owners: [P5](../docs/spec.md#5-requirements-and-independent-fit-analyses); [A6](../docs/architecture.md#6-requirements-fit-and-analysis-orchestration); [A10.2](../docs/architecture.md#102-protected-inputs-and-ordered-reduction); [A11](../docs/architecture.md#11-budgets-and-resource-admission); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F03, F05, F06, F08, F09, F10, F11.

**Required Contract scope before development:** F01/F03/F05/F06: exact baseline/Job/Requirements, eligibility, selection/final freeze, target keys, compatible publication and score availability; F08/F09/F10: per-task admission, bounded repair, frozen permission and shared-operation budget ownership; F11: Candidate-scoped judging and separate Skill-versus-composed-workflow evidence. Complete selected score policy expressions without inventing a rollout threshold.

**Test / Eval categories:** Actual Frame coverage and bounded negatives, UNKNOWN and valid unscored outcomes, unusable dependency fail-fast, no Memory/Resume leakage, capacity/revocation termination, competing targets and failed rerun preservation, partial batch outcomes and separate parse/Fit costs. Required proof destinations: [V5](../docs/acceptance.md#5-requirements-and-independent-fits); [V8.2](../docs/acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9.1](../docs/acceptance.md#91-owners-reservations-and-limits); [V12](../docs/acceptance.md#12-eval-execution-and-evidence-integrity); [V13](../docs/acceptance.md#13-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Completion conditions:** A user can independently run Candidate Fit and inspect grounded, scope-limited results/history; optional scoring absence is honest. Composed workflow evidence includes actual dependency preparation, and Skill-only trials do not claim parser quality. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-06 Independent Resume Fit

**Goal and business value:** Assess what an exact formal Resume actually expresses, without silently supplementing it from all Candidate Knowledge.

**Scope:** Independent ResumeJobFit selection/Run/result/history; exact eligible Resume/Requirement inputs; permitted grounding validation, scoped assessments, independent score/rescore/unscored behavior; compatible target serialization and per-Job selection/orchestration.

**Out of Scope:** Candidate Fit as a prerequisite or authority, unseen Knowledge added through grounding or judges, ResumeCoverage/score-gap models and mandatory ordering between the two scores.

**Upstream dependencies:** SL-02 formal Resume/grounding/current eligibility; SL-03 shared Requirements/runtime/Eval. SL-05 is independent. Shared F06 implementation may be reused without merging task identity, authority or output.

**Already-decided capabilities and provenance:** Q19, Q35, Q46, Q51, Q75, Q77, Q82–Q83, Q87, Q110–Q117, Q123, Q142, Q168, Q171–Q172, Q184, Q186, S5.3, S22.1. Actual behavior/mechanism owners: [P5](../docs/spec.md#5-requirements-and-independent-fit-analyses); [A5.4](../docs/architecture.md#54-grounding-and-demand-driven-artifacts); [A6](../docs/architecture.md#6-requirements-fit-and-analysis-orchestration); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F03, F04, F05, F06, F08, F09, F10, F11.

**Required Contract scope before development:** F01/F03/F04/F05/F06: exact expressed Resume scope, grounding-as-validation, current-use and output/score/target meaning; F08/F09/F10: this task's protected inputs and budget/concurrency/recovery reuse; F11: Resume-scoped evaluator evidence distinct from broader deterministic audit access. Shared family ownership cannot make Candidate Fit an operational dependency.

**Test / Eval categories:** Candidate/other-Resume leakage, incomplete inspection versus MISSING, original/current version compatibility, unscored assessments, two freeze points, fail-closed capacity/revocation and independent success/failure/batch history. Required proof destinations: [V5](../docs/acceptance.md#5-requirements-and-independent-fits); [V8.2](../docs/acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9.1](../docs/acceptance.md#91-owners-reservations-and-limits); [V12](../docs/acceptance.md#12-eval-execution-and-evidence-integrity); [V13](../docs/acceptance.md#13-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Completion conditions:** Resume Fit runs and remains understandable on its own, with evidence limited to what that Resume expresses. Candidate Fit can be absent, fail or have a different score without invalidating a valid Resume Fit. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-07 Advisor discussion, exact Proposals and confirmed changes

**Goal and business value:** Turn conversational resume advice into trustworthy, explicitly confirmed formal changes without creating a second editing authority.

**Scope:** One durable Session model, bounded foreground Turns, general and Job-specific Advisor entry, lazy exact admitted reads, verifiable user statements, discussion/default/apply-target distinctions, Suggestions and concrete target-specific Proposals; ended generating Run and later Application confirmation, shared Save, narration/commit separation and deletion races. Include necessary interactive Context reduction/checkpoints, auxiliary limits and exact source retention. Add full Scenario/N+1 evaluation for these interactions.

**Out of Scope:** Either Fit as a prerequisite, Advisor ResumeDraft/export, inferred target or consent, continuing a Run through human confirmation, unrestricted chat search; persistent collaboration Memory itself is SL-12 and remains required v1 work.

**Upstream dependencies:** SL-02 formal facts/Resume/default/shared Save; SL-03 runtime and Application-owned Requirement preparation for Job-specific work only. General conversation needs no Job/RequirementSet, and neither Fit is required. Preparation-originated entry/adopt-back integration is completed in SL-10.

**Already-decided capabilities and provenance:** Q24, Q41, Q47, Q52, Q85, Q88–Q89, Q93–Q94, Q128, Q132–Q144, Q146, Q148–Q149, Q155–Q159, Q166–Q167, Q178, Q180, Q183–Q185. Actual behavior/mechanism owners: [P6](../docs/spec.md#6-job-assistant-and-resume-advisor); [P9.3](../docs/spec.md#93-conversation-context-and-retention); [A7](../docs/architecture.md#7-session-advisor-proposal-and-confirmed-changes); [A9](../docs/architecture.md#9-shared-harness-skills-and-controlled-actions); [A10](../docs/architecture.md#10-context-engineering); [A12](../docs/architecture.md#12-durable-execution-and-recovery); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F05, F06, F08, F09, F10, F11.

**Required Contract scope before development:** F01–F06 relevant facts/target/Proposal/Job/Ensure interfaces; F08/F09/F10 foreground ownership, pure typed reads, Session provenance, compaction, exact post-write inputs, durable Proposal/confirmation/deletion and committed-result recovery; F11 coherent N+1 boundaries and fixed authored multi-step Scenarios. Context ownership is complete for delivered conversation even before SL-12 Memory exists.

**Test / Eval categories:** Lazy actual visibility, target/default and exact patch, one concrete confirmation, ended Run and free Session, dependency wait versus human wait, source spoofing and privacy, concurrent deletion/confirmation, saved result with failed narration, budgeted compaction/fencing, exact-one Proposal selection in real-path Scenarios. Required proof destinations: [V6](../docs/acceptance.md#6-advisor-proposal-confirmation-and-session); [V8](../docs/acceptance.md#8-harness-tools-and-actual-context); [V9](../docs/acceptance.md#9-budget-durable-execution-and-recovery); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V12.2](../docs/acceptance.md#122-n1-and-complete-scenarios); [V12.3](../docs/acceptance.md#123-evaluator-inputs-authority-and-conclusions); [V13](../docs/acceptance.md#13-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Completion conditions:** Advice and an exact confirmed change work through the real Application/Save boundary, with honest independent commit/presentation outcomes and full boundary evidence. Any pre-SL-12 delivery is explicitly partial against full v1 Memory capability, not a change to v1 scope or default enablement. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-08 BOSS collection and shared platform safety

**Goal and business value:** Acquire eligible complete Jobs without unnecessary detail access or unsafe platform activity, and establish safety shared with later execution.

**Scope:** User-authorized initial/explicit collection and refresh; metadata screening before full details, complete Job+version admission, local browsing, aggregate rejection audit, exact source observations, frozen collection Preferences versus latest local filtering; stop/partial results and persistent account/platform safety with explicit strong-risk restoration.

**Out of Scope:** Requirement parsing as part of collection, model-autonomous browsing, recoverable rejected-content datasets, cross-platform merge, background polling/Monitor, cooldown-only strong-risk reset, default numeric quotas.

**Upstream dependencies:** SL-01 Preferences/Jobs; reuse the relevant durable outcome/audit/recovery scope first demonstrated in SL-03, without making Collector an Agent Skill or requiring model invocation. Pinned upstream source/license/mapping and channel research precede concrete adapter claims.

**Already-decided capabilities and provenance:** Q3, Q27, Q44–Q45, Q48–Q50, Q55–Q56, Q110, Q122, Q160–Q161, Q164, S9.1. Actual behavior/mechanism owners: [P4](../docs/spec.md#4-jobs-preferences-and-collection); [P8.2](../docs/spec.md#82-batch-behavior-and-shared-platform-safety); [A4](../docs/architecture.md#4-jobs-screening-collection-and-platform-access); [A8](../docs/architecture.md#8-preparation-execution-and-application-events); [A12](../docs/architecture.md#12-durable-execution-and-recovery); [A13](../docs/architecture.md#13-storage-retention-and-audit); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F05, F10, F11.

**Required Contract scope before development:** F01/F02/F05: source identity, admission, frozen Preferences, adapter observations/audit, platform/account safety ownership and recovery; F10: durable stop/outcome/retention obligations for platform work; F11: controlled adapter fixtures and evidence. Agree shared safety admission with F07's future Executor consumer at the interface level, without designing every later execution payload.

**Test / Eval categories:** No detail fetch on definite rejection, no rejected-content persistence, strict BOSS versus Manual admission, local changes without fetch, mid-collection Preferences edits and cancellation, risk persistence/restart, ordinary failure versus strong risk and no implicit execution permission after restoration. Required proof destinations: [V3](../docs/acceptance.md#3-workspace-jobs-screening-and-collection); [V7](../docs/acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.2](../docs/acceptance.md#92-crash-and-cancellation-boundaries); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V12.1](../docs/acceptance.md#121-isolation-exact-inputs-and-declared-experiment-scope). These are future obligations, not existing tests or results.

**Completion conditions:** Actual collection and refresh preserve complete Jobs, bounded operational evidence and shared safety; local reads cause no platform access. Controlled tests prove the relevant risk/stop boundaries; tests do not themselves authorize live account access or certify source quotas. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-09 Human-reported applications and event-derived progress

**Goal and business value:** Track real applications and interview events immediately, including manual Jobs with no JD, without waiting for automated execution.

**Scope:** Explicit human reports, separate real attempts and reapplication, append-only deduplicated events, occurrence/observation distinctions, appended correction/retraction and versioned projected progress. My Applications reflects real evidence.

**Out of Scope:** Invented browser/Snapshot/approval history, automatic execution, an independent Interview Aggregate/assistant or a freely writable duplicate progress authority.

**Upstream dependencies:** SL-01 Job identity/local persistence only. No Profile/Resume, RequirementSet, Fit, Preparation, Collector or Executor prerequisite is introduced for a legitimate human report.

**Already-decided capabilities and provenance:** Q7, Q16–Q17, Q21, Q30–Q31, Q36–Q37, Q44, Q48. Actual behavior/mechanism owners: [P8.3](../docs/spec.md#83-real-application-history); [A8](../docs/architecture.md#8-preparation-execution-and-application-events). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F05, F07, F10.

**Required Contract scope before development:** F01/F05: Job and real-attempt identity/history references, including Manual roots without JobVersion; F07: human provenance, event/correction/deduplication and projection-policy responsibilities, kept distinct from future Executor technical evidence; F10: durable event history and appropriate privacy. Concrete event detail is later Grill work.

**Test / Eval categories:** Manual no-JD reports, duplicate/delayed events, separate repeated attempts, appended corrections/retractions and derived progress; absence of fabricated execution receipts or consent. Required proof destinations: [V7](../docs/acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not existing tests or results.

**Completion conditions:** A user can record and review truthful application/interview history independently of automated paths. Evidence traces every displayed progression to actual admitted events and a policy, without rewriting history. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-10 Preparation, viewed-material confirmation and adopt-back

**Goal and business value:** Prepare exact current materials and a manually editable Greeting for each Job, making confirmed content and later execution authorization distinct.

**Scope:** Single/multi-Job independent Preparation, idempotent create/resume/reentry and revision conflicts; formal material selection/view, fixed generic Greeting, eligibility/render/readiness, actual-view MaterialApproval and exact snapshot preparation. Integrate existing Advisor through the same Session/entry semantics and explicit narrow adopt-and-return.

**Out of Scope:** Automatic sending, ExecutionApproval/Attempt consumption, editing Resume body inside Preparation, personalized/generated Greeting or silent adoption of changed facts.

**Upstream dependencies:** SL-01 Job identity; SL-02 saved eligible material and safe requested renders; SL-07 for the accepted optimize-and-return integration. This is a development integration dependency, not a requirement that users run Advisor or either Fit before ordinary preparation. Detailed channel/material requirements need related research.

**Already-decided capabilities and provenance:** Q16, Q25, Q30, Q36, Q42, Q77, Q91, Q108, Q118, Q146–Q147, Q150, Q152, Q157, Q162, Q165. Actual behavior/mechanism owners: [P7](../docs/spec.md#7-application-preparation-and-materials); [A5.4](../docs/architecture.md#54-grounding-and-demand-driven-artifacts); [A7](../docs/architecture.md#7-session-advisor-proposal-and-confirmed-changes); [A8](../docs/architecture.md#8-preparation-execution-and-application-events). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F05, F07, F09, F10, F11.

**Required Contract scope before development:** F01–F05 exact Job/Profile/Evidence/Resume/grounding references and current eligibility; F07 Preparation, Greeting, actual viewed artifact approval and immutable intended-input boundary; F09 Advisor entry references only, without changing apply target; F10 safe demanded rendering; F11 authored adoption/conflict evidence. Settle handoffs to the future execution-approval owner without treating content approval as permission to send.

**Test / Eval categories:** Actual rendered artifact versus mere version, Greeting reconfirmation, unchanged bytes with revoked eligibility, concurrent edits, duplicate reentry and multiple candidates, explicit adopt-back preserving Greeting/unrelated edits, render failure and independent batch preparation. Required proof destinations: [V4.3](../docs/acceptance.md#43-demand-and-safe-derivative-recovery); [V6](../docs/acceptance.md#6-advisor-proposal-confirmation-and-session); [V7](../docs/acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.3](../docs/acceptance.md#93-streams-presentation-and-safe-work); [V12.2](../docs/acceptance.md#122-n1-and-complete-scenarios). These are future obligations, not existing tests or results.

**Completion conditions:** Prepared and confirmed content is inspectable and exactly bound, including an honest readiness failure when required materials are absent. Neither approval nor snapshot performs external action; adopted formal changes require no hidden target or permission. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-11 Explicit authorized execution and independent batch outcomes

**Goal and business value:** Execute exactly approved applications with trustworthy outcome tracking, bounded shared platform access and honest uncertainty.

**Scope:** Separate exact, scoped, expiring, single-use ExecutionApproval; at most one Attempt consuming it; frozen material/source eligibility; authorized minimal live identity/availability checks; independent per-Job scheduling/outcomes, narrower renewed approval for partial continuation, reliable read-back into real application events and persistent shared risk handling.

**Out of Scope:** Silent Job refresh or Requirement parsing, new model Job analysis, automatic replay after unknown effects, assuming a technical click is business success, cross-Job transactions, undispatched-as-failed reporting and future Monitor.

**Upstream dependencies:** SL-10 frozen/viewed materials, SL-09 real event authority, the shared safety scope introduced by SL-08 and outcome-sensitive recovery reused from SL-03. Collector success is not a runtime prerequisite; the shared safety component must be ready even if scheduling changes. Verify actual channel/read-back feasibility before detailed integration claims.

**Already-decided capabilities and provenance:** Q25, Q30–Q31, Q36–Q37, Q42, Q77, Q122, Q150, Q157, Q160, Q164, Q173–Q174. Actual behavior/mechanism owners: [P8](../docs/spec.md#8-external-execution-and-application-tracking); [A4.3](../docs/architecture.md#43-observation-and-safety-boundaries); [A8](../docs/architecture.md#8-preparation-execution-and-application-events); [A12](../docs/architecture.md#12-durable-execution-and-recovery); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F04, F05, F07, F10, F11.

**Required Contract scope before development:** F01/F04/F05 exact eligible material/Job identity, minimal verification and shared risk; F07 snapshot, separate consent, Attempt, technical versus real events and batch membership/outcomes; F10 durable dispatch/unknown/recovery without unsafe replay; F11 controlled scenario evidence. Complete cross-family approval/safety/receipt boundaries before enabling any external effect; planned paths or mocked success cannot satisfy readiness.

**Test / Eval categories:** Concurrent double consumption, stale/changed input, closure/mismatch without refresh, crash around dispatch/receipt, unknown results without success/retry, reliable read-back/human evidence, Collector-to-Executor risk propagation, explicit restoration without auto-resume, independent batch/undispatched outcomes. Required proof destinations: [V7](../docs/acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.2](../docs/acceptance.md#92-crash-and-cancellation-boundaries); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V12.1](../docs/acceptance.md#121-isolation-exact-inputs-and-declared-experiment-scope); [V12.2](../docs/acceptance.md#122-n1-and-complete-scenarios). These are future obligations, not existing tests or results.

**Completion conditions:** The delivered channel executes only admitted frozen approvals and records real outcomes with traceable evidence; uncertain outcomes remain uncertain. Deterministic/fault/scenario checks use controlled adapters; they grant no live recruiting-site access themselves. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

### SL-12 Collaboration Memory with independent controls and forgetting

**Goal and business value:** Carry permitted collaboration preferences between conversations while keeping saved career facts, consent and task evidence under their existing owners.

**Scope:** Admitted user-sourced collaboration Memory, independent background MemoryExtraction, durable ranges/coalescing and isolated failed/unknown ranges; Auto Learning/Recall/manual management, allowed summaries/lookups, source/entry deletion and non-resurrection; independent background budgets/capacity and controlled Memory Eval. Recheck Session deletion, checkpoint source exclusion and current Recall admission.

**Out of Scope:** Career USER_FACT store, unrestricted chat search, automatic historical backfill, complex Memory graphs/vector consolidation, General Assistant/interview Skills, Candidate Evidence RAG and erasure of indirect influence from real past assistant messages.

**Upstream dependencies:** SL-07 durable authorized Session sources and independent Context machinery; SL-03 shared invocation/admission/unknown recovery, extended for separate background owners and priority/capacity. F03/F04 business-write boundaries are referenced to prevent Memory replacing facts, not to grant writes.

**Already-decided capabilities and provenance:** Q127–Q133, Q135–Q139, Q145, Q155, Q167, Q169–Q170, Q172, Q187. Actual behavior/mechanism owners: [P10](../docs/spec.md#10-collaboration-memory); [A10](../docs/architecture.md#10-context-engineering); [A14](../docs/architecture.md#14-collaboration-memory); [A15](../docs/architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; the proposed Slice placement/order is this draft's planning arrangement.

**Dependent Contract families:** F01, F03, F04, F08, F09, F10, F11.

**Required Contract scope before development:** F01/F03/F04 source and authority restrictions; F08 MemoryExtraction task scope; F09 independent controls, admitted source ranges, entries/derived summaries, recall and forgetting; F10 background budget/headroom, pending-range durability, deleted-source publication and retention; F11 controlled learning fixtures/scenarios with separate cost/evidence. Exact ranges/markers/policies and values await Grill; do not infer defaults from examples.

**Test / Eval categories:** Three independent controls, Skill allowlists and no Fit/parse Memory exposure, checkpoint exclusion/current Recall, failed-range isolation, deleted Session publication ban, manual edits beating older extraction, forgetting without resurrection, startup/unknown extraction and background capacity, comparable frozen-Memory versus explicit-learning Scenarios. Required proof destinations: [V8.2](../docs/acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9](../docs/acceptance.md#9-budget-durable-execution-and-recovery); [V10](../docs/acceptance.md#10-privacy-storage-and-honest-history); [V11](../docs/acceptance.md#11-collaboration-memory); [V12.1](../docs/acceptance.md#121-isolation-exact-inputs-and-declared-experiment-scope); [V12.2](../docs/acceptance.md#122-n1-and-complete-scenarios); [V13](../docs/acceptance.md#13-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Completion conditions:** Permitted collaboration reuse and management work without changing business facts or consent. Background failures do not roll back foreground success or silently rejoin later ranges. Actual learning evidence is separate from learning-disabled Advisor trials. This is required v1 scope, not a post-v1 deferral. All necessary Contract scope must have been written and reconciled before development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now.

## 5. Cross-cutting work belongs to its first consumer

| Responsibility | First required delivery and later extensions | Preserved boundary |
| --- | --- | --- |
| Identity, canonical persistence and privacy | SL-01's real local consumers, SL-02's multi-asset authority, then every relevant Slice | No generic lifecycle, invented Candidate root or assumed package/database layout; new-system original history remains interpretable |
| Atomic facts and safe derivatives | SL-02, reused by SL-04/SL-07/SL-10 | Save includes all affected authority and necessary durable intent; demand-driven render failure never converts to an asynchronous authority gap |
| Model/Tool execution, exact input, budget and unknown recovery | SL-03 before its first actual provider call; SL-05/SL-06 reuse exact-task rules; SL-07 adds interactive Context; SL-12 adds background ownership | No temporary unguarded model path, hidden SDK retry, protected-input degradation or remote replay; enforce relevant safeguards when the path first exists |
| Eval and redacted observability | SL-03 real parsing path, exact fixtures/configuration, independent scoped judges, completeness, retention/re-evaluation and admitted export; SL-05/SL-06 extend scoped Fit and composed workflows | No test-only Agent, telemetry-owned success, expected-answer leakage, invented threshold or delayed safety enforcement |
| Scenario driving and coherent N+1 | SL-07 for real discussion/Proposal/confirmation; SL-10/SL-11 extend workflow cases; SL-12 extends controlled Memory/background cases | Actual uniquely matching Proposal through Application, no consent/state injection; recorded replay and live behavior are distinct |
| External platform safety and outcome evidence | SL-08 introduces shared persistent safety; SL-11 consumes that exact owner and adds execution authorization/evidence | Capacity/risk recovery is not consent or automatic restart; technical action is not an application event |
| Retention, historical readability and forgetting | Each asset/payload owner from first persistence; runtime scopes in SL-03, Session/Context in SL-07, Memory-specific forgetting in SL-12 | Active recovery pins differ from historical availability; no current-state reconstruction mislabeled as an old Frame and no whole-Workspace trace export |

Eval remains an implementation responsibility of the relevant Slice, even though this draft adds no separate “Eval platform last” Slice. SL-03 is intentionally substantial: it introduces only the complete shared contracts needed to deliver and prove RequirementParse, not every future Skill. SL-02 and SL-07 are also broad because their atomicity/confirmation boundaries cannot be weakened. Structure review may recommend smaller delivery increments with explicit acceptance scope; retain the first-use safeguards and source trace in any split.

No unfinished current-v1 item becomes Deferred solely because it is scheduled later. In particular, SL-12 Memory is still required v1 work. An earlier Advisor increment can be reported as a bounded implemented subset when proven, but cannot establish complete v1 Advisor/Memory delivery. Production defaults and rollout consequences remain later Q175 work.

## 6. Capability coverage and exclusions

| Owning Product scope | Proposed coverage and limits |
| --- | --- |
| Product 2: workspace/task organization | SL-01 navigation/local organization; each later Slice adds its actual entry/workflow; no mandatory product pipeline |
| Product 3: Knowledge, import, Resumes, materials | SL-02 authority/manual maintenance/grounding/materials, SL-04 import, SL-07 confirmed conversational changes, SL-10 material adoption/approval |
| Product 4: Jobs, Preferences, collection | SL-01 local/Manual/Preferences/screening, SL-08 BOSS/refresh/safety |
| Product 5: Requirements and independent Fits | SL-03 parsing/Ensure, SL-05 Candidate Fit, SL-06 Resume Fit, with independent task selection and batch semantics preserved |
| Product 6: Advisor and Session | SL-07; Preparation-originated entry and explicit return in SL-10; independent Memory integration in SL-12 |
| Product 7: Preparation/material approval | SL-10, consuming safe artifacts from SL-02 and formal changes from SL-07 |
| Product 8: execution and application history | SL-09 manual event/history authority, SL-11 approved execution/batches, SL-08/SL-11 shared safety |
| Product 9: privacy, execution and recovery | First-use safeguards across SL-01/SL-02/SL-03, interactive Context in SL-07, platform/Memory extensions in SL-08/SL-11/SL-12 |
| Product 10: collaboration Memory | SL-12, with supporting Session/runtime boundaries already owned by SL-07/SL-03 |
| Product 11: evidence and quality | Deterministic proof with each affected Slice; semantic/Eval foundations from SL-03, scoped evidence and Scenario extensions as above |
| Product 12: non-goals and pending detail | No Slice adds rejected merge/Overlay, KnowledgeConfirmation, Advisor Draft, Coverage authority, RAG fallback, General Assistant/interview Skills, bookmark UX, mandatory Monitor or legacy migration |

The original 179-record matrix remains the source-clause index. This macro coverage table and individual Q-ID lists are not a fresh complete clause audit or final W6 traceability mapping. Formal W6 completion must reconcile source clauses and actual Contract structure; W7 still applies all 29 semantic regressions and the process checks. No removed record is restored.

Current detail still pending includes per-function inputs, precise interfaces/references/target keys, approval/concurrency protocols, scoring values, budget/Context/Memory policies, retention/cleanup, render/channel criteria and Eval interfaces/metrics. Q117 certification and Q175 rollout remain separately deferred; S24.1 Candidate Agentic RAG remains post-v1. The structure discussion locates their owners without answering them.

## 7. Questions for the Contract structure conversation

1. Map each current family to coherent prospective documents and single owners. Use consumer/change boundaries; neither an object-per-file rule nor a one-family-per-file rule is assumed.
2. For each SL identifier, identify exact structural destinations and the required scope within them, already-shared scope versus newly needed scope, allowed later scope and cross-document dependencies.
3. Reconcile all seven groups in Architecture 16.3: Save/propagation/intent; Proposal/Session/confirmation; Requirements/Fit/Harness; materials/execution/safety; Context/Memory/Storage; Budget/Runtime/Recovery; Eval versus real canonical semantics.
4. Keep shared definitions sufficient for the earliest consumers without forcing all later fields or workflows to be specified. Distinguish joint interface agreement from a whole-Slice implementation dependency.
5. Identify any ambiguous ownership, actual dependency cycle, oversized Slice or conditional choice requiring clarification. Propose a bounded structural adjustment with source and consumer consequences; do not invent new business behavior.
6. Return the family-to-document map, responsibility/exclusion/reference catalog, Slice-to-document required-scope matrix, suggested structural Grill grouping/order and unresolved questions. Proposed filenames are structure, not created or completed Contracts.
7. Once the structure is agreed through that conversation, write its responsibility/reference outcome to Architecture 16 and a structural handoff. Retain the eleven-family provenance map and source IDs; downstream W6 planning incorporates the result before formal plan finalization.

Structure-only discussion within W6 and the later per-Slice detailed Contract Grill are distinct. The former can organize a future field owner; it does not decide a field, schema, lifecycle enum, API payload, error vocabulary, migration protocol or complete transition matrix. No normative Contract body should be created merely to anchor a link.

## 8. Scoped review and continuation

**Decision-to-Document Traceability Seam:** Each proposed Slice maps accepted capabilities to current owners, controlling Q-IDs, candidate families, required Contract scope and Acceptance destinations. Product topic coverage and all eleven family consumers are visible. Ordering and grouping are explicitly provisional planning proposals; excluded/deferred content remains outside the current capability list. Contract filenames, structural locators and normative IDs are not invented as settled facts.

**Cross-Document Semantic Consistency Seam:** The draft preserves independent Fits, Advisor without Fit prerequisites, manual reporting without automated history, complete all-affected Save, actual viewed material versus execution consent, protected input/unknown outcome rules, and separate Memory/Eval authority. Development dependencies are distinguished from runtime prerequisites. Current ownership is still in Product/Architecture/Acceptance/Development; this working draft is an input to W6, not a substitute for those owners.

No scoped contradiction was identified in those mappings. Remaining review work includes Contract document decomposition, conditional import choices, shared-component granularity and full clause-level W6/W7 checks. No product test has run, no implementation is complete, and no final W6 handoff is produced by this macro draft.

Mechanical checks covered all twelve Slice entries and eleven family aliases, required per-Slice content, the dependency graph including conditional/shared prerequisites, 588 local links/anchors and 84 source ranges across the two new working files and two updated status files. No graph cycle or reference/structure/whitespace issue was found. The existing matrix still covers all 179 records. All twenty other pre-existing Markdown inputs retain their incoming hashes, including the original Grill records, Architecture, both authoring-spec editions and W1–W5 handoffs. These checks do not establish complete clause semantics, Contract readiness or product acceptance.

Next: use the companion prompt in the other conversation to perform the bounded structure review; carry agreed structural mappings back to Architecture and W6. Then author/finalize `docs/implementation-plan.md`, reconcile Progress/matrix with real planning references, produce the W6 completion handoff and proceed to W7/user review. Current Slice detail remains for its later Contract Grill before development.
