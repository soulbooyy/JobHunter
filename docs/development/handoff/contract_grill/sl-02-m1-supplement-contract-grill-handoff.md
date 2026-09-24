# SL-02.M1 Supplemental Architecture and Contract Grill Handoff

> **Closure notice — 2026-09-24:** This source-time interview prompt is fulfilled by accepted CG03S1-Q6–Q41/BC1–BC3 and [formal review/implementation handoffs](../../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope). Its unanswered/migration-preservation descriptions below are historical; Q38/Q41 authorizes explicit full development reset with no legacy conversion. Do not restart Q6 or restore old choices. No code/reset occurred here.

> Execute this session prompt in a new conversation. Formal documentation is English; interview and report to the user in Chinese. This is a transfer instruction, not a normative Contract or implementation proof.

[Supplemental decisions](../../../design/contract/sl-02-m1-supplement-grill.md) · [Original M1 decisions](../../../design/contract/sl-02-m1-grill.md) · [Progress](../../../progress.md) · [Scope and evidence ledger](../../../progress/traceability.md) · [SL-02 plan](../../../plans/slices/sl-02-saved-authority-materials.md)

## 1. Task and controlling user choice

Work in `/Users/soulboy/projects/JobHunter`. Use `/Users/soulboy/.codex/skills/grill-me/SKILL.md` and its underlying `/Users/soulboy/.codex/skills/grilling/SKILL.md`. Read them before applying them. The established session rule is five independent questions per ordinary round, each with a reasoned recommendation, followed by waiting for answers.

Complete a separately recorded SL-02.M1 supplemental Grill for a major source-authority change. Resolve its product and architecture boundaries, then publish the authorized architecture/Contract/plan/acceptance changes and a concrete implementation-impact handoff. Do not implement the backend/frontend or migrate databases in this task.

The user's latest and controlling selection is:

1. The Workspace supports multiple independently maintained Resumes.
2. One selected **default Resume** supplies the Workspace's user portrait. This is the Workspace default, not whichever Resume happens to be open or selected for a particular task.
3. Knowledge is extracted from that default Resume and stored for Agent/user-portrait consumption. Other Resumes must not silently add capabilities to that portrait.
4. Switching the default rebuilds Knowledge to form the new portrait. It does not union the old and new Resumes into a cumulative current fact library.
5. A capability absent from the source Resume cannot be treated as known merely because another Resume, a historical document or unrelated Memory mentions it.
6. The intended direction is Resume -> derived Knowledge. The user wants to eliminate reciprocal maintenance between an independently edited fact library and Resumes.
7. After formal writeback, explicitly tell the user which actual Slice milestones need backend changes, frontend changes, first implementation, or verification only. Write those deltas into their maintained plans/status records and development handoffs so the next implementing conversation can act on them.

This selection is accepted as CG03S1-BC1. Do not ask the user to choose again between a task-selected Resume, a basic/master Resume hierarchy and a union of all Resumes. An intervening message selected a task-specific Resume; the final message explicitly restored and clarified the **Workspace default** as the portrait source. Do not revive that superseded interpretation.

Do not infer that only one Resume can be saved. Do not infer that all future operations must use the default Resume as their output document. How an explicitly selected non-default document interacts with default-derived context is a downstream consumer question.

## 2. What is not yet decided

The accepted source direction does not freeze these implementation/product details:

- Whether all structured experience/contact values become directly owned Resume content, and the exact replacement for shared CandidateProfile editing.
- Knowledge's editable/read-only UI, source links, supported extracted categories and whether extraction is deterministic, semantic or hybrid.
- Whether and when editing/saving the current default rebuilds Knowledge; treatment of non-content presentation changes.
- Synchronous versus asynchronous rebuild, switching visibility, failure/retry, old-result access and in-flight task behavior.
- First use with no Resume, default removal/replacement, history retention and actual privacy erasure.
- Which old Evidence/Profile/Baseline identities survive as historical support or derived representations, and their migration.
- Whether Candidate Fit and Resume Fit remain separate internal/product capabilities, or a narrower analysis surface replaces them.
- Import confirmation, Advisor proposal application, automatic Save recovery, concurrent editing or merge.

Never convert an open choice into a DTO, example, test fixture, schema, default UI behavior or a claimed accepted requirement.

## 3. Required reading, in dependency order

Start with `git status --short`, current HEAD and applicable AGENTS.md. Many documents and the Candidate frontend were modified/untracked during this transfer. Preserve all unrelated changes; inspect the actual current state rather than resetting to the handoff checkpoint. Read current owners alongside relevant diffs where another task is publishing them.

### A. Navigation, state and workflow

Read these before deciding the interview frontier:

- `AGENTS.md`.
- `docs/index.md`, `docs/contracts/README.md`, `docs/contracts/index.md`, `docs/contracts/structure.md`.
- `docs/design/README.md`, `docs/design/contract/README.md`.
- `docs/progress.md`, `docs/progress/README.md`, `docs/progress/traceability.md`: distinguish original normative review, real code availability, frontend evidence and remaining acceptance.
- `docs/development.md`, especially documentation maintenance, Git discipline and §9.2's two verification seams; `docs/development/README.md`.
- `docs/development/repository-structure.md` and `docs/development/technology-stack.md` for implementation feasibility and ownership, not permission to scaffold new code.

### B. Effective decisions and existing source model

- `docs/design/contract/sl-02-m1-supplement-grill.md`: the sole record for this supplement, including CG03S1-BC1.
- `docs/design/contract/sl-02-m1-grill.md`: BC1/BC3, A1–A5, Q26–Q40, Q48–Q60, Q63–Q65, Q70–Q100 and further passages needed to trace affected rules. Preserve the original history.
- `docs/design/contract/sl-02-m2-grill.md`: exact-source/material projection, identity/currentness, derived demand and recovery decisions affected by changing what a Resume contains.
- `docs/spec.md`: Candidate Knowledge, Resume editing/import/defaults, Fit, Advisor and application material behavior.
- `docs/architecture.md`: authority/object inventory, version/lineage, Save/default selection, derived work, analysis/context, import/Advisor, storage and Contract ownership.
- `docs/acceptance.md` and relevant `docs/acceptance/evaluation.md`: positive/negative, concurrency, recovery, analysis-source and historical-read proof.
- `docs/design/grill-me-design-tree.md` and `docs/design/contract/contract-design-inventory.md` only where historical interpretation matters. Inventory examples and superseded architecture proposals are not current requirements.

### C. Normative bodies to read in full for direct impacts

- `docs/contracts/candidate/profile.md`: PRO-001–009, shared contacts, exact display, separate Save/adoption, material projection.
- `docs/contracts/candidate/evidence.md`: typed facts, standalone writes, retirement/history, Baseline and material projection.
- `docs/contracts/candidate/resumes-grounding.md`: especially RES-001/002/005/010/011/013/015/016, membership, source-provided fields, local content, source freshness and rendering reads.
- `docs/contracts/candidate/candidate-save.md`: request/result shapes, authority transactions, canonical equality, receipt/replay, revision/freshness, uncertain outcomes and any later consumer extensions.
- `docs/contracts/foundation/workspace.md`: default selection, first/last/removal and independent selection revision.
- `docs/contracts/applications/materials.md` and `docs/contracts/foundation/derived-work.md`: exact render inputs, output identity/publication/reuse, durable work and stale completion rules.
- `docs/contracts/foundation/storage.md`: existing migration/retention, relational lineage and persisted representations. Inspect the actual latest version rather than assuming schema 3 or 5 is still current.
- `docs/contracts/common.md`: applicable naming, IDs, errors, text, canonicalization and boundary conventions. Preserve older consumers unless an explicit scoped change is accepted.

### D. Consumer boundaries and milestone scope

Read `docs/plans/implementation-plan.md` and `docs/plans/slices/README.md`, then these plans for source-consuming portions:

| Plan | Actual milestones to inspect |
| --- | --- |
| `sl-02-saved-authority-materials.md` | M1 saved authority/Save; M2 demanded preview/export |
| `sl-03-invocation-requirements.md` | M1 runtime/recovery; M2 protected invocation/context; M3 RequirementParse/Ensure |
| `sl-04-resume-import.md` | M1 reviewed structural import |
| `sl-05-candidate-fit.md` | M1 single-target Candidate Fit; M2 selection/batches/rescoring |
| `sl-06-resume-fit.md` | M1 single-target Resume Fit; M2 selection/batches/rescoring |
| `sl-07-advisor.md` | M1 discussion; M2 Job-targeted discussion; M3 confirmed formal changes |
| `sl-10-preparation.md` | M1 ordinary Preparation/approval; M2 Advisor adopt-back |
| `sl-11-execution.md` | M1 authorized execution; M2 batches |
| `sl-12-collaboration-memory.md` | M1 manual Memory/Recall; M2 background learning |

Paths in that table are under `docs/plans/slices/`. This is an impact-search inventory, not a declaration that every listed milestone needs reimplementation. Follow references into SL-01/08/09 only when an actual dependency or scope change requires it. Search current bodies for affected symbols and rules, not only filenames.

Read any existing relevant bodies discovered through Contract Index, especially `agent/context.md`, `agent/tools.md`, `agent/execution-runtime.md`, `foundation/budget.md` and `evaluation/evaluation-observability.md`. Some were being published concurrently; verify status. Planned Fit/Import/Advisor/Memory/Preparation/Execution paths are not existing norms merely because Structure names them. Their future contracts need revised plans, not invented full schemas now.

### E. Development handoffs, API and implementation reality

- Automatically read `docs/development/handoff/sl-02-m1-handoff.md` and `sl-02-m2-handoff.md`. Their original preparation sections are historical; later transfer notes/current Progress and actual code determine availability.
- Read applicable SL-03 handoffs and other affected milestone handoffs if they now exist. Discover files instead of assuming their absence.
- Read `docs/api/README.md`, `docs/api/sl-02-m1.md` and `docs/api/sl-02-m2.md`. They are derived guides; they cannot supersede Contracts.
- Read `backend/README.md`, the actual manifest/lock and versioned migrations. Inspect `backend/src/jobhunter/application/candidate/authority.py`, its Domain/persistence/HTTP adapters, material source projection/renderer and relevant tests to locate real changes.
- Inspect `frontend/src/features/resume/editor/resume-editor.tsx`, `frontend/src/features/resume/preview/draft-preview.tsx`, Profile/Evidence editors, Candidate command recovery, entities/API schema and Candidate/Resume pages. Discover moved paths if needed.
- For UI obligations read `docs/ui/DESGIN.md` (this spelling), `frontend/README.md`, manifest, generated-client workflow and existing Candidate tests. UI implementations/screenshots remain consumers, not authority.

Read focused sections and expand along actual references. Do not read every historical Grill transcript before asking the first useful questions. If a fact requires independent lookup, follow the skill's bounded read-only research/delegation instruction; do not ask the user to locate code facts.

## 4. Entry facts and screenshot limits

The previous session's static inspection found that Profile/Evidence writes already leave saved Resumes unchanged. The remaining coupling was structured fields provided by exact Evidence versions, current-at-Save admission for newly selected sources, and explicit shared Profile/Evidence writes within the editor. This is a model change, not a confirmed automatic-propagation bug.

Original M1 Contracts are 2026-09-21.S2M1-r1; M2 material interfaces were subsequently published. Progress at the transfer recorded a schema-5 runtime and prior scoped backend/frontend evidence, with other documents still changing. Recheck this, and do not claim untracked frontend code is committed or rerun historical tests by citation.

The nowclaw screenshot showed categorized career information, source labels and an edit-Resume action. The user's explicit selection governs; do not infer nowclaw's hidden implementation. The screenshot does not authorize chat-memory facts, arbitrary local-document Knowledge ingestion, interview review, all pictured navigation or broad UI redesign. The new conversation must be understandable without access to the temporary image file.

## 5. Interview and persistent decision protocol

Maintain only `docs/design/contract/sl-02-m1-supplement-grill.md` for this supplement. Keep stable CG03S1 provenance IDs. The initial Q1–Q5 were asked before the architecture pivot and received no batch answers; mark them withdrawn, not accepted. Continue with Q6 unless the current register shows later answers.

For each ordinary round:

1. Ask five concrete, independently answerable questions in Chinese; each includes a recommendation, reason and relevant example. A question depending on an unsettled answer belongs to a later round.
2. Wait. Silence does not approve a choice. Amendments override only their actual scope.
3. Record accepted conclusions, rationale/boundaries, supersession and intended writeback destinations. Do not copy question transcripts or store unaccepted recommendations as decisions.
4. Recompute unresolved branches; ask narrow clarifications separately when necessary. Fewer than five remaining genuine decisions is acceptable.
5. Make scoped approved writeback only under the agreed phase/authorization. Do not silently publish unresolved architecture in Contract examples.

No arbitrary question/round quota. Keep questions understandable without exposing revision/lineage implementation concepts unnecessarily. A status question does not cancel the task; honor explicit pauses or requests for a plan before edits.

## 6. Required decision branches

Resolve these progressively; this is not a preapproved implementation:

- **Independent Resume content:** structured experience fields, rich body, contacts/Header, create/copy/remove, user edits and AI-proposed changes. Establish what the document owns and what source provenance still means; avoid circular Evidence -> Resume -> Evidence authority.
- **Knowledge interface:** categories, read-only versus explicit editing routes, source attribution, empty/partial source handling and unsupported claims. Contact privacy and model admission must not expand merely because portrait extraction exists.
- **Trigger and source:** initial default, saved default edits, non-default edits, set-default, no-op, presentation-only change and removal/replacement. Distinguish dirty drafts from committed source documents.
- **Rebuild and consumers:** default-selection switch versus portrait publication, success/failure/retry, stale/in-progress UI and exact source used by Agent calls. An old portrait must not silently masquerade as the new default. Decide whether consumers wait, reject or use explicitly identified historical inputs.
- **Concurrency:** A -> B -> A switching; source Save during rebuild; late completion for an obsolete source; simultaneous default changes; crash recovery; transaction versus durable-work boundaries. Do not freeze an implementation token before selecting the semantics.
- **History and existing data:** retained Resume/output/analysis history, old Evidence/Profile readers and receipts, unreferenced library-only facts, migration from actual current schema and preservation/export choices. The current-source rule does not authorize deleting historical/user data.
- **Import:** when uploaded/extracted content becomes a confirmed Resume, when portrait derivation starts, partial parse failure and user correction. The former two-phase Evidence-then-Resume decision requires explicit reconsideration, not accidental preservation or silent reversal.
- **Fit and Advisor:** default portrait versus explicitly selected non-default Resume; equality when both use the same Resume; whether two analyses still have useful distinct semantics; proposal source/target, explicit application and rebuild consequences. Do not silently delete a Slice or preserve redundant consumers just to retain an old plan.
- **Agent context and Memory:** user-portrait reads must use the accepted default source. Separate other legitimate task inputs and conversational memory from portrait authority; do not let them smuggle extra career capabilities into it. Freeze task inputs and switching behavior explicitly.
- **Materials and external actions:** render complete independently owned Resume content; preserve exact historical outputs and viewed-material consent. Default/portrait changes must not silently retarget prepared or executing applications.
- **Recovery UX:** source version management should not dominate ordinary editing, but hidden automatic merge/retry is not already authorized. Decide such behavior only if this revision actually needs it.

## 7. Architecture and normative writeback

Before broad edits, present a concrete impact/writeback plan with actual sections/IDs: old rule, accepted replacement, affected consumers, retained behavior, required proof and unresolved decisions. The user has requested the eventual writeback after this Grill; do not repeatedly ask permission for already authorized routine edits. If a newly uncovered material choice is unresolved, ask that choice before dependent publication.

After the replacement semantics are confirmed, complete the authorized documentation work:

- Update Product, Architecture, Acceptance and applicable Eval proof, including diagrams/examples and surviving references.
- Update actual Contract owners and required interfaces. Preserve published IDs; mark replaced core meanings with explicit supersession and new stable IDs. Never reuse an old ID for opposite authority semantics.
- Common retains shared naming/value/error definitions; new portrait/domain representation belongs to its chosen owner. Do not use CandidateProfile as a casual synonym for user portrait; it currently names the three-contact authority whose future must be decided.
- Reconcile Contract README/index/Structure, consumer scope maps, global Implementation Plan and affected Slice plans. Do not implement all future families merely to change their prerequisites.
- Update affected API guides as target integration references, clearly separating revised target contracts from still-running old backend behavior. Do not generate new client code against an unimplemented API and claim compatibility.
- Reconcile Storage evolution with actual migrations and retained legacy data; record required forward migration work. Do not modify published migration history or run a migration as part of documentary closure.
- Update actual progress/readiness and development handoffs as specified below. Preserve original decision/history and historical execution evidence with explicit current supersession notes.

The task ends with reviewed documents and implementation handoffs, not a partly implemented model. No code changes, dependency installation, database migration, commit or push unless the user separately authorizes them.

## 8. Required per-milestone backend/frontend impact handoff

This is a mandatory deliverable, not an optional final suggestion. Inspect actual implementation before classifying work. For every affected milestone, distinguish backend and frontend using categories such as:

- Existing implementation requires targeted adaptation.
- Existing behavior requires replacement/removal.
- Not implemented yet; implement first against the revised baseline.
- Verification only, with no identified behavior change.
- Unaffected, with a concrete dependency reason where initially suspected.

Do not label every touched Slice as a full rewrite. For example, command receipts or AST validation may remain reusable even when source ownership changes. Determine that from the reviewed result and code.

Put normative consumption/dependencies and completion conditions in owning Slice plans. Put actual state, affected requirement-to-code/test evidence, review revisions and blockers in Progress/traceability. Put executable cross-conversation instructions in milestone development handoffs:

1. Update `docs/development/handoff/sl-02-m1-handoff.md` in place. It is the user's stated backend implementation entry. Add a prominent current-baseline notice and a concrete new implementation-delta section; retain source-time implementation/verification history as history.
2. Update `docs/development/handoff/sl-02-m2-handoff.md` if source projection/render/storage interfaces change, with its own precise delta and prerequisites.
3. Discover and update other affected existing handoffs. Create an owning `sl-XX-mY-handoff.md` only when needed for the user's requested real development transfer, not as a generic completion report. Do not duplicate backend and frontend instructions across competing handoffs.
4. Keep this session prompt in `handoff/contract_grill/`; it does not replace those development entries.

Each affected development handoff must state:

- Revised normative scope/version and exact IDs; old rules no longer valid for new implementation.
- Concrete before/after behavior and payload/storage/UI implications.
- Actual code/API/migration baseline and known uncommitted work, with evidence limits.
- Reusable components versus required replacement, separately for backend and frontend.
- Migration/old-reader/API-client compatibility work and published-history constraints.
- Upstream dependencies and recommended implementation order, including staged backend/frontend integration.
- Positive, negative, concurrency, failure/recovery, historical-data and browser proof required for acceptance.
- Known open blockers; documents/commands the developer must read and verify before implementing.

The final user-facing result must contain a table: Slice.Milestone | Backend work | Frontend work | Upstream/order | Linked development handoff. Distinguish already changed documentation from code still needing work. Do not merely list document names or tell the user to ask another agent to assess impact later.

## 9. Progress and traceability update policy

Do not update both files after every five answers. Ordinary decisions and the unresolved frontier live in the supplemental register.

Update `docs/progress.md` when work starts, scope/dependencies materially change, review readiness is invalidated, or the revised publication closes. It provides the current concise state, not round history.

Update `docs/progress/traceability.md` for actual affected scope/IDs, explicit supersession, required interfaces, review evidence, implementation mismatch and new acceptance requirements. Preserve old executed test evidence for its old revision; do not claim it proves the replacement model. Split scopes if only a portion must reopen. An existing Ready label never authorizes implementing a conflicting new rule.

At closure, reviewed revised Contract scope may be Ready while implementation remains Partial/outdated/pending adaptation. Preserve established status vocabulary and explain the limitation; do not mark the milestone Implemented just because all documents are written. Keep unaffected consumers and parent-Slice remainder separate.

## 10. Closure checks

Perform both Development §9.2 seams:

1. **Decision-to-Document Traceability:** every effective accepted supplemental decision maps to a current owner/ID and required proof, or an explicit scoped exclusion. Reverse-check that new requirements have accepted provenance. Keep old superseded statements visibly historical.
2. **Cross-Document Semantic Consistency:** check default identity, exact Resume input, portrait derivation/currentness, independence, transactional/recovery boundaries, Agent consumers, material history, plans, readiness and all revised handoffs agree.

Additionally check stable ID uniqueness/references, file/anchor links, readiness counts, actual-versus-planned Contract paths, API-guide target/runtime distinctions and forward-migration instructions. Run the maintained `scripts/check_contract_links.py` and `git diff --check`; test the checker if changed. Do not weaken tooling to hide inconsistent IDs.

Do not claim runtime/browser/migration verification from documentation checks. If bounded research is needed, report precisely what was observed. No architecture proposal is validated merely by a successful demo or screenshot.

Before finishing, confirm that each affected developer can open the actual milestone handoff and identify the replacement work without reading this entire conversation. Report reviewed scope, stable IDs/supersession, checks, remaining implementation risks/dependencies and the required backend/frontend impact table.

## 11. First response in the new conversation

Read the focused current baseline automatically. Then provide, in Chinese:

1. A concise restatement of the accepted default-Resume source direction and the remaining major choices.
2. The initial owner/milestone impact map, distinguishing facts from impact hypotheses.
3. A dependency-ordered supplemental Grill outline.
4. The next five independent questions beginning at Q6, each with a concrete recommendation.

Do not ask the user to repeat the already settled direction or supply repository facts. Do not begin with a full schema rewrite, code changes or a blanket request for permission to start. Continue the decision -> scoped supersession -> formal review -> per-milestone implementation handoff workflow until the authorized documentation transfer is complete.
