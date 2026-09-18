# Agent Eval Acceptance and Evaluation Evidence

> English is authoritative. This document owns specialized Eval proof and evidence-integrity obligations within the existing Acceptance category. It preserves the former Acceptance 12–13 requirements; it does not define a new product/runtime authority, detailed Contract representation or release policy, and records no executed results.

[Acceptance overview](README.md) · [Unified product/system acceptance](../acceptance.md) · [Global documentation index](../index.md)

## 1. Authority and relationship to other documents

[Product](../spec.md) owns behavior and [Architecture](../architecture.md) owns mechanisms and invariants. The [main Acceptance document](../acceptance.md) remains the unified product/system acceptance authority for business and runtime capabilities. This child owns what Agent Eval and evaluation evidence must prove, including isolation, exact fixtures, Scenario/N+1 scope, judge admission, telemetry, retained evidence and semantic/reliability/efficiency claims. Its criteria supplement the relevant business/runtime scenarios rather than relocating those scenarios by domain.

[Product 11](../spec.md#11-quality-and-evidence-boundaries) and [Architecture 15](../architecture.md#15-eval-and-observability) provide the common behavior/design boundary. RequirementParse/Fits, Advisor, Context/Tools, authority and Memory evidence also consumes their existing main Acceptance scenarios and Product/Architecture owners; source references below preserve those associations. A judge or quality average cannot replace required deterministic product/runtime proof.

The [Development Eval guide](../development/evaluation.md) describes how developers prepare, execute and maintain evaluation using these criteria. It references this document for proof sufficiency, conclusions and limits instead of defining a second oracle. [Progress recording rules](../progress/README.md) owns status/readiness/evidence records; actual values remain in Progress/matrix. Document-authoring verification belongs to [Development 9.2](../development.md#92-two-separate-verification-seams), not to product acceptance.

Sections 2.1–2.4 retain former Acceptance 12.1–12.4; sections 3.1–3.2 retain former Acceptance 13.1–13.2. Old V12/V13 source and planning shorthand remains traceable through the main document's short routing sections; current direct links locate the child criteria. Section and scenario names are locators, not normative Contract IDs or runnable tests. Main Acceptance 2 supplies general evidence interpretation; this child owns the specialized Eval criteria. Fields, interfaces, metrics/denominators, thresholds and rollout details remain pending with their existing owners.

## 2. Eval execution and evidence integrity

**Design owner:** [Architecture 15](../architecture.md#15-eval-and-observability), grounded in Q173–Q187 and [Agent Evaluation](../design/eval/agent-evaluation.md). These scenarios verify that later evaluation measures the intended real path and reports defensible evidence. They do not claim a deployed Langfuse installation, verified SDK behavior, or implemented runner.

### 2.1 Isolation, exact inputs, and declared experiment scope

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Execute an isolated Trial that commits a confirmed change | Use real Application/Domain/Repository/Harness/validators and production prompts/permissions; changes affect test state only. Controlled external adapters prevent real platform effects without bypassing guards | Task entry, actual test-state effects and external isolation; no test-only Agent; Q173 |
| Run independent Trials, including successful mutations, approvals or learned Memory | Each reconstructs its own immutable fixture; no cross-Trial state leakage. A declared multi-step Scenario retains only its intended internal progression | Initial and final fixture/state identities, isolation and guard evidence; Q173, Q177, Q187 |
| Resolve exact Dataset version with missing/mismatched/unrecoverable business input or configuration | Explicit non-reproducibility; never fall back to latest Workspace roots, current permissions or a guessed checkpoint. Freeze fixture, authored events/expectations and exact execution/evaluator configuration | Resolved immutable references, hashes and actual configuration; no claim of identical remote model text; Q177 |
| Measure Fit with a preexisting compatible Set versus a workflow needing parse | Both use real Ensure. Ready-Set experiment measures Fit, not parser quality; workflow records dependency preparation actually executed. Failed dependency does not count unexecuted Fit as success or bad Fit semantics | Declared scope, actual stage lineage/outcomes/cost; partial path is not end-to-end cost/quality; Q186 |
| Run ordinary Advisor comparison versus a Memory-learning Scenario | Ordinary Trials freeze initial Memory/Recall/permissions and suppress unscripted learning via supported controls. Learning cases explicitly drive the real workflow and separate background evidence/cost | Configuration plus actual background activity and cross-Trial isolation; production defaults remain unchanged; Q187 |

### 2.2 N+1 and complete Scenarios

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Reproduce one known next-turn failure | Restore preceding conversation and coherent exact business/Session/runtime/Proposal/source boundary, then execute only N+1. Do not replay historical model/Tool calls or writes to reconstruct it | Hydrated boundary, actual next-turn calls/effects; missing state is non-reproducible; Q178, Q183 |
| Need to prove state creation, Proposal progression, confirmation/refusal, CAS or revocation | Use a complete authored Scenario on real interfaces. Apply declared events at logical checkpoints, not wall-clock sleeps or a generative User Simulator | Reached inputs/events, actual structured results and canonical post-state; N+1 cannot claim preceding-history coverage; Q178, Q183 |
| Driver attempts confirmation with zero, multiple, or one actual matching Proposal | Only exactly one real Proposal satisfying declared conditions can be confirmed through Application. Missing preconditions are not repaired by arbitrary selection, DB success injection, fabricated consent or Agent hints | Actual Proposal match and Application confirmation/result; Q158 generating Run already ended; Q178 |
| Equivalent legal action/read order reaches a valid outcome | Accept the allowed path without requiring the illustrative sequence; retain strict target/version/confirmation and impact requirements | Scenario constraints and actual trajectory/state; Q180 |
| Observe canonical completion while telemetry is delayed/absent | Driver assertions use actual results/events/state, not span-arrival timing. Do not rerun or wait for a trace as a substitute for proof of business action | Actual canonical evidence and separate telemetry condition; Q174, Q178 |

### 2.3 Evaluator inputs, authority, and conclusions

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Put expected answers, future Turns, confirmation scripts, rubrics or previous Trial scores in Dataset content | Agent-under-test can access only reached current/past inputs and admitted business data, not evaluation reference or hidden Scenario control through prompts or Tools | Actual Agent Frames/Tool access compared with the three distinct input roles; Q185 |
| Embed instructions to change scoring inside candidate output or Tool text | Judge treats task-produced text as untrusted evidence; trusted rubric/control is unchanged | Actual judge input/control and observed assessment; include semantic review of attempted influence; Q185 |
| Judge Resume Fit, Candidate Fit or Advisor using potentially broader audit state | Semantic judge receives only necessary admitted assessed evidence: no Candidate supplement to Resume Fit, no excluded facts for Candidate Fit, and no confusion between Session assertions and saved facts for Advisor | Actual judge-visible inputs separately from deterministic audit access; unavailable necessary evidence stays incomplete; Q184 |
| Judge fails, changes opinion, or incurs cost after a task commits | Original task outcome/Domain state/budget remains unchanged; Eval costs and execution stay distinct. Do not assume platform judge calls inherit business Runtime fencing/reservation | Canonical before/after state, separate judge configuration/cost and findings; Q176 |
| One deterministic check finds a violation while judge is unavailable, or task succeeds with incomplete checks | Preserve each actual conclusion and missing scope. Correct business rejection may pass its expected behavior; do not erase a finding, drop a sample, or count missing evidence as pass | Actual task outcome plus per-check evidence/error/coverage reporting; representations/denominators remain pending; Q179 |
| Semantically valid alternative differs from a gold sentence/citation/Tool sequence | Check required meaning/coverage/support and allowed behavior, not unique wording. Exact references and permissions stay strict; ambiguous expected meaning receives review/unassessable disposition | Reviewed constraints, deterministic identity checks and scoped semantic review; Q180 |

### 2.4 Telemetry, regression retention, and re-evaluation

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Fail Langfuse upload, lose spans, or disable observations during a successful local task | No rollback, reexecution, duplicate settlement or changed business outcome. Missing span alone need not invalidate a sufficiently evidenced local check; missing required evidence is explicitly incomplete | Controlled export outage, canonical invocation/commit/usage and actual available check evidence; Q174, Q178–Q179 |
| Observe graph callbacks and explicit SDK/auxiliary paths | Common pre-export redaction and admitted canonical correlation; no duplicated invocation/cost counts. Calls outside callback-producing nodes remain observable without becoming a new authority | Exported controlled samples versus actual Run/Model/Tool activity, including repair/compaction/recovery; Q174 |
| Attempt full sensitive export or a judge requests raw evidence | Self-hosting grants no permission. Default observations remain minimal and admitted; secrets stay excluded; evaluator evidence has separate task-scoped admission | Actual callback/SDK exports and judge inputs, [Acceptance 10](../acceptance.md#10-privacy-storage-and-honest-history); Q125, Q174, Q184 |
| Promote a production failure into a retained regression | Human review precedes a minimal admissible sanitized/synthetic fixture. Transform refs consistently and verify the failure mechanism still holds; raw trace is not truth or permission to copy Workspace | Reviewed expected behavior and reproducible transformed case; raw sensitive sources retain independent retention; Q181 |
| Source payload expires and no admissible executable fixture remains | Disclose missing executable regression coverage. A lineage/hash does not prove content availability; do not retain raw data indefinitely for convenience | Actual retained fixture/evidence availability and coverage statement; Q181 |
| Change evaluator/rubric or retry judge on retained Trial evidence | Reassess same actual outcome/trajectory/post-state, preserve prior evaluations, and identify new evaluator configuration. No Agent/Tool/mutation replay; judge cost remains separate | Captured original evidence and new evaluation lineage/calls; initial fixture is not original post-state; Q182 |
| Required original evidence is purged during re-evaluation | Report unavailable/incomplete check without silently rerunning task. Intentional new execution is a new Trial with fresh frozen inputs and independent cost | Evidence availability and absence of undeclared execution; Q182 |

Later platform integration verification must use actual selected versions and deployment configuration. The accepted LangGraph/self-hosted Langfuse direction and research appendix do not prove that callbacks, workers, judges, masking or SDK features are installed and functioning. JobHunter remains thin task/Scenario/domain integration; generic platform features need no second implementation or generic Telemetry Port.

**Sources:** Q173–Q187, S35.1; Architecture 15; Eval sections 4–6, 18–31 and research Appendix A.

## 3. Semantic quality, reliability, and efficiency evidence

### 3.1 Capability-specific review

The following identifies required evaluation questions and evidence, not frozen formulas, scoring payloads, numerical targets, dataset sizes, or a requirement to implement every candidate metric listed in the Eval record.

Expected outputs express required meaning, coverage, grounded support, and allowed behavior. Accept legitimate semantic alternatives; do not require a unique sentence, requirement decomposition, valid citation choice, or Tool order. Exact identities, versions, authorization, and scope remain strict. If a required source is already legally available as an admitted pinned input, do not demand a redundant read solely for a metric. Ambiguous expectations require review or an explicit unassessable disposition, not self-certification by the Agent under test.

| Capability/dimension | What evaluation must examine | Evidence and interpretation limits |
| --- | --- | --- |
| RequirementParse | Omitted/hallucinated/duplicate requirements, valid source support, necessity and logical alternatives/uncertainty, bounded repair and final failure | Exact JD and produced Set, real-JD tests/manual checks; structural/source-span validation and semantic coverage are separate; Q111, Q117, Q171 |
| Candidate Fit | Supported MATCHED/PARTIAL, false negatives, appropriate UNKNOWN, exact admitted facts, one-to-one Requirement coverage and defensible score availability | Producing Frame, exact Requirements/baseline, output/support, scoped semantic review; missing support is not real-world incapability; Q82–Q83, Q112, Q115, Q168 |
| Resume Fit | Unsupported match, Candidate/other-Resume leakage, wrong version, bounded absence of expression, UNKNOWN and score availability | Actual exact Resume/Requirements, Frame/access and support; separate deterministic leakage from semantic quality; no ordered Candidate/Resume scores; Q112, Q115, Q168, Q184 |
| Advisor outcome and grounding | Relevant, specific, actionable, clear advice; supported rewrites; legitimate Session claims versus saved facts; real target/patch/confirmed effect | Scoped human-calibrated semantic judgments plus canonical mutation/authorization; correct shared-fact propagation is not unauthorized fan-out; Q133, Q138, Q146, Q148–Q149, Q156, Q158 |
| Trajectory and Tool behavior | Necessary versus unrelated/repeated actions, valid arguments and exact objects, allowed alternative paths, forbidden attempts versus effects | Actual invocations/access/results and Scenario constraints; no universal redundant-read requirement or conflated enforcement/behavior score; Q143–Q144, Q173, Q180 |
| Context behavior | Necessary admitted acquisition, unnecessary/forbidden content, actual exact versions, protected-input inclusion and safe compaction | Actual Frames and source/permission evidence; available Package content is not proof of visibility; Q80, Q83, Q132, Q139, Q172 |
| Authorization and authority | Exact confirmation, permission, target/version/impact, real commits and absence of forbidden replay | Deterministic state/admission/fault checks from [Acceptance 4–11](../acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts) and section 2; fluent prose/judges never replace production enforcement; Q118, Q122, Q148–Q149, Q174–Q176 |
| Reliability and efficiency | Single-attempt experience, variation across declared repeated Trials, failed/unknown attempts, repair/loop behavior, actual calls/steps/tokens/cost/latency | Report measured path, counts and limitations; background and judge costs separate; partial paths are not complete-workflow performance; Q175–Q176, Q179, Q186–Q187 |

Calibrate semantic judges with human review of appropriately admitted task evidence. A resolvable EvidenceRef/source span or matching hash is not semantic entailment. Preserve unsupported positive judgments and false negatives as visible findings rather than hiding them in an overall average. Samples, agreement measures, bias controls, metric matching/denominators and numerical targets remain later Eval/Contract work.

**Sources:** Q82, Q117, Q175–Q176, Q179–Q180, Q184, Q186; Eval sections 11–19 and 26; Product 11; Architecture 15.1–15.4.

### 3.2 Comparable experiments and honest reporting

Hard invariant findings, quality, reliability, cost, and latency remain separate. Assess absolute quality and regression against a declared approved comparison baseline independently. Thresholds, Trial counts, default enablement, release consequences, and repository/CI policy are not set here. Q117 still requires real-JD tests, manual checks, and traceable quality work without mandatory annotated ParserVersion publication certification.

Use separate development and holdout datasets by Skill with positive, negative, boundary and regression intent. Dataset names and case counts in source examples are not required identifiers or sizes. Holdout used for targeted tuning loses an independent-performance claim; disclose the contamination. User-configured acquisition scope or a few example occupations/cities establishes no wider demonstrated quality.

Declare recorded replay versus live model, exact input/configuration, Skill-focused versus composed workflow, N+1 versus full Scenario, and controlled Memory/learning scope. Reproducible inputs do not guarantee identical remote outputs. Pass@1 describes the single-attempt experience; repeated Trials show variability, not best-of-N selection. Keep an independent Trial distinct from bounded in-Run repair and explicit user Retry after unknown outcome, and retain failed/unknown attempts in the evidence.

Reports keep Hard Gate findings, semantic quality, reliability and efficiency separate, with actual checked scope and unfinished checks. Quality improvement cannot compensate for an authority/permission/replay violation. Absolute quality and relative regression comparisons answer different questions; an improved average alone does not establish an absolute target. No baseline approval, target attainment or release readiness is inferred from this document.

Regression expectations remain while their governing behavior remains effective. If a later decision supersedes that behavior, update the case meaning and source trace deliberately; do not restore old mechanisms for compatibility with an old fixture. Privacy-safe retained intent and original production-payload retention remain distinct under section 2.4.

**Sources:** Q4, Q117, Q175, Q177–Q187, S17.1, S37.1; Eval sections 8–10, 18–21 and 29–31.
