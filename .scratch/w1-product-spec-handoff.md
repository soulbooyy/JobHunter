# W1 Product Spec — Authoring Handoff

> English authoring notes only. This file records the W1 task and review scope; it is not another formal document category, a normative Contract, a product requirement source, or a substitute for the later Progress traceability matrix.

## Deliverable and actual state

W1 authored [docs/spec.md](../docs/spec.md) from the [English authoritative authoring spec](document-authoring-spec.en.md). The product document describes target behavior and explicitly identifies itself as a draft awaiting joint review. No product implementation, executable tests, detailed Contracts, or user review approval is claimed.

At this handoff, the other four main documents, `docs/contracts/*`, and the Progress supporting matrix have not been authored. W2 is next. W6's joint review and the subsequent user review remain pending. This task did not modify the nine Grill records or either authoring-spec edition.

## Sources consulted and reading scope

- English authoring spec: document ownership, Implementation Decisions, both verification seams, the semantic regression checklist, W1–W6 responsibilities, coverage index, and pending-detail boundaries.
- [Decision Register](../docs/design/grill-me-design-tree.md): Purpose/Session State; Q4/Q22/S24.2/S37.1/S38.1; W1 topic records for navigation, assets, Jobs, Fit, Advisor, preparation, execution/tracking, privacy, Memory, and their later corrections. Earlier clauses were checked against the controlling decisions listed below, rather than accepted by status alone.
- [Memory](../docs/design/harness/memory.md): complete module, including independent controls, source admission, forgetting, failed ranges, deleted-source behavior, and future-Skill exclusions.
- [Context](../docs/design/harness/context.md): source/control/acquisition, entry and page boundaries, exact lazy reads, foreground serialization, human versus dependency waits, Session deletion, protected inputs, oversized Fit, score availability, revocation, and dynamic Memory sections.
- [Tool Actions](../docs/design/harness/tool.md): action purity/permission, dependency preparation, exact reads, target-specific Proposal and confirmation, material approval, deletion, derived work, and platform boundaries.
- [Recovery](../docs/design/harness/recovery.md): durable remote-call and streaming boundaries, allowed local recovery, explicit Retry, per-target serialization, and shared parse ownership.
- [Budget](../docs/design/harness/budget.md): unknown usage, exhaustion/partial success, and Context-capacity boundaries.
- [Storage](../docs/design/harness/storage.md): independent retention, durable derived-work intent, stale-artifact publication, and honest interpretation after purge.
- [Agent Evaluation](../docs/design/eval/agent-evaluation.md): status/precedence and sections 18–20 on reliability, distinct evidence, and deferred release policy; the authoring spec supplies the wider W2/W3 Eval agenda.
- [Contract Design Inventory](../docs/design/contract/contract-design-inventory.md): purpose, reading rules, and controlling-change notice only. It was not used to generate schemas or fill unspecified product behavior.

Consulting selected sections is not a claim to have revalidated every architectural clause of all nine modules in W1. W2 requires all nine records; W6 checks complete cross-document coverage.

## Section-to-decision handoff

Product sections are the visible-behavior destinations. W2 owns supporting architecture explanations and future Contract responsibility planning; W3 owns acceptance scenarios. References below are source decision IDs, not newly assigned normative Contract IDs.

| Product section | Effective decision and controlling sources | Boundary handed to subsequent work |
| --- | --- | --- |
| 1 | Clean slate, six document categories, documentation-first review: Q2–Q6, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1 | W2/W4 explain design and delivery sequence; W5 owns actual status and matrix; language rule is user instruction |
| 2.1–2.2 | Independent tasks and five entries: Q1, Q6, Q8, Q16, Q23–Q24, Q53, S5.1, S5.3, S17.1–S17.4 | Navigation is not Aggregate ownership; no extra preparation/pursuit/assistant entry |
| 3.1 | Shared experience facts, one temporal current version: Q15, Q54, Q63, Q66, Q75, Q79, Q98, Q108, S15.1 | W2 owns exact reference/history mechanisms; typed payloads and reference validation await Contracts |
| 3.2 | Draft before formal Save, user-confirmed facts, no completeness Gate: Q64, Q70–Q74, Q98, Q108, Q113, Q118, Q146, Q166 | Atomic write/reconciliation protocols await Architecture/Contracts; no current implementation claim |
| 3.3 | Shared body edits, all-affected atomic propagation, whole experiences: Q96–Q98, Q108, Q114, Q118–Q119, Q153, Q163 | Preserve Profile display choices; no per-Resume bullet graph or recursive fact versioning |
| 3.4 | Default and logical Resume removal: Q88, Q93, Q100 | Last-Resume constraint is independent of permitted empty content |
| 3.4 | Knowledge-only global deletion and task-specific missing input: Q151, Q153–Q154 | Direct membership determines impact; no sentence graph, universal Profile Gate, or mandatory count |
| 3.5 | Actual-dependency grounding versus whole-baseline Candidate Fit: Q75–Q77, Q87, Q108, Q114, Q118–Q119 | W2 explains durable derived identity; historical readability is not current-use eligibility |
| 3.5, 7.2 | Demand-driven artifacts and stale-work rules: Q147, Q150–Q152, Q165 | W2 owns authority-plus-intent transaction/recovery; exact formats and work representation remain pending |
| 4.1 | Source identity, Manual root without JD, complete BOSS admission: Q12–Q13, Q17, Q44, Q48–Q49, S9.1 | Reject merging; one JobVersion meaning despite source-specific admission |
| 4.2–4.3 | Hard global Preferences, metadata-only screening, explicit collection: Q45, Q49, Q55–Q56, Q110, Q161, S9.1, S17.1 | No Requirement parsing on collection, default preferences, or hidden refresh |
| 4.4 | Content version, observation, availability, and readiness differ: Q7, Q44, Q48, Q50 | W2 applies Q18's minimal evolution mechanisms; no universal lifecycle |
| 5.1 | Shared bounded parse, immutable reusable Set, no usable target failure: Q10, Q14, Q58–Q59, Q110–Q111, Q117, Q142, Q144, Q159, Q171 | W2 owns producer claim and owner-only cost; exact parse/validation outputs await Contracts |
| 5.2 | Independent Candidate and Resume Fit, separate selection/defaults/results: Q19, Q24, Q35, Q112, Q115, S5.3, S22.1 | Resume sees no unexpressed Knowledge; no Coverage authority or score ordering |
| 5.3 | Scoped assessment vocabulary, deterministic scores, unscored success: Q46, Q51, Q72, Q82–Q83, Q112–Q115, Q168 | Accepted meanings are not a new enum schema; score weights/availability thresholds remain pending |
| 5.4 | Two freeze points, single active target, independent partial success: Q35, Q40, Q76, Q108, Q110, Q113, Q116, Q121–Q124 | W2 owns exact target keys, budget, fencing, and final publication checks |
| 5.4, 9.1 | Full Context limits and protected-input revocation: Q121, Q123, Q135, Q172, S24.1 | No lossy fallback or scope shrink; new configuration/scope means new task |
| 6.1 | Unified Advisor Session, lazy reads, no Fit prerequisite, source distinction: Q24, Q41, Q47, Q52, Q58, Q85, Q88–Q89, Q93–Q94, Q128, Q133, Q138–Q139, Q143, S17.3 | W2 explains Package/Frame and pinned acquisition, not a new Session type |
| 6.2 | Current-instruction/default apply target, concrete preview, one confirmation: Q96, Q108, Q113–Q114, Q118–Q119, Q128, Q133, Q146, Q148–Q149 | Target-specific patch; no suggestion-source state, Advisor draft, or second Save |
| 6.2–6.3 | End generating Run, persist mutation outcome, bounded dependency wait: Q142, Q144, Q155–Q159 | No model consent interpretation, suspended confirmation Run, duplicate commit, or dependency takeover |
| 6.3, 10.3 | Session-delete races and source deletion: Q52, Q131, Q167, Q170 | Pending actions/learning are revoked; committed facts and existing Memory have independent lifecycles |
| 7.1 | Mutable Preparation, explicit narrow return, idempotent reentry: Q16, Q25, Q30, Q36, Q42, Q91, Q108, Q118, Q146, Q162 | W2 owns revision checks; selected exact materials/Greeting are preserved |
| 7.2 | Viewed artifact approval and fixed generic Greeting: Q42, Q77, Q108, Q118, Q150, Q152, Q157 | Render before confirmation; changed Greeting reconfirms; no personalized generation |
| 8.1 | Snapshot/material confirmation/execution approval/Attempt distinctions: Q25, Q30–Q31, Q77, Q150, Q157, Q164 | W2/Contracts own approval/attempt representation; live checks cannot silently refresh authority |
| 8.2 | Per-Job batch isolation and shared persistent platform safety: Q36, Q49, Q160–Q161, Q164 | Capacity/risk sharing does not merge lifecycle, budget, or authorization; no frozen quota numbers |
| 8.3 | Verified or human-reported business events; projected progress: Q7, Q16–Q17, Q21, Q30–Q31, Q37, Q44, Q48 | Technical action is not success; channel proof and event representations remain pending |
| 9.1–9.3 | Minimum visibility, typed permission, honest recovery/retention: Q19, Q47, Q52, Q54, Q72, Q82–Q83, Q94, Q116, Q120–Q128, Q131–Q132, Q135–Q144, Q147, Q152, Q156, Q165, Q172 | W2 owns runtime/storage mechanisms; no live code, retention constants, or runtime transition table is specified |
| 10.1–10.3 | Collaboration-only Memory, independent controls, conservative learning/forgetting: Q127–Q133, Q137–Q139, Q141, Q145, Q155–Q156, Q169–Q170 | W2 owns policies and background execution; field representation, cadence, amounts, and markers remain pending |
| 11 | Evidence-scoped quality claims, business versus evaluation authority: Q82, Q117, Q168, Q173–Q180, Q184–Q186, S17.1, S35.1 | Full Eval design belongs to W2/W3; rollout remains deferred under Q175 |
| 12 | Non-goals and pending detail with source-specific reasons | Later tasks preserve these dispositions; deferral is not missing implementation or a new architecture question |

### Source-index coverage dispositions

The authoring spec's coverage-index rows naming Product as a consumer contain 135 existing Q/S records. Product sections carry direct references to 133 of those records, including bounded ranges. The other two are explicitly assigned rather than silently omitted:

- **Q18:** its product consequence is the separation of eligibility, readiness, and event-derived progress in sections 4.4 and 8.3. The minimal evolution-mechanism review and rejection of a generic lifecycle framework belong to W2/W4 and later Contracts.
- **S7.1:** independent interaction policies are reflected in sections 2, 5, and 6. Shared Harness infrastructure/static Skill decomposition and upstream resume-optimization research belong to W2/W4; Q120/Q121 and S17.4 control the actual Skill boundaries. No product-specific duplicate Advisor is introduced.

This record-level comparison is a mechanical coverage check, not proof of clause-level completeness. Section semantics and the following supersession checks provide the interpretation evidence. W2/W3 still need architectural and acceptance coverage for sources whose W1 treatment is only a visible consequence.

## Clause-level supersession and semantic regression review

The authoring spec's 29 regression topics were reviewed for W1 disposition. “Covered” below means the product prose expresses the effective behavior, not that a product test exists or passed.

| Earlier mechanism or risk | Effective controlling decision | W1 disposition |
| --- | --- | --- |
| RequirementSet/ScreeningProfileSnapshot in QuickScreen | Q56, Q110 | Covered in 4.2–4.3; Q8/Q10 survive only for distinct assets/reusable requirements |
| Incomplete BOSS Job persisted like Manual | Q44, Q48–Q49, S9.1 | Covered in 4.1; Q17's tracking allowance survives without an immediate version |
| Import immediately creates formal Resume | Q70–Q74 | Covered in 3.2; shared ownership from Q63 remains |
| KnowledgeConfirmation survives inside ACCEPTED records | Q113 | Removed as an active rule throughout; explicitly excluded in 3.2 and 12.1 |
| Private Resume facts, free historical choice, per-bullet selection | Q63, Q108, Q163 | Covered in 3.1/3.3; Q109 rejected branch excluded in 12.1 |
| Manual refresh or GroundingSet-only rescue of changed facts | Q108, Q114, Q118–Q119 | Covered in 3.3/3.5; actual-dependency grounding survives |
| Advisor persistent working draft/export | Q146, Q148–Q149 | Covered in 6.2; earlier Q41/Q85/Q94/Q108/Q138 draft clauses are historical only |
| Discussion or Preparation implicitly determines apply target | Q146, Q149 | Discussion priority in 6.1; distinct current-instruction/default apply rule in 6.2 |
| Apply skips preview or old Run waits for confirmation | Q146, Q148, Q158 | Covered in 6.2; Q133 conversational use and Q134 append-only lineage remain, not their superseded flow interpretation |
| Removing one Resume experience deletes shared Evidence | Q151, Q153 | Covered in 3.4; only Knowledge management initiates global deletion |
| Editor crash checkpoint or Advisor draft recovery | Q146, Q166–Q167 | Covered in 3.2/6.2/6.3; pending Proposal persists but cannot survive Session deletion as an eligible action |
| Joint dual-axis DeepFit/Coverage/ordered scores | Q112, Q115, S22.1 | Covered in 5.2–5.3; assessments and scores remain independent |
| Empty Requirements yield perfect score; unavailable score means zero/failure | Q168, Q171 | Covered separately in 5.1 and 5.3 |
| Latest-intent arbitration of overlapping same-target analyses | Q116 | Covered in 5.4; one active target and latest compatible success |
| Full Context overflow silently truncates, switches model, or invokes RAG | Q121, Q123, Q132, S24.1 | Covered in 5.4/9.3; explicit supported configuration selection remains allowed |
| All available data enters model by default or follows latest | Q83, Q94, Q139, Q143 | Covered in 6.1/9.1; W2 explains exact acquisition/Frames |
| Read secretly parses missing Requirements | Q142, Q144, Q159 | Covered in 5.1/6.3/9.1; independent visible preparation and owner-only charges |
| Memory owns compaction or has one combined off switch | Q132, Q139 | Covered in 9.3/10.2; Session and Memory remain separate |
| Failed learning ranges silently recur or deleted sources publish | Q169–Q170 | Covered in 10.3; explicit old-range Retry and publication prevention |
| Unknown calls replay or SDK hides retries | Q122, Q135, Q140 | Covered in 9.2; uncertainty/cost survive Retry |
| Loop steps replenish auxiliary allowances | Q121, Q135 | Product bounded-work obligation in 5.4/9.2; exact cumulative runtime allowances belong to W2, not a new product configuration |
| Eagerly render every format or retry external actions as derivatives | Q147, Q152, Q165 | Covered in 3.5/9.2; demand and safe-work scope retained |
| Remove revoked exact input and continue same Fit | Q172 | Covered in 5.4/9.1; new admitted scope needs new task |
| Resume selection or MaterialApproval authorizes execution | Q30, Q150, Q157 | Covered in 7.2/8.1; actual viewed material and separate execution approval |
| Cooldown alone restores strong risk or live checks refresh JD | Q160, Q164 | Covered in 8.1–8.2; ordinary workflow failures remain distinct from account risk |
| Langfuse/judges decide business success | Q174, Q176, Q184 | Product authority boundary in 11; detailed platform/judge ownership goes to W2/W3 |
| Unique golden text, replayed N+1 history, Dataset/control leakage | Q178, Q180, Q183, Q185 | Eval mechanics go to W2/W3; no such product requirements added. Section 11 limits quality claims without inventing an Eval UI |
| Trial counts/universal release gate already settled | Q175 | Explicitly deferred in 11/12; Q117 parser certification remains deferred |
| Legacy order/status constrains new repository | Q4, Q22, S37.1, S38.1 | Section 1 and this handoff distinguish target, authored draft, review, and implementation |

## Verification seam results

### Decision-to-Document Traceability Seam

W1 review found no unresolved contradiction in the product clauses written. Each product section records effective source IDs, with explicit later controlling decisions at the major supersession boundaries. The section mapping and regression table record surviving, replaced, excluded, and deferred meanings. Mechanical checks cover existing Q/S identifiers, coverage-index dispositions, local links, section/table structure, and unchanged source files. Those checks do not substitute for semantic review.

Scope is W1 product behavior only. This is not a full 179-record formal Traceability Matrix or a claim that Architecture, Acceptance, detailed Contracts, implementation, or tests are complete. Exact destinations and acceptance/evidence mappings remain future work.

### Cross-Document Semantic Consistency Seam

Preliminary W1 review checked internal consistency and alignment with the English authoring spec and relevant Grill module semantics: fact versus derived authority, current versus historical use, discussion versus apply target, Session versus Memory, materials versus execution approval, technical versus business events, and design versus actual status.

Full formal cross-document verification is **pending**: Architecture, Acceptance, Development, Progress, and Contracts do not yet exist. W2 must compare its explanation against this product draft, W3 must compare acceptance against both, and W6 must perform the joint main-document review. No “all documents consistent” pass is claimed. The Chinese authoring reference was preserved and is not a competing authority.

## Pending details and W2 entry instructions

Read the actual English authoring spec, the full Product Spec, and all nine design records. Start with register Purpose/Session State and Q4/Q22/S24.2/S37.1/S38.1. Recheck later corrections at clause level; this handoff is a locator, not a replacement for sources.

W2 should explain, without freezing fields or transitions:

1. Business authorities, immutable roots/versions/derived assets, current-use eligibility, dependency directions, and source/reference readers for new-system history.
2. Atomic authority changes, all-affected Resume propagation, direct-membership deletion, revision conflicts, durable derivative intent, and current-artifact publication.
3. Shared parsing, two input-freeze points, independent Fit targets/results, Application orchestration, single-flight/cancellation/cost ownership, and full-input admission.
4. One shared Harness with separate static Skills; Runtime/Invocation/Tool/Context/Budget/Recovery/Storage responsibilities and exact recorded inputs.
5. Advisor Proposal target/preview/confirmation, ended generating Run, Session deletion races, exact mutation results, and explicit narrow return to Preparation.
6. Material/readiness versus execution permission, platform safety versus workflow ownership, verified business events, and projected progress.
7. Independent Context and Memory mechanisms; learning/Recall/management, source minimization, forgetting, older-candidate conflicts, failed ranges, and deleted sources.
8. Full Eval/observability responsibilities and evidence boundaries from Q173–Q187, including topics deliberately left out of product prose.
9. Candidate Contract document families, their owners/exclusions/reference directions, and exact questions awaiting Contract Grill. No Contract bodies or fixed file count.

Product section 12.2 carries the detailed pending-topic categories: per-function inputs, exact references and interfaces, score policy, Proposal/approval lifetime representation, render/channel proofs, tool catalog, privacy/redaction, budgets, Context/Memory triggers, retention/cleanup, source research, and later rollout policy. Keep those pending rather than supplying defaults.

If W2 reveals a real ownership or wording inconsistency, correct this W1 draft with controlling-source references. Do not introduce new architecture decisions to make the documents agree. Preserve source files and do not mark user review or implementation complete from file existence.
