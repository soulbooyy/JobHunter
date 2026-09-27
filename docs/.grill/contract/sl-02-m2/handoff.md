# SL-02.M2 Contract Grill Handoff and Session Prompt

> This is a user-authorized cross-conversation prompt, not normative Contract text, implementation evidence or a new milestone plan. Follow it to conduct the next interview. Formal documents remain English; communicate with the user in Chinese.

[Milestone plan](../../../plans/slices/sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) · [Contract Structure](../../../contracts/structure.md) · [Actual Progress](../../../progress.md) · [M1 normative review](../../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) · [M1 decisions](../sl-02-m1/decisions.md)

## 1. Task and intended outcome

Work in `/Users/soulboy/projects/JobHunter`. Start **SL-02.M2 — Demanded preview and export Contract Grill**, using the user's `$grill-me` skill at `/Users/soulboy/.codex/skills/grill-me/SKILL.md` and the underlying skill it invokes. Read their actual instructions before applying them. The session-specific workflow below takes precedence over a generic skill instruction to ask the entire frontier at once.

The user wants to understand the exact data and behavior that development will implement, rather than only understand the high-level architecture. Use a progressive interview to establish the actual product capabilities, owners, objects, fields, relationships, commands, state transitions, persistence, concurrency, recovery, HTTP/client obligations and required proof consumed by this milestone.

Complete the actual consumed scope, not every future responsibility in a containing file or family. At the end, after explicit user confirmation that the decisions are settled, publish reviewed normative definitions with stable IDs, coordinate required interfaces, update scope readiness and prepare a concrete development handoff. Contract readiness and implementation/upstream readiness are separate.

Do not implement backend/frontend features, scaffold a renderer/worker, install dependencies, migrate user data, commit or push during the interview. Read-only inspection and scoped research are authorized. Discuss necessary UI behavior, but actual frontend implementation remains deferred until UI design. A later explicit user instruction may authorize publication, development or Git actions independently.

## 2. Required context acquisition

Begin with `git status --short` and applicable AGENTS.md instructions. Preserve unrelated changes, generated assets and other conversations' work. A dirty working tree is not evidence that the milestone is implemented.

Read the relevant current owners before the first questions:

1. `docs/index.md`, `docs/contracts/README.md`, `docs/.grill/README.md` and `docs/.grill/README.md`.
2. `docs/progress.md`, `docs/progress/recording-rules.md`, and relevant sections of `docs/progress/traceability.md`, particularly actual upstream implementation and Contract readiness.
3. `docs/plans/implementation-plan.md`, `docs/plans/slices/README.md`, and both milestones in `docs/plans/slices/sl-02-saved-authority-materials.md`.
4. `docs/spec.md` sections covering Resume editing, saved materials and future application preparation; `docs/architecture.md` sections covering independent authority, rendering/demand, local recovery, Storage and Contract ownership; `docs/acceptance.md` especially §4.3, §9.3 and §10. Locate actual headings rather than assuming line numbers.
5. `docs/contracts/index.md`, `docs/contracts/structure.md`, and the actual bodies consumed here:
   - `docs/contracts/applications/materials.md`;
   - `docs/contracts/candidate/resumes-grounding.md`;
   - `docs/contracts/candidate/candidate-save.md`;
   - `docs/contracts/foundation/storage.md`;
   - `docs/contracts/common.md`;
   - `docs/contracts/foundation/workspace.md`, `candidate/profile.md` and `candidate/evidence.md` where referenced.
6. Check whether `docs/contracts/foundation/derived-work.md` now exists. If not, read its planned Structure entry; a planned filename is not a normative body. Do not create an empty placeholder.
7. `docs/development/handoff/sl-02-m1-handoff.md` and any newer applicable transfer. Reconcile their source-time snapshots with current owners and actual code.
8. `docs/.grill/contract/sl-02-m1/decisions.md`, focusing on BC1–BC3/A1–A5, UI1, Q36–Q47, Q59–Q66, Q86–Q100 and especially Q95. Read further provenance only where interpretation requires it.
9. Relevant portions of `docs/.grill/contract/contract-design-inventory.md`, original `docs/.grill/grill-me-design-tree.md`, and the Harness storage/execution records referenced by the current owners. Inventory examples and historical proposals are not finalized schema.
10. `docs/development.md`, especially §9.2, plus `docs/development/repository-structure.md` and `docs/development/technology-stack.md`. Inspect actual manifests, backend README, migrations and affected code when implementation facts or integration feasibility matter.

Do not read the entire repository or all original conversations merely to begin. Resolve facts through targeted search and current owners; deepen the relevant branch as needed.

### Baseline at this handoff's preparation

SL-02.M1 Contracts were published as **2026-09-21.S2M1-r1** and committed in `9667ab5` (`docs(contracts): publish SL-02.M1 saved authority contracts`). The scope has 73 new IDs, 178 total repository requirements, and eight reviewed S2M1 portions. This snapshot does not freeze repository HEAD or future counts.

At M1 publication, actual backend runtime was schema 2, while M1's new schema-3 implementation was not started. Prior schema-2 tests were inherited evidence, not evidence for S2. **Recheck actual code and Progress now**: another conversation may have implemented M1 since this snapshot. M1 Contract Ready alone cannot establish available exact readers, actual migrations or passing backend tests. Missing implementation does not prevent independent M2 Contract discussion, but it must remain an explicit development dependency.

## 3. Controlling boundaries to preserve

Do not ask the user to reconfirm these unless a concrete new conflict makes a scoped change necessary:

- Candidate Knowledge/Evidence is the sole fact authority. Profile owns the three contact values. Resume owns exact source selection, local expression and presentation.
- A saved ResumeVersion binds exact Profile/Evidence versions. Existing historical/retired Evidence bindings remain valid lineage. Later source updates/ordinary retirement do not automatically change that Resume, its local text/marks/links or its material compatibility solely because source current pointers moved.
- New or switched references entering Resume Save have their already-published freshness rules; unchanged historical references do not become current-only again.
- Source availability, permissions, document changes and renderer/demand configuration remain distinct concerns. Historical lineage is not semantic grounding or a permission bypass.
- Editor-local Draft A4 preview is already M1's frontend obligation and is not a durable saved artifact. Do not move this entire obligation to M2 or treat a Draft preview as PDF/export readiness.
- M1 owns saved authority, exact readers, consistent source/currentness boundaries and receipts. **CG03-Q95 explicitly places first delivery of real material demand/configuration/durable intent/work/output/recovery in M2.** Do not assume M1 supplied a render queue or intent protocol.
- Where an existing actual material demand requires intent on Save, M2 must extend the owning Save transaction atomically. A lossy post-commit event is not a substitute. Rendering itself happens after commit; rendering failure cannot roll back a successful Save.
- `materials.md` owns output meaning, exact material lineage and readiness; `derived-work.md` owns demanded local work/claim/reuse/recovery/publication; `candidate-save.md` owns atomic command participation; `storage.md` owns persistence/recognition/retention/integrity. Do not create competing owners of one state.
- Safe local rebuilding/recovery does not authorize repeating model calls, browser submissions or other external effects.
- No eager all-format generation, generic universal job framework, new Aggregate, new Analysis or all-family readiness gate is justified merely by this milestone.
- Preparation approval, Greeting, authorization to send, automatic application execution and Application History remain outside M2.
- Existing Common naming, scalar and error conventions are the default. Common alone owns shared error vocabulary/representation; business owners define triggers. Do not duplicate error-code systems.
- Published requirement IDs are stable and never reused. Preserve old consumer behavior unless the user explicitly approves an affected change and its interface reconciliation.

Read the current exact clauses, especially MAT-001–003, RES/SAV and STO S2 additions, rather than relying only on this summary.

## 4. First response in the new conversation

After reading, give a concise Chinese orientation containing:

1. The intended M2 outcome and its exclusions.
2. Current actual upstream state, separating Contract availability from code/test availability.
3. A proposed owner-to-consumed-document map, including M1 portions to reuse and actual M2 additions.
4. A dependency-ordered Grill outline and the main factual research gaps.
5. The first **five questions, Q1–Q5**, with clear recommended answers and reasons.

Do not start by asking permission to read files, create the decision record or begin an already-authorized interview. Do not merely return a plan and offer to start later. Do not publish unreviewed schemas as norms.

If a prerequisite fact is not yet available, work on other independent branches; never ask the user to supply facts you can look up. Follow the skill's bounded delegation instructions for factual lookups/reviews where available. Agents may find facts and review consistency; they cannot decide product choices on behalf of the user.

## 5. Five-question round protocol

Use five questions per ordinary round, consecutively numbered across the milestone. Each question must be independently answerable from already settled prerequisites. Do not place a dependent question in the same round as the unsettled decision it depends on.

Format each question in Chinese:

❓ **Qn — Concrete decision title?**

Explain the actual user/developer consequence and the alternatives only where useful.

➡️ **Recommendation:** Give a concrete proposal, its reason, the owner and an example/edge case when needed.

Questions must elicit decisions, not vague agreement with an entire framework. Avoid packing unrelated decisions into one oversized question. Explain fields in familiar language with examples; do not assume the user knows renderer, storage or concurrency jargon.

After presenting a round, wait for the user's answers. Do not treat silence as acceptance. Interpret “all agreed” as agreement only to the immediately presented batch, subject to the user's amendments. Partial acceptance must retain unresolved parts; an amendment overrides only the affected proposal. Keep no more than five unresolved ordinary questions active.

After each answered batch, before asking the next batch:

1. Resolve exactly what was accepted, rejected, amended or superseded.
2. Persist accepted conclusions in the single decision record.
3. Update affected current Product/Architecture/Acceptance/plan/scope owners where the approved decision changes them; keep them consistent.
4. Recompute the decision frontier and identify research or downstream questions newly enabled.
5. Run appropriate targeted documentary checks and briefly explain the result and remaining uncertainty.
6. Present the next five independent questions unless the user has asked to pause questions or the frontier has closed.

A narrow clarification discovered during writeback may be asked separately; do not manufacture four unrelated questions to fill a batch. If fewer than five real decisions remain at the end, say so and ask only those. Do not extend the interview to hit an arbitrary round count.

When asked how many rounds remain, estimate from the current unresolved branches, explain uncertainty, and update the estimate after major scope changes. Do not promise a fixed number or copy M1's 100-question count as a quota.

## 6. Persistent decision tree

Use one file:

`docs/.grill/contract/sl-02-m2/decisions.md`

If it already exists, inspect and continue it; do not replace earlier work. Use the structure/style of `sl-02-m1-grill.md` and `docs/.grill/grill-me-design-tree.md`.

The record contains conclusions and provenance, **not original question text or a transcript of recommendations**. Maintain:

- Milestone, purpose, current session state and last answered batch.
- Verified upstream snapshot and controlling inherited boundaries.
- Required definition owners and consumed scopes.
- Stable decision locators, accepted result, rationale where useful, invariants, relevant boundary examples and actual writeback destinations.
- Explicit rejected/superseded branches and their replacement links.
- Current dependency frontier and genuinely unresolved details.
- Scoped verification/publication records, not runtime claims.

Check existing namespaces before selecting the next milestone namespace. If CG04 is unused, use CG04-Q1 onward; conversational questions remain Q1 onward. Architectural changes may use a stable BC locator with linked question decisions. These are provenance IDs, not normative requirement IDs.

Keep original accepted history visible and mark later scope corrections explicitly. Do not leave old text marked ACCEPTED as if it still controls without a clear later supersession note. Do not reset numbering after compaction or a resumed task.

Do not create per-module `storage-decisions.md`, rendering decision logs, duplicate decision trees, daily completion reports or copies of the same decision in several provenance files. Current normative definitions eventually belong only to their proper Contracts; the record links them.

## 7. Expected decision branches, ordered by dependencies

Use this as a coverage checklist, not a frozen schema or mandatory set of new objects.

### A. Product demand and deliverable scope

Clarify actual saved-source preview/export entry points, supported first-release output formats, what constitutes a user's demand, and visible success/failure meanings. Distinguish local Draft preview, durable preview, export/download and future Preparation use. Establish what must be ready to perform each action and what may remain unavailable.

### B. Exact inputs and rendering semantics

Clarify exact Resume/source binding, use of local expression and structured facts, renderer/template/font configuration, compatibility/version meaning, A4/pagination, overflow, missing glyphs and layout failure. Research actual feasible rendering/font options before claiming guarantees. Existing font enums/settings remain inputs, not automatic proof that matching font assets are installed/licensed or PDF output is deterministic.

### C. Material identities and output relationships

Determine which distinct concepts actually need identities, immutable versions, relationships, checksums/media types, manifests, payload locations and timestamps. MaterialBundle/Artifact/RenderManifest are planned responsibility names, not permission to freeze examples without a consumer. Separate database identity, filesystem location, download address and content equality.

### D. Demand, reuse and publication

Clarify exact target/compatibility keys, current versus historical demand, output/work reuse, concurrent requests, obsolete work and publication fencing. State what changes really invalidate compatibility. Do not silently infer obsolescence from unrelated Knowledge/Profile current pointers.

### E. Atomic Save and explicit-demand interfaces

Specify how actual durable intent joins a Save or later demand command, with precise transaction participants, revision/idempotency boundaries and results. Preserve independent fact/document commits. Determine what replay means after newer Resume or demand changes. Reuse the existing Candidate Save namespace/protocol only if semantically applicable; do not automatically merge unrelated namespaces.

### F. Local execution and recovery

Only after product/demand semantics are settled, define necessary persisted work states, claims, leases/fencing if justified, attempts, cancellation, retry, startup/crash recovery, partial-file handling and failure classes. Distinguish command uncertainty, work outcome, artifact validity and client observation. Local safe work recovery cannot replay remote/model effects.

### G. Stored and served bytes

Clarify atomic file publication versus database commit, source/manifest/file consistency, reads/downloads, path validation/access, historical retention, cleanup and missing/corrupt bytes. Establish actual disk/size limits and retention consumers without inventing a comprehensive backup/erasure product. Research implementation facts before freezing filesystem guarantees.

### H. Wire representation and client behavior

Complete field names/types/requiredness/null/empty distinctions, enums, canonical equality, numeric/time units, schemas, HTTP methods/routes, envelopes, errors and validation precedence. Define polling/refresh/download behavior, stale observations, retries and honest UI messages. Common owns shared error structures/codes; materials/work owners supply triggers. Add body/node/depth limits only for the actual interfaces and formats consumed.

### I. Migration, conformance and development readiness

Inspect actual current schema before selecting the next schema version; do not assume M1's planned schema3 is already implemented or that M2 must blindly choose schema4. Preserve published migrations and prior consumers. Define exact failure/concurrency/restart/history proof and interface agreement. Distinguish Contract Ready, actual upstream availability, frontend prerequisites and full parent-Slice completion.

## 8. Research and fact-finding discipline

Use focused research only where a pending decision requires it: renderer and PDF behavior, fonts/license/distribution, browser print limitations, deterministic layout, local file publication/recovery, existing storage primitives and current client/API capabilities.

Pin versions or commits and use primary documentation. Separate observed facts, inference, recommendation and accepted decision. Do not turn a library default, example payload, existing UI screenshot or speculative future consumer into authority. Avoid adopting a whole stack or general worker framework before demand and recovery needs are established.

Store necessary research evidence in the single Grill record or the existing appropriate engineering owner, with source/version and implications. Do not create a competing normative definition. No dependency installation or production-data experiments are authorized by research alone.

## 9. Handling architecture or milestone supersession

If an answer conflicts with a published invariant, ownership boundary, transaction/recovery model, milestone allocation or prior accepted decision:

1. Identify the exact conflict and affected current owner/requirement IDs. Distinguish a proposal from a previously accepted rule.
2. Pause dependent questions. Give a concrete writeback plan: documents and actual sections, old meaning, proposed replacement, necessary interfaces, acceptance and readiness impact.
3. Ask only unresolved architectural choices. If user authorization already clearly includes a specific writeback, proceed within it; if the user requests “plan first,” honor that and wait for approval before changing the affected owners.
4. After approval, write the scoped supersession, preserve historical provenance and update all current consumers affected by the change.
5. Recheck both verification seams, then resume ordinary questions from the revised frontier.

Do not silently repair a conflict in DTOs, examples, diagrams, SQL or tests. Do not postpone an accepted architectural correction solely to keep an obsolete plan intact. Conversely, do not reopen unrelated settled boundaries.

Published requirement IDs must not be repurposed. Add a new requirement and explicit supersession when core meaning changes. Applicability extensions should state precisely which consumer they affect and preserve older behavior where required.

## 10. Normative publication phase

Until a branch is settled, record accepted design and update its actual high-level owners; do not publish unresolved examples as requirements. Once the consumed frontier is empty, tell the user what is settled and request the explicit transition to normative publication. The user may authorize it earlier; do not ask again if already authorized.

After that authorization, complete publication autonomously:

1. Extend the actual `applications/materials.md`; create a substantive `foundation/derived-work.md` if required and absent. Extend only genuinely consumed Common/Storage/Candidate Save/Resume/Workspace interfaces.
2. Read the latest requirement ranges before allocating stable owner-prefixed IDs. MAT already has MAT-001–003 at this snapshot. Do not preallocate future IDs or assume no other conversation has published since then.
3. Write complete English normative content: exact fields/types/nullability/enums/relationships, authority, canonical equality, operations/results, persistence, errors/precedence, concurrency/recovery and client obligations. Use MUST/MUST NOT/SHOULD/SHOULD NOT/MAY consistently and map requirements back to accepted decisions.
4. Keep naming and shared error representation in Common. Keep product meaning, technical work state, command orchestration and physical storage in their own owners; reference rather than duplicate ownership.
5. Reconcile both sides of every necessary interface. In particular, actual material intent versus Save commit, work completion versus artifact publication, exact source versus current-output eligibility, and byte availability versus readiness must have no ownership gap.
6. Update Contract README/index/Structure and actual Slice-to-Contract paths; keep existing grouped directory organization. Do not require finishing all future sections of a partially published body.
7. Reconcile Product, Architecture, Acceptance and implementation plans only where publication reveals or implements approved changes. Preserve unrelated work and historical handoff snapshots.
8. Update the maintained Contract-ID checker when new actual prefixes/counts require it; do not weaken checks to obtain a pass. Run relevant checks on the changed checker as appropriate.
9. Complete the reviews and status recording below before marking any consumed scope Ready.
10. Create or update one real milestone development handoff at `docs/development/handoff/sl-02-m2-handoff.md`, covering consumed IDs, verified upstream state, backend/frontend division, implementation order, proof and remaining dependencies. This Grill-session prompt is not a substitute for that future reviewed development baseline.

No automatic Git commit/push follows publication. If the user asks to commit, inspect/stage only the authorized changes, exclude `.DS_Store` and unrelated work, run staged whitespace/ID checks, follow the repository commit format, and report the resulting hash. Do not claim a clean tree if unrelated files remain.

## 11. Verification and readiness evidence

Apply both mandatory seams from Development §9.2:

- **Decision-to-Document Traceability:** Every accepted effective decision has a normative/current-owner destination, or an explicit future-consumer/out-of-scope reason. Every added normative rule has accepted provenance. Historical rejected/superseded proposals cannot reappear as current requirements.
- **Cross-Document Semantic Consistency:** Product, Architecture, actual Contract bodies, milestone dependency/consumption plan, Acceptance, Progress and handoff agree on sources, authority, exact versions, demand, state, transactions, recovery, readiness and success meaning.

Use independent read-only factual/semantic review where the skill authorizes it. Findings must be fixed or explicitly remain open; an ID count or passing link checker cannot replace semantic review.

Check as appropriate:

- Requirement-ID uniqueness, valid references/ranges and protected published meanings.
- Markdown file/anchor links, new versus planned body navigation and consumer mappings.
- Preserved original history and published migration definitions.
- Scoped old-consumer compatibility and genuine supersession impacts.
- `git diff --check`; after staging, `git diff --cached --check` to include new files.
- The repository's maintained Contract checker and relevant checks for any changed checking script.
- Readiness/table counts derived from actual rows, not copied historical totals.

Record actual commands/results and limitations in existing Progress/traceability owners, not a new generic completion report. Do not run runtime tests merely to make documentary evidence look stronger. If research uses a bounded prototype, record its exact limits; it does not become production implementation or certify all rendering/platform behavior.

Mark Ready only for the actual consumed normative portion after definitions and necessary interfaces are reviewed. Keep future family portions separate. If M1 code is still unavailable, M2 Contract scope may be Ready while development remains blocked on actual upstream implementation. Frontend/UI approval and whole-milestone/parent acceptance remain distinct. Never claim schema migration or renderer output was executed unless it actually was.

## 12. Interaction and continuation rules

Use concise Chinese progress updates during work. Lead with what changed or what remains uncertain, not a running log of commands. Explain recommended decisions clearly enough that the user can understand the eventual implementation without reading code.

Honor steering such as “do not ask the next round,” “give a writeback plan first,” “only persist decisions here,” “pause Grill,” or “commit this round.” A status question does not cancel the ongoing objective. Do not create a new task/conversation or send messages to others without explicit authorization.

After context compaction or a resumed session, reread the single decision record's session state/frontier and current owners. Continue numbering and unresolved branches; do not repeat accepted questions or restore stale recommendations.

When final consumed decisions are closed and publication is authorized, finish the reviewable normative work rather than only describing a plan. Report the actual scope, paths, new IDs, checks, readiness and remaining implementation/consumer limits. Do not ask for repeated permission for routine authorized documentation edits.

## 13. Execute now

Start the required focused reads, inspect actual M1 availability and the current M2 record if one exists, then present the owner/scope map, Grill outline and the first five dependency-safe questions. Do not jump directly to schema/worker design or implement the renderer. Continue the agreed read → five questions → user answers → single-record decisions → scoped writeback/review → next frontier workflow until the consumed scope is fully resolved and its authorized publication is completed.
