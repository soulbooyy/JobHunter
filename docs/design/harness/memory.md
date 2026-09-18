# Harness Memory — Detailed Architectural Design Record

## Status, scope, and authority

- Architectural decisions: Q127 refined by Q128-Q149, with Q155-Q156 and Q169-Q170 runtime integration; supporting boundaries include Q19, Q47,
  Q52, Q80, Q83, Q94, Q108, Q113, Q120, Q125, and Q126.
- Q132 removes Compaction from this module and supersedes SessionSummary as a compaction object.
- Last updated: 2026-09-18.
- This file preserves the full module design, not only a Decision Register summary.
- It is a design-stage record, not a seventh class of authoritative project document.
  Formal authority remains in spec, architecture, acceptance, development, contracts, and progress.
- Conceptual objects, categories, and attribute examples below describe responsibilities.
  They are not finalized database tables, API schemas, exhaustive fields, or transition enums.
- This record covers Memory v1. It does not introduce General Assistant or interview capabilities
  into the current product merely because their possible Memory access is illustrated.
- The current filename is `memory.md`, corrected by the user; all design links use this name.

The short decision entry lives in the [Decision Register](../grill-me-design-tree.md).
Related runtime designs: [Recovery](recovery.md), [Budget](budget.md),
[Context Engineering](context.md), and [Storage](storage.md).

## 1. Design commitment

JobHunter distinguishes four data/source layers:

1. Business Authority holds formal personal and job-seeking information.
2. Session Memory preserves the complete durable conversation.
3. Harness Long-term Memory preserves admitted cross-session collaboration preferences, feedback,
   working style, and reusable assistant learning.
4. Memory Retrieval Infrastructure supplies rebuildable summaries, indexes, and lookup helpers.

Context Engineering is a separate Harness subsystem. Its Context Compaction can reduce model-visible
history, but does not mutate Session history, write Long-term Memory, or own these source stores.

Long-term Memory is not another Candidate Knowledge database. The main conversational AgentRun
performs the user task; a separate headless MemoryExtraction AgentRun proposes candidates from eligible
durable user-facing Turns. MemoryWriteAdmissionPolicy chooses long-term acceptance, Session-only use,
business routing, or rejection. Q139 also permits explicit user Memory management through
deterministic validation, without an extraction Run; Auto Learning and Recall are separate controls.

**Model proposes; Policy decides.** A candidate is not business authority, Tool authorization, or
external execution approval. User-confirmed business changes can instead use Q128's controlled
Application write path, which is distinct from Memory extraction.

## 2. Corrected four-layer model and independent Context Engineering

| Layer | Owned concern | Representative objects | Authority and lifetime |
| --- | --- | --- | --- |
| L0 Business Authority | Formal user/business information | CandidateProfile, PreferenceSet, Evidence, Resume, Application, interview records | Sole authority for its business concern |
| L1 Session Memory | What happened in this conversation | ChatSession, Turn, Tool-history refs, AgentRun refs | Durable Session source; not career-fact authority |
| L2 Harness Long-term Memory | Accepted cross-session collaboration information | Preference, feedback, working-style, reusable-learning entries | Limited non-business collaboration semantics |
| L3 Memory Retrieval Infrastructure | Memory lookup/presentation | MemorySummary, search/index, routing metadata | Derived and rebuildable |

Independent Context Engineering contains ContextStrategyPolicy, ContextAdmission, ContextBuilder,
ContextCompaction, and ContextFrame. Its full design is in [context.md](context.md), not in a Memory
layer.

```text
Control / active Skill -----------------+
durable Session projection -------------+
dynamically recalled Memory ------------+--> Context Engineering --> ContextFrame
business data via admitted LAZY_TOOL ----+
headless frozen EAGER_EXACT inputs ------+
runtime / ToolResult sources -----------+
```

Q132 supersedes Q127's original placement of Session Compaction at L2 and Context Engineering at
L5. ContextCheckpointSummary is an execution-continuity artifact owned by Context Engineering;
MemorySummary is a lightweight derived view of accepted Long-term Memory. They are different objects.

Interview records retain the existing Application/Event boundary; no Interview Aggregate is added.
The Workspace remains single-user without a new Candidate root or tenant system.

Q139 makes Business Authority an available source, not a default injected payload. Interactive
Skills normally acquire it through typed Tools; exact headless Skills use Application-frozen
EAGER_EXACT input. Core Skill instructions are protected Control Context, not a Memory layer.

## 3. Three distinct conflict and authority rules

Q128 replaces a single universal priority chain with three separate rules:

| Concern | Governing source |
| --- | --- |
| Business facts | Saved Business Authority |
| Execution permissions | Skill allowlist, runtime policy, required approval |
| Interaction style | Current explicit user instruction > admitted Long-term Memory > derived conversation/checkpoint summary |

A current request for detail overrides an old preference for concise answers for this task.
A temporary override does not change Long-term Memory. Only an explicit durable instruction such as
“from now on” becomes a new preference candidate for MemoryWriteAdmissionPolicy.

Neither Memory nor a request to avoid repetitive confirmation may waive required fact-conflict
handling, MaterialApproval, ExecutionApproval, or Tool permissions.

### Business ownership remains narrow

- Career experience belongs to Evidence.
- Identity/contact belongs to CandidateProfile.
- Search intent belongs to PreferenceSet.
- Saved Resume content/default selection belongs to Resume/configuration.
- Actual applications belong to Application records/events.
- Conversation continuity belongs to durable ChatSession/Turn plus Context-derived representations.
- Cross-chat collaboration preferences belong to admitted Long-term Memory only.

### Confirmed business updates from chat

Q133 distinguishes conversational use from formal persistence. A current user statement may immediately
inform discussion, questions, and proposed wording, even if the saved Evidence does not contain it.
For example, "the project also used Kafka; how should I describe it?" does not require interruption
or a Save prompt. It stays Session-level information, not saved Evidence or Long-term Memory.

Only explicit intent to change formal facts enters the write path. For Advisor application to a
Resume, Q146 requires a preview of the concrete change, target, and shared-fact/current-Resume
impact, then one user confirmation. Use the specified Resume or Workspace default if unspecified;
do not silently use conversation provenance as apply authorization. After confirmation, the
authorized typed Tool directly delegates to UpdateCandidateKnowledge with no separate draft Save.
Resolve remaining target/content conflicts and validate revisions. Model parameters do not prove
consent; ordinary discussion never triggers compulsory fact-save prompts.

That shared write path creates the new EvidenceItemVersion, advances current_version_id, snapshots
the baseline, and atomically synchronizes affected current ResumeVersions under Q118. The model's
arguments are not proof of confirmation or permission.

This is an explicit Q128 refinement of earlier draft-only chat fact routing. It does not grant Fit
or MemoryExtraction business write permission, allow generic database writes, or give Harness fact
authority. Q134 governs continuation after the Application returns committed exact references; see
[Context Engineering](context.md). An unrelated concurrent edit is not an authorized scope upgrade.

CandidateJobFit still reads saved current Candidate Knowledge only; ResumeJobFit reads its exact
saved ResumeVersion. Interactive discussion may use unsaved Session assertions, but cannot relabel
them as authoritative Evidence or promote them into formal Fit scores/application materials. A
one-off request to consider Hong Kong or answer at length need not modify PreferenceSet or Memory.

### Information that must not become Long-term Memory

| Example | Correct destination |
| --- | --- |
| “I used Kafka in a project.” | Evidence through the confirmed controlled business-write path |
| “My target city is Shenzhen.” | PreferenceSet workflow |
| “Make Backend the default Resume.” | Resume configuration |
| “I applied to Tencent.” | Application reporting workflow |
| “My phone number is …” | CandidateProfile |

The table identifies where a fact belongs if the user elects to persist it, not a requirement to
interrupt every conversation. ROUTE_TO_BUSINESS_AUTHORITY identifies the proper workflow; it does
not itself authorize a write.
MemoryExtraction cannot silently confirm facts on the user's behalf.

### Valid collaboration examples

- Show a Resume diff before Save.
- Prefer Java/Spring analogies.
- Prefer concise answers without repetitive confirmation.
- Use a particular interview-review structure if that future Skill is implemented.

Generated assistant text/checkpoints are not independent evidence of a user's preference. A derived
checkpoint never automatically becomes Long-term Memory.

Q138, narrowed by Q146, makes user-provided Session facts directly usable in Advisor Suggestions with
validated SessionContextRef / UserTurnRef, distinct from canonical EvidenceRef. The reference must
identify real text in an authorized Session/Turn; Tools receive explicit references rather than
scanning chat history. ResumeAdvisor owns optimization semantics; resume.suggest_improvement is
not a second implementation of the Skill. Q148-Q149 require a target-specific ChangeProposal:
read the actual target's exact version, show its patch/shared-fact impact, and obtain one confirmation.
Do not infer a suggestion-source Resume or treat a Memory preference as authorization. Changing the
target/content or encountering revision conflict requires a replacement preview. The controlled
Application path applies confirmed changes; unsaved discussion is neither Memory nor formal Fit input.
No Advisor ResumeDraft survives chat deletion: drafts exist only in My Resumes. Formal results retain
their independent business lifecycle after chat deletion.

## 4. Long-term Memory types

v1 recognizes four conceptual categories:

| Type | Purpose | Example |
| --- | --- | --- |
| PREFERENCE | Stable communication preference | Chinese answers; conclusion before explanation |
| FEEDBACK | User feedback about assistant behavior | Explain why a Resume change is proposed |
| WORKING_STYLE | Stable collaboration pattern | Discuss before finalizing; show a diff |
| REUSABLE_AGENT_LEARNING | Reusable non-career interaction learning | Structured diffs have worked better for this user |

There is no USER_FACT category. Category PREFERENCE is about assistant collaboration, not the
job-search Preferences owned by PreferenceSet.

REUSABLE_AGENT_LEARNING remains a category, but Q129 requires explicit traceable user expression
or correction for v1 automatic long-term admission. Pure behavioral inference and assistant guesses
cannot become durable preferences merely because the category sounds reusable. Uncertain candidates
remain Session-local or are rejected; no confidence formula or threshold is frozen.

## 5. Session persistence is not Context Compaction

ChatSession/Turn persist the complete durable conversation, necessary Tool-history references, and
Run references. Each user Turn still uses finite execution rather than a permanently waiting Agent.

Session Runtime records what happened. Context Engineering chooses what the next Invocation needs
and may create a ContextCheckpointSummary. A checkpoint plus a short recent window does not delete
the original Session and is not another Memory layer.

Session Compaction / SessionSummary are superseded names for this concern. See [context.md](context.md)
for deterministic stages, bounded semantic compaction, same-Run auxiliary invocation, and reactive
rescue. That mechanism is distinct from MemoryExtraction.

Deleting conversation content remains separate from cleaning derived Context or forgetting Memory.
It cannot invalidate independently saved Resume, Suggestion, HumanChoice, Evidence, or application
results.

Q141 excludes uncompleted streaming deltas from durable conversation requirements. They may appear
through StreamBridge/SSE but need not survive refresh or crash. Only complete durable responses,
after required parse/validation, form formal Assistant Turns or adoptable Suggestions. An incomplete
stream is not a durable completed user-facing Turn and does not trigger MemoryExtraction.

Q155 permits one active foreground Turn per ChatSession. New input waits or follows explicit stop;
different Sessions and independent MemoryExtraction/dependency/auxiliary Runs may execute under
their own admission/budgets. Background extraction is not another conversational Turn.

Q156 separates persisted business mutation from later reply failure. Saved facts stay saved, and
retries cannot duplicate versions. A committed Tool mutation alone does not convert an unfinished
assistant stream into a completed extraction source or allow career facts into Long-term Memory.

Q158 ends the Turn that generates/displays Proposal; the pending user choice is Application state,
not a waiting Agent. Confirmation does not require Memory or a model to reinterpret the exact patch.
Optional subsequent narration is new bounded execution. Q159's machine-dependency wait is different:
its foreground Turn remains active with deadline/cancel, while independent Runs retain their own scope.
Neither a pending Proposal nor a dependency event is by itself a completed extraction source.

Q167 Session deletion invalidates unconfirmed originating ChangeProposals and cancels active foreground
work, not already committed facts/results. Old IDs/checkpoints cannot resurrect action eligibility.
This does not conflate Session deletion with forgetting existing Long-term Memory under Q131.
Q166's unsaved editor state is disposable UI, not Session/Long-term Memory or a recovery source.

## 6. Durable pending work and independent background extraction

```text
Auto Learning enabled
             |
completed durable user-facing Turn
             |
durably mark extraction pending
             |
coalesce adjacent pending Turn ranges
             |
MemoryExtractionTriggerPolicy
(debounce / idle / accumulated range)
             |
background budget + Provider/capacity admission
             |
independent MemoryExtraction AgentRun
             |
MemoryCandidate[]
             |
MemoryWriteAdmissionPolicy
    +-- ACCEPT_LONG_TERM_MEMORY
    +-- KEEP_SESSION_ONLY
    +-- ROUTE_TO_BUSINESS_AUTHORITY
    +-- REJECT
```

The system does not depend on a nonexistent reliable “Session ended” event, and does not invoke a
model unconditionally after every Turn. Only eligible new user-facing Turns create automatic work.
MemoryExtraction output, candidates, and other background Runs cannot recursively trigger extraction.

Pending work is durable, not a timer's private state. A range of completed Turns must remain
discoverable after a crash. Processed-through/pending-through examples describe successful progress,
not a mandatory single prefix cursor that blocks every later Turn behind one failed extraction.
Timers are scheduling optimizations, not pending-work authority.

Q169 separates failed/OUTCOME_UNKNOWN batches from later eligible source ranges. Old failures neither
block newer Turns nor get silently included in a newly coalesced batch. Mark success only for work
actually processed successfully; retain failure/uncertainty distinctly. Only explicit Retry reprocesses
an old failed/unknown range, through a new Run and existing budget/recovery/admission rules.
Undispatched work waiting for capacity/budget is still pending, not a failed batch. Detailed
cursor/range/status representation remains Contract work; no complex new queue is required.

MemoryExtraction has its own Skill Contract, Context, Invocations, recovery, and budget. It does not
block a completed user response. Failure, insufficient budget, or OUTCOME_UNKNOWN never rewrites
the foreground task's success and never authorizes infinite background retry. Durable pending work
does not override Q122's ban on silently replaying an unknown remote call.

### Deleted extraction sources (Q170)

A deleted source Session cannot start new automatic extraction or publish new Memory from its
pending/in-flight ranges. Recheck source availability/validity before dispatch and publication.
Cancel in-flight extraction where possible; late candidates from deleted source cannot be published.
A timer, old payload, or restored page cannot revive deleted-source learning.

Previously accepted Memory remains governed separately from Session deletion/forgetting under Q131.
Already transmitted remote content cannot be retracted. Preserve truthful usage/unknown outcome and
necessary recovery/audit according to policy; deletion is not a refund or a zero-usage assertion.

### Source minimization

Prefer relevant user messages, necessary assistant response context, and explicit correction/
confirmation evidence. Do not send full Tool results, Evidence, webpages, or the complete Agent
transcript by default. The extractor sees only admitted source content needed to support candidates.

### Independent Auto Learning, Recall, and user management (Q139)

Auto Learning authorizes durable pending extraction work, background dispatch, and automatic Memory
publication. Recheck it before dispatch/publication; disabling it stops new automatic learning and
prevents a late candidate from publishing under stale permission. Existing entries may still be
recalled if Recall remains enabled.

Recall / Injection independently controls reads and model-visible Memory blocks. Recheck it for
every Frame and Memory lookup, including summaries and continuing Runs. Recall off takes effect
from the next Frame; initial ContextPackage admission does not override the current control.
It does not delete stored entries or automatically disable learning.

View/Add/Edit/Delete/Clear All is a third, explicitly user-controlled management path. It does not
require MemoryExtraction or either automatic-learning/recall switch to be enabled. Deterministic
validation enforces allowed collaboration categories and the prohibition on a second career-fact
store. Explicit user action supplies management authority, not unrestricted business mutation.

Reenabling automatic learning does not default to scanning pre-enablement or disabled-period chats.
Neither switch removes Session continuity, disables normal Business Authority reads, or retracts
content already transmitted. Durable pending ranges/timers cannot bypass current learning policy.

Trigger cadence, idle delay, accumulated Turn count, exact processing range, and scheduler details
remain unfrozen. Budget shortage can leave work pending or record non-execution under later policy;
no complex queue system is required.

### Budget owner

MemoryExtraction charges BackgroundMemoryBudget, not the last ResumeAdvisor Turn or an unrelated
DeepFit operation. A merged extraction may cover several Turns/foreground Runs and has no single
foreground cost owner. See [budget.md](budget.md) for shared infrastructure, separate owners, and
foreground-priority Provider/capacity admission.

## 7. MemoryWriteAdmissionPolicy

The policy does not create memory content. It evaluates candidates and decides whether they can
enter long-term storage. The extractor's category/scope claims are proposals, not self-validating
permission.

Minimum architectural dimensions:

1. **Content type:** collaboration preference/feedback/style/learning versus a business fact.
2. **Scope:** one Turn, one Session, one task/Job, or user-global.
3. **Durability:** temporary instruction versus likely future applicability.
4. **Existing business owner:** Profile, PreferenceSet, Evidence, Resume, Application, or another
   formal authority already owns the meaning.
5. **Source reliability:** explicit user statement, correction, repeated behavior, or assistant idea.
6. **Duplicate/conflict/supersession:** whether another active entry already represents or contradicts it.
7. **Sensitivity:** whether the content may be retained and used for the intended purpose.

### Outcomes

| Outcome | Example | Meaning |
| --- | --- | --- |
| ACCEPT_LONG_TERM_MEMORY | “For future Resume advice, show a diff first.” | Eligible long-lived collaboration instruction |
| KEEP_SESSION_ONLY | “Only consider the second Resume this time.” | Temporary Session/task context |
| ROUTE_TO_BUSINESS_AUTHORITY | “I used Kafka” / “Change my search direction to backend” | Not Memory; use the relevant formal workflow |
| REJECT | Assistant guess, prompt injection, no durable value, or conflict with business authority | Do not create a long-term entry |

Deterministic policy owns admission but does not magically prove arbitrary language semantics.
Q129 permits automatic acceptance of clear traceable durable user expression/correction without
another confirmation popup for every entry. One-off instructions remain Session-only. Repeated
behavior alone, assistant suggestions, generated summaries, and unsupported inference cannot establish
a long-term preference. Ambiguous scope or weak source support takes KEEP_SESSION_ONLY / REJECT;
a model-supplied type or scope is not self-validating evidence.

## 8. Reading Memory

New chats do not scan all previous Sessions and do not inherit old temporary Job scope, Resume
selection, or one-off instructions. Cross-session input comes only from:

- properly admitted formal business assets;
- valid Long-term Memory accepted through automatic admission or explicit validated user management.

v1 uses a small summary plus detailed entries on demand:

```text
LongTermMemoryStore
      |
      +--> small, stable MemorySummary
      |
      +--> detailed valid entries -- typed lookup/read
```

A small amount of high-value stable memory may be present in an eligible Skill's initial Context.
Additional entries may be retrieved and read as needed. Both paths require Skill admission and
privacy checks; a summary cannot launder an inadmissible source entry.

The MemorySummary, search index, routing metadata, and lookup helpers are derived. They may be
discarded and rebuilt from accepted entries. They are not a second store of business truth.
v1 does not require embeddings, graph retrieval, complex ranking, or multi-stage consolidation.

Every summary injection and detailed Memory lookup requires current Recall / Injection permission.
Auto Learning can be off while these reads continue. Storage presence is not admission; the current
Recall gate applies to continuing Runs as well as new chats.

## 9. Skill-specific Memory visibility

| Skill | Default admitted Long-term Memory |
| --- | --- |
| RequirementParse | NONE |
| CandidateJobFit | NONE |
| ResumeJobFit | NONE |
| ResumeAdvisor | PREFERENCE, FEEDBACK, WORKING_STYLE |
| Mock Interview / Interview Review (future) | PREFERENCE, FEEDBACK, WORKING_STYLE |
| General Assistant (future) | PREFERENCE, FEEDBACK, WORKING_STYLE, REUSABLE_AGENT_LEARNING |

Fit and parsing tasks must not acquire collaboration memories through either full Context,
summaries, or Tools. Their requirements and scoring inputs remain independent of conversational
preferences.

The future examples do not add those Skills to current product scope. REUSABLE_AGENT_LEARNING
storage does not implicitly grant ResumeAdvisor access to that category. MemoryExtraction has its
own source/admission policy; it does not inherit unrestricted access from another Skill.

## 10. ContextPackage and ContextFrame integration

Context Engineering combines:

- System/Skill instructions;
- admitted Session history/Context checkpoints;
- EAGER_EXACT business inputs for headless exact tasks, or admitted LAZY_TOOL reads for interactive tasks;
- admitted Long-term Memory;
- admitted Tool results.

ContextPackage records the task-level admitted scope/initial inputs and allowed capabilities.
ContextFrame records what one concrete ModelInvocation actually received, including memory blocks,
messages, readmitted Tool results, compaction/redaction, and token accounting.

This extends, rather than replaces, Q83/Q94:

- Initial ContextPackage is immutable.
- A later permitted lookup may add an admitted immutable runtime input.
- It produces a new ContextFrame; it does not edit the initial package or earlier Frames.
- Memory lookup is not a business scope change or authority write.
- Every invocation remains auditable according to actual visibility, not just allowed visibility.

No Memory layer may turn limited Context into a claim that a Fit model saw information it was not
allowed to receive.

After an explicitly authorized business write, Q134 permits the same Advisor Run to continue with
the actual committed references returned by Application. Append them as new admitted runtime inputs,
revalidate grounding/scope, and build a new Frame; do not rewrite the initial Package or old outputs.
Independent Fit Runs retain their own frozen inputs and stale checks.

Recheck Recall for every new Frame, independently of Auto Learning. Memory is dynamically injected,
not copied into ContextCheckpointSummary. Filter legacy direct mixtures or rebuild from permitted
Session/runtime sources; v1 does not remove indirect influence on real assistant messages.
Turning Recall off preserves Session history and immutable historical Frames.

Q158 narrows the actual ChangeProposal workflow: its generating Run is already ended before
user confirmation. Generic post-write admitted-input mechanics do not keep that Run alive or
revive it. Application confirms/commits independently; any subsequent narration uses new bounded
execution and the actual result, not a second interpretation of the authorized patch.

## 11. Minimal Memory Runtime components

| Component | Responsibility | Not responsible for |
| --- | --- | --- |
| MemoryCandidateExtractor | Independent MemoryExtraction Run proposing candidates | Direct memory/business writes |
| MemoryWriteAdmissionPolicy | Deterministic acceptance, session-only routing, business routing, rejection | Creating facts or authorizing side effects |
| LongTermMemoryStore | Accepted entries and their lifecycle/provenance | Career fact authority |
| MemoryRetriever | Type/scope/relevance-constrained lookup | Unrestricted historical-chat scanning |
| MemorySummaryBuilder | Small summary or lookup projection | New independent truth |
| MemoryRetentionPolicy | Expiry/invalidation/forgetting/cleanup policy | Deleting unrelated business history |

These are responsibility boundaries, not a requirement for six services, six frameworks, or six
processes. They reuse the shared Harness for model work and normal local persistence for data.

### Explicit user management

A deterministic Memory management path supports View, Add, Edit, Delete, and Clear All. It validates
type/scope/content and updates the Memory store and derived views without an extraction AgentRun.
The user action is its provenance/authorization; it need not claim an originating chat Turn.
Allow only PREFERENCE, FEEDBACK, WORKING_STYLE, and REUSABLE_AGENT_LEARNING. Career experience,
education, projects, target roles/cities, contact facts, and application records remain business data.
This is a third capability beside Auto Learning and Recall, not a new Agent or generic mutation Tool.

## 12. Conceptual entry semantics — not a finalized schema

A LongTermMemoryEntry needs to express:

- stable identity;
- category and scope;
- accepted content;
- provenance: source Session/Turn for extraction, or explicit user management for manual entries;
- current validity;
- creation history;
- supersession or invalidation relationships where applicable.

Q127 illustrates memory_id, type, scope, content, source_session_id, source_turn_id, provenance,
status, created_at, superseded_by, and invalidated_at. These names are examples for the later
field-level Grill, not frozen field requirements, SQL definitions, or API payloads.

## 13. Supersession, invalidation, and deliberate forgetting

Minimal lifecycle support remains necessary without complex consolidation:

- A superseded durable preference must not coexist as another active contradictory preference.
- Invalidation cancels future use while preserving whatever history the selected retention policy permits.
- Users can explicitly remove unwanted Long-term Memory.
- A new current-turn style request is not automatically a long-term replacement under Q128.

Q131 makes deliberate forgetting a constraint on future extraction/rebuilding, not merely a hidden
row:

1. New Context no longer admits the forgotten entry.
2. Derived MemorySummary and indexes stop presenting it as valid.
3. Old source Turns cannot automatically recreate the same forgotten memory.
4. In-flight extraction rechecks the forgetting decision before committing candidates.
5. Minimal anti-recreation markers/source-range constraints may survive without keeping the deleted
   original text forever; exact representation is deferred.
6. Later explicit user permission may establish a new memory about that topic.
7. Deleting chat and deleting Memory remain distinct, clearly explained actions, neither cascading
   into saved business assets.
8. Local deletion cannot retract content already sent to a Provider; recovery payload follows the
   explicit storage retention rules.

Logical versus physical deletion, marker representation, retention periods, and precise conflict
resolution schemas belong to later design. No complex forgetting/consolidation algorithm is introduced.

### Manual management versus older extraction (Q145)

Before committing an automatic candidate, recheck current entries, manual changes, deletion, and
supersession. A candidate based on sources preceding a clearly corresponding user edit cannot
overwrite that later management decision. If new durable preference versus old-source recurrence
cannot be established reliably, reject automatic mutation conservatively rather than repeatedly
prompting the user.

A later genuine explicit durable user instruction may update the preference through normal
admission; manual management is not a permanent lock. Memory Runtime enforces this conflict check,
not the extractor's claim that its candidate is "latest". Existing no-resurrection rules remain.

## 14. Storage, recovery, and runtime maintenance boundaries

All MemoryExtraction Provider calls pass through ModelInvocationRuntime and then ModelGateway.
MemoryExtraction uses [Recovery](recovery.md): durable dispatch/response, ownership/fencing, and
explicit retry for outcome-unknown model calls. Its cost belongs to BackgroundMemoryBudget under
[Budget](budget.md). It may run only when both budget and low-priority Provider/runtime headroom
admission permit dispatch.

The four storage layers and full retention design live in [storage.md](storage.md): business assets,
protected recovery payload, lightweight audit metadata, and minimal logs. Accepted Memory has its
own non-business lifecycle and MemoryRetentionPolicy. Neither entries nor summaries belong in
unrestricted diagnostics.

Context Compaction is not background extraction. Any semantic checkpoint Invocation is auxiliary
work inside the current AgentRun, sharing that Run's budget, ownership, and recovery. Its complete
design is in [context.md](context.md).

Chat deletion, Memory forgetting, recovery-payload purge, and business withdrawal are different
operations. Q131 prevents source-driven memory resurrection; Q125 prevents payload cleanup from
erasing business history or pretending that purged exact Context can be recreated.

## 15. v1 implementation boundary

Required Memory capabilities:

- durable ChatSession/Turn source and Run/Tool-history references;
- LongTermMemoryEntry storage and minimal lifecycle;
- independent MemoryExtraction Skill/Run;
- MemoryWriteAdmissionPolicy and explicit source-based automatic-admission constraints;
- durable pending extraction work with coalescing Trigger Policy;
- BackgroundMemoryBudget and foreground-priority capacity admission through shared Runtime;
- simple MemoryRetriever and lightweight derived MemorySummary;
- Skill-level memory allowlists;
- separate Auto Learning and Recall controls plus explicit View/Add/Edit/Delete/Clear All;
- forgetting that invalidates derivatives and prevents old-source re-creation.

Context checkpoints/compaction are implemented under independent Context Engineering, not here.

Permitted simplifications:

- simple debounce/idle/accumulated-range triggers once concrete values are chosen;
- simple lookup rather than complex ranking;
- small rule-oriented Memory summaries;
- local persistence and lightweight scheduling rather than distributed maintenance infrastructure.

Explicitly excluded:

- multi-stage consolidation;
- automatic complex merging or vector search over all historical Sessions;
- memory embedding graphs;
- complex forgetting algorithms;
- USER_FACT memory or a parallel career-fact database;
- automatic pre-enablement history backfill;
- new General Assistant/interview features implied only by examples.

Candidate Evidence Agentic RAG remains deferred beyond basic v1. Lightweight collaboration Memory
lookup does not un-defer that work.

## 16. Remaining architecture and later field design

Q128-Q137 settle the three authority concerns, conservative user-sourced learning, durable pending
extraction, separate background budgets, non-resurrecting forgetting, independent Context Compaction,
natural Session-local fact discussion, explicit Save authorization, admitted post-write continuation,
Run-wide auxiliary allowances, finite historical source retention, and scoped Memory controls refined by Q139 into independent learning, Recall, and management.

Remaining refinements must not reopen those choices or introduce field-level design prematurely.
In particular, the implementation must preserve the difference between conversational assertions and
saved facts, and enforce Recall disablement through derived Context as well as direct reads.

Later field-level work determines entry/candidate schemas, pending-range representation, authorization
binding, conflict/forgetting markers, policy identities, source references, retention durations,
trigger values, and API contracts. These examples do not establish an exhaustive schema or prove
implementation.

## 17. Verification implications and formal writeback

Derived verification scenarios for later acceptance mapping:

- A career fact routes away from Memory and becomes Evidence only through explicit confirmation
  plus the authorized Application write path.
- A one-off Resume choice remains Session-local.
- A memory cannot change Tool permission or authorize application.
- Parsing/Fit invocations see no Long-term Memory, including through summaries.
- An accepted collaboration preference is reusable only by allowed Skills.
- Extraction failure does not roll back a completed main task.
- Restart retains pending source ranges, while unknown remote extraction is not silently replayed.
- Background work never charges an arbitrary foreground Turn and yields to capacity pressure.
- Superseded entries do not both appear as active preferences.
- A rebuilt summary/index does not invent entries or restore invalid/forgotten ones.
- A late extractor cannot resurrect an entry the user forgot.
- Context Compaction does not delete the durable Session or write Long-term Memory.
- Payload cleanup preserves business history and accurately reports unavailable exact inputs.

These scenarios describe consequences of accepted boundaries, not already passing tests.
Write stable authority/ownership rules into architecture/contracts, user-facing behavior into spec,
verification into acceptance, and implementation status into progress during the planned refactor.

Additional Q133-Q137 scenarios: discussing a newly stated Kafka fact causes no implicit Save or
repeated confirmation; Advisor formal application uses one concrete impact preview/confirmation
and reaches only the authorized business command;
new committed references enter a new Frame, not old history; disabling Recall blocks later reads,
while disabling Auto Learning blocks automatic publication. Explicit user management works without
a model call and cannot persist career facts as collaboration Memory. Direct Memory blocks are not
checkpoint sources; incomplete streamed output does not trigger learning.

Related Tool naming, action purity, typed source validation, and dependency signaling are defined
in [Tool Actions](tool.md). Architectural objects/properties are collected for later design in
[Contract Design Inventory](../contract/contract-design-inventory.md); neither document finalizes
field schemas or reports implementation.

Q145 requires delayed automatic candidates not to overwrite newer matching manual edits or restore
deleted entries. Q146 requires no persisted Advisor working draft, no compulsory Save prompt for
discussion, and one explicit confirmation before shared-fact application.
