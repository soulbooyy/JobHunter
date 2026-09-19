# SL-01.M1 Contract Grill Decision Register

> English is authoritative. This register records conclusions only, following the structure of the [Architecture Grill Decision Register](../grill-me-design-tree.md). It is a recovery and handoff aid, not a normative Contract, a readiness declaration or implementation evidence.

[Contract design navigation](README.md) · [Milestone plan](../../plans/slices/sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-application-entries) · [Contract Index](../../contracts/index.md) · [Scope readiness ledger](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

Current planning annotation: [CG02-BC1/S1](sl-01-m2-grill.md#cg02-bc1) supersedes this register's source-time placement of pure QuickScreen in M2 and current-Preferences Job filtering. ManualApplicationEntry decisions and all published M1 requirements remain unchanged. M2 now supplies complete immutable acquisition Preferences; SL-08.M2 owns source/admission and independent Job Pool queries.

## Purpose and Authority

Preserve accepted decisions, rationale, effective scope, explicit supersession and formal writeback destinations for SL-01.M1. Do not retain question transcripts, proposed answer options or unaccepted recommendations. This file is the sole working decision record for this milestone, including common rules, module detail and architecture-boundary supersession. Do not create separate per-module decision files.

Product and Architecture own behavior and authority; the Implementation Plan owns delivery scope; actual Contracts own detailed normative definitions; Acceptance owns required proof; Progress owns readiness and evidence. A decision recorded here does not establish any of those artifacts or implementation results by itself.

Keep decision IDs stable. Record supersession explicitly and preserve valid portions of partially replaced decisions. The original architecture register, Inventory and historical handoffs remain unchanged; later user decisions control the identified portions.

## Status Vocabulary

- `ACCEPTED`: adopted for the identified scope; formal writeback/readiness is recorded separately.
- `OPEN`: still requires a decision for an actual consumer.
- `DEFERRED`: postponed to an identified later consumer or scope.
- `SUPERSEDED`: replaced by a later decision; retained here as concise provenance.
- `REJECTED`: explicitly excluded from the applicable design.

A partially superseded decision identifies both the surviving meaning and its replacement. An unanswered or stopped interview item is not an accepted or rejected design decision.

## Session State

- Current milestone: **SL-01.M1 — Local Workspace and Manual Application Entries**.
- Last answered batch: **CG01-Q41–Q45**, all accepted. Q42 permits finite recovery of transaction completion only when the underlying API guarantees safe semantics without re-executing the command; otherwise return `OUTCOME_UNKNOWN`. Q45 specifies final opener/referrer safety properties without fixing the frontend mechanism. CG01-BC1 remains controlling.
- Current precedence: [CG01-BC1](#cg01-bc1) separates mutable ManualApplicationEntry from formal Job/JobVersion. Manual-specific Q2–Q5 portions are superseded; formal completeness and immutable snapshot invariants survive.
- CG01-Q1's [24 common naming/expression rules](#cg01-q1) remain accepted.
- CG01-Q7–Q10 were stopped without adopting their recommendations. Their IDs are not reused; they establish no field, comparison, update or missing-value convention.
- Architecture/plan writeback and scoped review: complete; see [Progress 5](../../progress.md#5-verification-scope-and-next-step).
- Normative writeback: four actual M1 bodies, 69 stable IDs, revision `2026-09-19.M1-r1`; consumed scope is Ready after scoped review. [Progress](../../progress.md#6-sl-01m1-contract-review-and-handoff) owns evidence. No implementation or executed acceptance is claimed.
- Accepted entry detail: seven fields with Q21 text/URL limits; independent intentional duplicates, physical deletion, atomic revision-checked Save, minimal lifetime create receipts and browser-initiation-only outcomes. Update/delete have no durable operation receipts. See [accepted entry fields](#accepted-entry-field-inventory).
- Accepted Workspace/runtime behavior: automatic first initialization, reopening the same storage, explicit failures and a loopback local Web UI with new-tab entry opening; see [Workspace decisions](#cg01-q19). Stable physical placement is owned by [Storage decisions](#cg01-q25), not a multiple-Workspace product.
- Accepted interfaces: Q27 complete create/read/update/delete inputs and results; Q28 full separate list with deterministic ordering; Q29 revision-checked navigation resolution; Q30 structured service failures and separate client outcome uncertainty.
- Current batch: none. The planned interview is complete; all five final decisions and the user's refinements are accepted. Normative consolidation, interface review and readiness evidence follow; acceptance of the decisions is not implementation evidence.
- Next activity: start a development task from the [M1 handoff](../../development/handoff/sl-01-m1-handoff.md), perform actual engineering preparation and implement/verify the bounded scope. No interview question is currently pending.
- Updated: 2026-09-19 HKT.

## Round 1 — Common Expression and the Former Manual Job Boundary

<a id="cg01-q1"></a>

### CG01-Q1 — Shared naming and expression conventions

- **Status:** `ACCEPTED`
- **Decision:** Adopt the user's 24 common rules: PascalCase types, snake_case Contract fields, UPPER_SNAKE_CASE serialized enums, precise identity/version/reference names, distinct concurrency/schema/policy versions, positive predicates, explicit date/time/unit meanings, UTC timestamp boundary conventions, canonical names and explicit language-boundary mapping. Normative strength and stable, non-reusable requirement IDs use explicit supersession.
- **Ownership:** `common.md` defines these rules once. Other Contracts reference them; Contract Structure does not own naming semantics. Naming rules do not require every illustrated field on every object.
- **Rationale:** Consistent shared expression prevents ambiguous versions, duplicate names and unstable requirement references across modules.
- **Formal writeback:** Applicable `common.md` scope and genuine requirement IDs remain pending.

1. Type/object names use `PascalCase`, for example `ResumeVersion`, `EvidenceItemVersion`, and `CandidateJobFitAnalysis`.
2. Contract field names use `snake_case`, for example `resume_id`, `resume_version_id`, and `created_at`.
3. Canonical serialized enum values use `UPPER_SNAKE_CASE`, for example `MATCHED`, `PARTIAL`, `OUTCOME_UNKNOWN`, and `REVIEW_REQUIRED`.
4. Stable business object IDs use `*_id` for logical/stable identity, for example `resume_id`, `evidence_item_id`, and `job_id`.
5. Immutable version object IDs use `*_version_id`, for example `resume_version_id`, `evidence_item_version_id`, and `job_version_id`. Do not use an ambiguous bare `version_id`.
6. Optimistic concurrency tokens use `revision`. This describes mutable-object/persistence-row concurrency, not a business version.
7. Serialization/persisted-structure schema evolution uses `schema_version`, not a business-object or policy version.
8. Policy versions use meaningful `*_policy_version` names, for example `score_policy_version`, `admission_policy_version`, and `context_policy_version`. A bare `policy_version` is allowed only where the object has one unambiguous policy.
9. Avoid a bare ambiguous `version` field. Distinguish immutable object versions, schema versions, policy versions, and concurrency revisions.
10. References preferably use the referenced object's canonical name, for example `resume_version_id` or `requirement_set_id`, rather than `target_id`, `source_id`, or `version_id`. Generic names are reserved for genuinely generic Contract structures.
11. Collection fields use the canonical concept's plural, for example `requirement_ids`, `affected_resume_ids`, or `reason_codes`, without extra type suffixes such as `*_id_list`.
12. Boolean fields use positive predicates, preferably `is_*`, `has_*`, `can_*`, or `requires_*`, for example `is_current`, `has_conflict`, or `requires_confirmation`. Avoid negative predicates and double negatives.
13. State-like meanings preferably use an enum rather than combinations of Boolean flags. For example `status = OUTCOME_UNKNOWN` instead of separate failed/unknown/running flags. This does not join independent domain concerns into one universal lifecycle.
14. Timestamp fields use `*_at`, for example `created_at`, `updated_at`, `confirmed_at`, or `expires_at`.
15. Date-only fields use `*_date`, for example `application_date` or `graduation_date`. Dates and timestamps retain different meanings.
16. Duration and timeout names explicitly carry units, for example `timeout_ms`, `duration_ms`, or `ttl_seconds`, rather than unitless `timeout`, `duration`, or `ttl`.
17. The Contract timestamp boundary format is RFC 3339 UTC. The user's recommended canonical representation uses UTC, a `Z` suffix, and millisecond precision, for example `2026-09-19T06:34:12.381Z`. Internal database representation is an implementation choice. Input coercion/validation details remain to be specified where needed.
18. Each business concept has one canonical name across Contracts; `requirement_set_id` cannot acquire alternate names such as `requirements_id` or `requirement_group_id` for the same concept.
19. Internal code variables may follow language conventions, with explicit Contract-boundary mapping; for example internal TypeScript `resumeVersionId` maps to serialized `resume_version_id`.
20. Normative requirements use standard strength keywords `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY`. Ordinary explanation does not casually use those uppercase keywords.
21. Normative requirements have stable IDs, for example `COM-001`, `WSP-001`, `JOB-001`, and `STO-001`. Moving a heading, section, or paragraph does not change the ID.
22. Published requirement IDs are never reused. Deleted or deprecated requirements retain their reserved numbers; new requirements receive new numbers.
23. Supersession is explicit, for example `WSP-017 is superseded by WSP-031.` Do not change an old ID's core meaning and continue treating it as the same requirement.
24. `common.md` defines these rules once. Other Contracts reference them rather than owning duplicate conventions; `structure.md` does not own naming semantics.

These are naming and expression rules, not a requirement to add every illustrated field or enum to every object. Illustrative business names do not independently establish another milestone's schema. Actual object IDs, timestamp validation, missing-value representation, operation envelopes and real normative ID assignments are still separate detailed-design work.

<a id="cg01-q2"></a>

### CG01-Q2 — Former Manual Job admission

- **Status:** `SUPERSEDED` by CG01-BC1.
- **Historical decision:** A Manual Job previously required nonblank role/company content, allowed absent source URL/JD and could exist as a root without a version; duplicate URLs did not establish identity or trigger merging.
- **Replacement:** ManualApplicationEntry is an independent mutable company/role/application-URL record. The former root-only admission and optional source-URL/JD schema do not define it.
- **Rationale:** A browser-opening entry has no formal Job consumer and does not need a Job admission or version protocol.
- **Formal writeback:** The boundary replacement is recorded in Product 4.1 and Architecture 4.1. Entry field validation remains pending under `jobs/manual-application-entries.md`.
- **Historical detail (superseded):** The old `source_url` denoted opportunity provenance rather than an execution destination; later channel navigation prerequisites were not creation prerequisites. Only a non-blocking duplicate hint was allowed for equal nonempty source URLs. These old ownership/admission rules do not define ManualApplicationEntry.

<a id="cg01-q3"></a>

### CG01-Q3 — Complete canonical JD

- **Status:** `ACCEPTED` for the retained formal Job completeness invariant; the former Manual submission route is `SUPERSEDED` by CG01-BC1.
- **Historical decision:** The former Manual Job route trusted the user's complete-JD submission and applied deterministic legality checks without model-based completeness judgment.
- **Effective boundary:** ManualApplicationEntry supplies no JD or JobVersion. Formal JobVersion continues to require complete exact canonical JD; the actual producer's detailed acquisition/admission rules belong to the formal Job and Collection Contracts. The former manual declaration is not silently transferred to a collector.
- **Rationale:** Removing a producer route does not remove the completeness requirement of the formal asset.
- **Formal writeback:** Product 4.1 and Architecture 4.1 preserve the invariant; detailed `jobs/jobs-screening.md` and `jobs/collection.md` scope remains pending for their actual consumers.
- **Historical qualification:** The former manual declaration authorized no model completeness judgment, fixed descriptive sections, arbitrary length as completeness proof, or additional confirmation field/checkbox. It establishes no such declaration for a future collector.

<a id="cg01-q4"></a>

### CG01-Q4 — Immutable formal Job content

- **Status:** `ACCEPTED` for formal JobVersion snapshots; application to user-maintained Manual records is `SUPERSEDED` by CG01-BC1.
- **Historical decision:** Company, role title and raw JD belonged to the immutable version snapshot after the former Manual Job's first version, rather than independently overwritable root content.
- **Effective boundary:** Formal Job/JobVersion retains immutable canonical snapshots and exact history. ManualApplicationEntry is mutable and creates no business versions. This retained invariant does not finalize the full formal Job schema or its change-comparison algorithm.
- **Rationale:** Formal downstream consumers need exact historical content; the independent entry does not participate in those consumers.
- **Formal writeback:** Architecture 3–4 and the planned `jobs/jobs-screening.md` owner; no immutable entry-version requirement.
- **Historical detail:** The old Manual route allowed root metadata edits before the first version and envisaged a new complete snapshot for changed content, none for identical effective content. Its application to entries is superseded. Formal exact comparison, source-address ownership and invalid/incomplete-update behavior remain with their actual consumers; a current read projection is not a second writable authority.

<a id="cg01-q5"></a>

### CG01-Q5 — Manual availability reporting

- **Status:** `REJECTED` for M1 availability report/correction capability; the former Manual Job UNKNOWN framing is `SUPERSEDED` by CG01-BC1.
- **Decision:** M1 provides no manual availability report/correction subsystem. The user may remove an unwanted entry from current use. The independent entry has no formal Job availability/freshness model.
- **Retained boundary:** Formal Job source observation and availability remain with the actual formal Job/Collection consumers. Formal Job human application reports are separate and remain in scope.
- **Formal writeback:** Product 4, Architecture 4, Acceptance 3 and the revised M1 scope. Q14 subsequently chooses physical entry deletion; remaining command detail is still open.
- **Retained source boundary:** Local capture or edits do not manufacture source verification or imply closure. The formal observation capability survives; the superseded Manual UNKNOWN/history framing creates no current M1 availability obligation.

## Round 2 — Independent Manual Application Entry

<a id="cg01-q6"></a>

### CG01-Q6 — Removal from current use

- **Status:** `ACCEPTED`, scoped by CG01-BC1.
- **Decision:** An unwanted ManualApplicationEntry can be removed from its current view. It has no immutable business versions and never supplies a downstream formal Job target.
- **Supersession:** The former Job root/version retention and downstream selection assumptions do not apply to this independent entry.
- **Later resolution:** Q14 chooses physical business-record deletion without hidden entries, recycle-bin copies or edit history. Detailed commands and coordination remain open; no comprehensive media-erasure interface or restore product is established.
- **Formal writeback:** Revised M1/Product scope; detailed `jobs/manual-application-entries.md` and consumed `foundation/storage.md` requirements remain pending.

<a id="cg01-bc1"></a>

### CG01-BC1 — ManualApplicationEntry outside the formal Job family

- **Status:** `ACCEPTED`; architecture/plan writeback complete, detailed Contracts pending.
- **Rationale:** Keep simple mutable navigation entries independent while preserving formal Job authority and exact history.

#### Accepted boundary

**Decision locator: CG01-BC1.** This locator identifies the later user architecture decision; it is not an original architecture Q/S identifier or a normative requirement ID.

`ManualApplicationEntry` is an independent mutable record outside the formal Job family. It saves a company, role title and user-provided application URL, supports repeated edits and removal from its current view, and opens the browser at that URL only when the user clicks its action. Job Pool offers a button into a separate entry view; these records do not mix with automatically collected Jobs. The product may call this the manual application shortcut entry, while Domain/Contract terminology is `ManualApplicationEntry`.

It creates no Job or JobVersion and participates in no Requirements, DeepFit/Candidate Fit, Resume Fit, Job-targeted Advisor, Preparation, automatic Execution or Application History. Opening a URL is navigation, not an application fact, ExecutionAttempt, approval consumption or evidence of application success. No implicit conversion to a formal Job or hidden collection is introduced.

Formal Job/JobVersion continues to own complete canonical JD/content, immutable snapshots, exact lineage, source identity, observations and downstream eligibility. Its normative definition owner remains `jobs/jobs-screening.md`. Collection is a producer that validates and admits source content under those rules. SL-08.M2 is the first planned producer and integration milestone, not the owner of Job semantics.

At the time of CG01-BC1, detailed entry schema, validation, commands, revision, opening and removal mechanics remained Grill work; later accepted decisions below resolve their identified portions. No immutable entry version history is required. The original acceptance of removal from current use did not reinstate the old Manual Job's version-retention assumptions or establish physical erasure/recovery interfaces.

#### Scoped supersession

| Earlier locator | Superseded portion | Retained meaning |
| --- | --- | --- |
| Q12 | Applying a manual source-platform Job identity to this entry | Formal platform Job source identity and no cross-platform merge |
| Q17, Q44, Q48 | Manual root-only Job, subsequent complete Manual JobVersion, shared Manual/BOSS admission exception, and no-JD Manual tracking | Complete formal JobVersion meaning, immutable exact snapshots, and atomic complete collected Job admission |
| Q50 | Giving this manual entry a Job availability/freshness model, including initial UNKNOWN | Formal Job capture/observation/verification distinctions and honest history |
| CG01-Q2 | Old Manual Job field ownership, optional source URL/JD admission and root-only path | Common naming rules remain; the new entry's business content is company, role title and user-provided application URL. Do not copy its old schema or source/execution URL split automatically |
| CG01-Q3 | User complete-JD submission as a Manual JobVersion production route | Formal Job requires complete exact canonical JD; its actual source-admission detail remains with the formal Job/Collection consumers |
| CG01-Q4 | Immutable snapshots for user-maintained Manual entries | Formal JobVersion retains immutable canonical content snapshots; this decision does not finalize its full schema or comparison algorithm |
| CG01-Q5 | Manual Job UNKNOWN/removal framing | No manual-entry availability report/correction feature; current-view removal remains requested without imposing formal Job history |
| CG01-Q6 | Old root/version retention and downstream selection assumptions applied to this entry | User accepted removal from current use, then explicitly separated the mutable entry from all downstream Job features |
| CG01-Q7–Q10 | Continuation of the old Manual Job interview batch | User stopped these questions; recommendations were not accepted. Generic missing-value rules are still unresolved if a later concrete Contract needs them |

CG01-Q1's 24 common naming/expression rules remain accepted. A mutable object's concurrency `revision` is not an immutable business version. Original architecture sources, Inventory, Chinese authoring reference and historical handoffs retain their source-time text; the current formal owners and traceability record this later decision's precedence.

Human-reported real application facts for a **formal Job** remain in scope. Excluding ManualApplicationEntry from tracking does not delete that Application History capability and does not make automatic execution a prerequisite for a human report.

#### Accepted delivery adjustment

Keep twelve macro Slices and 24 milestones:

- SL-01.M1 delivers local Workspace and ManualApplicationEntry maintenance, separate view and explicit browser opening.
- SL-01.M2 delivers Preferences and the pure metadata QuickScreen component, not a populated formal Job Pool. It does not wait for collection.
- SL-08.M2 implements the first formal Job producer, owned Job persistence/version/read operations, collection and formal local views, including current-Preferences filtering versus frozen collection inputs.
- SL-03.M3, SL-09.M1 and SL-10.M1 consume formal Jobs from SL-08.M2. Fits and Job-targeted Advisor inherit the required producer through RequirementParse; their own independent meanings remain intact.
- Shared invocation infrastructure and ordinary Advisor can proceed without formal Jobs. Only actually implemented local primitives may be reused from M1; entry delivery does not establish immutable Job/reference machinery.

This avoids a cycle between screening and collection. Component fixtures demonstrate component behavior only, not a populated user Job Pool, working collection or user-available formal analysis. Formal data-dependent product paths await their real producer; no test-only Manual ingestion route replaces it.

#### Writeback destinations and evidence

Product owns behavior; Architecture owns authority; the Slice plans own scheduling and completion; `jobs/manual-application-entries.md` is the new planned normative entry owner; `jobs/jobs-screening.md` remains formal Job owner. Contract Structure/Index record organization only. Acceptance and Development retain proof and delivery discipline; Progress records scope readiness separately.

Affected owners: Product 2/4/5/7/8/12; Architecture 2/3/4/8/16; Acceptance 3/7/14; Development 6; Implementation Plan and SL-01/03/08/09/10/11; Contract Structure/Index; Progress and traceability. Existing milestone IDs remain unchanged; changed headings and consumer links are reconciled together.

Writeback and scoped two-seam review are complete; evidence and limits are recorded in [Progress 5](../../progress.md#5-verification-scope-and-next-step). Historical W7 review applies to its earlier baseline, not automatically to this changed scope. No normative body, requirement ID, implementation or executed product acceptance is supplied by this architecture writeback.

## Round 3 — Entry Content and Maintenance

<a id="cg01-q11"></a>

### CG01-Q11 — Required business fields

- **Status:** `ACCEPTED`
- **Decision:** The three business fields are `company_name`, `role_title` and `application_url`. All are required. Company and role title are nonblank after removing leading/trailing whitespace. The application URL is required and validated under Q12.
- **Meaning:** `application_url` is the user-provided browser destination for this independent entry. It is not a formal Execution Target or sending authorization. No JD or formal Job fields are introduced.
- **Later resolution:** Q16 and Q20 define identity, revision and timestamps; Q21 defines text limits. Complete validation/error representation remains open.
- **Formal writeback:** Planned `jobs/manual-application-entries.md`, referencing accepted common naming rules.

<a id="cg01-q12"></a>

### CG01-Q12 — Explicit HTTP(S) URL

- **Status:** `ACCEPTED`
- **Decision:** Accept a valid complete URL with an explicit `http://` or `https://` scheme. Remove leading/trailing whitespace before validation/storage. Preserve its path, query parameters and fragment; do not infer a scheme, strip parameters or replace the address with a guessed standard destination.
- **Boundary:** Saving does not access the network to verify the page or opportunity. Explicit browser opening uses the saved address. Login, ordinary site redirects and the user's subsequent manual application occur in the browser, outside JobHunter's application workflow.
- **Later resolution:** Q21 settles length, host, control-character and credential constraints. Complete validation/error representation remains open; no source acquisition or automated page verification follows from this decision.
- **Formal writeback:** Entry admission and URL-opening scope in `jobs/manual-application-entries.md`.

<a id="cg01-q13"></a>

### CG01-Q13 — Independent intentional duplicates

- **Status:** `ACCEPTED`
- **Decision:** Intentional new entries remain independent even when company, role title or application URL match. None of these content fields is a uniqueness key. No automatic merge or duplicate-warning feature is required in M1.
- **Boundary:** Retrying the same create operation is different from intentionally creating another entry. The operation protocol must handle repeated submission rather than deriving identity from business content.
- **Formal writeback:** Entry identity/create behavior; applicable common operation representation after it is settled.

<a id="cg01-q14"></a>

### CG01-Q14 — Physical business-record deletion

- **Status:** `ACCEPTED`
- **Decision:** Remove an entry by physically deleting its business record. Do not retain a hidden entry, recycle-bin copy or edit/version history. A later deliberate addition is a new entry.
- **Supersession:** Resolves the removal/retention choice left open in CG01-Q6 and CG01-BC1. Formal Job history rules do not apply to this independent record.
- **Boundary:** This is deletion from the application's business storage, not a newly specified comprehensive media/backup erasure mechanism. Any minimal operational receipt required for safe repeated commands must be designed explicitly; it cannot silently retain a deleted entry's content or become a hidden entry/history store.
- **Later resolution:** Q16 requires revision-checked deletion; Q17/Q22 define minimum create-request receipts, retention and replay after deletion; Q23 defines delete retry behavior. Remaining command/result representation is open.
- **Formal writeback:** `jobs/manual-application-entries.md` and its consumed `foundation/storage.md` deletion/retention scope.

<a id="cg01-q15"></a>

### CG01-Q15 — Explicit whole-record Save

- **Status:** `ACCEPTED`
- **Decision:** Editing requires an explicit Save. The three business fields form one complete update, validated and persisted atomically. Only successful validation and persistence change the saved current record.
- **Boundary:** Unsaved input does not change the list or the saved URL used by the open action. A failed Save preserves input in the current editor and leaves the prior saved record unchanged. No per-field autosave or immutable business versions are introduced.
- **Later resolution:** Q16 defines revision checking and increments only on actual content changes; Q20 leaves modification time unchanged for no-op saves; Q23 resolves update retry behavior. Full command payloads/results remain open. Keeping failed input in the editor does not establish crash-recoverable drafts.
- **Formal writeback:** Entry update protocol and storage atomicity, after the outstanding interface decisions are resolved.

## Round 4 — Concurrency, Replay, Initialization and Time

<a id="cg01-q16"></a>

### CG01-Q16 — Stable entry identity and revision

- **Status:** `ACCEPTED`
- **Decision:** `manual_application_entry_id` is a system-generated unique string without company, role or URL meaning; it stays unchanged after creation. `revision` is an integer starting at `1`, incremented when actual content changes, not an immutable business version.
- **Mutation admission:** Update and delete carry the revision read by the caller. A mismatch rejects the operation and surfaces a conflict while preserving current edit input. A deleted/missing record returns not-found; update cannot recreate it.
- **Later resolution:** Q27 settles logical inputs/results, Q30 the minimum service error object, Q31 ID/revision representation and Q34 mutation admission order.
- **Formal writeback:** Entry identity/write admission, common revision interpretation and storage atomic compare-and-write/delete guarantees.

<a id="cg01-q17"></a>

### CG01-Q17 — Create request identity

- **Status:** `ACCEPTED`
- **Decision:** Create carries an independent `request_id`. Retries of one creation reuse it; intentional new creation uses another ID. Same ID and same content resolve the original creation outcome without adding a record; the same ID with different content is a request conflict.
- **Deletion boundary:** An old create retry cannot recreate an entry after physical deletion. Keep only the minimum operational receipt needed to recognize the processed request, without a deleted company's name, role title or URL copy. The receipt is not an entry, version history or application fact.
- **Later resolution:** Q22 settles minimum receipt contents, identity-only replay, lifetime retention and transaction coupling; Q36 specifies fingerprint representation. Q23 limits durable operation receipts to create.
- **Formal writeback:** Entry create protocol and applicable storage/common request identity scope.

<a id="cg01-q18"></a>

### CG01-Q18 — Observable browser initiation only

- **Status:** `ACCEPTED`
- **Decision:** Report only that browser opening was initiated or could not be initiated. Do not claim the target page is accessible, loaded successfully, or that an application occurred.
- **Effects:** Opening changes no entry content and adds no click count, last-opened timestamp or application state. Failure preserves the entry and is shown to the user; there is no automatic background retry. Each new explicit click may initiate another opening.
- **Later resolution:** Q24 selects a local Web UI and new-tab handoff; Q29 defines revision-checked URL resolution. The implementation must support truthful reporting of its observable initiation outcome; concrete browser integration remains implementation preparation and Contract work.
- **Formal writeback:** Entry opening boundary and corresponding proof; no Executor or Application History interface is introduced.

<a id="cg01-q19"></a>

### CG01-Q19 — Default local Workspace

- **Status:** `ACCEPTED`
- **Decision:** Initialize the default local Workspace automatically on first use, then reopen that same Workspace. ManualApplicationEntry maintenance does not require Profile, a Resume or Preferences to be configured first.
- **Failure boundary:** Corrupt, unreadable or unwritable existing storage produces an explicit failure. Do not silently substitute/recreate an empty Workspace and report successful initialization.
- **Later resolution:** Q24 selects the local Web runtime form; [Q25](#cg01-q25) settles stable placement/configuration under storage ownership; Q26 defines first-use eligibility and the nonempty-directory failure boundary. Storage recognition representation and initialization/open results remain open.
- **Formal writeback:** `foundation/workspace.md`, consumed `foundation/storage.md` initialization/durability guarantees and the actual implementation-preparation instructions when verified.

<a id="cg01-q20"></a>

### CG01-Q20 — Consumer-driven creation/modification times

- **Status:** `ACCEPTED`, with the user's consumer-driven scope clarification.
- **Decision:** The entry has system-maintained, read-only `created_at` and `updated_at`. Successful creation sets both to the same creation time. `created_at` never changes; an actual successfully saved content change updates `updated_at`. Saving identical effective content or opening the browser does not refresh it. The list defaults to descending last-modification time.
- **Representation:** Use Q1's accepted UTC timestamp boundary convention. Q28 subsequently settles deterministic tie-breaking and the complete unpaginated list response.
- **Shared scope:** A mutable business record uses these fields when real consumers need creation and last-modification times. Immutable objects, version objects and events do not mechanically acquire `updated_at`. This is not a mandate for identical columns on every persistence table.
- **Formal writeback:** Entry fields/list semantics; shared applicability in `common.md`, with specific timestamp consumers kept in their owning Contract.

## Round 5 — Validation, Receipt Lifetime and Local Runtime

<a id="cg01-q21"></a>

### CG01-Q21 — Business content validation limits

- **Status:** `ACCEPTED`
- **Decision:** After outer whitespace trimming, `company_name` and `role_title` each contain 1–200 Unicode code points, on one line and without control characters. Preserve internal spaces, case and punctuation.
- **URL validation:** After outer trimming, `application_url` contains at most 8192 Unicode code points, has an explicit HTTP(S) scheme and valid host, and contains neither control characters nor embedded username/password credentials. Preserve path, query and fragment under Q12.
- **Failure boundary:** Reject invalid or oversized input; never silently truncate it. Saving still performs no network validation.
- **Later resolution:** Q32 settles fixed trim membership, control/line-separator handling and exact effective-content comparison; Q30/Q35 settle the service error object and HTTP mapping. Field-level codes remain open.
- **Formal writeback:** Entry field constraints, coordinated with consumed common text representation.

<a id="cg01-q22"></a>

### CG01-Q22 — Minimal create receipts for the Workspace lifetime

- **Status:** `ACCEPTED`
- **Decision:** Retain only the create `request_id`, an input-content fingerprint and the original `manual_application_entry_id`. Do not copy company, role title or URL into the receipt. Q36 subsequently defines fingerprint naming, encoding and algorithm.
- **Atomicity and retention:** Only successful creation writes a receipt, in the same transaction as the entry. Retain it for the Workspace lifetime; M1 has no automatic expiration.
- **Replay result:** Replaying the same request/content returns the original creation identity, not an original mutable-content snapshot. Read current entry content separately. If the original entry was deleted, report that fact without recreating it. Changed content under the same request ID remains a request conflict under Q17.
- **Rationale:** Lost create responses must not produce duplicate or resurrected records, while physical deletion must not leave a hidden business record.
- **Formal writeback:** Entry create/replay interface and the corresponding atomicity/retention scope of `foundation/storage.md`.

<a id="cg01-q23"></a>

### CG01-Q23 — No update/delete operation ledger

- **Status:** `ACCEPTED`
- **Decision:** Durable operation receipts apply only to create. Update/delete use entry identity and the caller-read `revision`. Repeating an update with a revision made stale by a successful change returns conflict; repeating deletion after the entry is gone returns not-found.
- **Unknown response:** A lost response requires checking the current record/outcome. Do not report definite failure solely from the missing response or automatically retry using a newly fetched revision. Current reads do not prove every intervening operation's history.
- **No-op compatibility:** Q16/Q20 still apply: a save with unchanged effective content does not advance revision or timestamps; no receipt is added to force otherwise.
- **Rationale:** Existing revision admission is sufficient for these mutations without an additional command-history subsystem.
- **Formal writeback:** Entry update/delete errors and client recovery, with atomic storage admission.

<a id="cg01-q24"></a>

### CG01-Q24 — Local Web interaction boundary

- **Status:** `ACCEPTED`
- **Decision:** M1 runs as a local backend service with a browser frontend. By default the service is available only on the local machine through loopback. An explicit entry-opening click opens the saved application URL in a new browser tab.
- **Boundary:** Browser handoff retains Q18's initiation-only meaning and produces no application fact. This runtime selection does not choose framework versions, an API protocol or startup scripts.
- **Rationale:** Give the local Workspace a concrete interaction boundary without introducing desktop packaging or remote deployment requirements.
- **Open detail:** Concrete read/command/error and opening interfaces; verified tooling and startup instructions during implementation preparation.
- **Formal writeback:** Applicable Workspace/runtime/navigation scope, entry opening agreement and Development setup. Storage placement is owned separately by [Q25](#cg01-q25).

<a id="cg01-q25"></a>

### CG01-Q25 — Physical data placement, not Workspace identity

- **Status:** `ACCEPTED`, with the user's explicit configuration and ownership clarification.
- **Decision:** M1 uses a stable default local `data_directory` independent of the source checkout and process working directory. Startup configuration may explicitly select its location. Resolve and fix the directory at startup; do not switch it during a run.
- **Explicit-path failure:** If the explicitly configured directory does not exist, is unreadable or is unwritable, fail startup clearly. Do not silently fall back, create the missing configured directory, or create another empty data store elsewhere.
- **Default initialization:** Q19's automatic first-use initialization remains applicable to the default location. Q26 subsequently defines eligibility without fixing storage recognition metadata.
- **Ownership:** `data_directory` is storage/infrastructure configuration that determines physical placement. It is not a Workspace identity field or an additional product Workspace. M1 remains single-user with one default Workspace and no create/switch/manage-multiple-Workspaces UI.
- **Rationale:** Restart behavior must not change with the checkout or launch directory; configuration failure must not masquerade as empty user data.
- **Later resolution:** Q26 settles first-use semantics, Q33 selects recognition metadata and M1 format compatibility, and Q38 defines startup diagnostics. Actual default OS path and configuration wiring belong to implementation preparation under this boundary.
- **Formal writeback:** `foundation/storage.md` owns placement/startup guarantees. `foundation/workspace.md` references them for initialization; Development records the verified runtime configuration.

## Round 6 — Initialization Admission and Consumed Interfaces

<a id="cg01-q26"></a>

### CG01-Q26 — First-use eligibility and storage recognition ownership

- **Status:** `ACCEPTED`, with the user's ownership and representation clarification.
- **Decision:** A missing default `data_directory` may be created and initialized. An explicitly configured missing directory fails under Q25. An existing selected directory that is completely empty is eligible for first initialization.
- **Nonempty directory:** Never infer first use merely because the database was not found. Open only recognized, complete and compatible JobHunter storage. Missing required files, corruption, unsupported schema and interrupted-initialization residue produce explicit failure; do not overwrite or construct a replacement database.
- **Known limit:** If the user manually empties the entire directory, its former existence cannot be inferred. The now-empty directory is treated as first use.
- **Ownership:** `foundation/workspace.md` owns first-initialization semantics; `foundation/storage.md` owns recognizable/supported storage and opening failures. Q26 did not fix concrete recognition metadata; Q33 subsequently chooses its representation.
- **Rationale:** Distinguish eligible empty storage from an unknown or broken existing store without claiming historical knowledge the application does not have.
- **Formal writeback:** Workspace initialization referencing Storage recognition/compatibility/failure scope; implementation preparation verifies the actual startup path.

<a id="cg01-q27"></a>

### CG01-Q27 — Minimal complete read/write operations

- **Status:** `ACCEPTED`
- **Decision:** Use the logical inputs and successful results below. Q35 subsequently maps these to HTTP.

| Operation | Input | Successful result |
| --- | --- | --- |
| Create | `request_id`, `company_name`, `role_title`, `application_url` | `manual_application_entry_id`; read current content separately |
| Read one | `manual_application_entry_id` | Complete seven-field entry |
| Update | `manual_application_entry_id`, caller-read `revision`, all three business fields | Complete saved seven-field entry |
| Delete | `manual_application_entry_id`, caller-read `revision` | Deleted `manual_application_entry_id` |

- **Admission:** Create/update require complete business fields; no partial PATCH operation. Reject unknown fields, wrong types and attempts to set system-owned fields rather than silently ignoring or coercing them. Update `revision` is the expected concurrency token, not a user-assigned next value.
- **Rationale:** Keep the UI and storage boundary explicit while preserving whole-record atomic Save and identity-only create replay.
- **Formal writeback:** `jobs/manual-application-entries.md` operation representations, common consumed types and coordinated storage commands.

<a id="cg01-q28"></a>

### CG01-Q28 — Complete separate list and deterministic ordering

- **Status:** `ACCEPTED`
- **Decision:** Return every ManualApplicationEntry in one `items` collection, each with all seven fields. An empty list returns `items: []`. Sort by `updated_at` descending, then `manual_application_entry_id` string ascending for ties.
- **Scope:** M1 supplies no pagination, search, filters or caller-selectable ordering, and never silently truncates results. Formal Jobs are excluded from this list.
- **Rationale:** Provide the actual small local entry consumer with one complete, predictable read interface.
- **Formal writeback:** Entry read Contract and Workspace's separate entry view; no formal Job read scope is completed.

<a id="cg01-q29"></a>

### CG01-Q29 — Revision-checked browser destination resolution

- **Status:** `ACCEPTED`
- **Decision:** The open action supplies `manual_application_entry_id` and the revision displayed by the caller. If the stored entry exists with that revision, resolve its saved `application_url` for the frontend's new-tab handoff. A changed revision requires refresh and a new explicit click; a missing entry returns not-found. Do not open a different unseen destination or use stale cached content after failed validation.
- **Effects and race boundary:** Resolution changes no record and holds no database transaction across browser activity. Updates/deletion after successful resolution do not recall navigation already initiated. This is a bounded read check, not an Execution lease or application fact.
- **Rationale:** The explicit click refers to the entry state the user saw, while browser navigation remains outside authority transactions.
- **Formal writeback:** Entry resolution input/result and error agreement, Workspace/UI handoff and atomic storage read consistency.

<a id="cg01-q30"></a>

### CG01-Q30 — Structured failures and client uncertainty

- **Status:** `ACCEPTED`
- **Decision:** Service errors contain stable enum `code`, human-readable `message`, and a `field_errors` collection whose items contain `field` and `code`. Use `field_errors: []` when no field-specific errors exist. Programs branch on codes, not message wording; errors do not echo user input.
- **Service codes:** The M1 minimum is `VALIDATION_ERROR`, `NOT_FOUND`, `REVISION_CONFLICT`, `REQUEST_CONFLICT`, `ORIGINAL_ENTRY_DELETED`, and `STORAGE_UNAVAILABLE`. Q35 settles their transport mapping; Q37 adds field codes, malformed-request, exhausted-revision and unexpected-error representation.
- **Deleted originals:** `ORIGINAL_ENTRY_DELETED` applies to replay of a creation whose original entry has since been deleted. Ordinary read/update/delete on missing records uses `NOT_FOUND`.
- **Client boundary:** Browser initiation failure is reported separately by the frontend. A timeout or lost response means outcome requires confirmation, not a server-confirmed failure. These client outcomes do not create a persisted business status or universal project error vocabulary.
- **Rationale:** Give the UI deterministic recovery signals while retaining truthful distinctions between known service rejection and an unobserved result.
- **Formal writeback:** Common consumed error structure and entry-owned codes/recovery, with Storage failures mapped at the application boundary.

## Round 7 — Canonical Representation and HTTP Mapping

<a id="cg01-q31"></a>

### CG01-Q31 — UUID identity and bounded revision representation

- **Status:** `ACCEPTED`
- **Decision:** The backend generates `manual_application_entry_id` as UUIDv4. The frontend generates an independent UUIDv4 `request_id` for a new create intent, reuses it for retries and generates another for a deliberate new creation. Both use lowercase, hyphenated 36-character boundary representations. Reject alternate representations rather than silently correcting them.
- **Revision:** A JSON integer from `1` through `9007199254740991`, excluding strings and Booleans. Increment cannot wrap; exhaustion explicitly rejects modification under Q37's `REVISION_EXHAUSTED` code. A valid no-op at the maximum remains allowed.
- **Scope:** These are M1-consumed representations, not a requirement that every future object family adopt this ID format. UUID format follows [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.4).
- **Formal writeback:** Common consumed identifier/revision types, entry generation and command admission, coordinated storage constraints.

<a id="cg01-q32"></a>

### CG01-Q32 — Fixed trim semantics and exact content comparison

- **Status:** `ACCEPTED`, with the user's stable-standard and absolute-URL refinements.
- **Decision:** Use a fixed trim character set defined once by `common.md`; never inherit a moving Unicode latest release or language-default trim behavior. Record the accepted White_Space set explicitly: `U+0009–U+000D`, `U+0020`, `U+0085`, `U+00A0`, `U+1680`, `U+2000–U+200A`, `U+2028`, `U+2029`, `U+202F`, `U+205F`, `U+3000`. This enumeration, not an external latest URL, controls membership.
- **Text processing:** Reject invalid Unicode text, including unpaired surrogates. Trim only leading/trailing members of the fixed set, then enforce length and remaining control-character restrictions. Control characters are `U+0000–U+001F` and `U+007F–U+009F`; company/role content also rejects internal line/paragraph separators `U+2028`/`U+2029`. No case folding, Unicode normalization, internal-space collapse or fullwidth/halfwidth conversion.
- **URL admission:** Require an absolute URL with scheme `http` or `https` and Q21's valid-host/no-credentials rules. Reject other schemes, including `javascript:`, `file:` and `data:`. After outer trim, reject remaining internal whitespace and backslashes; do not automatically repair, infer, normalize or rewrite the URL. Preserve path/query/fragment under Q12.
- **Equality:** Compare all three admitted field values exactly. The same effective-content semantics govern no-op updates and create-request content comparison. For example, outer spaces alone do not change `Acme`, but `ACME` remains different from `Acme`.
- **Ownership:** `common.md` owns the fixed text primitives; entry-specific length, single-line, URL and equality rules remain with `jobs/manual-application-entries.md`.
- **Formal writeback:** Common text representation, entry deterministic admission/comparison and create fingerprint input agreement.

<a id="cg01-q33"></a>

### CG01-Q33 — Minimal SQLite storage recognition

- **Status:** `ACCEPTED`
- **Decision:** Use the primary database `jobhunter.sqlite3`, without a separate manifest. SQLite `application_id` is `0x4A484E54`; the application-owned storage `schema_version` maps to SQLite `user_version`, with M1 value `1`. Do not use SQLite's internal `schema_version` as the product format version.
- **Initialization:** Required tables/constraints and recognition metadata become initialized together in one successfully committed transaction. Existing-store opening checks application identity, supported version, required structure and integrity. Failure does not run repair-by-table-creation, create another database or automatically upgrade the format.
- **Recovery:** Allow normal SQLite journal/WAL recovery before checking the resulting store. Sidecar presence alone is not evidence of incomplete initialization and does not authorize deletion. Missing initialization identity or required structures after recovery fails opening. One primary database does not mean SQLite can never maintain auxiliary files.
- **Basis:** [SQLite application metadata](https://www.sqlite.org/pragma.html#pragma_application_id), [user version](https://www.sqlite.org/pragma.html#pragma_user_version), [atomic recovery](https://www.sqlite.org/atomiccommit.html#rollback) and [WAL](https://www.sqlite.org/wal.html#the_wal_file).
- **Formal writeback:** Storage-owned layout/recognition/version/initialization requirements referenced by Workspace. Q38 subsequently defines startup diagnostics; exact required table/constraint definitions remain to be completed.

<a id="cg01-q34"></a>

### CG01-Q34 — Mutation admission before no-op comparison

- **Status:** `ACCEPTED`
- **Decision:** Update first validates request structure, types and business fields; then checks existence (`NOT_FOUND` if absent), then expected revision (`REVISION_CONFLICT` if stale), and only then compares content. Equal content returns the original record unchanged; changed content commits atomically with its revision/timestamp update.
- **Concurrency boundary:** A stale revision conflicts even if supplied content equals the current record. Delete and URL resolution also check existence before revision. Storage guarantees consistent read/check/write admission; a separate unlocked read followed by an unconditional write is insufficient.
- **Rationale:** No-op handling cannot bypass the caller's concurrency token or overwrite another editor's work.
- **Formal writeback:** Entry command/result precedence, coordinated storage compare-and-write/delete and read-resolution guarantees.

<a id="cg01-q35"></a>

### CG01-Q35 — Versioned local HTTP interface

- **Status:** `ACCEPTED`, with the user's project API-prefix correction.
- **Decision:** Use JSON at base path `/api/v1/manual-application-entries`, following the user's existing `/api/v1/...` convention. The earlier unversioned `/api/manual-application-entries` proposal is not adopted.

| Operation | HTTP method and path relative to the base | Body / result agreement |
| --- | --- | --- |
| Create | `POST` base | Q27 create body; identity result |
| List | `GET` base | Q28 `items` result |
| Read one | `GET /{manual_application_entry_id}` | Complete entry |
| Update | `PUT /{manual_application_entry_id}` | Expected `revision` and three business fields; saved entry result |
| Delete | `POST /{manual_application_entry_id}/delete` | Expected `revision`; deleted identity result |
| Resolve browser destination | `POST /{manual_application_entry_id}/resolve-url` | Expected `revision`; `application_url` result |

- **Representation:** Do not duplicate path identity in the body. Delete/resolve bodies contain only `revision`. Resolution returns the saved address for frontend browser handoff, not server navigation.
- **Success:** All these successful operations use HTTP `200` with their agreed result; create is not required to return `201`.
- **Failures:** Malformed JSON uses `400`; field validation `422`; missing entry `404`; revision/request conflict and replay of an original deleted entry `409`; storage unavailable `503`. Use Q30's structured error object.
- **Rationale:** Keep the project's versioned API style, avoid a DELETE-body dependency and express revision-checked destination resolution as a command. API path versioning is distinct from storage schema versioning.
- **Formal writeback:** Entry-owned transport mapping referencing common representation/error conventions; no new parallel API prefix or Contract owner.

## Round 8 — Receipt Encoding, Diagnostics and Uncertain Outcomes

<a id="cg01-q36"></a>

### CG01-Q36 — Precisely framed create fingerprint

- **Status:** `ACCEPTED`, with the user's byte-length and idempotency-key clarification.
- **Decision:** A minimum create receipt has `request_id` (UUIDv4 primary key), `request_fingerprint` (SHA-256 digest, 64 lowercase hexadecimal characters) and the original `manual_application_entry_id` (UUIDv4). No original business-text copy is retained.
- **Fingerprint input:** Begin with the exact UTF-8/ASCII bytes of `ManualApplicationEntryCreate:v1`, then one zero byte (`0x00`). Append Q32-admitted `company_name`, `role_title`, `application_url` in that order. Encode each value as UTF-8 and precede its bytes with its byte length as a four-byte unsigned big-endian integer. Hash the resulting bytes. Length means UTF-8 byte count, not Unicode code points, UTF-16 units or displayed characters.
- **Excluded input:** `request_id` is the idempotency key and is not part of the fingerprint. Entry identity, revision and timestamps are not part of the three-field content fingerprint.
- **Persistence:** Create commits entry and receipt together. No relationship may cascade receipt deletion when its original entry is physically removed. Treat retained digests as local private data; a digest is not a recoverable content copy or an anonymity guarantee.
- **Formal writeback:** Entry-owned replay/content agreement, Storage receipt representation/atomicity/retention and common consumed digest representation.

<a id="cg01-q37"></a>

### CG01-Q37 — Field error vocabulary and remaining service failures

- **Status:** `ACCEPTED`, with the user's missing-versus-null clarification.
- **Decision:** Use the following field-level codes with Q30's error structure.

| Field code | Meaning |
| --- | --- |
| `REQUIRED` | Required field is absent |
| `UNKNOWN_FIELD` | Field is not accepted by this operation, including attempts to set system-owned fields |
| `INVALID_TYPE` | Wrong type; explicit `null` for a required string/integer belongs here, not under `REQUIRED` |
| `BLANK_VALUE` | Text is empty after the accepted outer trim |
| `TOO_LONG` | Text exceeds its code-point limit |
| `INVALID_CHARACTERS` | Invalid Unicode, controls or forbidden characters |
| `INVALID_FORMAT` | UUID or URL does not satisfy its required format |
| `OUT_OF_RANGE` | Revision is outside the admitted range |

- **Additional service codes:** `BAD_REQUEST` for unparseable JSON (400); `REVISION_EXHAUSTED` for an actual content change at maximum revision (409); `INTERNAL_ERROR` for an unexpected failure (500). A valid no-op at maximum revision remains successful under Q34.
- **Privacy:** Error messages do not expose submitted business text, SQL or stack traces. Q40 distinguishes known rejection from uncertain commit rather than treating HTTP error status alone as proof that no write occurred.
- **Formal writeback:** Common consumed field-error representation and entry-specific validation/status mapping. This does not predefine all future modules' error enums.

<a id="cg01-q38"></a>

### CG01-Q38 — Startup diagnostics outside business resources

- **Status:** `ACCEPTED`, with the user's diagnostic-only and pre-listen clarification.
- **Decision:** Successful initialization/opening emits `LocalStartupResult` with `outcome` (`INITIALIZED` or `OPENED`), the run's fixed absolute `data_directory`, and actual storage `schema_version` (M1: `1`).
- **Boundary:** This is startup/infrastructure diagnostics only. Do not persist it or expose it as an HTTP business resource; it adds no Workspace identity field or initialization HTTP endpoint. Workspace owns first-use semantics; Storage/startup owns physical information and diagnostic representation.
- **Failure vocabulary:** Structured startup errors distinguish `DATA_DIRECTORY_UNAVAILABLE`, `STORAGE_NOT_RECOGNIZED`, `SCHEMA_UNSUPPORTED`, `STORAGE_CORRUPT`, `INITIALIZATION_FAILED` and `STORAGE_UNAVAILABLE` using the common error shape.
- **Admission:** Finish initialization/recognition checks successfully before listening for or accepting business requests. On startup failure, exit with nonzero status; no fallback empty data store or falsely ready service.
- **Formal writeback:** Workspace startup sequencing, Storage/startup results and failures, and verified Development launch diagnostics.

<a id="cg01-q39"></a>

### CG01-Q39 — Nondecreasing per-entry modification time

- **Status:** `ACCEPTED`, including the user's explicit cross-record ordering limit.
- **Decision:** Creation sets `created_at` and `updated_at` to the same system UTC millisecond value. For a real committed change, set `updated_at = max(now, old_updated_at)`. Same-millisecond changes may have equal timestamps; revision orders changes to that entry. No-op and opening behavior remain unchanged.
- **Clock boundary:** Do not fabricate a one-millisecond increment or block editing because the clock moved backwards. Do not introduce a logical clock. Cross-record timestamps during clock rollback cannot strictly express real modification order; Q28's deterministic timestamp/ID ordering remains in force.
- **Scope:** This policy applies to ManualApplicationEntry, not automatically every future timestamp consumer.
- **Formal writeback:** Entry field/update/list semantics and atomic persistence of the chosen timestamp with its revision/content.

<a id="cg01-q40"></a>

### CG01-Q40 — Client recovery for uncertain writes

- **Status:** `ACCEPTED`, with the user's commit-aware uncertainty refinement.
- **Decision:** Timeout, connection loss, and 5xx failures for which commit cannot be determined enter pending verification. A definite 4xx Contract rejection is not outcome unknown. Do not infer rollback from an error status or missing response; conversely, a known rejection need not be mislabeled uncertain.
- **Create recovery:** Retain the submitted `request_id` and exact submitted content in current-page memory. An explicit verify/retry action replays that same request; do not generate another ID for the uncertain original creation.
- **Update/delete recovery:** Read current state for the user to inspect. Do not automatically fetch a fresh revision and resubmit the mutation. Current state does not reconstruct every intervening operation, and verification does not overwrite unsaved editor content.
- **Lifetime:** M1 adds no persistent command queue or cross-refresh/browser-restart recovery. If page state is lost, prompt inspection of the list rather than automatically creating another record.
- **Formal writeback:** Entry client recovery and error interpretation, UI state lifetime and persistence failure agreement. Pending verification is not a persisted entry/application status.

## Round 9 — Persistence, Runtime and Browser Closure

<a id="cg01-q41"></a>

### CG01-Q41 — Two application tables and independent receipts

- **Status:** `ACCEPTED`
- **Decision:** `manual_application_entries` stores the seven accepted fields, all non-null, with entry ID as primary key; revision is INTEGER and other fields are TEXT, including canonical UTC millisecond timestamps. `manual_application_entry_create_receipts` stores the three accepted non-null TEXT fields, with request ID as primary key and original entry ID unique to prevent reuse of historical identity.
- **Constraints:** Enforce directly representable length, revision-range and `updated_at >= created_at` invariants in storage. Application admission still owns complete text/URL validation. Company, role, URL and fingerprint are not unique. No receipt foreign key may block entry deletion, cascade receipt deletion or clear its original identity.
- **Boundary:** Alembic may maintain technical version metadata; two application tables does not mean exactly two physical tables. M1 adds no Workspace business table, click table or immutable entry-version table.
- **Formal writeback:** Storage table/constraint scope referencing Entry/Common field semantics.

<a id="cg01-q42"></a>

### CG01-Q42 — Durable acknowledgement and bounded transaction recovery

- **Status:** `ACCEPTED`, with the user's safe-recovery qualification.
- **Decision:** A mutation succeeds only after confirmed transaction commit. Entry creation and receipt commit together; changed content/revision/timestamp commit together; deletion is atomic. Confirmed non-commit/rollback on storage failure uses `STORAGE_UNAVAILABLE`; uncertain commit uses command outcome `OUTCOME_UNKNOWN`, HTTP 503, and Q40 verification.
- **Recovery boundary:** Storage implementation may attempt finite recovery of the same transaction completion only when the underlying API guarantees safe retry semantics and no re-execution of the business command. Otherwise report `OUTCOME_UNKNOWN`. This is permission under a proved condition, not a requirement to repeat `COMMIT` after an ambiguous result.
- **Domain boundary:** `OUTCOME_UNKNOWN` is a command outcome, never an Entry status/state machine or application fact.
- **Durability scope:** Proper durable SQLite transactions cover process crash and power-loss recovery on supported, correctly functioning local storage. Hardware damage, manual file deletion and devices falsely reporting durable flush are outside that guarantee. Concrete settings and fault verification belong to implementation preparation.
- **Formal writeback:** Storage commit/failure guarantees and Entry/Common operation-error agreement.

<a id="cg01-q43"></a>

### CG01-Q43 — One backend owner per selected data directory

- **Status:** `ACCEPTED`
- **Decision:** Acquire exclusive runtime ownership of the resolved data directory before initialization/opening and hold it until exit. Another backend targeting it fails startup with `DATA_DIRECTORY_IN_USE`; it does not select another directory or empty store. Multiple browser pages remain allowed under revision admission.
- **Recovery:** Ownership can be reacquired after process death. A leftover filename/PID alone does not prove a live owner. Lock coordination must not contaminate Q26's empty-directory recognition.
- **Boundary:** OS/library lock selection is implementation preparation; this adds no multiple-Workspace management UI.
- **Formal writeback:** Storage runtime exclusion/startup errors referenced by Workspace's startup sequencing.

<a id="cg01-q44"></a>

### CG01-Q44 — Local access and privacy boundary

- **Status:** `ACCEPTED`
- **Decision:** Keep data in the current user's local directory with appropriate filesystem access permissions. M1 adds no application encryption/key-management or backup/restore product. Logs contain only necessary operation category, correlation IDs, duration and result codes, not company/role text, full URLs, request bodies, SQL parameters or fingerprints.
- **Exposure:** No automatic upload of entries or diagnostics. Explicit external navigation remains the accepted browser function. Bind only loopback, validate allowed local Host/Origin and do not grant arbitrary cross-origin business access. M1 adds no account-login system.
- **Deletion scope:** Physical business-record deletion does not promise comprehensive media-remanence or backup erasure.
- **Formal writeback:** Storage data/log privacy and Workspace runtime access, coordinated with Entry browser behavior.

<a id="cg01-q45"></a>

### CG01-Q45 — Activated waiting page and property-based navigation safety

- **Status:** `ACCEPTED`, with the user's implementation-independent security refinement.
- **Decision:** The click immediately obtains a neutral waiting page through user activation. Resolve the selected entry/revision asynchronously; only a successful result permits that page to navigate to the returned URL. Failure does not navigate externally; close the waiting page or show failure. If blocked or closed, report the limitation without opening a replacement automatically; another click performs a new resolution.
- **Safety properties:** Before an external page gains control, it must not retain a usable opener relationship and must not receive referrer information. Do not prescribe opening with `noopener` at the outset or a specific opener API sequence. Waiting-page self-resolution/self-navigation and same-origin page coordination are both permitted if the properties hold.
- **Observable result:** Report initiation only after actually submitting the validated target URL for browser navigation, not merely creating the waiting page. Never label this as successfully opened/loaded or applied. The product requests a new tab while respecting browser presentation settings.
- **Formal writeback:** Entry navigation effect/observer boundary, Workspace interaction and browser conformance checks under the actual frontend setup.

## Accepted entry field inventory

This table summarizes accepted decisions; the formal field schema belongs in the Entry Contract. Q21/Q32 settle text rules, Q31 identifier/revision representation, Q27–Q30 logical interfaces and Q35 HTTP mapping. Q36–Q45 settle receipts, errors, diagnostics, time, uncertainty, persistence, runtime and browser boundaries. Normative reconciliation and evidence remain separate from accepted decisions.

| Field | Accepted meaning | Write authority |
| --- | --- | --- |
| `manual_application_entry_id` | Stable lowercase hyphenated UUIDv4 string under Q31 | System; immutable after creation |
| `company_name` | Required single-line company name, 1–200 Unicode code points after outer trim, under Q21 | User through explicit atomic Save |
| `role_title` | Required single-line role title, 1–200 Unicode code points after outer trim, under Q21 | User through explicit atomic Save |
| `application_url` | Required absolute HTTP(S) destination, at most 8192 Unicode code points after fixed outer trim, under Q12/Q21/Q32 | User through explicit atomic Save |
| `revision` | JSON integer in Q31's range, initially 1, advances on actual content change without wrapping | System |
| `created_at` | Initial successful creation time | System; immutable after creation |
| `updated_at` | Initially creation time; actual changes use `max(now, old_updated_at)` under Q39 | System |

`request_id` belongs to the create operation and its minimum receipt, not to the mutable entry's business content. Local initialization follows [CG01-Q19](#cg01-q19).

## Formal Writeback and Closed M1 Frontier

The planned interview is complete. Accepted detailed decisions now map to actual normative owners:

| Owner | M1 requirement range | Review boundary |
| --- | --- | --- |
| [Common](../../contracts/common.md) | COM-001–032 | Shared conventions and consumed M1 representation only |
| [Workspace](../../contracts/foundation/workspace.md) | WSP-001–006 | Local startup/navigation/access; no future Resume defaults |
| [ManualApplicationEntry](../../contracts/jobs/manual-application-entries.md) | MAE-001–018 | Complete selected mutable-entry/browser scope |
| [Storage](../../contracts/foundation/storage.md) | STO-001–013 | M1 layout/recognition/transactions/receipts/privacy only |

The earlier per-round “pending” notes describe decision-time scope unless superseded by this writeback table and the later rounds. [Progress scope evidence](../../progress/traceability.md#61-sl-01m1-reviewed-scope-and-interface-evidence) supplies exact decision-to-ID mappings, interfaces, reviewed revision and hashes. Normative text has a single definition owner; this register remains decision provenance.

Consolidation clarified transport details needed by accepted decisions: a non-echoing `$` field-error locator, ACCESS_DENIED/403 for runtime Host/Origin rejection, a pinned URL-validity definition, exact JSON integer-value semantics and post-commit response-failure handling. These are documented in the [development handoff](../../development/handoff/sl-01-m1-handoff.md#5-review-clarifications-and-preserved-ownership); no additional business capability or stopped Q7–Q10 rule is inferred.

No substantive M1 consumer decision remains open after scoped source and interface review. Concrete dependency locks, SQL/migration artifacts, platform adapters, browser implementation and runtime proof are engineering work in the next task, not already implemented results. Formal Job/JobVersion/JD/observations and later Common/Workspace/Storage scopes remain deferred to their actual consumers.

## Continuation and Maintenance

- Resume from Session State and the open frontier, not from superseded Manual Job assumptions.
- After an answered round, record conclusions using Status, Decision, Rationale and Formal writeback, with scoped supersession or open detail where needed. Record accepted detail here only; do not create parallel module decision records or append original questions or recommendations.
- Keep stable decision locators and same-file references to accepted detail. Actual normative Contracts remain separate formal owners when authorized and ready to write.
- Before closing the Grill, resolve applicable branches and confirm the shared understanding. Actual normative IDs, necessary interface agreement and review evidence precede any readiness claim.
- Contract readiness, implementation and acceptance remain separate. Split mixed readiness scopes so M1 cannot mark another milestone's unfinished scope ready.
