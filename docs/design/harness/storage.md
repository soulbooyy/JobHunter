# Harness Storage, Retention, and Audit — Detailed Architectural Design Record

## Status, scope, and naming

- Accepted basis: Q125, reaffirmed with Q132; integrations: Q83, Q94, Q122, Q124,
  Q127-Q172 and the existing immutable-business-history decisions.
- Last updated: 2026-09-18.
- This design record preserves architectural storage boundaries, not finalized schemas, retention
  durations, encryption choices, database layouts, or a new Source of Truth.
- The filename is `storage.md`, because logging is only one of four concerns. A file named log.md
  would incorrectly suggest that durable response, recovery, audit, and business history are logs.
- Storage is a cross-cutting responsibility split, not a mandate for four databases or a new
  monolithic persistence service.

Related records: [Recovery](recovery.md), [Budget](budget.md), [Memory](memory.md),
[Context Engineering](context.md), [Decision Register](../grill-me-design-tree.md).

## 1. Core commitment

Durable response and exact ContextFrame mean that Harness reliably persists what the model
actually received and the complete business response when needed for recovery and invocation-level
inspection. They do not require permanent retention of every sensitive payload and never require
writing those payloads to ordinary logs.

```text
Business authority        -> business lifecycle
Recovery payload          -> recovery need + independent retention
Audit metadata            -> lightweight durable explanation
Operational logs          -> minimal diagnostics
```

Durability, immutability, authority, recoverability, and retention duration are different properties.

An immutable Frame is never overwritten with a different input. Its payload may later become
unavailable under retention policy; the retained metadata must say so honestly.

## 2. Four storage layers

| Layer | Purpose | Representative content | Lifetime principle |
| --- | --- | --- | --- |
| Business Durable Assets | Formal business authority and accepted durable results | Evidence, Resume, RequirementSet, Analysis, Application history, required lineage | Business lifecycle |
| Harness Recovery Payload | Recover execution and inspect actual Invocations | Exact ContextFrame payload, complete ModelInvocation business response, necessary ToolResult | Protected local storage; independent retention |
| Harness Audit Metadata | Explain identity, boundaries, provenance, and outcomes without full payload | Run/Invocation/Frame refs, Skill/model/policy versions, hashes, usage, time, status, lineage | Lightweight durable history |
| Operational Logs / Telemetry | Diagnose operational behavior | Trace IDs, event, elapsed time, status, error category | Minimal content by default; not business storage |

The table names concepts, not exhaustive column definitions. Metadata still needs access and
sensitivity controls; “lightweight” is not permission to embed arbitrary business text.

## 3. Business Durable Assets

The Domain/Application layer owns formal assets and their valid mutation paths:

- saved Profile/Evidence/Resume versions and current pointers;
- immutable EvidenceBaselineSnapshot;
- derived-but-durable RequirementSet and validated analyses;
- Suggestion/HumanChoice/Grounding lineage where required;
- application preparation/execution/application history according to their own contracts.

These assets remain independently meaningful if a chat or model recovery payload is later cleaned.
Their exact references preserve historical interpretation.

“Business Durable Assets” is a persistence category, not a claim that every derived asset has equal
fact authority. For example, a RequirementSet remains derived from exact JobVersion JD, and an
Analysis remains a validated analysis result rather than a new Candidate fact.

Recovery cleanup must not cascade into these assets. Explicit business deletion/withdrawal,
Resume logical removal, and future personal-data erasure are separate workflows.

Q146 confines ResumeDraft to My Resumes page-level editing. Advisor/ChatSession/Preparation do not
own a working-draft business asset. Accepted Advisor changes create formal versions immediately after
the concrete impact preview and one confirmation; business lineage survives chat cleanup.

Q148-Q149's ChangeProposal records a non-editable target-specific operation preview and its exact
confirmation binding, not a replacement Advisor draft. Changes of target/patch or revision conflicts
require a replacement preview. Necessary authorization/result lineage is not merely model recovery
payload; final storage schema/lifetime remains later design.

Q150 binds MaterialApproval to actual displayed frozen material artifact/hash and sources. An approved
artifact is never rewritten by rerendering. Q151 logically deletes an experience and synchronizes
directly containing current Resumes; historical EvidenceVersions, ResumeVersions, analyses, completed
applications, and already rendered PDF/MaterialArtifacts remain immutable. Historical material
describes what was rendered then; it is not proof of present formal-use eligibility. New formal
analysis/Save/render/application uses current eligible inputs. No deletion-time semantic Claim graph
or per-version user-facing withdrawal mechanism is introduced.

Q153 separates Resume-only selection removal from global Evidence deletion, available only in
Candidate Knowledge management. Selection removal versions only that Resume; shared baseline and
other Resumes remain unchanged. Q154 allows empty saved states; later Contracts define each
operation's fail-fast required basic/career inputs.

Q156's persisted mutation result survives subsequent chat-generation failure and is the recovery/
idempotency basis for a confirmed Proposal. Do not report committed facts as rolled back or recreate
their versions on retry. This outcome is not an incomplete assistant stream or disposable recovery
payload; exact persistence representation is later Contract work.

Q157 stores editable Greeting within Preparation, initialized from fixed generic product text,
not an independent root/template/Skill. MaterialApproval and ExecutionSnapshot freeze actual exact
text/hash as needed; later edits never replace frozen historical content.

### Pending Proposal, platform safety, and retained collection (Q158-Q162)

Pending ChangeProposal persists as Application interaction state after its creating Turn/Run ends.
Confirmation executes the exact validated command; mutation result remains durable independently
of later narration. Exact schema/lifetime remains Contract work.

PlatformAccessSafety has persistent shared Safety State by (platform, account), reused across
workflows/restarts. This is risk/admission metadata, not raw credentials or a new Candidate/tenant
identity. Strong risk cannot disappear on process restart.

Stopping collection retains successfully saved Jobs and frozen-Preference audit. Current Preferences
alter local filtering, not historical results or Job retention. Preparation reentry preserves
unfinished selections/Greeting; refresh/repeated requests cannot duplicate creation or overwrite it.
Explicit new preparation and later real reapplication remain independent histories.

### Disposable page drafts versus persisted pending actions (Q166-Q167)

My Resumes ResumeDraft is temporary UI state; crash loss is acceptable and v1 does not persist
a recovery checkpoint/autosave copy. This does not weaken formal Save durability or Harness recovery.

Pending ChangeProposals are different: Session deletion makes its unconfirmed proposals ineligible
(e.g. INVALIDATED_BY_SESSION_DELETE), including access through old IDs/restored pages. Application
arbitrates competing deletion/confirmation atomically. Necessary invalidation/authorization metadata
must preserve non-executability without implying indefinite retention of the deleted chat payload.

Existing mutation results, Evidence/Resume versions, completed applications and required audit
lineage survive Session deletion. Completed historical PDF/material assets also remain immutable.

### Independent outcome records and deleted extraction sources (Q168-Q172)

A valid Fit Analysis may persist assessments/reasons/lineage without a comparable aggregate score.
No-score is not a stored zero or permission to enter normal score ranking. An unusable empty
Requirement target is instead a pre-Fit failure; do not publish it as a usable downstream dependency.

Failed/unknown Memory extraction source ranges remain distinguishable from successfully processed
and newer pending work. They cannot be hidden inside the next automatic batch or marked successful
merely to advance a cursor. Deleted Session sources cannot create new accepted Memory; previously
accepted Memory has a separate lifecycle.

Mid-run protected-input revocation prevents further authorized consumption/current Analysis
publication, not truthful recording of prior dispatch/usage. Necessary audit/recovery data follows
protected retention; no ordinary log dump or claim of remote data retraction is authorized.

## 4. Harness Recovery Payload

Recovery payload includes the complete business data necessary to continue local processing:

- the exact input messages/blocks and admitted content of a ModelInvocation's ContextFrame;
- the complete model business response;
- necessary ToolInvocation results;
- retained checkpoint/source payloads when needed by the execution's recovery boundary.

It is stored in protected local storage, not ordinary logs.

### Durable response is not a raw HTTP dump

Do not retain:

- Authorization headers;
- API keys;
- cookies;
- login tokens;
- browser sessions;
- unrelated transport secrets.

A complete business response may be structurally invalid as a Domain result. It is retained to
explain/recover validation, not accepted automatically as authority.

### Recovery boundary

Under Q122:

- persist dispatch intent before the remote call;
- persist the complete response before local parse/validation;
- an in-memory response is not yet durable;
- partial output is not assumed complete;
- lack of a durable response after dispatch intent implies uncertainty for outcome-sensitive calls.

The recovery module owns replay decisions. The storage module ensures it can distinguish
persisted intent, available complete content, and unavailable content truthfully.

### Streaming deltas are outside durable recovery payload (Q141)

Live deltas carried through StreamBridge/SSE are transient presentation and need not be retained.
A partial stream does not become a formal Assistant Turn, adoptable Suggestion, or completed
extraction source. Refresh/recovery may discard it; never concatenate it with a new Retry response.

The complete response must be RESPONSE_DURABLE before local parse/validation and formal publication.
Backend completion may still persist the full result after a frontend disconnect; reconnect reads
that result. Neither a displayed phrase nor a fragment establishes an Application Save. Invocation
failure/unknown metadata and conservative usage remain durable even when all deltas disappear.

## 5. Harness Audit Metadata

Retain lightweight explanatory facts such as:

- Run, Invocation, and Frame identity/references;
- Skill, model, and relevant policy lineage;
- input/output hashes;
- known/estimated/unknown usage;
- time, status, and execution relationships;
- references to business results and retained/purged payloads.

These are semantic examples, not frozen field schemas.

Metadata supports questions such as:

- Which task attempted which model call?
- Which exact business versions were referenced?
- Was there a complete durable response?
- Did validation/publication succeed?
- Was usage measured or unknown?
- Is exact payload still available?

Metadata alone does not answer “what exact text did the model see?” once that payload is purged.
A hash is an integrity/provenance aid, not a compressed copy of the content.

## 6. Operational Logs and Telemetry

Ordinary operational output defaults to minimum diagnostics:

- correlation identities;
- event;
- elapsed time;
- status;
- sanitized error category.

Do not log full Resume, Evidence, prompt, Tool content, model response, or secrets by default.
Do not accidentally use exception formatting or adapter diagnostics to copy a remote payload into
a log. Typed boundary errors and safe summaries are consistent with the existing engineering rules.

Local-first storage does not authorize external telemetry upload. The selected self-hosted Langfuse
integration remains derived telemetry, not authority for business commit, Invocation completion,
usage settlement, or recovery. Delivery failure cannot cause business rollback or invocation replay
(Q174). Callback and explicit SDK instrumentation apply the same masking/redaction before export
and correlate canonical Run/Invocation IDs without duplicate invocation or cost accounting.

Logging is not a fallback persistence mechanism for missing durable business or recovery records.

## 7. Retention and cleanup boundary

Accepted policy principles:

1. Payload necessary for an unfinished Run's recoverable state stays available until its recovery
   boundary is explicitly ended.
2. Completed-task raw Context/response may be cleaned under an independent retention policy.
3. Cleaning recovery payload does not delete formal business assets or application history.
4. Necessary lightweight audit metadata can remain when the raw payload is removed.
5. Availability is explicit, for example PAYLOAD_AVAILABLE / PAYLOAD_PURGED.
6. Concrete periods, purge timing, storage mechanism, and complete status vocabulary are deferred.

Cleanup must not race live recovery into believing a required response exists when it was removed.
The detailed coordination mechanism is for later Contract design.

Ending a Run does not automatically settle unknown remote cost. Budget reservations and audit
uncertainty have their own rules; deleting payload cannot retroactively prove usage was zero.

Q147 requires necessary DerivedWorkItem(PENDING) intents in the same SQLite transaction as the
authority Save. Do not rely on a post-commit in-memory task registration. Pending work remains durable
for restart discovery; expensive computation is post-commit. Publication checks exact inputs/current
references and cannot replace a current artifact with a stale result. These intents are technical
recovery records, not career-fact authority or permission to replay outcome-sensitive remote work.

Q151 applies the same transaction rule to logical Evidence deletion: new baseline, all directly
affected current Resume versions/pointers, and necessary derivative intents commit together.
Q152 separates synchronous authority/currentness updates from actual artifact demand. Do not render
every format eagerly on every Save. A required page preview, explicit export, or Preparation need
may register exact-source/configuration work; later demand must persist intent before execution too.
Missing/stale derivatives cannot be advertised as current. Existing compatible work may be reused
idempotently, without rewriting historical artifacts or expanding replay permissions.

Q165 rechecks exact source/current references and demand before expensive derivative execution.
A queued obsolete current-artifact intent may end as no longer needed; durability records the
disposition rather than compelling every historical intermediate render. Already running safe work
can finish without publishing current; completed artifacts/audit stay. No platform/model replay is
authorized by this derivative-only lifecycle rule.

## 8. Honest historical interpretation after purge

After exact payload cleanup:

- retain available lineage, hashes, outcomes, and business results;
- identify that invocation-level content is unavailable;
- do not regenerate input from current Resume/Evidence/Memory and label it the old Frame;
- do not substitute a lossy ContextCheckpointSummary for the historical exact payload;
- do not claim a hash or reference proves semantic contents no longer retained.

Historical business explanation can remain possible through exact durable business versions.
Exact reproduction of a model invocation is a stronger claim and is no longer possible from
missing payload alone.

## 9. Context externalization and checkpoints

Q132 externalizes large Tool results into a durable complete source plus a bounded model-visible
preview/metadata/reference. Compaction reduces active model Context; it does not delete Session
history. A checkpoint is a derived continuity artifact, validated and durably published before use.

Q136 distinguishes two retention relationships:

| Relationship | Retention obligation |
| --- | --- |
| Active Recovery Dependency | Keep exact payload needed by a running/recoverable Run until the final safe recovery boundary ends |
| Historical Source Reference | Permit independent payload retention/cleanup; preserve lightweight metadata, hash, lineage, and honest availability |

A source_ref says where a checkpoint came from; it does not promise that the source exists forever.
Do not purge an active dependency just because its producing Invocation completed. Conversely, a
terminal historical checkpoint does not pin every Tool response or Context payload indefinitely.

Before historical continuation or Session reopening, check source availability and current admission.
When the referenced exact EvidenceItemVersion/ResumeVersion or other Business Authority still exists
and access is permitted, a controlled new ToolInvocation may read it. Its result is a new read,
never a reconstruction masquerading as the original ToolResult or historical ContextFrame.

Retain PAYLOAD_PURGED / SOURCE_UNAVAILABLE or equivalent explicit availability when content is gone.
If a necessary source cannot be obtained, stop or request user-supplied content rather than guessing
from a checkpoint. Do not automatically revisit recruiting platforms, replay old external requests,
or execute side effects to fill historical gaps. Exact pin/cleanup coordination and enum fields
remain later detailed work; the active-versus-historical lifetime rule is settled.

Q139 does not eagerly read authority merely because it is locally stored. Interactive LAZY_TOOL
reads record the admitted exact versions actually obtained; headless EAGER_EXACT inputs are frozen
before Run creation. Externalized lazy Resume content may be reread at its exact version as a new
ToolInvocation. This does not require preserving every old ToolResult forever.

## 10. Memory storage and deliberate forgetting

Long-term Memory entries have their own non-business lifecycle and MemoryRetentionPolicy.
MemorySummary and indexes are derived from eligible entries, not alternative authorities.

Q131's accepted boundaries:

- forgetting removes an entry from new Context use;
- derived summaries/indexes must cease presenting it as valid;
- old source Turns cannot automatically recreate deliberately forgotten memory;
- a pending extractor rechecks forgetting before committing;
- minimal anti-recreation markers may remain without keeping the deleted raw content forever;
- later explicit user permission may create new memory;
- chat deletion and Memory deletion are distinct operations whose scope must be visible;
- neither operation cascades into formal business assets;
- local deletion cannot retract already sent remote model input.

Exact logical/physical deletion choices, marker representation, and retention durations remain
later design work. This is not a claim that deleting a memory instantly removes every historical
invocation payload or externally transmitted copy.

Q139 separates Auto Learning, Recall / Injection, and explicit user management. Auto Learning off
blocks new automatic extraction/publication, not reads. Recall off blocks subsequent model-visible
Memory, not stored entries or automatic learning. Explicit View/Add/Edit/Delete/Clear All uses
deterministic validation without an extraction Run; provenance reflects the user management action.
Neither switch deletes Session/Business Authority or retracts remote content. Reenablement does not
default to disabled-period history extraction; payloads retain their recovery/privacy lifecycle.

Long-term Memory is not a direct ContextCheckpoint source. Legacy directly mixed blocks are excluded
or continuity rebuilt from allowed durable Session/runtime sources. v1 does not erase second-order
effects on actual assistant conversation. Memory CRUD cannot create a parallel career-fact store.

## 11. Scope and privacy checks still apply after persistence

Persisted content is not automatically model-visible.

- Business data still passes task/Skill admission and redaction.
- Tool results pass readmission before entering another Frame.
- Memory passes its category/scope/Skill admission.
- Source references do not authorize arbitrary file, URL, SQL, or Tool access.
- Old stored data is not a substitute for current permission or approval.

A stored exact input can be valid historical audit while being invalid for a new Run. Historical
readability and new business eligibility remain different contracts.

## 12. Non-goals and later detailed work

This architecture does not finalize:

- a universal retention duration;
- exact database/table/blob layouts;
- encryption technology or key management;
- every payload-availability enum;
- export/erasure APIs;
- a central log platform;
- remote telemetry permissions;
- metadata schemas and amount/token representation;
- live-reference pinning and cleanup coordination mechanics.

Those details must implement the accepted authority, recovery, privacy, and honesty boundaries.
Formal writeback belongs in architecture/contracts/acceptance/development; current implementation
status belongs in progress.

## 13. Verification implications

Later verification should cover:

- crash recovery with a retained complete response and no second model call;
- explicit unavailability after valid payload purge;
- no business-history deletion through recovery cleanup;
- no secrets or business payloads in default diagnostics;
- unknown usage remaining unknown after payload cleanup;
- no replacement of a purged Frame by reconstructed current inputs;
- no compaction-induced Session history deletion;
- Memory forgetting invalidating its derived summaries/indexes;
- attempted old-source re-extraction not reviving forgotten Memory;
- source rehydration honoring exact identity and admission.

These are design implications, not claims of passing implementation tests.

Q136-Q137 add: cleanup cannot remove still-needed active recovery dependencies; expired historical
source references retain honest unavailable status; permitted exact business rereads are new reads;
Recall disablement retains entries while blocking Context use; Auto Learning independently gates
pending automatic publication. Transient deltas need not survive restart, but complete durable
responses and committed business results follow their own retention boundaries.

Related Tool naming, action purity, typed source validation, and dependency signaling are defined
in [Tool Actions](tool.md). Architectural objects/properties are collected for later design in
[Contract Design Inventory](../contract/contract-design-inventory.md); neither document finalizes
field schemas or reports implementation.
