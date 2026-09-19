# JobHunter Development

> English is the authoritative documentation language. This draft was authored in W4 and maintains stable delivery discipline for the user-approved plan-first, scoped-Contract process. It defines delivery and verification rules for future work. It is not a repository setup guide or evidence of implemented features, existing test commands, deployed Eval, or completed acceptance. See [Progress](progress.md) for current joint-review and user-approval state.

## 1. Responsibility and authority

Development owns the process and discipline for turning reviewed requirements into implemented, verified capabilities: source interpretation, research, test-first work, verification routing and handoffs. It consumes the behavior defined by [Product](spec.md), the boundaries defined by [Architecture](architecture.md), and the required proof defined by [Acceptance](acceptance.md). The independent [Implementation Plan](plans/implementation-plan.md) owns macro Slice and internal milestone decomposition, business value, recommended order, dependencies, required Contract scope and completion conditions. Development owns the general discipline for executing that plan. Specialized Eval procedure lives in [Evaluation development and evidence](development/evaluation.md); status, readiness and evidence-recording rules live in [Progress recording rules](progress/README.md). These documents do not redefine business rules, duplicate the acceptance scenario catalog or choose missing Contract details for implementation convenience.

| Document category | Authoritative responsibility | Development's relationship |
| --- | --- | --- |
| Product | Scope, user tasks, prerequisites, visible behavior and non-goals | Identify the capability and intended outcome before planning work |
| Architecture | Owners, dependencies, authority, permissions, persistence, concurrency, recovery and high-level Contract boundaries | Preserve the real boundaries through implementation and verification |
| Acceptance | Observable scenarios, required evidence and limits on conclusions | Select the relevant proof obligations; do not replace them with a happy-path demonstration |
| [Implementation Plan](plans/implementation-plan.md) | Macro Slice decomposition, scope, order, dependencies, required Contract scope and completion conditions | Independent peer of Development; supplies the planned unit of delivery, not business authority or actual completion |
| Contracts, planned under `docs/contracts/*` | Detailed normative business/data/interface requirements progressively written after each relevant milestone's Contract Grill | Consume complete reviewed definitions for the current milestone and stable IDs; other milestones in the same Slice may remain pending |
| Development | Delivery sequence and general engineering/verification discipline | Define the process without inventing another product or runtime authority |
| [Progress recording rules](progress/README.md), [Progress](progress.md) and its [matrix](progress/traceability.md) | Status/readiness/evidence-recording rules and separate actual documentation, implementation, verification, gaps and next step | Update from real changes and evidence; keep transient status out of normative Contracts |

The [English authoring spec](../.scratch/document-authoring-spec.en.md) governs current documentation work; the [W3 handoff](../.scratch/w3-acceptance-handoff.md) locates its preceding results and pending details. The [Decision Register](design/grill-me-design-tree.md) and detailed modules preserve accepted design provenance. The [Contract Design Inventory](design/contract/contract-design-inventory.md) remains non-normative. Neither handoffs nor the inventory become an additional formal-document category. The [user-approved process revision](../.scratch/document-authoring-spec.en.md#f-user-approved-delivery-process-revision) adds Implementation Plan as the seventh category and changes the older Q22/S38.1 delivery ordering. This is later user authority, not a claim that the original Grill already selected this sequence.

All formal documents and supporting formal documentation use English. Preserve the existing Chinese authoring reference; it is not a competing authority and no formal Chinese editions are planned at this stage. This authoring rule does not change product UI labels or establish a UI localization policy.

**Sources:** Q2, Q5, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1; language and automatic handoff reading are explicit user instructions.

[Implementation Plan](plans/implementation-plan.md) governs its linked Slice plans; concrete milestone scope, dependencies and required Contract portions stay there. Supporting guides do not create another document category. Most READMEs/indexes provide navigation only; the user explicitly assigns Progress recording rules to [progress/README.md](progress/README.md). Formal review includes the relevant supporting guides, plans and evidence records, not just the main documents.

## 2. Delivery sequence and stage boundaries

| Stage | Work and boundary before continuing |
| --- | --- |
| Main documentation and macro planning | Establish reviewed Product/Architecture/Acceptance boundaries and the Implementation Plan before detailed milestone work; documentation is not implementation evidence |
| Joint baseline and user review | Apply both verification seams to the main documents and their relevant supporting guides/plans/records; authored drafts and scoped checks do not establish user approval |
| Selected milestone's Contract Grill | Resolve the complete normative scope identified in Implementation Plan, using accepted architecture, required research and shared-interface dependencies |
| Normative writeback and reconciliation | Write actual clauses and stable IDs, reconcile required producer/consumer interfaces and affected owners, and record scope readiness under Progress rules |
| Development and scoped acceptance | Begin only after required scope and real upstream prerequisites are ready; apply test-first work and appropriate deterministic/semantic verification |
| Evidence, handoff and continuation | Update actual Progress records and handoff; follow the plan's milestone/parent completion conditions; repeat the cycle or reconcile shared changes and affected prior consumers |

The later explicit user process revision controls plan-first, independently ready milestone delivery. Q22/S38.1 retain their clean-slate/documentation-first boundary, not the older whole-system Contract gate. Current authoring tasks, milestone allocations, review state and next work belong to [Implementation Plan](plans/implementation-plan.md) and [Progress](progress.md). This discipline selects no first Slice, bootstrap, code layout, runner or dependency version. Accepted target architecture is not an installed implementation.

Work requiring unresolved detail must identify the exact missing definition and its owner. A deferred field or threshold is not an invitation to reopen the entire Architecture Grill, nor does it prevent writing accurate main-document boundaries. A genuine unresolved semantic conflict must be reported with the conflicting clauses, controlling sources and impact; do not silently invent a mechanism to make the documents agree.

**Sources:** Q4, Q22, Q26, Q32, Q117, Q175, S24.2, S35.1, S37.1, S38.1 for surviving commitments; later user process revision linked in section 1 for the current sequence; Architecture 1/16–17; Acceptance 1/14.

## 3. Source interpretation and change discipline

Start each task at [docs/index.md](index.md), then the relevant directory README and actual owning documents, not solely from the prior completion summary. Read the preceding handoff automatically, the English authoring spec, relevant formal owners and the register's Purpose/Session State. Read the user-approved process revision before applying Q4/Q22/S24.2/S37.1/S38.1 to the new-repository and delivery boundary; the later revision controls category/stage/Contract ordering, while topic decisions and module sections control actual behavior. Compare the source snapshot with the preceding handoff and record any change affecting interpretation.

Resolve supersession at clause level. A later decision replaces the meaning it addresses, not every surviving clause in the earlier record. An ACCEPTED label cannot restore obsolete confirmation, targeting, recovery or scoring behavior. REJECTED branches are exclusion evidence; DEFERRED capabilities retain their named boundary. Removed identifiers are historical links, not requirements to reconstruct deleted mechanisms. Preserve original Q/S identifiers in mappings instead of renumbering them.

Keep one normative owner for each design fact. A change explanation should identify the affected behavior or invariant, its source/decision, the owner being changed, dependent references, acceptance consequences and actual status implications. Correct downstream wording to match the owner; do not copy a new independent definition into Product, Architecture, Acceptance, implementation and tests. Before detailed Contracts exist, retain the controlling Grill references and explicitly pending representation. After they exist, use their stable IDs while preserving design provenance.

The nine original Grill records and Chinese authoring reference remain unchanged. The English authoring spec is updated for explicit user-approved process changes with provenance and scoped precedence. Preserve W1–W4 historical handoffs; the earlier process revision updated the W5 next-task entry while retaining its original delivery and check facts. The current milestone refinement preserves all W1–W5 handoffs unchanged. S25.1/S26.1 and S27.1/S28.1/S29.1/S29.2/S30.1 describe source organization and maintenance history; they do not authorize another cleanup or create product features. Later accepted changes need explicit traceable decisions and consistent formal writeback, not retrospective alteration of the input snapshot to hide an earlier contradiction.

Under the clean-slate decision, old APIs, schemas, tests, fixtures and completion claims impose no mandatory compatibility, dual-running, migration or mapped-successor obligation. Optional old-data import is separate scope. New-system immutable history and exact references still require correct original interpretation: do not redirect historical references to latest, rewrite old payloads, or confuse logical deletion/current eligibility with historical readability. Original readers and future evolution detail belong to the relevant Contracts; the rebuild does not erase those obligations.

**Sources:** Q4, Q12–Q13, Q18, Q26, Q32, Q75, Q79, Q86–Q87, Q108, Q114, S24.2, S25.1, S26.1, S27.1, S28.1, S29.1–S29.2, S30.1, S37.1, S38.1; Architecture 3.2/17; Acceptance 4.2/14.

### 3.1 Git commit message format

Use the following commit message format:

```text
<type>(<scope>): <subject>
```

The scope is optional. When omitted, omit the parentheses as well:

```text
<type>: <subject>
```

The scope identifies the area affected by the commit, such as the data, controller or view layer, or another area appropriate to this project. For changes affecting multiple scopes, `*` may be used as the scope; a scope is not required for every commit.

```text
docs(development): document commit message format
docs: update documentation
refactor(*): align shared interfaces
```

**Source:** Explicit user instruction for Git commit messages.

## 4. Research and integration preparation

Research establishes evidence for a concrete consumer or integration boundary. A library's example fields, code layout, retry defaults or deployment claims cannot become JobHunter authority. Distinguish an accepted architectural direction, source evidence, verified behavior of a selected version, and an implementation result.

Use the [target technology stack](development/technology-stack.md) for the user's planned selections; verify concrete versions and integration behavior when the consuming milestone adopts them. Target selection is not installation or compatibility evidence.

| Research subject | Required work before the related detailed design or integration claim | Authority retained by JobHunter |
| --- | --- | --- |
| BossHunter and boss-zhipin-scraper | Pin studied commits; inspect license and maintenance; inspect source identity, payloads, extraction/pagination, authentication, acquisition/application flow and risk behavior; inventory and map raw source through adapter to canonical consumers before detailed Job Contract review | Runtime-validated adapter output; minimal consumer-driven canonical data; no external field/state/token becoming Domain authority or automatic model input |
| Resume optimization/tailoring projects | Identify and pin actual research inputs; inspect relevant prompt, workflow, targeting, rewrite and interaction patterns, with license/maintenance and applicability evidence for any intended reuse | Saved Evidence grounding, no fabrication, exact references, current permission and actual Proposal confirmation; research does not restore an Advisor working draft |
| Channel verification and platform access | Establish what source observations or read-back can actually support a business event, and what authorized live checks require; keep illustrative quotas/delays distinct from verified source behavior and later policy | Technical action is not application success; shared persistent safety, exact execution approval and explicit refresh remain separate |
| LangGraph/Langfuse integration | Verify the actual selected versions, callback and explicit SDK coverage, pre-export masking/correlation, workers/evaluator execution, judge connections and deployment requirements relevant to the integration | Real Application/Harness semantics, local canonical commit/recovery/settlement, separate judge scope/cost, and admitted evidence |

Research notes must make the studied source/version, observed fact, proposed mapping/use, limits and unresolved questions recoverable. This is an evidence requirement, not a prescribed report schema or another top-level document category. The Eval research appendix records prior research and specifically requires rechecking selected deployed versions; it proves neither an installed platform nor working privacy defaults. NiceEval is an accepted source of Scenario design inspiration, not a required dependency.

Do not freeze access counts, cooldowns, budget constants, default enablement or field sets from examples. Do not bypass JobHunter admission because an upstream SDK retries automatically or exposes more data. Any reused module remains behind the owned adapter/port and its runtime validation; a research candidate does not settle a reuse decision. This W4 document records those obligations and makes no new external verification claim.

**Sources:** Q3, Q27, Q30–Q31, Q49–Q50, Q120–Q121, Q140, Q146, Q149, Q160, Q164, Q174–Q176, Q178, S7.1, S35.1; Architecture 2.2/4.3/15.5; Acceptance 3/7/12.

## 5. Future Slice planning and test-first work

### 5.1 Define a bounded, reviewable capability

Use the [Implementation Plan](plans/implementation-plan.md) and its linked Slice plans as the single planning authority for decomposition, scope, dependencies, required Contract portions and completion conditions. Development applies that plan; it does not repeat the current Slice count, allocations or dependency tables. Planning identifiers remain distinct from Q/S and normative Contract IDs.

Before development, the selected milestone's actually consumed normative Contract scope, necessary shared clauses and both sides of required interfaces must be complete and reviewed. Satisfy its actual research and upstream implementation prerequisites. Unrelated scopes may remain pending. Do not split atomic invariants, defer first-consumer safeguards or guess missing definitions in code or fixtures. Follow [Progress recording rules](progress/README.md#5-two-level-progress-and-scope-level-contract-readiness) to record readiness and evidence; a filename, planned component or written stub cannot establish it.

Create only the packages and files actually needed by the current milestone, following the user-approved [target repository organization and incremental creation principles](development/repository-structure.md); the target tree is not a directive to generate empty packages or placeholders.

Reconcile shared boundaries and changes with affected owners, prior consumers, tests/Eval and evidence. If Contract work reveals a dependency change, update Implementation Plan's owning entry before proceeding. Scope changes cannot create product prerequisites or new Domain authority through engineering convenience.

Apply Q18's smallest suitable mechanism: immutable versions for content history, append-only events for factual history, projections for derived views, policy versions for explainable decisions, bounded Run outcomes for computation, and a state machine only where genuine long-lived legal stages need one. Do not create a generic lifecycle framework or select final transition representations in advance of Contracts.

**Sources:** Q7, Q18, Q22, Q26, Q32, Q37, Q42, Q118–Q119, Q173, Q186, S24.2, S38.1; later user plan-first and milestone-readiness direction; Architecture 2–3; Acceptance 2/14. Concrete allocations and dependency categories belong to Implementation Plan.

### 5.2 Test-first delivery loop

1. Locate the reviewed macro Slice and selected internal milestone, its complete required Contract scope and relevant Acceptance scenarios. Confirm necessary upstream dependencies and cross-family references, then identify observable proof of behavior and prohibited effects. Return unresolved necessary definitions to that milestone's Contract work; do not start implementation by guessing them.
2. For future code changes, establish the relevant deterministic failing check or regression case before the implementation change. Use real Domain/Application/Repository/Harness boundaries where their behavior is under test, with controlled external adapters and reconstructible isolated state. A failing semantic example has a scoped reviewed expectation; it is not necessarily unique model text.
3. Implement against the owned boundary and completed definitions, preserving runtime enforcement independently of Eval or telemetry. Test helpers cannot fabricate consent, canonical success or cross-domain authority to make the scenario pass.
4. Run the affected deterministic, integration, interaction and semantic verification appropriate to the change. Inspect actual failure/concurrency/recovery evidence as required by Acceptance; a live-model success cannot replace transaction or permission checks. Record the real command/runner/configuration and outcome once those exist, including failed, incomplete or unexecuted checks.
5. Reconcile affected normative references, acceptance and required regression evidence; update the actual Progress/matrix rows and handoff. Claim only the behavior demonstrated by the resulting evidence, with remaining scope and blockers visible.

This is the operational expression of accepted TDD, Slice acceptance and traceability, not a preselected first Slice or repository bootstrap. No runner, package command, fixture directory or automation has been created by this document. Current document-only checks establish documentation integrity, not the failing/passing code-test cycle described here.

**Sources:** Q4, Q22, Q26, Q32, Q117, Q173, Q178–Q183, S37.1; Acceptance 2/12–14; Eval sections 16–17 and 29.

## 6. Verification discipline across implementation boundaries

The [Acceptance](acceptance.md) scenarios remain the proof authority. The routing below tells future tasks which existing proof obligations to carry into development; it does not replace their detailed expectations or reassign business ownership. Select relevant positive, negative, boundary, concurrent, failure, recovery and permission cases from the actual changed behavior.

| Changed boundary | Required verification focus and destination | Controlling decisions to preserve |
| --- | --- | --- |
| Jobs, observations and collection | Acceptance 3/7: ManualApplicationEntry isolation versus complete formal Job admission, metadata-supported collection admission, retained local data, exact-version collection admission versus independent view queries, source observation and safety | Q12–Q13, Q44, Q48–Q50, Q56, Q110, Q160–Q161; later clauses and [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1) and [CG02-BC1](design/contract/sl-01-m2-grill.md#cg02-bc1) override old admission/screening/cooldown meanings |
| Facts, Resume Save and history | Acceptance 4: import remains Draft, Save confirms, shared whole experiences, all-affected atomic propagation/rollback, direct-membership deletion, exact original readers and eligibility | Q66, Q70–Q75, Q79, Q86–Q87, Q108, Q113–Q114, Q118–Q119, Q151, Q153–Q154, Q163, Q166, S15.1 |
| Grounding and derived material | Acceptance 4.2–4.3/7: actual-dependency grounding differs from whole-baseline Fit; authority plus durable demanded intent, skip obsolete work, prevent stale publication, preserve historical artifacts | Q75–Q77, Q87, Q114, Q147, Q150–Q152, Q165 |
| Requirements and independent Fits | Acceptance 5: exact usable dependency, bounded parse/repair and owner cost, separate semantic Runs, two freezes, serialized targets, independent failures, scoped negatives and valid unscored results | Q19, Q35, Q40, Q72, Q82–Q83, Q110–Q117, Q121, Q142, Q144, Q168, Q171–Q172, S22.1 |
| Session, Advisor and confirmed mutation | Acceptance 6: real conversational provenance, distinct discussion/apply target, exact Proposal/impact, ended generating Run, Application confirmation, idempotent commit, independent narration, human versus dependency wait and deletion race | Q47, Q52, Q89, Q128, Q133–Q134, Q138–Q139, Q143, Q146, Q148–Q149, Q155–Q159, Q167 |
| Preparation, material, execution and events | Acceptance 7: mutable revision checks/reentry, actual viewed artifact/Greeting, snapshot versus separate approval, single-use consumption, minimal live checks, real event provenance and projected progress | Q7, Q16, Q25, Q30–Q31, Q37, Q42, Q150, Q157, Q160, Q162, Q164 |
| Shared Harness, Tools and Context | Acceptance 8: one business Provider boundary, typed action admission, pure reads, actual immutable Frames, lazy pinning versus eager exact inputs, protected-input overflow/revocation, bounded compaction/rescue | Q80, Q83, Q120–Q123, Q126, Q132, Q134–Q144, Q158, Q172, S7.1, S17.4, S22.1 |
| Budget, recovery and streaming | Acceptance 9: competing reservations, actual idempotent settlement, unknown exposure, durable dispatch/response/result fault boundaries, fencing and safe continuation, no hidden replay, transient streams versus actual commit | Q116, Q122, Q124–Q125, Q130, Q135–Q136, Q140–Q142, Q156 |
| Privacy, storage and retained sources | Acceptance 10: actual admitted/exported data, secrets exclusion, active recovery dependencies, truthful historical unavailability and distinct deletion effects | Q19, Q52, Q125, Q131–Q132, Q136, Q139, Q141, Q151, Q167, Q170, Q174, Q184 |
| Collaboration Memory | Acceptance 11: collaboration-only authority, separate learning/Recall/management, admitted sources, independent budget, forgetting/manual precedence, isolated failed ranges and deleted-source publication ban | Q127–Q133, Q137–Q139, Q145, Q169–Q170, Q187 |
| Eval and observations | [Eval acceptance](acceptance/evaluation.md): isolated real paths, exact fixtures, declared experiment scope, real confirmation, independent judges, scoped evidence and actual-output re-evaluation | Q173–Q187, S35.1 |

Use deterministic checks and controlled fault injection to prove runtime/transaction/permission behavior. Observe the actual effect, access, producing Frame, canonical mutation or durable boundary needed by the assertion. A returned success value, UI text, manifest of available data, graph checkpoint, hash or Langfuse span alone is insufficient. Keep a model's forbidden request that Runtime rejects distinct from an actual forbidden execution or exposure.

For semantic judgments, combine referential/structural checks with task-scoped human review or calibrated judges. A resolvable citation is not entailment; full admitted input is not proof of no semantic omission. Strong bounded MISSING claims retain Q82/Q83/Q115's inspection and reliability obligations, while Q117 still defers mandatory offline annotated ParserVersion certification. Do not replace UNKNOWN with a forced decision or valid unscored Analysis with zero/failure to satisfy a metric.

Future dependency, model, prompt, Context, Tool, policy or persistence changes must identify the affected exact-input and historical meanings, then recheck the relevant acceptance boundaries. The test expectation cannot preserve an obsolete behavior merely because an old implementation or fixture used it. Maintain genuine regression coverage under the retention and supersession rules in [Evaluation development and evidence](development/evaluation.md#5-privacy-regression-retention-and-re-evaluation).

**Sources:** Q4, Q18, Q26, Q32, Q82–Q83, Q115, Q117, Q168, Q173–Q180, S37.1; Acceptance 2–13 and the Harness modules' Verification implications.

## 7. Eval development and evidence reporting

<a id="71-real-paths-isolation-and-exact-experiments"></a>
<a id="72-scenario-integrity-and-evaluator-admission"></a>
<a id="73-findings-comparison-and-release-policy-boundary"></a>
<a id="74-privacy-regression-retention-and-re-evaluation"></a>

Apply the specialized [Evaluation development and evidence guide](development/evaluation.md) when the changed behavior requires Eval. It carries the real-path, isolation, Scenario, evaluator-admission, findings, privacy, retention and re-evaluation procedure previously held here, with its controlling Q/S references. Architecture retains runtime ownership and Acceptance retains required proof; the guide supplies no new release policy or completion claim.

## 8. Traceability, evidence, and actual progress

<a id="81-preserve-the-chain-without-inventing-completed-artifacts"></a>
<a id="82-status-requires-evidence"></a>
<a id="83-planned-unified-checks"></a>
<a id="84-two-level-progress-and-scope-level-contract-readiness"></a>

Follow [Progress recording rules](progress/README.md) for traceability, evidence-backed status, planned unified checks, separate parent/milestone records and scope-level Contract readiness. Update [actual Progress](progress.md) and its [matrix](progress/traceability.md) from real work and evidence. The rules and records remain in the Progress category; Development requires truthful reporting without maintaining a second status specification.

## 9. Cross-context handoffs and document review

### 9.1 Task entry and completion evidence

At task entry, use the [global index](index.md) and relevant directory README to locate the latest applicable handoff and actual governing documents, then read them automatically. Compare their scope and availability with repository state; a historical handoff may correctly say a document was absent at its own delivery point. Do not repeat a read-confirmation question. Recheck relevant controlling records and modules when a dependency, source snapshot or interpretation changed.

A handoff must identify the sources read and controlling Q-IDs; actual changed files/sections; owner/reference relationships; clause-level coverage, later replacements, exclusions and reasons; separately reported results of both seams; exact pending details and owners; real document/implementation/verification state; and next-task required reading. Include actual evidence locations when they exist, not invented future paths presented as completed artifacts.

Handoffs locate work and preserve context; the next task must reread actual files. Keep transient notes outside competing formal authority, and feed actual status/evidence into [Progress](progress.md). Report the scope of semantic and mechanical checks accurately. Do not call a planned test executed, a reviewed draft user-approved, an absent runner passed, or a local change committed/published without evidence.

**Sources:** Q22, Q26, Q32, S37.1, S38.1; English authoring spec, Further Notes C; automatic handoff reading is the user's explicit instruction.

### 9.2 Two separate verification seams

**Decision-to-Document Traceability Seam:** Resolve effective source clauses, controlling Q/S, partial supersession and source-module meaning. Locate actual formal destinations and acceptance counterparts; explain pending, excluded and historical-only content. Reverse-check every added rule for an accepted source or clearly identified authoring arrangement. A complete ID count does not prove clause-level interpretation. Maintain source provenance after Contract IDs arrive.

**Cross-Document Semantic Consistency Seam:** Compare actual documents along shared facts and references. Product behavior, Architecture owners, the actual Implementation Plan's Slice/dependency/required-scope mappings, planned/future Contract definitions, Acceptance expectations, Development discipline and Progress evidence must agree. Check current versus historical inputs, authority versus derived results, exact versions, consent and scope, waits, actual outcomes and claimed proof. Repeating a fact cannot create a conflicting authority. Planned paths must not look like already available normative sources.

Use the authoring spec's 29 semantic regression topics and the actual [W3 mapping](../.scratch/w3-acceptance-handoff.md) as locators, not substitutes for source review. In particular, fixtures/engineering shortcuts must not restore old screening dependencies, immediate-formal import, completeness confirmation, private Resume facts, Advisor drafts, implicit apply targets, joint Fits, latest-intent arbitration, overflow fallback, hidden dependency reads, coupled Memory controls, unknown replay, renewed allowances, eager all-format derivatives, reduced-scope continuation after revocation, merged approvals, cooldown-only restoration or Eval-owned business success.

Report each seam's findings, scope and remaining issues separately. Neither substitutes for the other or for runtime acceptance. Planning review applies both seams to actual source/owner mappings. Joint baseline review includes the main documents, linked Slice plans, Contract Structure, specialized Eval acceptance and execution guides, Progress recording rules and actual matrix, then presents the concrete result for user review. Check capability-to-Slice-to-required-Contract-to-acceptance coverage and consistency of milestone readiness and parent Slice completion. After each Contract scope is completed or changed, reconcile affected documents, dependencies, acceptance and progress before the relevant development; an earlier review cannot excuse a later conflict.

**Sources:** Q22, Q26, Q32, Q56, Q70–Q74, Q108, Q112–Q116, Q123, Q132, Q135, Q139–Q144, Q146–Q152, Q158, Q160, Q165, Q169–Q175, S24.2, S37.1, S38.1; both named seams were confirmed by the user.

## 10. Remaining decisions and next stage

Use [Architecture 17](architecture.md#17-deferred-detail-exclusions-and-handoff-boundaries) and [Acceptance 14.1](acceptance.md#141-requirements-preserved-while-details-remain-pending) for pending-detail owners and exclusions. [Implementation Plan](plans/implementation-plan.md) locates the selected scope and dependencies; [Progress](progress.md) records actual review/readiness, gaps and next work. Development does not maintain a parallel milestone list, Contract catalog or implementation snapshot.

Resolve only the definitions and research actually needed for the selected scope, preserving the governing invariants and explicit deferrals. The specialized [Eval guide](development/evaluation.md) preserves the distinction between required runtime/semantic proof and deferred rollout policy. Documentation or framework setup cannot establish Contract readiness, accepted capability or executed verification; record actual evidence under [Progress rules](progress/README.md).

**Sources:** Q2–Q5, Q11, Q13, Q18, Q22, Q26–Q27, Q32, Q81, Q109, Q117, Q121, Q123, Q175, S7.1, S24.1–S24.2, S35.1, S37.1, S38.1. The current user instruction relocates specialized procedure and reporting without changing these decisions.
