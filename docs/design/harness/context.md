# Harness Context Engineering — Detailed Architectural Design Record

## Status, scope, and authority

- Primary accepted design: Q132, substantially refined by Q138-Q139 and Q140-Q172. Supporting boundaries: Q19, Q47, Q52, Q72, Q79-Q83,
  Q94, Q111-Q115, Q120-Q128, and Q130.
- Last updated: 2026-09-18.
- This is a complete architecture-stage module record, not a new final Source of Truth.
  Formal architecture/contracts/acceptance remain the eventual normative destinations.
- Conceptual objects and example attributes express semantics; this Grill does not finalize
  schemas, field lists, token limits, thresholds, or detailed transition tables.
- Context Compaction replaces the earlier Session Compaction/SessionSummary proposal.
  It is owned here, not by Memory Runtime, and does not mutate Session history.

Related records: [Memory](memory.md), [Recovery](recovery.md), [Budget](budget.md),
[Storage](storage.md), and [Decision Register](../grill-me-design-tree.md).

## 1. Context sources, control, and runtime responsibilities

**Context Source is not default Prompt content.** Business Authority remains the sole formal fact
source, but availability never means every Agent sees it at startup. Q139 replaces that eager-default
interpretation throughout this module.

| Source class | Role | Entry into a Frame |
| --- | --- | --- |
| Control / Instruction | Harness instructions, active Skill contract, Tool/Memory allowlists, output/interaction/repair/context policy, runtime/approval/safety rules | Protected control needed by the current invocation |
| Session | Current User Turn, admitted recent Turns, ContextCheckpointSummary | Bounded conversation continuity; not career-fact authority |
| Long-term Memory | Collaboration preference, feedback, working style, reusable learning | Dynamic, relevant subset only when Recall and Skill admission allow |
| Business capabilities | Typed resume.read, evidence.read/search, job.read / job.requirements.read, preference.read, application.read | Allowed Tool definitions, not the underlying business contents |
| Business Authority | Profile, Preferences, Evidence, Resume, Job/RequirementSet, Application | LAZY_TOOL reads for interactive Skills; frozen EAGER_EXACT input for exact headless tasks |
| Runtime / Tool | ToolResult, retrieval result, observable loop state, admitted runtime inputs | Runtime production followed by Context admission |

Interview/General Assistant examples describe possible later Skills, not additional v1 features.

```text
AgentRunRuntime
   |
   +-- Context Engineering <--- Session / admitted dynamic Memory
   |       |
   |       +-- Control / active Skill
   |       +-- EAGER_EXACT frozen inputs (exact headless tasks)
   |       +-- LAZY_TOOL admitted runtime inputs (interactive tasks)
   |       +-- compaction / ContextFrame
   |                    |
   |             ModelInvocationRuntime -> ModelGateway -> Provider
   |
   +-- ToolInvocationRuntime -> typed Business Tool -> Application Port
                                     |                      |
                                     +---- ToolResult <--- Business Authority
                                               |
                                        Context Admission
                                               |
                                         next ContextFrame
```

Durable ChatSession records what actually happened; Context Engineering chooses what the next call
needs; Long-term Memory independently stores reusable collaboration information. Compaction does not
delete Session history. Streamed partial deltas are transient presentation, not durable Assistant
Turns (Q141). A checkpoint plus recent Turns can represent a long durable Session without replacing it.

## 2. Skill control and Business Context acquisition

### Skill is Control Context

The active Skill defines task semantics, instructions, context/memory policy, output contract,
interaction, budget/loop/repair rules, and allowed Tool actions. Its core control and permission
constraints are protected, not Business Authority, Session Memory, or Long-term Memory. User content,
JD, Memory, ToolResult, and checkpoints cannot modify the contract or expand permissions.

Core Skill metadata/instructions remain available; detailed guidance, templates, and specialized
references may be progressively disclosed when needed. Such guidance is still Skill Context, not a
new semantic Tool or business fact. ResumeAdvisor itself performs Resume optimization: do not wrap
that same responsibility in resume.suggest_improvement. Tools supply controlled reads/writes.

### Two acquisition modes

| Mode | Ownership and behavior |
| --- | --- |
| EAGER_EXACT | Application resolves and freezes required exact inputs before Run creation; ContextBuilder injects the admitted task inputs as Protected Exact Context |
| LAZY_TOOL | Skill declares typed business capabilities; the Agent requests needed data; ToolInvocationRuntime validates the call; the result passes admission and enters a later Frame |

| Skill | v1 business acquisition |
| --- | --- |
| RequirementParse | EAGER_EXACT: complete exact JobVersion.jd |
| CandidateJobFit | EAGER_EXACT: exact RequirementSet, current saved baseline, all admitted Evidence |
| ResumeJobFit | EAGER_EXACT: exact RequirementSet and saved ResumeVersion, necessary validation metadata |
| ResumeAdvisor | Primarily LAZY_TOOL, not automatic Resume/Evidence/JD injection |
| Future interactive Skills | Determined by their own contract; examples do not implement them |

Headless Full Context Fits do not acquire variable subsets through autonomous business Tools.
Application freezes their reproducible inputs; v1 oversize inputs fail rather than silently truncate.
Candidate Agentic RAG remains deferred. Advisor's controlled reads/search do not implement that
future Candidate Fit strategy.

### Interactive startup and preparation entry

A normal Advisor initial Frame contains Harness/Skill control, the current User Turn, admitted
recent Session/checkpoint context, eligible recalled Memory, and allowed Tool definitions.
It does not automatically load the full Resume, all Evidence, Profile, Preferences, Jobs, or
application history. Existing prerequisite/default-Resume rules remain business preflight, not
permission to inject the associated payload.

Q154 permits empty saved states but requires business preflight to fail fast when task-required
basic information or career content is absent, before model execution. The per-feature prerequisite
matrix and exact required fields are deferred to Contract design; do not assume every Skill needs
Profile/contact data or introduce a new completeness confirmation.

Example: "help optimize my Backend Resume" leads to an allowed resume.read; the returned exact
R2/V5 is admitted and recorded in the next Frame. A Tool never secretly scans ChatSession to decide
which Resume was meant. Skill interprets intent and passes explicit validated references.

Preparation entry creates an ordinary new ChatSession with structured Preparation/Job/Resume
references and an explicit optimization intent. References can identify the intended scope without
including JD, RequirementSet, Resume text, or Evidence. Read needed requirements through
job.requirements.read, Resume through resume.read, and career data through admitted Evidence actions.
No separate Job-targeted Agent/Session type is introduced, and references alone do not prove the
model has seen their content. Existing exact selections and no-silent-switch rules still apply;
acquisition changes do not authorize implicit selection changes.

### Component responsibilities

- ContextStrategyPolicy governs Full Context versus future Retrieval and budget policy.
- BusinessContextAcquisition governs EAGER_EXACT versus LAZY_TOOL; it is not the same axis as Retrieval.
- ContextAdmission validates Control, Session, Memory, Business inputs, and Tool results.
- ContextBuilder assembles admitted control/continuity/dynamic memory plus the appropriate business
  inputs into each Frame; it does not indiscriminately fetch all available authority.
- ContextCompaction reduces eligible history/runtime context, not required exact headless inputs.
- ContextPackage captures initial allowed scope; ContextFrame records one actual model input.

### Pure requirement reads and Application dependency preparation (Q144)

job.requirements.read reads only an already compatible RequirementSet for a specified exact JobVersion.
Missing input returns DEPENDENCY_MISSING / REQUIREMENT_SET_REQUIRED, not a hidden parsing call.
Application executes EnsureRequirementSet, reusing or single-flight-producing the Set under Q142.
An independent RequirementParse AgentRun uses ModelInvocationRuntime, actual owner budget, bounded
repair, recovery, and audit. Its successful exact Set becomes an admitted runtime input in the
Advisor's next Frame. The Advisor waits; parsing is not folded into its semantic task.

Job-targeted optimization does not require prior manual DeepFit. Parsing failure is dependency
failure, not permission for Advisor to reinterpret JD into another formal requirements authority.
See [Tool Actions](tool.md) for action naming and purity.

### Page boundaries after Q146

My Resumes alone permits manual Resume CRUD; page-local ResumeDraft must be handled through
Save / Discard / Cancel before leaving. Saved versions, not editor dirty state, reach other flows.
Advisor has no ResumeDraft/working-draft store and applies confirmed suggestions directly to formal
authority. Preparation displays the final rendering of the selected saved Resume and permits
selection changes only; it does not edit Resume body text. Its optimization button opens ordinary
Advisor chat with references. Q162 Apply reentry resumes an existing unfinished Job/channel Preparation
by default, preserving selections/Greeting and revalidating eligibility without silently upgrading
exact inputs. Explicit new preparation/reapplication has its own chain.
Adopting a newly produced formal version back into Preparation is a
separate explicit Q91 CAS update; no successful Advisor write silently overwrites Preparation.

Q153 restricts My Resumes removal to the selected Resume's experience membership: create a new
ResumeVersion without deleting Evidence or changing baseline/other Resumes. Global Evidence deletion
is available only in Candidate Knowledge management (求职资料库), not through this page or an Advisor
delete action. Selection removal is not an implicit request to remove saved shared facts.

Q157 leaves Greeting editing inside Preparation: a product-fixed generic default, optionally edited
under Preparation CAS. No Job/Resume/Knowledge/Memory customization, model call, independent
Skill/root/version history, or template library. Actual confirmed text is frozen into materials and
execution inputs; later edits require material reconfirmation.

### Whole-experience inclusion and disposable editor state (Q163/Q166)

A Resume selects whole EvidenceItems and uses the selected current version's complete experience
body. Resumes can differ in included experiences/order/layout, not per-Resume alternate fact text
or independent bullet-selection mappings. This does not remove finer EvidenceRef grounding pointers
or expand Profile fields beyond existing display/privacy choices.

ResumeDraft is transient My Resumes UI state. Normal navigation still uses Save / Discard / Cancel;
a sudden crash may lose unsaved edits. v1 has no draft recovery checkpoint/autosave guarantee and
does not promote unsaved text to authority, Memory, or Harness recovery input.

## 3. ContextPackage, runtime inputs, and ContextFrame

ContextPackage is the immutable Run-start scope, policy, frozen-input and capability manifest.
It is not a bundle of every payload a model might eventually need.

An Advisor Package can contain Skill identity, permitted Session scope, initial Preparation/Job/
Resume references, Tool and Memory capability policy, and no initial business body payload.
An EAGER_EXACT Package instead binds Application-resolved exact business inputs before execution.
These are conceptual semantics, not a finalized field inventory.

```text
initial immutable ContextPackage
        |
Frame 1: control + admitted Session + dynamically admitted Memory + Tool definitions
        |
allowed ToolCall -> validated ToolResult -> admitted exact runtime input
        |
Frame 2: actual admitted business content added
        |
ModelInvocation -> discussion / Suggestion / confirmed formal result
```

Each ModelInvocation binds its own immutable ContextFrame: exact messages, control, relevant Session/
checkpoint, dynamically recalled Memory, admitted Tool content, Tool schemas, and accounting.
Allowed scope is not actual model visibility. Analysis completeness is checked against the actual
assessment-producing Frame.

Reads and writes append admitted runtime inputs, never rewrite the initial Package or historical
Frames. Querying another Resume is not permission to switch the editing baseline. Actual outputs
bind the exact ResumeVersion and references used, not merely a starting default.

### Authorized post-write continuation

Q134 still permits the same Advisor Run to continue after an explicit authorized Save. Application
returns committed exact references; readmit them for privacy, permission, grounding, and scope, then
build a new Frame. Old suggestions and Frames remain unchanged. Do not guess version IDs, reset
budget, silently adopt unrelated concurrent changes, or upgrade an independent Fit Run's frozen inputs.

Q156 separates committed mutation from subsequent narration. Persisted Application mutation result
remains the business outcome even if a later model call/stream fails. UI shows saved changes and
unfinished reply separately. Recovery/retry idempotently recognizes the same confirmed Proposal,
without duplicate Evidence/Resume versions. New changes require a newly confirmed Proposal;
remote model retries still obey Q122.

Q158 narrows the actual ChangeProposal workflow: its generating Run is already ended before
user confirmation. Generic post-write admitted-input mechanics do not keep that Run alive or
revive it. Application confirms/commits independently; any subsequent narration uses new bounded
execution and the actual result, not a second interpretation of the authorized patch.

### Session-sourced facts and controlled actions (Q138)

Saved facts use canonical EvidenceRef. A newly stated unsaved fact may immediately support Advisor
discussion and Suggestion using a lightweight SessionContextRef / UserTurnRef:
exact authorized Session/Turn and the actual cited text. It is verifiable conversational provenance,
not Evidence authority or proof that the claim has been formally saved.

Skill Context Engineering admits relevant Session content explicitly. Business Tools do not scan
the chat history themselves. If an action needs this source, pass a controlled source reference.
ToolInvocationRuntime validates Session membership, scope, and that cited text actually exists;
model-generated references do not validate themselves. Suggestion/source boundary validation must
likewise not accept fabricated user statements as support.

Q146 replaces Advisor working drafts with discussion, Suggestions, and explicit formal application.
Q148-Q149 make formal apply a target-specific ChangeProposal. Use the Resume explicitly specified
in the current instruction, otherwise Workspace default; do not infer or maintain a "suggestion source
Resume". Read the actual target's exact ResumeVersion before producing its own before/after patch.
Display that target/version/default indication, concrete changes, Candidate Knowledge impact, and
affected current Resumes. One confirmation authorizes that exact Proposal, not arbitrary model parameters.
A changed target invalidates the old Proposal and requires a fresh read/preview; changed requested
content likewise requires a replacement preview. Revision conflict regenerates the preview, never
silently retargets or overwrites. No unrequested experiences are copied from another Resume.

ChangeProposal is a non-editable operation preview, not ResumeDraft or exportable/application material.
Actual consumed inputs retain exact lineage without inventing implicit suggestion-source state.
Confirmed changes commit through UpdateCandidateKnowledge; there is no second draft Save or
confirmation for every affected Resume. See [Tool Actions](tool.md).

Unsaved user statements remain Session Context, not Memory, formal Fit inputs, or business authority.
Do not add an optimization Tool duplicating ResumeAdvisor. ResumeDraft exists only in the My Resumes
editing page; Preparation cannot edit Resume text and only consumes formal versions/materials.

Historical payload expiry follows [Storage](storage.md): metadata/hash is not an invented substitute
for the exact historical Frame.

### Lazy acquisition with exact-version consistency (Q143)

An unresolved permitted root reference may resolve on its first controlled read, which records the
actual exact version. Later reads of the same analysis/optimization object within that Run use the
bound version rather than silently tracking latest. Already explicit Chat/Preparation exact inputs
are not downgraded to an unresolved default.

An authorized same-task Application write may append its actual new committed version under Q134.
Unrelated concurrent page writes do not silently update the Run; official application rechecks
revisions and compatibility. Readability of an old version does not prove eligibility for new business.
Q149's formal apply uses only the current instruction's explicit target or Workspace default.
Proposal creation validates that target's actual exact version; an old discussion read is not proof
that the patch applies to the current target. Stale inputs require a new target-specific preview, not
a silent version upgrade. Read pinning and immutable historical lineage remain; no extra
"suggestion source Resume" state is inferred or displayed.

Q151 deletion uses explicit EvidenceItem inclusion in current ResumeVersions, not model-inferred
Claim/sentence dependencies. Current facts and directly affected current Resumes advance atomically;
historical ContextFrames and their source assets are not rewritten. Old readable references alone
cannot authorize new formal Fit/render/application after deletion.

### Foreground Session serialization (Q155)

One ChatSession permits at most one active foreground Turn. New user input waits or follows an
explicit stop; two user Turns cannot concurrently advance its Context/business state. This is a
backend invariant, not only UI disabling. Different Sessions may run in parallel, and independent
dependency/auxiliary/background AgentRuns are not a second foreground Turn.

Run/Turn lifecycle, cancellation/fencing, per-Frame inputs and budgets remain distinct. This does
not create a permanently waiting Agent process.

### Human confirmation versus machine dependency waiting (Q158-Q159)

Generating/showing ChangeProposal ends its foreground Turn/Run. Pending Proposal is persisted
Application interaction state, not a suspended Run or occupied Session slot. Explicit confirmation
executes the exact validated Application command without model reinterpretation of consent/patch.
Conflict requires new preview. Any subsequent conversational response uses new bounded execution
and actual mutation result. Pending proposals do not prevent further discussion or abandonment.

Requirement parsing is a machine dependency. The Advisor foreground Turn stays active in dependency-wait
while Application runs/awaits independent RequirementParse. Release model/Provider invocation capacity;
overall deadline and cancellation remain active. No model read polling or indefinite wait. Success
admits the exact Set into the next Frame; timeout/failure/cancel ends waiting under Q142 owner/waiter
rules, never inline JD parsing or silent producer takeover.

### Session deletion revokes pending action eligibility (Q167)

Deleting ChatSession invalidates its still-unconfirmed ChangeProposals, e.g.
INVALIDATED_BY_SESSION_DELETE, and cancels active foreground work under current fencing rules.
Old Proposal IDs or restored pages cannot confirm them again. Application checks Session/Proposal
state at one atomic boundary when deletion competes with confirmation: only one competing outcome
wins, never success acknowledgements for both incompatible operations.

Already committed mutation results and formal Evidence/Resume/application assets remain unchanged.
Session deletion cannot roll them back or reconstruct an actionable Proposal from old Context.
A further desired modification needs a new Proposal in a valid context.

## 4. Stage 0 — Classify by task obligation and acquisition mode

| Protected Context | Compactable Context |
| --- | --- |
| Harness and core Skill instructions/output contract | Older Session messages |
| Current User Turn/instruction | Observable AgentLoop intermediate history |
| Runtime/Tool permission and required approval state | Old LAZY_TOOL ToolResult projections |
| EAGER_EXACT RequirementSet / Resume / admitted Evidence required by formal analysis | Search/retrieval history and transient task continuity |
| Other task-required exact inputs explicitly declared by contract | Prior derived checkpoint and redundant completed steps |

Authority and prompt residency are different concerns. An interactive resume.read result remains
authoritative at its source, but an old inline ToolResult may be externalized and later reread at
the exact version. This does not turn a summary into a substitute business fact.

Headless EAGER_EXACT inputs cannot be dropped or replaced by lossy summaries. ContextBuilder
reinjects required protected payloads from their frozen exact sources, subject to privacy/stale/
permission checks; it does not automatically inject all Business Authority into every Skill Frame.
A current root lookup never silently substitutes for a pinned exact version.

Long-term Memory is a separate dynamic source, not Session history or semantic checkpoint input.
Exclude Memory-only blocks from compaction source material and reapply Recall admission per Frame.
The current user Turn remains protected even when it describes unsaved conversational facts.

## 5. Multi-stage Compaction pipeline

```text
Raw admitted Context sources
              |
              v
Stage 0: protected/compactable classification
              |
              v
Stage 1: ToolResult externalization / budgeting      0 LLM
              |
              v
Stage 2: history window compaction                   0 LLM
              |
              v
Stage 3: structured / micro compaction               0 LLM
              |
              v
Context target-budget check
      | fits                      | still too large
      v                           v
build Frame              Stage 4: bounded semantic checkpoint
                                  |
                                  v
                          validate and durably publish
                                  |
                                  v
                   checkpoint + recent context + protected inputs
                                  |
                                  v
                              build Frame

Provider explicitly returns CONTEXT_TOO_LARGE
              |
              v
more aggressive reactive compaction of eligible transient content
              |
              v
one admitted retry; another size failure => fail closed
```

Cheap deterministic reductions precede expensive semantic compression. Internal model work and
reactive retries are real Invocations; neither bypasses budget or recovery.

## 6. Stage 1 — ToolResult externalization and budgeting

A large Tool result should not remain inline forever merely because the Tool completed successfully.

Preserve the complete result in durable Tool-result storage subject to admission and retention.
Use a bounded model-visible projection containing the conceptual equivalents of:

- source ToolInvocation reference;
- result metadata;
- bounded preview;
- relevant object references;
- durable source reference.

Example:

```text
search returned 184 records
relevant object references: E3, E7, E19
bounded preview: ...
source reference: ToolInvocation TI17
```

The numbers are illustrative. The pattern is:

```text
durable exact source + bounded/lossy model-visible projection
```

It is not deletion of the source result. If detail is needed later, a controlled read may retrieve
it, but only if the current Skill/mode already permits that action. Externalization does not grant
Tools to a Full-Context Fit or widen its admitted Evidence set.

Generic retrieval examples illustrate the mechanism and do not bring Candidate Agentic RAG into v1.
Required exact analysis Evidence cannot be replaced by a search preview.

For LAZY_TOOL Advisor context, an old resume.read(R2/V7) result can leave the active Frame while
its exact reference remains. If needed again, resume.read(R2/V7) is a new controlled ToolInvocation,
not a replayed TI17 or an implicit read of the latest R2. By contrast, required EAGER_EXACT Fit input
must remain complete; acquisition mode and Skill contract determine which guarantee applies.

## 7. Stage 2 — History window compaction

Deterministic history selection may retain:

- current user Turn;
- recent relevant messages;
- unresolved ToolCall/ToolResult correspondence;
- recent key decisions;
- current structured task state.

Completed, redundant, or recoverable old intermediate messages may leave active model Context.
They remain in their appropriate durable source stores.

Window size, character/token bounds, and message counts are not frozen. Tool-call/result structure
must remain valid; trimming cannot present an unresolved action as completed or lose a pending task
merely because its source message is older.

Session persistence records the conversation; window selection records which parts are useful to
the next invocation. These are not the same storage operation.

## 8. Stage 3 — Structured / micro compaction

Represent known runtime state directly instead of replaying a long sequence of natural-language
Tool observations.

For example:

```text
query A -> E1, E4, E7
query B -> E3
query C -> no result
```

can become a small retrieval-state projection. Task-continuity state may express the selected
Resume/Job, adopted Suggestions, unresolved items, and next step through exact references.

These are conceptual state examples, not a new Domain Aggregate or final schema.
Deterministic projection must preserve distinctions such as requested versus completed, suggested
versus adopted, and observed versus authorized.

Micro-compaction performs no model invocation and creates no new career facts.

## 9. Trigger and target watermark are separate

A policy must distinguish:

- **trigger threshold:** when compaction should begin;
- **target watermark:** how much headroom should remain after compaction.

Q132 uses roughly 80% and 50-60% only as possible evaluation examples. No numerical values are
accepted defaults.

The difference provides hysteresis: avoid repeatedly compacting a Context that remains just below
the trigger and immediately exceeds it again on the next step.

Policy considers the actual serialized model input, system/Tool schema overhead, output reserve,
and safety margin. A remaining spending balance does not guarantee Context capacity.

## 10. Stage 4 — Bounded semantic Context checkpoint

Only if deterministic stages remain insufficient may a bounded LLM compaction generate a
ContextCheckpointSummary. Its purpose is an execution handoff, not a generic account of the topic.

Conceptual content:

- current goal;
- completed work;
- key decisions;
- current user constraints;
- unresolved questions;
- active artifact/object references;
- important Tool/source references;
- pending actions;
- next steps.

Illustrative checkpoint:

```text
Goal: optimize the JobHunter section of Resume R2/V4
Decisions:
  retain three bullets
  avoid the word "led"
  Redis suggestion accepted
  Kafka suggestion rejected
References:
  Resume R2/V4
  Job J17/V2
  ToolInvocation TI14
Next: discuss the second project
```

This is a derived navigation/continuity artifact. It cannot establish that a business write or
external application occurred without the corresponding authoritative source.

Do not use SessionSummary as this object's name. ContextCheckpoint or ContextCheckpointSummary
distinguishes it from the durable Session and from MemorySummary over collaboration memories.

### Memory is excluded from checkpoint source material (Q139)

Compaction summarizes admitted Session history and observable AgentLoop/Tool/runtime history, not
Long-term Memory blocks. A preference available only from Memory must not be copied into the
checkpoint. Recalled Memory is dynamically injected anew when Recall and Skill admission permit.

Legacy checkpoints containing directly copied Memory must exclude separable blocks; if separation
is unreliable, rebuild continuity from permitted durable Session/runtime sources. v1 does not attempt
second-order removal of Memory's indirect influence on genuine assistant messages. Actual dialogue
is not retrospectively erased and no Provider unlearning guarantee is implied.

## 11. Semantic compaction stays inside the current AgentRun

Unlike MemoryExtraction, normal runtime compaction does not create a separate AgentRun:

```text
ResumeAdvisor AgentRun
  main ModelInvocation
  ToolInvocation
  main ModelInvocation
  Harness auxiliary compaction ModelInvocation
  next main ModelInvocation
```

The compaction exists only to let that Run continue the same user task. It shares:

- that Run's ExecutionBudget;
- execution_generation and ownership;
- audit lineage;
- deadline and local execution limits;
- dispatch durability and recovery semantics.

It is a Harness auxiliary Invocation, not a new user task and not background Memory maintenance.
This refines S22.1: one semantic task per Run can include task-supporting runtime maintenance.
It does not permit packaging unrelated Jobs or independent Fits into one Run.

Future idle-time precompaction could have a separate maintenance Run, but is not the default accepted
v1 path. MemoryExtraction remains independent and uses BackgroundMemoryBudget.

## 12. Budget admission for compaction

Stage 4 is a real Provider invocation, never a free helper:

```text
current AgentRun / ExecutionBudget
        |
ModelInvocationRuntime
        |
local allowance + Run total limits + atomic reservation
        |
durable dispatch through ModelGateway
        |
durable response / usage settlement
```

Q135 fixes the scope of allowances across the entire AgentRun:

- Skill validation repair for RequirementParse/Candidate Fit/Resume Fit: at most once.
- LLM semantic Context Compaction: at most once per Run, not per loop step.
- Reactive rescue retry after explicit Provider Context-size rejection: at most once per Run.

These are ceilings, not guaranteed extra calls. Every primary, repair, compaction, and reactive call
also consumes the Run's total ModelInvocation count, input/output tokens, cost/reservation, deadline,
and applicable step budget. Dispatch requires both an unused local allowance and sufficient total
budget. An allowance at 0/1 does not override exhausted Run capacity; a new loop step resets neither.

Deterministic externalization, trimming, and micro-compaction do not consume a model-call allowance,
but remain bounded runtime work. All actual Provider requests, including auxiliary maintenance,
pass through ModelInvocationRuntime; ModelGateway only adapts Provider/model requests and responses.

If budget cannot admit semantic compaction, reuse the deterministic result only if it safely fits
the task; otherwise stop explicitly, for example CONTEXT_BUDGET_EXCEEDED. Protected exact Fit input
overflow fails under Q123; never spend compaction allowance summarizing facts to claim Full Context.

See [Budget](budget.md) and [Recovery](recovery.md) for reservation, ownership, dispatch, and unknown
outcomes. Kind labels such as PRIMARY, VALIDATION_REPAIR, CONTEXT_COMPACTION, and REACTIVE_RETRY are
conceptual audit categories, not an exhaustive finalized field schema.

## 13. Recovery and checkpoint publication

Compaction follows the same Invocation durability boundary:

```text
prepared
   |
dispatch intent durable
   |
Provider
   |
complete response durable
   |
validate candidate checkpoint
   |
fenced durable checkpoint publication
```

- Dispatch intent without durable response is OUTCOME_UNKNOWN for the model call, not a reason to
  repeat compaction silently.
- A durable response permits recovery of local validation/publication without another model call.
- An invalidated execution generation cannot publish its late checkpoint.
- A checkpoint is not business authority merely because its model response was stored durably.

Never delete the old recoverable Context before producing its replacement:

```text
retain recoverable sources
   -> generate candidate
   -> validate
   -> durably publish
   -> use in a later new ContextFrame
```

Required validation includes structural completeness, protected references, current goal, valid
source references, and recoverable key runtime state. The complete checkpoint schema is deferred.

Failed generation/validation does not publish an untrusted checkpoint. Original durable Session
and retained Context/Tool sources remain available under their own storage policies.

## 14. Durable source references

A checkpoint source_ref preserves provenance, not a promise of permanent payload availability.
For example, a reference to Turn T33, ToolInvocation TI17, or Evidence E7/V4 explains the source
used for the checkpoint; the paraphrase is not itself authoritative Evidence.

Q136 distinguishes:

- **Active Recovery Dependency:** exact Context, ToolResult, and durable response needed by a
  running/recoverable Run until its safe recovery boundary ends. Retention must not purge them.
- **Historical Source Reference:** a reference left after that boundary ends. Its payload may expire
  under independent retention, retaining metadata/hash/lineage and explicit availability such as
  PAYLOAD_PURGED or SOURCE_UNAVAILABLE. A surviving old checkpoint does not pin everything forever.

Historical continuation/reopening first checks availability and current permission. If an exact
Business Authority version remains available, an allowed new ToolInvocation may read it again.
Record a new read; never fabricate the old ToolResult, substitute a newer version, or claim the
historical Frame was reconstructed exactly.

If the source is unavailable, report SOURCE_UNAVAILABLE. Stop or request supplied content when the
missing source is necessary for reliable work. Do not guess the source from the checkpoint or
automatically revisit BOSS, replay external requests, or repeat side effects to restore it.
See [Storage](storage.md) for lifecycle ownership and [Recovery](recovery.md) for replay limits.

## 15. Reactive compaction rescue

Provider-side Context rejection can occur despite local preflight. A typed, explicit
CONTEXT_TOO_LARGE / prompt-too-long response permits the bounded rescue branch.

Rescue more aggressively reduces compactable content while retaining:

- current user instruction;
- protected exact business inputs;
- current structured task state;
- necessary recent messages;
- valid ToolCall/ToolResult relationships.

Q135 permits at most one reactive rescue retry across the entire AgentRun. Another Context-size
rejection fails closed; later loop steps do not renew the allowance.
Every retry is admitted, budgeted, durable, and audited.

This is not permission to retry a timeout, disconnected stream, or unknown outcome under a
“maybe too large” guess. Q122's unknown-outcome rule still applies. The rescue must pass both its
Run-wide local allowance and the Run's total budget through ModelInvocationRuntime. It does not
grant a second semantic checkpoint if the separate once-per-Run compaction allowance is exhausted.

No rescue silently switches Provider/model or summarizes protected business inputs.

## 16. Protected Exact Inputs invariant

A checkpoint cannot replace current user instructions, Harness/Skill control, Tool permissions,
runtime constraints, approval state, or the EAGER_EXACT business inputs required by formal analysis.
ContextBuilder restores those specific exact sources for each applicable invocation.

This does not require every interactive Frame to contain a full Resume, all Evidence, or every
referenced Job. LAZY_TOOL business results can be externalized; exact content is read again through
controlled actions when required. A reference/preview proves neither complete inspection nor current
authority. The model's narration of approval or "saved" never replaces an Application commit record.

Compactable context consists of older dialogue, observable intermediate execution, old Tool/runtime
history, and transient continuity. It does not include Long-term Memory blocks as summary input.
No private Provider reasoning trace is required as a new authority source.

## 17. Full Context Fit remains fail-closed on oversized exact inputs

If RequirementSet plus all required admitted Candidate Evidence already exceeds capacity, the
following is prohibited:

```text
summarize Evidence with an LLM
   -> evaluate the summary
   -> label the result FULL_CONTEXT Candidate Fit
```

Stop under Q123 instead. The same rule protects the exact Resume used by Resume Fit.

Future Retrieval Mode may define a different admitted Context strategy and completeness semantics;
it is not achieved by lossy compression of formal analysis inputs. Compaction and Retrieval solve
different problems and have different implications for MISSING/UNKNOWN.

### Requirement usability, score availability, and runtime revocation (Q168/Q171/Q172)

An empty/non-usable RequirementSet cannot start Candidate/Resume Fit. Schema-shaped parser output
alone is not a usable assessment target. Application fails fast with explicit input/dependency
failure; downstream Skills may not invent requirements or treat zero items as perfect match.
Existing parsing/repair limits remain; no unbounded retry is added.

For a nonempty usable target, valid RequirementAssessments may still lack enough information for
a defensible aggregate. Q168 permits a durable analysis with assessments/reasons/references/lineage
but no comparable total score/ranking. ScorePolicy determines availability; unavailable is not zero.
Weights/thresholds and representation remain later Contract design.

Q172 distinguishes admission exclusions before Run freeze from permission revocation during a
protected EAGER_EXACT task. Initial exclusions retain existing UNKNOWN/completeness semantics.
Revoking required input permission mid-run ends the affected frozen task fail-closed: do not silently
remove those inputs and continue the same analysis, create later Frames/repair/Tools using revoked
content, or publish a new valid current Analysis. A requested new analysis freezes new admitted
inputs in a new task. Prior transmission cannot be undone; necessary usage/recovery/audit remains.

## 18. Dynamic Memory, independent controls, and checkpoint exclusion

Q139 separates Auto Learning, Recall / Injection, and explicit user management:

- Auto Learning controls background extraction and automatic publication.
- Recall controls whether existing Memory may enter each new Frame.
- Users may view/add/edit/delete/clear allowed collaboration Memory through deterministic management,
  without an extraction model call. Business facts still belong to their Domain owners.

Turning Auto Learning off does not turn Recall off. Turning Recall off excludes Long-term Memory
from the next Frame, including derived Memory summaries, but does not delete entries or Session
history. Check current Recall every Frame; immutable initial Package capability is not permanent
admission. Automatic publication rechecks Auto Learning independently.

ContextCheckpointSummary is Session/runtime continuity, not MemorySummary. Do not directly copy
Memory into it. Legacy direct mixtures are filtered or rebuilt from permitted durable sources.
v1 explicitly defers second-order contamination through actual assistant responses.

A one-off Session instruction does not become permanent Memory merely by appearing in a checkpoint.
Automatic durable learning still uses MemoryExtraction plus MemoryWriteAdmissionPolicy. Explicit
user Memory CRUD is the separate authorized path. Neither can rewrite business authority or expand
Tool permissions. No default historical backfill is introduced on reenablement.

## 19. v1 scope and later design

Accepted now:

- separate durable Session, Memory, and Context responsibilities;
- protected versus compactable classification and deterministic stages before semantic compaction;
- one semantic checkpoint invocation and one reactive rescue retry at most across a whole Run;
- unique ModelInvocationRuntime admission, shared total budget, recovery, fencing, and audit;
- validated durable publication before checkpoint use;
- no lossy authority substitution, hidden Retrieval, or retry of unknown outcomes;
- Session-local discussion distinct from explicit business Save;
- admitted immutable post-write runtime inputs without rewriting initial or historical Context;
- active-recovery retention versus expiring historical references;
- interactive LAZY_TOOL and headless EAGER_EXACT business acquisition;
- independent Auto Learning, Recall, and explicit Memory management;
- per-Frame Recall checks, checkpoint exclusion of direct Memory, and verified Session source refs;
- stream deltas as transient presentation rather than formal Assistant Turns.

Further architectural questions must refine only genuine gaps, not reset accepted safety or scope.
Later field design covers object schemas, policy identities, event/status vocabularies, trigger/target
values, window sizes, pricing/model choice, and exact publication/authorization mechanics.

## 20. Verification implications and formal writeback

Later acceptance scenarios should verify:

- compaction never deletes Session history;
- externalization retains a recoverable source rather than just a preview;
- Tool permission does not grow when a preview needs rehydration;
- protected Evidence/Resume content is never replaced by a summary for formal Fit;
- checkpoint failure leaves the former recoverable state intact;
- semantic compaction uses the current Run's budget and fencing;
- unknown compaction calls are not silently replayed;
- an explicit Provider size rejection gets no unbounded retry loop;
- historical Frames remain immutable and accurately reflect actual visible content;
- a temporary checkpoint instruction is not written into Long-term Memory automatically.

These are verification implications, not claims of implemented tests. Formalize ownership in
architecture/contracts, user-visible failure behavior in spec, and tests in acceptance/development;
keep implementation status in progress.

Q134-Q137 additionally require post-write Frames to reference committed versions, no allowance reset
on later loop steps, no auxiliary call after total-budget exhaustion, no replay of a purged historical
Tool response, and no new Long-term Memory injection when Recall is disabled.

Q138-Q142 additionally require an interactive initial Frame not to eagerly load business bodies;
every lazy result to pass Tool and Context admission; Session citations to match real authorized
user text; Tools not to scan chats; EAGER_EXACT Fit inputs to stay complete; directly recalled Memory
not to enter semantic checkpoint sources; learning-off/recall-on and learning-on/recall-off to work
independently; and no incomplete stream to become a formal Suggestion.

Related Tool naming, action purity, typed source validation, and dependency signaling are defined
in [Tool Actions](tool.md). Architectural objects/properties are collected for later design in
[Contract Design Inventory](../contract/contract-design-inventory.md); neither document finalizes
field schemas or reports implementation.
