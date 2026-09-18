# SL-04 Resume import into reviewed Draft and shared Save

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 1 milestone remains in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Bring existing resumes into the workspace without turning a parser's interpretation into unreviewed formal facts.

**Scope:** Upload and structural import, preserving sections/whole experiences; proposed Profile/Evidence changes; human reconciliation, conflict resolution and completeness of factual support; use SL-02.M1's atomic Save, eligibility and necessary durable intent/currentness interface. Rendering is an optional integration only if the selected Import Review actually consumes it.

**Out of Scope:** Immediate formalization on upload, automatic conflict merges, omission-as-deletion, permanent bullet/Assertion graphs, a second fact-confirmation object, or a new mandatory semantic-enhancement Skill.

**Already-decided capabilities and provenance:** Q15, Q63–Q64, Q70–Q75, Q98, Q108, Q113–Q114, Q118–Q119, Q146, Q163, Q166. Actual behavior/mechanism owners: [P3.2](../../spec.md#32-import-review-and-save); [A5.1](../../architecture.md#51-preparation-before-authority); [A5.2](../../architecture.md#52-one-atomic-authority-change). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F03, F04, F10; F07 only for actually consumed material currentness or conditional rendered Import Review. F08, F09 and F11 apply additionally to a later explicitly selected model path.

**Test / Eval categories:** Structure preservation, conflicting matches, absent experiences, user-authorized facts, unresolved-support Save refusal, atomic rollback, navigation/crash distinction and no source-document leakage; semantic checks only for model behavior actually introduced. Required proof destinations: [V4.1](../../acceptance.md#41-authority-import-and-atomic-save); [V4.3](../../acceptance.md#43-demand-and-safe-derivative-recovery); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 3.1](../../acceptance/evaluation.md#31-capability-specific-review). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-04.M1](#sl-04m1-reviewed-structural-import). Dependencies are implemented components, not completion of upstream parents.

## SL-04.M1 Reviewed structural import

**Goal/value:** Reuse an existing resume while keeping human review and shared fact authority.

**Scope:** Source upload/structural parse, whole-experience proposals, Profile/Evidence reconciliation, support resolution and explicit reviewed Save, including applicable durable intent/currentness. Imported source display and factual reconciliation do not inherently consume the formal Resume rendering pipeline.

**Out of scope:** Automatic formalization/merge, omission-as-deletion, a mandatory model enhancement, persistent Assertions and private Resume facts.

**Required upstream capability:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — reviewable Draft, fact reconciliation, grounding and complete atomic Save

**Reused component/infrastructure:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — Save/idempotency and necessary durable intent/currentness interfaces

**Conditional integration, not a baseline prerequisite:** [SL-02.M2](sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) only if Import Review demonstrably needs that rendered preview capability; freeze the exact consumed rendering scope and test that integration before enabling it. Otherwise import acceptance ends at reviewed atomic Save. General preview/export/Preparation output remains owned and verified in its consuming milestone. Optional model assistance separately adds [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) only if explicitly selected; neither integration is an unconditional dependency.

**Required Contract portions before development:** `resume-import.md` — source ingestion, temporary proposals, reconciliation/provenance; `profile.md`, `evidence.md`, `resumes-grounding.md` — imported-input preparation; `storage.md` — source retention/disposal; reuse `candidate-save.md` and the necessary `derived-work.md` intent/currentness interface. Consume `materials.md` only where currentness crosses the actual Save interface; complete rendering scope only for a selected rendered Import Review integration. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Imported content is not saved authority. Reconciliation must close all facts/support before using the same full Save; retain source privacy independently of rendered outputs.

**Research / unresolved Grill detail:** Research selected source formats/parsers and retention. If optional model enhancement is later explicitly selected, add SL-03.M2 and the complete applicable Context/Budget/Tools/Eval scopes before use; do not wait for all SL-03 or silently enable it.

**Tests / Eval:** V4.1–4.2, V10 and V4.3's necessary intent/currentness boundary: contradictory/partial import, whole experiences, omission, rejected proposal, factual support, rollback and exact saved provenance. Actual rendering/material-output checks apply only to a selected rendered Import Review integration; semantic Eval only to a selected model path. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real imported document reaches reviewed Draft and the existing atomic Save with correct grounding and necessary intent/currentness, without extra fact authority. Rendering success is not required for this baseline. Verify rendered Import Review separately only if that integration is selected. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Import produces reviewable temporary proposals, and only the shared valid Save path creates formal versions. Skipping an old experience does not delete it. Evidence describes the selected parsing path honestly, without claiming optional model work ran. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 1 listed milestone must be accepted. Integrated proof must cover source import → human reconciliation → full Save/grounding and necessary durable intent; rendered Import Review additionally only when selected. Parent completion is separate from rollout/production enablement.
