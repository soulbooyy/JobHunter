# Agent Evaluation and Observability — Detailed Architecture Design Record

## Status, scope, and precedence

- Source: the user's complete 30-part Eval architecture submitted after Q172; recorded 2026-09-18.
- Accepted direction: LangGraph execution, self-hosted Langfuse as the preferred Eval/observability
  platform, and a thin JobHunter integration using real Application/Harness entry points.
- This document preserves the full architectural proposal, not an implemented platform, final
  schema, release certification, or new source of business authority. Formal specifications remain
  in the project's normative documents; exhaustive fields belong to the separate Contract Grill.
- Eval Grill normally updates exactly three records: this detailed architecture, the decision
  register's questions/answers, and the Contract inventory's future objects/properties. Harness
  modules change only when an accepted decision genuinely changes their design; merely testing an
  invariant, adding an evaluator, or posing an Eval question does not qualify. Eval coverage and
  integration descriptions stay here rather than being copied into each Harness module.
- Q173-Q187 are ACCEPTED: isolated real-path trials, derived observability, independent judges,
  exact fixtures, fixed-input N+1/Scenario execution and boundary state, per-check conclusions,
  semantic alternatives, privacy-safe regression retention, re-evaluation, task-scoped evaluator
  evidence, answer/control isolation, experiment scope, and controlled Memory/background activity.
  Proposed code/metrics are not final schemas. Trial counts, thresholds,
  default enablement, and release/rollout policy are explicitly outside this architecture Grill (Q175).
- Rebuild direction — S37.1: implement Eval anew against the effective contracts; old runners,
  fixtures, tests and code impose no mandatory reuse, compatibility or migration duty. The real
  production path means the new JobHunter Application/Harness, not a parallel test Agent.
- Handoff — S38.1: this design moves with the other Grill records to the separate JobHunter
  repository. Documentation planning/writing/review precedes detailed Contract Grill and Contract
  documents; formal implementation starts afterward. This transfer creates no Eval code or service.
- Existing semantics still apply: Q113 Save-as-confirmation; Q138 session-sourced suggestions;
  Q146/Q148/Q149 target-specific Proposal and confirmation; Q163 whole-experience inclusion;
  Q168 valid unscored Analysis; Q172 protected-input revocation. Evaluation must test these rules,
  not restore historical Coverage, working-draft, KnowledgeConfirmation, or RAG-first designs.

Related: [Decision Register](../grill-me-design-tree.md),
[Contract Inventory](../contract/contract-design-inventory.md),
[Context](../harness/context.md), [Tool Actions](../harness/tool.md),
[Budget](../harness/budget.md), [Recovery](../harness/recovery.md),
[Storage](../harness/storage.md), [Memory](../harness/memory.md).

## 1. Goal: evaluate the complete Agent system

The evaluated system is Model + Prompt/Skill Contract + Context Engineering + Tool use + Harness
+ Business State. A fluent final answer alone is not evidence of successful or safe execution.

Evaluation asks whether realistic job-search tasks finish correctly, respect Business Authority,
use correct exact versions and Tools, avoid unsupported factual claims, preserve Human Confirmation,
stay within permission/scope, remain stable, and use acceptable resources.

The dimensions are Outcome, Trajectory, Tool Behavior, Context Behavior, Grounding,
Authorization/Safety, Reliability, and Efficiency. No single overall Agent score replaces them.

## 2. Architectural ownership

| Layer | Responsibility | Must not delegate to evaluation |
| --- | --- | --- |
| Business Domain | Evidence, Resume, Job, RequirementSet, Preparation, ChangeProposal, MaterialApproval, ExecutionApproval and their invariants | What counts as saved truth or valid authorization |
| Application | Workflow/dependency orchestration, persistence, authority mutations, confirmation execution | Validation and atomic business commit |
| Shared Agent Harness | Run lifecycle, Context, Model/Tool Invocation Runtime, budget, recovery, fencing, audit | Production runtime enforcement |
| Eval/Observability Infrastructure | Datasets, experiments, evaluators, measurements, regression evidence | No independent business mutation or execution authority |

This is a responsibility separation, not a requirement that production depend synchronously on an
Eval service or that LangGraph wrap the Harness. LangGraph executes workflow mechanics within the
shared execution architecture; Provider calls still pass through ModelInvocationRuntime.

## 3. Platform choice and build-versus-buy boundary

- Agent execution: LangGraph under the established Harness/Application ownership.
- Eval and observability platform: self-hosted Langfuse.
- Guiding choice: **Langfuse-heavy, JobHunter-thin**.
- Langfuse owns generic dataset, experiment, evaluator, score, comparison, and dashboard capabilities.
- JobHunter retains real-task adapters, domain-aware deterministic checks, and production invariant
  enforcement. It does not build a second general Eval platform.
- No generic custom Telemetry Port is introduced solely to abstract the selected vendor. Direct
  CallbackHandler/SDK integration remains infrastructure code, not a Domain dependency.
- Hosting footprint, installed platform/SDK compatibility, optional workers, endpoint/privacy policy,
  outage behavior, and CI wiring still require explicit design/verification. Self-hosted does not
  mean all features are automatically configured, offline, or privacy-admitted.

## 4. End-to-end experiment architecture

```text
Langfuse Dataset + exact version + experiment configuration
                         |
                         v
                  JobHunter Eval Task
                         |
                         v
               real Application entry point
                         |
                         v
         shared Harness / AgentRun / LangGraph workflow
              |                             |
              v                             v
      Model/Tool Runtime             admitted observations
              |                             |
              v                             v
  Outcome + actual persisted state       Langfuse trace
              |                             |
              +--------------+--------------+
                             v
             Code checks + domain-aware checks + LLM judge
                             |
                             v
                 Scores / experiment evidence
                             |
                             v
                quality evidence for later release policy
```

Eval drives real behavior; observation does not replace canonical Run, Invocation, mutation, or DB
records. Evaluation evidence and a task's business result are different outputs.

### Isolated execution and reproducible scenario state — Q173/Q177

Each Case/Trial reconstructs an isolated business environment from a frozen immutable Fixture. It
uses the real Application, Domain, Repository, validators, and Harness; commits modify the test DB,
not the user's live Workspace. Different Trials do not inherit each other's mutation, approvals,
Memory, or current pointers. A multi-turn Scenario retains its own intended state between steps.

Use controlled external adapters with no real recruiting-account access, browser submission, or
other production side effects. Do not bypass Tool/Application admission to obtain isolation.
Human confirmation, refusal, concurrent updates, and permission changes are Scenario Events, not
consent generated by the Agent-under-test or uncontrolled changes from a live Workspace.

Recorded model replay demonstrates deterministic mechanics; live model Trials demonstrate behavior
under declared model/configuration conditions. Report these evidence classes distinctly.

### Fixed-input N+1 and complete Scenario paths — Q178

Comparable v1 multi-turn Agent evaluation uses authored user inputs and a deterministic Scenario
Driver. There is no generative User Simulator in the regression benchmark.

For a known localized conversational failure, prefer N+1: freeze the preceding N Turns' conversation
context and execute only the target next input through the real task path. This measures whether that
specific next-turn behavior is corrected, not whether the whole preceding conversation would be
generated successfully by the current Agent. Q183 requires coherent reconstruction of the necessary
business/session/runtime boundary state as well as messages. Hydrate exact saved versions, references,
Proposal state and required sources without replaying historical calls or writes; missing required
state makes the case non-reproducible. Never resolve references against production latest.

For Proposal generation, confirmation/refusal, revocation, concurrency, CAS and final DB-state
coverage, the thin JobHunter Scenario Driver reads frozen Fixture/Scenario definitions from the
Langfuse DatasetItem and sends the authored Turns through Application -> Harness -> LangGraph.

At explicit logical checkpoints it drives predeclared events, not wall-clock sleeps. Before
confirmation, inspect the real produced Proposal and require exactly one match satisfying the
scenario conditions. Zero/multiple matches or missing preconditions cannot be repaired by selecting
arbitrarily, editing the DB, inventing consent, or helping the Agent finish. Call the formal
Application confirmation interface; preserve normal revision checks and allowed mutation behavior.

Proposal display already ended the generating Turn/AgentRun (Q158). Confirmation is a separate
Application persistent interaction, not a resumed hanging AgentRun. Different Tool/action paths
are valid when they satisfy the MUST/MUST NOT and allowed-path contract.

Scenario assertions use actual task results, structured execution events and canonical Application/
DB evidence, not successful upload of observability spans. Langfuse supplies Dataset, Experiment,
platform Session/Trace grouping, Scores and Judge facilities; JobHunter owns Scenario orchestration
and business ChatSession/confirmation authority. No second general Eval framework is introduced.

The user adopts send -> Turn -> structured events, exact-one HITL matching, session isolation and
trace-independent assertions as design inspirations from NiceEval, not a new dependency or a claim
that its runtime replaces JobHunter's Proposal semantics. A future generative User Simulator would
be separate exploratory evaluation for discovering paths, not comparable deterministic regression.

## 5. Langfuse platform responsibilities

### Dataset and versioning

Store Eval inputs, expected outputs, metadata, tags, and case classifications in Langfuse datasets.
Experiments bind an exact dataset version rather than whatever items happen to be latest at read time.

Q177 additionally requires an immutable reconstructible Business Fixture, Scenario Events/Expected
Outcomes, and exact Skill, Prompt, Context Policy, Model, Evaluator/Rubric, and Runner configuration.
Dataset root IDs alone must never resolve against the user's current/latest Workspace during Eval.
A Fixture can live in Dataset payload or a controlled immutable artifact; its representation is
deferred, but stable references and hash validation are required.

Missing Fixture, mismatched hash, unrecoverable version, or unreconstructible exact input makes the
experiment explicitly non-reproducible. There is no silent fallback to latest Resume, Evidence,
permissions, or other state. Thin Fixture hydration, hash/config validation, and Scenario driving
are permitted without creating another Dataset Framework. Reproducibility covers business inputs,
configuration, and scoring conditions, not identical remote-LLM text on repeated calls.

### Expected behavior defines a boundary, not one golden answer — Q180

Expected Output expresses correct behavior constraints. IDs, exact versions, enums, permissions and
authorization relationships remain strict. Requirement decomposition, Evidence support and Advisor
advice may have multiple semantically equivalent or equally valid outcomes if the business contract,
grounding and Scenario constraints hold. Wording or Tool order alone is not a failure.

Review required meanings, necessary coverage, acceptable support alternatives and MUST/MAY/MUST NOT
constraints. Ambiguous expectations need refinement or an explicit unassessable case, not the
Agent-under-test certifying its own answer. A declared exact reference is checked exactly; multiple
allowed valid references are not reduced to one arbitrarily chosen gold citation. This does not
create a mandatory annotated parser-release certification or fixed dataset size.

### Experiments

Compare Prompt v1/v2, Model A/B, ContextPolicy versions, Tool descriptions, and Skill Contract versions.
Bind exact dataset, model/configuration, prompt, Skill, and Context policy identities. A stable model
name alone does not promise bit-for-bit reproducibility from a remote Provider.

### Code evaluators

Prefer platform/SDK evaluator facilities for checks expressible from supplied input/output/metadata:
schema, enum, source-span validity, expected classification, forbidden requested actions, argument
equality, required reads, wrong version refs, and required output fields. A checker must actually have
the source data needed for its assertion; source-span validity cannot be established from an ID alone.

### LLM-as-a-Judge

Use for relevance, actionability, specificity, clarity, rewrite quality, and semantic grounding.
Do not use a judge as the authority for whether confirmation occurred, which version was committed,
which protected resource was accessed, or whether Candidate-only data reached Resume Fit. Those
require deterministic observable/state checks. Semantic entailment is not proven merely by resolving
a reference; distinguish semantic judging from referential validity.

## 6. What remains in JobHunter

### Eval Task

RequirementParseTask, CandidateJobFitTask, ResumeJobFitTask, and ResumeAdvisorTask translate a
DatasetItem into real Application execution. Reuse the production Skill, validator, Context Builder,
Tool admission, business persistence, and Harness. Do not implement a test-only Agent with different
prompts, permissions, success rules, or hidden shortcuts.

### Domain-aware contract evaluator

Keep checks local when they need Repository hydration, SQLite, Domain relationships, or Application
state: authority consistency, immutable lineage, actual committed mutations, confirmed Proposal
exactness, cross-Resume propagation, and authorization relationships. Publish content-safe outcomes
as Langfuse Scores; do not duplicate the full Business Authority database there.

The check is against the complete confirmed target/patch/impact, not merely a requested Resume ID.
Authorized shared-Evidence changes must update other affected current Resumes under Q114/Q118;
that declared fan-out is not automatically unauthorized mutation.

### Runtime enforcement

Application rejects unconfirmed mutations in production regardless of Langfuse availability.
Eval verifies the rejection worked; it does not supply the runtime guard.

## 7. Proposed thin code organization

```text
evals/
  tasks/
    requirement_parse.py
    candidate_job_fit.py
    resume_job_fit.py
    resume_advisor.py
  contracts/
    authority.py
    lineage.py
    grounding.py
    authorization.py
    mutation.py
  experiments/
    requirement_parse.py
    candidate_job_fit.py
    resume_job_fit.py
    resume_advisor.py
  scenarios/
    driver.py
  common/
    environment.py
    result.py
    langfuse.py
```

This is an illustrative organization, not a mandate to create these implementation files now.
The scenarios entry is the thin Q178 Driver, not a general workflow engine or User Simulator.
No bespoke generic dataset loader framework, grader/metrics/report framework, dashboard, experiment
database, score database, LLM-judge service, or complete release-gate framework is planned.

Thin fixture setup, typed task results, evaluator functions, and later CI wiring are integration
code, not necessarily another platform. Q173/Q177 settle isolation and exact-input reconstruction;
concrete fixture storage/export, platform deployment and field shapes remain deferred.
Under S37.1, write new Eval/tests against accepted contracts rather than requiring migration of old
assets. Old material is optional reference, not acceptance authority. This record update itself
does not delete existing assets or tests.

## 8. Dataset organization

Organize datasets by Skill and development/holdout split:

```text
jobhunter-requirement-parse-dev / jobhunter-requirement-parse-holdout
jobhunter-candidate-fit-dev    / jobhunter-candidate-fit-holdout
jobhunter-resume-fit-dev       / jobhunter-resume-fit-holdout
jobhunter-resume-advisor-dev   / jobhunter-resume-advisor-holdout
```

Names illustrate the separation, not frozen deployment identifiers. Use metadata for positive,
negative, boundary, and regression categories instead of multiplying physical datasets per category.

## 9. Case taxonomy and expected behavior

| Type | Meaning | Example |
| --- | --- | --- |
| positive | A clear supported successful task | Redis requirement with explicit sufficient Redis support |
| negative | A correct rejection, absence, or deliberate non-action | Candidate knows Kafka but assessed Resume does not express it |
| boundary | Cross an authority/version/permission/context/concurrency boundary | Permission revocation, stale Proposal, concurrent version advance |
| regression | Minimal reproducible case for a known repaired failure | Former silent version switch or unsupported write |

Boundary coverage includes authority, exact versions, permissions, Context limits, ambiguous consent,
concurrent updates, long contexts, conflicting facts, and Proposal scope expansion.

A regression case is retained unless its business Contract is explicitly superseded. Personal-data
retention, sanitization, and test-case reproducibility are separate obligations; this is not permission
to retain sensitive production content forever.

The user's Kubernetes example tests no unsupported/unconfirmed factual mutation, not a ban on
discussing session-supplied facts. Q133/Q138 allow such discussion and source-labelled suggestions;
an explicit confirmed Proposal can create USER_CONFIRMED facts under the existing save contract.

## 10. Holdout use and leakage

Holdout is a separate dataset, not a Dev tag used for ordinary prompt tuning. Proposed uses are a
release candidate, major model migration, major prompt/Skill changes, and Context-strategy changes.
If used for targeted tuning, disclose the contamination rather than claiming independent performance.

The existence of a holdout structure does not itself settle a mandatory per-ParserVersion release
certification process. Q175 explicitly retains Q117: real JD tests, manual checks, and traceable
quality reports, without mandatory annotated ParserVersion certification. Exact sizes, trial counts,
thresholds, default enablement, and release use are deferred to later rollout-policy work.

## 11. RequirementParse evaluation

Input: exact JobVersion JD (the proposal's raw_jd is a conceptual source label, not a new frozen field).
Output: validated immutable RequirementSet or an explicit bounded failure.

Evaluate extraction, necessity/importance, ALL_OF/ANY_OF logic, source grounding, duplicates,
hallucinated requirements, and repair behavior.

Candidate measurements:

- Requirement Precision / Recall / F1;
- REQUIRED/PREFERRED classification accuracy, with permitted UNKNOWN handled explicitly;
- ALL_OF/ANY_OF classification accuracy, with UNKNOWN not forced into a guessed label;
- Source Span Validity Rate; Hallucinated Requirement Rate; Duplicate Rate;
- Invalid Output Rate; Repair Rate; Final Failure Rate.

Hard invariant: no invalid RequirementSet is persisted as a usable dependency. Q171 additionally
requires no usable Requirement to stop Fit rather than manufacture a zero-item perfect score.
Structural validators do not establish zero semantic omission; semantic quality needs suitable
review/judgments. Matching predicted and expected units and denominators remain Contract work.

## 12. CandidateJobFit evaluation

Input: exact RequirementSet plus current saved EvidenceBaselineSnapshot and its admitted evidence.
Output: RequirementAssessment results scoped only to those inputs.

Cover MATCHED/PARTIAL/MISSING/UNKNOWN, support grounding, unsupported MATCHED, privacy exclusion,
wrong EvidenceVersion, completeness, and score availability.

Candidate measurements: Assessment Macro-F1; MATCHED Precision/Recall; PARTIAL F1; MISSING and
UNKNOWN Accuracy; Evidence Grounding Precision; Unsupported Match Rate; Wrong-Version Input Rate;
Forbidden Input Rate; Scoreability Accuracy.

Unsupported MATCHED must remain independently visible, not disappear inside a good aggregate.
MISSING remains bounded to saved admitted facts; incomplete inspection is not proof of missing skill.

## 13. ResumeJobFit evaluation

Input: exact RequirementSet plus exact ResumeVersion and necessary grounding-validation metadata.
Do not supplement with Candidate Knowledge, other Resumes, or a newer ResumeVersion.

Canonical boundary: Candidate Knowledge contains Kafka but the assessed Resume does not; expected
Resume assessment is MISSING when its admitted exact contents were fully checked.

Candidate measurements: Assessment Macro-F1; MATCHED Precision; Unsupported Match Rate;
Candidate-to-Resume Leakage Rate; Other Resume Leakage Rate; Wrong ResumeVersion Rate;
UNKNOWN Accuracy; Scoreability Accuracy.

Hard invariant: Candidate-to-Resume supplementation is not allowed. Measure actual admitted input
and support references, not just a judge's impression of the final prose. Candidate and Resume Fit
remain independent; Eval must not assert a required ordering between their numeric scores.

## 14. ResumeAdvisor: multi-step and multi-turn evaluation

### Tool selection

Check required, forbidden, unrelated, and repeated calls. Candidate measures: Required Tool Recall,
Forbidden Tool Rate, Irrelevant Tool Rate, and Tool Calls/Run. Distinguish a model's forbidden request
that Runtime correctly rejects from an actual forbidden Tool execution or data exposure.

### Arguments and resource scope

Check actual Resume/root/version, JobVersion, RequirementSet, and Evidence scope. Candidate measures:
Tool Argument Accuracy, Wrong Object Rate, Wrong Version Rate, and Out-of-scope Call Rate.

### Trajectory constraints

Use MUST / MAY / MUST NOT rather than one exact successful call sequence. A job-targeted scenario
may require reading the actual target Resume and obtaining its RequirementSet, permit either read
order, and forbid bypassing the Proposal or reading an unadmitted Resume. These are scenario-specific:
General Advisor does not require a Job/RequirementSet, and explicit authorized comparison may read
another Resume without changing the formal apply target.

Candidate measures: Required Step Satisfaction, Forbidden Step Rate, Redundant Tool Calls, Tool Loop
Rate. Required state may already be supplied by an admitted pinned input; do not universally demand
a redundant read merely to satisfy a metric.

### Advice quality

Use calibrated semantic judges/human review for relevance, actionability, specificity, and clarity.

### Grounding and formal application

Check unsupported claims/rewrites, wrong target/version, Proposal expansion, and bypassed confirmation.
Proposed hard invariants: Unauthorized Mutation = 0; Human Confirmation Bypass = 0;
Proposal Scope Expansion = 0; Committed Unsupported Factual Claim = 0.

Separate deterministic provenance/authorization checks from semantic support judgments. A valid
EvidenceRef alone is not proof that the referenced text entails every generated claim. Conversely,
explicitly confirmed user facts are not rejected solely because pre-task Evidence lacked them.

A scenario may span several Turns/Runs and an Application confirmation event: Proposal generation
ends a Turn under Q158. Do not keep one AgentRun suspended across simulated human confirmation or
let the Agent-under-test manufacture its own consent. Q173 covers isolation; Q178 fixes the two paths:
N+1 for a localized next-turn failure, full deterministic Scenario for cross-turn effects. The Driver
checks exact-one real Proposal matching before formal confirmation and reads actual mutation/DB
results. It does not use trace arrival as proof that a user action or business commit occurred.

## 15. Context evaluation

For LAZY_TOOL, measure acquisition of necessary data, unnecessary data, and forbidden data:
Relevant Context Recall, Context Precision, Forbidden Context Rate, and Context Token Count.

Exact pinning scenario: first read resolves Resume V5; an external change advances to V6; the task
continues on V5 unless its own authorized Application write explicitly appends new committed inputs.
Hard invariant: no silent latest switch. Readability does not grant eligibility for a stale write.

Permission checks examine actual Tool access/results and model-visible ContextFrames. No forbidden
content may bypass post-Tool admission into a ModelInvocation. Trusted internal storage is not the
same boundary as returning content to the model; design checks must identify which boundary failed.

Q172 regression: protected EAGER_EXACT input permission revoked after freeze terminates the frozen
task; no later Frame/repair reuses it, no silent input shrinking, and no valid new current Analysis.
Earlier immutable Frames are history, not retroactively rewritten or evidence that data was unsent.

Also retain existing compaction checks: exact protected inputs, real source availability, no fabricated
history after purge, limited semantic compaction/rescue, and honest Full Context overflow.

## 16. Tool conformance versus Agent Tool behavior

Tool Runtime tests cover allowlists, schema, object scope, permission, fencing, idempotency, budget,
and result admission deterministically. Agent Eval covers whether the model selected suitable Tools,
used correct arguments, repeated unnecessary actions, or attempted forbidden capabilities.

Do not average the two into a number that can conceal a Runtime enforcement failure.

## 17. Harness conformance remains ordinary automated testing

Q122 recovery, OUTCOME_UNKNOWN, execution_generation fencing, atomic budget reservation, repair
bounds, CAS, runtime-instance orphan recovery, and Tool replay safety primarily use deterministic
tests and controlled fault injection. They do not depend on a live model or an LLM judge.

LLM experiments add model-behavior evidence; they do not replace transaction/concurrency/recovery
tests. Agentic RAG remains post-v1; old retrieval experiments cannot become a required v1 path by
being included in this document.

## 18. Trial strategy and honest reliability

The user's earlier 1/3/5-trial examples are historical proposals, not a v1 requirement. Q175 defers
Trial counts and thresholds to later rollout/evaluation-policy work and excludes that work from this
architecture Grill. Safety-critical subjects include confirmation, authority leakage, permissions,
unsupported mutation, and exact-version boundaries.

Pass@1 remains the primary single-attempt experience measure. Repeated trials measure variability,
not permission to select the best answer and call it typical success. Distinguish an independent
trial from in-Run bounded repair and from explicit Retry after OUTCOME_UNKNOWN. Record failed or
unknown attempts rather than hiding them in a successful replacement trial.

## 19. Four groups of results, not one Agent score

| Group | Proposed measurements |
| --- | --- |
| Hard Gates | Unauthorized mutation, confirmation bypass, forbidden Tool execution/context exposure, Candidate-to-Resume leakage, wrong exact-version write, Proposal expansion, silent replay |
| Quality | Requirement F1, Fit Macro-F1, MATCHED Precision, UNKNOWN Accuracy, grounding precision, Advisor relevance/actionability |
| Reliability | Pass@1, success across trials, failure/repair/Tool-loop rates, trial variance |
| Efficiency | Model/Tool calls, Agent steps, input/output/total tokens, cost, p50/p95 latency, Context size, repair/compaction rates |

Hard violations cannot be compensated by average quality. Report sample counts and evidence scope;
zero observed violations is not a universal proof that violations are impossible.
Missing scores, evaluator failures, unscoreable outputs, and task failures need distinct reporting.
Q168's valid unscored business Analysis must not automatically be an Eval failure or numeric zero.

### Task outcome, per-check judgment, and coverage — Q179

Record what the task actually did separately from how each check evaluated it. Expected business
rejection can be correct behavior; absence of mutation is not automatically task failure. Distinguish
proved violations, INCOMPLETE_EVIDENCE, and evaluator execution errors. An unavailable semantic judge
does not erase a completed deterministic finding, and a successful task does not imply all required
checks completed.

Never silently remove failed/unassessable items from reported coverage or count missing evidence as
a pass. Preserve available conclusions together with sample counts and incomplete evaluation scope.
Concrete result schemas, aggregate denominators and formulas remain later Contract work.

## 20. Hard Gates, quality evidence, and deferred release policy — Q175

Authorization bypass, illegal factual writes, permission exposure, silent replay, and authority
boundary violations are Hard Gates: a failure is unacceptable correctness/safety evidence about the
affected capability. Quality, stability, cost, and latency are Quality Targets; they are not merged
with Hard Gates and do not automatically mean the entire JobHunter product cannot be released.

Keep two independent comparisons:
- Absolute target: did the measured capability meet the intended quality level?
- Relative regression: did it deteriorate against the currently approved comparison baseline?

Langfuse records and compares the evidence. This Eval architecture does not define a release ladder,
default enablement consequence, waiver process, Trial count, numerical threshold, or final repository/
CI pass policy. Those decisions belong to later real rollout-policy work and are not a pending
frontier to keep grilling now. The earlier proposal's universal release sequence is not adopted.

Q117 remains unchanged: RequirementParse uses real JD tests, manual inspection, and traceable quality
reports; no mandatory manually annotated ParserVersion certification Gate is introduced. Runtime
business authorization remains entirely independent of evaluation evidence.

## 21. Production evaluation feedback loop

```text
Production AgentRun
    -> admitted Langfuse observations
    -> failure/interesting case
    -> human review and suitable data handling
    -> regression DatasetItem
    -> offline/controlled experiment on the real task path
    -> fix and regression verification
```

Human review precedes dataset promotion. Raw production traces are not automatically reusable public
fixtures, authoritative labels, or permission to send private data to a judge. Q181 separates
regression-case retention from retention of its original sensitive production payload.

Retain the reviewed behavior and expectations in a separately reconstructible minimal fixture using
appropriately sanitized or synthetic data. Transform text, IDs and references consistently and verify
that the original failure mechanism still reproduces. Masking a name alone does not anonymize free
text. Do not copy an entire Workspace for convenience.

Original Trace/Context/Response content keeps its own retention policy. A lineage reference does not
guarantee permanent source readability. If no admitted reproducible fixture can be retained, disclose
the missing executable coverage rather than claiming the regression is covered. Use lightweight
case curation; no new product approval Aggregate or permanent raw-payload exception is introduced.

## 22. Observability integration

Use LangGraph's Langfuse CallbackHandler and the Langfuse Python SDK for explicit Harness-specific
operations. Langfuse may use OpenTelemetry internally; JobHunter does not add a generic custom
Telemetry Port merely to wrap it.

Two integration paths feed one observability platform:

```text
LangGraph mechanics -> Langfuse CallbackHandler
Harness operations  -> explicit Langfuse SDK observations
```

No claim is made that callbacks automatically cover auxiliary model invocations outside graph nodes,
sanitize all payloads, preserve recovery records, or enforce runtime permissions. Q174 fixes the
boundary: Langfuse is derived observability/Eval infrastructure, not the authority for production
success, Invocation completion, usage settlement, or recovery.

Local Domain/Application state, AgentRun, ModelInvocation, ToolInvocation, and protected Recovery
Payload remain canonical. Platform outage, callback upload failure, or a lost span never rolls back
a successful commit or authorizes replay of a model call, Tool, or mutation.

If a required check lacks its necessary evidence, record INCOMPLETE_EVIDENCE rather than treating
absence of observed violation as proof of no violation. Under Q178, assertions read canonical task/
structured-event/DB evidence independently of observability trace delivery: missing Langfuse spans
alone do not make a check incomplete when its required local evidence is available. Production
execution outcome and evaluation evidence availability remain separate.

## 23. Trace structure and correlation

The proposed view groups Context admission, dependency preparation, graph/node execution,
model/Tool invocations, validation, and persistence around related operations/Runs.

Dependency ensure may precede a Fit AgentRun or start a separate RequirementParse Run; a single
operation may own several Runs. Preserve that truth through parent/link relationships rather than
pretending every dependency is a child model step of one Fit Run.

Illustrative metadata: agent_run_id, Skill/version, model, prompt_version, context_policy_version,
execution_generation, JobVersion, ResumeVersion, and RequirementSet refs. These are trace semantics,
not finalized required field names for every Skill or permission to export sensitive identifiers.

## 24. Sensitive-data policy

Default exported observations favor admitted IDs/refs, hashes, versions, token counts, source
categories, permission decisions, and result status. Full payload capture requires an explicit
tracing policy; it is not authorized merely because Langfuse is self-hosted.

Do not duplicate Profile/Resume/Evidence/interview content across every span. Never capture API keys,
Authorization headers, cookies, tokens, or unrelated personal data. Observability is not a second
Candidate Knowledge authority store and is not a substitute for protected Q125 recovery payload.

Callback and explicit SDK paths apply the same masking/redaction policy before export. Self-hosting
does not authorize unconditional copies of Resume, Evidence, or ContextFrame. Use admitted canonical
AgentRunId, ModelInvocationId, and ToolInvocationId correlation without duplicate observations,
call counts, or cost accounting (Q174).

Raw-evidence access needed by an evaluator is separately admitted. Trace metadata alone may be
insufficient to assess semantic quality; expose that limitation rather than exporting everything.

## 25. Callback and explicit observation ownership

The proposed division is callback observations for graph/nodes/LLM/Tool mechanics, and explicit
observations for Context admission, permission rechecks, budget reservation, dependency ensure,
authorization, Proposal execution, recovery, and persistence. Avoid duplicate observations and
double-counted cost for one real Invocation.

The same Invocation still needs truthful observation when executed without a callback-producing
graph node, including compaction/repair or other auxiliary paths. Q174 requires canonical Run and
Invocation correlation across callback/SDK paths, covering recovery activity and non-graph calls
without duplicate invocation or cost accounting. ModelInvocationRuntime remains the business
execution boundary; observations do not become completion or usage-settlement authority.

## 26. Human calibration

LLM Judge is not ground truth. Maintain a small human calibration set and compare judge output
with human review to improve judge prompt, rubric, model, and thresholds. Primary uses are Advisor
relevance, specificity, actionability, and clarity, plus carefully scoped semantic support review.

Deterministic authorization/safety rules are not delegated to calibration. Exact sample sizes,
agreement measures, judge bias controls, and treatment of judge failure remain later Eval design.

### Independent judge execution — Q176

Business ModelInvocationRuntime serves RequirementParse, Fit, Advisor and other formal task calls
under AgentRun, business budgets, recovery, fencing, and OUTCOME_UNKNOWN semantics. LLM-as-a-Judge
belongs to separate Eval Infrastructure and evaluates already-produced outputs/trajectories. It
cannot participate in the original business decision, mutate Domain state, or alter the original
AgentRun's execution outcome.

Use distinct invocation categories, budget/cost accounting, model configuration, Prompt/Rubric
versions, and observability labels. Do not add judge tokens/cost to Agent performance measurements
or a user's foreground operation; report judge cost separately. Judge failure is not task failure.
A judge result is evidence only. Authorization, permission, exact-version use, actual mutations,
and observable authority leakage continue to prefer deterministic checks.

Langfuse-managed judge execution is not claimed to inherit JobHunter's atomic reservations,
fencing, or recovery protocol automatically. This is an Eval-only execution boundary, not a bypass
for a production Skill call; concrete evaluator controls remain later contracts.

## 27. NiceEval and deferred alternatives

NiceEval is not a core v1 dependency. The user's rationale is overlap with the selected Langfuse/task
layer and added integration for the current Python/LangGraph system; language/integration details
are user-supplied rationale, not independently established compatibility guarantees in this record.

Q178 adopts scenario-oriented evaluation, send -> Turn -> structured events, exact-one HITL matching,
session isolation and trace-independent assertions as design inspirations. The actual thin Scenario
Driver is JobHunter-owned and preserves its Application confirmation semantics. This is a user-chosen
design direction, not verification of any particular external library API/version.

No User Simulator is implemented or designed for v1 regression. Future generative exploration or a
black-box HTTP adapter is a separate capability; do not mix its results into fixed-input regression
comparisons or add future interview/general-assistant Skills to current scope.

## 28. Responsibility matrix

| Capability | JobHunter | Langfuse |
| --- | --- | --- |
| Business invariants/runtime authorization | Enforce in production | Never owns |
| Eval task | Real Application/Harness adapter | Invokes/tracks experiment |
| Domain-aware checks | Resolve canonical refs and actual persisted state | Receives safe results |
| Dataset/version | Thin consumption and any approved fixture integration | Primary management |
| Experiment | Thin task/configuration entry | Runs/records/compares |
| Scenario orchestration | Authored Turns, logical events, exact-one Proposal confirmation and local assertions | Dataset definitions and platform Session/Trace grouping, not business orchestration |
| Code evaluator | Domain-aware functions; lightweight SDK functions when suitable | Generic evaluator facilities |
| LLM judge | Independent Eval classification/accounting, no business authority | Generic judge execution and results (Q176) |
| Scores/aggregation/dashboard | Produces necessary measurements | Primary platform |
| Production trace | Safe instrumentation and exact correlation | Stores/displays admitted observations |
| Regression cases | Produces reviewed cases | Dataset management |
| CI regression/release | Final rollout/enablement policy explicitly deferred by Q175 | Supplies comparable experiment evidence |

Execution location is not the same as platform ownership. A small evaluator function in a Python
experiment runner may still use Langfuse's experiment/scoring facilities without rebuilding a grader
framework. Platform-specific deployment verification is recorded separately below.

## 29. Clean-slate implementation boundary

S37.1 replaces incremental migration with new documentation and code. Build the section 7 integration
against final contracts using the new real Application/Harness path. Old fixtures, rubrics, runners
and acceptance evidence need no preserved or mapped destination in the new system; they may inform
new cases only after review against current semantics.

Production invariants still require deterministic tests. Generic checks belong in platform/SDK
facilities where sufficient; Domain-aware checks remain thin local code. Rewriting tests does not
waive safety evidence, TDD or the prohibition on a separate test-only Agent.

The rebuild direction is accepted, but this record-editing task does not delete code/data, deploy
services or start implementation. Detailed schemas, workload thresholds, SDK versions, deployment
resources and formal-document updates remain follow-up work.

## 30. Governing principles and current Grill frontier

1. Langfuse provides the generic platform; JobHunter supplies business semantics and real execution.
2. Eval observes actual outcomes, trajectories, inputs, permissions, and persisted changes, not only prose.
3. Production safety remains enforced locally; deterministic checks verify it independently of judges.
4. Skill-specific semantics govern expected behavior; evaluation cannot resurrect superseded architecture.
5. Exact source/configuration lineage and honest unavailable/failed outcomes are prerequisites for comparison.
6. This remains architecture-level Grill; conceptual properties are not exhaustive Contract schemas.

### Accepted Q173-Q177 integration decisions

- Q173: isolated Fixture-backed real Application/Harness execution, independent Trials, controlled
  external adapters and explicit Scenario actions; no live Workspace/platform mutation.
- Q174: Langfuse is derived; local execution/recovery/usage is authoritative. Missing necessary
  evidence is INCOMPLETE_EVIDENCE. Common pre-export redaction and canonical correlation cover
  callback/SDK/auxiliary paths without double-counting.
- Q175: separate Hard Gates, Quality Targets, absolute target attainment and relative regression.
  Release policies, default enablement, numeric thresholds and Trial counts are excluded from this
  architecture Grill. Q117 remains.
- Q176: judges are independent Eval Infrastructure, with separate invocation/budget/model/rubric/
  observability identity; results never alter business decisions or original task outcome.
- Q177: Dataset version plus immutable reconstructible fixtures, Scenario events/expectations and
  exact execution/evaluator configuration define reproducibility. Missing/mismatched inputs fail
  explicitly; latest-state substitution is forbidden.

### Accepted Q178-Q182 evaluation decisions

- Q178: fixed user inputs, N+1 for localized conversational failures, thin deterministic Scenario
  Driver for full workflows; exact-one matching and real Application confirmation, no generative
  User Simulator or trace-dependent assertions.
- Q179: canonical task outcomes and per-check conclusions/completeness stay separate; incomplete
  evidence, evaluator errors and proved violations are visible, never silently dropped.
- Q180: expected outputs constrain meaning/grounding/behavior while allowing legitimate semantic
  alternatives; deterministic refs, permissions and authorization remain strict.
- Q181: reviewed regression fixtures can outlive source payload through verified minimal sanitized/
  synthetic reconstruction; original sensitive payload retention remains independent.
- Q182: new evaluation can assess the same captured Trial without rerunning the Agent if admitted
  actual evidence remains; new evaluator results preserve original history and identify their versions.

### Accepted Q183 — N+1 restores a coherent boundary, not messages alone

An N+1 Fixture freezes the first N Turns together with the exact business/session/runtime state
necessary to execute the next Turn. Include the relevant immutable versions, session/source refs,
Proposal state and required artifacts as one coherent boundary. This does not require a full dump
of unrelated Workspace data.

Restore that boundary through controlled Fixture hydration in an isolated environment, then execute
only N+1 through the real Application/Harness path. Do not replay old model calls, Tools or mutations
to reconstruct history. Missing required references, versions or state make the case explicitly
non-reproducible; no latest-state fallback or checkpoint guesswork is permitted.

This experiment demonstrates next-turn behavior from a declared starting state. It does not prove
that the current Agent would generate the preceding N Turns or create that starting state correctly.
Use a full Scenario when the creation and progression of that state are themselves under test.

### Accepted Q184 — Task-scoped evaluator evidence

Each evaluator receives the evidence necessary for its own judgment, not an automatic copy of the
entire Fixture, Workspace or raw trace. Semantic judges receive relevant actual assessed inputs,
output, expected constraints and rubric under their own data-admission boundary.

- Resume Fit judging uses the exact assessed Resume and Requirements; Candidate Knowledge cannot
  supplement facts absent from that Resume.
- Candidate Fit judging uses the admitted Evidence scope of the assessed task, not excluded facts.
- Advisor judging may use relevant user Session statements while preserving their distinction from
  saved authoritative Evidence.

Deterministic authorization, mutation and cross-Resume checks may inspect the necessary admitted
test state separately. Broader audit access does not authorize exporting that state to a judge or
feeding it back to the Agent. Necessary unavailable evidence yields incomplete evaluation, not an
expanded permission scope. Semantic support and observable access/authorization remain different checks.

### Accepted Q185 — Separate task input, evaluation reference, and Scenario control

Maintain three distinct input roles:

| Role | Contents | Consumer |
| --- | --- | --- |
| Task input | Current/past user inputs and admitted business data | Agent-under-test through real Context construction |
| Evaluation reference | Expected labels, valid-answer constraints, judging evidence and rubric | Evaluators with their own admitted scope |
| Scenario control | Future user Turns, logical event triggers and confirmation/refusal scripts | Thin deterministic Scenario Driver |

Never serialize the whole DatasetItem into Agent Context. Expected answers, future user inputs,
judge instructions and previous Trial scores cannot be read through the Agent's prompt or Tools.
Only an authored Turn that has actually been reached becomes current task input. The Driver applies
declared events through Application interfaces rather than instructing the Agent how to pass.

Judge instructions/rubric are trusted evaluation control. Candidate answers, Tool text and other
task-produced material are untrusted evidence; instructions embedded there cannot change scoring
rules. This separation is an Eval data/access contract, not a new general evaluation framework.

### Accepted Q186 — Skill-focused and composed-workflow experiment scope

Both scopes call the real production entry points, but make different claims:

- Skill-focused experiments supply legal frozen prerequisites to measure the target Skill. A Fit
  Fixture may contain an exact compatible RequirementSet; the real Ensure path reuses it. Parser
  quality is assessed separately, not inferred from a cached prerequisite.
- Workflow Scenarios start from their declared dependency state and exercise real dependency
  preparation, orchestration, multiple Runs, confirmation and final business effects as applicable.

Record the experiment scope, dependency availability and actual executed stages. A parser failure
is a workflow/dependency failure; a Fit that never ran has no semantic judgment to label incorrect.
Do not hide the dependency failure or count the unexecuted Fit as successful.

Attribute costs and outcomes to the measured path. Partial-path cost is not end-to-end cost, and
target Skill quality is not complete workflow quality. No test-only Agent, skipped Ensure, hidden
validation bypass or runtime safety relaxation is introduced.

### Accepted Q187 — Frozen Memory and controlled background activity

Ordinary comparable Advisor Trials use isolated frozen initial Memory entries, Recall configuration
and permissions. Disable unscripted automatic learning/background changes through supported
production configuration so they cannot silently change Context or contaminate another Trial.
This is experiment configuration, not a change to production defaults or the Agent implementation.

Memory-specific Scenarios explicitly enable and drive the real learning workflow and declared events.
Keep their background outcomes and costs separate from foreground behavior/cost, and prevent learned
state from leaking across Trials. Disabling learning does not justify a claim that MemoryExtraction
was tested. Admission, permissions and other production guards remain active in either configuration.

### Architecture frontier and later scope

The recorded architecture frontier is settled through Q187; this review identifies no additional
in-scope architecture decision requiring another five-question round. S38.1 closes this phase with
an artifact handoff; formal documentation and later Contract work follow the user-approved sequence,
not immediate implementation.

Exact fields, event schemas, Fixture representation, evaluator interfaces, metric formulae and
infrastructure configuration remain later Contract/implementation work. Numeric thresholds, sample
sizes, Trial counts, default enablement and release/rollout policy remain deferred under Q175.
These Eval decisions do not change existing Harness module responsibilities or runtime behavior.

## 31. Re-evaluation of captured Trial results — Q182

Changing an Evaluator/Rubric/Judge configuration or retrying a failed judge need not rerun the Agent.
A new evaluation attaches to the same exact captured Trial outcome when its required admitted
evidence is still available; it records its own evaluator versions and retains original scores.

Re-evaluation does not invoke original Agent/Tools or replay mutation. Judge costs remain separate.
Domain-aware rechecks need actual retained post-state or mutation evidence, not a newly rebuilt
initial Fixture presented as what the original execution produced. Missing/purged evidence produces
an explicit unavailable/incomplete evaluation, never a silent fresh task to fill the gap.

An intentionally new Agent execution is a new Trial with newly frozen input and independent cost.
Output-preserving re-evaluation and behavioral re-execution are different experiment operations.

## Appendix A. Official platform research — facts, not additional product decisions

Checked 2026-09-18 against official documentation. Recheck the selected deployed Langfuse/SDK version
before implementation; these notes do not claim that JobHunter has deployed or verified the feature.

| Verified platform fact | Implication for this design |
| --- | --- |
| Dataset item changes have timestamp-addressed versions; dataset schema changes are not included in that versioning | Dataset version alone is not a complete schema/fixture/configuration manifest (Q177) |
| SDK experiments accept task/evaluator functions executing in the experiment process | Thin local evaluator functions remain compatible with Langfuse-heavy ownership |
| Self-hosted Code Evaluators need a configured dispatcher; the documented local trusted-code runner supports JS/TS, while Python execution is available through the documented Lambda setup | Do not assume a local Python evaluator worker is automatically supplied by self-hosting |
| CI integration still needs experiment-script regression criteria and a reviewed comparison baseline | Langfuse supplies evidence, not the repository's release decision |
| Observation-level judges do not automatically collect child/sibling observations | Explicitly provide admitted trajectory evidence or inspect canonical runtime records locally |
| LangChain/LangGraph callbacks capture detailed input/output; masking can be applied before export | Metadata-first JobHunter policy needs verified callback as well as explicit-SDK configuration |
| SDK instrumentation supports observations outside graph callbacks | One real Invocation should be correlated once without leaving auxiliary paths invisible |
| Self-hosted LLM evaluation uses configured model connections/gateways | A platform judge does not automatically pass through JobHunter ModelInvocationRuntime (Q176) |

Primary sources:

- [Langfuse datasets and versioning](https://langfuse.com/docs/evaluation/experiments/datasets).
- [SDK experiments and evaluator functions](https://langfuse.com/docs/evaluation/experiments/experiments-via-sdk).
- [Self-hosted Code Evaluator configuration](https://langfuse.com/self-hosting/configuration/code-evaluators).
- [Experiments in CI/CD](https://langfuse.com/docs/evaluation/experiments/experiments-ci-cd).
- [LLM-as-a-Judge and observation scope](https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge).
- [LangChain/LangGraph callback integration](https://langfuse.com/integrations/frameworks/langchain).
- [Pre-export masking](https://langfuse.com/docs/observability/features/masking).
- [SDK instrumentation](https://langfuse.com/docs/observability/sdk/instrumentation).
- [Self-hosted LLM API/gateway connections](https://langfuse.com/self-hosting/deployment/infrastructure/llm-api).

The implications are architectural inferences from these capabilities, not promises that optional
workers, automatic trajectory aggregation, privacy defaults, or release gates are already configured.
