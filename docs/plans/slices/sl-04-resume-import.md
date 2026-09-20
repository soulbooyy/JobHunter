# SL-04 Two-stage reviewed Resume import

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 1 milestone remains in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Bring existing resumes into the workspace without turning a parser's interpretation into unreviewed formal facts.

**Scope:** Upload and structural import, preserving sections/whole experiences; proposed Profile/Evidence changes; human reconciliation, conflict resolution and explicit Knowledge Save followed by independent Resume-local Draft/Save under BC3/A5; use SL-02.M1's per-command lineage/results/currentness. Under CG03-Q95, material intent is an M2 extension consumed only for actual demand. Rendering is an optional integration only if the selected Import Review actually consumes it.

**Out of Scope:** Immediate formalization on upload, automatic conflict merges, omission-as-deletion, permanent bullet/Assertion graphs, a second fact-confirmation object, or a new mandatory semantic-enhancement Skill.

**Controlling supersession:** [CG03-BC3/A1–A5](../../design/contract/sl-02-m1-grill.md#cg03-bc3) replaces the old combined Save workflow while retaining structural parsing and explicit human fact confirmation.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q70–Q75, Q98, Q108, Q113–Q114, Q118–Q119, Q146, Q163, Q166. Actual behavior/mechanism owners: [P3.2](../../spec.md#32-import-review-and-save); [A5.1](../../architecture.md#51-preparation-before-authority); [A5.2](../../architecture.md#52-one-atomic-authority-change). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F10; F07 only for actually consumed material currentness or conditional rendered Import Review. F08, F09 and F11 apply additionally to a later explicitly selected model path.

**Test / Eval categories:** Structure preservation, conflicting matches, absent experiences, user-authorized facts, fact reconciliation, per-stage atomic rollback and stage-one durability after stage-two failure, navigation/crash distinction and no source-document leakage; semantic checks only for model behavior actually introduced. Required proof destinations: [V4.1](../../acceptance.md#41-authority-import-and-atomic-save); [V4.3](../../acceptance.md#43-demand-and-safe-derivative-recovery); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 3.1](../../acceptance/evaluation.md#31-capability-specific-review). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-04.M1](#sl-04m1-reviewed-structural-import). Dependencies are implemented components, not completion of upstream parents.

## SL-04.M1 Reviewed structural import

**Goal/value:** Reuse an existing resume while keeping human review and shared fact authority.

**Scope:** Source upload/structural parse, whole-experience proposals, Profile/Evidence reconciliation, explicit fact confirmation/Knowledge Save, then independent Resume expression/Save, including each command's durable result and, only when actual M2 material demand requires it, the atomic intent extension. Imported source display and factual reconciliation do not inherently consume the formal Resume rendering pipeline.

**Out of scope:** Automatic formalization/merge, omission-as-deletion, a mandatory model enhancement, persistent Assertions and Resume-private confirmed Knowledge facts.

**Required upstream capability:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — reviewable fact proposals, independent Knowledge Save and Resume Draft/Save with exact lineage

**Reused component/infrastructure:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — Save/idempotency and exact-source/currentness interfaces; actual material demand/intent comes from SL-02.M2 when consumed

**Conditional integration, not a baseline prerequisite:** [SL-02.M2](sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) only if Import Review demonstrably needs that rendered preview capability; freeze the exact consumed rendering scope and test that integration before enabling it. Otherwise import acceptance covers both explicit saves and independent first-stage durability. General preview/export/Preparation output remains owned and verified in its consuming milestone. Optional model assistance separately adds [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) only if explicitly selected; neither integration is an unconditional dependency.

**Required Contract portions before development:** `candidate/resume-import.md` — source ingestion, temporary proposals, reconciliation/provenance; `candidate/profile.md`, `candidate/evidence.md`, `candidate/resumes-grounding.md` — imported-input preparation; `foundation/storage.md` — source retention/disposal; reuse `candidate/candidate-save.md` for authority/results/currentness. Consume `foundation/derived-work.md` and the M2 atomic Save extension only when actual material demand/integration requires intent; no unconditional M1 intent prerequisite. Consume `applications/materials.md` only where currentness crosses the actual Save interface; complete rendering scope only for a selected rendered Import Review integration. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Under [CG03-BC3/A1–A5](../../design/contract/sl-02-m1-grill.md#cg03-bc3), two-stage Import is a product choice consistent with manual editing, not a technical prohibition on jointly creating valid refs in one transaction. Stage-one confirmed facts survive stage-two cancel, browser closure or failed Resume Save. CG03-Q63 limits the upstream M1 interface to single-Item Knowledge commands: Import requiring an atomic multi-fact confirmation stage must define and review a batch extension here. Several independently committed item commands cannot satisfy per-stage atomic rollback. Resolve each command's outcome without compensating away committed facts; manual local wording is not an automatic fact-support gate.

**Research / unresolved Grill detail:** Research selected source formats/parsers and retention. If optional model enhancement is later explicitly selected, add SL-03.M2 and the complete applicable Context/Budget/Tools/Eval scopes before use; do not wait for all SL-03 or silently enable it.

**Tests / Eval:** V4.1–4.2, V10 and V4.3's Save-not-output-ready/currentness boundary under CG03-Q95: contradictory/partial import, whole experiences, omission, rejected proposal, confirmed fact provenance, local document lineage and independent stage rollback/outcomes. Actual material-intent/output checks apply when actual M2 demand or a selected rendered Import Review integration is consumed; semantic Eval only to a selected model path. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real imported document reaches explicit reviewed Knowledge publication, then independent Resume-local editing/publication. Verify stage-one facts survive stage-two cancel/close/failure, no private-fact fallback or automatic merge, and exact source lineage. Rendering is required only for an explicitly selected rendered-review integration. No completion is claimed.

**Parent completion and remaining work:** The two-stage product flow replaces the former Evidence+Resume+Grounding transaction. Import remains provisional until fact confirmation; omission is not deletion; manual document expression does not become Knowledge. Full proof covers both saves and failure between them, with optional rendering/model checks only for real consumers. One milestone remains; no readiness or runtime acceptance is inferred.
