# JobHunter Implementation Plan

> English is authoritative. All subsequent formal documents are written in English; no Chinese formal edition is planned. W6 authoring snapshot: 2026-09-19. This plan contains twelve macro Slices and 24 independently executable internal milestones. W7 reviewed the earlier baseline; the user has since authorized SL-01.M1 Grill and approved the scoped CG01-BC1 architecture/plan revision; no milestone is Contract-ready or implemented merely because it is planned here.

## 1. Authority and use

This global main document owns macro capability decomposition, recommended progression and shared planning invariants. Its [Slice documents](slices/README.md) own detailed milestone dependencies, required Contract portions and completion conditions within the same Implementation Plan category. [Product](../spec.md) owns behavior; [Architecture](../architecture.md) owns mechanisms and architectural Contract boundaries; [Contract Structure](../contracts/structure.md) maintains the subordinate planned document organization; [Acceptance](../acceptance.md) owns required proof; [Development](../development.md) owns general delivery discipline; [Progress recording rules](../progress/README.md) owns status/readiness/evidence recording; [Progress](../progress.md) and its [matrix](../progress/traceability.md) own actual status/evidence. This plan references those owners rather than establishing competing business or protocol definitions.

Inputs are the [English authoring spec](../../.scratch/document-authoring-spec.en.md), [revised W5 entry](../../.scratch/w5-progress-handoff.md#w6-entry-and-concrete-handoff), actual W1–W5 drafts/matrix, preserved [macro draft](../../.scratch/w6-macro-slice-draft.md), and accepted [Contract structure handoff](../../.scratch/contract-structure-grill-handoff.md). The [Decision Register](../design/grill-me-design-tree.md) and detailed Harness/Eval modules remain provenance. Later clauses control even where an earlier record remains ACCEPTED. The Contract Design Inventory remains a non-normative checklist.

The later user process instruction and 2026-09-19 CS1–CS5 agreement control delivery and structure: dedicated candidate-save; independent task sections in one fit-analysis document; standalone platform safety; one execution/recovery protocol owner; and twelve macro Slices with independently ready internal milestones. These are not invented Q/S decisions. The historical fifteen-Slice proposal and whole-parent readiness gate do not apply. Specific milestone allocation in the linked Slice plans and the macro progression below are W6 planning proposals for W7/user review, not claims of earlier Grill approval.

The seven categories remain Product, Architecture, Implementation Plan, Contracts, Acceptance, Development and Progress. Six main documents are authored; four scoped normative Contracts now exist for SL-01.M1, reached through [Contract Index](../contracts/index.md). The later user-approved [CG01-BC1](../design/contract/sl-01-m1-grill.md#cg01-bc1) revises ManualApplicationEntry and formal Job delivery boundaries without changing the 12-Slice/24-milestone count. The earlier architecture/plan writeback created no Contract bodies or IDs. The subsequent M1 Grill/writeback supplies its own real normative clauses; neither step creates product code or executed acceptance. Historical W1–W5 handoffs and the provisional macro draft retain their original snapshots.

**Sources:** Q2–Q5, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1; later user authority in [Further Notes F](../../.scratch/document-authoring-spec.en.md#f-user-approved-delivery-process-revision).

## 2. Milestone readiness, completion and dependency meaning

After W7 and user review, each selected milestone follows [Development 5](../development.md#5-future-slice-planning-and-test-first-work): detailed Grill of its required scope → actual normative writeback with genuine Contract IDs → reconciliation of both sides of necessary interfaces and affected formal documents → required research/upstream implementation readiness → test-first development and scoped acceptance → actual Progress/matrix evidence. Other milestones in the same Slice may remain pending. One ready section does not make its whole file/family ready; Contract readiness is not implementation.

Each milestone entry in its Slice document identifies goal/value, scope/exclusions, implemented upstream scope, required document sections, joint agreements, research, tests/Eval and completion. Use stable planning identifiers distinct from Q/S and Contract IDs; a navigation entry, database table, generated file or illustrative Eval directory is not automatically a Slice or Domain owner. It inherits its parent's controlling sources/families and Acceptance destinations, plus the common obligations here. Document stems mean planned paths under `docs/contracts/`; the named responsibility portions are planning locators in [Contract Structure](../contracts/structure.md), under Architecture 16's boundaries, **not existing normative anchors or Contract IDs**. “Reuse” means verified future reuse of actually completed compatible scope, never a placeholder assumption.

Every milestone requires the applicable complete `common.md` identity/exact-reference/revision/idempotency/provenance/admission meanings and `foundation/storage.md` availability/history/privacy/retention scope it actually uses. Domain owners define their particular identity and content; this creates no all-system base object or whole-common/storage gate. Any needed action, source or runtime boundary not previously delivered must be completed for its first consumer. Fields, types, enums, state transitions, payloads, schema, validation errors and migrations remain entirely for later Contract Grill.

Dependency entries have two explicit categories:

- **Required upstream capability:** the exact already-working business capability/data authority that this milestone consumes. The cited milestone is an engineering delivery locator; Product and the task's Contracts alone define user-facing inputs and prerequisites. Neither its parent completion nor execution of an unrelated upstream workflow is required.
- **Reused component/infrastructure:** a concrete verified persistence, invocation, Context, budget, coordination or evidence component. Reuse is an engineering prerequisite where actually needed, never an instruction for the user to complete its originating product task. Name only the applicable portion and extend/verify it at the consumer when required.

Both categories need real implemented evidence before the dependent scope develops; changing a label does not waive a safety dependency. Contract-interface agreement and research remain separate prerequisites. Conditional integrations are identified explicitly, excluded from the unconditional dependency graph, and become required only for the selected consuming scope. Dependency relationships are transitive.

SL-02.M1 supplies inseparable authority participants because Save updates all affected state. Candidate Fit consumes its saved Evidence capability without requiring user possession of a Resume. Collector/Executor may reuse applicable SL-03.M1 invocation durability primitives without becoming Agent Skills, completing RequirementParse, or routing every platform operation through a universal effects framework. The invocation foundation does not absorb candidate-save, derived-work, collection/execution workflows, platform risk or consent merely because they involve failure/recovery; Q122 and Q147/Q152 retain their distinct replay and authority boundaries. Unselected rendering or model assistance does not block basic import; the owning Slice carries conditional integration scope.

An enabling component milestone may be accepted with actual executable component/interface and fault evidence. It cannot claim a business capability supplied by another milestone. No real model/platform consumer may run before its complete applicable permissions, exact inputs, budget, durable effect/recovery, safety and evidence safeguards are ready. No test-only replacement Agent, unguarded temporary provider call or asynchronous repair of authoritative facts qualifies.

Completion of a milestone requires its stated real outcome, all applicable Acceptance proof, truthful limits, and updated Contract→implementation→test/Eval→status mappings. A parent completes only when **all its listed required milestones and integrated/cross-milestone obligations** are accepted. No additional state enum or universal release threshold is defined here. Shared Contract changes require impact review of earlier consumers and evidence, with plan/dependency updates where needed.

### 2.1 Scope-level Contract readiness invariant

**Contract file existence ≠ Contract family complete; section complete ≠ document complete. A milestone requires only its consumed normative scope to be ready, but that scope and every necessary interface must be complete.**

Use [Progress recording rules](../progress/README.md#5-two-level-progress-and-scope-level-contract-readiness) to identify each actual scope, reviewed revision, covered/open clauses, interfaces, consumers and evidence. This plan selects the required scope; the recording rules define how readiness is represented, and the [scope ledger](../progress/traceability.md#6-contract-normative-scope-readiness-ledger) records actual readiness. Unrelated task/batch scope in the same file may remain pending; the owning Slice defines exactly what its milestone consumes.

### 2.2 Parent and milestone progress invariant

A milestone's accepted capability can be available while its parent remains incomplete; a completed child cannot complete the parent by itself. The plan's milestone and integrated parent completion conditions remain controlling. Record aggregate status, child availability, required remainder and evidence under [Progress recording rules](../progress/README.md#5-two-level-progress-and-scope-level-contract-readiness), with actual values in [Progress](../progress.md) and its [matrix](../progress/traceability.md). Readiness, implementation and acceptance remain separate observations.

## 3. Recommended progression and independent branches

This is a macro recommendation, not a calendar, committed estimate or mandatory user funnel. Begin with local Workspace/ManualApplicationEntry and then complete versioned acquisition Preferences. Saved authority and invocation infrastructure can proceed independently. Under [CG01-BC1](../design/contract/sl-01-m1-grill.md#cg01-bc1), formal Job production and local Job/Company views move to SL-08.M2; application history waits for that real Job provider but does not require automated execution.

Saved authority enables reviewed import without waiting for rendering. Demand-driven materials serve their actual consumers. Protected invocation enables parsing and general Advisor discussion; usable Requirements enable independent Candidate Fit, Resume Fit and Job-targeted discussion. Candidate and Resume Fit can develop in either order. Shared platform safety and applicable invocation primitives support collection and execution without turning them into semantic Agent tasks.

Ordinary Preparation consumes eligible materials and a formal Job without requiring Advisor. Execution consumes ordinary Preparation, event authority and shared safety/recovery without requiring a fresh collection for each execution or Advisor adoption. The actual formal Job producer remains an upstream capability; collection success never grants execution authorization. Collaboration Memory consumes eligible conversation/Context, not successful Proposal application. Every actual consumer still needs its complete first-use safeguards.

Under [CG02-BC1](../design/contract/sl-01-m2-grill.md#cg02-bc1), SL-01.M2 supplies complete explicit Preferences and immutable versions without waiting for Collection. SL-08.M2 consumes an exact PreferenceSetVersion, shared safety and applicable invocation durability; it implements source query/admission mapping, produces real formal Jobs and verifies independent local view queries. No M2 QuickScreen component or current-Preference re-filtering gate remains. SL-03.M3, SL-09.M1 and SL-10.M1 consume those formal Jobs; Fits and Job-targeted Advisor inherit that dependency through Requirements. Component fixtures cannot stand in for the user-visible producer. `jobs/jobs-screening.md` remains the normative Job owner; milestone scheduling does not transfer authority to Collection.

Exact **Required upstream capability** and **Reused component/infrastructure** entries, conditional integrations and acceptance boundaries live only in the owning Slice document. Use the [Slice index](slices/README.md) to open them. The macro relationships here do not add a hard dependency on an entire upstream Slice; the selected milestone consumes only its specified available capabilities/components.

## 4. Contract document and joint-interface map

[Architecture 16](../architecture.md#16-contract-document-structure-and-responsibility-plan) owns F01–F11 high-level responsibilities and seven cross-owner agreements. [Contract Structure](../contracts/structure.md) maintains the revised 28-document organization and structural consumer locators under those boundaries. [Contract Index](../contracts/index.md) distinguishes planned destinations from existing normative bodies. No file/family must be completed merely because a selected milestone consumes one of its scopes.

Each Slice document owns its exact required Contract portions and first-consumer agreements. The [scope readiness ledger](../progress/traceability.md#6-contract-normative-scope-readiness-ledger) records actual readiness by responsibility portion; the [milestone ledger](../progress/traceability.md#5-milestone-implementation-and-acceptance-ledger) records implementation/acceptance independently. These replace a duplicated global document-to-milestone dependency table.

Preserve the seven Architecture agreements whenever affected: Save/propagation/demanded intent; Proposal/Session; Requirements/Fit/Harness; material/Preparation/execution/safety/events; Context/Memory/Storage; Budget/runtime/recovery; and Eval consumption of canonical facts. Reciprocal Contract agreement is not automatically an implementation dependency cycle. Shared definitions have one owner, and every necessary producer-consumer interface must be complete before its actual consumer develops.

## 5. Macro Slices and executable milestones

The twelve linked plans retain all 24 milestone definitions and controlling Q/S references. Each Slice plan is the single detailed planning location for its parent and milestones. Milestones stay inline unless a particular plan becomes too large to maintain; splitting one later must retain its stable ID and link from its parent, without creating a new authority.

| Macro Slice | Detailed planning document | Milestones |
| --- | --- | --- |
| SL-01 | [Local Workspace, Manual Application Entries and Preferences](slices/sl-01-workspace-jobs-preferences.md) | 2 |
| SL-02 | [Saved Knowledge, formal Resumes and safe materials](slices/sl-02-saved-authority-materials.md) | 2 |
| SL-03 | [Shared controlled execution with RequirementParse](slices/sl-03-invocation-requirements.md) | 3 |
| SL-04 | [Resume import into reviewed Draft and shared Save](slices/sl-04-resume-import.md) | 1 |
| SL-05 | [Independent Candidate Fit](slices/sl-05-candidate-fit.md) | 2 |
| SL-06 | [Independent Resume Fit](slices/sl-06-resume-fit.md) | 2 |
| SL-07 | [Advisor discussion, exact Proposals and confirmed changes](slices/sl-07-advisor.md) | 3 |
| SL-08 | [BOSS collection and shared platform safety](slices/sl-08-collection-platform-safety.md) | 2 |
| SL-09 | [Human-reported applications and event-derived progress](slices/sl-09-application-history.md) | 1 |
| SL-10 | [Preparation, viewed-material confirmation and adopt-back](slices/sl-10-preparation.md) | 2 |
| SL-11 | [Explicit authorized execution and independent batch outcomes](slices/sl-11-execution.md) | 2 |
| SL-12 | [Collaboration Memory with independent controls and forgetting](slices/sl-12-collaboration-memory.md) | 2 |

A local edit to scope, dependency detail, Contract portions or proof belongs in the Slice file. Update this global plan only when macro coverage, shared invariants or cross-Slice direction actually changes. Update navigation on file/title/locator changes and Progress on real readiness/evidence changes; do not copy detailed dependency tables into README files.

## 6. Coverage, first-use evidence and maintenance

The [Progress matrix](../progress/traceability.md#2-existing-record-coverage-and-effective-destinations) retains all 179 original Q/S records across 73 clause/topic rows and now links each row to this plan's destinations or a reasoned non-capability disposition. It preserves controlling supersession and actual behavior/proof owners; the following compact coverage view cannot replace that clause mapping.

| Product scope | Required planned delivery |
| --- | --- |
| P2 task organization | SL-01 and actual entry points of every consuming milestone; no compulsory product pipeline |
| P3 Knowledge / Resumes / import / materials | SL-02 saved authority/materials; SL-04 reviewed import; SL-07 confirmed changes |
| P4 Jobs / Preferences / collection | SL-01 manual entries/complete versioned acquisition Preferences; SL-08 formal Job producer/local views/collection/safety |
| P5 Requirements / independent Fits | SL-03 Requirements; independent SL-05 Candidate and SL-06 Resume Fit |
| P6 Advisor / Session | SL-07 Advisor/Session; SL-10 Preparation-origin integration |
| P7 Preparation | SL-10 Preparation; SL-02 materials |
| P8 execution / history | SL-09 history; SL-11 execution; SL-08 shared safety |
| P9 privacy / execution / Context / retention | First persistence/use throughout; SL-03 runtime; SL-07 interactive; SL-12 background/Memory |
| P10 collaboration Memory | SL-12, required v1 scope |
| P11 evidence / quality | Proof with each consumer; SL-03 infrastructure/parser; SL-05/SL-06 Fit; SL-07 Scenario/N+1; SL-10/SL-11 workflows; SL-12 controlled Memory |
| P12 non-goals / pending detail | Section 7 and matrix dispositions; no invented delivery commitment |

Eval is not a final platform Slice. Isolated fixtures/trials exercise real Application/Harness paths; checks use canonical local state, actual input/output and declared task/experiment scope. Protected expected answers/control cannot enter model context. Independent judges have separate resources and cannot determine commit, consent or recovery. Check completeness, semantically valid alternatives, coherent boundary/N+1 behavior, privacy-safe retention and output-preserving re-evaluation apply as soon as their consuming scope exists. Telemetry is derived and its failure cannot invalidate a real business result.

Tests must cover relevant positive, rejection, permission, concurrency, failure and recovery paths. Use task-scoped semantic review where semantic behavior is introduced. A deterministic component check cannot claim end-to-end semantic quality; an apparently good answer cannot prove authority or safety. [Eval acceptance 2–3](../acceptance/evaluation.md#2-eval-execution-and-evidence-integrity) remains the proof owner; the [Eval development guide](../development/evaluation.md) supplies specialized implementation/evidence procedure. No test, Eval receipt or quality threshold is created by this document.

After each actual milestone, record real Contract IDs, implementation/test/Eval locations, evidence and unresolved limitations in Progress/matrix. Reconcile affected main documents and dependencies when a shared interface changes. Before parent completion, verify all required milestones and cross-milestone obligations; before any broader release claim, separately resolve applicable rollout decisions. File count, framework wiring or one successful happy path is not completion.

## 7. Pending detail, exclusions and next handoff

Four of the 28 catalog destinations now have reviewed M1 normative portions; 24 documents and additional portions of the existing shared documents still require later normative expression. Required fields/types/enums, detailed transitions, interfaces/API payloads/schema/errors/migration, score policies, reference/target keys, exact approval/concurrency protocols, budget/Context/Memory policies, retention, render/channel criteria and Eval interfaces/metrics are not answered here. Shared ownership is agreed; actual necessary interfaces must be Grilled together for the selected milestone. Research may expose a concrete feasibility gap; record it and revise affected scope rather than silently choosing unsupported behavior.

Explicit deferrals remain separate: Q23 future bookmark/Pursuit UX (not the separately accepted ManualApplicationEntry); Q117 formal annotated parser release certification pending demonstrated need; Q175 Trial counts/thresholds/default enablement/CI-release policy; Q81's retained retrieval boundary and S24.1 post-v1 Candidate Agentic RAG. Runtime parser quality, exact Context and required v1 Memory remain current scope, not deferred just because their milestones are later.

Q13 cross-platform merge and Q109 historical Overlay isolation remain rejected. No restored KnowledgeConfirmation, Advisor working draft, private Resume facts, Coverage/upper-bound comparison, silent RAG/degradation, hidden retry, historical fact rebinding rescue, universal lifecycle, generic execution Tool, second Eval Agent/platform, mandatory Monitor, General Assistant/interview Skill, old-lineage migration or inherited completion is planned. Source-organization records describe provenance, not implementation features or authorization to modify Grill history.

W6 delivered this global plan, twelve detailed Slice documents and the [W6 handoff](../../.scratch/w6-implementation-plan-handoff.md). The [W7 handoff](../../.scratch/w7-joint-review-handoff.md) now records joint review of the reorganized baseline under both seams, all 29 semantic regressions and milestone/parent checks. The user has selected SL-01.M1 and approved the scoped CG01-BC1 boundary/plan revision. M1 backend is now implemented and the later M2 Grill is complete through CG02-Q40, with actual scope review and backend-first handoff linked from the owning SL-01 plan. Development follows those reviewed consumed scopes; UI implementation still waits for design. Historical W7 review is not evidence that this later revision was previously reviewed. There is no need to complete every Contract family, file or parent Slice in advance.
