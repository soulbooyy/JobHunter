# JobHunter Document Authoring Spec

> **Language and authority rule — explicit user instruction:** This English edition is the authoritative document-authoring spec. Preserve `document-authoring-spec.md` as the existing Chinese reference; if the two editions differ, this English edition governs. All formal documents authored next—including Product Spec, Architecture, Contracts, Acceptance, Development, Progress, and their supporting documentation—must be written in English. English is the authoritative language. Chinese editions of the formal documents are not planned at this stage. This rule concerns documentation language; it does not change the accepted product UI labels or reopen architecture decisions.

## Problem Statement

The new JobHunter repository currently contains only nine completed Architecture Grill decision and design records. It has no formal product documentation, code, tests, or implemented features. Subsequent documentation will be authored across multiple tasks and contexts. Rereading historical answers without a shared authoring specification risks omitting decisions, assigning them to the wrong documents, or restoring clauses that remain inside ACCEPTED records but have been superseded in part.

The effective design needs to become a transferable, verifiable basis for authoring six documentation categories: product, architecture, Contracts, acceptance, development, and actual progress. That basis must preserve provenance and supersession, distinguish settled decisions from architecture-only boundaries and matters awaiting the later Contract Grill, and avoid presenting designs, examples, research references, or plans as current implementation.

## Solution

Produce a local document-authoring spec as the shared input for subsequent tasks. It synthesizes effective decisions, assigns document responsibilities, specifies task dependencies and handoff requirements, and uses the two related verification seams confirmed by the user:

1. **Decision-to-Document Traceability Seam**: effective Grill decisions → formal documents, verifying controlling Q-IDs, supersession, coverage, ownership, and reasons for deferral or exclusion.
2. **Cross-Document Semantic Consistency Seam**: formal documents ↔ formal documents, verifying consistent responsibilities, terminology, authority, state, and reference semantics. The same design fact must not acquire conflicting authorities.

This is a spec for documentation work, not the JobHunter product specification, a detailed Contract, or a seventh category of formal authority. This step delivers only the authoring spec; it does not create the six formal document categories. Follow Q22/S38.1: author and review the five main documents while planning Contract structure and responsibilities → conduct the separate detailed Contract Grill → complete Contracts and reconcile affected references → begin formal development. Exact paths, sources, and task handoffs are in Further Notes. Apply the opening English-language authority rule throughout that work.

## User Stories

Not applicable. This work documents an already-decided architecture and enables handoffs across contexts. It does not add product features or invent product User Stories to fit the template. Authoring requirements belong in Implementation Decisions; verification belongs in Testing Decisions.

## Implementation Decisions

### 1. Decision interpretation, terminology, and baseline

- Use the nine Grill records as design inputs and interpret later corrections at clause level. A newer decision supersedes only the semantics it actually addresses. It neither invalidates the entire earlier record nor permits obsolete mechanisms to survive because their parent record remains ACCEPTED. Resolve supersession before describing final behavior; do not present contradictory historical passages as simultaneous requirements.
- Preserve each effective design fact's source Q-ID/S-ID, controlling decision, and relevant detailed-module section. Historical descriptions of the old repository's “current” problems, implementation completion, or migration assumptions must not become facts about this new repository. Removed Q-IDs may explain supersession, but their text or mechanisms must not be reconstructed or restored.
- The Contract Design Inventory is a non-normative design checklist. Object names, example attributes, state labels, and conceptual diagrams are not complete Contracts. Do not translate its rows directly into field definitions, interfaces, or database tables. Example code layouts, numbers, model configurations, and deployment arrangements in module records must not be promoted into accepted requirements.
- Keep the domain names and distinctions among CandidateProfile, PreferenceSet, EvidenceItemVersion, EvidenceBaselineSnapshot, ResumeVersion, ResumeGroundingSet, RequirementSet, the two Fit Analysis types, ChangeProposal, ApplicationPreparation, and the different approval, execution, and application events. Resolve historical generic DeepFitAnalysis wording to the actual analysis type; do not create a new unified result authority.
- Task numbers, topic groupings, and checklists in this document organize authoring only. They add no Domain objects, product requirement IDs, Contract IDs, or business states. (Q2–Q5, Q11, Q22, Q26, S24.2, S29.2, S37.1, S38.1)

### 2. Responsibilities of the six formal document categories

| Category | Owns | Boundary with other categories |
| --- | --- | --- |
| Product Spec | Users, scope, non-linear task organization, entry points, prerequisites, visible outcomes and failures, non-goals | Does not duplicate field Contracts, equate navigation with Domain ownership, or report implementation completion |
| Architecture | Layers and responsibilities, business authority, dependencies and data flow, transaction/concurrency/recovery/permission/persistence invariants, Harness and Eval responsibilities | Does not fill unresolved details with pseudo-schemas or describe design modules as implemented services |
| Contracts | Eventually normative business/data/interface boundaries; currently only document structure, responsibilities, ownership, and cross-domain reference directions | Detailed fields, types, enums, transitions, API payloads, database schemas, validation errors, and migrations await the detailed Contract Grill; no fixed file count |
| Acceptance | Observable behavior and evidence needed for completion; positive, negative, concurrency, failure, recovery, and permission cases; meaning of Eval evidence | Verifies settled design without creating business authority; does not report planned tests as passing or invent release policy |
| Development | Documentation-first sequence, source/change discipline, test-first and Eval principles, external research requirements, handoffs, acceptance-evidence maintenance | Does not preselect an unaccepted first implementation Slice, fixed code layout, bootstrap, or CI release thresholds |
| Progress | Actual documentation/implementation/verification state, current task, gaps, blockers, next step, and traceability matrix | Does not own target architecture prose, infer implementation from files or documents, or inherit old completion claims |

The same fact may be explained from product, architecture, and acceptance perspectives, but its authoritative owner must be identified and referenced. Those explanations must not define conflicting rules. Before Contracts are complete, use the settled architecture and explicit “detailed Contract pending” boundaries; do not pretend the normative Contract already exists. Q32's traceability matrix belongs to Progress. Consider an ADR later only when a decision needs its own durable rationale; add no overview category. (Q2, Q5–Q7, Q11, Q18, Q26, Q32)

### 3. Product scope and entry points

- v1 is a single-user, local-first personal job-search workspace. Profile, Preferences, Evidence, Resume, and application records have independent identities. Do not add a unified Candidate Aggregate, CandidateId, tenant layer, or speculative ownership fields.
- Cover Job import/collection, deterministic QuickScreen, user selection, DeepFit, resume improvement, application preparation, external execution, and tracking. This is not a mandatory linear pipeline. Capabilities are independently callable when their own prerequisites hold; Advisor does not require completed DeepFit.
- The five navigation entries are My Resumes, Candidate Knowledge, Job Pool, Job Assistant, and My Applications, corresponding to the accepted labels `我的简历`, `求职资料库`, `岗位池`, `求职助手`, and `我的投递`. DeepFit belongs in Job Pool. Preparation is entered after selecting Jobs and has no top-level navigation. The application entry in My Applications routes to Job Pool. Job Assistant initially exposes only conversational resume optimization.
- Job Pool defaults to a flat list and may provide a Company aggregation read view. That view does not create a Company Aggregate. Acquisition directions, cities, and similar choices come from user Preferences; example roles or locations do not define product support or demonstrated quality scope.
- Shortlisted/PursuitDecision is distinct from screening success, a one-run analysis selection, beginning preparation, or a real application. Bookmark/follow functionality requires separate future design and must not be retained as a v1 requirement solely because old code had it. (Q1, Q6, Q8, Q23–Q24, Q53, S5.1, S5.3, S17.1–S17.4, S37.1)

### 4. Jobs, Preferences, QuickScreen, and collection

- One reliable platform source identity maps to one Job. Semantic content changes for that identity create immutable JobVersions. Cross-platform merging, multi-SourceListing canonicalization, and historical record merging are out of current scope.
- Each Manual creation receives an independent source identity; duplicate URLs may produce only a hint. Without JD, a Job root may support human reporting/tracking but has no formal JobVersion. A valid JD permits its first version. BOSS collection atomically saves the Job and first JobVersion only after complete detail/JD validation; it does not persist incomplete BOSS Jobs.
- Use one global versioned PreferenceSet. Every configured preference is hard; unset dimensions impose no restriction. Invent neither default preferences nor multiple SearchProfiles. Temporary list filters do not change Preferences.
- QuickScreen uses only Job/source metadata, the exact preference version, and screening policy. Only a definite conflict rejects; missing information remains uncertain. Do not restore RequirementSet, Evidence, Resume, or ScreeningProfileSnapshot inputs from Q10's earlier description.
- BOSS collection screens list data first. Rejected candidates receive no detail access, enter no Job dataset, and retain no recoverable rejected title/company/URL/JD content. Passing or uncertain candidates proceed to detail acquisition. CollectionRun retains operational, access-usage, aggregate rejection-reason, and risk audit, without becoming another Job fact store.
- Normal browsing and preference changes operate on the local persistent dataset. Apart from the agreed initial collection following preference setup, subsequent platform refresh requires explicit action. A collection freezes its starting Preferences. New Preferences immediately govern local display and future Runs without rewriting the active Run's rules. Stopping retains committed partial results; it neither recollects automatically nor deletes newly unmatched Jobs.
- Distinguish content capture, last source observation, and direct availability verification. Unchanged content updates observations; semantic change creates a version. Staleness is not closure, absence from search does not prove closure, and closure requires reliable source evidence without deleting history. Missing JD and task readiness are projections, not one universal Job lifecycle. (Q3, Q12–Q14, Q17, Q27, Q44–Q45, Q48–Q50, Q55–Q56, Q110, Q161, S9.1)

### 5. Profile, shared Evidence, and Resume facts

- CandidateProfile owns only identity/contact information, using immutable versions and a root revision. Career facts belong to shared Workspace Evidence; job-search intent belongs to Preferences. Contact information may enter local rendering. Contact details, identity numbers, family information, and raw source documents are model-invisible by default. UI/API visibility and model visibility are separate.
- Evidence is experience-level authority, such as one employment or project record. Preserve original paragraph/list structure rather than forcing persistent atomic Assertions. Fine grounding addresses an exact Evidence version and a location within it; reference granularity does not determine Aggregate granularity. Interpret new-system historical references with their original schema readers, without rewriting old references.
- Each EvidenceItem has exactly one current saved fact version. Older versions serve history and cannot be freely selected for new formal tasks. Restoring old text creates a new temporal version rather than rewinding the pointer. A Baseline freezes the current fact set at that time; it is neither another fact store nor a completeness assertion.
- Upload first creates non-authoritative ResumeDraft/Profile/Evidence proposals. Deterministic Document/Resume parsing restores layout, sections, experiences, and existing structure. LLM processing is optional semantic enhancement, not the default owner of from-scratch ingestion or atomic fact decomposition. Parsing and matching have no merge authority. Human review and reconciliation precede Save, which creates formal versions. Omission of an older experience from imported text does not delete it.
- Every career-fact claim in a formal Resume must be supported or create/correct a fact through user confirmation. Unresolved ambiguity blocks Save. Users may confirm their own facts without third-party proof or a second factual confirmation. Structure, targeting expression, presentation, and career facts have distinct validation responsibilities.
- Formal Resumes select complete current experiences. They may differ in selected experiences, order, and layout, but cannot independently select bullets or retain alternate career body text. Body edits version shared Evidence; presentation-only edits leave the career baseline unchanged. Profile display/privacy choices remain independent and are not expanded by whole-experience selection.
- Evidence Save atomically updates facts, current pointers, baseline, every affected current ResumeVersion, and grounding. Propagating an already-saved fact does not recursively create more Evidence versions. Profile Save similarly propagates atomically to referencing current Resumes while preserving field-display choices; contact changes do not alter the career Evidence baseline. Historical analyses, chats, already-selected Preparation inputs, and execution Snapshots are not rewritten. (Q15, Q19, Q54, Q63–Q64, Q66, Q70–Q75, Q79, Q86, Q96–Q98, Q108, Q113–Q114, Q118–Q119, Q163, S15.1)

### 6. Save, deletion, grounding, and derived work

- Save itself confirms facts. Remove KnowledgeConfirmation, Workspace-wide completeness confirmation, and associated prerequisite Gates. Unsaved My Resumes/Candidate Knowledge edits remain page-local. Normal navigation requires Save/Discard/Cancel; failed Save cannot appear successful. My Resumes ResumeDraft may be lost on crash, with no durable recovery or autosave guarantee.
- GroundingSet is an immutable durable derived asset whose compatibility depends on actual dependencies, not the entire baseline. One ResumeVersion may have multiple exact GroundingSets resolved by compatible inputs, with no mutable active GroundingSet pointer. Version ancestry alone does not prove support. Unrelated fact changes do not invalidate grounding automatically. If a referenced fact is no longer current, rebinding an old Resume to another GroundingSet cannot restore eligibility for new business; a formal version using current facts is required.
- Candidate Fit instead binds the complete exact baseline. Career body changes make the old analysis historical/stale; do not infer fine-grained incremental impact without evaluated support. Profile-only or presentation-only changes must not invalidate Candidate Fit when those changes are outside its inputs.
- Deleting a Resume logically removes it without deleting shared facts or history. The first Resume becomes default; multiple Resumes allow default switching. Deleting the default atomically selects another, and deleting the last Resume is prohibited. Continuing a chat using a removed Resume requires explicit reselection.
- Removing an experience in My Resumes changes only that Resume's selection. Global Delete Evidence originates only in Candidate Knowledge management. Its impact is determined by direct Item inclusion in current Resumes. After confirmation, atomically remove current eligibility and update baseline, directly affected Resumes, grounding, and necessary derivative intents. Do not add sentence/Claim semantic deletion graphs, fall back to old versions, or change historical PDFs or completed applications.
- Empty saved Knowledge/Resume states are permitted. Missing task-required information causes failure before model execution. The per-function prerequisite matrix awaits Contract Grill; do not invent a universal Profile Gate, required experience count, or completeness confirmation.
- Prepare validates, reconciles conflicts, checks revisions, and determines impact and necessary derived work. A short SQLite authority transaction commits formal changes and required durable work intents together. Rendering/previews/indexes/caches execute afterward. No MQ is required, and network/model calls do not belong inside that transaction.
- Derivative generation follows actual preview, export, or Preparation demand; Save does not eagerly render every format. Later demand also persists intent before execution. Compatible work with exact sources/configuration may be reused. Skip obsolete demand before execution; already-running safe computation may finish, but stale output cannot publish as current. Derivative failure affects material readiness without rolling back saved facts. This is not permission to retry remote model/platform calls. (Q66, Q70–Q71, Q73, Q75–Q77, Q87, Q93, Q97, Q100, Q108, Q113–Q114, Q118–Q119, Q147, Q151–Q154, Q165–Q166)

### 7. Requirement dependencies and independent Fits

- RequirementSet is an immutable durable derived asset for an exact JobVersion. Creation and activation are separate; validation may allow automatic activation as the current default, while historical consumers retain exact references. Collection retains JD without initiating parsing.
- Application's shared EnsureRequirementSet reuses compatible results or starts an independent RequirementParse Run. The LLM extracts semantics from the complete exact JD; deterministic code validates. Allow one normal extraction and at most one validation-guided repair. Failure cannot persist an untrusted dependency or produce formal scores from partial requirements.
- Structural validation does not prove zero semantic omission. Preserve uncertainty rather than guessing necessity/logic. Real-JD tests, manual checks, and quality reports remain required, but v1 does not mandate offline human-annotated ParserVersion release certification.
- Candidate Fit, Resume Fit, and job-targeted Advisor consume the exact RequirementSet as their sole Job-requirements input. They do not reread full JD to reinterpret it. No usable Requirement means failure before Fit, not a perfect empty-set score or additional repair allowance.
- Use database-backed single-flight/claim/CAS for one valid producer per exact parse target. The owner pays; waiters reuse the result, and waiter cancellation affects only that wait. Owner cancellation, failure, or unknown outcome does not trigger automatic takeover or reparsing. Explicit Retry first checks compatible durable results.
- DeepFitBatch first freezes known selections, then prepares dependencies, then freezes complete independent analysis requests. No placeholder RequirementSet or silent selected-version upgrade is permitted. Before dispatch, revalidate applicable non-reject QuickScreen, source/dependency compatibility, and permissions. Failed final validation after invocation preserves actual calls/usage/audit without publishing invalid analysis. Each Job offers Candidate Fit and Resume Fit separately. Tasks without compatible saved results default selected; those with compatible results default unselected. Explicit reruns create new immutable results. Each type has its own identity, Run, failure, history, and retry.
- Candidate Fit evaluates current saved admitted Evidence. Resume Fit evaluates only the exact formal Resume and necessary grounding-validation metadata. It cannot supplement unexpressed Candidate facts, another Resume, or Candidate Fit output. The two analyses have no prerequisite dependency, Coverage asset, score gap, or required score ordering.
- Each v1 Full Context Fit performs one structured evaluation and at most one deterministic-validation-guided repair, with no autonomous Evidence Tool loop. Local repair limits remain subject to whole-Run resources. Failure of one task does not roll back the other analysis or a successfully produced independent RequirementSet.
- Preserve the accepted scoped meanings of MATCHED/PARTIAL/MISSING/UNKNOWN. Candidate MISSING means no support found within saved admitted Knowledge. Resume MISSING means no supporting expression found after complete inspection of that exact Resume's admitted content. Privacy exclusion, truncation, unverifiable results, or incomplete inspection remain UNKNOWN, not proof of real-world incapability.
- Completeness checks apply to the assessment-producing Frame: all necessary Requirements, inclusion of admitted content, reference resolution, and output validation. FULL_CONTEXT alone does not prove MISSING. Baseline, eligibility, and actual model visibility remain separate boundaries.
- Different targets may run concurrently; each target permits only one effective active analysis, enforced by the backend too. Display the latest successful compatible result. A failed rerun preserves an older compatible success; stale output cannot become current. Do not use latest-user-intent arbitration between concurrent same-target Runs.
- Models produce assessments; versioned deterministic ScorePolicy derives scores. Minor matches cannot offset critical hard gaps, UNKNOWN cannot be mapped mechanically to a fixed low score, and scores are ranking/display summaries only. Preserve original analyses and original scores/unavailable-score results. Explicit rescoring is a derived projection, not new semantic analysis; comparisons use a common policy version, and missing dimensions required by a new policy cannot be guessed. Valid analysis may have no comparable total score: do not record zero, inherit an old score, or include it in ordinary numeric ranking. Weights, thresholds, and representation remain deferred. (Q10, Q14, Q35, Q40, Q46, Q51, Q58–Q59, Q72, Q76, Q82–Q83, Q110–Q117, Q121, Q142, Q168, Q171, S22.1)

### 8. Advisor, Session, and formal changes

- One ResumeAdvisor Skill serves ordinary and Preparation entry through a unified ChatSession. Each Preparation entry starts a new chat with explicit references/intent, without a targeted-Session compatibility mechanism or second Agent. General mode does not infer a concrete Job from a job-family request.
- Advisor may reuse compatible current Candidate/Resume Fit results, but neither is a prerequisite. Per-Requirement comparisons are transient optimization hints, not durable CoverageAnalysis. General resume optimization requires no specific Job/RequirementSet; job-targeted work uses shared Ensure for dependencies.
- Discussion/read context follows the established precedence: current explicit request, Session's explicitly adopted object, originating Preparation, then Workspace default. Default changes do not silently switch existing discussion. If no formal Resume exists, preflight provides import/create guidance before a Run. Ad hoc chat-file optimization is outside v1.
- **Formal apply has a separate target rule:** use the target explicitly named in the current instruction, otherwise Workspace default. Discussion-context precedence is not apply authorization, and no extra suggestion-source Resume is inferred. Read the actual target's exact version and build its own before/after ChangeProposal. Do not transplant a patch by swapping IDs or copy unrequested experiences.
- Newly stated Session facts can immediately support discussion and Suggestions with verifiable SessionContextRef/UserTurnRef provenance. They are not Evidence and do not automatically become Memory or formal Fit inputs. Ordinary discussion does not repeatedly prompt Save; the model cannot invent Session sources or confirmation.
- Advisor has no ResumeDraft, persistent working draft, or draft export path. ChangeProposal is a non-editable operation preview, not independently exportable/applicable material. It shows target/version/default selection, concrete changes, shared facts, and impact on other current Resumes. One confirmation authorizes only that complete change; target, patch, or revision changes require a new preview.
- Proposal generation/display ends its Turn/Run. Application later validates and executes the exact confirmed operation without asking a model to reinterpret consent. The old Run does not wait for a person, and there is no second draft Save. Subsequent conversation uses new bounded execution.
- A Session has at most one active foreground Turn. New input waits or explicitly stops the preceding Turn. Different Sessions and legitimate auxiliary/dependency/background execution may run concurrently. Waiting for independent RequirementParse retains the same active foreground Turn but releases model execution capacity, preserves overall deadline/cancel, and uses neither model polling nor automatic producer takeover.
- Application's committed mutation result is not rolled back by a later reply failure. UI distinguishes “saved” from “reply unfinished.” The same confirmed Proposal recognizes its committed result idempotently without duplicate versions. Streamed “saved” wording is not commit evidence.
- Session deletion atomically arbitrates pending Proposal confirmation/invalidation and cancels active foreground work. Old IDs/restored pages cannot execute unconfirmed actions again. Already-committed formal facts, results, and history remain.
- Return to Preparation is a separate explicit Resume-only CAS adoption, preserving Greeting and unrelated concurrent changes. Conflict requires loading current state and explicit readoption; it does not authorize external execution. (Q24, Q41, Q47, Q52, Q85, Q88–Q89, Q91, Q93–Q94, Q96, Q108, Q128, Q133–Q134, Q138–Q139, Q143–Q144, Q146, Q148–Q149, Q155–Q156, Q158–Q159, Q167, S17.3)

### 9. Preparation, materials, external execution, and tracking

- Preparation is an editable Job/channel root protected by revision/CAS, without immutable history for every edit. It displays/selects formally rendered Resumes and does not edit Resume body text. Reentry defaults to resuming unfinished preparation, preserving selections and manual Greeting. Repeated requests do not duplicate creation; multiple candidates require user choice. Explicit new preparation or a subsequent real application starts a separate chain.
- Greeting belongs to Preparation, with one fixed generic default and manual editing. It has no Job/company/Resume/Memory personalization, model call, independent Aggregate, template library, or version system.
- Required rendered material must actually be viewable before confirmation. MaterialApproval binds the displayed frozen artifact/hash/sources and actual Greeting, not merely a Resume name or version. Greeting edits require reconfirmation. Changing materials requires compatibility validation; equal hashes cannot bypass current fact eligibility.
- An immutable ExecutionSnapshot freezes exact intended inputs but grants no execution authority. ExecutionApproval is scoped, expiring, and single-use, consumable by at most one Attempt. MaterialApproval cannot replace it.
- Batch application is interaction and scheduling only. Each Job has independent Preparation, Snapshot, Approval, Attempt, and optional real application record. Partial continuation requires new narrower authorization. Unknown external outcomes produce no success event and cannot retry automatically. Undispatched members cannot be marked failed or applied.
- ExecutionEvent records technical actions/observations. ApplicationEvent requires a real business fact established by reliable channel read-back or explicit human report. Clicking Send is not proof of application, and manual reporting must not fabricate Executor history.
- ApplicationRecord represents one real Job/channel/account application attempt; reapplication creates a new record. Events are append-only, deduplicated, and distinguish occurrence from observation. Corrections/retractions use new events. Progress is a versioned-policy projection, not a second writable status authority. Interviews initially use structured ApplicationEvents, without a new Interview Aggregate.
- Necessary Executor live identity/availability checks cannot silently refresh JobVersion, generate RequirementSet, replace Snapshot, or add LLM Job analysis. Clear mismatch/closure stops execution; explicit refresh/repreparation is a separate workflow. (Q7, Q16, Q21, Q25, Q30–Q31, Q36–Q37, Q42, Q77, Q91, Q146, Q150, Q157, Q162, Q164)

### 10. Platform safety, source research, and adapters

- Before every platform access, Collector, Browser Executor, and any future implemented Monitor share persistent PlatformAccessSafety scoped by platform/account. Capacity, risk, and action admission are shared; workflows, budgets, approvals, and recovery ownership are not merged.
- Ordinary page/selector/browser failure is not automatically account risk. Predictable capacity may recover by policy; strong risk requires user handling and explicit restoration. Do not bypass it through cooldown-only recovery, account/tab switching, or increased concurrency.
- BossHunter, boss-zhipin-scraper, and open-source resume-optimization projects are research/implementation inputs only. Validate third-party sources into adapter DTOs; admit canonical data only for concrete consumers. Third-party data availability does not imply model visibility.
- Before detailed related Contracts/channel-verification design, research tasks must pin source commits, check licenses and maintenance, and map source→adapter→canonical. Access counts, delays, cooldowns, and third-party behavior in Grill records are neither official limits nor frozen defaults. This authoring work does not add unauthorized product/architecture decisions or claim that research has already been completed. (Q3, Q27, Q31, Q36, Q49, Q126, Q160, Q164, S7.1)

### 11. Harness, Tools, and model-call ownership

- Use one shared Harness with separate static Skill Contracts for RequirementParse, CandidateJobFit, ResumeJobFit, and ResumeAdvisor. MemoryExtraction is an independent headless Skill. One Run serves one bounded semantic task; a Job-specific task binds one exact Job. Independent Fits cannot share one semantic Run.
- Application owns dependency preparation, batch orchestration, complete-input freezing, business validation, and result persistence. Harness owns execution, Context, permission enforcement, budget, cancellation, recovery, and audit; it has no fact-write authority.
- ToolRegistry registration is not authorization. Effective actions are jointly constrained by Registry, Skill allowlist, Context policy, and current runtime permission. Expose typed scoped Business Actions only, without generic Shell, SQL, file, HTTP, or model-autonomous browser access.
- Before calls, validate action, arguments, objects, scope, Run authority, and required approval. Readmit results for privacy/scope before they enter a Frame. Model parameters, JD, webpages, ToolResults, or instructions inside references cannot expand permissions. Tools must not secretly scan chat to infer intent.
- ResumeAdvisor itself performs optimization; do not add a duplicate suggest_improvement Tool. The accepted job.requirements.read action is a pure read. Missing dependencies go to Application EnsureRequirementSet, without hidden model calls, nested Runs, or asset creation inside read. Other example names do not freeze a complete catalog.
- AgentRunRuntime owns Run lifecycle/ownership. ModelInvocationRuntime is the unique execution boundary for every business Provider call, including primary work, repair, compaction, rescue, and MemoryExtraction. ModelGateway only adapts transport; ToolInvocationRuntime owns Tool admission and replay.
- SDK/Gateway cannot transparently retry or fall back to another model/Provider. Every permitted new request is counted, budget-admitted, durably dispatched, and audited. An independent Eval Judge is a separately declared Eval execution responsibility, not an exception allowing uncounted business calls. (Q47, Q120–Q122, Q126–Q127, Q128, Q135, Q138, Q140, Q142–Q144, Q176, S7.1, S17.4, S22.1)

### 12. Context exactness, capacity, and compaction

- Advisor primarily uses LAZY_TOOL: initial control, current/recent Session, admitted Recall, and Tool definitions. Preparation references do not mean business bodies were injected. RequirementParse and both Fits use Application-frozen EAGER_EXACT inputs; v1 Fit has no autonomous Evidence Tool loop.
- ContextPackage is an immutable initial scope/policy/input/capability manifest. Every ModelInvocation binds its own immutable ContextFrame describing what was actually sent. Later reads or exact versions returned by authorized writes pass admission and append runtime inputs, without rewriting prior Package/Frames.
- Lazy resolution pins the exact version on first read; later reads do not follow latest. This task's authorized write may explicitly append committed versions, but unrelated concurrent changes cannot silently upgrade inputs. Q158's actual Proposal workflow does not keep or revive its generating Run for confirmation.
- Capacity checks use actual serialized input plus control/Tool/output reserves and margin. If complete admitted v1 input cannot fit, fail explicitly before invocation. Do not trim facts, switch models automatically, or enable unimplemented RAG. An independently feasible Fit remains unaffected.
- Context Engineering is separate from Memory. First classify protected exact and compactable content, then externalize ToolResults, trim history windows, and perform deterministic micro-compaction. Only if still insufficient use a bounded semantic checkpoint. Trigger and target are distinct; numeric values remain deferred.
- Normal semantic compaction is an auxiliary Invocation in the current Run, sharing budget/deadline/fencing/recovery, at most once per entire Run. Reactive rescue after explicit Provider size rejection is also at most once. All local allowances remain subject to total budget; loop progression does not reset them. Timeout/unknown outcome cannot be relabeled as size rejection.
- Validate and durably publish a checkpoint before using it in a new Frame. Failure retains former recoverable sources. Summaries cannot replace protected inputs or delete complete Session history. An old LAZY_TOOL result may be externalized and newly read at its exact version, without pretending to recreate the old ToolResult.
- Direct Long-term Memory blocks are excluded from checkpoints; Recall is dynamic per Frame. v1 does not promise removal of indirect influence in actual assistant history.
- Initial exclusions retain UNKNOWN semantics. After freeze, revocation affecting protected EAGER_EXACT input ends that task; do not shrink its scope and continue, let repair/Frames/Tools consume revoked content, or publish a new current Analysis. New scope requires a new task; already-transmitted content cannot be retracted. (Q19, Q72, Q80–Q83, Q94, Q121, Q123, Q132, Q134–Q136, Q138–Q139, Q143, Q172, S24.1)

### 13. Budget, Recovery, and Storage

- One shared Budget Runtime serves different owners: foreground operations and independent BackgroundMemoryBudget. Runs also have local call/token/step/deadline limits. Each charged/limited Invocation atomically checks and reserves, then settles actual usage. Both settled usage and outstanding exposure reduce availability. Reusing RequirementSet does not duplicate parsing charges.
- Budget, Provider headroom, runtime capacity, and platform safety are distinct resources. Background extraction yields to foreground work; combining several Turns does not charge the last Turn. Current-Run compaction charges that Run. Amounts, thresholds, allocation, overrun, and unknown-usage reconciliation remain later work.
- Commit durable dispatch intent before remote calls. Persist complete responses before local parse/validation. Intent without a complete durable response is outcome-unknown, even if the request might not actually have been sent; do not silently replay it. A durable response permits local processing recovery without another model call.
- Run ownership/generation fencing rejects late writes from cancelled, timed-out, or former owners. Startup reconciliation resumes safe work at durable boundaries or ends unknown tasks and releases target slots. Slot release proves neither remote cessation nor zero cost. Explicit Retry creates a new Run with fresh admission while retaining old uncertain exposure.
- LangGraph checkpoints restore workflow state, not remote-action receipts. Concrete action semantics must establish Tool replay safety; names or generic frameworks cannot authorize it. Recover committed canonical results idempotently without duplicate assets.
- Separate Business Durable Assets, protected Recovery Payload, lightweight Audit Metadata, and minimal Operational Logs/Telemetry. This is not a requirement for four databases. Pin exact payload needed by active recovery dependencies; terminal historical sources may expire under independent retention, retaining honest availability/hash/lineage. Do not reconstruct current assets and pretend they are old Frames.
- Ordinary logs must not contain HTTP secrets or complete Resume/Evidence/prompt/response payloads. Payload or chat cleanup does not erase business history. Persistence does not grant model admission; historical readability does not grant current business eligibility.
- Streaming deltas are transient presentation, not formal Turns, Suggestions, MemoryExtraction sources, or commit evidence. They need not persist and cannot be stitched into Retry output. Frontend disconnection does not automatically cancel a healthy backend; reconnect may read its complete final result. (Q83, Q116, Q122–Q125, Q130, Q132, Q135–Q136, Q140–Q142, Q147, Q156, Q165, S24.2)

### 14. Collaboration Memory

- Distinguish Business Authority, durable Session, Long-term Memory, and derived Memory retrieval. Context Engineering is not a Memory layer. Memory admits only collaboration preferences, feedback, working style, and reusable collaboration learning—not career USER_FACT, job-search Preferences, or application facts.
- Fact authority, action permission, and interaction style are three separate rules. Current explicit instructions can override style for this interaction without authorizing fact changes or approval bypass. One-off requests remain Session-local rather than becoming durable preferences automatically.
- Auto Learning, Recall, and explicit View/Add/Edit/Delete/Clear All are independent. Learning off does not stop Recall. Recall off excludes Memory from the next Frame without deleting entries. Management uses deterministic validation without extraction. Enabling does not default to backfilling disabled-period or historical chats.
- Completed durable user-facing Turns create durable pending source work. Coalescing/delayed triggers schedule independent background Extraction; do not depend on Session-ended events, unconditional per-Turn calls, or process timers as authority. Extraction proposes; deterministic admission decides. Automatic persistence requires traceable explicit durable user expression/correction. Assistant inference, repeated behavior, or summaries alone are insufficient.
- Parse and Fits read no Long-term Memory. Advisor's default admission covers collaboration preferences, feedback, and working style; storage support for reusable learning does not implicitly grant access to that category. Future General Assistant/interview Skill examples do not expand v1.
- Forgetting prevents entry use in new Context and derived indexes and prevents automatic resurrection from old sources. Late extraction cannot overwrite newer manual management. A genuinely later durable instruction may be admitted; manual editing is not a permanent lock.
- Failed/unknown extraction batches remain separate from newer sources. They cannot block later work, falsely advance a success cursor, or silently enter a new batch. Only explicit Retry processes old failed ranges. Undispatched budget waiting remains pending.
- Deleting a source Session prevents new extraction and late candidate publication, with checks at dispatch/publication. Previously accepted Memory has an independent lifecycle. Deletion cannot retract sent content or erase real costs/recovery audit. (Q52, Q127–Q131, Q133, Q137, Q139, Q145, Q169–Q170)

### 15. Formal documentation of Eval and observability

- Architecture must state the selected LangGraph execution and self-hosted Langfuse direction. Langfuse owns generic Dataset/Experiment/Evaluator/Score/comparison/observability facilities. JobHunter retains thin task adapters, real Application/Domain/Repository/Harness paths, and domain-aware checks. Do not build another generic Eval platform or test-only Agent.
- Acceptance must explain what outcome, trajectory, Tool, Context, grounding, authorization/safety, reliability, and efficiency evidence proves. Transactions, permissions, CAS, budget, recovery, and fencing primarily use deterministic tests and controlled fault injection. Semantic quality uses appropriate human review/calibrated judges; resolving a reference alone does not prove semantic support.
- Reconstruct each Trial from an isolated immutable fixture. Real test-DB commits are allowed; live Workspace mutation and real recruiting-platform side effects are not. Freeze Dataset, business fixture, Scenario events/expectations, and Skill/Prompt/Context/Model/Evaluator/Rubric/Runner configuration. Missing inputs or hash mismatches are explicitly non-reproducible, with no latest fallback.
- Separate development and holdout datasets by Skill, retaining positive/negative/boundary/regression case meanings without freezing example names or counts. Disclose holdout contamination if used for targeted tuning. Report recorded-replay evidence of deterministic mechanisms separately from live-model behavioral evidence. Exact reproducible inputs do not promise identical remote-model outputs. Pass@1 represents the single-attempt experience; repeated Trials measure stability, not best-of-N selection. Trials, in-Run repair, and user Retry are distinct.
- Prefer N+1 for localized conversational failures: freeze prior messages and coherent business/runtime boundary state, then execute only the next input. Do not replay historical model calls/Tools/mutations or claim to prove the first N Turns. Cross-Turn/Proposal/confirmation/concurrency/revocation scenarios use a thin deterministic Scenario Driver, fixed authored inputs, and logical checkpoints, without sleeps or a generative User Simulator.
- The Driver may confirm only an actually produced, uniquely matching Proposal through the formal Application interface. It cannot fill in DB success, fabricate consent, or help the Agent satisfy missing prerequisites. Q158's generating-Run completion boundary applies unchanged in Eval.
- Separate task outcomes from each check's conclusion. Expected rejection may be correct; violations, incomplete evidence, and evaluator errors remain distinct. Judge failure does not erase valid deterministic findings. Do not drop failed/unassessable samples or treat Q168's unavailable score as zero.
- Average quality cannot compensate for Hard Gates. Report quality, stability, cost, and latency separately; judge absolute target attainment and relative regression independently. Q117's ParserVersion certification remains deferred. Do not freeze a release ladder, default enablement, Trial counts, thresholds, or repository-wide CI release policy.
- Judges use independent Eval execution/budget/model/rubric configuration and assess existing outcomes. They do not write Domain state, change original Run success/failure, or add judge cost to business performance. Do not claim that Langfuse judges automatically inherit business Runtime reservation/fencing guarantees.
- Langfuse provides derived observations. Local canonical state determines commits, Invocation completion, settlement, and recovery. Upload failure cannot roll back business or replay calls. Callback and explicit SDK paths both redact before export, correlate canonical IDs including auxiliary calls, and avoid double-counting. Do not add a generic Telemetry Port.
- Missing necessary evidence is incomplete evaluation. If sufficient local canonical evidence exists, a missing span alone does not automatically fail the check. Self-hosting does not authorize copying full sensitive payloads. Evaluators receive task-scoped evidence; Resume Fit judges likewise cannot supplement from Candidate Knowledge.
- Separate Agent inputs, evaluation references, and Scenario control. Future Turns, expected answers, rubrics, and previous Trial scores cannot reach the Agent under test. Judge rubrics are control; candidate output and Tool text are evidence and cannot change scoring rules.
- Allow multiple correct results satisfying semantic, grounding, and behavioral constraints, without prescribing unique wording or Tool order. Exact IDs/versions/authorization remain strict. Declare Skill-only versus composed-workflow scope, dependency failures, unexecuted stages, and costs separately; make no false end-to-end quality claims.
- Retain reviewed minimal sanitized/synthetic regression fixtures that preserve the failure mechanism, independently of original sensitive-payload retention. If executable fixtures cannot be retained, disclose the coverage gap. New evaluators may reassess the same Trial's actual retained results/post-state without rerunning the Agent; missing evidence cannot trigger silent fresh execution.
- Ordinary comparable Advisor Trials freeze isolated Memory/Recall and control unscripted background learning. Memory-specific Scenarios explicitly drive actual learning with separate outcomes/costs. Learning-disabled experiments cannot claim Extraction coverage. Verify platform SDK/deployment capabilities against actual selected versions later; existing research appendices do not prove deployment. (S35.1, Q117, Q173–Q187, S37.1)

### 16. Contracts: structure, responsibilities, and boundaries only

Organize candidate document families by actual authority and consumption relationships. This is not a final file list or a requirement for one file per family:

| Candidate responsibility family | Accepted boundaries to carry forward | Cross-family references |
| --- | --- | --- |
| Shared identity/version/reference/concurrency/admission | Roots versus versions, exact references, CAS, idempotency, provenance, privacy, compatibility | Referenced by other families without conflicting copies |
| Workspace/Profile/Preferences | Single-user scope, default Resume, identity/contact and search-preference authority | Resume references Profile; collection/QuickScreen reference Preferences |
| Evidence/import/baseline | Experience facts, proposals and Save, current versions, deletion, snapshots | Resume/Candidate Fit reference exact facts; import adapters have no extra authority |
| Resume/grounding/Proposal | Formal presentation, atomic synchronization, conversational sources, target patch, confirmation, mutation result | References facts; supplies formal material sources; coordinates Session invalidation |
| Jobs/collection/platform safety | Source identity, completeness, versions, filtering, Runs, shared access risk | Requirements reference JobVersion; execution shares platform safety |
| Requirements/Fits/scoring/batch | Shared dependencies, independent analyses, exact scope, score availability, results versus orchestration | References Job, Evidence/Resume, and Harness execution; creates no facts |
| Materials/Preparation/Execution/Application | Rendering, readiness, two approvals, Snapshot, Attempt, real events, progress | References formal material and channel verification; technical execution does not directly set business progress |
| Harness/Skill/Invocation/Tools | Bounded tasks, permissions, unique business-model execution boundary, replay, fencing | Acts through Application Ports; has no Domain authority |
| Context/Session/Memory | Sources versus actual Frames, acquisition, compaction, independent Memory controls | Uses exact business references without changing facts or authorization |
| Budget/Recovery/Storage/derived work | Owners/reservations, durable boundaries, four-layer retention, safe derivative intent | Shares Run/Application boundaries without extending safe replay to external effects |
| Eval/observability | Fixture/scenario/evidence/judge separation, derived observations | References business/runtime norms without becoming production authority |

At this stage record only what each family owns, excludes, references, and leaves for Contract Grill. Even attributes named in Grill records must not become full types, enums, or payloads here. Later Contract Grill determines fields, validation errors, migration/new-system evolution details, and related specifics. Listing migration as a pending detail category does not introduce a legacy-migration requirement. (Q2–Q5, Q11, Q26, S24.2, S29.2, S37.1)

### 17. Development, acceptance, and actual progress

- Development documentation carries forward accepted test-first/TDD, deterministic boundary testing, real-path Eval, Slice acceptance, and traceability maintenance. Do not assume test commands, code layout, stack versions, or the first Slice exist or have been chosen. Explicit LangGraph, self-hosted Langfuse, and relevant SQLite transaction decisions may be described as targets; do not infer the whole application stack.
- Plan Q32's future unified check entry for unique IDs, valid references, and required mappings without claiming that a script exists, ran, or passed. Repository-wide CI/release policy left open by Q175 remains deferred; mechanical document checks do not replace it.
- Formal Contract requirements will later receive stable IDs. The progress matrix links implementation, tests/Eval, evidence, and actual status. Before Contracts are complete, retain Grill Q-ID design traceability and “detailed Contract pending,” without inventing published Contract IDs, implementation paths, or test evidence.
- Product implementation and tests have not started at the baseline. Architecture Grill and record handoff are complete. Completing this file means only that authoring guidance exists. Subsequent document completion, review approval, Contract completion, and implemented product capabilities must be recorded separately.
- Planned/Deferred describe targets and supported deferrals. Partial/Implemented require actual implementation and acceptance evidence, not extensive prose, file existence, or old-system evidence. (Q4, Q22, Q26–Q27, Q32, Q117, Q175, S37.1, S38.1)

## Testing Decisions

### 1. Verification subjects, prior art, and evidence standards

There is no reusable test suite, implementation seam, or execution result in this repository. Reusable verification inputs are the original Grill Q-IDs, module Verification implications, Eval evidence boundaries, and Q26/Q32 traceability principles. These are standards to implement later, not proof of passing tests.

This step verifies whether this file can guide subsequent authoring. Later tasks use the same two seams against actual formal documents. Both inspect externally readable document content and source semantics, not editor internals. Keyword matches, word counts, Q-ID occurrence counts, or file existence cannot substitute for semantic correctness. Mechanical checks can find missing references, invalid anchors, and duplicate IDs; interpretation still requires clause-level semantic review. Verify the opening English-language rule as an explicit authoring requirement without attributing it to an invented Grill Q-ID.

### 2. Decision-to-Document Traceability Seam

**Direction: effective Grill decisions → formal documents, with reverse checks that document rules have valid sources.**

Track each effective clause's original Q/S, surviving meaning, controlling Q/S, scoped supersession, primary document/section, other consuming/reference locations, acceptance counterpart, and pending/exclusion reason. Sharing a Q-ID across documents does not authorize multiple competing specifications. Split a record into surviving and replaced clauses as needed; a single record-level checkmark must not conceal internal contradictions.

Verification method:

1. Start with the Further Notes source baseline and coverage index. Reread original records and relevant detailed modules to determine each effective meaning; split earlier records into clauses where necessary.
2. Locate actual document sections/rules/acceptance items. Classify each as written, referenced, awaiting detailed Contract, explicit non-goal, or historical maintenance only; explain every gap.
3. Reverse-check added rules against effective design sources or clearly identified authoring arrangements. Examples, research candidates, and unaccepted recommendations cannot become normative rules. The language/authority rule comes from the user's later explicit instruction.
4. Link acceptance to expected proof and progress to actual evidence separately. Do not report planned acceptance as passed or derive implementation from a pending Contract.

**Pass conditions:** every existing Q/S and effective detailed-module content has a disposition; all product/architecture rules are traceable; partial supersession identifies controlling decisions; no REJECTED/SUPERSEDED mechanism is restored; every deferral/exclusion has a reason and appropriate home. Mechanical Q-ID coverage is necessary but insufficient.

This spec's coverage index is an entry point for later authoring, not a completed formal Traceability Matrix. Preserve original Q-IDs when adding actual destinations; do not renumber history.

### 3. Cross-Document Semantic Consistency Seam

**Direction: formal documents ↔ formal documents.** Use shared design facts and Q-IDs from the preceding seam to connect all occurrences of a topic, then compare their meanings.

Inspect these document boundaries:

| Comparison | Pass condition |
| --- | --- |
| Product ↔ Architecture | Entry points, independent capabilities, data prerequisites, permissions, confirmation, and failure behavior agree; navigation creates no Aggregate |
| Architecture ↔ Contract planning/future Contracts | Fact ownership, dependencies, input scope, and transactions agree; planning does not pretend to be a settled schema; completed Contracts trigger review of the five main documents |
| Product/Architecture ↔ Acceptance | Tests prove final behavior and prohibited boundaries, not old mechanisms; Eval does not redefine business success |
| Architecture/Acceptance ↔ Development | Testing/implementation order matches ownership; no hidden retries, test-only Agent, or undecided release threshold |
| All target documents ↔ Progress | Target, pending, authored, reviewed, implemented, and verified states remain distinct; no false completion claims |
| Reference destinations | Root/version, historical/current, authority/derived, eligibility/readability, and state/projection/event meanings agree; examples elsewhere do not become normative |

**Pass conditions:** the same design fact has no conflicting authorities; synonymous and distinct terms are clear; references identify applicable sources; architecture boundaries agree with acceptance expectations; pending details are consistently marked rather than silently decided in one document. Label nonexistent future paths as planned, rather than fabricating available normative references. Formal documentation is in English and follows the declared English authority; the preserved Chinese authoring reference does not become a competing authority.

Report each seam separately. Correct references do not guarantee consistent semantics; mutually consistent documents can still misread Grill together. Passing one seam does not offset failure of the other.

### 4. Required semantic regression examples

This is a minimum review set, not a substitute for reading all records. Check affirmative statements and behavior semantics. Historical terms may appear in explanations of history, prohibition, or supersession; a simple banned-word grep is inappropriate.

| Obsolete meaning at risk of restoration | Required final meaning | Controlling sources |
| --- | --- | --- |
| QuickScreen requires RequirementSet or a Candidate-capability snapshot | Metadata plus exact Preferences/policy; collection does not parse Requirements | Q56, Q110 supersede earlier Q8/Q10 input assumptions |
| Manual and BOSS both persist incomplete JobVersions | Manual may have a root only; BOSS creates root and first version atomically after completeness; JobVersion meaning is shared | Q44, Q48–Q49, S9.1 correct Q17 |
| Upload immediately creates a formal Resume | Draft first; complete grounding and atomic Save precede formal version | Q70–Q74 supersede Q63 import clauses |
| Confirmation wording in an older ACCEPTED record still creates a completeness Gate | Save confirms facts; no KnowledgeConfirmation | Q113 supersedes affected Q66/Q72/Q73/Q85/Q97/Q108–Q112 clauses |
| Resumes own private facts, freely select historical Evidence, or independently select bullets | Shared current experiences, temporal versions, whole-experience selection | Q63, Q108, Q163 |
| Fact changes require manual Resume refresh or only a replacement GroundingSet | Atomically propagate all affected current Resumes; preserve history; rebinding cannot restore new-use eligibility for old facts | Q108, Q114, Q118–Q119 supersede affected Q64/Q70/Q77/Q87 clauses |
| Advisor persists a working draft for later export/apply | Discussion, Suggestion, and target-specific Proposal; one confirmation commits formally | Q108, Q146, Q148–Q149 supersede affected Q41/Q85/Q94/Q138 clauses |
| Apply implicitly uses chat/Preparation Resume selection or inferred source Resume | Current instruction's target, otherwise default; read that target and build its own patch | Q146, Q149 scoped override of Q93 |
| Explicit apply skips concrete preview; old Run waits for confirmation and continues | Preview target/patch/shared impact, obtain one confirmation; generating Run has already ended | Q146, Q148, Q158 scoped refinements of Q133/Q134 |
| Removing an experience from one Resume deletes the shared fact | My Resumes removes selection; Candidate Knowledge performs global deletion with direct-membership propagation | Q151, Q153 |
| Page Draft crash checkpoints or Advisor draft recovery | Unsaved page state may be lost; pending Proposal persists but cannot be confirmed after Session deletion | Q146, Q166–Q167 |
| One DeepFit Run evaluates two axes/Coverage/score gaps | Independent Skills/Runs/Analyses; scoped four-state semantics; no required score ordering | Q112, Q115, S22.1 |
| Empty Requirements yield a perfect score; no total score means failure/zero | No usable target fails before Fit; valid assessments may lack a total score | Q168, Q171 |
| Latest overlapping analysis intent arbitrates current result | Serialize each target; retain latest successful compatible result and older success after failure | Q116 |
| Full Context overflow automatically triggers RAG/summarization/model switch | Explicit v1 pre-invocation failure; Agentic RAG is post-v1 | Q121, Q123, Q132, S24.1 |
| Stored Context sources are all injected by default or follow latest | Advisor lazy pinning; headless eager exact; each Frame records actual visibility | Q83, Q94, Q139, Q143 |
| Missing dependencies cause hidden parsing inside read | Pure read reports missing dependency; Application owns separate Ensure and owner cost | Q142, Q144, Q159 |
| Memory owns compaction and one switch controls both learning and reads | Separate Context; independent Auto Learning/Recall/management | Q132, Q139 partially supersede Q127/Q137 |
| Failed Memory ranges automatically join new batches or deleted sources still publish | Explicit retry for old failures without blocking new ranges; deleted sources cannot publish new learning | Q169–Q170 |
| Intent without response may replay automatically; SDK hides retries | Outcome unknown, explicit new Run; all business calls pass through Runtime | Q122, Q135, Q140 |
| Each loop renews repair/compaction/rescue allowances | Accepted local ceilings and Run totals jointly constrain dispatch; allowances do not reset | Q121, Q135 |
| Every format is eagerly rendered; safe derivative recovery authorizes platform/model replay | Persist demand-driven intent, skip obsolete work, keep safe derivatives separate from unknown remote retries | Q147, Q152, Q165 |
| Post-freeze revocation removes input and continues the same Fit | End affected frozen task; new scope requires new task | Q172 |
| Material confirmation of a ResumeVersion is execution authorization | Confirm actually viewed frozen artifact/Greeting; ExecutionApproval is separate | Q30, Q150, Q157 |
| Strong risks recover by cooldown; execution checks silently refresh JD | Shared persistent safety with explicit user restoration; checks and refresh are separate | Q160, Q164 |
| Langfuse spans or judges determine business success | Local canonical results; independent judges with scoped evidence and costs | Q174, Q176, Q184 |
| Unique golden Eval text, replayed N+1 history, whole Dataset in Context | Valid semantic alternatives, coherent boundary with next-turn-only execution, isolated references/control | Q178, Q180, Q183, Q185 |
| 1/3/5 Trials or a universal release gate are settled requirements | Counts, thresholds, default enablement, and CI release policy remain later work; Q117 is unchanged | Q175 supersedes earlier Eval proposals |
| Old migration order/completion claims constrain the new repository | Review five main documents before Contract Grill/Contracts/development; establish actual status anew | Q4, Q22, S37.1, S38.1 |

### 5. This deliverable versus future acceptance

Completion criteria for this deliverable: all seven default template sections exist; both confirmed seams retain their exact names and individual pass conditions; six documentation categories have responsibilities and transferable tasks; all 179 existing Q/S records are locatable in the coverage index; partial supersession and exclusions remain traceable; no detailed Contract definitions or invented implementation claims appear. Create only the requested local English edition, preserve the existing Chinese file and all nine source records, and state the English-only formal-authoring rule at the beginning.

Each subsequent document delivery must report actual results for both seams, changed locations, genuine unresolved issues, and the next step. The final five-document review must pass both seams before detailed Contract Grill. Here, “pass” proves document consistency only, not product implementation, tests, Eval deployment, or release readiness. After Contracts are complete, recheck affected main documents, acceptance, and progress.

## Out of Scope

- Authoring the six formal document categories in this step; starting Contract Grill; implementing code/tests/Eval services; deployment; recruiting-site access or external applications.
- Reopening Architecture Grill, adopting unaccepted Q188–Q192 recommendations, or selecting the first Slice, complete stack, code layout, or bootstrap for the user.
- Prematurely defining Contract fields, types, enums, detailed transitions, API payloads, database schemas, validation errors, or migrations; promoting inventory rows, conceptual attributes, example numbers, or code layouts into normative definitions.
- Restoring REJECTED/SUPERSEDED mechanisms, including historical Overlay/selectable old facts, KnowledgeConfirmation, ResumeCoverage, Advisor working drafts, old targeted Sessions, ScreeningProfileSnapshot, persistent Assertion authority, or per-version withdrawal UI.
- Expanding v1 into cross-platform Job merge, new Company/Candidate/Interview Aggregates, multi-tenancy, multiple SearchProfiles, bookmark UI, General Assistant/interview Skills, personalized Greeting, dynamic plugin markets, generic Shell/SQL/HTTP Tools, complete Candidate Agentic RAG, complex Memory graphs, or all-history scans.
- Turning safety constraints for a future platform Monitor into a mandatory Monitor feature; treating platform access numbers as official rules or research notes as verified capabilities of current dependencies.
- Mandatory legacy compatibility, old-database migration, dual-running, or mapped successors for old tests/Eval fixtures. New-system historical interpretability remains required and must not be confused with migration of the old system.
- Freezing Eval thresholds, Trial counts, default enablement, or release/CI policy; restoring mandatory human-annotated ParserVersion certification.
- Publishing a GitHub Issue, calling an external issue tracker, adding a ready-for-agent label, or modifying/cleaning original Grill records.
- Producing Chinese editions of subsequent formal documents at this stage or replacing the preserved Chinese authoring reference.

## Further Notes

### A. Output and source baseline

The authoritative authoring-spec path is `.scratch/document-authoring-spec.en.md`. Preserve `.scratch/document-authoring-spec.md` unchanged as the Chinese reference. This English edition carries forward the complete authoring plan and adds the user's explicit language/authority instruction; it is not a new formal-document category. Subsequent tasks must use this English edition as their governing authoring spec. The seven default to-spec second-level sections remain. User Stories are not expanded because the user explicitly scoped the work to the documentation system. The two verification seams have already been confirmed; do not request the same confirmation again.

The local Grill source snapshot is dated 2026-09-18: nine files totaling 8,474 lines. The decision tree contains 179 distinct existing Q/S identifiers: 157 Q and 22 S records. Gaps reflect previous cleanup; do not fill them or infer that deleted records are current requirements.

| Source | Path | Reading purpose |
| --- | --- | --- |
| Decision Register | [grill-me-design-tree.md](../docs/design/grill-me-design-tree.md) | All Q/S records, later corrections, formal ownership, and delivery sequence |
| Tool Actions | [tool.md](../docs/design/harness/tool.md) | Pure reads/Application Ensure, action permission, Proposal and business-write boundaries |
| Context | [context.md](../docs/design/harness/context.md) | Acquisition, Package/Frame, pinning, compaction, protected inputs |
| Memory | [memory.md](../docs/design/harness/memory.md) | Collaboration Memory, admission, three controls, background sources, forgetting |
| Budget | [budget.md](../docs/design/harness/budget.md) | Multiple owners, local/total limits, atomic reservation, unknown costs, capacity |
| Recovery | [recovery.md](../docs/design/harness/recovery.md) | Durable boundaries, ownership/fencing, retry, safe derivative recovery |
| Storage | [storage.md](../docs/design/harness/storage.md) | Four storage layers, retention, payload availability, history versus current eligibility |
| Eval | [agent-evaluation.md](../docs/design/eval/agent-evaluation.md) | Complete evaluation design, Q173–Q187, platform research, pending details |
| Non-normative inventory | [contract-design-inventory.md](../docs/design/contract/contract-design-inventory.md) | Candidate responsibilities, related objects, later-detail checklist; not Contract authority |

Every task first reads this English document, the Decision Register's Purpose/Session State, and Q4/Q22/S24.2/S37.1/S38.1, then relevant topic Q-IDs and detailed modules. Verify cross-module semantics against effective decisions; do not rely only on the inventory or this summary. If sources change during later tasks, record the changes and their impact before proceeding instead of silently using the old snapshot. The opening language rule comes from the user's subsequent explicit instruction, not a new Grill identifier.

### B. Formal output locations and stages

These are target paths for later tasks, not claims that the files exist or a creation list for this step. All resulting formal documents must be in English; do not plan parallel Chinese editions at this stage.

| Output | Planning scope/future task destination |
| --- | --- |
| `docs/spec.md` | First-stage main document: product scope and visible behavior |
| `docs/architecture.md` | First-stage main document: effective architecture, authority, dependencies, invariants, and Contract-document responsibility planning |
| `docs/contracts/*` | First stage plans structure, responsibilities, and boundaries in the authoring plan/Architecture only; no premature normative Contracts; complete separately after detailed Grill |
| `docs/acceptance.md` | First-stage main document: required proof and observable acceptance, without fabricated test results |
| `docs/development.md` | First-stage main document: delivery sequence, engineering/verification discipline, traceability, and handoffs |
| `docs/progress.md` | First-stage main document: summary grounded in the new repository's actual state, updated as work occurs |
| `docs/progress/traceability.md` | Q32's accepted supporting matrix within Progress, maintained by later progress work; no new top-level category |

Contract filenames and count await responsibility-based decomposition. Do not create “temporary complete Contracts” to bypass later Grill. Before detailed Contracts are complete, the Q32 matrix may use Grill sources for design plans and explicitly mark Contract IDs pending. This document's organizational labels are not formal Contract IDs.

### C. Cross-context tasks and dependencies

These are documentation task arrangements, not new product architecture decisions or already-created tasks. Every task shares section A's source rules and preserves evidence for both verification seams. English is mandatory for all formal outputs.

| Task | Required topics/sources | Output and responsibility | Completion and handoff |
| --- | --- | --- | --- |
| W1 Product Spec | Implementation sections 3–10 and 14; corresponding Q/S; user-facing Context/Tool/Memory boundaries | Author `docs/spec.md`: non-linear tasks, five navigation entries, Knowledge/Resumes, collection, both Fits, Advisor, Preparation/execution/tracking, Memory, non-goals | User behavior has effective sources; no old mechanisms, pseudo-fields, or implementation claims; hand off section→Q-ID mapping, pending Contract prerequisites, and boundaries needing architecture explanation |
| W2 Architecture and Contract structure planning | All nine records; Implementation sections 1–17, especially all Harness and Eval records | Author `docs/architecture.md`: responsibilities, owners, dependencies, transactions, evolution mechanisms, candidate Contract families; no Contract bodies | Align boundaries with W1; no conflicting cross-domain write/permission/recovery/persistence owners; hand off Contract Grill topics, reference directions, explicit exclusions |
| W3 Acceptance | W1/W2, module Verification implications, Q82, Q117, Q173–Q187 | Author `docs/acceptance.md` from product/architecture behavior, covering failure/concurrency/permission/recovery/Eval evidence | Scenarios have controlling sources; deterministic tests and semantic Eval remain distinct; no invented thresholds/release policy; hand off requirement→acceptance mapping and specific pending Contract details |
| W4 Development rules | W1–W3; Q22/Q26–Q27/Q32/S24.2/S37.1/S38.1; Eval delivery boundaries | Author `docs/development.md`: document review before Contract Grill before implementation; test-first, research, evidence rules | Do not assume scripts/tests exist or select the first Slice/CI release rules; hand off next-task entry points and checklist |
| W5 Actual progress and matrix | Actual W1–W4 files/review evidence; Q4/Q22/Q26/Q32/S38.1; current repository state | Author `docs/progress.md` and Q32 matrix, separating authored documents, pending Contracts, unstarted implementation, accepted post-v1 deferrals | No unsupported Implemented/Partial; target architecture is not progress prose; entries trace to sources, actual documents, and real evidence; hand off gaps/blockers/next step |
| W6 Joint review of five main documents | W1–W5, complete coverage index and semantic regression table; reread all nine sources as needed | Fully apply both seams, fix document conflicts, present concrete reviewable results for user review | Report seams separately; leave unresolved details explicitly for Contract Grill, without treating pending detail as invalid architecture or filling it silently; advance only after user review |
| Later stage, not executed here | Reviewed five documents, Contract structure plan, complete sources and pending-detail list | Separate detailed Contract Grill → complete `docs/contracts/*` → reconcile main-document/acceptance/matrix references → formal development | Do not reopen settled architecture to fit old code; review concrete schemas/errors/migrations at this stage; establish implementation status from later actual evidence |

W1–W5 provide a convenient authoring order across contexts; they do not restore the D0–D6 mandatory pipeline superseded by S38.1. W2 may correct W1 ownership wording. W3/W4 cannot add undecided business constraints merely for testability. W5 records actual state. Further task splitting must follow the same responsibilities and sources without expanding formal document categories.

Each handoff must include at least: sources read and controlling Q-IDs; actual changed sections and ownership/reference relationships; clause-level coverage and supersession dispositions; results for both seams; questions still awaiting detailed Contracts and their sources; real document/implementation status; next-task required reading. Put these in task completion notes and later Progress/matrix records, without creating another durable authority. The next context must reread actual files rather than rely solely on the preceding completion summary, and must continue using this English authoritative edition.

### D. Decision coverage index

The table covers every existing Q/S record and groups sources into searchable authoring topics. Different clauses within one source still require separate checks under Testing Decisions. The controlling-source column does not mean “read only the last ID,” nor does it invalidate every earlier decision wholesale. Effective semantics are described in Implementation Decisions and the original records.

Document abbreviations: P=Product Spec, A=Architecture, C=Contract structure/boundary planning (detailed norms later), V=Acceptance, D=Development, G=actual Progress/matrix. Primary ownership follows Implementation section 2. Multiple consuming documents do not create multiple authorities.

| Existing source records | Effective topic and scoped-supersession disposition | Controlling/supplemental sources | Consuming documents |
| --- | --- | --- | --- |
| Q1, Q6 | Non-linear tasks; navigation is not Domain ownership; use later five-entry navigation | S17.2–S17.4 | P, A, V |
| Q2, Q3, Q5, Q11 | Separate minimal canonical Contracts, six categories, incremental responsibility-based split | S24.2, S38.1 | A, C, D |
| Q4, Q22 | Clean slate and documentation first; no inherited code/completion/old ordering | S37.1, S38.1 | P, A, C, V, D, G |
| Q7, Q18 | Separate eligibility/readiness/progress; minimal evolution mechanism per object | Q37, Q42 and other specific mechanisms | P, A, C, V, D |
| Q8 | Independent Profile/Preferences/Evidence/Resume; remove screening snapshot | Q53–Q56, Q63 | P, A, C |
| Q10, Q14, Q58, Q59 | Independent durable RequirementSet, validated activation, shared Ensure; not a QuickScreen input | Q56, Q110–Q111, Q117, Q142, Q171 | P, A, C, V |
| Q12, Q13 | Source-identity Job; cross-platform historical merging REJECTED | Q12 | P, A, C, D |
| Q15, Q63, Q64 | Shared experience facts, human reconciliation; import-immediately-formal and fragment interpretations replaced | Q70–Q75, Q108, Q114, Q163 | P, A, C, V |
| Q16, Q25, Q42 | Separate Candidate assets/mutable Preparation/frozen execution; later Greeting and reentry rules | Q30, Q150, Q157, Q162 | P, A, C, V, D |
| Q17, Q44, Q48 | Manual root may lack JD; BOSS admission differs but JobVersion meaning is shared | Q48, Q49, S9.1 | P, A, C, V |
| Q19, Q72, Q82 | Baseline/eligibility/actual visibility, completeness, bounded MISSING; remove confirmation Gate | Q83, Q112–Q115, Q139, Q172 | P, A, C, V, D |
| Q21 | Interviews as ApplicationEvents, not independent Aggregate | Q21, Q37 | P, A, C, V |
| Q23 | Pursuit distinct from one-run selection; bookmarks await future design, without legacy-only retention | S37.1 | P, A, C, G |
| Q24 | Advisor independent of DeepFit; no old-lineage migration requirement | Q58, Q112, Q139, S37.1 | P, A, C, V, G |
| Q26, Q32 | Norms versus status, stable IDs/matrix/future checks; existence does not mean completion | S37.1, S38.1 | A, C, V, D, G |
| Q27 | Upstream research, version/license verification, adapter boundary | Q3, Q49 | P, A, C, D, G |
| Q30, Q31 | Snapshot/Approval/Attempt/real business fact distinctions; read-back and human reports | Q150, Q157, Q164 | P, A, C, V, D |
| Q35, Q40 | Batch orchestrates independent tasks; select, prepare dependencies, then full freeze; fail closed on stale/revoked input | Q110–Q112, Q172, S22.1 | P, A, C, V, D |
| Q36, Q37 | Batch is not a transaction; technical/business events differ; non-linear append-only progress | Q160 | P, A, C, V |
| Q41, Q85 | Conversation does not implicitly write facts; all old Advisor working-draft behavior removed | Q128, Q133, Q138, Q146, Q148–Q149, Q158 | P, A, C, V |
| Q45, Q55, Q56 | Global hard Preferences, deterministic screening, removed redundant screening authority | Q161 | P, A, C, V, G |
| Q46, Q51 | Assessment authority, independent deterministic scores, explicit rescoring | Q112, Q168 | P, A, C, V |
| Q47, Q52 | Unified durable Session/bounded Turn; later compaction and wait rules | Q89, Q132, Q139, Q155, Q158–Q159, Q167 | P, A, C, V, D |
| Q49, Q50 | Two-stage collection, aggregate audit, freshness/availability; no cooldown-only strong-risk recovery | Q160–Q161, Q164 | P, A, C, V, D |
| Q53, Q54 | Single-user scope without Candidate root; narrow Profile and privacy | Q119 | P, A, C, V |
| Q66, Q70, Q71, Q73, Q74 | Saved baseline, Draft before atomic Save, complete factual grounding; no confirmation object | Q108, Q113–Q114, Q118–Q119, Q147, Q166 | P, A, C, V, D |
| Q75, Q79, Q86, Q87 | No persistent Assertions; exact refs/historical readers; actual-dependency grounding cannot rescue old facts by rebinding | Q108, Q114 | A, C, V, D |
| Q76, Q77, Q96, Q97, Q98 | Body-fact versions/current use; deletion/propagation preserve history; distinguish presentation changes | Q108, Q113–Q114, Q118–Q119, Q146, Q151, Q163 | P, A, C, V |
| Q80, Q81, Q83 | Harness Context strategy/per-call Frame; retrieval retained only as future boundary | Q121, Q123, Q132, Q136, Q139, S24.1 | A, C, V, D, G |
| Q88, Q89, Q93, Q100 | Default/discussion selection, unified Session, logical Resume deletion; separate apply precedence | Q146, Q149 | P, A, C, V |
| Q91, Q94 | Explicit narrow CAS return to Preparation; append-only runtime inputs; no Advisor draft | Q108, Q134, Q146, Q158 | P, A, C, V |
| Q108, Q109 | One current temporal fact; old Overlay-isolation branch REJECTED; working-draft clauses superseded | Q113–Q114, Q146, Q151, Q163 | P, A, C, V |
| Q110, Q111, Q112 | Two-stage freezing, independent LLM parsing, independent Fits; no Coverage/gap/upper-bound model | Q113–Q117, Q142, Q168, Q171 | P, A, C, V |
| Q113, Q114, Q115, Q116, Q117 | Save authority, automatic sync, scoped four states, target serialization, deferred parser-release Gate | Q118–Q119, Q122, Q168, Q171 | P, A, C, V, D |
| Q118, Q119 | Atomic commit of all affected authority; Profile changes do not alter career baseline | Q147, Q151–Q152 | P, A, C, V, D |
| Q120, Q121, Q126 | Shared Harness/independent Skills, typed actions, Full Context; no v1 RAG/generic execution tools | Q123, Q127–Q128, Q138–Q139, Q144 | P, A, C, V |
| Q122, Q124, Q125 | Durable recovery/fencing, owner reservation/usage, four storage layers | Q130, Q135–Q136, Q140–Q142, Q156 | A, C, V, D |
| Q123 | v1 exact-input capacity preflight failure; no silent degradation | Q132, Q172 | P, A, C, V |
| Q127, Q128, Q129, Q130, Q131 | Collaboration Memory/supported user sources, three authority rules, background owner, non-resurrecting forgetting | Q132–Q133, Q139, Q145, Q169–Q170 | P, A, C, V, D |
| Q132, Q134, Q135, Q136 | Separate Context, actual exact post-write inputs, Run-wide allowance, active pins versus history | Q139, Q140, Q158 | A, C, V, D |
| Q133, Q138 | Session assertions support discussion with real provenance; formal apply follows later Proposal rules | Q146, Q148–Q149, Q158 | P, A, C, V |
| Q137, Q139 | Independent learning/Recall/management, lazy/eager distinction, Memory excluded from checkpoints | Q143, Q172 | P, A, C, V |
| Q140, Q141, Q142 | No hidden retry, transient streams, durable parse single-flight/owner-only cost | Q144, Q156, Q159, Q171 | P, A, C, V |
| Q143, Q144, Q145 | Exact lazy pinning, pure read/Application Ensure, newer manual Memory management prevails | Q149, Q159 | A, C, V |
| Q146, Q148, Q149 | Page-only Draft, actual-target Proposal/one complete confirmation; no source-selection concept | Q156, Q158, Q166–Q167 | P, A, C, V |
| Q147, Q152 | Authority plus durable intent, post-commit demand-driven derivatives | Q165 | P, A, C, V, D |
| Q150, Q157 | Freeze actually viewed material/Greeting; fixed default/manual editing; separate execution approval | Q30 | P, A, C, V |
| Q151, Q153, Q154 | Knowledge-page logical deletion/direct membership; Resume selection-only removal; empty state differs from task readiness | Q163 | P, A, C, V |
| Q155, Q156, Q158, Q159 | Foreground serialization, commit independent of narration, human versus dependency wait | Q167 | P, A, C, V |
| Q160, Q161, Q162 | Shared persistent safety, frozen collection/latest local filtering, unfinished Preparation reentry | Q164 | P, A, C, V |
| Q163, Q164, Q165, Q166, Q167 | Whole experiences, execution checks without refresh, obsolete derivative skipping, disposable Draft, atomic Session-delete revocation | Q170 adds background-source deletion | P, A, C, V |
| Q168, Q169, Q170, Q171, Q172 | Unscored versus no-target distinction, isolated Memory failures/deleted-source publication ban, protected-input revocation ends task | Each record remains effective | P, A, C, V |
| Q173, Q174, Q175, Q176, Q177 | Isolated real paths, derived telemetry, evidence categories do not define release, independent judges, exact fixtures/configuration | S35.1 | A, C, V, D; P for quality boundaries only |
| Q178, Q179, Q180, Q181, Q182 | Fixed-input Scenario/N+1, per-check completeness, valid alternatives, regression retention, output-preserving re-evaluation | Q183–Q187 | A, C, V, D |
| Q183, Q184, Q185, Q186, Q187 | Coherent boundary, task-scoped evaluator, answer/control isolation, experiment scope, controlled Memory | Each record remains effective | A, C, V, D |
| S5.1, S5.3 | Flat list/Company view, Job-side and Resume-side entry points | S17.2–S17.3, Q112, Q139 | P, A, C, V |
| S7.1, S17.4, S22.1 | Shared Harness, independent Skills, one semantic task per Run; compaction is same-Run auxiliary work | Q120–Q121, Q127, Q132 | P, A, C, V, D |
| S9.1 | Local durable Jobs and explicit refresh; no rejected BOSS content persistence | Q48–Q49, Q160–Q161, Q164 | P, A, C, V |
| S15.1 | Retain experience-level facts/Full Context First; supersede old coverage/confirmation/v1 overflow retrieval | Q79, Q98, Q108, Q111–Q113, Q121, Q123, Q163 | P, A, C, V, D |
| S17.1, S17.2, S17.3 | User-owned acquisition scope, five navigation entries, one Assistant/two entry modes, not separate Sessions | Q89, Q139, Q146, Q149 | P, A, C, V |
| S24.1, S24.2 | Agentic RAG post-v1; settled architecture is not completed detailed Contracts | Q123, Q22, S38.1 | A, C, D, G |
| S25.1, S26.1 | Detailed Harness records and separate Context/Storage ownership; records are not new authority | Q125, Q132 | A, C, V, D; record history |
| S27.1, S28.1, S29.1, S29.2, S30.1 | Module maintenance, explicit cleanup, Tool/inventory, Memory filename correction; not product features or permission to edit sources now | Q139; original maintenance history | D/source notes; inventory is planning only |
| S35.1 | Langfuse-heavy/JobHunter-thin Eval with real task semantics | Q173–Q187 | A, C, V, D; P quality boundaries |
| S37.1, S38.1 | New repository rebuild, nine source files, documentation first; earlier first-Slice/bootstrap recommendations unaccepted | Q4, Q22 updated in place | Stage boundaries for all categories; G actual status |

Interpret removed historical identifiers only through retained replacement links, for example Q9→Q12, Q57/Q62→Q75, Q65/Q68/Q69→Q112, Q78/Q84→Q113, Q92/Q95/Q99/Q102–Q104/Q106–Q107→Q108, Q101→Q146, and Q105→Q151. They are not counted as current records and do not require restoring original text. REJECTED Q13/Q109 remain exclusion evidence; DEFERRED S24.1 remains post-v1 scope evidence.

### E. Handoff boundaries for pending details

The following assigns unresolved matters to later work; document authors must not supply the answers:

- Detailed Contract Grill: actual Profile/Evidence/Job inputs, per-function prerequisites, canonical reference syntax/validation, exact Fit target keys, output/error/status representations, complete Tool catalog, command/API payloads, approval/Proposal lifecycle, runtime transitions, transaction protocols, schemas, and new-system historical evolution/migration details.
- Related Contract/policy design: score availability and weights, budget units/amounts/overrun/unknown reconciliation, compaction and Memory trigger/range representation, retention periods/physical storage/cleanup coordination, render/channel payloads. Preserve accepted constraints without inferring numeric defaults.
- Research and implementation preparation: pinned source commits and mappings; actual Langfuse/SDK versions, deployment/worker capabilities, and redaction configuration. A selected platform does not imply that every version's capabilities have been verified.
- Later rollout work: Q175's Trial counts, thresholds, default enablement, CI/release rules. Architecture Grill closure does not mean those policies were settled.
- Explicitly deferred extensions: Candidate Agentic RAG, formal annotated parser certification, bookmark/Pursuit UX, General Assistant/interview capabilities, cross-platform merging, multiple Candidates/multi-tenancy, comprehensive physical erasure, and old-data import. Start separately under their source decisions, not inside these authoring tasks.

Distinguish “settled architecture awaiting detailed Contract expression,” “explicitly deferred capability,” and “later research/rollout work.” If later decisions cannot resolve a genuine textual conflict, report the exact clauses, sources, and impact. Do not silently choose a new mechanism or reopen the entire Architecture Grill.
