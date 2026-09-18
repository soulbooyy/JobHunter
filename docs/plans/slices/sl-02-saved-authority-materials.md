# SL-02 Saved Knowledge, formal Resumes and safe materials

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Establish trustworthy reusable career facts and formal Resumes before analyses, import automation or Advisor writes consume them.

**Scope:** Profile and manual Knowledge/Resume maintenance; page-local Draft/Save; whole current experiences; exact grounding; atomic all-affected propagation and logical deletion; default/last-Resume rules and permitted empty content. Deliver the demanded preview/export path with durable intent, exact source eligibility, safe derivative recovery and honest material readiness, without eagerly rendering all formats.

**Out of Scope:** File ingestion/reconciliation UI (SL-04), Advisor-generated Proposals (SL-07), Preparation/material approval (SL-10), private Resume career facts, KnowledgeConfirmation, persistent Assertions and draft crash recovery.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q66, Q70–Q77, Q79, Q86–Q89, Q93, Q96–Q98, Q100, Q108, Q113–Q114, Q118–Q119, Q146–Q147, Q151–Q154, Q163, Q165–Q166. Actual behavior/mechanism owners: [P3](../../spec.md#3-candidate-knowledge-and-resumes); [A3](../../architecture.md#3-authority-identity-and-evolution); [A5](../../architecture.md#5-fact-maintenance-formal-resumes-and-derived-work). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F07, F10.

**Test / Eval categories:** All-affected rollback and races, direct-membership deletion, current versus historical grounding, contact versus career/presentation changes, empty states/default selection, navigation Save/Discard/Cancel, committed Save versus render failure, crash recovery and obsolete derivative publication. Required proof destinations: [V4](../../acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts); [V9.3](../../acceptance.md#93-streams-presentation-and-safe-work); [V10](../../acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save), [SL-02.M2](#sl-02m2-demanded-preview-and-export). Dependencies are implemented components, not completion of upstream parents.

## SL-02.M1 Complete saved authority and atomic Save

**Goal/value:** Give all later consumers consistent career facts and formal Resume content.

**Scope:** Profile, saved whole experiences and baseline, formal Resume/grounding, page Draft and explicit Save, default/last-Resume and empty-state rules, direct membership and logical deletion; all affected authority and necessary demanded-work intent commit together.

**Out of scope:** Actual rendered preview/export delivery is M2; import and Advisor-generated changes are later entry points.

**Required upstream capability:** [SL-01.M1](sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-job-authority) — local Workspace configuration

**Reused component/infrastructure:** [SL-01.M1](sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-job-authority) — local persistence/reference/privacy primitives

**Required Contract portions before development:** `workspace.md` — default Resume; `profile.md` — identity/contact/privacy; `evidence.md` — current/history, baseline and eligibility; `resumes-grounding.md` — Draft, whole experiences, exact support/Ensure and removal; `candidate-save.md` — complete prepare/commit, conflict/idempotency and all affected participants; `derived-work.md` — demanded intent included atomically; `materials.md` — source binding, currentness and unavailable-output meaning needed by Save. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Architecture 16.3 Save agreement must be complete on both sides before any successful Save. No asynchronous authority repair. Define necessary intent and output invalidation now even though the rendering worker comes in M2.

**Research / unresolved Grill detail:** Resolve actual grounding/support validation and local transaction feasibility; do not select model assistance by implication.

**Tests / Eval:** V4.1–4.2, V4.3 intent boundary, V10: rollback/races, Profile versus career changes, deletion/membership, exact old readers, unsupported current use, Save/Discard/Cancel and empty/default cases. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Every actual manual authority change preserves the full invariant and durable demand; pending material work is reported honestly. Evidence consumers need no user-owned Resume or rendered artifact. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-02.M2 Demanded preview and export

**Goal/value:** Turn valid formal Resumes into usable material without coupling Save success to rendering.

**Scope:** Selected required preview/export formats, actual demand, MaterialBundle/Artifact/RenderManifest source binding, safe local work claim/reuse/recovery, obsolete skipping and fenced current publication.

**Out of scope:** Preparation approval, Greeting and authorization to send; remote/model replay.

**Required upstream capability:** [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save) — eligible saved Resume/grounding and currentness

**Reused component/infrastructure:** [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save) — durable demanded intent and source/currentness checks

**Required Contract portions before development:** `materials.md` — required rendered output/readiness/history; `derived-work.md` — demand, local execution/recovery and publication; `resumes-grounding.md` — current versus historical source eligibility. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Reuse candidate-save intent; material meaning stays in materials, technical work in derived-work. A stale result cannot become current or resurrect removed source.

**Research / unresolved Grill detail:** Research formats/rendering and retained historical reader requirements before specifying the chosen consumer path.

**Tests / Eval:** V4.3, V9.3, V10: post-commit rendering failure, restart, obsolete job, concurrent newer Save, exact output provenance and no false readiness. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real demand produces correctly bound usable artifacts; crashes and stale work preserve committed authority and currentness. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** The actual manual maintenance and demanded material paths preserve all shared authority together; no affected current Resume waits for asynchronous fact synchronization. Unavailable derivatives block only the operations that require them. Required positive, failure, concurrency and recovery evidence exists. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover authority Save → durable demanded intent → actual output/currentness, including edits/deletion during work. Parent completion is separate from rollout/production enablement.
