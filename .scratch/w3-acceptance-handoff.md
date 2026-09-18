# W3 Acceptance Handoff

> English is authoritative. This is an authoring handoff and scoped review record, not an additional normative authority or a report of executed product acceptance. Subsequent stages automatically read the preceding handoff and actual documents; no separate confirmation to read them is needed.

## Delivered scope and actual state

W3 authored [Acceptance](../docs/acceptance.md) from the [English authoring spec](document-authoring-spec.en.md), [W2 handoff](w2-architecture-handoff.md), actual [Product](../docs/spec.md) and [Architecture](../docs/architecture.md), and effective original-source meanings. It defines observable scenarios and required future evidence without implementing tests, assigning Contract IDs, freezing Contract detail, or selecting rollout policy.

Product sections 1, 11 and 12.2 and Architecture sections 1 and 17 now link the authored Acceptance draft and describe its responsibility. These are document-availability/ownership updates; no product or architecture decision changed. W1/W2 handoffs remain unchanged historical records of their respective delivery points.

Product, Architecture and Acceptance are drafts awaiting the five-document joint review and subsequent user review. Development, Progress and its supporting matrix, and detailed Contracts remain unauthored. Product implementation, executable tests, Eval deployment and acceptance execution have not started in this repository. No product pass, implementation completion or user review approval is claimed. Work remains uncommitted. The nine Grill originals and both authoring-spec editions remain unchanged.

## Sources read and controlling interpretation

| Source | W3 use and reading scope |
| --- | --- |
| [English authoring spec](document-authoring-spec.en.md) | Ownership, W3/W4 responsibilities, required handoff, both seams, semantic regression set, source index and pending-detail limits |
| [W2 handoff](w2-architecture-handoff.md), [Product](../docs/spec.md), [Architecture](../docs/architecture.md) | Actual behavior/mechanism baseline, full topic mapping, prior supersession dispositions, Contract structure plan and remaining detail; handoff did not replace actual documents |
| [Decision Register](../docs/design/grill-me-design-tree.md) | Purpose/Session State, Q4/Q22/S24.2/S37.1/S38.1, Q82/Q117, full Q173–Q187 and targeted rechecks including Q42/Q121/Q150/Q168; other topic meanings were compared with the controlling mappings already established in W1/W2 and the detailed modules |
| [Tool Actions](../docs/design/harness/tool.md) | Verification implications and later-Contract boundary: pure reads, permission/source validation, exact Proposal and material approval, owner cost and safe derived work |
| [Context](../docs/design/harness/context.md) | Verification implications and W2 mechanisms: actual Frame, protected input, exact source, compaction, checkpoint publication, dynamic Memory and bounded allowances |
| [Memory](../docs/design/harness/memory.md) | Verification implications plus independent controls, budget ownership and actual post-write/Q158 refinement; source/forgetting/failure/deletion scenarios retain Q145/Q169/Q170 controls |
| [Budget](../docs/design/harness/budget.md) | Verification implications, unknown-usage/Retry boundary and W2 owners/limits; illustrative dollar amounts were not adopted as requirements |
| [Recovery](../docs/design/harness/recovery.md) | Verification implications including every listed crash boundary, fencing, local recovery versus replay, parse contention and transient streams |
| [Storage](../docs/design/harness/storage.md) | Verification implications: active dependency protection, truthful purge, independent history/usage, safe rehydration and source admission |
| [Agent Evaluation](../docs/design/eval/agent-evaluation.md) | Detailed normative-direction sections 1–31 and precedence, including Q173–Q187, candidate metric limitations, isolation, human calibration, per-check results and retained-output re-evaluation. Research Appendix A remains future version/deployment verification, not a new external capability claim |
| [Contract Inventory](../docs/design/contract/contract-design-inventory.md) | Purpose/status/reading rules only; no field list or illustrative operational default became an executable oracle |

This stage did not repeat the Architecture Grill or independently reread every old record as a new decision. It reused the effective W1/W2 synthesis and rechecked the acceptance-specific source boundaries above. Later corrections still control clauses inside earlier ACCEPTED records. Complete five-document coverage review remains W6 work.

## Requirement-to-acceptance mapping

Section numbers locate actual Acceptance prose and named scenario rows. Product owns visible rules, Architecture owns supporting mechanisms, and Acceptance owns the required proof. Sources below are decision IDs, not formal Contract or test IDs.

| Requirement family and owning documents | Acceptance destination and required proof | Controlling sources and pending boundary |
| --- | --- | --- |
| Documentation-first, clean slate, authority and actual state: P1/12; A1/16/17 | 1, 14: stage/ownership review and the two document seams; no claimed implementation | Q2–Q5, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1; future Contract IDs/matrix remain pending |
| Evidence standards and correct claim scope: P11; A15 | 2, 12–13: deterministic proof versus live semantic evidence; task outcome versus check conclusion | Q82–Q83, Q117, Q173–Q187, S35.1; no schemas/formulas/thresholds or release policy |
| Independent tasks/navigation and source-specific Jobs: P2/4.1; A2–4 | 3: entry/routing, exact identities, validated complete BOSS admission versus Manual root-only, observation/history | Q1, Q6–Q7, Q12–Q14, Q17–Q18, Q23–Q24, Q44, Q48–Q50, Q53, S5.1, S5.3, S9.1, S17.1–S17.4; Q13 exclusion only |
| Preferences, pure screening and collection: P4.2–4.4; A4 | 3: inputs/call absence, no rejected-content persistence, frozen Run versus current local view and stop retention | Q3, Q27, Q45, Q49–Q50, Q55–Q56, Q110, Q161; actual adapters/fields need Contracts/research |
| Shared facts/import/Save and whole experiences: P3.1–3.3; A3/5.1–5.2 | 4.1: non-authoritative import, confirmation/reconciliation, atomic fan-out, rollback and concurrent edits | Q15, Q54, Q63–Q64, Q70–Q75, Q76–Q77, Q96–Q98, Q108, Q113–Q114, Q118–Q119, Q147, Q163; no transaction schema or universal completeness gate |
| Defaults/deletion/empty state and historical grounding: P3.4–3.5; A3.2/5.3–5.4 | 4.2: direct-membership effects, independent history, task preflight, actual-dependency grounding versus whole baseline and original readers | Q75–Q77, Q79, Q86–Q88, Q93, Q100, Q108, Q113–Q114, Q118–Q119, Q151, Q153–Q154; exact refs/prerequisite matrix pending |
| Safe demand-driven derivatives: P3.5/7.2/9.2; A5.4/12.3 | 4.3, 9.3: authority-plus-intent crash boundary, demand/reuse, obsolete dispatch and stale-publication rejection | Q147, Q150–Q152, Q165; render/work representations pending; no remote replay |
| Requirements and dependency ownership: P5.1/6.3; A6.1/7.3/9.2 | 5.1: real Ensure, exact usable Set, bounded repair, pure reads, cross-process single-flight, owner-only cost and waiter independence | Q10, Q14, Q24, Q58–Q59, Q110–Q111, Q117, Q121, Q142, Q144, Q159, Q171; concrete parse/claim/error interface pending |
| Independent Fits and scoped assessment/score: P5.2–5.3; A6.2 | 5.2, 13.1: exact actual Frame, no supplementation, bounded repair, complete coverage, semantic support/false negatives, valid unscored analysis and rescoring | Q19, Q24, Q35, Q46, Q51, Q72, Q76, Q82–Q83, Q108, Q112–Q115, Q121, Q135, Q168, Q184, S22.1; score formulas/availability details pending |
| Freeze/concurrency/failure/permission: P5.4; A6.3/10.3 | 5.3: two freezes, serialized exact target, compatible success, capacity, independent outcomes, final admission and revocation interleavings | Q35, Q40, Q110, Q113, Q116, Q121–Q124, Q132, Q172, S24.1; exact target keys and detailed transitions pending |
| Advisor/Proposal/Session: P6; A7 | 6: source-labeled discussion, exact apply target/patch/impact, one Application confirmation after generating Run ends, idempotent mutation, two waits and Session-delete races | Q24, Q41, Q47, Q52, Q85, Q88–Q89, Q91, Q93–Q94, Q96, Q108, Q113–Q114, Q118–Q119, Q128, Q133–Q134, Q138–Q139, Q143–Q144, Q146, Q148–Q149, Q155–Q159, Q167; exact commands/lifetimes pending |
| Preparation/materials/execution/events: P7–8; A4.3/8 | 7: reentry/CAS, actual viewed approval, atomic snapshot freeze, single-use execution, minimal live checks, shared safety and real event provenance | Q7, Q16–Q17, Q21, Q25, Q30–Q31, Q36–Q37, Q42, Q49, Q77, Q91, Q108, Q146, Q150, Q157, Q160–Q164; channel/read-back and rendering details pending |
| Harness/Tool/Context: P9; A9–10 | 8: unique business Provider boundary, permission intersections, actual access/Frames, pinned reads, protected inputs, bounded compaction and checkpoint failure | Q19, Q47, Q72, Q80, Q83, Q94, Q120–Q128, Q132, Q134–Q144, Q158, Q172, S7.1, S17.4, S22.1; full catalog/Context representation pending |
| Budget/recovery/streams: P5.4/9.2; A11–12 | 9: competing reservations, settlement, conservative unknown exposure, crash/fencing boundaries, safe local continuation, no hidden requests, stream versus commit | Q116, Q121–Q126, Q130, Q132, Q135–Q136, Q140–Q142, Q147, Q152, Q155–Q156, Q165, Q169–Q172, Q176; amounts/overrun/reconciliation/replay details pending |
| Privacy/storage/history: P9; A3.2/13 | 10: actual admitted/exported inputs, secrets exclusion, active retention, truthful unavailable history and distinct deletion effects | Q19, Q52, Q54, Q75, Q100, Q124–Q125, Q131–Q132, Q136, Q139, Q141, Q151, Q167, Q170, Q174, Q184; retention/layout/erasure interfaces pending |
| Memory: P10; A14 | 11: source admission, independent controls, learning/Recall Skill scope, pending source durability, budget/failure isolation, newer management and deleted sources | Q52, Q127–Q133, Q137–Q139, Q141, Q145, Q155–Q156, Q169–Q170, Q187; categories/ranges/markers/triggers remain later detail |
| Eval integrity and declared evidence: P11; A15 | 12: isolated real paths, reproducibility, next-turn versus full Scenario, exact-one confirmation, task/reference/control separation, independent judges, telemetry and actual-output re-evaluation | Q173–Q187, S35.1; no new fixture/evaluator schemas, code layout or platform deployment claim |
| Quality and honest comparison: P11; A15.4 | 13: capability-specific questions, scoped human calibration, holdout, alternative answers, Pass@1/variability, stage-specific cost and coverage | Q82–Q83, Q111–Q117, Q168, Q171, Q175–Q187, S17.1; metrics and rollout policy unresolved |
| Exclusions, structure and remaining work: P12; A16–17 | 14: explicit pending owners, rejected/superseded exclusions, post-v1 scope and two independent review seams | Q13/Q109 rejected; Q81/S24.1 post-v1; source-maintenance S25.1/S26.1/S27.1/S28.1/S29.1/S29.2/S30.1 remain history, not product scenarios |

Mechanical source-index comparison finds all **161 existing records** in rows listing Acceptance as a consumer directly referenced in Acceptance, including bounded ranges. Acceptance references 178 of all 179 existing records; **Q8** is already owned by Product 2–4 and Architecture 3.1, with its surviving independent-authority meanings covered here through the later specific owners and Q56's removal of the screening snapshot. It needs no additional scenario or competing definition. This is a locator/coverage result, not proof that a citation alone preserves every clause.

## Clause-level semantic regression review

The 29 required topics were checked against the actual draft. Destinations below retain the effective meanings; they are not passing product test results.

| Historical mechanism at risk | Controlling meaning preserved | Acceptance destination |
| --- | --- | --- |
| Requirements/capability snapshot in screening | Q56/Q110: metadata and exact Preferences/policy only | 3 screening inputs and collection call evidence |
| Incomplete BOSS admission like Manual | Q44/Q48/Q49/S9.1: complete atomic BOSS admission; Manual root-only allowed | 3 source-specific cases |
| Import immediately formal | Q70–Q74: Draft/reconciliation/grounding/Save | 4.1 import and Save cases |
| Confirmation wording restores completeness gate | Q113: Save confirms; no KnowledgeConfirmation | 4.1/4.2 and 14.2 |
| Resume-private facts, historical variants or bullet selection | Q63/Q108/Q163: shared current temporal facts and whole experiences | 4.1–4.2 |
| Manual refresh or grounding-only rescue of old facts | Q108/Q114/Q118/Q119: atomic propagation; historical readability is not new-use eligibility | 4.1–4.2 |
| Advisor draft/export | Q146/Q148/Q149: target-specific operation preview and formal confirmed commit | 6 and 14.2 |
| Discussion/Preparation implicitly selects apply target | Q146/Q149 scope Q93: current instruction, otherwise default; target-specific read/patch | 6 target comparison case |
| Apply skips preview or waits in old Run | Q146/Q148/Q158 scope Q133/Q134: concrete preview; generating Run ends before Application confirmation | 6; 8.2 own-write caveat; 12.2 |
| Removing Resume membership deletes shared fact | Q151/Q153: Knowledge-only global deletion and direct-membership impact | 4.2 |
| Crash-recoverable page/Advisor Draft | Q146/Q166/Q167: disposable editor state; durable Proposal cannot survive Session deletion as eligible action | 4.1, 6, 14.2 |
| Joint Fit/Coverage/score ordering | Q112/Q115/S22.1: independent tasks, meanings and results | 5.2 |
| Empty target means perfect score; unavailable total means zero/failure | Q171 no-target preflight versus Q168 valid unscored analysis | 5.1–5.2; 2.2 |
| Latest overlapping analysis intent wins | Q116: one effective active target and latest successful compatible result | 5.3 |
| Overflow silently trims/summarizes/switches/RAG | Q121/Q123/Q132/S24.1: explicit v1 pre-invocation failure | 5.3, 8.2, 14.2 |
| Available inputs are eagerly injected or follow latest | Q83/Q94/Q139/Q143: actual Frames and exact acquisition/pinning | 6, 8.2 |
| Pure read secretly parses | Q142/Q144/Q159: missing dependency, separate Application Ensure, owner-only cost | 5.1, 6 |
| Memory owns compaction or one switch controls all use | Q132/Q139 scope Q127/Q137: separate Context and three independent controls | 8.2, 11 |
| Failed ranges auto-rejoin or deleted source publishes | Q169/Q170: explicit failed-range Retry and source checks | 11 |
| Unknown request replays or SDK hides extra calls | Q122/Q135/Q140: durable boundaries, explicit new Run and retained exposure | 8.1, 9.1–9.2 |
| Later loop replenishes allowances | Q121/Q135: local ceilings and entire-Run totals jointly govern | 5.2, 8.2, 9.1 |
| Eager all-format rendering or derivative permission replays remote work | Q147/Q152/Q165: demanded durable intent and safe local work only | 4.3, 9.3 |
| Revoke protected input and continue reduced same task | Q172: terminate affected task; new task for new scope | 5.3, 8.2, 9.2 |
| Selected Resume/material approval authorizes execution | Q30/Q150/Q157: actual viewed frozen material plus separate single-use authorization | 7 |
| Cooldown restores strong risk or checks refresh JD | Q160/Q164: persistent shared admission and explicit restoration; refresh separate | 7 |
| Judge/telemetry decides business success | Q174/Q176/Q184: local canonical authority, independent scoped judges | 2, 12.3–12.4 |
| Unique golden answer, historical N-turn replay or whole-Dataset prompt | Q178/Q180/Q183/Q185: semantic alternatives, coherent boundary and N+1-only execution, separated inputs | 12.1–12.3 |
| Fixed Trial counts/universal release gate/default enablement | Q175 excludes rollout policy; Q117 certification remains deferred | 2.2, 13, 14.1 |
| Old order/legacy completion governs new repository | Q4/Q22/S37.1/S38.1: documentation first, real evidence and no assumed legacy obligation | 1, 14 |

## Verification seam results

### Decision-to-Document Traceability Seam

W3 scoped review found no unresolved contradiction in the authored acceptance expectations. Each scenario group links Product/Architecture owners, required observations and controlling Q-IDs; the mapping above records its proof and pending Contract boundary. The 29 semantic regressions preserve later corrections instead of relying on ACCEPTED labels. Rejected branches, post-v1 capabilities and source-maintenance history have explicit dispositions rather than invented scenarios.

Mechanical review checks existing identifiers and bounded ranges, coverage-index consumer records, local links/anchors, table/fence structure, English-only prose, whitespace and unchanged source files. These checks supplement semantic interpretation. This result does not prove runtime behavior, exhaustive future test coverage or completed detailed Contracts. Original-reader/reference fixtures, concrete validation oracles and other pending details remain explicit in Acceptance 14.1.

### Cross-Document Semantic Consistency Seam

W3 compared the actual three formal drafts and their source meanings. No unresolved inconsistency was found in the reviewed scope. Product-visible outcomes agree with Architecture ownership and the acceptance proof: exact current versus historical sources; Frame versus manifest; discussion versus apply target; complete shared impact versus unauthorized writes; pending human confirmation versus active machine wait; safe derivatives versus remote replay; MaterialApproval versus ExecutionApproval; Session versus Memory; canonical task outcome versus judge/telemetry evidence.

The only changes to prior drafts are current document links, availability and evidence-ownership wording. Acceptance adds no detailed Contract body, release threshold, default-enablement consequence or implementation claim. Missing details are consistently assigned to later owners instead of silently decided for testability.

The five-document joint review remains **pending W6** because Development and Progress are not authored. User review and later completed-Contract reconciliation remain pending. Neither seam result is a passed product test or an all-documents approval.

## W4 entry and remaining detail

Automatically read this handoff, then the actual English authoring spec, Product, Architecture and Acceptance. Recheck register Purpose/Session State and Q4/Q22/Q26/Q27/Q32/S24.2/S37.1/S38.1, plus relevant Eval delivery boundaries and Q117/Q175. Verify source changes against this snapshot before relying on the prior dispositions. The earlier handoffs explain history, not current file availability.

Author `docs/development.md` in English. It owns the documentation-review → separate Contract Grill → complete Contracts/reconcile → formal-development sequence; accepted test-first/TDD and real-path Eval discipline; source/research/change rules; future Slice acceptance evidence; traceability maintenance and automatic handoff reading. Acceptance now provides the required future proof; Development must not reinterpret that as executed evidence or invent a second behavioral authority.

Preserve Acceptance 14.1's pending topics: business fields/per-function inputs; exact references and historical evolution; commands/target keys/CAS/idempotency/approval transitions; parser/Fit outputs and scoring; Tool/admission/Context/Memory/budget/retention detail; render/channel verification; fixture/evaluator/metric interfaces; pinned upstream/platform research; later rollout/CI policy. Do not select an unaccepted first Slice, fixed code layout, bootstrap, test runner/commands, sample count or release threshold merely to make delivery concrete.

Q32's future unified reference/mapping check is a requirement to plan, not an existing script or current CI result. Formal Contract IDs, implementation paths and test/Eval evidence become matrix inputs only when actually available. W5 owns actual Progress and the supporting matrix; W6 owns joint review. This stage leaves those files and Contract detail for their planned work.
