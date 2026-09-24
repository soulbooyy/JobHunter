# JobHunter Product Specification

> **2026-09-24 supplemental baseline.** [CG03S1](design/contract/sl-02-m1-supplement-grill.md) supersedes shared Profile/Evidence authority and parallel Fits. Independent Resumes, default-derived read-only portrait and suggestion-only optimization below are approved scope; implementation status is separate.

> English is the authoritative documentation language. This document defines intended product behavior; it does not report implemented features or passed tests.

## 1. Purpose, scope, and document authority

JobHunter is a single-user, local-first personal job-search workspace. It helps its user maintain career facts and resumes, acquire and screen Jobs, assess fit, improve resumes, prepare and authorize applications, and track real application outcomes. These are independently accessible tasks with their own prerequisites, not a mandatory sequence that every Job must traverse.

This specification owns product behavior; [Architecture](architecture.md), [Contracts](contracts/index.md), [Acceptance](acceptance.md), and the [other documentation owners](index.md#formal-document-owners) own their respective responsibilities.

**Sources:** Q1–Q6, Q11, Q22, Q26, Q32, Q53, S24.2, S37.1, S38.1; Q/S references identify provenance in the [Decision Register](design/grill-me-design-tree.md).

## 2. Workspace and task organization

### 2.1 Independent capabilities

The workspace supports independent ManualApplicationEntry maintenance, formal Job collection under saved acquisition Preferences, explicit task selection, single DeepFit over the default-derived portrait and independent selected-Resume optimization, conversational resume improvement, application preparation, authorized external execution, and application tracking. The user can enter a capability when that capability's own prerequisites hold. A completed Fit is not required before using Resume Advisor or beginning preparation.

Resumes own candidate-material facts and contacts; Profile/Evidence are read-only projections. Preferences and application history retain separate authorities. A navigation entry may combine them without creating another owner. The single-user boundary does not introduce a unified Candidate Aggregate, Candidate identity layer, or tenant system.

**Sources:** Q1, Q6, Q8, Q16, Q24, Q53, Q112, S17.4.

### 2.2 Five navigation entries

The English names below describe the five accepted entries; they do not decide a new UI-localization policy or rename the labels accepted in S17.2.

| Entry | User task and boundary |
| --- | --- |
| My Resumes | Import, create, manually edit, organize, select a default, and remove formal Resumes; the only manual Resume CRUD surface |
| Candidate Knowledge | Read the default-derived portrait, inspect source attribution, refresh or open the source Resume for editing; no independent fact CRUD |
| Job Pool | Browse formal Jobs; select Job(s) for DeepFit using the ready default portrait, or explicitly select a Resume for targeted optimization/Preparation |
| Job Assistant | Conduct ordinary or preparation-originated resume-optimization conversations through the same ResumeAdvisor capability |
| My Applications | Review real application history and progress; its application entry routes to Job Pool for Job selection |

DeepFit is inside Job Pool, not a separate navigation entry. Preparation is a contextual flow after selecting Jobs and choosing to apply, not a top-level page. Job Assistant initially exposes conversational resume optimization only.

Job Pool defaults to a flat Job list. It may offer a Company aggregation view that summarizes related Jobs and returns to the ordinary list with a company filter. This browsing view creates no independent Company authority. Local filters and sorting are view choices, distinct from saved search Preferences.

ManualApplicationEntry records appear only in their separate view within Job Pool, never mixed into the formal Job list or Company projection. They provide a manual application shortcut without another top-level navigation entry.

A one-run Fit selection, Collection admission, beginning preparation, and a real application are different actions. Long-lived pursuit/bookmark intent remains deferred; that exclusion does not exclude the explicitly accepted ManualApplicationEntry capability. See [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1).

**Sources:** Q6, Q23, Q146, Q153, S5.1, S5.3, S17.1–S17.4; S37.1 removes compatibility-only retention of old Shortlisted behavior.

<a id="33-whole-experiences-and-shared-edits"></a>
## 3. Candidate Knowledge and Resumes

### 3.1 What the user saves

Users maintain multiple independent Resumes, each with its own name, contacts, structured career entries, rich text, presentation and immutable version chain. There is no Master/Application subtype or mandatory derivation from the default. Editing A cannot modify B. Contacts belong to each document; there is no separate shared contact Profile Save or source-adoption workflow. Existing contact privacy remains.

The Workspace owns one `default_resume_id`. It selects the current ResumeVersion used to understand the candidate globally; choosing another document for optimization or application does not switch it. “Knowledge” is a read-only portrait composed of CandidateProfileProjection and CandidateEvidenceProjection. It is not a separately maintained fact library. Correct the source Resume or explicitly refresh the projection.

### 3.2 Import, review, and Save

Upload/parse produces a temporary editable Resume draft, with disclosed gaps when parsing is incomplete. Review/correction followed by one confirmed Save creates the independent formal document. Upload/parse/cancellation alone saves no career facts. If the saved document becomes default, ordinary portrait derivation follows. A valid Save never depends on model success, and model failure cannot undo it.

### 3.3 Structured entries and the read-only portrait

The editor keeps structured education, work, project, skill, award and certification entries. TipTap is adapted to the application canonical AST; stable entry/block IDs survive edits and reorder. Copy creates new IDs; split/merge and undo follow the Resume Contract. These IDs are not another editable Evidence store.

Evidence preserves exact original entry context and individual paragraph/listItem text. The Profile is a small semantic index with an `entries: ProfileIndexEntry[]` collection; each entry contains **name, description, evidence_refs** (schema v1). Education, skills and demonstrated domains use that same shape. Every capability needs concrete support; no proficiency score, personality or unsupported upgrade is inferred. Header, contacts, hidden link targets and project URL do not enter portrait generation; actual education comes from education entries and intent from Preferences. Stored link provenance is preserved and never fetched.

### 3.4 Defaults, removal, and empty states

Default switch commits immediately and rebuilds asynchronously. A meaningful saved-default change does the same; dirty drafts and non-default Saves do not. Publish Profile and Evidence as a coherent pair. While rebuilding or failed, show portrait unavailable with source and refresh, and reject new DeepFit with a clear prerequisite message. Do not fall back to an older portrait or expose a partial-Evidence workflow. Ordinary GET/page reload cannot invoke a model. Explicit refresh deduplicates matching running work; refreshing a ready source also makes it unavailable until success. Failure requires explicit retry.

Deleting default with other Resumes preselects next, otherwise previous, in the canonical list, allows the user to choose another replacement and shows the change before confirmation. Backend cannot silently reselect after a race. Final Resume removal is allowed and clears default/portrait. Empty or contacts/Header-only Resumes can save and be default, but produce no usable portrait or model call. Create/import is available; Preferences and manual application entries remain independent.

### 3.5 Current use, grounding, and generated materials

Presentation-only saves may reuse supported semantic interpretation only after proving compatible admitted content and remapping every Evidence ref to the new exact version. Old histories are unchanged. An in-flight DeepFit retains its original complete inputs after Save/default switch; its result is historical, not a result for the new portrait.

Saved preview/export renders the selected exact ResumeVersion directly. It requires neither default selection nor a ready portrait. Source Save, portrait readiness, rendered bytes and application success are different outcomes. Default changes cannot retarget material selection, viewed-material confirmation or execution approval. Ordinary removal retains exact history; the development reset exception is explicit and offline, not normal deletion.

**Normative detail:** [Resume](contracts/candidate/resumes-grounding.md#res-017), [Evidence](contracts/candidate/evidence.md#evd-016), [Profile](contracts/candidate/profile.md#pro-010), [Save](contracts/candidate/candidate-save.md#sav-018), [Workspace](contracts/foundation/workspace.md#wsp-013). **Provenance:** CG03S1-BC1–BC3, Q6–Q23, Q27, Q31–Q41.

## 4. Jobs, Preferences, and collection

### 4.1 Job identity and manual entry

One reliable platform source identity identifies one Job. Semantic changes to that source's content create immutable JobVersions. Similar listings from different sources remain separate; v1 performs no cross-platform or historical Job merging.

ManualApplicationEntry is an independent mutable record outside the formal Job family. It saves only a company, role title and user-provided application URL as business content. The user can repeatedly edit it through explicit whole-record Save, physically delete it and click its action to request a new browser tab at the saved URL. A neutral waiting page resolves the displayed revision before external navigation; only navigation initiation is reported. It has no JobVersion or immutable content-version history. Saved entries require all three business values; removal physically deletes the entry while minimum create receipts remain for replay protection. Exact fields, validation and operation semantics are owned by the [Entry Contract](contracts/jobs/manual-application-entries.md).

An entry is not a Requirements, DeepFit, Job-targeted optimization, Job-targeted Advisor, Preparation, automatic Execution or Application History target. Browser opening does not create a Job, collect its content, convert the entry into a Job, or establish any application fact. Formal consumers continue to require their own eligible Job/JobVersion inputs.

Formal BOSS collection admits only validated complete details/JD, creating a Job and its first immutable JobVersion together. There is no Manual root-only exception in the formal Job family. Complete canonical JD and exact immutable content snapshots remain required.

**Sources:** Q12–Q13, Q17, Q44, Q48–Q49, S9.1, with later [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1) replacing the Manual Job path while retaining formal Job completeness/version/history invariants.

<a id="42-preferences-and-deterministic-quickscreen"></a>
### 4.2 Preferences as future collection intent

One global PreferenceSet owns durable user intent for future automatic acquisition. The six dimensions are job search keywords, accepted work cities, minimum salary, recruitment types, excluded companies and maximum required education. Work mode remains deferred. No personal target defaults or soft weights are invented.

Before first formal acquisition, the user must explicitly choose a legal value for each dimension and successfully Save one complete immutable PreferenceSetVersion. Missing/unfilled dimensions or an all-empty object cannot represent valid unrestricted configuration. Keywords require at least one valid term; each of the other five dimensions permits an explicit UNLIMITED choice, mutually exclusive with its concrete effective values. The five fields use explicit UNLIMITED/LIMITED mode objects under CG02-Q16; missing, empty or simultaneously active concrete/unlimited values reject. Unfinished configuration and explicit no-constraint choices remain distinguishable. This requires complete user choices, not a restrictive predicate in every dimension.

`target_job_keywords` contains user-maintained terms for source searches, not terms that every returned Job title must contain. A Java developer returned for a backend search cannot be rejected merely because its title omits the search term. First release does not automatically expand terms into synonyms or model-generated queries. Preferences does not own query composition, OR execution, search count, deduplication or source encoding.

City intent is city-level, without inferred neighbouring cities, districts or commute distances. Salary intent is a minimum CNY pre-tax monthly base amount, without automatic annual/day-rate, bonus/equity or extra-month conversion. Recruitment types support multi-selection of CAMPUS, INTERNSHIP, EXPERIENCED and PART_TIME; unrestricted is not a persisted type enum member. These are user acquisition categories, not a claim of one mutually exclusive source field. Company exclusions use complete display-name equality after fixed outer trim without case/Unicode/width or suffix/alias conversion, without implicit fuzzy/substring/affiliate matching. `max_required_education` limits a Job's required education; MASTER means master's and below, not the Candidate's own credential. CG02-Q18 defines six ordered education levels, grouping high school and secondary vocational/technical school into UPPER_SECONDARY; source qualification mapping remains later Collection work.

The canonical dimension fields are `target_job_keywords`, `accepted_cities`, `minimum_salary`, `recruitment_types`, `excluded_companies` and `max_required_education` under [CG02-Q11–Q15](design/contract/sl-01-m2-grill.md#cg02-q11). Keyword/city/company controls add one structured item at a time and display removable Chips; there is no comma-string parser. The other five dimensions have explicit UNLIMITED checkboxes that disable their concrete controls. Salary UI accepts ordinary integer input in CNY/month; the backend accepts exact JSON integer values in [1, 300000], including equivalent decimal/exponent spellings, without coercing strings or rounding invalid fractions; recruitment types are multi-select and education is single-select. Short UI labels use explanatory text to distinguish monthly base pay and Job-required education from Candidate credentials. Any invalid field makes the complete Save fail atomically; backend validation cannot be replaced by UI checks. Inactive unsaved drafts are not authoritative constraints.

Only successful explicit Save publishes authority. Ordinary Save checks revision before canonical comparison; stale revision conflicts even for equal content. A current-revision canonical no-op creates neither a version nor a revision increment. A real change publishes a new immutable PreferenceSetVersion. Keyword/city/type/company values are unordered sets; backend field-specific normalization/deduplication and deterministic ordering establish equality, so order/duplicate-only differences are no-ops. Keywords use fixed Common outer trim without case/Unicode/width/internal-space or synonym conversion. Cities/companies use the same fixed trim and preserve other text. Text sets use Unicode code-point order; recruitment types use their declared enum order. CG02-Q20 fixes item/canonical-set limits; complete request/error/retry representation remains Contract work. PreferenceSet is lazily created with its first immutable version and current pointer in the first successful complete Save; Workspace initialization creates none, and failed first Save leaves no root. First publication starts revision at 1; real changes increment it, while maximum revision still permits a valid no-op. Successful immutable versions retain complete content for the Workspace lifetime, without automatic expiry, single-version deletion or rollback. Reading current Preferences before first Save succeeds as NOT_CONFIGURED and creates nothing. Each logical Save has a request identity for durable successful replay, which returns its original result without restoring an old current pointer. Successful request receipts, including no-op receipts, are retained for the Workspace lifetime and committed atomically with their outcomes. Current reads return a consistent root/version pair; exact-version reads never substitute current. Save success distinguishes CREATED, UPDATED and UNCHANGED and replays the original result. The actual [Preferences Contract](contracts/candidate/preferences.md) now owns these operations and their detailed error/receipt interfaces. No named SearchProfiles or parallel long-lived configurations are introduced.

**Sources:** Q45/Q55/Q56/Q161 and S17.1 as explicitly revised by [CG02-BC1](design/contract/sl-01-m2-grill.md#cg02-bc1), [CG02-Q6–Q10](design/contract/sl-01-m2-grill.md#cg02-q6) and [CG02-S1](design/contract/sl-01-m2-grill.md#cg02-s1). The former M2 QuickScreen, current-Preference re-screening and CG02-Q2 versioning deferral are superseded.

### 4.3 Local browsing and explicit collection

Collection consumes one exact complete user-confirmed PreferenceSetVersion. It determines source-capable query pushdown and necessary deterministic candidate admission under the Collection/Job Contracts. Unsupported query parameters do not permit silently inventing user intent. Search-result title mismatch alone is not an admission conflict. Source mapping and admission policy are not owned or implemented by M2 Preferences.

Before fetching details, Collection applies its defined deterministic admission checks wherever available list metadata supports them; confirmed rejection prevents detail access and creates no formal Job. Missing or incomparable source information cannot masquerade as a confirmed conflict or satisfaction. Complete validated detail/JD remains necessary for formal Job admission. Rejected listing content is not retained as a recoverable dataset; audit retains admitted operational usage/reasons/failures/risk/stop information. Collection does not parse Requirements. The accepted salary interval comparisons in CG02-Q8 belong to future Collection admission policy, not a Preferences predicate or a standalone QuickScreen.

Normal Job Pool browsing uses saved local data. Initial acquisition after complete configuration and explicit collection/refresh are platform-access entries; merely opening the pool or saving Preferences does not fetch the platform. Every active CollectionRun keeps its original exact PreferenceSetVersion; later saves affect future Runs only. Explicit stop prevents subsequent accesses, preserves committed partial Jobs and causes no automatic restart.

Changing Preferences must not delete or hide existing formal Jobs, add preference-conflict status, change their authority or rewrite their acquisition history. Current Preferences are not a continuing eligibility invariant for RequirementParse, Fit, Preparation, Execution or Application History; those consumers retain their actual source, content, material, permission and safety requirements.

JobPoolViewFilter is independent browsing/query state over existing Jobs. Company/role query, city, batch, industry and update-time filters are examples, not a finalized schema. View filters do not modify Preferences, create PreferenceSetVersion, affect future Collection, delete or mutate Jobs, or generate QuickScreenResult. They may remain frontend state or be carried as backend query parameters; persistence and concrete fields belong to the later query/UI Contract under jobs-screening. No new Company authority or query document is introduced.

**Sources:** Q49/Q161 and S9.1, with [CG02-BC1](design/contract/sl-01-m2-grill.md#cg02-bc1) superseding current-Preference formal-Job filtering while preserving exact collection provenance, complete admission, stop and retention boundaries.

### 4.4 Freshness and availability

The pool distinguishes when content was captured, when a source listing was last reliably observed, and when availability was directly verified. Unchanged content can update observations without creating a new JobVersion. Semantic change creates a new version without rewriting old consumers.

Old data can be stale without being closed. Absence from one search result is not closure. Reliable source evidence of closure blocks new automatic application but retains the Job and history. These freshness/availability meanings apply to formal Jobs, not ManualApplicationEntry. User reports remain distinguishable from direct source verification; formal content eligibility, material readiness and application progress remain separate concerns. [CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1) replaces the former Manual Job UNKNOWN rule.

**Sources:** Q7, Q44, Q48, Q50.

<a id="5-requirements-and-independent-fit-analyses"></a>
<a id="52-what-each-fit-answers"></a>
<a id="53-assessment-meanings-and-scores"></a>
## 5. Requirements and DeepFit

### 5.1 Shared on-demand requirements

Exact JobVersion remains the job-fact authority; RequirementSet is its derived structured requirements. Dependency preparation is explicit bounded work with its own outcome/cost; merely requesting analysis does not establish usable requirements. ManualApplicationEntry is not a formal Job input.

### 5.2 One analysis with separate meanings

DeepFit produces one CandidateJobFitAnalysis, combining Preference Fit, Capability Fit, strengths, gaps and evidence citations. It does not execute parallel CandidateFit and ResumeFit analyses. Freeze exact JobVersion/RequirementSet, the ready default-derived Profile/Evidence pair and the optional exact PreferenceSetVersion. The default is an observation source, not an assertion that the candidate has no other abilities.

Start with the small Profile index, retrieve relevant exact block Evidence, expand to parent entries and more admitted Evidence when needed. No full Resume dump is required at the initial input. A Profile omission or failed retrieval is not a gap. Incomplete/failed/budget-limited inspection is UNKNOWN; a sufficiently inspected negative means only that the source Resume does not express support.

### 5.3 Preference and capability assessment

Keep the existing six Preferences fields; add no work-mode setting. Manual DeepFit works without configured Preferences and reports intent not configured/not assessed, never unlimited or inferred. City/salary/blacklist mismatch does not block manual analysis or contaminate capability findings. Unknown Job fields remain indeterminate. Intent-dependent automatic functions require configuration if separately delivered; this supplement adds none.

Exact score policy, comparison and coverage/result serialization remain the future Fit Contract’s consumed scope. Valid unscored/unknown findings must not be converted into fabricated zero scores, ordinal gaps or total-person judgments.

### 5.4 Execution, compatibility, and failures

New DeepFit requires a ready coherent portrait. Once started with frozen inputs, source Save/default switch does not swap inputs, restart the call or duplicate cost. Preserve original lineage and label historical compatibility honestly. Actual revocation/source unavailability remains separate admission/failure. Multi-Job orchestration keeps per-target outcomes and costs; no batch-wide success inferred from one result.

SL-05.M1 owns single-target DeepFit; SL-05.M2 owns multi-Job/result management. SL-06 instead owns independent optimization. **Provenance:** CG03S1-BC2, Q12–Q17, Q20/Q25/Q26/Q30/Q31; [shared interfaces](contracts/agent/context.md#ctx-016).

<a id="6-job-assistant-and-resume-advisor"></a>
<a id="61-entry-context-and-discussion"></a>
<a id="63-conversation-progress-waiting-and-deletion"></a>
## 6. Job Assistant and Resume Optimization

### 6.1 Entry, context, and suggestions

Generic Optimization improves wording, structure, action orientation, grammar and information density of any explicitly selected saved ResumeVersion. Job-targeted Optimization additionally uses exact JobVersion/RequirementSet to select, order and emphasize supported content. Missing useful quantities are requests for user supplementation, never invented metrics. DeepFit is not a prerequisite or another optimizer.

The candidate context for optimization contains only the selected Resume’s admitted content. Default portrait, another Resume, Memory and conversational career assertions cannot augment it, even as supplementary hints. Thus empty default A does not block optimization of populated B. Empty selected B returns “当前简历没有可供优化的内容，请补充资料” without model invocation.

SL-06.M1/M2 own generic/targeted suggestions; durable ordinary/Job conversations in SL-07.M1/M2 reuse them. Sessions preserve exact selected input and durable user-facing outcomes; streamed fragments are not committed suggestions. Existing typed permissions, bounded invocation, explicit dependency waiting and honest uncertainty remain.

### 6.2 Applying a change to a formal Resume

Current optimization only gives suggestions. It cannot Save, create a new ResumeVersion, switch default or create material demand. Users may manually edit/Save through the ordinary editor. Assistant application and Preparation adopt-back are explicitly deferred at SL-07.M3 and SL-10.M2; their future exact confirmation/concurrency protocols require their own consumed Contract review. If later implemented, application advances the same Resume, with normal default rebuild consequences.

### 6.3 Conversation progress and deletion

A Session has at most one active foreground Turn; new input waits or follows explicit stop. Different Sessions/supporting tasks may execute concurrently. Visible Requirements waiting retains the same bounded foreground Turn and releases model capacity; cancellation/deadline and producer/waiter rules apply. No model polling, inline JD reinterpretation or silent parser takeover is allowed. Deleting a Session cancels active foreground work and blocks its future use, while separately committed business results/history survive.

Discussion, dependency waits, invocation failure and completed suggestions must remain distinguishable. Session deletion and revoked future input prevent new use without undoing separately committed business history. No silent remote replay, hidden formal writes or implicit target inferred from old chats is allowed. This revision does not deliver the deferred Proposal/application workflow.

**Provenance:** CG03S1-BC2, Q14/Q26/Q28/Q29 (option A); [RES-024](contracts/candidate/resumes-grounding.md#res-024).


## 7. Application preparation and materials

### 7.1 Entry and editable preparation

Preparation requires a formal Job and an explicitly selected independent ResumeVersion. The selected document may differ from default and need not derive from it. Exact rendered materials come directly from that document. Default switch, portrait rebuild or another Resume Save cannot replace the selected source or approved material. Preparation is not a Fit/optimization success or external application event.

Each Job/channel has an independent Preparation. Reentry resumes an unfinished instance preserving selected material and manual Greeting, while rechecking eligibility/readiness/approval compatibility; repeated clicks/retries cannot duplicate creation. If multiple instances are resumable, the user chooses. Explicit new preparation or reapplication starts a separate chain. Detect revision conflicts rather than overwriting edits; Preparation does not edit Resume body.

### 7.2 Greeting and material confirmation

Each Preparation starts with one fixed generic, manually editable Greeting, without personalization/model generation or a template/history library. Required rendered material must exist and actually be viewable before confirmation. Greeting changes require reconfirmation; rerendering cannot replace an approved artifact in place. Equal bytes do not waive source/permission/approval checks. Missing or failed required render blocks material readiness without undoing saved Resume content.

Preserve exact viewed-material confirmation: bind the actual inspected artifact and exact Greeting before freezing the application snapshot. Personalized/generated Greeting remains outside current scope. A snapshot alone does not authorize execution; §8’s separate explicit approval and read-back boundary remains. Resume changes require honest new preparation/confirmation rather than silently replacing consented content. Ordinary Preparation is SL-10.M1; Advisor adopt-back (SL-10.M2) is explicitly deferred with SL-07.M3.

**Provenance:** existing viewed-material/execution decisions and CG03S1-BC2/Q14/Q26; [MAT-033](contracts/applications/materials.md#mat-033).

## 8. External execution and application tracking

### 8.1 Frozen material is not execution authorization

An immutable ExecutionSnapshot records the exact intended Job, channel/account, Resume, Greeting, and materials. It answers what will be sent, not whether sending is authorized. MaterialApproval confirms content; a separate explicit, scoped, expiring, single-use ExecutionApproval authorizes external execution. At most one execution Attempt can consume that approval.

Executor uses only the approved frozen inputs. Necessary live target-identity or availability checks remain within the authorization and shared platform safety boundary. They do not silently refresh JobVersion, parse requirements, replace the snapshot, or add model Job analysis. Clear closure, target mismatch, or execution-relevant change stops further actions and explains the need for explicit refresh/repreparation.

Partial continuation needs new narrower authorization. An unverifiable external outcome creates no success event and cannot automatically retry; external-state confirmation is needed. A click, submission gesture, or technical completion alone is not proof of a real application.

**Sources:** Q25, Q30–Q31, Q77, Q150, Q157, Q164.

### 8.2 Batch behavior and shared platform safety

A batch groups interaction and scheduling, not business success or atomicity. Each Job has its own Preparation, snapshot, approval, execution Attempt, and any resulting application record. Bulk confirmation may create separate exact approvals. One task's failure does not rewrite another's outcome. Members not dispatched cannot be shown as failed or applied.

Before every platform access, Collector and Browser Executor share persistent capacity and risk controls for the platform/account. A risk detected by one workflow can block subsequent affected access by the other. This does not share their business authorizations, budgets, or outcomes.

Ordinary page, selector, or browser failure is not automatically account risk. Predictable capacity can recover under policy. Strong risks such as security verification or account restriction require user handling and explicit restoration; they cannot be bypassed through cooldown alone, account/tab switching, or increased concurrency. Restoring safety is not new ExecutionApproval or automatic restart of a stopped operation. Explain the stop and retained completed work.

Platform limits and delays quoted in research are not official guarantees or frozen product defaults. A future Monitor must use the same safety boundary if implemented; this does not add monitoring to v1 scope.

**Sources:** Q36, Q49, Q160–Q161, Q164. Q160 replaces undifferentiated cooldown-based strong-risk recovery in earlier clauses.

### 8.3 Real application history

Technical ExecutionEvents describe actions and observations. ApplicationEvents represent real business facts established through reliable channel read-back or explicit human report. Contact, material sending, formal application, and replies remain distinguishable; no universal channel sequence is implied. Human reporting for a formal Job creates human-reported history without fabricating browser execution, approvals, or snapshots. It does not require prior automated execution. ManualApplicationEntry cannot be its target, and opening an entry URL establishes no application fact ([CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1)).

One ApplicationRecord represents one real application attempt for a Job/channel/account. Reapplication creates a new record. Events are append-only and deduplicated; delayed events retain occurrence and observation distinctions. Corrections and retractions append new events rather than erasing history.

Displayed progress is derived from events under a versioned policy, not another independently editable status. Interviews are initially recorded as structured application events—scheduling, completion, cancellation, feedback, and next-round confirmation—without a separate Interview Aggregate or implied interview-assistant capability.

**Sources:** Q7, Q16–Q17, Q21, Q30–Q31, Q37, Q44, Q48.

## 9. Privacy, controlled execution, and honest recovery

### 9.1 Model visibility and permission

Local availability does not grant model access. Tasks receive only admitted inputs under their scope, privacy, sensitivity, and authorization rules. Contact details, identity numbers, family information, and raw source documents are model-invisible by default, even when they may be displayed or rendered locally. Tool results receive the same admission checks.

Advisor uses typed, permitted business actions. It is not a general Shell, SQL, file, HTTP, or browser agent. A registered capability, generated ID, source document, JD, webpage, Tool result, or Memory entry cannot expand permissions or establish consent. Reads do not conceal platform fetches, parsing, or formal mutations. Formal fact changes and external execution retain their distinct confirmation boundaries.

Saved scope, admitted scope, and what a model actually saw are separate. References alone are not proof of content inspection. Revocation and future-use restrictions apply even when immutable historical records remain readable. Content already sent to a Provider cannot be retracted by local deletion or a switch change.

**Sources:** Q19, Q54, Q72, Q82–Q83, Q94, Q120–Q121, Q126, Q128, Q138–Q139, Q143–Q144, Q172; [Tool Actions](design/harness/tool.md).

### 9.2 Bounded work and recoverable outcomes

Every model task is bounded by its applicable budget, call/step limits, and deadline. Primary work, permitted repair, Context maintenance, and background learning cannot hide additional Provider calls. SDK retry or model fallback cannot silently bypass those controls. Numeric budgets and policies remain later design details.

An interrupted remote call without a complete durable response has uncertain outcome and possible cost. It must not silently replay, count as zero usage, or turn into business success. Explicit Retry starts new bounded work with fresh admission, preserving the prior uncertainty. Releasing a task slot or cancelling local work does not prove the remote call stopped or was refunded.

If a complete response is durably available, local processing can recover without a new model call. If a formal result already committed, recovery preserves it without duplicate assets. Safe regeneration of derived previews is distinct from replaying model calls, platform collection, or external actions.

Partial streamed text is temporary presentation, not a durable Suggestion, completed Turn, Memory source, or proof of Save. It may disappear after refresh and cannot be joined to a Retry's output. Frontend disconnection does not itself cancel a healthy backend; reconnection can retrieve its completed result.

**Sources:** Q116, Q122, Q124–Q125, Q135, Q140–Q142, Q147, Q152, Q156, Q165; [Recovery](design/harness/recovery.md), [Budget](design/harness/budget.md), [Storage](design/harness/storage.md).

### 9.3 Conversation context and retention

Conversation continuity does not mean every past message is sent on every model call. Context Engineering can select and compact eligible history while keeping complete durable Session history. A summary cannot replace protected exact analysis inputs, user authorization, or current task constraints. Context compaction neither creates Long-term Memory nor changes saved business facts.

Formal business history, Session content, collaboration Memory, protected recovery payload, and minimal audit/logging have different purposes and retention. Ordinary logs must not contain secrets or complete sensitive Resume/Evidence/prompt/response payloads. Cleaning payload or chat does not erase independent business history. If exact historical invocation content is unavailable, the product must not imply it can reconstruct it from current facts or a summary. A necessary unavailable source prevents reliable continuation or requires user input; it does not authorize automatic platform revisits or external replay. Exact retention periods and cleanup interfaces remain deferred.

**Sources:** Q47, Q52, Q83, Q125, Q127, Q131–Q132, Q136, Q139, Q141; [Context](design/harness/context.md), [Storage](design/harness/storage.md).

## 10. Collaboration Memory

### 10.1 Scope and authority

Long-term Memory supports cross-session collaboration preferences, feedback, working style, and reusable collaboration learning. It is not another career-fact, search-preference, or application store. Business facts stay with their formal owners; Session-local assertions remain conversational until explicitly saved through their proper workflow.

Current explicit instructions override remembered interaction style for that interaction. A one-off request does not automatically become a durable preference. Neither remembered style nor a request to avoid repetitive confirmation bypasses factual reconciliation, material confirmation, execution approval, or action permissions.

RequirementParse, Profile derivation and DeepFit receive no Long-term Memory, including through summaries or Tools. Advisor may use admitted collaboration preferences, feedback, and working style. Storing reusable learning does not implicitly authorize Advisor to read that category or introduce a General Assistant/interview Skill.

**Sources:** Q127–Q129, Q133, Q138–Q139; [Memory](design/harness/memory.md), sections 3, 4, and 9.

### 10.2 Three independent user controls

| Control | Effect and boundary |
| --- | --- |
| Auto Learning | Controls automatic extraction and publication from eligible new conversation sources; disabling it blocks new learning and late publication under stale permission |
| Recall | Controls whether stored Memory can be read or injected into each subsequent model input, including derived summaries; disabling it takes effect from the next input without deleting entries |
| View/Add/Edit/Delete/Clear All | Explicit management with deterministic validation, independent of both switches and without an extraction model call |

Learning off does not turn Recall off, and Recall off does not disable learning. Neither switch deletes Session continuity or disables ordinary authorized business reads. Reenabling learning does not automatically backfill earlier or disabled-period conversations. New chats do not scan all old Sessions or inherit old temporary Job scopes and Resume selections.

Direct Memory blocks are excluded from Context checkpoints so that Recall controls future admission. v1 does not promise to remove indirect influence already present in actual assistant history or retract earlier transmissions.

**Sources:** Q131–Q132, Q137, Q139, Q145; [Memory](design/harness/memory.md), sections 6, 8, 10, and 13. Q139 controls over earlier combined-switch wording.

### 10.3 Learning, failure, and forgetting

Automatic learning uses eligible completed durable user-facing Turns and independently scheduled background extraction. Sources are minimized to relevant user expression and necessary conversational context, not full Tool, Evidence, webpage, or transcript dumps by default. It does not run unconditionally after every Turn or depend on a reliable Session-ended event. Incomplete streams and extraction output do not recursively trigger learning. It proposes candidates; admission decides whether traceable explicit durable user expression or correction supports them. Assistant guesses, summaries, or repeated behavior alone cannot establish a durable preference. Clear eligible durable expressions need no extra confirmation popup for every Memory entry.

Background extraction has its own budget and yields to foreground capacity. Failure or insufficient budget does not undo a successful user task or charge an arbitrary last conversation Turn. Failed or uncertain source ranges require explicit Retry and do not block later eligible ranges or get silently absorbed into a new batch.

Forgetting stops future admission and removes the entry from valid derived summaries/indexes. Old sources and late extraction cannot automatically recreate it. Older automatic candidates cannot overwrite newer corresponding manual changes. A genuinely later durable user instruction may establish new Memory; manual management is not a permanent topic lock.

Session deletion and Memory forgetting are distinct. Deleting a source Session prevents new extraction or publication from its pending/in-flight ranges but does not delete previously accepted Memory. Already committed business facts remain. Cancellation where possible and truthful usage/audit remain necessary; deletion cannot retract remote transmission or establish zero cost.

**Sources:** Q127–Q131, Q139, Q141, Q145, Q155–Q156, Q169–Q170; [Memory](design/harness/memory.md), sections 6, 7, and 13–15.

## 11. Quality and evidence boundaries

Product quality claims must identify the capability and input scope actually evaluated. User-configured search scope does not establish demonstrated quality for every occupation, city, or source. Structural parsing checks, resolvable citations, and complete input inclusion do not by themselves prove semantic correctness or zero omissions.

[Acceptance](acceptance.md) defines required future evidence for the real task path and its boundaries. Permission bypass, unconfirmed mutation, wrong-target writes, hidden replay, or Candidate-to-Resume evidence leakage cannot be compensated by a good average quality score. Semantic quality, reliability, cost, and latency are separate concerns. Valid unscored analysis and correct business refusal must not be mislabeled as failure or zero quality merely because no numeric score was produced.

Evaluators and observations assess outcomes; they do not decide whether a fact committed, whether execution was authorized, or whether an application happened. Missing evaluation evidence is not a pass. Exact inputs do not guarantee identical remote-model output, and repeated trials do not justify hiding failed attempts behind a best result.

The Architecture and Acceptance drafts own Eval responsibilities and required evidence mapping; concrete Eval interfaces remain Contract work. This document defines no trial count, numerical acceptance threshold, automatic enablement or release policy. Formal annotated ParserVersion certification remains deferred; real-JD tests, manual inspection, and traceable quality work remain required. No implementation or Eval results are asserted by this specification.

**Sources:** Q82, Q117, Q168, Q173–Q180, Q184–Q186, S17.1, S35.1; [Agent Evaluation](design/eval/agent-evaluation.md), especially sections 18–20.

## 12. Non-goals and pending detail

### 12.1 Excluded or deferred product scope

The following are not v1 requirements established by this specification:

- Multiple Candidates, tenants, a unified Candidate Aggregate, or speculative ownership fields: Q53.
- Cross-platform canonical merging or historical Job merge operations: Q12 controls; Q13 is rejected.
- Bookmark/pursuit UX retained merely for compatibility: Q23, S37.1. The explicitly accepted ManualApplicationEntry in section 4.1 is separate current scope ([CG01-BC1](design/contract/sl-01-m1-grill.md#cg01-bc1)).
- Named SearchProfiles and parallel saved search configurations: Q55.
- Competing private Knowledge fact stores, arbitrary historical-version pickers, persistent atomic Assertions or independently editable bullet-level fact authorities (read-only exact-version block Evidence is required). BC3 supersedes the old ban on retained historical Resume bindings and alternate local expression; Q109's rejected Overlay-isolation mechanism is not reinstated.
- Knowledge completeness confirmation, persisted Resume coverage scoring, a joint Fit score, or a mandatory Fit-before-Advisor pipeline: Q24, Q56, Q112–Q113.
- Advisor working drafts, temporary draft export/application, ad hoc chat-file optimization, or implicit application targets inferred from past discussion: Q88, Q108, Q146, Q148–Q149.
- Personalized/generated Greeting, Greeting templates, or a general agent that autonomously performs every job-search capability: Q157, S17.4.
- General Assistant, mock-interview/review Skills, an independent Interview Aggregate, or a required platform Monitor inferred from future examples: Q21, Q127, Q139, Q160, S17.2.
- Unapproved vector/RAG infrastructure or silent overflow retrieval fallback remains deferred. The exact block/entry Evidence Tool is current accepted DeepFit scope under CG03S1-BC3.
- Career USER_FACT Memory, unrestricted historical-chat search, complex Memory graphs/consolidation, automatic historical backfill, or removal of indirect Memory influence from actual assistant messages: Q127–Q132, Q139; Memory design sections 8 and 15.
- Comprehensive physical personal-data erasure, an unsaved ResumeDraft crash-recovery guarantee, old-system import, mandatory legacy migration, or compatibility with old implementation behavior: Q4, Q100, Q131, Q166, S37.1.
- Mandatory offline annotated parser release certification or invented numerical rollout/release gates: Q117, Q175.

These exclusions do not remove accepted immutable history, current-use validation, privacy, explicit authorization, or the requirement to verify actual implementation later.

### 12.2 Details reserved for later work

| Pending matter | Owning follow-up and preserved boundary |
| --- | --- |
| Exact inputs and per-capability prerequisites beyond reviewed Profile/Evidence scope | Future consumer Contract Grill; preserve empty saved states, complete JobVersion admission, and fail-fast task prerequisites without a universal completeness Gate: Q3, Q15, Q44, Q48, Q54, Q154 |
| Identity/reference syntax, schemas, fields/types/enums, API payloads, errors, transitions, and migration/evolution details | Contract Grill after main-document review; preserve accepted authority, exact history, compatibility, and concurrency without treating the inventory as normative: Q2, Q22, Q26, S24.2 |
| Fit target keys, scoring weights/thresholds, score availability, and comparison representation | Contract/ScorePolicy design; preserve single DeepFit and independent optimization, frozen targets, bounded negatives, and valid unscored outcomes: Q46, Q51, Q112, Q115–Q116, Q168 |
| Concrete Proposal/approval representation, lifetime details, channel readiness, render formats, and reliable read-back criteria | Related Contract and channel design; preserve exact preview/consent, actual viewed materials, separate execution authorization, and honest unknown outcomes: Q27, Q30–Q31, Q42, Q148–Q150, Q157, Q164 |
| Full Tool catalog, model admission/redaction details, capacity and budget values, Context/Memory policies, retention periods and cleanup coordination | Architecture boundaries followed by Contract/policy work; preserve least privilege, independent Memory controls, no hidden retries, and honest payload availability: Q19, Q123–Q125, Q132, Q135–Q145, Q169–Q172 |
| Source/adapter verification and actual upstream capabilities | Research before related detailed Contracts; pin commits and inspect licenses, maintenance, and source-to-canonical mapping. Examples are not verified platform guarantees: Q3, Q27, Q31, Q49 |
| Demonstrated quality scope, Trial counts, release thresholds, and default enablement | Acceptance defines evidence; later rollout-policy work resolves policy, without reinstating parser certification: Q117, Q173–Q187, S17.1 |

These are remaining expressions, policies, or explicitly deferred capabilities, not an invitation to reopen the settled Architecture Grill. [Architecture](architecture.md) explains supporting mechanisms and high-level Contract boundaries; [Contract Structure](contracts/structure.md) maintains the planned document organization; [Acceptance](acceptance.md) defines required future proof, and [Development](development.md) defines delivery discipline. [Implementation Plan](plans/implementation-plan.md) owns delivery planning, and [Progress](progress.md) records actual review, readiness and implementation state.

**Sources:** Q22, S24.2, S37.1, S38.1; English document-authoring spec, Further Notes B–E.
