# SL-05 Independent Candidate Fit

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Assess the user's admitted saved Knowledge against one Job's reusable Requirements, with bounded conclusions and defensible score availability.

**Scope:** Independent CandidateJobFit selection/Run/result; two-stage freeze and actual complete admitted baseline; task-scoped assessment meanings, deterministic score/rescore policy, valid unscored results; target serialization/latest compatible success, history and multi-Job task orchestration.

**Out of Scope:** Resume Fit as a prerequisite, coupled dual-axis analysis, score ordering/gaps, capability claims beyond inspected saved facts, automatic RAG/model switching or silent trimming.

**Already-decided capabilities and provenance:** Q19, Q35, Q46, Q51, Q72, Q82–Q83, Q110–Q117, Q123, Q135, Q142, Q168, Q171–Q172, Q184, Q186, S22.1. Actual behavior/mechanism owners: [P5](../../spec.md#5-requirements-and-independent-fit-analyses); [A6](../../architecture.md#6-requirements-fit-and-analysis-orchestration); [A10.2](../../architecture.md#102-protected-inputs-and-ordered-reduction); [A11](../../architecture.md#11-budgets-and-resource-admission); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F03, F05, F06, F08, F09, F10, F11.

**Test / Eval categories:** Actual Frame coverage and bounded negatives, UNKNOWN and valid unscored outcomes, unusable dependency fail-fast, no Memory/Resume leakage, capacity/revocation termination, competing targets and failed rerun preservation, partial batch outcomes and separate parse/Fit costs. Required proof destinations: [V5](../../acceptance.md#5-requirements-and-independent-fits); [V8.2](../../acceptance.md#82-exact-acquisition-reduction-and-checkpoints); [V9.1](../../acceptance.md#91-owners-reservations-and-limits); [Eval acceptance 2](../../acceptance/evaluation.md#2-eval-execution-and-evidence-integrity); [Eval acceptance 3](../../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-05.M1](#sl-05m1-single-target-candidate-fit), [SL-05.M2](#sl-05m2-candidate-selection-batches-and-rescoring). Dependencies are implemented components, not completion of upstream parents.

## SL-05.M1 Single-target Candidate Fit

**Goal/value:** Assess the candidate's saved eligible career baseline against one Job.

**Scope:** Independent Candidate task/result, complete baseline, selection then dependency preparation/full freeze, scoped four assessment meanings, valid unscored result, deterministic score when supported, per-target serialization/publication and protected-input revocation.

**Out of scope:** Resume Fit, Coverage/upper-bound comparison, required formal Resume possession/rendering, Advisor and Memory; multi-Job execution/rescore in M2.

**Required upstream capability:** [SL-02.M1](sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) — saved task-eligible Evidence baseline; user possession of a formal Resume is unnecessary; [SL-03.M3](sl-03-invocation-requirements.md#sl-03m3-requirementparse-and-shared-ensure) — compatible usable Requirements/Ensure

**Reused component/infrastructure:** [SL-03.M2](sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) — protected invocation, Context, budget and evidence

**Required Contract portions before development:** `fit-analysis.md` — Candidate, shared assessment/scoring and single-target freeze/publication; `evidence.md` — complete task-eligible baseline; `requirements.md` — usable target; `context.md`, `execution-runtime.md`, `budget.md` — actual Fit inputs/operation admission; `evaluation-observability.md` — Candidate-scoped fixtures/judges and Skill/workflow attribution. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Baseline eligibility is not actual Frame visibility. Agree Requirement producer cost versus Fit allowance; score absence is not task failure or an unusable target. No later success may publish over a serialized incompatible target.

**Research / unresolved Grill detail:** Complete bounded MISSING/UNKNOWN and score policy expressions in Grill; assess representative candidate/job cases without defining a universal completeness Gate.

**Tests / Eval:** V5.2–5.3, V8–9, V12–13: full baseline/exact Frame, two freezes, contention/revocation, honest unscored result, semantic entailment and unsupported claims. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** A real Candidate result has the correct admitted baseline, scope, publication and evidence independently of Resume Fit. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-05.M2 Candidate selection, batches and rescoring

**Goal/value:** Compare selected Jobs and update scoring policy without rerunning semantic judgments unnecessarily.

**Scope:** Candidate-side multi-Job selection/dependency orchestration, independent results/failures, task versus workflow evidence and explicit deterministic rescoring of retained valid assessment.

**Out of scope:** Transactional batch success, new Pursuit state, automatic rerun on scoring change or Resume Fit dependency.

**Required upstream capability:** [SL-05.M1](#sl-05m1-single-target-candidate-fit) — independent Candidate assessment/current-result capability

**Reused component/infrastructure:** [SL-05.M1](#sl-05m1-single-target-candidate-fit) — single-target task controls and compatible shared Ensure/runtime paths

**Required Contract portions before development:** `fit-analysis.md` — Candidate selection/batch orchestration and explicit rescore; `budget.md` — applicable shared operation ceilings; `evaluation-observability.md` — multi-task/workflow scope and retained assessment evidence. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Each target retains M1 freeze/publication and parse ownership. Batch selection is temporary task intent, not durable pursuit or shared result identity.

**Research / unresolved Grill detail:** Resolve actual batch admission/accounting and score-version compatibility; no quota or threshold is selected here.

**Tests / Eval:** V5, V9.1, V12–13: partial failures, shared Ensure cost, concurrent targets, current-result validity, rescore without hidden model calls and honest aggregate evidence. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Actual selected Candidate tasks and rescoring preserve independent outcomes and original assessment authority. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** A user can independently run Candidate Fit and inspect grounded, scope-limited results/history; optional scoring absence is honest. Composed workflow evidence includes actual dependency preparation, and Skill-only trials do not claim parser quality. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover single Candidate assessment, independent batch outcomes and retained assessment rescoring. Parent completion is separate from rollout/production enablement.
