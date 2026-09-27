# Agent Evaluation

> English is authoritative. This guide brings Eval acceptance criteria and execution procedure together. It creates no new product/runtime authority, normative interface, release policy or claim of executed acceptance.

[Documentation index](index.md) · [Acceptance](acceptance.md) · [Development](development.md)

## 1. Scope and ownership

[Product](spec.md#11-quality-and-evidence-boundaries) owns behavior and [Architecture](architecture.md#15-eval-and-observability) owns mechanisms and Eval/runtime boundaries. Main [Acceptance](acceptance.md) remains the unified product/system proof owner; section 2 supplies its specialized Eval criteria. Main [Development](development.md) owns delivery discipline; section 3 supplies its Eval workflow and consumes section 2 without defining another oracle. A judge or quality average cannot replace deterministic product/runtime proof.

[Actual Contracts](contracts/index.md) own reviewed detailed interfaces and requirements. The [Implementation Plan](plans/implementation-plan.md) and selected Slice identify consumed scope. [Progress recording rules](progress/recording-rules.md) define status and evidence recording; [Progress](progress.md) and [traceability](progress/traceability.md) record actual readiness/results. Producing evidence does not itself establish milestone completion. Document-authoring verification remains in [Development 9.2](development.md#92-two-separate-verification-seams).

RequirementParse/Fits, Advisor, Context/Tools, authority and Memory evidence also consumes the relevant Product/Architecture and main Acceptance scenarios. [Acceptance 2](acceptance.md#2-evidence-and-interpretation-rules) supplies general evidence interpretation. Fields, evaluator interfaces, metrics/denominators, numerical thresholds and rollout decisions remain pending with their existing owners; this consolidation resolves none of them.

Section 2 retains former `acceptance/evaluation.md` criteria: its §§2.1–2.5 are now §§2.1.1–2.1.5 and its §§3.1–3.2 are now §§2.2.1–2.2.2. Historical V12/V13 references still originate in main Acceptance 12/13. Section 3 retains former `development/evaluation.md` §§2–5 and Development 7.1–7.4 procedure. Source Q/S references remain provenance; section names are locators, not Contract IDs or runnable tests.

## 2. Evaluation acceptance criteria

This section defines what Eval must prove and the limits on conclusions. It supplements the unified business/runtime scenarios without splitting those scenarios by business domain.

### 2.1 Eval execution and evidence integrity

CG03S1 supersedes parallel Fits and current assistant application. Proposal/confirmation Scenario examples below apply only to deferred SL-07.M3/SL-10.M2; current portrait/DeepFit/optimization proof uses EVO-027 without adding a runtime semantic judge.

**Design owner:** [Architecture 15](architecture.md#15-eval-and-observability), grounded in Q173–Q187 and the historical Agent Evaluation record (the standalone source file has been deleted). These scenarios verify that later evaluation measures the intended real path and reports defensible evidence. They do not claim a deployed Langfuse installation, verified SDK behavior, or implemented runner.

#### 2.1.1 Isolation, exact inputs, and declared experiment scope

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Execute an isolated Trial that commits a confirmed change | Use real Application/Domain/Repository/Harness/validators and production prompts/permissions; changes affect test state only. Controlled external adapters prevent real platform effects without bypassing guards | Task entry, actual test-state effects and external isolation; no test-only Agent; Q173 |
| Run independent Trials, including successful mutations, approvals or learned Memory | Each reconstructs its own immutable fixture; no cross-Trial state leakage. A declared multi-step Scenario retains only its intended internal progression | Initial and final fixture/state identities, isolation and guard evidence; Q173, Q177, Q187 |
| Resolve exact Dataset version with missing/mismatched/unrecoverable business input or configuration | Explicit non-reproducibility; never fall back to latest Workspace roots, current permissions or a guessed checkpoint. Freeze fixture, authored events/expectations and exact execution/evaluator configuration | Resolved immutable references, hashes and actual configuration; no claim of identical remote model text; Q177 |
| Measure Fit with a preexisting compatible Set versus a workflow needing parse | Both use real Ensure. Ready-Set experiment measures Fit, not parser quality; workflow records dependency preparation actually executed. Failed dependency does not count unexecuted Fit as success or bad Fit semantics | Declared scope, actual stage lineage/outcomes/cost; partial path is not end-to-end cost/quality; Q186 |
| Run ordinary Advisor comparison versus a Memory-learning Scenario | Ordinary Trials freeze initial Memory/Recall/permissions and suppress unscripted learning via supported controls. Learning cases explicitly drive the real workflow and separate background evidence/cost | Configuration plus actual background activity and cross-Trial isolation; production defaults remain unchanged; Q187 |

#### 2.1.2 N+1 and complete Scenarios

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Reproduce one known next-turn failure | Restore preceding conversation and coherent exact business/Session/runtime/Proposal/source boundary, then execute only N+1. Do not replay historical model/Tool calls or writes to reconstruct it | Hydrated boundary, actual next-turn calls/effects; missing state is non-reproducible; Q178, Q183 |
| Need to prove state creation, Proposal progression, confirmation/refusal, CAS or revocation | Use a complete authored Scenario on real interfaces. Apply declared events at logical checkpoints, not wall-clock sleeps or a generative User Simulator | Reached inputs/events, actual structured results and canonical post-state; N+1 cannot claim preceding-history coverage; Q178, Q183 |
| Deferred assistant-apply Scenario: driver attempts confirmation with zero, multiple, or one actual matching Proposal | Only exactly one real Proposal satisfying declared conditions can be confirmed through Application. Missing preconditions are not repaired by arbitrary selection, DB success injection, fabricated consent or Agent hints | Actual Proposal match and Application confirmation/result; Q158 generating Run already ended; Q178 |
| Equivalent legal action/read order reaches a valid outcome | Accept the allowed path without requiring the illustrative sequence; retain strict target/version/confirmation and impact requirements | Scenario constraints and actual trajectory/state; Q180 |
| Observe canonical completion while telemetry is delayed/absent | Driver assertions use actual results/events/state, not span-arrival timing. Do not rerun or wait for a trace as a substitute for proof of business action | Actual canonical evidence and separate telemetry condition; Q174, Q178 |

#### 2.1.3 Evaluator inputs, authority, and conclusions

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Put expected answers, future Turns, confirmation scripts, rubrics or previous Trial scores in Dataset content | Agent-under-test can access only reached current/past inputs and admitted business data, not evaluation reference or hidden Scenario control through prompts or Tools | Actual Agent Frames/Tool access compared with the three distinct input roles; Q185 |
| Embed instructions to change scoring inside candidate output or Tool text | Judge treats task-produced text as untrusted evidence; trusted rubric/control is unchanged | Actual judge input/control and observed assessment; include semantic review of attempted influence; Q185 |
| Judge Profile, DeepFit or optimization | Judge only the admitted exact source: Profile/Evidence support, frozen DeepFit coverage or selected Resume; no other-document/Memory/chat career supplementation | Actual judge input is separate from broader deterministic audit; incomplete required evidence is not a pass; EVO-027 |
| Judge fails, changes opinion, or incurs cost after a task commits | Original task outcome/Domain state/budget remains unchanged; Eval costs and execution stay distinct. Do not assume platform judge calls inherit business Runtime fencing/reservation | Canonical before/after state, separate judge configuration/cost and findings; Q176 |
| One deterministic check finds a violation while judge is unavailable, or task succeeds with incomplete checks | Preserve each actual conclusion and missing scope. Correct business rejection may pass its expected behavior; do not erase a finding, drop a sample, or count missing evidence as pass | Actual task outcome plus per-check evidence/error/coverage reporting; representations/denominators remain pending; Q179 |
| Semantically valid alternative differs from a gold sentence/citation/Tool sequence | Check required meaning/coverage/support and allowed behavior, not unique wording. Exact references and permissions stay strict; ambiguous expected meaning receives review/unassessable disposition | Reviewed constraints, deterministic identity checks and scoped semantic review; Q180 |

#### 2.1.4 Telemetry, regression retention, and re-evaluation

| Scenario and trigger | Required observable outcome | Required evidence and controlling sources |
| --- | --- | --- |
| Fail Langfuse upload, lose spans, or disable observations during a successful local task | No rollback, reexecution, duplicate settlement or changed business outcome. Missing span alone need not invalidate a sufficiently evidenced local check; missing required evidence is explicitly incomplete | Controlled export outage, canonical invocation/commit/usage and actual available check evidence; Q174, Q178–Q179 |
| Observe graph callbacks and explicit SDK/auxiliary paths | Common pre-export redaction and admitted canonical correlation; no duplicated invocation/cost counts. Calls outside callback-producing nodes remain observable without becoming a new authority | Exported controlled samples versus actual Run/Model/Tool activity, including repair/compaction/recovery; Q174 |
| Attempt full sensitive export or a judge requests raw evidence | Self-hosting grants no permission. Default observations remain minimal and admitted; secrets stay excluded; evaluator evidence has separate task-scoped admission | Actual callback/SDK exports and judge inputs, [Acceptance 10](acceptance.md#10-privacy-storage-and-honest-history); Q125, Q174, Q184 |
| Promote a production failure into a retained regression | Human review precedes a minimal admissible sanitized/synthetic fixture. Transform refs consistently and verify the failure mechanism still holds; raw trace is not truth or permission to copy Workspace | Reviewed expected behavior and reproducible transformed case; raw sensitive sources retain independent retention; Q181 |
| Source payload expires and no admissible executable fixture remains | Disclose missing executable regression coverage. A lineage/hash does not prove content availability; do not retain raw data indefinitely for convenience | Actual retained fixture/evidence availability and coverage statement; Q181 |
| Change evaluator/rubric or retry judge on retained Trial evidence | Reassess same actual outcome/trajectory/post-state, preserve prior evaluations, and identify new evaluator configuration. No Agent/Tool/mutation replay; judge cost remains separate | Captured original evidence and new evaluation lineage/calls; initial fixture is not original post-state; Q182 |
| Required original evidence is purged during re-evaluation | Report unavailable/incomplete check without silently rerunning task. Intentional new execution is a new Trial with fresh frozen inputs and independent cost | Evidence availability and absence of undeclared execution; Q182 |

Later platform integration verification must use actual selected versions and deployment configuration. The accepted LangGraph/self-hosted Langfuse direction and research appendix do not prove that callbacks, workers, judges, masking or SDK features are installed and functioning. JobHunter remains thin task/Scenario/domain integration; generic platform features need no second implementation or generic Telemetry Port.

**Sources:** Q173–Q187, S35.1; Architecture 15; Eval sections 4–6, 18–31 and research Appendix A.

#### 2.1.5 SL-03.M2 infrastructure proof

The former SL-03.M2 Contract and conformance agreement have been withdrawn for S3 redevelopment. Their specific proof matrix is removed. Define replacement acceptance against newly reviewed Contracts before implementation; general system and consumer-specific acceptance elsewhere remains applicable.

### 2.2 Semantic quality, reliability, and efficiency evidence

#### 2.2.1 Capability-specific review

The following identifies required evaluation questions and evidence, not frozen formulas, scoring payloads, numerical targets, dataset sizes, or a requirement to implement every candidate metric listed in the Eval record.

Expected outputs express required meaning, coverage, grounded support, and allowed behavior. Accept legitimate semantic alternatives; do not require a unique sentence, requirement decomposition, valid citation choice, or Tool order. Exact identities, versions, authorization, and scope remain strict. If a required source is already legally available as an admitted pinned input, do not demand a redundant read solely for a metric. Ambiguous expectations require review or an explicit unassessable disposition, not self-certification by the Agent under test.

| Capability/dimension | What evaluation must examine | Evidence and interpretation limits |
| --- | --- | --- |
| RequirementParse | Omitted/hallucinated/duplicate requirements, valid source support, necessity and logical alternatives/uncertainty, bounded repair and final failure | Exact JD and produced Set, real-JD tests/manual checks; structural/source-span validation and semantic coverage are separate; Q111, Q117, Q171 |
| DeepFit | Requirement-to-Evidence support, Profile omission versus true source-bounded negative, progressive coverage, UNKNOWN, optional Preference Fit versus Capability Fit | Actual frozen Job/Requirements/portrait/optional intent, producing Frames/Tool results and coverage; no parallel analysis or real-world incapability inference; EVO-027 |
| Resume Optimization | Generic/targeted suggestion usefulness and fidelity, no invented metrics/unsupported upgrades, selected-source isolation, empty-input response | Exact selected Resume (+Job/Requirements in targeted mode), actual Frames and no formal mutation; populated B with empty default A; EVO-027 |
| Evidence and Profile derivation | Deterministic text/ID fidelity; Entry-scoped support and no cross-Entry merge; complete dirty-Entry context; empty versus missing groups; semantic omissions/upgrades; excluded-input leakage; entire invalid-output rejection | Exact baseline/target/diff and actual current-version single-call Frame/grouped result; unchanged/deleted groups, exact reattachment and ref rebinding; mixed provenance, explicit full refresh and frozen-merge recovery; schema success alone is not semantic proof; EVO-027/028 |
| Advisor outcome and grounding | Relevant, specific, actionable, clear advice; supported rewrites; legitimate Session claims versus saved facts; real target/patch/confirmed effect | Scoped human-calibrated semantic judgments plus canonical mutation/authorization; BC3 authorizes only the confirmed Resume-local change; new/corrected facts need a separate explicit Knowledge flow, not cross-Resume fan-out; Q133, Q138, Q146, Q148–Q149, Q156, Q158 |
| Trajectory and Tool behavior | Necessary versus unrelated/repeated actions, valid arguments and exact objects, allowed alternative paths, forbidden attempts versus effects | Actual invocations/access/results and Scenario constraints; no universal redundant-read requirement or conflated enforcement/behavior score; Q143–Q144, Q173, Q180 |
| Context behavior | Necessary admitted acquisition, unnecessary/forbidden content, actual exact versions, protected-input inclusion and safe compaction | Actual Frames and source/permission evidence; available Package content is not proof of visibility; Q80, Q83, Q132, Q139, Q172 |
| Authorization and authority | Exact confirmation, permission, target/version/impact, real commits and absence of forbidden replay | Deterministic state/admission/fault checks from [Acceptance 4–11](acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts) and section 2.1; fluent prose/judges never replace production enforcement; Q118, Q122, Q148–Q149, Q174–Q176 |
| Reliability and efficiency | Single-attempt experience, variation across declared repeated Trials, failed/unknown attempts, repair/loop behavior, actual calls/steps/tokens/cost/latency | Report measured path, counts and limitations; background and judge costs separate; partial paths are not complete-workflow performance; Q175–Q176, Q179, Q186–Q187 |

Calibrate semantic judges with human review of appropriately admitted task evidence. A resolvable EvidenceRef/source span or matching hash is not semantic entailment. Preserve unsupported positive judgments and false negatives as visible findings rather than hiding them in an overall average. Samples, agreement measures, bias controls, metric matching/denominators and numerical targets remain later Eval/Contract work.

**Sources:** Q82, Q117, Q175–Q176, Q179–Q180, Q184, Q186; Eval sections 11–19 and 26; Product 11; Architecture 15.1–15.4.

#### 2.2.2 Comparable experiments and honest reporting

Hard invariant findings, quality, reliability, cost, and latency remain separate. Assess absolute quality and regression against a declared approved comparison baseline independently. Thresholds, Trial counts, default enablement, release consequences, and repository/CI policy are not set here. Q117 still requires real-JD tests, manual checks, and traceable quality work without mandatory annotated ParserVersion publication certification.

Use separate development and holdout datasets by Skill with positive, negative, boundary and regression intent. Dataset names and case counts in source examples are not required identifiers or sizes. Holdout used for targeted tuning loses an independent-performance claim; disclose the contamination. User-configured acquisition scope or a few example occupations/cities establishes no wider demonstrated quality.

Declare recorded replay versus live model, exact input/configuration, Skill-focused versus composed workflow, N+1 versus full Scenario, and controlled Memory/learning scope. Reproducible inputs do not guarantee identical remote outputs. Pass@1 describes the single-attempt experience; repeated Trials show variability, not best-of-N selection. Keep an independent Trial distinct from bounded in-Run repair and explicit user Retry after unknown outcome, and retain failed/unknown attempts in the evidence.

Reports keep Hard Gate findings, semantic quality, reliability and efficiency separate, with actual checked scope and unfinished checks. Quality improvement cannot compensate for an authority/permission/replay violation. Absolute quality and relative regression comparisons answer different questions; an improved average alone does not establish an absolute target. No baseline approval, target attainment or release readiness is inferred from this document.

Regression expectations remain while their governing behavior remains effective. If a later decision supersedes that behavior, update the case meaning and source trace deliberately; do not restore old mechanisms for compatibility with an old fixture. Privacy-safe retained intent and original production-payload retention remain distinct under section 2.1.4.

**Sources:** Q4, Q117, Q175, Q177–Q187, S17.1, S37.1; Eval sections 8–10, 18–21 and 29–31.

## 3. Evaluation workflow

This section describes how developers prepare, run, compare, retain and reassess Eval evidence under the criteria above. It adds no competing isolation, admission, evidence-completeness or quality rule.

### 3.1 Real paths, isolation, and exact experiments

Prepare the selected thin JobHunter task adapters, domain-aware checks, fixture hydration and authored Scenario driving around the selected Langfuse facilities and existing Application/Domain/Repository/Harness boundaries. Apply [Architecture 9/15](architecture.md#9-shared-harness-skills-and-controlled-actions) for runtime ownership and the [general research discipline](development.md#4-research-and-integration-preparation) for actual version/integration verification; this does not select a runner or create a second Eval platform.

For the chosen case, assemble the fixture, Dataset references, authored events/expectations and execution/evaluator configuration, then execute on the declared path and capture actual state/call evidence. Use [Isolation and exact-input criteria](#211-isolation-exact-inputs-and-declared-experiment-scope) as the checklist for isolation, exact inputs, reproducibility and measured scope. Select the ready-Requirements or composed Fit path and the ordinary Advisor or explicit Memory-learning setup that matches the intended claim; retain the configuration and actual stage/background evidence needed by that checklist.

**Sources:** Q120–Q122, Q140, Q173, Q177, Q186–Q187, S35.1; Architecture 9/15; [Isolation and exact-input criteria](#211-isolation-exact-inputs-and-declared-experiment-scope).

### 3.2 Scenario integrity and evaluator admission

Choose a localized N+1 case or complete authored Scenario according to the proof requested in [Scenario criteria](#212-n1-and-complete-scenarios). Hydrate the corresponding boundary or initial fixture, drive authored events at logical checkpoints through the real interfaces and collect the reached inputs, actual Proposal matching/confirmation, trajectory and canonical post-state for its assertions. Evaluate the result against those criteria rather than adding driver shortcuts to repair an unmet precondition.

Prepare Agent inputs, evaluation references and Scenario control separately; prepare each checker/judge's admitted evidence and configuration using [Evaluator criteria](#213-evaluator-inputs-authority-and-conclusions). Run deterministic checks and separately configured judges against captured evidence, retaining actual checker inputs and findings for review. The linked criteria own visibility, trusted-control, authority and cost boundaries; this procedure does not redefine them or assume that platform judges inherit business Runtime guarantees.

**Sources:** Q158, Q173, Q176, Q178, Q180, Q183–Q185; Architecture 15.2–15.3; [Scenario and evaluator criteria](#212-n1-and-complete-scenarios).

### 3.3 Findings, comparison, and release-policy boundary

Collect task results, deterministic findings, judge findings/errors and evidence availability, then prepare the checked-scope report under [Evaluator criteria](#213-evaluator-inputs-authority-and-conclusions) and the [Progress recording rules](progress/recording-rules.md). Those owners define admissible conclusions and status; producing a report does not itself establish acceptance.

Use the selected development/holdout inputs and declared comparison configuration to run the relevant capability checks, human calibration and comparisons in [Quality, reliability and efficiency criteria](#22-semantic-quality-reliability-and-efficiency-evidence). Assemble actual sample/attempt counts, source/input/configuration references, semantic review, task/background/judge observations and limitations needed by those criteria. They own semantic alternatives, contamination, single-attempt versus repeated-Trial interpretation, separate quality/reliability/efficiency claims and deferred rollout boundaries; this guide sets no competing pass formula, threshold or release rule.

**Sources:** Q82, Q117, Q168, Q174–Q180, Q184, Q186–Q187, S17.1; [Acceptance 2](acceptance.md#2-evidence-and-interpretation-rules) and [Quality, reliability and efficiency criteria](#22-semantic-quality-reliability-and-efficiency-evidence); Eval sections 8–10, 18–20 and 26.

### 3.4 Privacy, regression retention, and re-evaluation

Apply [Telemetry and retained-evidence criteria](#214-telemetry-regression-retention-and-re-evaluation) when promoting a production case, retaining regression evidence or reassessing an existing Trial. Conduct the human review, prepare the admissible sanitized/synthetic fixture, reconcile its references and verify that it still exercises the reviewed failure mechanism. Record available evidence and any resulting coverage gap under Progress rules; the linked criteria own retention and completeness requirements.

For evaluator/rubric reassessment, locate the retained actual Trial evidence, run the selected evaluation against it and preserve earlier evaluation history plus the new configuration/lineage. Use the same section's distinction between re-evaluation and intentional new Trial execution when choosing the procedure and recording cost. Its prohibition on silently recreating unavailable original evidence remains controlling.

At telemetry integration, verify the selected callback and explicit SDK paths with controlled export/admission/correlation cases from section 2.1.4 and the [privacy/history scenarios](acceptance.md#10-privacy-storage-and-honest-history). Collect actual exported samples and canonical evidence for those checks. Architecture and Eval acceptance retain ownership of local authority, masking/admission, evaluator privacy and limits on telemetry conclusions.

**Sources:** Q125, Q136, Q174, Q176, Q178–Q179, Q181–Q184; Architecture 13/15.4–15.5; [Acceptance 10](acceptance.md#10-privacy-storage-and-honest-history) and [Telemetry and retained-evidence criteria](#214-telemetry-regression-retention-and-re-evaluation).

## 4. Related documents

| Owner | Read for |
| --- | --- |
| [Architecture: Eval and observability](architecture.md#15-eval-and-observability) | System boundaries and authority |
| [Acceptance](acceptance.md) | General proof interpretation and business/runtime scenarios |
| [Development](development.md) | Delivery, source/research, verification and handoff discipline |
| [Evaluation / Observability Contract](contracts/evaluation/evaluation-observability.md) and [Contract Index](contracts/index.md) | Retained normative scope and planned/withdrawn scope; existence is not readiness |
| [Progress](progress.md) and [traceability](progress/traceability.md) | Recorded outcomes, coverage and evidence limitations |
| [Grill records](.grill/README.md) | Retained decisions and scoped supersession; the standalone Eval design file was deleted |

Legacy references to Eval source sections and its research appendix retain their historical meaning; they do not imply that the deleted file or old SL-03 foundations are available. Read retained source IDs and current formal owners rather than reconstructing a deleted source as an approved design.
