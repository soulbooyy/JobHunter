# JobHunter Progress

> English is authoritative. Snapshot: 2026-09-19, SL-01.M1 backend implemented with 87 passing tests; frontend/browser integration remains pending. Contract scope readiness is unchanged. Historical W7/global approval remains separate. This document records actual state; target architecture, Contract structure and planned milestones do not establish implemented capabilities.

## 1. Current state and task

The user has started **SL-01.M1 — Local Workspace and Manual Application Entries** and approved [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1). This architecture/plan writeback separates the mutable ManualApplicationEntry from formal Job/JobVersion. It opens a user-provided URL only and cannot enter analysis, Preparation, automatic execution or Application History.

Formal Job semantics remain owned by planned `jobs/jobs-screening.md`; SL-08.M2 is its first planned producer and integrates collection, exact Job history and formal local views. SL-01.M2 supplies Preferences and pure QuickScreen without depending on Collection. Formal Job consumers now depend on the actual producer. The plan retains twelve Slices and 24 milestones.

The W7 handoff preserves review of the preceding baseline. The new scoped user approval does not retroactively approve every old baseline detail or reuse W7's PASS as evidence for new semantics. Current writeback checks are recorded in section 5. The original nine Grill sources, Inventory, Chinese authoring reference and historical handoffs remain unchanged; CG01-BC1 explicitly supersedes their Manual Job portions.

The [Contract Index](contracts/index.md) now lists **four actual M1 normative bodies and 24 still-planned destinations**. Common, Workspace, ManualApplicationEntry and Storage contain **69 stable requirement IDs** at scope revision `2026-09-19.M1-r1`. Their consumed M1 portions are Ready; all other 63 planning scope rows remain Pending.

The user accepted CG01-Q1–Q45's effective decisions (Q7–Q10 were stopped), including Q42's optional safe transaction completion and Q45's implementation-independent browser safety. Normative writeback and scoped interface reviews are complete. The backend subset is now implemented; see [operation and evidence](../backend/README.md) and the [M1 development handoff](development/handoff/sl-01-m1-handoff.md). M1 and parent SL-01 are **Partial**: UI design, frontend/browser behavior and integrated acceptance remain outstanding. M2 backend need not wait for M1 frontend; its own Contract prerequisites still apply.

## 2. Documentation and review state

| Work | Actual artifact/state | Remaining boundary |
| --- | --- | --- |
| Architecture Grill | Original register, six Harness records and Eval record; Inventory remains a checklist | Accepted provenance, not detailed Contracts or implementation |
| W1 Product | [Product](spec.md), authored draft; current plan availability reconciled | Earlier baseline reviewed in W7; CG01-BC1 behavior changes explicitly user-approved and reviewed separately |
| W2 Architecture | [Architecture](architecture.md), authored draft; high-level Contract families/boundaries retained, concrete catalog relocated to [Contract Structure](contracts/structure.md) | Earlier baseline reviewed in W7; CG01-BC1 authority changes explicitly user-approved; no normative detail added |
| W3 Acceptance | [Acceptance](acceptance.md), unified business/runtime proof; [Eval acceptance](acceptance/evaluation.md) owns specialized evidence criteria; authoring checks belong to Development | Backend scenarios executed; UI/browser and full acceptance pending |
| W4 Development | [Development](development.md), stable general discipline; [Eval guide](development/evaluation.md) carries specialized procedure | Backend tooling/code now established; see section 7 |
| W5 Progress/matrix | [Recording rules](progress/README.md), this summary and [matrix](progress/traceability.md); actual values remain unchanged | Original source records retained with scoped supersession; M1 Contract evidence now recorded separately from pending implementation |
| W6 structure discussion | [Structural handoff](../.scratch/contract-structure-grill-handoff.md), agreed CS1–CS5 | Detailed representations remain pending; historical fifteen-Slice proposal is not adopted |
| W6 Implementation Plan | [Plan](plans/implementation-plan.md) and [W6 handoff](../.scratch/w6-implementation-plan-handoff.md), authored; scoped seams/checks reported | Earlier allocation reviewed in W7; CG01-BC1 dependency revision user-approved; no capability completion |
| W7 joint baseline review | [W7 handoff](../.scratch/w7-joint-review-handoff.md): six main documents and current supporting plans/guides/records reviewed under both seams | Completed document review only; no runtime acceptance |
| User direction | Explicit M1 start and CG01-BC1 architecture/plan revision approved | Scoped approval; do not infer retrospective blanket approval of all earlier baseline detail |
| Detailed Contracts | Four actual M1 bodies, 69 IDs, four consumed portions Ready; 24 destinations remain planned | Other 63 scope portions remain Pending; backend evidence is separate from scope readiness |

Historical handoffs preserve their own evidence snapshots; obsolete whole-Slice/global Contract gates do not override current [Development 5](development.md#5-future-slice-planning-and-test-first-work). English remains authoritative for all formal work.

## 3. Implementation and verification baseline

The matrix retains **179 original source records (157 Q and 22 S), across 73 clause/topic rows**, with a new W6 planning destination/reason for every row. Locator coverage is separate from the source-topic and cross-document semantic review recorded in the W7 handoff; neither is runtime verification.

| Subject | Actual state |
| --- | --- |
| Current in-scope product/runtime/Eval capabilities | M1 backend implemented; overall M1 Partial, all other capabilities remain Planned |
| Explicit exclusions/deferrals | Preserve original clause-specific reasons; later scheduling does not itself mean Deferred |
| Planning locators | SL-01–SL-12 and 24 internal milestone locators exist in Implementation Plan; planning identifiers with a scoped user-approved CG01-BC1 revision, not Contract IDs or implemented capabilities |
| Contract readiness | SL-01.M1 has four complete reviewed consumed scopes and 69 IDs; other milestones remain Pending |
| Milestone implementation and parent completion | M1 and SL-01 Partial; no completed milestone or parent |
| Product checks/Eval/integration | Backend executable checks and scripts/check supplied; frontend/integrated proof and CI remain pending |
| Document checks | Historical W7 review plus the scoped CG01-BC1 two-seam review and mechanical checks in section 5; original handoff snapshots preserved |

Future evidence must identify the accepted milestone, parent, actual required Contract IDs and implementation/test/Eval locations. Ready Contracts are not implemented capability; accepted milestones are not completed parents. Parent completion needs all required milestones and integrated proof. Shared Contract changes can require rechecking earlier consumers and evidence.

### 3.1 Parent Slice aggregation

Parent completion and child capability availability are recorded separately. No complete milestone has been accepted; the M1 backend subset is available with the evidence in section 7. Future Partial/Implemented claims require evidence under [Progress recording rules](progress/README.md); an incomplete parent must still expose any actually accepted child scopes.

| Parent Slice | Aggregate implementation status | Accepted milestones | Required milestone work remaining | Parent integrated acceptance |
| --- | --- | --- | --- | --- |
| SL-01 | Partial | 0 / 2 | M1 frontend/browser/integration; M2 | Not executed |
| SL-02 | Planned | 0 / 2 | SL-02.M1, SL-02.M2 | Not executed |
| SL-03 | Planned | 0 / 3 | SL-03.M1, SL-03.M2, SL-03.M3 | Not executed |
| SL-04 | Planned | 0 / 1 | SL-04.M1 | Not executed |
| SL-05 | Planned | 0 / 2 | SL-05.M1, SL-05.M2 | Not executed |
| SL-06 | Planned | 0 / 2 | SL-06.M1, SL-06.M2 | Not executed |
| SL-07 | Planned | 0 / 3 | SL-07.M1, SL-07.M2, SL-07.M3 | Not executed |
| SL-08 | Planned | 0 / 2 | SL-08.M1, SL-08.M2 | Not executed |
| SL-09 | Planned | 0 / 1 | SL-09.M1 | Not executed |
| SL-10 | Planned | 0 / 2 | SL-10.M1, SL-10.M2 | Not executed |
| SL-11 | Planned | 0 / 2 | SL-11.M1, SL-11.M2 | Not executed |
| SL-12 | Planned | 0 / 2 | SL-12.M1, SL-12.M2 | Not executed |

### 3.2 Milestone and normative-scope records

The [milestone ledger](progress/traceability.md#5-milestone-implementation-and-acceptance-ledger) records all 24 children with separate consumed-Contract readiness, implementation, acceptance and evidence columns. The [Contract scope ledger](progress/traceability.md#6-contract-normative-scope-readiness-ledger) records independently consumed responsibility portions rather than file-wide completion. SL-01.M1 alone has Ready consumed Contract scope; its backend implementation/checks are recorded in section 7; full acceptance remains pending. The other milestones and other 63 normative portions remain Pending.

These are current records, not the hypothetical READY/COMPLETE/PASSED example. Once a milestone is actually accepted, update its own evidence and expose its capability even if its parent remains Partial. Parent Implemented requires every required milestone plus integrated acceptance. “Verified” belongs to acceptance evidence, not a new Q26/Q32 implementation status. A ready Contract scope or written code alone does not establish accepted capability.

## 4. Gaps and prerequisites

| Remaining work | Owner and boundary |
| --- | --- |
| Scoped design completion | M1 decisions and consumed normative scope are complete; later milestones require their own Grill and writeback |
| Selected milestone's normative scope | Contract Grill/writeback resolves exact expressions and both sides of needed interfaces; no requirement to finish the entire parent/file/family first |
| Research/preparation | M1 official-source findings and observed host limits are in the handoff; pin actual adopted versions and verify driver/lock/browser behavior during engineering preparation. Later collector/model integrations retain their own research prerequisites |
| Actual development/proof | Implement a milestone only after its own Contract/research and real upstream components are ready; execute appropriate deterministic and semantic evidence |
| Parent integration | Verify all required milestones and integrated behavior before declaring a macro Slice complete |
| Rollout/explicit deferrals | Q117/Q175 certification/rollout and post-v1 RAG remain separate; no new defaults, Trial counts or release gate |

## 5. Verification scope and next step

W7's two-seam PASS remains evidence for its source-time baseline in the [historical handoff](../.scratch/w7-joint-review-handoff.md). CG01-BC1 changes product boundaries and dependencies after that review.

**CG01-BC1 scoped Decision-to-Document Traceability Seam: PASS.** The accepted mutable-entry/formal-Job split is reflected in Product/Architecture, proof scenarios, plans, Contract organization and current decision records. Explicit partial supersession preserves formal complete JD, immutable snapshots and human reports for formal Jobs. Q1's 24 common rules remain unchanged. This reviews the changed clauses, not a new full-baseline or normative-Contract certification.

**CG01-BC1 scoped Cross-Document Semantic Consistency Seam: PASS after corrections.** Independent read-only reviews checked business/provenance boundaries and plan/scope dependencies. Corrections removed ambiguous producer implementation wording, added BC1 provenance to admission proof, clarified producer dependency versus fresh-collection/consent, corrected catalog/coverage remnants, added SL-08.M2 as a shared screening consumer and recorded immutable Preference storage separately. Reviewers rechecked those corrections with no unresolved finding in this scope.

Historical CG01-BC1 document-time checks on 2026-09-19 (before normative M1 writeback; current counts are in section 6):

- Twelve Slice files and 24 unique milestone definitions retained; combined required-upstream/reused-component graph has no cycle or unknown dependency.
- Twenty-eight planned catalog entries exactly match Contract Index. Zero normative bodies or requirement IDs have been created.
- Sixty-seven independently recorded planning scopes remain Pending, including entry/common/storage separation and the new explicit Preferences storage scope. No scope is marked ready by this writeback.
- No new broken local Markdown file/anchor references relative to the incoming snapshot; `git diff --check` passes.
- All 73 original traceability topic rows retain their source identifiers. Content comparison preserves all 22 protected source/reference/handoff files in the incoming snapshot, including the original nine Grill sources, both authoring references and historical handoffs.

These are scoped document-authoring checks and read-only review findings. They are not execution of the future `./scripts/check`, product tests, implementation evidence or milestone acceptance.

That BC1-only writeback did not establish readiness. The subsequent complete M1 Grill and normative review are recorded below; the earlier evidence remains a historical snapshot.

## 6. SL-01.M1 Contract review and handoff

**Consumed Contract scope: Ready**, revision `2026-09-19.M1-r1`. [Exact ranges, interface agreement, decision mapping and content hashes](progress/traceability.md#61-sl-01m1-reviewed-scope-and-interface-evidence) identify the four independently ready portions. The 12-Slice/24-milestone plan and formal Job producer/owner separation are unchanged.

**Decision-to-Document Traceability Seam: PASS.** Read-only coverage review compared effective CG01-BC1 and Q1–Q45 decisions with all four bodies, excluding unadopted Q7–Q10. All material accepted M1 decisions are represented; there is no formal Job scope drift or duplicate definition owner. The 24 shared conventions remain intact.

**Cross-Document Semantic Consistency Seam: PASS after corrections.** Separate read-only checks covered Entry/Common/browser boundaries and Storage/Workspace/schema/receipt/transaction boundaries. Corrections pinned URL validity separately from parser serialization, removed an unintended extra JSON numeric-spelling restriction, clarified that schema-recognition specifications are not runtime manifest files, bounded uncertain-commit recovery, handled response failure after confirmed commit, and changed browser context creation from an impossible guarantee to an observable request. Reviewers rechecked the corrected normative scope with no remaining substantive finding.

Document-time evidence: 69 unique requirement definitions with matching stable anchors and resolved cross-owner IDs; real catalog/index/scope agreement; source/provenance preservation and link/whitespace checks. Acceptance 3.1 now maps future proof to those IDs. Final mechanical checks also confirmed zero broken local Markdown file/anchor references, 28 catalog destinations matching four actual plus 24 planned bodies, unchanged 12 Slice/24 milestone definitions and all 73 original source-topic identifier rows. Original design sources and historical handoffs were content-hash checked; only the intended design navigation README changed outside the active register. `git diff --check` passed. These are authoring/review checks, not execution of product tests or the future unified runner.

The original Contract handoff recorded system Python 3.9.6 and no application artifacts. That historical observation is superseded for runtime adoption by section 7: uv-managed Python 3.12.13, pinned dependencies and real backend checks now exist. Client and browser adoption remain future work; the original research itself is not runtime evidence.

No normative family is globally complete by implication. Four of 67 scope rows are Ready; 63 remain Pending. No milestone is complete; the M1 backend subset and executed checks are recorded below. SL-01.M2 and parent integrated completion remain outstanding.

Directory relocation on 2026-09-19: Contract bodies and planned paths now follow the grouped [directory layout](contracts/structure.md#directory-layout); the Contract-to-milestone mapping remains in Structure. The M1 handoff and its inbound/internal links use `docs/development/handoff/`. Comparison with the incoming documents confirmed that all four normative bodies differ only in paths, retaining 69 requirement IDs/anchors, revision `2026-09-19.M1-r1` and the same readiness. The scope ledger retains the original review hashes alongside current hashes. Checks found no broken local Markdown file/anchor links; all 28 catalog destinations and milestone mappings agree, 22 historical/design source files remain unchanged, and `git diff --check` passes. This is documentation relocation evidence, not implementation or acceptance evidence.

## 7. SL-01.M1 backend implementation

Backend scope is implemented under the unchanged 2026-09-19.M1-r1 Contracts: local startup/ownership/recognition, atomic SQLite storage, six HTTP entry operations, retained create receipts, revision/idempotency admission, exact JSON/text/URL validation, sanitized errors, explicit Host/Origin boundaries and generated OpenAPI. Actual platform, locked versions and maintained install/start/check commands are in [Backend operation](../backend/README.md).

The final unified check passed: Ruff lint/format, Pyright strict (0 errors/warnings), **87 pytest tests**, 69-ID/matrix-reference checks and whitespace checks. Requirement-specific evidence is in [traceability section 7](progress/traceability.md#7-sl-01m1-backend-implementation-evidence). Tests use temporary databases, real SQLite, separate processes and loopback HTTP; no real user data or recruiting account is used. Current operating instructions live in the stable backend README; detailed requirement/test evidence stays in traceability.

Source now follows the prescribed Domain/Application/Infrastructure/API/Bootstrap layers; tests use semantic names under integration/conformance, with workspace startup separated from storage. The per-milestone backend report was removed; durable commands live in `backend/README.md`, test naming in `development/repository-structure.md`, and documentation maintenance rules in `development/README.md`. No new handoff was created.

No frontend project, UI dependency, TypeScript client, page, navigation or browser automation was added. MAE-013, WSP-005 and client portions of MAE-014/017/018 remain pending, as do real browser security and whole-M1 integration acceptance. The API alone does not establish those obligations. M1 and SL-01 remain Partial; scope readiness remains four Ready / 63 Pending.

Per the current user direction, M2 backend can start after the M1 backend component is complete without waiting for M1 frontend; M2 still needs its own ready Contracts. Milestone completion means every declared user-visible, backend, integration and verification obligation is covered, not a universal requirement to add a UI to milestones that have none. Full M1 does require its already-declared UI/browser scope. The user has now authorized committing the reviewed backend and organization changes; pushing is not requested.
