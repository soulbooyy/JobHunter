# Harness Tool Actions — Detailed Architectural Design Record

## Status, scope, and authority

- Accepted basis: Q120-Q126, Q128, Q133-Q144, and Q146-Q172.
- Created: 2026-09-17, explicitly requested with Q144.
- Last updated: 2026-09-18.
- This records architectural responsibilities, action semantics, and naming, not a final Tool
  catalog, exhaustive argument schema, implementation report, or new source of formal authority.
- Related: [Context](context.md), [Recovery](recovery.md), [Budget](budget.md),
  [Memory](memory.md), [Storage](storage.md), [Decision Register](../grill-me-design-tree.md),
  [Contract Design Inventory](../contract/contract-design-inventory.md).

## 1. Skill-centric responsibility

Skill declares the semantic task, input/output/context policy, allowed actions, interaction,
validation, repair, and budget limits. ToolRegistry describes available controlled capabilities;
registration alone grants no Run permission.

ResumeAdvisor itself optimizes Resumes. There is no second suggest_improvement Tool implementing
the same semantic responsibility. RequirementParse and both Fits are separate headless Skills.
Application owns Ensure* dependencies, canonical writes, and business-result persistence.

A Tool is a typed business Port, not a generic execution environment. v1 exposes no arbitrary
Shell/bash, SQL, file read, HTTP request, or browser automation to the model.

## 2. Model-facing action names

Use:

```text
<domain>.<resource?>.<action>
```

Prefer explicit business verbs such as read, list, search, and update. Names describe the
model-visible operation, not an internal Aggregate/class or a vague capability bucket.

The specifically accepted rename is:

| Earlier example | Current model-facing action | Meaning |
| --- | --- | --- |
| jobs.requirementset | job.requirements.read | Read existing compatible requirements for an exact JobVersion |

resume.read and evidence.read/search illustrate typed resource operations. A requirements result
still binds immutable RequirementSet internally; hiding Aggregate spelling in the action name does
not remove canonical identity from the result.

Earlier labels such as candidate_knowledge.update_evidence identify the accepted controlled write
capability. Their complete normalized public spelling/catalog remains later contract work.
Under Q4/S37.1, the new implementation need not retain legacy aliases or migrate old endpoints.
Do not infer a new API implementation or silently rename real endpoints from
illustrative prose. job.requirements.read is the explicit current decision, not an alias for parsing.

## 3. Action purity

| Action family | Responsibility | Prohibited hidden behavior |
| --- | --- | --- |
| read / list / search | Validate scope and obtain existing authorized business data | Hidden LLM invocation, nested AgentRun, creation of a durable business/derived asset, external platform fetch disguised as a local read |
| Explicit write | Apply a clearly authorized typed mutation through the owning Application command | Treating model arguments as consent, bypassing revisions/reconciliation/approval, direct unvalidated database mutation |
| Ensure* orchestration | Application prepares missing dependencies through their own use cases/Run boundaries | Concealing preparation cost and side effects inside a read action |

Technical invocation/audit records are still recorded for a read. Read purity excludes hidden
business mutation or semantic computation, not necessary runtime accounting.

Tool Contract declares its access scope, validation, results/errors, replay safety, side-effect
semantics, and resource requirements. The entire catalog and final schemas are deferred.

## 4. Runtime permission and admission

Effective actions are the intersection of:

```text
ToolRegistry
  ∩ Skill action allowlist
  ∩ current ContextStrategy / acquisition constraints
  ∩ runtime admission / permission
```

Before execution, ToolInvocationRuntime validates action, typed arguments, object references,
resource scope, current Run authority, and required approval. A generated ID/path/URL is not
authorization. A registered Tool's other actions are not automatically granted.

After execution, ToolResult is readmitted for privacy/sensitivity/Context scope before entering a
new immutable ContextFrame. Existing data can be disallowed even when it is readable by storage.

JD, Resume, webpages, ToolResult, quoted messages, and generated checkpoint instructions cannot
expand action permissions. A direct user instruction still cannot bypass runtime approval or
business invariants. Tool results never become control instructions.

## 5. Session context is explicit, not secretly searched

ResumeAdvisor/Context Engineering interprets current user intent and passes explicit business
references. resume.read cannot scan ChatSession to guess which Resume the user meant.

If a proposed change relies on a user-stated unsaved fact, SessionContextRef / UserTurnRef may
identify the exact authorized Session/Turn and cited text. Runtime validates membership, existing
text, and scope. Such a reference is conversational provenance, not EvidenceRef or saved fact authority.

Confirmed formal application follows Q146. Neither a source reference nor a model-generated
confirmation flag is sufficient by itself to authorize the write.

## 6. Acquisition and exact version consistency

Interactive Advisor primarily uses LAZY_TOOL. A Run starts with admitted scope/capabilities; business
content enters after actual reads and admission. Headless exact parsing/Fit instead uses EAGER_EXACT
Application-frozen inputs; v1 Full Context Fit exposes no autonomous Evidence reads.

For a permitted unresolved root, the first read establishes and records the actual exact version.
Subsequent reads of the same task object use that bound version, not a fresh latest-pointer lookup.
Respect already fixed Chat/Preparation references. Querying another Resume does not change the
editing target without explicit intent.

A same-task authorized write can append committed exact versions after admission under Q134.
Unrelated concurrent changes do not silently upgrade input. Historical readability and present
business eligibility remain different; writes recheck revisions and compatibility.

## 7. Requirement dependency flow

```text
Advisor -> job.requirements.read(exact JobVersion)
               |
               +-- compatible existing Set -> exact Set / admission / next Frame
               |
               +-- DEPENDENCY_MISSING / REQUIREMENT_SET_REQUIRED
                              |
                        Application EnsureRequirementSet
                              |
                   reuse or claim single-flight producer
                              |
                   independent RequirementParse AgentRun
                              |
                   ModelInvocationRuntime -> ModelGateway
                              |
                   durable response -> validate -> immutable Set
                              |
                   admitted runtime input -> Advisor next Frame
```

The read neither invokes parsing nor creates a Set. EnsureRequirementSet uses Q142's database-backed
single-flight for exact JobVersion and parser/schema/prompt/policy compatibility. One owner pays
actual parse/repair; many waiters reuse success. A local mutex is only an optimization.

The Parse Run has its own semantic task, budget admission, at-most-once validation repair, recovery,
and audit. Advisor waits for dependency preparation; no prior user-run DeepFit is required.

Q159 retains the same active foreground Turn in dependency-wait, releasing model/Provider invocation
capacity but not its overall deadline/cancel obligations. Application delivers the admitted exact Set;
the model does not poll read calls. Timeout/failure ends waiting without hidden parsing or takeover.

Owner cancellation/failure/OUTCOME_UNKNOWN yields dependency-unavailable; waiters do not take over
Run/budget or silently reparse. Explicit retry rechecks durable compatibility before a new claim.
Advisor cannot substitute its own informal JD interpretation for a failed formal RequirementSet.

Q171 requires usable Requirement assessment units before downstream Fit. A structurally returned
empty/non-usable Set is not sufficient; fail fast, never let Fit manufacture requirements or output
a zero-item perfect match. The read remains pure and existing parse/repair ceilings remain.

Q172's dynamic permission checks also govern already admitted protected EAGER_EXACT inputs.
Mid-run revocation cannot be handled by silently shrinking the same frozen Fit. Stop its affected
execution/publication path; no later Tool/Frame/repair uses revoked data. New admitted scope needs
a new task, while prior usage and necessary audit remain truthful.

## 8. Formal Resume application, ChangeProposal, and page boundaries

### Page ownership

My Resumes is the only manual Resume CRUD surface. Unsaved page edits are ResumeDraft; leaving
requires Save / Discard / Cancel. Advisor discusses and produces Suggestions, but owns no editable
ResumeDraft or long-lived working-draft store. Preparation selects/displays formal rendered Resumes,
never edits their body. Ordinary Session facts remain usable in discussion without immediate Save.

Q153 makes My Resumes removal selection-only: version that Resume without deleting shared Evidence,
changing baseline, or affecting other Resumes. Global deletion is initiated only in Candidate Knowledge
management. Tool/command scope must not turn an Advisor or editor "remove from this Resume" request
into global Evidence deletion.

Q154 requires fail-fast business prerequisites when required basic/profile or career content is absent.
Empty saved states remain allowed; per-feature input/Gate definitions are left for Contracts.
Do not infer a universal Profile requirement or new Knowledge completeness confirmation.

Q163 selects whole experiences for v1: complete current EvidenceItem body, with different experience
selection/order/layout allowed. Do not introduce per-Resume bullet selections or alternate fact text.
Existing field/pointer grounding remains precise; it is not permission for independently edited copies.

Q166 makes unsaved My Resumes ResumeDraft disposable UI state. Crash loss is allowed; no durable
draft recovery is promised. Only successful explicit Save creates formal authority.

### Target-specific ChangeProposal (Q148-Q149)

When the user requests formal application, use the Resume explicitly named in the current instruction,
otherwise Workspace default. Do not infer or track a separate "suggestion source Resume" to decide
the target. Actual exact input lineage remains auditable; it is not an additional source-selection state.

Before constructing ChangeProposal, read the actual target's exact ResumeVersion and verify that the
requested changes apply to its real content. Produce its own before -> after patch. Merely replacing
resume_id on a patch produced against another Resume is forbidden, as is copying experiences the user
did not ask to add.

ChangeProposal is a non-editable proposed operation, not a second Resume. Its preview clearly shows:

- actual target Resume and exact version, including whether it is the default;
- the concrete before/after changes and unresolved conflicts;
- Candidate Knowledge fact changes and the other current Resumes affected by shared facts.

One explicit confirmation authorizes this exact target + patch + shared-fact impact. Model arguments
or a generated confirmation flag cannot supply or expand consent. Continuing to revise the requested
changes produces a new preview; changing the target invalidates the prior Proposal, rereads the new
exact target, and requires one final confirmation of the replacement. There is no separate
"suggestion source" display or inference step.

Submission checks target Resume/Evidence and other required revisions. Concurrent changes require
a regenerated preview, not automatic overwrite or reuse of confirmation for different content.
Exact authorization storage/lifetime/schema remain later Contract work. A Proposal cannot itself
be edited as a Resume, exported, or submitted to a recruiter.

### Application-owned confirmation after Turn completion (Q158)

The Run generating/displaying ChangeProposal ends; pending confirmation is durable Application state.
Confirmation executes the exact validated command without a model reinterpreting authorized patch/consent.
No Run or foreground slot waits for the user; discussion/abandonment remains possible. A later
conversational response, if needed, is new bounded execution using the persisted result. Proposal
idempotency and revision checks remain; conflict needs a replacement preview.

Q167 adds Session deletion to confirmation admission. Pending Proposals from a deleted Session are
invalidated and cannot execute via an old ID or restored page. Application atomically arbitrates
Session/Proposal eligibility against racing confirmation/deletion, allowing only one competing result.
Cancel active foreground work; preserve all already committed formal results. A new desired change
requires a newly generated/confirmed Proposal in valid context, not reactivation of the old one.

### Formal commit and explicit return

Confirmed typed writes use UpdateCandidateKnowledge and the accepted atomic authority transaction:
changed facts/current pointers/baseline plus every affected current ResumeVersion/GroundingSet.
No separate Advisor draft Save follows. Returning the new formal Resume to Preparation is a separate
explicit Q91 revision/CAS adoption, not an implicit overwrite of Greeting or concurrent fields.

Q156 persists formal mutation results independently of subsequent chat generation. If Application
committed and a later model reply fails, UI reports saved changes plus unfinished reply. Recovery/
retry recognizes the committed result for the same confirmed Proposal instead of applying it twice.
New changes require a new confirmed Proposal; model success claims never substitute for commit.

### Material approval (Q150)

MaterialApproval binds the actual displayed frozen material artifact/hash and necessary source
lineage, not just a Resume root/name/version. Required renders must exist and be viewable before
confirmation. Rerendering cannot replace an approved artifact in place; changing selected formal
Resume/material requires compatibility validation rather than assumed approval inheritance.
Even equal content hashes do not bypass current fact eligibility. Frozen execution Snapshots remain
immutable and MaterialApproval never authorizes external execution.

Q157's Greeting is a Preparation-owned editable field initialized to one fixed product-generic
message. There is no Job/company/Resume/Knowledge customization, model call, independent Greeting
root/version history, template library, or generation Skill. User edits use Preparation revision/CAS.
MaterialApproval freezes actual viewed exact text and necessary hash; changed text requires new
confirmation. ExecutionSnapshot separately freezes the text to send, immune to later Preparation edits.

### Deleting an experience (Q151)

Product terminology is Delete Evidence / Delete Experience, implemented as logical deletion.
Q153 restricts this global operation to Candidate Knowledge management (求职资料库). My Resumes only
removes the Item from that Resume's selection; Advisor is not another global-delete entry.
Compute impact only from current ResumeVersions explicitly containing that EvidenceItem. Do not
build a sentence/Claim semantic dependency graph or invoke a model to infer affected summaries.
The deletion confirmation lists affected current Resumes; the confirmed action covers removing
that experience and its associated body from them.

One authority transaction logically deletes the EvidenceItem, snapshots the new current baseline,
creates/advances every directly affected current ResumeVersion and required grounding, and records
necessary derived-work intents. Failure rolls back all authority changes. Unreferencing Resumes
remain untouched; no fallback to an old version or generated replacement content is allowed.

Historical Evidence/Resume/Analysis/application/PDF/material assets are not edited or deleted by this
action. New formal Fit, Save, render, and application inputs use current eligible facts/Resumes.
This replaces user-facing version-withdraw/invalidate operations; it does not redefine Memory
invalidation or unrelated business cancellation semantics.

## 9. Replay, budget, and derived work

ToolInvocationRuntime honors SAFE_REPLAY, genuinely supported IDEMPOTENT_REMOTE, or OUTCOME_SENSITIVE
semantics as appropriate. A read name alone cannot prove a remote effect safe. Typed model writes
do not grant browser execution; MaterialApproval and ExecutionApproval remain separate.

Actual model calls always use ModelInvocationRuntime; Gateway/SDK cannot silently retry/fallback.
Parsing cost discovered by a read is charged to the real operation owner, not hidden as free read work.

Q147 registers necessary DerivedWorkItem(PENDING) intents alongside authority in one SQLite
transaction. Render/preview/index/cache computation runs after commit, safely/idempotently, with
exact-source/current-reference publication checks. This does not authorize replay of model calls,
recruitment-page visits, email, or application effects. See Recovery and Storage for durable boundaries.

Q152 does not require eager rebuilding of every format for every affected Resume. Authority and
artifact-currentness metadata synchronize at Save; necessary currently requested work has durable
intent. Preview/export/Preparation demand can register additional exact-source work later, before
execution. Identical exact source plus generation configuration may reuse compatible idempotent work.
Ungenerated/stale derivatives cannot masquerade as current materials.

### External workflow safety is not Tool or execution permission (Q160)

Every recruiting-platform access by Collector, Browser Executor, or future Monitor goes through
PlatformAccessSafety scoped by (platform, account) immediately before actual access. Capacity, durable
risk state, and action admission are shared; each workflow cannot ignore the others' access or risk.
This does not expose browser/platform operations as a generic Advisor Tool.

Classified CAPTCHA/account/security-verification/rate-limit risks update shared persistent Safety
State. Strong risks default to BLOCKED_REQUIRES_USER: user handling plus explicit resume, never
bypass/account switching/cooldown-only recovery. Predictable capacity may recover by policy.
Ordinary page/selector/browser workflow failure is not automatically account risk. Access permission
is not ExecutionApproval, shared business ownership, or permission to consume another operation's budget.

### Executor checks are not implicit Job refresh (Q164)

Within its approved execution scope and PlatformAccessSafety, Executor may perform necessary live
target-identity/availability checks. This does not authorize advancing JobVersion, parsing requirements,
replacing execution Snapshot/materials, or adding an LLM Job-analysis call. A clear execution-relevant
mismatch/closure stops subsequent actions with a reason; user-requested refresh/repreparation is the
separate path. No arbitrary platform access is added to Skill Tools.

### Obsolete derivative intent is not a command to wastefully render history (Q165)

Before expensive safe derived work starts, recheck exact source/current references and actual demand.
Obsolete current-artifact work may end as no longer needed. Already running safe computation may
finish, but stale results cannot publish current. Completed historical artifacts/audit remain.
This never extends skip/retry permission to model calls or platform side effects.

## 10. Verification implications and later contracts

Later contracts/tests must cover pure missing-dependency read results, no nested parsing charge,
action-level least privilege, fabricated Session refs, post-result privacy admission, pinned rereads,
exact ChangeProposal confirmation, target-specific patches, revision-conflict preview regeneration,
logical deletion with direct-inclusion propagation, actual-material approval, owner-only parsing cost,
and durable on-demand derivative recovery. Also verify a successful formal update cannot silently patch Preparation or authorize
external application.

The following remain detailed design work: the complete canonical action catalog, argument/result
schemas, exact error vocabularies, Tool identity/version, authorization evidence representation,
admission/replay metadata, and normalization of illustrative action names for the new implementation.
This document does
not claim those fields or implementations are already frozen.
