# W4 Development Handoff

> English is authoritative. This is an authoring handoff and scoped review record, not another normative authority or a report of implemented capabilities. Subsequent work automatically reads the preceding handoff and actual documents; no read-confirmation question is needed.

## Delivered scope and actual state

W4 authored [Development](../docs/development.md) using the [English authoring spec](document-authoring-spec.en.md), [W3 handoff](w3-acceptance-handoff.md), actual [Product](../docs/spec.md), [Architecture](../docs/architecture.md) and [Acceptance](../docs/acceptance.md), and the controlling original decisions. It defines delivery sequence, source/change discipline, research, future Slice/TDD work, verification/Eval discipline, traceability, honest status and handoffs.

Product sections 1 and 12.2, Architecture sections 1 and 17, and Acceptance sections 1, 14.1 and 14.3 now reference the authored Development draft and reflect four available main documents. Changes concern availability, ownership and cross-document review scope; no product requirement, architecture invariant or acceptance scenario changed. Prior W1–W3 handoffs remain unchanged historical records of their delivery points.

The four main documents are authored drafts with scoped authoring review; W5 Progress/matrix, W6 joint review and user review remain pending. Detailed Contract Grill and normative Contracts are pending. No product implementation, executable test suite, test runner, `./scripts/check`, CI pipeline or deployed Eval platform was created or verified. No first implementation Slice, complete stack, bootstrap, numerical threshold or rollout policy was selected. No commit or external publication was performed.

The nine original Grill records and both authoring-spec editions remain unchanged. W4 creates no Progress or Contract file. Target architecture, document existence and old-repository results remain insufficient evidence for Implemented or Partial capability status.

## Reading scope and controlling sources

| Input | W4 reading and interpretation |
| --- | --- |
| English authoring spec and W3 handoff | Actual ownership, W4/W5/W6 tasks, both seams, 29 regressions, coverage index and pending-detail obligations; automatic handoff entry preserved |
| Actual Product, Architecture and Acceptance | Governing behavior and mechanism/proof mappings; focused reconciliation of authority, stage/status language, Contract planning, Eval and pending details |
| [Decision Register](../docs/design/grill-me-design-tree.md) | Purpose/Session State and direct review of Q2/Q3/Q4/Q5/Q11/Q18/Q22/Q26/Q27/Q32/Q117/Q175/S7.1/S24.2/S37.1/S38.1; prior W1–W3 controlling mappings supply the related business/runtime topic baseline |
| [Tool](../docs/design/harness/tool.md), [Context](../docs/design/harness/context.md), [Memory](../docs/design/harness/memory.md), [Budget](../docs/design/harness/budget.md), [Recovery](../docs/design/harness/recovery.md), [Storage](../docs/design/harness/storage.md) | Current Verification implications and later-Contract boundaries, compared with Acceptance routing; illustrative costs and conceptual structures were not frozen |
| [Eval](../docs/design/eval/agent-evaluation.md) | Deterministic conformance versus model behavior, reliability/findings, Q175 release boundary, regression curation, human calibration/independent judges, platform responsibilities, clean-slate TDD and research Appendix A; Q173–Q187 semantics reconciled with Architecture 15 and Acceptance 12–13 |
| [Contract Inventory](../docs/design/contract/contract-design-inventory.md) | Purpose/status/reading rules only; inventory fields and examples did not become engineering defaults or normative Contracts |

No Architecture Grill was reopened, and W4 does not claim a fresh line-by-line review of every old source record. Source files match the unchanged baseline; current task-specific readings supplement the established W1–W3 interpretation. W6 still owns complete joint coverage review.

## Development section and decision mapping

| Development section | Delivery rule and controlling sources | Ownership/reference boundary |
| --- | --- | --- |
| 1 | Six formal categories, English authority, no extra normative handoff/inventory: Q2/Q5/Q11/Q22/Q26/Q32/S24.2/S37.1/S38.1 and user language instruction | Product owns behavior, Architecture mechanism, Acceptance proof, later Contracts detail and Progress actual state |
| 2 | Five documents and user review before separate Contract Grill, complete Contracts/reconciliation before formal development: Q4/Q22/S24.2/S37.1/S38.1 | Replaces old D0–D6 order; no first Slice or bootstrap selected; Q117/Q175 remain scoped deferrals |
| 3 | Clause-level supersession, stable provenance, source preservation, no legacy compatibility obligation; original readers still required: Q4/Q12/Q13/Q18/Q26/Q32/Q75/Q79/Q86/Q87/Q108/Q114 | Architecture 3.2/17 and Acceptance 4.2/14; maintenance supplements S25.1/S26.1/S27.1/S28.1/S29.1/S29.2/S30.1 remain history |
| 4 | Pinned source/version/license/maintenance and consumer mapping; actual selected platform checks: Q3/Q27/Q30/Q31/Q49/Q50/S7.1/S35.1 | Architecture 2.2/4.3/15.5 and Acceptance 3/7/12; research is neither upstream authority nor an implemented integration/default policy |
| 5 | Bounded Slice rationale/prerequisites/owner/Harness/persistence/proof/status; minimal mechanisms and test-first loop: Q4/Q7/Q18/Q22/Q26/Q32/Q37/Q42/Q118/Q119/Q173/Q178–Q183/Q186/S37.1/S38.1 | Relevant completed Contracts and Acceptance govern future implementation; no code/test framework chosen |
| 6 | Route real changes to actual Acceptance boundaries; preserve atomicity, exact inputs, permission, independent tasks, unknown outcomes and scope | Acceptance 3–13 remain proof authority; the topic table carries the relevant original and later controlling Q-IDs without duplicating their full business definitions |
| 7.1–7.2 | Real isolated paths, exact fixtures, declared stages, controlled Memory, coherent N+1/full Scenario, exact-one Application confirmation, scoped judges/control separation: Q120–Q122/Q140/Q158/Q173/Q176–Q178/Q180/Q183–Q187/S35.1 | Architecture 9/15; Acceptance 12.1–12.3; no test-only Agent or trace-controlled business result |
| 7.3–7.4 | Per-check findings, holdout/alternatives, honest variability/cost, retained regression intent, actual-output re-evaluation and derived telemetry: Q82/Q117/Q125/Q136/Q168/Q174–Q187/S17.1 | Acceptance 2/10/12.4/13; no release thresholds, universal gates or raw-payload retention exception |
| 8 | Normative requirements versus actual Progress; stable IDs later, evidence-backed status, matrix per Slice and future unified checks: Q4/Q22/Q26/Q32/Q175/Q179/S37.1/S38.1 | Planned `docs/progress/traceability.md` belongs to Progress; `./scripts/check` is a future obligation, not an existing command or result |
| 9 | Automatic actual-file/handoff entry, required completion record and separate verification seams: Q22/Q26/Q32/S24.2/S37.1/S38.1, authoring spec and user instruction | Handoff is a locator; both seams remain scoped and do not imply implementation/user approval |
| 10 | Pending Contract/policy/research/rollout work and W5/W6 sequence: Q2–Q5/Q11/Q13/Q18/Q22/Q26/Q27/Q32/Q81/Q109/Q117/Q121/Q123/Q175/S7.1/S24.1/S24.2/S35.1/S37.1/S38.1 | Architecture 16–17 and Acceptance 14.1 retain pending owners; no new document category or deferred feature is implemented |

All **89 existing Q/S records** in authoring-index rows naming Development as a consumer are directly referenced in the Development draft, including bounded ranges. Its 143 current references are not a claim that Development owns those business facts. Section 6 routes their verification back to Acceptance and Architecture; remaining Product-only details stay with their owners. The complete 179-record source index remains available for W5/W6. A citation count is only a mechanical locator check, not proof of correct interpretation.

## Semantic regression dispositions

All 29 authoring regression topics were checked for the way Development directs implementation/tests. D denotes Development and V denotes Acceptance; rows cite the actual governing acceptance destination instead of creating a second scenario catalog.

| Historical meaning at risk | Controlling meaning and W4 disposition | Actual destination |
| --- | --- | --- |
| Screening requires Requirements/capability snapshot | Q56/Q110: metadata-only; engineering must not introduce the removed dependency | D6, V3 |
| BOSS permits incomplete Jobs like Manual | Q44/Q48/Q49/S9.1: source-specific admission with one complete JobVersion meaning | D6, V3 |
| Import immediately formalizes Resume | Q70–Q74: Draft, reconciliation and atomic Save | D6, V4.1 |
| Old confirmation wording creates completeness gate | Q113: Save confirms facts; no KnowledgeConfirmation | D6/9.2, V4 |
| Resume-private facts, freely selected old variants or bullet graph | Q63/Q108/Q163: shared current temporal facts and whole experiences | D3/6, V4 |
| Manual refresh or grounding-only rescue | Q108/Q114/Q118/Q119: all-affected atomic propagation and current-use checks | D5.1/6, V4 |
| Advisor persistent draft/export | Q146/Q148/Q149: exact operation Proposal and formal commit | D4/6/9.2, V6 |
| Discussion/Preparation implicitly supplies apply target | Q146/Q149 scope Q93: actual instruction/default target and its own patch | D6/9.2, V6 |
| Explicit apply skips preview or generating Run waits | Q146/Q148/Q158 scope Q133/Q134: concrete preview; later Application confirmation | D6/7.2, V6/12.2 |
| Removing one Resume selection deletes Evidence | Q151/Q153: Knowledge-only deletion with direct membership impact | D6, V4.2 |
| Draft crash checkpoint or Advisor draft recovery | Q146/Q166/Q167: page state disposable, pending Proposal subject to Session eligibility | D6, V4.1/6 |
| Joint Fits/Coverage/ordered scores | Q112/Q115/S22.1: independent tasks/results/scopes | D6, V5.2 |
| Empty targets score perfectly; no total is zero/failure | Q171 dependency failure versus Q168 valid unscored result | D6/7.3, V5.1–5.2 |
| Latest overlapping intent selects current analysis | Q116: serialize target and preserve compatible success | D6, V5.3 |
| Full Context overflow trims/switches/RAG | Q121/Q123/Q132/S24.1: fail before invocation; retrieval post-v1 | D6/10, V5.3/8.2 |
| Available inputs are eager or follow latest | Q83/Q94/Q139/Q143: actual Frames and exact acquisition/pinning | D6, V6/8 |
| Read hides parsing | Q142/Q144/Q159: pure missing-dependency read and Application-owned Ensure | D6, V5.1/6 |
| Memory owns compaction or a combined off switch | Q132/Q139 scope Q127/Q137: distinct Context and independent controls | D6, V8/11 |
| Failed ranges auto-rejoin or deleted sources publish | Q169/Q170: explicit failed-range Retry and source checks | D6, V11 |
| Unknown calls replay or SDK hides requests | Q122/Q135/Q140: durable boundary and explicit new Run with retained exposure | D4/6/7.1, V8–9 |
| Each loop renews auxiliary allowance | Q121/Q135: local and whole-Run ceilings both apply | D6, V8.2/9.1 |
| Eager every-format render or safe work replays remote effects | Q147/Q152/Q165: demanded durable intent, obsolete skipping, safe local recovery | D6, V4.3/9.3 |
| Revocation reduces and continues frozen task | Q172: end affected task; new scope needs new task | D6/9.2, V5.3 |
| Material selection/approval authorizes execution | Q30/Q150/Q157: actual viewed material and separate execution approval | D6, V7 |
| Cooldown restores strong risk or execution check refreshes JD | Q160/Q164: explicit restoration, checks separate from refresh | D4/6, V7 |
| Judge/Langfuse owns business success | Q174/Q176/Q184: local canonical authority and independent scoped judging | D7.2–7.4, V12 |
| Unique golden answer, replay prior N Turns, whole Dataset prompt | Q178/Q180/Q183/Q185: valid alternatives, coherent N+1 boundary and separated input roles | D7.2–7.3, V12–13 |
| Fixed Trials/defaults/universal release policy | Q175 leaves rollout undecided; Q117 certification remains deferred | D2/7.3/8.3/10, V2/13/14 |
| Old migration order or completion constrains new repo | Q4/Q22/S37.1/S38.1: documentation first, actual new evidence and no legacy obligation | D2/3/8/10, V1/14 |

## Verification seam results

### Decision-to-Document Traceability Seam

W4 scoped review found no unresolved contradiction in the delivery rules written. Sequence, authority/status separation, test-first work, research, Eval and handoffs have controlling sources and real owning destinations. The source-index comparison covers all 89 Development consumer records; the semantic table records later replacements and exclusions. Q32's future script, Q26's later stable IDs and Q175's deferred release policy remain correctly distinguished from current artifacts or execution.

Mechanical checks cover valid current identifiers/ranges, links/anchors, table/fence structure, English-only formal prose, whitespace, and preservation of sources/prior handoffs. These checks do not prove clause semantics or product behavior. Exact Contract details, first Slice/tooling choices and actual implementation/test evidence remain pending with named owners.

### Cross-Document Semantic Consistency Seam

W4 compared the actual four formal drafts. No unresolved conflict was found within this scope. Product owns behavior, Architecture mechanisms and Contract planning, Acceptance required proof, and Development delivery discipline. Engineering/test arrangements do not gain authority to change consent, source eligibility, runtime admission, actual commit, Eval findings or missing-detail policy. Prior-document edits only update availability, links and review scope.

Full five-document review remains **pending W6** because Progress and its matrix have not been written. User review and later completed-Contract reconciliation remain pending. These scoped review findings are not an all-documents approval, a product test pass or proof of implementation.

## W5 entry and concrete handoff

Automatically read this handoff and the actual English authoring spec, Product, Architecture, Acceptance and Development. Recheck register Purpose/Session State and Q4/Q22/Q26/Q32/S37.1/S38.1; use the complete authoring coverage index and original topic sources for ambiguous mappings. Compare repository state and source changes rather than carrying forward historical handoff availability as current fact.

Author `docs/progress.md` and `docs/progress/traceability.md` in English, within the single Progress category. The summary should describe the actual task/documentation state, gaps/blockers and next step. The matrix should retain source-to-document/acceptance trace while marking detailed Contract IDs pending. Include implementation/test/Eval locations and evidence only when they actually exist; do not fabricate IDs, paths or successful outcomes to fill columns.

At this handoff, the evidenced baseline is four authored main drafts and their scoped authoring checks; joint/user review, detailed Contracts, product implementation and executed acceptance are pending. Separate authored/reviewed documentation from Q26/Q32's implementation labels. Planned current capabilities are not Deferred merely because no code exists; accepted post-v1 deferrals need their governing sources. Partial/Implemented require actual implementation and matching verification evidence, not broad target prose or old completion claims.

Development 8 specifies future matrix/status/check responsibilities. Its mention of `./scripts/check` is not evidence of a current script. Development 10 and Acceptance 14.1 locate remaining Contract fields/interfaces/transitions/errors/schemas/migrations, policy values, source/platform research, Eval interfaces and rollout decisions. Do not resolve them in Progress or choose a first implementation Slice.

Report both seams separately and hand off unresolved mappings for W6. W6 must review all five documents and complete source dispositions, present concrete documents for user review, and only then move to separate Contract Grill and Contracts. W5 may correct availability/reference wording as artifacts are created, while preserving original Grill records and historical handoffs.
