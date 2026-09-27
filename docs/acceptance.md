# JobHunter Acceptance

> **2026-09-24 supplemental baseline.** CG03S1 replacement proof below supersedes shared fact authority/two-stage import/parallel Fits. These are required future tests, not executed acceptance. Deferred application/adopt-back is not a current optimization gate.

> English is the authoritative documentation language. This W3 draft defines required future verification and evidence, not passing tests or implemented capabilities. See [Progress](progress.md) for current joint-review and user-approval state. Detailed Contracts and executable acceptance work remain later stages.

## 1. Authority, scope, and use

The [Product Specification](spec.md) owns visible tasks and behavior. [Architecture](architecture.md) owns supporting responsibilities, authority, dependencies, and invariants. This main document remains the unified product/system acceptance authority for how those settled requirements must be demonstrated, including positive, negative, boundary, concurrency, failure, recovery, permission, and semantic-quality cases. An acceptance expectation cannot create a new business rule or supersede either owner merely to simplify a test. The supporting [Eval acceptance document](evaluation.md#2-evaluation-acceptance-criteria) owns specialized evaluation-evidence criteria within this same category; the [Development Eval guide](evaluation.md#3-evaluation-workflow) owns execution procedure.

The [English authoring spec](../.scratch/document-authoring-spec.en.md) and [W2 handoff](../.scratch/w2-architecture-handoff.md) govern this stage. Q/S references resolve to the [Decision Register](.grill/grill-me-design-tree.md) and effective detailed modules. Later corrections control the clauses they replace even inside earlier ACCEPTED records. The [Contract Design Inventory](.grill/contract/contract-design-inventory.md) is a non-normative checklist. It supplies no final schema, default-enablement policy, or test oracle.

All scenarios below are requirements for future verification. They have not been executed. Table scenario names and section numbers are document locators, not Contract requirement IDs, executable test names, product states, or a prescribed suite layout. Evidence columns name what a check must observe; they do not freeze fields, event schemas, tool interfaces, payloads, database layouts, validation errors, migration procedures, metric formulae, or detailed state transitions. Section 14 identifies the details needed before executable checks can be finalized.

Product, Architecture, Acceptance, [Development](development.md), and [Progress](progress.md) are authored drafts, with the supporting [Traceability Matrix](progress/traceability.md). [Implementation Plan](plans/implementation-plan.md) is now the sixth main draft; detailed `docs/contracts/*` remain planned. Development defines delivery discipline; Progress records actual evidence and status. This document is not a test-results ledger. The [user-approved process revision](../.scratch/document-authoring-spec.en.md#f-user-approved-delivery-process-revision) adds W6 macro Implementation Plan and W7 joint review of six main documents for user review. Each independently developed milestone needs its own complete required Contract scope, reconciled interfaces and upstream prerequisites before implementation and verification; other milestones in the same macro Slice may remain pending. Under the 2026-09-19 CS5 refinement, completing one milestone does not complete its parent Slice: all necessary milestones and cross-milestone/integrated proof are required. The new sequence is later user authority, not a new product requirement or an original Grill decision. No legacy implementation/test result or file existence proves acceptance in the new repository.

**Sources:** Q2–Q5, Q11, Q22, Q26, Q32, S24.2, S37.1, S38.1. The language rule is the user's explicit authoring instruction.

## 2. Evidence and interpretation rules

### 2.1 Match the proof to the claim

| Subject | Required evidence approach | What that evidence cannot establish alone |
| --- | --- | --- |
| Domain/Application invariants | Deterministic checks of actual canonical inputs, command outcomes, before/after state, and immutable history through real boundaries | A displayed success sentence, resolved reference, or judge score cannot prove commit or consent |
| Concurrency, budgets, cancellation, recovery | Controlled competing operations and fault injection at the relevant durable/admission boundaries; actual calls, ownership, reservations, and writes | A successful restart or sequential happy path does not prove race safety or absence of remote replay |
| Tool conformance and model-visible data | Runtime admission/results, exact resources and permissions, actual Tool access and producing ContextFrames | Registration, a Package manifest, or final prose does not prove what was accessed or transmitted |
| Product interaction | Observable entry, selection, preview, confirmation, failure, and history behavior tied to canonical outcomes | A screenshot alone cannot prove atomicity, hidden-call absence, or correct version lineage |
| Semantic behavior | Declared real-path model Trials, appropriate task-scoped human review/calibrated judges, actual assessed inputs and outputs | Structural validity does not prove no omitted requirement, correct entailment, or real-world Candidate capability |
| Eval and telemetry correctness | Isolated fixture execution, controlled evaluator/observation failures, retained task results and per-check evidence | Missing spans are not proof of no violation; telemetry delivery does not determine business success |

Use controlled external adapters and isolated test state for automated scenarios. Real test-database commits exercise production invariants; no live Workspace mutation or real recruiting-account action is needed or authorized by these acceptance requirements. A recorded model response may drive deterministic tests, but must not be presented as live-model quality evidence. No alternative test Agent or bypassed Application/Tool guard is allowed.

Each eventual verification report must make the checked requirement/source, actual case/input/configuration, method, executed scope, observations, conclusion, and evidence limitations traceable. These are reporting obligations, not a new result schema. Required evidence must be available and admitted for the checker that consumes it; do not silently broaden access to complete a check.

**Sources:** Q26, Q32, Q82–Q83, Q117, Q173–Q180, Q184–Q187, S35.1; Architecture 15; [Agent Evaluation](.grill/eval/agent-evaluation.md), sections 1–6 and 16–20.

### 2.2 Outcomes, incomplete checks, and scope

Record the task's actual outcome separately from each check's conclusion. Expected rejection or deliberate non-action can satisfy a scenario. A proven violation, missing necessary evidence, evaluator execution error, and ambiguous expectation are different findings; their concrete encodings remain Contract work. A failed judge does not erase an established deterministic result. Task success does not imply every required check completed.

Do not omit failed or unassessable samples, count unavailable evidence as a pass, or equate Q168's valid unscored Analysis with zero quality. Report sample counts and unverified scope. Zero observed violations is limited evidence for the exercised cases, not proof that violations are impossible. Quality averages cannot offset unauthorized writes, confirmation bypass, forbidden access, exact-version violations, authority leakage, or silent replay.

Specialized semantic interpretation and comparison criteria are owned by [Eval quality and comparison criteria](evaluation.md#22-semantic-quality-reliability-and-efficiency-evidence).

**Sources:** Q117, Q168, Q175, Q179–Q180; Architecture 15.3–15.4; Product 11.

## 3. Workspace, Jobs, screening, and collection

**Behavior owners:** Product 2 and 4; Architecture 2–4. The scenarios verify independent capabilities and accepted source-specific admission, not a mandatory acquisition-to-application pipeline.

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Enter capabilities independently with their legal prerequisites | Advisor and Preparation require no completed Fit. The five accepted entries and contextual Preparation route work as specified; no extra top-level DeepFit/Preparation entry, Candidate or Company Aggregate, or required bookmark flow | Interaction/routing checks and owned-state inspection; Q1, Q6, Q23–Q24, Q53, S5.1, S5.3, S17.1–S17.4 |
| Maintain ManualApplicationEntry and click its URL action | Company/role/user-provided application URL remain a mutable record in a separate Job Pool view. Repeated edits create no JobVersion. Deletion physically removes its business row while retaining minimum replay protection under its Contract. Clicking opens the browser only; no formal Job creation, Requirements/Fits, targeted Advisor, Preparation, automatic Execution or Application History | Owned entry persistence, view isolation, browser-navigation boundary and absence of downstream business effects; [CG01-BC1](.grill/contract/sl-01-m1/decisions.md#cg01-bc1); [M1 normative proof mapping](#31-sl-01m1-contract-conformance) |
| Collect BOSS candidates with complete, missing, or invalid details | Only validated complete detail/JD atomically creates root and first version. Failure cannot leave an incomplete formal Job; there is no Manual root-only exception. | Adapter validation, transaction failure injection, persisted Jobs; Q44, Q48–Q49, S9.1; [CG01-BC1](.grill/contract/sl-01-m1/decisions.md#cg01-bc1) removes the Manual exception |
| Observe unchanged, semantically changed, stale, absent, and reliably closed listings | Unchanged content updates observation without a new version; semantic change creates an immutable version. Age/search absence does not imply closure. Verified closure blocks new automatic application but preserves history | Exact versions, observation provenance, derived availability and admission; Q7, Q44, Q48, Q50 |
| Admit candidates under a complete exact collection Preference version | Source query mapping and deterministic candidate admission follow the real consumer policy; keywords are not a returned-title substring gate. Missing/incomparable metadata is not falsely treated as conflict or satisfaction. No Candidate/Requirements/model screening is introduced | SL-08.M2 source/admission conformance, exact version and aggregate evidence; CG02-BC1/Q6–Q10; detailed representation remains pending |
| Attempt first acquisition with incomplete versus complete explicit Preferences | All six dimensions need legal explicit selections and successful Save before configured status. Missing/unfilled values or an all-empty object cannot authorize acquisition. Explicit no-constraint choices use each dimension's defined representation; no persisted recruitment-type unrestricted enum | Real Preference Save/read/configuration admission, later Collection preflight; CG02-S1; no QuickScreen PASS scenario |
| Configure recruitment types and required-education ceiling | CAMPUS/INTERNSHIP/EXPERIENCED/PART_TIME are selectable acquisition categories, not mutually exclusive source-field claims. MASTER expresses a Job requirement ceiling, not the Candidate's education. Unsupported source mapping is not fabricated | Preferences meaning checks in M2 and real adapter/admission checks in SL-08.M2; CG02-Q9; six-level vocabulary follows CG02-Q18; source mapping remains pending |
| Compare source salary and company exclusions during admission | CNY pre-tax monthly base salary uses the accepted interval distinction; incomparable pay remains uncertain. Company-name exclusion uses the agreed complete-name comparison without implicit group/fuzzy matching. Neither rule retrospectively filters saved Jobs | Future Collection/Job admission policy conformance; CG02-Q8/Q10, not an M2 screening implementation |
| Complete structured inputs and switch explicit UNLIMITED | Keywords require at least one valid item; the other five dimensions allow explicit no-constraint choices, mutually exclusive with effective concrete values. No comma splitting, implicit empty-list unrestricted state or validation only in UI. Invalid content fails the entire Save | Authoritative backend boundary plus later UI control/field-error checks; CG02-Q11/Q12; complete error/command representation remains pending |
| Admit explicit choices and exact canonical values | UNLIMITED forbids value; LIMITED requires valid concrete value. Salary uses exact integer-value semantics in [1, 300000], admitting equivalent numeric spellings without fractional rounding or string/bool coercion. Validate every item before deduplication; apply set/item limits, code-point text ordering and declared recruitment enum order | Future M2 raw JSON/canonical Save conformance; CG02-Q16–Q20; no implementation result claimed |
| Retry a successful logical Preference Save after current state changes | Same request identity/canonical content/precondition yields its original success without creating history or reverting current; changed input under the same key conflicts. Distinct concurrent first-save requests cannot both initialize | Future real request/receipt/transaction evidence under CG02-Q22/Q23; wire/error/storage follows PRF-012–020 and STO-014–020; runtime proof remains pending |
| Read and replay the declared Preference HTTP operations | Unconfigured read returns 200 NOT_CONFIGURED; configured root/version form one consistent snapshot; exact missing version is 404; Save returns original CREATED/UPDATED/UNCHANGED result even after later current advancement | Future route/result and competing-read evidence under CG02-Q26–Q28; no executed proof claimed |
| Publish within one millisecond or during clock rollback, then no-op/replay | Publication timestamps follow max(now, previous root.updated_at); root creation time stays fixed; no-op/replay leave business times unchanged. Tests impose no total historical ordering on UUIDv4 or created_at | Controlled clock and transaction fixtures under CG02-Q29; current pointer/revision checked for their own meanings only |
| Restart after a successful Save, including a no-op | Durable receipt reproduces original success; receipt and outcome commit atomically; no expiry, duplicate configuration authority or no-op business-state change | Future fault-injection/retention evidence under CG02-Q30; storage representation still pending |
| Submit malformed, duplicated-key, nested-invalid or oversized Preference requests | M2 rejects without mutation/coercion/truncation; media-type parsing permits compatible UTF-8 charset; non-identity encoding is rejected. Nested paths identify original submitted items without echoing unknown keys; byte/raw-item limits apply before canonical capacities | Future HTTP/parser/validation fixtures under CG02-Q31/Q32/Q35; M1 input/error behavior remains unchanged |
| Lose a Save response, retry a stale request or race same-ID requests | Preserve original request identity/precondition/content; admission precedes receipt replay, then ordinary revision/equality checks. One successful result survives races; current equality is not proof of that request outcome. Distinguish known non-commit from OUTCOME_UNKNOWN | Future controlled races/fault injection under CG02-Q33/Q34; shared error representation and operation-specific triggers checked separately |
| Read unconfigured Preferences or retained immutable history | Unconfigured current read succeeds without root/version creation. Published complete versions remain readable as retained content, not digest substitutes; reading one does not activate or roll back it | Future read/restart/retention evidence under CG02-Q24/Q25; no product check claimed |
| Perform first Preference Save or fail during first publication | Workspace startup creates no Preference root. First complete successful Save atomically creates root/version/current pointer; failure leaves none. Persisted root absence means unconfigured | Actual transaction/concurrency/fault evidence under CG02-Q15, after its detailed storage/command Contract is ready |
| Save changed, canonically equal, or stale complete Preferences | Successful real change atomically publishes an immutable PreferenceSetVersion and current authority. A current-revision canonical no-op changes neither version nor revision; stale revision conflicts before equality. Unsaved edits do not affect any Run | Real publication/concurrency/history evidence; CG02-Q3/Q4 with CG02-BC1/S1; normative equality/representation now follows PRF-002–010; runtime proof remains pending |
| Screen rejected versus passing/uncertain list candidates | Rejected entries receive no detail call and create no Job or recoverable rejected-content dataset; passing/uncertain entries proceed to complete-detail validation. Audit retains allowed usage/reasons without rejected title/company/URL/JD bodies | Controlled adapter access log, all persisted audit/data destinations, no RequirementParse call; Q49, Q110, S9.1 |
| Browse saved Jobs or change Job Pool view filters | Company/role query, city and other admitted view filters query saved Jobs independently. They do not Save Preferences, create versions, alter future Collection, delete/mutate Jobs or produce QuickScreenResult; browsing causes no implicit platform fetch | Actual view/query and authority-state checks at SL-08.M2; CG02-BC1; query fields/persistence remain later Contract work |
| Save new Preferences during collection, then stop | Active Run retains its exact immutable PreferenceSetVersion; later Runs may consume the new complete version. Saved Jobs are not hidden, deleted, marked preference-conflicting or made ineligible because Preferences changed. Stop prevents further accesses, retains commits and causes no restart | Deterministic interleaving, fixed version lineage, unchanged Job/query authority and retained results; Q161 partially superseded by CG02-BC1/S1 |
| Feed source payloads through an adapter | Only validated, consumer-justified canonical data is admitted. External transport shapes or available personal data do not become Domain or model authority | Controlled malformed/unneeded-source cases and admission checks; concrete mapping/validation depends on later Contracts and pinned research; Q3, Q27, Q49 |

Current eligibility, missing input, availability, material readiness, and event-derived application progress must remain distinguishable throughout these cases. Verification must not assert one universal Job lifecycle or demand excluded cross-platform/historical merging. Source access values from examples are not test constants establishing product defaults.

**Sources:** Q7, Q12–Q14, Q18, Q27, Q44–Q50, Q55–Q56, Q110, Q161, S9.1. Q13 is exclusion evidence; Q44/Q48 historically corrected Q17 admission wording. Later [CG01-BC1](.grill/contract/sl-01-m1/decisions.md#cg01-bc1) supersedes their Manual exception while retaining complete formal Job admission. CG02-BC1/Q6–Q10/S1 further supersede current-Preference re-screening and restore complete immutable acquisition versions. Collection admission is a future consumer policy, not an M2 QuickScreen or downstream Fit gate.

### 3.1 SL-01.M1 Contract conformance

This is required future proof for the real `2026-09-19.M1-r1` scope, not an executed result. Use the [development handoff](development/handoff/sl-01-m1-handoff.md) for preparation and [Progress](progress/traceability.md#61-sl-01m1-reviewed-scope-and-interface-evidence) for actual evidence.

| Scenario | Required proof and normative locator |
| --- | --- |
| Admit boundary values through server and frontend | Fixed trim/code-point counts, surrogate/control rejection, missing versus null, strict UUID, exact integral revision without rounding, unknown/read-only field rejection and sanitized errors. COM-025–032; MAE-002–004/016/018. |
| Save and read a real entry | Required seven fields, stable ID, explicit atomic Save, persistence across restart, unsaved-input preservation and complete separate list with deterministic ties. MAE-002/005/006/009/017; STO-003/004/009. |
| Retry/concurrently submit one create | Same normalized content/request converges on original identity; different admitted content conflicts; intentional new request allows duplicate content; entry/receipt commit together. MAE-007/008; STO-007/010. |
| Edit or delete from stale pages | Revision checks precede no-op; no lost update/recreation; max-revision no-op succeeds; clock rollback does not decrement updated_at or create a logical clock. MAE-006/010/011; STO-007. |
| Physically delete then replay create | No hidden business row/history; original receipt survives; old create returns original-deleted; historical ID cannot be reused. MAE-005/007/011; STO-003/004/010. |
| Lose a mutation response or inject commit failure | Confirmed success only after commit; known rejection/non-commit distinct from unknown; safe completion recovery is conditional, never command replay; post-commit response failure cannot certify rollback. MAE-014/016; STO-007/008/012. |
| Initialize/reopen controlled directories | Missing default may initialize; missing explicit fails; empty may initialize; nonempty unknown/incomplete/corrupt/unsupported fails without creating or upgrading. Atomic DDL/metadata verified at injected interruption points; normal SQLite recovery preserves valid storage. WSP-001–004; STO-001/003–006/011. |
| Run competing backend processes | Same resolved directory/aliases reject second owner before startup; locks do not pollute empty-directory recognition; owner crash allows reacquisition; multiple browser pages remain usable. WSP-002; STO-002. |
| Invoke every local HTTP route | Exact versioned paths, bodies/results, all success 200 and declared error mappings; generated client agrees with server schema; no framework-default shape, hidden command retry or deferred replay. COM-029–031; MAE-015/016/018; WSP-006. |
| Open a saved URL with controlled browser destinations | Waiting page alone is not success; only matching revision navigates; failures/closed/blocked contexts do not navigate or auto-replace; external page has no usable opener and receives no referrer. No page-load/application claim or business mutation. MAE-001/012/013; WSP-005/006. |
| Inspect UI and recover page state | Entries stay separate from formal Jobs; no fake available downstream features. Verification/refetch preserves dirty input; refresh loses only the explicitly non-durable pending request state and cannot auto-create. MAE-001/009/014/017; WSP-001/005. |
| Exercise privacy and local access | Appropriate local file permissions, loopback/Host/Origin enforcement, no automatic uploads; logs/errors lack business content, URLs, SQL parameters and fingerprints. Startup diagnostics stay non-persisted and outside HTTP resources. WSP-004/006; STO-011–013. |

Use real temporary SQLite files and process/browser integration for the relevant claims, with controlled destinations rather than live recruiting applications. Fault injection proves the injected boundaries only; it does not establish hardware failure immunity. Static Contract checks, fixtures alone and code existence cannot establish milestone acceptance. M1 needs no model-based Eval or BOSS/Provider integration merely to verify deterministic entry behavior.

### 3.2 SL-01.M2 Contract conformance

Required future proof for 2026-09-20.M2-r1; this table is not runtime evidence. Use the [M2 handoff](development/handoff/sl-01-m2-handoff.md) and [review mapping](progress/traceability.md#62-sl-01m2-reviewed-scope-and-interface-evidence).

| Scenario | Required proof and actual normative IDs |
| --- | --- |
| Configure six dimensions | Explicit modes, forbidden combinations, Unicode trim/control/length, integer-value salary, exact enum/order, every-item validation and canonical sets; boundary/raw JSON fixtures. PRF-001–006; COM-033–035. |
| Publish and retain authority | Lazy first root/version; immutable history; real change/no-op/stale/max revision; A→B→A; clock rollback and same-millisecond publications without UUID ordering. PRF-007–011; STO-015/016/020. |
| Compare and fingerprint requests | Independently constructed byte/golden fixtures, UTF-8 lengths, prefix/mode/precondition markers, field/set order; equivalent JSON spelling/key order/dedup input gives equal fingerprint, changed precondition/content conflicts. PRF-012–014/023; COM-032/037. |
| Race first Save and replay | Same-ID matching requests converge; differing same-ID input conflicts; distinct first requests cannot both initialize; no-op receipts survive restart; old success never resets current. PRF-008/009/012/014/017/019; STO-016/020. |
| Invoke exact HTTP and error paths | Three routes and exact objects; null precondition, GET rejection, UTF-8 media types, duplicate keys, 1 MiB limit, 1,000 raw items, original-index errors, UNLIMITED+value INVALID_FORMAT at parent. PRF-015–020; COM-033–036; WSP-007. |
| Read current and exact history | One consistent root/version snapshot; missing exact ID distinct from unconfigured; no implicit creation/current substitution; retained full content and equivalent JSON TEXT spelling. PRF-007/011/018/023; COM-037; STO-017/020. |
| Lose response or commit certainty | Original request retry only; distinguish known non-commit and uncertain outcome, including post-commit response failure; current equality proves no request outcome. PRF-021; STO-008/020. |
| Initialize/migrate/open | Real temporary SQLite source/target databases, exclusive process locks and interruption injection. Fresh schema 2 atomicity; normal schema-1 startup refusal; explicit atomic upgrade preserving live and deleted-original M1 receipts; no initial Preference root; no silent repair/fallback. STO-014–019; WSP-007. |
| Enforce persistence/privacy | Real database constraints reject cross-root current/receipt references and duplicate singleton; active constraints, retained original versions/receipts, restart durability, loopback/Host/Origin and no business payload/fingerprint logs. STO-015–020; WSP-007. |
| Deliver future UI | Structured chips, explicit UNLIMITED controls, salary/education explanations and inputs, backend field feedback, truthful Save/replay and recovery. PRF-022/021. Pending UI design; backend proof alone is not full M2 acceptance. |

M2 needs no live BOSS access, model invocation or semantic Eval. Run relevant M1 regressions against schema 2 to prove preserved Entry behavior; old schema-1 test results alone do not establish migration compatibility. Static document checks and review cannot replace runtime evidence.

<a id="4-saved-facts-resumes-grounding-and-derived-artifacts"></a>
<a id="42-removal-eligibility-and-historical-support"></a>
## 4. Independent Resumes, projections, and derived artifacts

### 4.1 Authority, import, and atomic Save

- Independently edit contacts/structured fields/body in A and B; neither changes the other. No Profile/Evidence Save or adoption prerequisite exists. Invalid document/ID/raw input rejects atomically; canonical no-op and receipt replay retain precise historical outcomes. Stale revisions conflict before equality.
- Save valid empty, contacts/Header-only and populated documents without a model; import review/cancel/parse-gap cases prove one confirmed Save and no earlier fact publication. Source success survives model/configuration/admission/output failure.
- Prove canonical AST↔TipTap text/marks/order/ID round-trip; edit/mark/reorder/paragraph↔listItem retains IDs; copy/paste/new gets new; split/merge and undo/redo follow RES-020. Cross-Resume ID transplant, duplicates and missing IDs fail. Entry/block units preserve exact source text; listItem and its editor paragraph are not double counted.
- Profile schema-v1 entries use source_entry_id/name/description/evidence_refs with exact same-Entry source support. Test invalid/cross-Entry refs, citation-valid unsupported claims, missing versus explicit-empty Entry result groups, empty final Profile and one-invalid-entry whole-result rejection. Header/contact/hidden URLs/project_url/other Resume/Memory never enter actual model Frames or Tools. No hidden URL fetch or second semantic-judge invocation.

### 4.2 Default lifecycle and historical support

- First-create races preserve one selected default; saved-default change atomically records durable rebuild obligation and receipt. Non-default Save, dirty drafts and rename do not rebuild. Presentation-only reuse proves equality, rebinds exact refs and records reuse; changed content invalidates only its owning Entry group. Explicit full refresh bypasses reuse.
- Test switch, ready refresh, failed refresh, duplicate refresh, page reload and same-default SET. A current pair is coherent and only READY is usable; no old/partial fallback. UI shows unavailable with refresh; new DeepFit rejects without dispatch. No source directs create/import.
- Exercise A→B→A, Save during build, replacement/remove/refresh during completion and two workers. Only latest source/build fence may publish. Crash after source commit cannot lose obligation; no uncertain remote replay. Complete durable response recovers locally; per-attempt model count ≤1, proven reuse count 0.
- Default removal shows next/previous preselection and permits manual choice; race rejects rather than silently reselects. Final removal clears selection/portrait; later creation works at noninitial selection revision. New-model histories survive ordinary removal and later default changes.

### Entry-scoped incremental portrait scenarios

- Modify one W1 Block or W1 background field: actual model input contains W1's entire admitted current background/Evidence and excludes unchanged P2, deleted text, prior Profile summaries and other Resumes. W1's prior group is replaced entirely. W1 and P2 may independently mention Redis without merging refs or dirtying P2. Verify every Entry kind, structured-only entries, copied/new IDs, local Block reordering and global Entry reordering.
- Delete a Block: rebuild its surviving Entry. Delete a whole Entry: remove its group and reuse other equal Entries with zero requests when no dirty Entry survives. A requested explicit empty group removes old capabilities; a missing/duplicate/unrequested group rejects the whole response. Validate reused and generated refs against the target exact projection before atomic publication. Empty final Profile is unavailable; no partial or stale fallback.
- From successful A1, fail A2 and then save A3: compare A1 against A3, covering every changed Entry. A different Resume is never a baseline. Switching B→A at unchanged exact A1 may reattach its latest successful compatible pair under the new current fence; multiple full refreshes of A1 must not resurrect an older interpretation; A at a newer source version needs a new pair and rebound refs. Incompatible generation rules require full generation; corrupt/missing required source is an integrity failure, not permission to assume equivalence.
- Verify current single-request dispatch for all dirty Entry groups, zero-call reuse/removal, full first generation, truthful MODEL/INCREMENTAL/REUSE provenance, current-source ordering and unchanged historical refs. Capacity overflow fails without truncation, silent batches, repair or retry. Actual semantic support/omission and input scope require EVO-028 Eval; compare meaning, not identical model wording.
- Refresh a READY or FAILED source with unchanged content: FULL regenerates all current Entries. Active matching FULL refresh deduplicates; active AUTOMATIC work is superseded with a new FULL fence and honest Invocation/cost disposition. Test same-key replay, two-worker claims, source/default changes, A→B→A, crashes around plan/response/merge/attachment and bounded recovery using the frozen baseline/plan, never a newer baseline or repeated remote request.

### 4.3 Demand and safe derivative recovery

Retain MAT/DRW positive, negative, concurrent and recovery acceptance for explicit exact demand, compatible Artifact/unfinished Work/new Work selection, independent receipts, fenced publication, bounded renderer and verified complete bytes. Replace old Profile/Evidence joins with complete schema-2 Resume source and schema-2 manifest. Empty Resume still renders; missing portrait/model never blocks rendering. Default/source/portrait changes do not retarget accepted demand or readable historical artifacts.

Verify actual PDF/PNG text, contacts/structured fields, marks/links, spaces, all fonts, pagination, long tokens, missing glyph failure and A4 page assembly under the registered pipeline. Metadata/hash alone is not visual proof. Exercise source/config corruption, dependency loss, timeout/live writer, crash/orphans, byte-unavailable/integrity failures, uncertain request and out-of-order polling. Frontend Draft preview is local; saved preview/export must display/download verified artifact bytes. [CG04 proof](contracts/foundation/derived-work.md#drw-026) survives except replaced source shape.

<a id="5-requirements-and-independent-fits"></a>
## 5. Requirements and DeepFit

### 5.1 Dependency preparation and bounded parsing

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Request Requirements with a compatible Set, or without one | Real Ensure reuses the exact usable immutable Set or starts an independent RequirementParse Run. DeepFit, Job-targeted optimization and Job-targeted Advisor use that exact Set as their sole Job-requirements input. Collection never initiates parsing; Generic optimization and ordinary Advisor requires no Job/Set. Successful dependency survives downstream failure | Actual Ensure path, exact sources/configuration, Run/result lineage and usage; Q10, Q14, Q24, Q58–Q59, Q110–Q111 |
| Return valid, invalid-then-valid, or repeatedly invalid extraction | Parse sees complete exact JD. Deterministic validation allows at most one guided repair within total limits; continued invalidity stops without persisting an untrusted usable Set. Downstream tasks cannot supplement from full JD | Actual Frames/calls, validation findings, canonical dependency, bounded failure; Q111, Q117, Q121 |
| Produce a structurally valid Set with no usable assessment targets | Stop before analysis; no empty-target perfect match, invented requirements, or extra repair allowance. Distinguish this dependency failure from valid unscored analysis | Usability check, downstream-call absence and result explanation; Q168, Q171 |
| Advance the active requirements default | New consumers may use the validated compatible default; historical consumers keep their exact Set. Creation and activation do not mutate old analyses | Immutable asset references and current selection; Q59, Q110 |
| Contend for one compatible parse across processes, cancel a waiter, or lose the owner | Database-backed claim admits one producer; a local mutex alone is insufficient. Waiter cancellation does not cancel production. Only owner pays; owner failure/cancellation/unknown outcome exposes unavailable dependency without takeover, budget transfer or automatic reparse | Controlled cross-process contention, actual invocations/charges, owner/waiter results; explicit Retry checks durable reuse first; Q142, Q144, Q159 |
| Call pure `job.requirements.read` with missing dependency | Return the missing dependency condition without model calls, nested Runs, new assets, or hidden platform fetch. Application controls visible preparation | Tool conformance plus Application orchestration evidence; ordinary invocation audit remains allowed; Q144 |

Semantic parser review must examine omission, hallucination, duplicate requirements, source support, and necessity/logic uncertainty using real-JD cases and manual inspection. JSON validity alone is insufficient. Uncertain meanings remain uncertain, not guessed labels. Section 13 defines the quality-evidence boundary without making illustrative metric names or parser certification mandatory.

### 5.2 Inputs, assessment meaning, and scores

Prove one CandidateJobFitAnalysis from exact Job/Requirements, ready Profile/Evidence and optional exact Preferences. Test no configured Preferences as unassessed, city/salary/blacklist mismatch as intent findings without blocking manual capability assessment, and unknown Job data as indeterminate. No duplicated stored intent in Profile.

Actual initial Frame uses a small capability index; controlled reads retrieve relevant block, expand entry and inspect more when needed. Test an ability absent from Profile but present in source, initial miss, denied/failed read, incomplete budget-limited coverage and complete source-bounded negative. Neither omission nor citation existence proves absence/support. Future score policy must preserve UNKNOWN and valid unscored results; numeric policy/result serialization still needs its own Contract review.

### 5.3 Freeze, concurrency, partial failure, and revocation

Freeze exact inputs at accepted analysis start. Switch/save/refresh while running must retain historical input and cost without latest substitution/restart; new run requires READY current source. Genuine revocation/unavailable exact input is independently enforced. Multi-Job batches preserve each accepted/undispatched/failed/unknown outcome; one success never establishes batch success. Historical results are not relabeled as current-compatible without the owned policy.

<a id="6-advisor-proposal-confirmation-and-session"></a>
## 6. Optimization and conversations

Verify generic and Job-targeted suggestions independently of DeepFit/global portrait. Selected populated B works while default A is empty; selected empty B yields the specific prerequisite message without a model. Actual Frames/history/summaries/Tools contain only selected Resume candidate content; test attractive but excluded abilities from default, other documents, Memory and chat assertions. Job-targeted mode adds only exact Job/Requirements as job context. No fabricated quantities, unsupported capability upgrades, Save/new Version/default switch/material demand occurs.

Durable ordinary/Job conversations reuse the optimization capability, preserving exact source, dependency waiting, honest failure/cost and complete durable suggestions versus streamed fragments. Session/permission rules still require later consumer-specific Contracts. Assistant apply/Proposal and Preparation adopt-back are explicitly deferred (SL-07.M3/SL-10.M2); their historical Scenario designs are future requirements, not current completion gates.

Prove one active foreground Turn per Session, explicit stop/new-input admission, dependency wait releasing Provider capacity while preserving deadline/cancel, no model polling or hidden parser takeover, and Session deletion cancelling active work without deleting committed business history. Pin the selected exact Resume for each task through default/source changes. Advice quality still requires relevance, specificity, actionability, clarity and factual support.

## 7. Preparation, execution, platform safety, and application history

Add a default switch, portrait failure/refresh and unrelated Resume Save between material selection, actual viewing, approval, freeze and execution. Exact selected material/consent must remain unchanged (MAT-033); none of those events grants external authorization.

**Behavior owners:** Product 7–8; Architecture 4.3 and 8. Use controlled channel adapters; exact render formats, readiness details and reliable read-back criteria remain later Contract/research work.

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Reenter unfinished Preparation, repeat creation, or find several resumable instances | Resume without silently replacing selected versions or Greeting; repeated requests do not duplicate creation. Multiple candidates require choice; explicit new/reapplication has its own chain. Concurrent edits detect conflict | Actual preparation identity/revisions and selected inputs; no required immutable version per reversible edit; Q16, Q25, Q42, Q162 |
| Edit Greeting or request body editing from Preparation | One fixed generic Greeting is manually editable, with no personalized/model-generated default. Body editing remains outside Preparation; it displays rendered formal Resumes | Interaction and call evidence, ownership of changed values; Q146, Q157 |
| Confirm unavailable material, rerender approved material, or change Greeting/material | Required artifact is viewable before confirmation. Approval binds actual frozen displayed artifact, exact sources and Greeting. Rerender cannot replace approval in place; Greeting change reconfirms; material change validates compatibility | Displayed-to-approved-to-frozen identity checks, readiness and current eligibility; equal bytes do not bypass stale facts; Q42, Q77, Q150, Q152, Q157 |
| Race Preparation/material changes against execution-snapshot freeze | Revision, exact reference, approval compatibility and artifact checks precede atomic freeze. Concurrent changes cannot produce a mixed snapshot or silently refresh the user's selection | Controlled freeze/modify interleaving, approved material versus immutable snapshot and retained Preparation state; Q42, Q77, Q150 |
| Freeze inputs, then attempt execution with only Snapshot/material approval or wrong/expired/reused scope | Snapshot and material approval grant no execution authority. Separate exact scoped, expiring single-use approval admits at most one Attempt. Concurrent consumption cannot authorize two attempts | Deterministic admission, actual approval consumption and adapter effects; Q25, Q30, Q150 |
| Live identity/availability check finds closure or mismatch | Stop further actions and require explicit refresh/repreparation; check does not create JobVersion/Requirements, replace snapshot, or invoke Job analysis | Controlled channel response, frozen sources, actual calls and business writes; Q164 |
| External outcome becomes unknown or only part of a batch completes | No inferred success or automatic replay. Verification is needed; continuation needs new narrower authorization. Preserve completed members; undispatched members are neither applied nor failed | Per-Job approvals/Attempts/outcomes and actual external calls; Q30–Q31, Q36 |
| Collector detects strong risk before Executor's next access, including after restart | Shared platform/account safety blocks affected later access across workflows, without merging budgets, recovery or approval. User handling and explicit restoration are required; no cooldown/account/tab/concurrency bypass or automatic restart/authorization | Persistent safety admission before each controlled access and independent workflow records; Q49, Q160–Q161 |
| Ordinary selector failure or predictable capacity shortage occurs | Do not automatically classify ordinary workflow failure as account risk. Policy-based capacity recovery does not stand in for strong-risk restoration or execution approval | Classified cause, subsequent admission and separate permission checks; classification details/limits await Contracts; Q160 |
| Observe a click/technical completion, reliable channel business fact, or human report | Only supported real business facts create ApplicationEvents. Human reporting targets a formal Job without requiring prior automated execution and cannot fabricate Executor/Snapshot/Approval history. ManualApplicationEntry URL opening creates no application fact or event. Unknown technical outcome is not an application | Controlled read-back or explicit human provenance, technical versus business event records; Q30–Q31 plus [CG01-BC1](.grill/contract/sl-01-m1/decisions.md#cg01-bc1) replacing the Q17/Q44/Q48 Manual-root path |
| Receive duplicate/delayed events, correct a report, or reapply | Deduplicate and preserve occurrence/observation distinctions; corrections/retractions append. Progress is a versioned-policy projection, not writable duplicate status. Reapplication creates a new real attempt; interviews remain events | Canonical event history, projection provenance and separate attempt identity; Q7, Q16, Q21, Q37 |

No universal channel sequence, live-site success demonstration, numeric platform quota, personalized Greeting, or mandatory Monitor is added. A future Monitor's use of shared safety is an extension boundary, not required v1 feature coverage.

**Sources:** Q7, Q16–Q17, Q21, Q25, Q30–Q31, Q36–Q37, Q42, Q49, Q77, Q91, Q108, Q146, Q150, Q157, Q160–Q164.

## 8. Harness, Tools, and actual Context

**Behavior owners:** Product 9; Architecture 9–10. Runtime conformance is proved deterministically; Agent Eval separately judges whether the model chose suitable actions or attempted forbidden ones.

### 8.1 Shared execution and action admission

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Execute primary work, repair, compaction, reactive rescue and MemoryExtraction | Every actual business Provider request passes the unique ModelInvocationRuntime admission/durable boundary. SDK retry/fallback cannot hide a second request. Static Skills remain separate bounded tasks, one semantic task per Run and one exact Job for Job-specific work | Controlled Provider requests correlated with actual invocation, budget and task scope; Q120–Q122, Q126–Q127, Q135, Q140, S7.1, S17.4, S22.1 |
| Register an action but deny it in Skill, Context policy, runtime permission, object scope or approval | Registration grants no permission. Reject impermissible execution before effect/exposure; model-generated IDs or parameters do not expand scope | Deterministic action/argument/object/permission checks and actual side effects; Q126, Q128, Q138–Q139 |
| Place instructions or unadmitted data in JD, webpage, Tool output, Memory or source references | Untrusted data cannot change protected control/consent. Returned content passes privacy/scope admission before a Frame even if the Tool itself was allowed | Actual access boundary and returned-to-model Frame checked separately; Q19, Q126, Q128, Q138–Q139, Q144 |
| Attempt generic Shell/SQL/file/HTTP/browser access or hide parsing/writes inside a read | No generic execution capability or duplicate optimization Tool appears. Reads cannot conceal platform/model calls or canonical mutation; ordinary invocation audit is allowed | Registry/permission review and controlled-call/state evidence; Q120, Q126, Q144 |
| Runtime rejects a model's forbidden request | Record model behavior and successful runtime refusal separately. Do not call the attempted request actual unauthorized execution, or hide an actual exposure in a favorable Agent score | Requested versus admitted/executed actions and actual returned data; Q173–Q175; Eval sections 14 and 16 |

### 8.2 Exact acquisition, reduction, and checkpoints

For Profile derivation protect complete admitted deterministic Evidence/background for each Entry in the frozen generation scope; for DeepFit protect the frozen index/job/intent and enforce exact progressive Evidence access. Prove per-result privacy and actual coverage, with UNKNOWN for incomplete inspection. For optimization protect the selected Resume only. No summary, Memory or latest source can substitute protected inputs (CTX-016/TOL-015).

Protected-input overflow and post-freeze revocation must also satisfy section 5.3. Compaction cannot turn incomplete or prohibited evidence into a complete Fit. Numeric triggers, watermarks, serialization details and exact checkpoint/Tool representations remain deferred.

**Sources:** Q19, Q47, Q72, Q80, Q83, Q94, Q120–Q126, Q128, Q132, Q134–Q144, Q158, Q172; [Context](.grill/harness/context.md), sections 4–20; [Tool Actions](.grill/harness/tool.md), sections 3–10.

## 9. Budget, durable execution, and recovery

**Behavior owners:** Product 5.4 and 9.2; Architecture 11–12. Exercise actual durable boundaries, not only successful completion followed by restart. Test amounts and timing controls are fixture choices, not product defaults.

### 9.1 Owners, reservations, and limits

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Race requests that each fit available budget but jointly exceed it | Atomic admission prevents oversubscription of both budget and local/total allowances; settled spend and outstanding exposure reduce availability. Check foreground and independent background owners | Concurrent reservation/dispatch evidence at the persistence boundary, not only in-process locking; Q124, Q130, Q135 |
| Settle once, settle again, overrun estimate, or restart with unresolved reservations | Settlement is idempotent; record actual overrun honestly. Restart/retry does not reset exposure, reserve twice, settle twice, or infer zero from unknown usage | Actual invocation/reservation/settlement lineage; overrun and reconciliation policy detail remains pending; Q122, Q124, Q140 |
| Have unused repair/compaction allowance after total budget/deadline exhaustion | No further call dispatches. Local ceilings do not add credit or reset across loop steps; deterministic reductions remain bounded without model charges | Complete admission/call history and aggregate limits; Q121, Q124, Q132, Q135 |
| Reuse parsing or coalesce several Turns for background extraction | Reuse incurs no second parse charge. Background work uses its own owner, not an arbitrary last Turn; current-Run compaction charges that Run. Judge cost is separate Eval cost | Per-owner actual calls and settlement; Q130, Q132, Q142, Q176 |
| Have money but no Context capacity, Provider headroom, runtime slot, or platform permission | Monetary balance cannot bypass other admission. Background work yields foreground capacity; insufficient budget/capacity preserves independently completed results and creates no Fit negative | Controlled resource conditions, dispatch/no-dispatch and independent outputs; Q123–Q124, Q130, Q155, Q160 |

### 9.2 Crash and cancellation boundaries

The rows describe known evidence boundaries and permitted behavior, not a new AgentRun state enum or transition matrix. Apply them to relevant primary/auxiliary/background invocations while retaining task-specific ownership and permissions.

Proposal-specific cases below apply only to deferred assistant application; generic command/runtime proof remains current. | Injected interruption or race | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Crash while local work is provably undispatched | Revalidate current exact inputs, permissions, budget/deadline and ownership before safe continuation; no silent update of frozen references | Durable absence of dispatch and controlled subsequent calls; Q122, Q124 |
| Crash after dispatch intent but before send, or after response receipt but before response persistence | Treat remote outcome as uncertain; neither missing complete response nor local belief authorizes replay. Preserve possible spend; no automatic fallback or success | Intent/response boundary, controlled Provider call count and exposure; Q122, Q135, Q140 |
| Crash after complete response is durable but before parse/validation/commit | Resume safe local processing without a second Provider request, including compaction-response recovery. Invalid response still fails validation rather than becoming authority | Retained complete business response, validation/publication and actual calls; Q122, Q125, Q132 |
| Crash after canonical commit or recover the same confirmed Proposal twice | Reconcile existing exact result; no duplicate facts/Resume/Analysis or repeated authority mutation | Persisted result/lineage and repeated recovery outcome; Q122, Q141, Q156 |
| Cancel/timeout, change owner, then let old coroutine return | Obsolete owner cannot publish canonical results or checkpoints. Releasing slots does not prove remote cessation or refund; retained usage remains truthful | Write-boundary fencing, actual late-write attempts and accounting; Q116, Q122, Q124, Q135 |
| Restart with stale/revoked input or an unfinished target slot | Startup reconciles durable boundaries, fences former owners and releases ended slots; stale/unknown work cannot become current through recovery | Startup result, exact eligibility/permission and late publication checks; Q116, Q122, Q136, Q172 |
| Explicitly initiate Run-level Retry for unknown remote work | New Run receives fresh admission and preserves original lineage/exposure; prior uncertainty is not erased or silently retried first | Old/new Run and invocation relationship, actual requests and budgets; Q122, Q124, Q140 |
| Recover a replay-safe local read versus an outcome-sensitive remote Tool | Replay is justified by the concrete action contract and current admission, never its name or a graph checkpoint. No generic exactly-once promise or reconsumption of execution approval | Controlled effects and actual action-specific proof; M1 controlled-read proof is specified in EXR-029/030 while production action contracts remain pending; Q30, Q122, Q126 |

The [SL-03.M1 deterministic Contract](contracts/evaluation/evaluation-observability.md) makes the following scoped proof mandatory for the actual Runtime/persistence with controlled adapters. Production SDK, business Tool and semantic Eval evidence remain later scopes; these rows are required tests, not executed results.

| M1 boundary | Required observable proof |
| --- | --- |
| Grant/revoke/regrant and uncertain grant acknowledgement | Generations advance only on grants; a matching stored owner alone cannot establish the winning live path; stale revocation cannot clear a replacement owner |
| Intent committed with lost acknowledgement while original path remains alive | Proven original winner with no adapter entry may continue once after confirming commit; crash/replacement/unknown entry cannot consume the intent |
| Existing response confirmation after Run ending, expiry or owner replacement | Identical verified bytes return the original immutable result without writes or a decoder dependency; different bytes conflict; no new publication permission |
| Legitimate durable response recovered after deadline | Only explicitly admitted bounded local work may proceed under valid qualification; no new remote dispatch, deadline reset or late first publication |
| Business completion reconciliation and ending race | Confirm whole-Run criteria, skip unnecessary response decoding, end only through lawful authority/atomic coordination and fence siblings; one committed result does not automatically complete the Run |
| Missing/corrupt payload or unavailable format/consumer versus unreadable storage | Confirmed required dependency failures converge affected OPEN Runs with the owned code; uncertain reads/failed ending commits remain honest; no Provider replay or unrelated startup failure |
| Complete oversized response versus stream stopped before termination | Only confirmed remote termination supports RESPONSE_TOO_LARGE evidence; incomplete reception preserves uncertainty and does not fabricate a durable/truncated response |
| Controlled exact-version local-read recovery | Reuse valid result or repeat the original unfinished Invocation only under its concrete pure-read agreement with fresh authority and unchanged exact inputs; no hidden Ensure, parse or business write |
| Restart with OPEN Run but no Invocation | Consult consumer completion/admission, do not invent remote intent, corruption or OUTCOME_UNKNOWN |
| Persistence evolution and format bytes | Forward migration preserves existing records, no historical Run backfill; per-format deterministic-byte fixtures, atomic publication and OPEN payload protection/terminal retention are verified |

### 9.3 Streams, presentation, and safe work

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Interrupt a half-stream, refresh, or explicitly Retry | Deltas are not formal Turns/Suggestions, extraction sources, recovery receipts or proof of Save. Do not join old fragments to new output; invocation uncertainty persists independently | Presentation versus durable response/Turn/business records and extraction scheduling; Q141 |
| Disconnect only the frontend while backend completes | Healthy backend is not automatically cancelled; reconnect can read its complete result without another task or mutation | Backend canonical result and reconnect/no-extra-call evidence; Q141 |
| Lose narration after Save, or recover demanded derivatives | Save survives reply failure; show committed result honestly. Safe derivative recovery obeys exact demand/currentness and cannot replay unknown model/platform effects | Canonical outcome versus narration and derivative trace; sections 4.3/6; Q147, Q152, Q156, Q165 |

**Sources:** Q116, Q121–Q126, Q130, Q132, Q135–Q136, Q140–Q142, Q147, Q152, Q155–Q156, Q165, Q169–Q172; [Budget](.grill/harness/budget.md), section 13; [Recovery](.grill/harness/recovery.md), section 14.

### 9.4 SL-03.M2 protected invocation conformance

The former SL-03.M2 Contract and conformance agreement have been withdrawn for S3 redevelopment. Their specific proof matrix is removed. Define replacement acceptance against newly reviewed Contracts before implementation; general system and consumer-specific acceptance elsewhere remains applicable.

## 10. Privacy, storage, and honest history

Test explicit offline development-store reset against configured data only: old DB/generated materials may be discarded, including test/preferences/manual-entry data; source/Git/configuration survive. Startup and reads must never reset silently. Fresh initialization has null selection and no shared Profile/Baseline; no old-format adapter, conversion or archive is required. Historical migration source/evidence remains documentary history, not a requirement to preserve old development records.

After initialization, prove atomic source/selection/build/receipt commits, exact root/version/logical-ID ownership, immutable pair/reuse lineage and retained historical analysis/material references through ordinary Save/removal/default changes. Corrupt stored lineage fails honestly without repair/current substitution. Preserve exclusive store ownership, sanitized diagnostics and protected payload storage; contact/Header/hidden URLs must not leak into model/Tool Frames, summaries or ordinary logs. Missing exact retained input is not permission to reconstruct from current content. Business history, Session, Memory and execution payload retention retain distinct owners.

## 11. Collaboration Memory

Prove Memory, recalled summaries and historical conversation assertions cannot fill missing default-portrait abilities or supplement a selected Resume in optimization, including apparently helpful hints. Existing collaboration-only controls/forgetting remain independent.

**Behavior owners:** Product 10; Architecture 14. Use supported production controls and actual source/admission paths. A learning-disabled Advisor Trial alone cannot demonstrate these learning scenarios.

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Offer a career/contact/search/application fact, temporary Resume choice, or one-off style request to learning/management | Memory owns collaboration semantics only. Business facts require their authorized owners, not extraction. Temporary scope/style remains Session-local; neither Memory nor style overrides fact/permission authority | Admitted/rejected candidates, business state and actual current instructions; Q127–Q129, Q133, Q138 |
| Provide explicit durable preference/correction versus inference, repeated behavior or a summary | Traceable durable expression may be admitted without an extra popup for every entry. Unsupported/ambiguous inference is not promoted; extractor output is only a proposal | Actual minimal user/assistant source, admission rationale, scoped semantic review and persisted result; Q127–Q129, Q139 |
| Combine learning-off/Recall-on, learning-on/Recall-off, and explicit management | Controls remain independent. Recheck learning at dispatch/publication and Recall at each new read/Frame. Management uses deterministic validation with no extraction call and works independently of both | Calls, actual Frames, retained entries and deterministic management results; Q137, Q139 |
| Reenable learning or start a new chat | No automatic old/disabled-period backfill, all-Session scan, or inherited temporary Job/Resume target. Existing entries remain independently governed | Pending sources, lookup scope and new Session inputs; Q127, Q137, Q139 |
| Run Parse/Fits, Advisor, or a checkpoint with Memory available | Parse/Fits see no Long-term Memory through any route. Advisor receives only allowed collaboration categories, not reusable learning by storage availability alone. Direct Memory stays outside checkpoint sources | Skill policy, actual Tool/Frame/checkpoint content, section 8.2; Q127, Q132, Q139 |
| Complete several durable Turns, restart before extraction, or interrupt streamed output | Eligible completed sources persist as pending work independent of a timer/Session-ended signal. Coalescing does not imply an unconditional call per Turn. Partial streams or extraction output do not recursively trigger learning | Durable pending ranges versus trigger/call history; exact scheduling/range representation deferred; Q127, Q130, Q139, Q141 |
| Fail extraction, exhaust its budget, or lack foreground headroom | Foreground result survives; independent background cost does not debit the last Turn. Waiting before dispatch differs from failed/unknown remote work | Separate task/budget/capacity and actual pending outcome; Q130, Q155–Q156, Q169 |
| Process new eligible sources after an old range fails or becomes unknown | New work can proceed without silently incorporating old failures or claiming their successful consumption. Old range requires explicit Retry; unknown remote work is not auto-replayed on restart | Exact source-range lineage, pending/retry decisions, actual requests and usage; Q169 |
| Edit/delete/clear Memory while an older extractor is in flight | Newer corresponding manual management wins; forgotten/superseded content disappears from admitted summaries/indexes. Old sources or late candidates cannot resurrect it; uncertain recurrence is conservative | Deterministic interleaving, admitted entries/derived lookup and source chronology; Q131, Q145 |
| Give a genuinely later durable instruction on a forgotten topic | Later legitimate instruction may be admitted under current rules; manual management is not an eternal lock. Rebuilding a derived summary cannot itself create or restore entries | Source/admission provenance and canonical versus derived Memory; Q131, Q145 |
| Delete source Session before dispatch or while extraction is running | Prevent new extraction and late publication from deleted sources; cancel where possible without claiming remote cost zero. Existing accepted Memory and committed facts keep independent lifecycles | Dispatch/publication source rechecks, late-candidate rejection, retained usage and independent assets; Q170 |

Exact category/interface types, source-range/cursor encodings, forgetting markers, triggers, retention and budget values await Contracts. Fixtures must not smuggle in career USER_FACT Memory, permanent topic locks, future Skills, or automatic historical backfill.

**Sources:** Q52, Q127–Q133, Q137–Q139, Q141, Q145, Q155–Q156, Q169–Q170, Q187; [Memory](.grill/harness/memory.md), section 17.

## 12. Eval execution and evidence integrity

<a id="121-isolation-exact-inputs-and-declared-experiment-scope"></a>
<a id="122-n1-and-complete-scenarios"></a>
<a id="123-evaluator-inputs-authority-and-conclusions"></a>
<a id="124-telemetry-regression-retention-and-re-evaluation"></a>

Agent task execution and its evaluation infrastructure require evidence of isolation, exact inputs, declared measured scope, Scenario integrity, admitted evaluator inputs and trustworthy observations. [Eval evidence-integrity criteria](evaluation.md#21-eval-execution-and-evidence-integrity) owns those detailed proof obligations, including telemetry, regression retention and re-evaluation; business/runtime acceptance remains in sections 3–11.

## 13. Semantic quality, reliability, and efficiency evidence

<a id="131-capability-specific-review"></a>
<a id="132-comparable-experiments-and-honest-reporting"></a>

RequirementParse, Profile derivation, DeepFit and Resume Optimization, Advisor, Context/Tool behavior and applicable learning behavior need task-scoped semantic evidence alongside their deterministic scenarios. Reliability and efficiency claims require evidence for their actual measured scope. [Eval quality and comparison criteria](evaluation.md#22-semantic-quality-reliability-and-efficiency-evidence) owns the capability-specific questions, comparison rules and limits; it defines no release thresholds or substitute for authority/permission proof.

<a id="14-pending-detail-exclusions-and-document-verification"></a>

## 14. Pending detail and exclusions

### 14.1 Requirements preserved while details remain pending

Pending detail prevents an executable oracle from being finalized where that detail matters; it does not erase the settled invariant. Do not invent an API, fixture field, error code, status, timeout, budget amount or release threshold to make a scenario appear executable. Later Contract work must reconcile affected Product/Architecture/Acceptance references before implementation.

| Pending owner/topic | Acceptance obligations already settled | Details still required |
| --- | --- | --- |
| Business/identity Contracts | Sections 3–7: complete admission, exact facts/history, saved authority, task-specific preflight and current eligibility | Actual fields, types, reference syntax/readers, per-function inputs, validation errors, schema and new-system evolution/migration detail; Q3, Q15, Q26, Q54, Q79, Q86, Q154 |
| Commands, concurrency, Proposal/approval and runtime Contracts | Sections 4–9: per-command atomicity and no implicit cross-Resume propagation under BC3, exact target/patch/impact, revision conflicts, single-use execution, fencing and no unknown replay | Command/API payloads, idempotency/target keys, approval lifetime representation, detailed transitions and transaction protocols; Q30, Q42, Q116, Q118–Q119, Q122, Q148–Q149, Q158, Q167 |
| Parser/Fit/ScorePolicy Contracts | Section 5: bounded valid dependency, no-target failure, exact scoped assessment, valid unscored results | Exact structured output/validation detail, score availability, numerical weights/formulae/comparisons; Q46, Q51, Q111, Q115, Q117, Q168, Q171 |
| Tool, Context, Memory, Budget and retention policies | Sections 8–11: least privilege, exact inputs, bounded work, independent controls, protected retention and truthful unknown costs | Complete action catalog, privacy/redaction interfaces, capacity triggers/values, source ranges/forgetting markers, allocation/overrun/reconciliation, cleanup/retention and storage layout; Q123–Q145, Q169–Q172 |
| Materials, source/channel Contracts and research | Sections 3–4/7: validated adapters, actual viewed material, frozen approved execution and reliable business evidence | Formats/channel readiness/read-back criteria, pinned upstream commits/licenses/mappings and verified selected platform capabilities; Q27, Q31, Q49, Q150, Q157, Q164, S7.1 |
| Eval Contracts/integration | [Eval acceptance](evaluation.md#2-evaluation-acceptance-criteria): exact isolated real paths, scoped evidence, semantic alternatives, per-check completeness and actual-output re-evaluation | Fixture/Scenario/evaluator interfaces, evidence schemas, metrics/matching/denominators, calibration measures, selected SDK/deployment verification; Q173–Q187, S35.1 |
| Later rollout policy | Section 2 and [Eval quality and comparison criteria](evaluation.md#22-semantic-quality-reliability-and-efficiency-evidence): separate hard violations, quality, stability, efficiency and absolute/relative comparisons | Trial counts, sample targets, thresholds, enablement, release consequences and repository/CI rules; Q175; Q117 certification remains deferred |
| Implementation planning, Development and Progress | Map accepted capabilities to proposed Slices and required Contract scope; maintain requirement-to-proof trace, test-first discipline and actual new-repository status | [Implementation Plan](plans/implementation-plan.md) is authored in W6; its milestone and parent-Slice completion conditions must reference this document's scoped and integrated proof obligations. [Development](development.md) requires Contract-ready development and defines general delivery rules; [Progress recording rules](progress/recording-rules.md) defines readiness/status/evidence recording; [Progress](progress.md) and its [matrix](progress/traceability.md) record actual state. Later Contract IDs, implementation/test paths and executed evidence do not exist yet; Q22, Q26, Q32, S37.1, S38.1 |

### 14.2 Excluded expectations and later extensions

Acceptance excludes rejected cross-platform merge/Overlay, KnowledgeConfirmation, invented Coverage/score ordering, persistent page-draft recovery and cooldown-only strong-risk restoration. Single DeepFit replaces the old paired analyses. Current suggestions do not require deferred assistant application/adopt-back or a suspended human-confirmation Run. Independent Resume-owned content and exact read-only block Evidence are accepted.

Unapproved vector/RAG and silent overflow fallback remain deferred; accepted exact Entry/Block Evidence acquisition is current DeepFit scope. Other explicit Product exclusions remain. No old fixture forces legacy compatibility; post-transition exact historical interpretation remains required.

High-level Contract families and architectural boundaries are owned by Architecture section 16; [Contract Structure](contracts/structure.md) owns their subordinate planned file organization. This document creates no Contract body or additional family. Source-maintenance supplements describe record organization/history and do not become product scenarios or permission to edit original records. The complete source-index disposition belongs in authoring handoffs and the [Progress matrix](progress/traceability.md), not fabricated product behavior.

**Sources:** Q4, Q13, Q21, Q23, Q53, Q81, Q100, Q109, Q112–Q113, Q115, Q117, Q121, Q123, Q127, Q131, Q146, Q148, Q158, Q160, Q163, Q166, Q175, S24.1–S24.2, S25.1, S26.1, S27.1, S28.1, S29.1–S29.2, S30.1, S37.1, S38.1.

<a id="143-the-two-document-verification-seams"></a>

Document-authoring review follows [Development 9.2](development.md#92-two-separate-verification-seams); it does not establish product acceptance or executed evidence.
