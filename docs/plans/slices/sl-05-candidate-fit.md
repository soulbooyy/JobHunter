# SL-05 DeepFit

> Revised by accepted CG03S1-Q26 at **2026-09-24.S2M1S1-r1**. Planning is not implemented capability or whole-file Contract readiness. Earlier source-model/allocation descriptions are superseded.

[Global rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) · [Decisions](../../design/contract/sl-02-m1-supplement-grill.md) · [Progress](../../progress.md)

DeepFit produces one CandidateJobFitAnalysis with separate preference/capability meanings. No parallel ResumeFit or mandatory full-Evidence initial Frame remains.

<a id="sl-05m1-single-target-candidate-fit"></a>
## SL-05.M1 Single-target DeepFit

**Scope:** Exact Job/Requirements, READY default-derived pair and optional exact Preferences; Profile-first progressive block→entry→broader Evidence; supported findings, honest UNKNOWN/source-bounded negatives and historical frozen lineage.

**Upstream:** Actual SL-02.M1 portrait; SL-03.M2 protected invocation; SL-03.M3 RequirementParse/Ensure and its formal Job producer SL-08.M2. Reuse scoped Runtime/Context/Tools/Budget/Eval, not test-only substitute calls. SL-01.M2 intent is optional at manual run admission; missing is unassessed.

**Required interfaces:** PRO-010–016/EVD-016–023, PRF-024, CTX-016/TOL-015/EVO-027. Future fit-analysis and Job/Requirement consumer scopes still must define run/admission/result/coverage/scoring/compatibility and typed Evidence Tool payloads before implementation; documentary boundary agreement is not whole Fit readiness.

**Backend/frontend:** First implementation of one analysis orchestration/result; UI single DeepFit action and unavailable prerequisite, separate intent/capability findings, exact source/citations, unknown/historical state. No document selection that silently switches default, no parallel fit results or forced intent mismatch rejection.

**Proof:** Acceptance §5/§8–9 and EVO-027, actual progressive acquisition/coverage, hidden-input privacy, profile omission/source support, preference absence/mismatch, freeze across switch/save, revocation and cost honesty.

**Development entry:** [SL-05.M1 handoff](../../development/handoff/sl-05-m1-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

<a id="sl-05m2-candidate-selection-batches-and-rescoring"></a>
## SL-05.M2 Multi-Job analysis and result management

**Scope:** Multi-Job selection, scheduling, independently truthful outcomes and exact result/history management over M1. Reuse one analysis capability; no paired Candidate/Resume tasks. Result compatibility/rescoring only after its owned policy is reviewed, not a newly invented numeric policy.

**Upstream:** Implemented SL-05.M1 plus formal Job queries and applicable orchestration/runtime. M2-specific fit-analysis result/batch/score-policy Contracts remain pending.

**Backend/frontend:** First implementation of per-target frozen runs and result management; UI selection, per-target pending/unknown/success/failure, actual source/history and unavailable portrait. Undispatched members are not failed or successful.

**Proof/completion:** Mixed target outcomes, concurrency/duplicate commands, old successful result after failed rerun, independent costs, default switch during batch and per-run historical lineage. M1 success alone cannot complete this milestone.

**Development entry:** [SL-05.M2 handoff](../../development/handoff/sl-05-m2-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

**Parent completion:** Single and multi-Job DeepFit plus actual integration/Eval; no dependency on SL-06 optimization or parallel analysis integration.
