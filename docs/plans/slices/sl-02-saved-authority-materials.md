# SL-02 Saved Knowledge, formal Resumes and safe materials

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Establish trustworthy reusable career facts and formal Resumes before analyses, import automation or Advisor writes consume them.

**Scope:** Separate Profile/Knowledge and Resume maintenance; exact historical source snapshots, local expression/presentation, page Draft and per-command atomic Save under [CG03-BC3/A1–A5](../../design/contract/sl-02-m1-grill.md#cg03-bc3). Retirement retains referenced history without Resume propagation. Default/last/empty rules survive. Deliver demanded source-bound materials without eager all-format rendering.

**Out of Scope:** File ingestion/reconciliation UI (SL-04), Advisor-generated Proposals (SL-07), Preparation/material approval (SL-10), competing private Knowledge authority (local Resume expression is allowed), KnowledgeConfirmation, persistent Assertions and draft crash recovery.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q66, Q70–Q77, Q79, Q86–Q89, Q93, Q96–Q98, Q100, Q108, Q113–Q114, Q118–Q119, Q146–Q147, Q151–Q154, Q163, Q165–Q166. Actual behavior/mechanism owners: [P3](../../spec.md#3-candidate-knowledge-and-resumes); [A3](../../architecture.md#3-authority-identity-and-evolution); [A5](../../architecture.md#5-fact-maintenance-formal-resumes-and-derived-work). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F07, F10.

**Test / Eval categories:** Independent command rollback/races, two-stage creation, immutable historical/retired refs, no cross-Resume propagation, manual lineage versus AI support, empty/default states and material recovery. Required proof: [Acceptance 4](../../acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts), [Acceptance 10](../../acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save), [SL-02.M2](#sl-02m2-demanded-preview-and-export). Dependencies are implemented components, not completion of upstream parents.

## SL-02.M1 Complete saved authority and atomic Save

**Goal/value:** Give all later consumers consistent career facts and formal Resume content.

**Scope:** Three-field versioned Profile; six-kind Evidence and current baseline; exact-version Resume membership with independently versioned local wording/blocks/inline presentation; local A4 Draft preview; explicit contact/source adoption; separate owned Knowledge/Profile/Resume Saves; default/last/empty rules and exact-source/currentness boundaries. [CG03-BC3/A1–A5](../../design/contract/sl-02-m1-grill.md#cg03-bc3) replaces current-only sources and all-affected propagation. Q32 Evidence semantic AST and Q34 editing capabilities survive; field validation through Q30 remains applicable. Q36–Q40 adds one-time local-body initialization, new-member current-at-Save checks, explicit source adoption with separately confirmed body reset, legal empty member content and ordered runs/marks. Q41–Q45 adds canonical marks/merge, distinct source/local whitespace, per-body capacities and current-at-commit checks for replacement Evidence bindings. Q46–Q50 fixes allowed-whitespace-only runs, raw validation before merge, Item-owned permanent kind, typed version fields/content and initial empty Profile publication. Q51–Q55 fixes saved Profile/Evidence/root/member/Snapshot fields, initial empty Baseline and Evidence/Baseline-owned current pointer with optional physical config-row placement. Q56–Q60 fixes UUIDv4 identity, revision-first no-op/publication, scoped shared times, ResumeVersion envelope and Profile-reference freshness. Q61–Q65 adds concrete four-setting document presentation, whole-Resume capacities, single-Item Knowledge commands, one-way lifecycle with historical reads/repeated no-op, and full business-content replacement. Q66–Q70 adds exact scalar admission/Color Picker, nine POST mutation routes, success receipts for all user writes, per-Item concurrency without a global Baseline precondition and confirmed adjacent default replacement. Q71–Q75 adds stable ACTIVE Resume order, small independently revisioned Workspace default selection, SL-02-scoped lifetime receipts, replay-before-state admission and consistent current root/version reads. Q76–Q80 adds exact remove/default preconditions with lifecycle no-op precedence, consistent full ACTIVE Resume list/selection, exact Version/Baseline readers and strict transport/raw budgets. Q81–Q85 adds the 100-ACTIVE-Resume cap, complexity/path errors, complete write bodies, first-create concurrency without a caller default token and frozen success results including no-op Baseline/default snapshots. Q86–Q90 adds receipt snapshots/exact refs, typed tuple fingerprint with booleans/negative zero, Evidence admission subsequently superseded by Q98, lifecycle/reference error classes and unknown-write recovery. Q91–Q95 adds explicit-ID Evidence list/1,000-ACTIVE cap, planned schema 3 and relational lineage/JSON content, and moves actual material demand/durable intent to M2. Q96–Q100 adds local HTTP admission, Common-owned field-error vocabulary, authoritative immutable Item.kind lookup before Update field validation/receipt, receipt-race arbitration and stored-lineage integrity. The consumed 2026-09-21.S2M1-r1 normative scope and reviewed interfaces are linked below; no generic configuration/idempotency framework is required.

**Out of scope:** Durable saved-source rendered preview/PDF/export delivery is M2; editor-local non-authoritative Draft preview is in the M1 frontend scope under CG03-UI1. Import and Advisor-generated changes are later entry points; no Resume DSL/source mode is introduced. Frontend implementation still waits for UI design.

**Required upstream capability:** [SL-01.M1](sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-application-entries) — local Workspace configuration

**Reused component/infrastructure:** [SL-01.M1](sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-application-entries) — local persistence/reference/privacy primitives

**Required Contract portions before development:** `foundation/workspace.md` — default Resume; `candidate/profile.md` — exact contact snapshots/privacy; `candidate/evidence.md` — current baseline, historical lineage and retirement; `candidate/resumes-grounding.md` — local expression/presentation, manual lineage validation, the ownership boundary to later AI support, and removal; `candidate/candidate-save.md` — separate commands, revisions/idempotency and two-stage outcomes; `applications/materials.md` — exact-source/currentness and Save-not-output-ready boundary only. Under CG03-Q95, `foundation/derived-work.md` is not an M1 required portion; actual material demand/intent is M2. Applicable Common/Storage is required only as consumed; no whole-family gate.

**Joint agreement:** Architecture §16.3 must agree on each command's owned atomic participants. Knowledge/Profile Save cannot fan out into Resumes; Resume Save cannot silently write facts. New fact creation commits before Draft inclusion, and later Resume cancellation cannot undo it. Lineage must not masquerade as manual semantic verification. No model/network/render inside transactions.

**Research / unresolved Grill detail:** Effective decisions through CG03-Q100 and Q98's missing-target precedence are published as [2026-09-21.S2M1-r1](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence). No known consumed M1 semantic decision remains open. Concrete SQL, component placement and backend engineering checks remain implementation work against existing infrastructure. Actual Renderer assets/configuration/demand/work is M2; AI support is SL-07; Import multi-fact confirmation needs its later batch extension. Frontend implementation awaits UI design. Do not reopen automatic source/format propagation.

**Development entry:** [SL-02.M1 handoff](../../development/handoff/sl-02-m1-handoff.md). Required IDs are COM-038–042, WSP-008–011, PRO-001–008, EVD-001–014, RES-001–015, SAV-001–016, MAT-001–003 and STO-021–028 plus their explicit shared references. Readiness is documentary; actual schema remains 2 until implementation.

**Tests / Eval:** V4.1–4.3/V10: independent rollback, retained old/retired refs, Profile snapshots, untouched Resumes/materials after Knowledge updates, no Knowledge write-back from local wording, two-stage failure/cancel, source/permission checks and exact old readers. Manual Save requires no semantic model Eval; AI support has its own consumer proof.

**Milestone completion:** The real Knowledge/Profile/Resume command paths preserve separate authorities and durable command results; exact history remains usable and no automatic synchronization occurs. Record actual backend/frontend evidence separately; no readiness or completion is claimed by BC3 writeback.

## SL-02.M2 Demanded preview and export

**Goal/value:** Turn valid formal Resumes into usable material without coupling Save success to rendering.

**Scope:** Under CG03-Q95, first delivery of actual material demand/configuration/durable intent, necessary atomic candidate-save/Storage extensions, and durable saved-source preview/export formats; MaterialBundle/Artifact/RenderManifest source binding, safe local work claim/reuse/recovery, obsolete skipping and fenced current publication.

**Out of scope:** Preparation approval, Greeting and authorization to send; remote/model replay.

**Required upstream capability:** [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save) — eligible exact saved Resume/lineage and currentness

**Reused component/infrastructure:** [SL-02.M1](#sl-02m1-complete-saved-authority-and-atomic-save) — owned Save, retained exact sources and source/currentness checks; demanded intent is delivered in M2 under CG03-Q95

**Required Contract portions before development:** `applications/materials.md` — required rendered output/readiness/history; `foundation/derived-work.md` — demand, local execution/recovery and publication; `candidate/candidate-save.md` / `foundation/storage.md` — atomic intent extension for actual Save-coupled material demand; `candidate/resumes-grounding.md` — exact historical lineage and task-specific permissions/availability. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Extend the M1 Resume Save transaction with necessary durable intent only for actual M2 demand; this capability is not pre-delivered by M1 and cannot be replaced with a lossy post-commit notification; materials owns output and derived-work owns safe work. Evidence/Profile current-pointer changes or ordinary retirement alone do not obsolete an unchanged Resume or its output. Only actual document/configuration/demand/permission changes affect that consumer's readiness/publication.

**Research / unresolved Grill detail:** Research formats/rendering and retained historical reader requirements before specifying the chosen consumer path.

**Tests / Eval:** V4.3, V9.3, V10: post-commit rendering failure, restart, obsolete job, concurrent newer Save, exact output provenance and no false readiness. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real demand produces correctly bound usable artifacts; crashes and stale work preserve committed authority and currentness. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Manual Knowledge and independent Resume editing plus demanded materials satisfy BC3. Integrated proof covers Knowledge Save surviving Resume cancellation; existing Resumes retaining exact sources; local expression affecting only its document; and actual demand/output recovery. Both milestones require their own consumed ready scope and accepted runtime evidence; this document claims no implementation or completion.
