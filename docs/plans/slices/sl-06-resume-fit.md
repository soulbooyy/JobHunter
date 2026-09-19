# SL-06 Independent Resume Fit

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Assess what an exact formal Resume actually expresses, without silently supplementing it from all Candidate Knowledge.

**Scope:** Independent ResumeJobFit selection/Run/result/history; exact eligible Resume/Requirement inputs; permitted grounding validation, scoped assessments, independent score/rescore/unscored behavior; compatible target serialization and per-Job selection/orchestration.

**Out of Scope:** Candidate Fit as a prerequisite or authority, unseen Knowledge added through grounding or judges, ResumeCoverage/score-gap models and mandatory ordering between the two scores.

**Already-decided capabilities and provenance:** Q19, Q35, Q46, Q51, Q75, Q77, Q82–Q83, Q87, Q110–Q117, Q123, Q142, Q168, Q171–Q172, Q184, Q186, S5.3, S22.1. Actual behavior/mechanism owners: [P5](../../spec.md#5-requirements-and-independent-fit-analyses); [A5.4](../../architecture.md#54-grounding-and-demand-driven-artifacts); [A6](../../architecture.md#6-requirements-fit-and-analysis-orchestration); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F03, F04, F05, F06, F08, F09, F10, F11.

**Test / Eval categories:** Candidate/other-Resume leakage, incomplete inspection versus MISSING, original/current version compatibility, unscored assessments, two freeze points, fail-closed capacity/revocation and independent success/failure/batch history. Required proof destinations: [V5](../../acceptance.md#5-requirements-and-independent-fits); [V8.2](../../acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9.1](../../acceptance.md#91-owners-reservations-and-limits); [Eval acceptance 2](../../acceptance/evaluation.md#2-eval-execution-and-evidence-integrity); [Eval acceptance 3](../../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-06.M1](#sl-06m1-single-target-resume-fit), [SL-06.M2](#sl-06m2-resume-selection-batches-and-rescoring). Dependencies are implemented components, not completion of upstream parents.

## SL-06.M1 Single-target Resume Fit

**Goal/value:** Assess only the content actually expressed in an exact formal Resume.

**Scope:** Independent Resume task/result with exact grounding eligibility; shared assessment/scoring meanings, two freezes, target serialization/publication, valid unscored output and revocation safeguards.

**Out of scope:** Candidate Fit as prerequisite, unexpressed Knowledge supplementation, rendering as analysis prerequisite, Coverage comparison and Memory.

**Required upstream capability:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — formal Resume with exact expressed-content grounding; [SL-03.M3](sl-03-invocation-requirements.md#sl-03m3-requirementparse-and-shared-ensure) — compatible usable Requirements/Ensure

**Reused component/infrastructure:** [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) — protected invocation, Context, budget and evidence

**Required Contract portions before development:** `jobs/fit-analysis.md` — Resume and necessary shared assessment/scoring/single-target sections; `candidate/resumes-grounding.md` — exact expressed source/support eligibility; `jobs/requirements.md` — usable target; `agent/context.md`, `agent/execution-runtime.md`, `foundation/budget.md` — admitted task scope; `evaluation/evaluation-observability.md` — Resume-only evaluators. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Grounding validates expressed support without importing additional career content. Introduce shared Fit sections here if SL-05 has not done so; one document never joins task identity or readiness.

**Research / unresolved Grill detail:** Resolve Resume-specific assessment/support cases and score expression in Grill; do not inherit a Candidate evaluator's broader evidence.

**Tests / Eval:** V4.2, V5, V8–9, V12–13: no supplemental Knowledge, exact history/eligibility, incomplete or unscored output, revocation and scope-correct semantic judgments. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real Resume result is independently valid, scoped and evidenced without Candidate Fit. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-06.M2 Resume selection, batches and rescoring

**Goal/value:** Run independent Resume comparisons and retain assessments across explicit scoring changes.

**Scope:** Job-side/Resume-side selection, independent per-target batch tasks and outcomes, retained assessment rescoring and scope-correct workflow evidence.

**Out of scope:** Candidate batch prerequisite, combined Fit task, shared batch transaction and automatic pursuit.

**Required upstream capability:** [SL-06.M1](#sl-06m1-single-target-resume-fit) — independent Resume assessment/current-result capability

**Reused component/infrastructure:** [SL-06.M1](#sl-06m1-single-target-resume-fit) — single-target task controls and compatible shared Ensure/runtime paths

**Required Contract portions before development:** `jobs/fit-analysis.md` — Resume selection/batch and rescore with shared definitions reused or first completed here; `foundation/budget.md` — operation limits; `evaluation/evaluation-observability.md` — Resume workflow scope. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Resume eligibility and target serialization survive batch orchestration. Shared definitions may be reused from SL-05.M2 only if actually complete; that milestone is not a dependency.

**Research / unresolved Grill detail:** Resolve selection and multi-target admission under the same independent task meanings.

**Tests / Eval:** V5, V9.1, V12–13: differing target outcomes, shared parse reuse, rescore/no hidden inference and independent evidence. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Actual Resume batches and rescoring work without Candidate task results or broader factual scope. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Resume Fit runs and remains understandable on its own, with evidence limited to what that Resume expresses. Candidate Fit can be absent, fail or have a different score without invalidating a valid Resume Fit. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover single Resume assessment, independent batch outcomes and retained assessment rescoring. Parent completion is separate from rollout/production enablement.
