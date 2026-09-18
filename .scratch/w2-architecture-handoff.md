# W2 Architecture Handoff

> English is authoritative. This is a task handoff and review record, not another normative product or architecture authority. Subsequent stages automatically read the preceding handoff, actual available documents, governing authoring spec, and relevant original decisions; no separate user confirmation to read the handoff is needed.

## Delivered scope and actual state

W2 authored [Architecture](../docs/architecture.md) under the [English document-authoring spec](document-authoring-spec.en.md), starting from the [W1 handoff](w1-product-spec-handoff.md) and actual [Product Specification](../docs/spec.md). Architecture describes target responsibilities and mechanisms, including future Contract structure, responsibilities, and reference boundaries. Both formal documents remain drafts awaiting W6 joint review and subsequent user review.

W2 also updated Product sections 1 and 12.2 to link the now-authored Architecture draft and accurately describe document availability. No product behavior changed. The W1 handoff remains an unchanged historical account of its delivery point; its then-pending Architecture status is not the current status.

Acceptance, Development, Progress, its supporting matrix, and detailed Contracts have not been authored. No product code, executable tests, implemented feature, deployed Eval service, passed acceptance, or user review approval is claimed. No Contract files were created. The nine original Grill records and both authoring-spec editions remain unchanged. This work has not been committed.

## Sources and interpretation

W2 considered all nine source records, including the full Harness and Eval design, their later corrections, verification implications, and pending-detail boundaries. The English authoring spec and full Product draft supplied the document-ownership and cross-document comparison baseline. The W1 handoff was used as a locator, not a substitute for actual documents or decisions.

| Source | Reading and control used in W2 |
| --- | --- |
| [Decision Register](../docs/design/grill-me-design-tree.md) | Purpose/Session State, all topic groups in the coverage index, stage rules Q4/Q22/S24.2/S37.1/S38.1, clause-level later corrections, Q173–Q187, and source-maintenance supplements |
| [Tool Actions](../docs/design/harness/tool.md) | Application actions, permission intersections, pure reads/Ensure, Proposal confirmation, source refs, external access and replay |
| [Context](../docs/design/harness/context.md) | Protected control, exact acquisition, Package/Frame, compaction ordering and publication, dynamic Recall, bounded rescue, revocation |
| [Memory](../docs/design/harness/memory.md) | Authority rules, independent controls, admitted types/sources, background ownership, conservative learning, non-resurrection and source deletion |
| [Budget](../docs/design/harness/budget.md) | Operation/Run/background owners, atomic admission and reservation, local/total ceilings, settlement, unknown exposure, foreground capacity |
| [Recovery](../docs/design/harness/recovery.md) | Durable intent/response/result, fencing, startup, action-specific replay, stream presentation, safe derivatives and independent committed effects |
| [Storage](../docs/design/harness/storage.md) | Four responsibilities, active recovery retention, historical availability, sensitive transport exclusions, deletion distinctions |
| [Agent Evaluation](../docs/design/eval/agent-evaluation.md) | Complete task/platform responsibilities and Q173–Q187: exact isolated trials, fixed Scenarios, scoped evidence, coherent N+1, per-check outcomes, regression retention, re-evaluation and independent judges |
| [Contract Design Inventory](../docs/design/contract/contract-design-inventory.md) | Candidate responsibility/dependency checklist only; conceptual rows, example layouts, fields, status names and operational examples did not become normative Contracts |

Later controlling clauses prevail over earlier ACCEPTED wording. For example, the inventory's integration-row wording about Collector/Executor being disabled by default is not sufficient to establish a default-enablement decision: the original source does not settle that default, and Q175 leaves rollout/default enablement for later work. Architecture sections 2.2, 15.4 and 17 keep examples, research obligations, and pending rollout separate. No new default was selected.

## Section-to-decision and ownership map

Architecture section numbers below locate the actual prose. Product remains the authority for visible tasks/behavior; Architecture explains the supporting invariants. Future detailed Contracts own representation, Acceptance owns required proof, Development owns delivery discipline, and Progress owns actual status. References are Grill identifiers, not invented Contract IDs.

| Architecture destination | Effective meaning and controlling sources | Cross-document responsibility |
| --- | --- | --- |
| 1; 16.1; 17 | Clean slate, documentation-first review and exact ownership: Q2–Q5, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1 | Product 1; future Development/Progress; no old compatibility or completion claims |
| 2.1; 3.1 | Local single user, navigation/read views versus owners: Q1, Q6, Q53, S5.1, S17.2–S17.4 | Product 2 owns five entries/two Advisor entry modes; no new Aggregate or UI entry |
| 2.2 | Minimal canonical consumers, validated adapters, pinned research obligations: Q3, Q27, Q31, Q49, S7.1 | Future source/channel Contracts and Development; no verified-upstream or default rollout claim |
| 3.1–3.2 | Independent authorities, minimal evolution mechanisms, exact historical readers: Q7–Q8, Q10, Q15–Q16, Q18, Q21, Q25, Q30–Q31, Q37, Q42, Q46, Q51, Q54–Q55, Q59, Q63, Q66, Q75, Q79, Q86–Q87, Q98, Q108, Q112–Q113 | Product 3–8; exact syntax/types/errors and evolution details await Contracts |
| 4.1 | Source identity, Manual root-only admission, complete BOSS admission: Q12–Q13, Q17, Q44, Q48–Q50, S9.1 | Product 4.1; Q13 supplies exclusion evidence, not merge permission |
| 4.2 | Metadata-only hard screening, exact collection Preferences, latest local views, retained partial successes: Q45, Q49, Q55–Q56, Q110, Q161, S9.1, S17.1 | Product 4.2–4.3; no parse during collection or rejected-content persistence |
| 4.3; 8 | Observations versus content, shared safety versus authorization: Q36, Q49–Q50, Q160–Q161, Q164 | Product 4.4/8; no mandatory Monitor, cooldown bypass, or numeric quota |
| 5.1 | Deterministic import/Draft, saved authority, no completeness confirmation: Q15, Q63–Q64, Q70–Q75, Q85, Q96, Q98, Q108, Q113, Q146, Q166, S15.1 | Product 3.1–3.2; unsaved page state is not model input or crash-recoverable authority |
| 5.2 | All-affected atomic Save, shared body facts, separate Profile/presentation changes: Q73, Q96–Q98, Q108, Q114, Q118–Q119, Q147, Q152, Q163 | Product 3.3; transaction detail awaits Contracts; no asynchronous authority propagation |
| 5.3 | Defaults, logical Resume removal, Knowledge-only global deletion, empty saved state: Q88, Q93, Q100, Q108, Q151, Q153–Q154 | Product 3.4; direct membership, task-specific prerequisites, no sentence dependency graph |
| 5.4 | Actual-dependency grounding versus complete-baseline Candidate Fit; demand-driven derivatives: Q75–Q77, Q87, Q108, Q114, Q118–Q119, Q147, Q150–Q152, Q165 | Product 3.5/7.2/9.2; safe derived recovery does not authorize remote replay |
| 6.1 | Independent immutable Requirements, bounded parse, usable-target validation, database single-flight/owner cost: Q10, Q14, Q24, Q58–Q59, Q110–Q111, Q117, Q121, Q142, Q144, Q171 | Product 5.1/6.3; detailed dependency and parser outputs await Contracts |
| 6.2 | Independent Fits, scoped MISSING/UNKNOWN, actual Frame completeness, unscored success: Q19, Q46, Q51, Q72, Q76, Q82–Q83, Q108, Q112–Q115, Q121, Q168, S22.1 | Product 5.2–5.3; no cross-supplementation, Coverage, score gap or fixed formula |
| 6.3 | Two freezes, separate targets/results, compatible success, revocation: Q23, Q35, Q40, Q110, Q112, Q116, Q122–Q124, Q142, Q172, S5.3, S22.1 | Product 5.4; W3 proves independent failure/concurrency; detailed target keys await Contracts |
| 7.1 | Unified durable Session, explicit source provenance, lazy pinning, foreground serialization: Q41, Q47, Q52, Q85, Q88–Q89, Q93–Q94, Q128, Q133–Q134, Q138–Q139, Q143, Q155, S17.3 | Product 6.1; Session claims can support discussion without becoming saved facts |
| 7.2–7.3 | Current-instruction/default apply target, concrete Proposal, completed generation, Application confirmation, exact result and deletion arbitration: Q91, Q96, Q108, Q113–Q114, Q118–Q119, Q128, Q133–Q134, Q142, Q144, Q146, Q148–Q149, Q155–Q159, Q167, Q170 | Product 6.2–6.3; no suspended generating Run; later narration uses actual commit |
| 8 | Mutable/idempotent Preparation, viewed material/Greeting, separate execution approval, real events/projected progress: Q7, Q16–Q17, Q21, Q25, Q30–Q31, Q36–Q37, Q42, Q77, Q91, Q108, Q146, Q150, Q157, Q160, Q162, Q164 | Product 7–8; execution checks cannot refresh frozen business inputs |
| 9 | Static independent Skills/shared Harness, unique business invocation boundary, typed/pure actions: Q47, Q120–Q122, Q126–Q128, Q132, Q135, Q138–Q144, Q155, Q176, S7.1, S17.4, S22.1 | Product 9.1; Contracts later define full catalog; Judge has separate Eval ownership |
| 10 | Eager/lazy acquisition, Package/Frame, protected exact inputs, ordered bounded compaction, honest retained sources: Q19, Q72, Q80, Q83, Q94, Q121–Q125, Q132, Q134–Q136, Q138–Q140, Q143, Q146, Q158, Q172 | Product 9.1/9.3; no hidden RAG, automatic model switch, or regenerated old payload |
| 11 | Shared mechanism/distinct budget owners, atomic reservations, known/unknown settlement, local and whole-Run ceilings: Q35, Q110–Q112, Q121–Q124, Q130, Q132, Q135, Q140, Q142, Q144, Q155, Q158–Q160, Q169–Q172, Q176 | Product 5.4/9.2/10.3; concrete policies and amounts await later work |
| 12 | Durable dispatch/response/result, owner fencing, safe continuation, no unknown replay, commit survives narration: Q30–Q31, Q40, Q116, Q122, Q124–Q126, Q135–Q136, Q140–Q142, Q146–Q149, Q152, Q155–Q156, Q158, Q165–Q167, Q172 | Product 6.2–6.3/9.2; bounded invariants, not a finalized lifecycle table |
| 13 | Four storage responsibilities, active retention versus history, secrets exclusion, distinct deletion effects: Q52, Q75, Q100, Q125, Q131–Q132, Q136, Q139, Q141, Q146–Q152, Q156–Q162, Q165–Q172, Q174 | Product 9.1–9.3; no four-database prescription, indefinite payload guarantee or physical layout |
| 14 | Collaboration-only Memory, three independent controls, admitted sources, background ownership, non-resurrection: Q127–Q133, Q137, Q139, Q141, Q145, Q155–Q156, Q169–Q170 | Product 10; Context remains independent; detailed markers/triggers remain pending |
| 15.1–15.2 | Thin real-path Eval, independent judges, exact isolated fixtures/configuration, scoped evidence and control separation: Q117, Q173–Q177, Q184–Q185, S35.1 | Product 11; W3 owns proof expectations; no judge or telemetry business authority |
| 15.3 | Authored next-turn/full Scenarios, coherent restore, actual Proposal confirmation, experiment scope and controlled Memory: Q158, Q173, Q177–Q178, Q180, Q183, Q186–Q187 | W3 must distinguish observed stages from unexecuted capabilities |
| 15.4 | Per-check completeness, valid semantic alternatives, regression retention, actual-output re-evaluation, pending rollout: Q117, Q168, Q173, Q175, Q177–Q182, Q186 | Product 11/12; no fixed Trial counts, thresholds, universal release gate or parser certification |
| 15.5 | Derived admitted telemetry, local canonical authority, privacy and correlation: Q125, Q174, Q176, Q178, Q184, S35.1 | W3 separates missing telemetry from missing required evidence; actual platform research remains pending |
| 16 | Candidate Contract families, one normative owner per meaning, reference directions and reconciliations: Q2–Q5, Q11, Q22, Q26, Q32, S24.2, S29.2, S38.1 | Structure planning only; no fixed file count, fields, enums, transitions, payloads, schemas, errors or migrations |
| 17 | Deferred RAG, rejected Overlay, stage/source maintenance and pending work: Q7, Q18, Q22, Q26–Q27, Q32, Q81, Q109, Q120–Q127, Q175, S7.1, S24.1–S24.2, S25.1, S26.1, S27.1, S28.1, S29.1–S29.2, S30.1, S35.1, S37.1, S38.1 | Product 12; future Development/Progress; maintenance history is not a new product rule |

Architecture includes locatable references to all 179 existing Q/S identifiers, counting explicit bounded ranges. This is a record-level coverage check, not a claim that every source clause becomes an Architecture requirement. Product-only presentation details stay in Product; source-maintenance records remain history; rejected branches are exclusions; post-v1 capabilities and unresolved detail retain their reasons and future owners. Q18 and S7.1, explicitly handed over by W1, are explained in Architecture sections 3.2 and 9.

## Clause-level supersession and semantic regression dispositions

The 29 required regression topics were reviewed in the actual Architecture prose against Product and effective source meaning. These are documentation findings, not executed product tests.

| Historical meaning at risk | Controlling meaning | Architecture / Product destinations |
| --- | --- | --- |
| Requirements/capability snapshot drives QuickScreen | Q56/Q110: metadata and exact Preferences/policy only | A4.2 / P4.2–4.3 |
| Incomplete BOSS root/version behaves like Manual | Q44/Q48/Q49/S9.1: complete atomic BOSS admission; Manual may have root only | A4.1 / P4.1 |
| Upload directly creates formal Resume | Q70–Q74: Draft, reconciliation/grounding, atomic Save | A5.1–5.2 / P3.2 |
| Earlier confirmation wording creates a completeness Gate | Q113: Save confirms facts; no KnowledgeConfirmation | A5.1–5.3 / P3.2/12.1 |
| Resume-private facts, parallel historical variants, per-bullet selection | Q63/Q108/Q163: shared current temporal facts, whole experience selection | A3.2/5.2 / P3.1/3.3 |
| Manual refresh or only replacement grounding after fact edits | Q108/Q114/Q118/Q119: all-affected atomic propagation; rebinding cannot restore old-fact eligibility | A5.2/5.4 / P3.3/3.5 |
| Advisor persistent working draft/export | Q146/Q148/Q149: Suggestion and target-specific Proposal, one confirmed formal commit | A5.1/7.2 / P6.2 |
| Discussion/Preparation selection implicitly authorizes apply | Q146/Q149 override Q93 for apply: current instruction, otherwise default; read actual target | A7.1–7.2 / P6.1–6.2 |
| Explicit apply skips preview or leaves old Run waiting | Q146/Q148/Q158 refine Q133/Q134: concrete preview; generating Run ends; Application confirms | A7.2–7.3/10.1 / P6.2 |
| Removing Resume membership deletes global Evidence | Q151/Q153: only Knowledge global deletion; direct membership propagation | A5.3 / P3.4 |
| Editor crash checkpoints or Advisor draft recovery | Q146/Q166/Q167: disposable page Draft; persisted Proposal loses eligibility on Session deletion | A5.1/7.3/12.3 / P3.2/6.3 |
| One dual-axis DeepFit/Coverage/ordered scores | Q112/Q115/S22.1: independent Skills/Runs/Analyses and scoped meanings | A6.2/9.1 / P5.2–5.3 |
| Empty Requirements mean perfect score; no score means zero/failure | Q171 blocks no-usable-target Fit; Q168 allows valid unscored analysis | A6.1–6.2 / P5.1/5.3 |
| Latest overlapping intent wins | Q116: serialize target and preserve latest successful compatible result | A6.3/12.2 / P5.4 |
| Full Context overflow silently invokes RAG/summarizes/switches model | Q121/Q123/Q132/S24.1: pre-invocation failure; RAG post-v1 | A6.3/10.2/17 / P5.4/9.3 |
| Available data is automatically injected or follows latest | Q83/Q94/Q139/Q143: actual Frames, eager exact or lazy pinned reads | A7.1/10.1 / P6.1/9.1 |
| Pure read secretly parses | Q142/Q144/Q159: missing dependency; separate Application Ensure, producer cost | A6.1/7.3/9.2 / P5.1/6.3 |
| Memory owns compaction or one switch controls all use | Q132/Q139 supersede affected Q127/Q137: separate Context; independent learning/Recall/management | A10/14 / P9.3/10.2 |
| Failed learning ranges auto-rejoin or deleted sources publish | Q169/Q170: explicit old-range Retry; new ranges proceed; source checks prevent publication | A14.2 / P10.3 |
| Unknown dispatch silently replays or Gateway hides requests | Q122/Q135/Q140: explicit new Run, unique Runtime boundary and retained exposure | A9.1/11/12 / P9.2 |
| Each loop resets auxiliary allowances | Q121/Q135: local ceilings plus Run totals, once-per-Run compaction/rescue | A10.3/11 / P5.4/9.2 |
| Save renders every format or derivative recovery permits remote replay | Q147/Q152/Q165: durable demanded intent, skip obsolete work, safe local recovery only | A5.4/12.3 / P3.5/9.2 |
| Revoke frozen input, remove it and continue | Q172: terminate affected task, new task for new scope | A6.3/10.3/12.2 / P5.4/9.1 |
| ResumeVersion/material confirmation grants execution | Q30/Q150/Q157: actual viewed artifacts/Greeting; separate single-use execution approval | A8 / P7.2/8.1 |
| Cooldown restores strong risk or execution check refreshes JD | Q160/Q164: persistent safety with explicit restoration; checks separate from refresh | A4.3/8 / P8.1–8.2 |
| Langfuse/judge determines business success | Q174/Q176/Q184: local canonical authority; separate judges and admitted evidence | A15.1–15.2/15.5 / P11 |
| One golden text, replay historical N Turns, expose whole Dataset | Q178/Q180/Q183/Q185: semantic alternatives, coherent boundary and N+1-only execution, separate task/reference/control | A15.2–15.4 / P11 scope only |
| 1/3/5 Trials, defaults or universal release Gate are settled | Q175: rollout deferred; Q117 parser certification stays deferred | A15.4/17 / P11/12.2 |
| Old migration order or prior completion constrains new repo | Q4/Q22/S37.1/S38.1: review main docs before Contract Grill/Contracts/development; actual status anew | A1/17 / P1/12.2 |

## Verification seam results

### Decision-to-Document Traceability Seam

W2 review found no unresolved contradiction in the written architectural scope. Controlling Q-IDs, surviving earlier clauses, later replacements, excluded branches, future owners, and reasons for deferral are recorded in Architecture and the tables above. All 179 existing identifiers are locatable; Q13/Q109 remain exclusion evidence and S24.1 remains post-v1 evidence. Inventory examples were not promoted into new decisions.

Mechanical checks validate current identifier references and bounded ranges, local links/anchors, heading/table structure, English-only formal prose, whitespace, and preservation of original tracked records. These checks supplement semantic review; a citation count does not establish correct interpretation. Detailed Contract completeness, W3 evidence mappings and the W5 formal supporting matrix remain pending.

### Cross-Document Semantic Consistency Seam

W2 compared the actual Product and Architecture drafts with the authoring rules and source modules. No unresolved contradiction was found in this two-document scope. Checks covered business versus derived authority; current eligibility versus exact history; discussion versus apply target; Session versus Memory; Package versus actual Frame; human confirmation versus dependency wait; commit versus narration; material confirmation versus execution permission; safe derivatives versus unknown remote work; technical events versus business progress; and local canonical results versus Eval/telemetry.

Product sections 1 and 12.2 were corrected only for the new Architecture link and availability. Product owns visible behavior, Architecture owns its explanation, and neither invents pending Contract representations or implementation status. The Chinese authoring reference remains preserved and non-authoritative for formal authoring.

Full cross-document validation remains **pending W6** because Acceptance, Development and Progress have not yet been written. Detailed Contracts will require subsequent reconciliation after Contract Grill. This result is not an all-documents pass, user approval, product test result, or implementation claim.

## Pending detail and reference directions

Architecture section 16 is the Contract structure plan. Its candidate families are not fixed filenames or a required file count. Consumers must reference a single normative owner for shared meanings; new Contract IDs remain pending. Preserve these directions:

- Profile/Evidence provide exact authority to Resume/grounding and admitted Candidate Fit; Resume Fit cannot import unexpressed Knowledge.
- JobVersion provides exact source to Requirements; Fits and targeted Advisor consume the validated Set. Pure reads delegate missing-dependency preparation to Application.
- Session provides verifiable conversational provenance and current eligibility for Proposal; Application executes the confirmed operation and records its result. Preparation only explicitly adopts a formal result.
- Material/readiness and execution approval remain distinct; Executor shares platform safety without inheriting Collector budgets, ownership, or authorization.
- Harness consumes Application/Domain rules; Context records actual visibility; Memory supplies only admitted collaboration content; Storage and Recovery preserve exact boundaries without becoming business authority.
- Budget accounts for actual invocation owners and exposure; Eval consumes isolated real paths and actual evidence without redefining business success.

Architecture section 17 and Product section 12.2 identify unresolved representation and policy questions: per-function fields/prerequisites, reference syntax/types/errors, target keys, command and approval protocols, state transitions, payloads/schema/migrations, scoring values, Tool catalog, compaction/Memory triggers and ranges, retention/cleanup, budget amounts and unknown reconciliation, rendering/channel proof, fixture/evaluator interfaces, pinned upstream/platform research, and rollout policy. Contract Grill and the specified later owners must resolve these; W3 must not fill them for test convenience.

## W3 entry and handoff instructions

Read this handoff automatically, then reread the actual English authoring spec, Product, and Architecture. Start original-source verification with register Purpose/Session State and Q4/Q22/S24.2/S37.1/S38.1. Read relevant controlling records and module Verification implications, especially Q82/Q117/Q173–Q187. Recheck source changes and their impact rather than assuming this snapshot remains current.

Author `docs/acceptance.md` in English. Translate settled behavior and invariants into observable acceptance and required evidence, preserving failure, concurrency, privacy, authorization, recovery, and partial-success cases. Distinguish deterministic mechanism proof from semantic Eval, N+1 from full Scenario coverage, Skill-focused from workflow experiments, and actual task outcome from each check's evidence. Do not freeze Trial counts, thresholds, release policy, pending fields or statuses, or imply that acceptance was executed.

The next handoff should map requirements to acceptance destinations, retain controlling/superseding sources, identify exact pending Contract prerequisites, and separately report both seams. W4 then owns Development, W5 owns actual Progress/matrix, and W6 jointly reviews the five main documents before user review and detailed Contract Grill. Do not create those later documents or implementation merely to make this handoff appear complete.
