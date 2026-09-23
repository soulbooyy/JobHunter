# SL-02.M2 Contract Grill Decision Register

The implementation-time [2026-09-23 font-role amendment](#cg04-font-20260923) is the latest effective decision for MAT-012. Earlier native-role and Source Han Sans-only restrictions below are historical within that superseded scope.


> English is authoritative. This is the single decision/provenance record for this milestone, not normative Contract text or implementation evidence. Record accepted conclusions and scoped supersession, not question transcripts or unaccepted recommendations.

[Design navigation](README.md) · [Milestone plan](../../plans/slices/sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) · [Session handoff](../../development/handoff/contract_grill/sl-02-m2-contract-grill-handoff.md) · [Readiness ledger](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger)

## Purpose and session state

- Milestone: SL-02.M2 — Demanded preview and export.
- User instruction: execute the session handoff using grill-me/grilling, communicate in Chinese and use English documentation. The initial five-question cadence is replaced by ten independent questions per round from Q74 onward under CG04-S5.
- Decision namespace: CG04-Qn; no prior CG04 decision was found at entry. These locators are provenance, not normative requirement IDs.
- Last interview decision: Q135 accepted with explicit native-Bold-plus-synthetic-italic meaning for BoldItalic and an actual-output verification gate. The Source Han Sans 2.005R exception is scoped; it does not authorize synthetic bold or style substitutions for other logical fonts. Catalog mapping and renderer execution remain unverified.
- Session: Contract design and authorized documentary closure are complete under CG04-S1/S2/S3/S4/S5 and CG04-PUB. Q1–Q135 have effective normative destinations at revision `2026-09-21.S2M2-r1`. Premature ordinary-round writeback was removed under CG04-S4; the later explicit publication authorization permits the scoped owner reconciliation now completed. M2 consumed Contract scope is Ready; implementation, concrete renderer/font research and runtime acceptance remain Pending.
- After each ordinary answered batch: update this register only with effective conclusions, rationale, boundaries, intended normative destinations and the unresolved frontier; check accuracy, relevant known constraints and changed references locally, then advance. Authoritative-document review/writeback follows the explicit user direction and approved plan required by CG04-S3, not the round number.
- Final transfer completed: the [backend development handoff](../../development/handoff/sl-02-m2-handoff.md) contains the reviewed consumption scope, actual upstream checkpoint, engineering order and remaining proof required by CG04-S2.
- Backend/frontend implementation, dependency installation, renderer/worker scaffolding, user-data migration, commit and push are outside this interview's authorization.
- Verification preference: use targeted checks for each changed scope; reserve sub-agents for key factual or interface checks, not a complete independent review every round.

## Verified upstream snapshot

Inspection date: 2026-09-21. Entry HEAD: `16e801c` (`docs(handoff): add SL-02.M2 contract grill prompt`). Entry working tree contained only untracked `docs/.DS_Store`. During read-only inspection, untracked `backend/tests/integration/api/test_candidate_authority.py` appeared from concurrent work. The final status check also showed new untracked Profile/Evidence/Resume/Workspace Domain modules, candidate scalar helpers and a fingerprint module. All are preserved as unverified implementation work; their existence is not runtime availability or passing-test evidence.

| Subject | Observed state and evidence | Consequence |
| --- | --- | --- |
| M1 Contracts | Eight consumed portions reviewed at `2026-09-21.S2M1-r1`; [review](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) lists 73 additions and 178 total IDs | Documentary readiness only; future material portions remain pending |
| Runtime composition | [Container](../../../backend/src/jobhunter/bootstrap/container.py) assembles only ManualApplicationEntry and Preferences | No available Profile/Evidence/Resume exact readers, nine-command Candidate Save or S2 receipts at inspection |
| Storage | [Store](../../../backend/src/jobhunter/infrastructure/persistence/sqlalchemy/uow/store.py) serves schema 2; migration revisions are `b720a94fd381_initial.py` and `cd891047a2e6_preferences.py` | Schema 3 is specified by M1 Contracts but not yet delivered in runtime; do not select an M2 schema number from a historical assumption |
| Frontend | [Router](../../../frontend/src/app/router/router.tsx) and [API generator](../../../frontend/scripts/generate-api.mjs) cover SL-01 consumers | M1 Resume editor/local A4 preview and M2 saved preview/export are unavailable |
| Tests | SL-01's recorded 160 backend tests and frontend/Chromium evidence are inherited only; concurrent S2 API test drafts are unverified | No runtime test was rerun in this Grill; no S2 runtime acceptance is claimed |
| M2 definitions | [Materials](../../contracts/applications/materials.md) contains MAT-001–003 source-boundary scope only; `foundation/derived-work.md` is absent | Actual demand/configuration/work/output/recovery definitions are open; the [planned destination](../../contracts/structure.md#planned-derived-work) is not a normative body |

M1 development appears to be starting concurrently, so its historical Not started entries are source-time records rather than a promise that no files will change. Recheck actual upstream implementation, migrations, APIs and evidence before M2 development. Missing M1 runtime does not block independent M2 Contract decisions.

Round-one writeback update: the entry table above is historical. Current container composition now registers CandidateAuthority/routes, Store recognizes schema 3, and revision `ef03c92ba671_candidate_authority.py` exists. The maintained [backend evidence](../../progress/traceability.md#saved-candidate-backend-evidence) records 294 passing backend tests and the [M1 handoff §6](../../development/handoff/sl-02-m1-handoff.md#6-backend-to-frontend-and-next-consumer-transfer--2026-09-21) transfers the implemented subset. This Grill inspected the changed composition/storage and read that evidence; it did not independently rerun the suite. M1 frontend/local A4 preview and M2 materials remain undelivered. Preserve concurrent implementation work and reverify relevant interfaces at actual M2 development entry.

## Controlling inherited boundaries

- [CG03-BC1–BC3/A1–A5](sl-02-m1-grill.md#cg03-bc3), PRO-001/006, EVD-001/011 and RES-001/010/011 preserve separate fact/contact/document authority, exact retained bindings and independent local expression. Historical propagation/current-only proposals remain superseded.
- MAT-001–003, SAV-006/016 and STO-025 implement CG03-Q95: M1 supplies saved authority and receipts; M2 first supplies actual demand/configuration/intent/work/output/recovery. Necessary Save-coupled intent commits atomically with its owning command; rendering remains post-commit.
- CG03-UI1 and RES-015 keep editor-local A4 Draft preview in M1 frontend scope. It is neither a saved artifact nor export readiness.
- Source current-pointer movement or ordinary retirement alone does not invalidate an unchanged Resume or its materials. Document changes, actual demand/configuration, permissions and byte/source availability are separate concerns.
- RES-002–014, PRO-007 and EVD-013 provide exact saved sources and strict readers. RES-012 defines four document settings and fixed A4; logical font names do not prove available font assets or fidelity.
- Common owns naming/scalars and shared error representation/vocabulary. Existing request namespaces, published IDs and old consumer behavior remain protected.
- Safe local recovery does not authorize model/platform replay. Preparation approval, Greeting, send authorization, execution and Application History remain later consumers.
- No eager all-format rendering, new Aggregate/Analysis, universal job framework, empty normative placeholder or whole-family readiness gate follows from this milestone.

## Initial definition-owner map and consumed scopes

| Owner | Reused scope | Actual M2 additions to resolve |
| --- | --- | --- |
| [Product](../../spec.md#35-current-use-grounding-and-generated-materials) | Independent authority, legal empty saved state, Save versus material success; §7 future Preparation boundary | Conditional writeback only when a concrete Contract gap requires an explicitly approved product clarification; no general product redesign |
| [Architecture](../../architecture.md#54-grounding-and-demand-driven-artifacts) | §§3/5/12.3/13/16: exact identity, owner separation, local recovery and storage | Concrete demand/publication/Save/storage interface responsibilities where decisions require refinement |
| [Materials](../../contracts/applications/materials.md) | MAT-001–003 | Output meaning, exact lineage, required formats/configuration compatibility, readiness, current/historical reads and download obligations |
| Planned [Derived Work](../../contracts/structure.md#planned-derived-work) | Existing architectural demand/recovery constraints; no normative body yet | Durable demand/intent, necessary identities, claim/reuse/obsolescence, safe execution/recovery and fenced publication |
| [Candidate Save](../../contracts/candidate/candidate-save.md) | SAV-001–016 command, revision, receipt and uncertain-outcome boundaries | Q17 excludes follow-current demand: content Save does not advance these exact targets or create speculative intent. Preserve MAT-003's conditional future Save/intent invariant; remaining removal/admission interfaces must still be reconciled |
| [Resume](../../contracts/candidate/resumes-grounding.md), [Profile](../../contracts/candidate/profile.md), [Evidence](../../contracts/candidate/evidence.md) | Exact document/local AST/settings and retained source readers, lifecycle/privacy | Only necessary material-consumer eligibility/availability agreements; no rewritten fact authority or universal semantic gate |
| [Storage](../../contracts/foundation/storage.md) | STO-001/002/007–009/012/013 and STO-021–028 as applicable | Persisted intent/work/artifact relations, file publication/integrity/retention, explicit schema evolution and recovery |
| [Common](../../contracts/common.md), [Workspace](../../contracts/foundation/workspace.md) | Shared scalars/names/errors and local access/ownership; default selection remains independent | Only consumed vocabulary, transport or startup applicability extensions |
| [Slice plan](../../plans/slices/sl-02-saved-authority-materials.md), [Acceptance](../../acceptance.md#43-demand-and-safe-derivative-recovery), [Progress](../../progress.md) | M1/M2 division; Acceptance §§4.3/9.3/10; scope-level readiness | Approved scope corrections, exact proof requirements, and actual readiness/evidence without implementation claims |

Q105 excludes MaterialBundle from M2's consumed scope; a future concrete combination consumer can define it. Q2–Q4 establish derived RenderManifest provenance, immutable configuration identity and independent Artifact identity; subsequent decisions below refine their shapes and relationships. At the interview stage no new normative requirement IDs had been allocated. The final allocations and actual destinations are recorded under CG04-PUB and in the linked review ledger; this initial map preserves the planning baseline.

## Round 1 — Exact Sources, Provenance, Identities and Command Receipts

<a id="cg04-q1"></a>
### CG04-Q1 — One exact client source reference

Status: ACCEPTED with user refinement. The sole client source parameter for an explicit material request is `resume_version_id`. The server derives `resume_id`, `profile_version_id` and Evidence references from that exact saved Version. Clients cannot also submit those derived source fields, replacement source bodies or overrides. This does not prohibit separately owned non-source request fields such as the eventual output/configuration selector.

Exact historical resolution is not admission for new generation. This decision alone grants no historical/removed generation permission. Q14 subsequently admits retained historical Versions of ACTIVE Resume roots for local generation, without active/current Evidence checks; other source availability, permissions, configuration and downstream admission clauses remain separate.

Intended normative destination: Materials/Derived Work request admission consumes RES/PRO/EVD exact readers. Existing M1 readers and Save bodies are unchanged. Earlier Architecture/Acceptance writeback was removed under CG04-S4.

<a id="cg04-q2"></a>
### CG04-Q2 — Deterministically derived, ordered material provenance

Status: ACCEPTED with user refinement. RenderManifest explicitly records the complete exact lineage rooted in `resume_version_id`, including its bound Profile and Evidence references. It is a derived provenance record, never a second source authority. The server deterministically derives and validates all references against that ResumeVersion; clients cannot provide or mutate the manifest to change sources. Do not copy canonical fact or Resume bodies into the lineage record.

Evidence relationships preserve the structure and ordering actually used by the ResumeVersion, rather than collapsing them into an unordered set. Q6 subsequently defines the section/ref representation and Q8 settles Manifest containment. An empty local member body does not authorize source-body fallback or omission of its actual source relationship.

Intended normative destination: Materials manifest definition and Storage consistency consume Resume lineage. No Profile/Evidence authority or M1 AST definition changes. Earlier Architecture/Acceptance writeback was removed under CG04-S4.

<a id="cg04-q3"></a>
### CG04-Q3 — Immutable configuration identity, separate compatibility

Status: ACCEPTED with user refinement. RenderConfiguration has its own immutable identity. Each Artifact remains bound to the exact `render_configuration_id` used for its creation. Output-affecting configuration changes cannot rewrite an existing configuration in place. Identity is separate from canonical equality and compatibility: semantic equality does not automatically merge configuration identities, and reuse across different configuration IDs needs an explicit compatibility policy.

The eventual configuration definition covers template, renderer, font/asset versions and representation/schema version; concrete field names, structures, version encodings and publishing mechanism remain unsettled. Q7 subsequently requires an exact client configuration selector; Q9 limits first-release reuse to the same configuration ID. No user-facing configuration-management feature is implied.

Intended normative destination: Materials configuration/compatibility definitions and Derived Work reuse consume that distinction. Existing RES-012 logical document settings remain unchanged. Earlier Architecture/Acceptance writeback was removed under CG04-S4.

<a id="cg04-q4"></a>
### CG04-Q4 — Artifact identity and persisted-byte integrity

Status: ACCEPTED with user refinement. `artifact_id` is a server-generated independent UUIDv4. A separate SHA-256 value checks the actual persisted Artifact bytes; it is not a Resume/RenderConfiguration business fingerprint. Equal digests do not merge Artifact identities: lineage, creation results and readiness identity can differ.

Storage may deduplicate physical content beneath the Materials boundary, but physical sharing cannot leak into material-identity merging or bypass provenance/readiness rules. Concrete metadata fields, byte-publication/verification protocol and deduplication implementation remain open.

Intended normative destination: Materials identity and Storage integrity/physical-sharing definitions reuse Common UuidV4/Sha256Hex. No published Common meaning changes. Earlier Architecture/Acceptance writeback was removed under CG04-S4.

<a id="cg04-q5"></a>
### CG04-Q5 — Operation-scoped Materials receipts and immutable acceptance replay

Status: ACCEPTED with user refinement. Within one Workspace, explicit Materials commands use an independent namespace keyed by `(operation, request_id)`, or a representation with exactly that namespace meaning. A UUID used in Candidate Save and Materials does not conflict; different Materials operations have distinct key scopes. Matching normalized input under the same key replays the original committed acceptance snapshot; different normalized input under that same key conflicts. Exact operation tags, fingerprint encoding and receipt shape remain open; retention is subsequently settled by Q10.

Replay never reconstructs a result from today's Derived Work/Artifact state. For example, if an original acceptance eventually references a render intent, later completion cannot change the replayed acceptance into a newly assembled ready result. The example does not yet freeze an intent object, identifier field or READY enum. Current readiness is obtained through an independent read interface. Save-coupled internal intent remains part of its Candidate Save transaction and is not represented as a second client command. No existing M1 command namespace or receipt schema is changed.

Intended normative destination: Derived Work explicit-command/receipt/read protocol and Storage persistence, with Candidate Save atomic participation reconciled at its actual demand consumer. Earlier Architecture/Acceptance writeback was removed under CG04-S4.

Scope reconciliation: Product behavior and the SL-02 milestone allocation are unchanged by Q1–Q5, so they need no new product policy or scope correction. Materials/Derived Work/Storage detailed norms remain pending publication; existing normative bodies are not prematurely extended with unresolved shapes. Ordinary accepted design is recorded here only, without changing Contract readiness or adding per-round Progress entries.

## Round 2 — Lineage Shape, Configuration Selection, Containment and Retention

The user accepted Q6–Q10 in full and supplied additional refinements for Q6 and Q10. Q7–Q9 retain the presented decisions without amendments. No other open topic is treated as accepted.

<a id="cg04-q6"></a>
### CG04-Q6 — Ordered source_sections projection

Status: ACCEPTED with user refinement. RenderManifest uses `source_sections`, an ordered array whose entries contain `kind` and ordered `evidence_refs`. Each ref contains `evidence_item_id` and `evidence_item_version_id`. It is a deterministic lineage projection of `ResumeVersion.sections`: section kinds, section order, member order and exact member pairs match item by item. A Resume with no sections produces `source_sections: []`. No extra section/member identity is introduced.

The server derives and validates this projection; clients cannot submit or modify it. A member with empty Resume-local content still retains its Evidence ref; do not flatten to an unordered set, omit that relationship or fall back to the source narrative. Full Manifest envelope and persisted integrity handling remain later detail.

Intended normative destination: Materials Manifest schema/derivation, consuming RES-005 and RES-010; Storage enforces the corresponding retained relationships. Actual writeback: this register only.

<a id="cg04-q7"></a>
### CG04-Q7 — Explicit exact configuration selector

Status: ACCEPTED. Each explicit material request carries `render_configuration_id`; there is no omitted-means-current-default behavior or silent substitution during handling. It is a configuration selector, separate from Q1's unique client Resume source parameter. A later default change cannot change the configuration expressed by an identical retried request.

Q13 subsequently scopes configuration HTTP to read-only, with server-controlled application delivery/publication. Detailed discovery, publishing and new-request availability protocols remain open. An exact configuration reference alone does not establish current eligibility or installed asset availability.

Intended normative destination: Materials configuration selection and Derived Work request admission/fingerprint. Actual writeback: this register only.

<a id="cg04-q8"></a>
### CG04-Q8 — Artifact-contained immutable Manifest

Status: ACCEPTED. Each Artifact has exactly one immutable RenderManifest, read through that Artifact. No independent `render_manifest_id`, standalone mutation or rebinding operation is introduced. Physical storage may use separate tables without creating another business identity. Q11 subsequently defines the Manifest envelope and Q12 limits formal Artifact existence to successful publication; the complete Artifact envelope and physical publication protocol remain open.

Intended normative destination: Materials object relationship/read representation and Storage physical mapping. Actual writeback: this register only.

<a id="cg04-q9"></a>
### CG04-Q9 — Same-configuration-only first-release reuse

Status: ACCEPTED. M2 first delivery does not implement cross-configuration equivalence/reuse. Matching exact ResumeVersion, `render_configuration_id` and the remaining output-target parameters is necessary, not sufficient, for work/output reuse. Permissions, availability, integrity and the eventual demand/publication conditions still apply.

Different configuration IDs do not become interchangeable because their content is equal. Cross-configuration compatibility needs a later explicit extension; no equivalence evaluator or identity merging is introduced here. This narrows Q3's deliberately open compatibility branch without changing immutable identity or earlier lineage rules.

Intended normative destination: Materials compatibility and Derived Work reuse/admission. Actual writeback: this register only.

<a id="cg04-q10"></a>
### CG04-Q10 — Workspace-lifetime receipts independent of payload retention

Status: ACCEPTED with user refinement. Successful Materials acceptance receipts and the information needed to reconstruct their original acceptance results remain for the Workspace lifetime, without automatic TTL. Work completion/failure or ordinary Resume removal does not delete the receipt. Replay preserves Q5's original snapshot.

Receipt existence does not guarantee that Artifact payload bytes remain readable forever. Original-acceptance replay and subsequent Artifact availability reads have separate meanings. File cleanup cannot erase a success receipt or rewrite the original acceptance into the current unavailable outcome. This does not define or authorize a payload cleanup schedule; exact output retention, metadata dependencies and availability representation remain open. No permanent-file guarantee follows from permanent receipt retention.

Intended normative destination: Derived Work receipt/replay, Materials availability reads and Storage retention dependencies. Actual writeback: this register only.

Local consistency review: Q6/Q8 refine Q2 without adding a source authority; Q7/Q9 preserve Q3's identity/compatibility distinction; Q10 preserves Q5's immutable replay independently of files. The accepted scope does not change existing M1 command bodies, source admission, lifecycle retention or Common representations. Only this register is updated; no normative publication, authority-file writeback, status/readiness change or runtime verification follows from this round.

## Round 3 — Manifest Envelope, Publication and Explicit Admission

The user accepted Q11–Q15 in full, adding Q12's reservation visibility rule and Q14's explicit prohibition on current/ACTIVE Evidence readmission. Q11/Q13/Q15 retain the presented decisions without amendments.

<a id="cg04-q11"></a>
### CG04-Q11 — Closed RenderManifest envelope

Status: ACCEPTED. RenderManifest contains exactly these seven required, non-null fields:

| Field | Accepted representation and meaning |
| --- | --- |
| schema_version | integer 1; Manifest representation schema |
| resume_id | UuidV4; server-derived owning Resume |
| resume_version_id | UuidV4; exact saved source |
| profile_version_id | UuidV4; source Version's bound Profile |
| source_sections | ordered lineage projection under Q6 |
| render_configuration_id | UuidV4; exact immutable configuration used |
| artifact_id | UuidV4; owning published Artifact |

No source body, file path, work state, standalone Manifest timestamp or Manifest business ID is added. The owning artifact_id establishes containment, not another identity. Root/source/configuration/Artifact references are validated under their respective owned relationships; client input cannot construct or override the Manifest.

Intended normative destination: Materials Manifest schema and Storage containment/reference consistency. Actual writeback: this register only.

<a id="cg04-q12"></a>
### CG04-Q12 — Published artifacts only, internal reservation isolation

Status: ACCEPTED with user refinement. Artifact denotes a successfully published immutable output. Queueing, execution, failure and retry belong to Derived Work, not mutable Artifact lifecycle states. Do not publish an incomplete Artifact without its required file, digest or Manifest.

An implementation may reserve artifact_id internally. Before successful Artifact publication, that reserved ID cannot be externally read, referenced or represented as an existing Artifact. Reservation is not an Artifact resource or an acceptance result's available Artifact reference. Exact publication/transaction/file consistency mechanics remain open.

After publication, missing/corrupt bytes are independent availability/integrity observations. They do not return the Artifact to a generating state or erase its historical identity.

Intended normative destination: Materials Artifact meaning, Derived Work state/output boundary and Storage publication. Actual writeback: this register only.

<a id="cg04-q13"></a>
### CG04-Q13 — Read-only configuration HTTP scope

Status: ACCEPTED. M2 configuration HTTP operations are read-only: clients discover/read server-provided configurations and select exact IDs. No user HTTP operation creates, edits or deletes RenderConfiguration. Configurations are delivered with the application and published through server-controlled mechanisms.

Concrete registration, persistence, upgrade, discovery and withdrawal from new-request admission remain open. This does not authorize silent rewriting of immutable configuration records or automatic migration of user storage.

Intended normative destination: Materials configuration/read API and Storage server publication/evolution. Actual writeback: this register only.

<a id="cg04-q14"></a>
### CG04-Q14 — ACTIVE Resume historical generation without Evidence readmission

Status: ACCEPTED with user refinement, subsequently narrowed by Q67 on required payload scope. A new local material-generation request may explicitly use any legally retained ResumeVersion whose owning Resume is ACTIVE, including a historical Version. A REMOVED owning Resume rejects new generation. Exact historical payloads actually required for rendering must remain resolvable, and relevant permission/configuration checks still apply. Mere presence of an Evidence reference in lineage does not make its entire payload a rendering prerequisite. Never substitute the current ResumeVersion.

Do not require the bound EvidenceItems to remain ACTIVE or their Versions to remain current. Ordinary Evidence retirement or source current-pointer changes do not invalidate the saved ResumeVersion's exact lineage. Rendering uses those retained historical references, including the bound historical Profile under the inherited rules. This does not restore the superseded current-Knowledge gate or infer semantic support from lineage.

Existing Artifact history/download and downstream Preparation/execution eligibility remain separately admitted; this decision grants no downstream authorization. Dispatch/publication rechecks after concurrent Resume removal remain open. Q17 subsequently excludes follow-current demand from M2.

Intended normative destination: Materials local-generation admission and Derived Work consumption of retained Resume/Profile/Evidence sources. Actual writeback: this register only.

<a id="cg04-q15"></a>
### CG04-Q15 — Receipt replay before new-generation source/configuration admission

Status: ACCEPTED. Explicit material commands first pass access, request transport/structure/value validation and canonical fingerprint computation, then inspect the success receipt in Q5's namespace. Only a receipt miss enters source/configuration resolution and new-request admission. Exact raw limits, operation fields, fingerprint encoding and error precedence within those phases remain to be defined.

A matching receipt returns the original committed acceptance snapshot without rechecking current generation eligibility. Same key with different admitted input conflicts. Later Resume removal or a configuration no longer admitting new requests does not convert replay into new execution. A genuinely damaged persisted receipt fails honestly; do not treat it as absent and run the command again.

Intended normative destination: Derived Work command admission/replay and Storage receipt reconstruction/integrity. Existing M1 admission exceptions and namespaces are unchanged. Actual writeback: this register only.

Local consistency review: Q11 preserves Q6/Q8 derived ordered containment; Q12 keeps internal reservation separate from formal output; Q13 does not introduce client configuration mutation; Q14 respects MAT-002/RES exact historical lineage rather than restoring active/current Evidence checks; Q15 separates original acceptance from mutable new-request admission under Q5/Q10. Q1/Q7/Q8 open-detail references above now point to the later decisions. Only this record changed; no authority/status writeback or runtime test is required for this batch.

## Round 4 — Artifact Metadata and Exact-Version Demand Scope

The user accepted Q16–Q20 with Q17 explicitly amended. The proposed CURRENT_RESUME mode was never accepted; it is excluded from M2 under the effective Q17 conclusion. Q16/Q18/Q19/Q20 retain their presented decisions.

<a id="cg04-q16"></a>
### CG04-Q16 — Closed immutable Artifact metadata

Status: ACCEPTED. The Artifact object contains exactly seven required, non-null fields:

| Field | Accepted representation and meaning |
| --- | --- |
| artifact_id | UuidV4 |
| schema_version | integer 1; Artifact representation schema |
| manifest | Q11 RenderManifest; its artifact_id equals the enclosing ID |
| media_type | MIME value for a supported output format; Q30 subsequently selects application/pdf and image/png |
| byte_length | exact integer number of persisted file bytes, 1 through 9007199254740991 |
| sha256 | Common Sha256Hex over actual persisted bytes |
| created_at | Common UtcTimestamp at successful publication |

No work state, mutable availability, physical path or download URL belongs to this immutable object. The scalar byte_length range is not an operational file-size allowance; actual output-size limits remain open. Filename/download representation, exact publication time rules and file availability use their own later definitions.

Intended normative destination: Materials Artifact schema and Storage byte/metadata consistency. Actual writeback: this register only.

<a id="cg04-q17"></a>
### CG04-Q17 — EXACT_VERSION-only demand in M2

Status: ACCEPTED AS AMENDED by the user. M2 supports only fixed EXACT_VERSION demand. A demand remains bound to its accepted exact resume_version_id; later Resume Saves do not retarget it or automatically create replacement intent. A consumer wanting the latest document first reads current_resume_version_id, then explicitly requests that exact Version. A later Save between the read and request does not substitute a different source; Q14's historical-Version admission still applies.

The proposed CURRENT_RESUME mode is NOT ACCEPTED for M2. There is no demonstrated sustained-current consumer requiring atomic Save-driven target advancement, subscription lifetime/release or supersession of fixed targets. Add such a mode only for a later real consumer through an explicit Contract extension. Exact-only semantics do not themselves require a wire mode field; complete command fields remain open.

Impact: prune follow-current subscription/target-advancement and content-Save-triggered material intent branches from this M2 interview. MAT-003 and the Slice's joint agreement require atomic Save+intent only where actual demand needs it; that invariant remains intact and does not justify manufacturing such a demand. Explicit-demand acceptance still needs its own durable atomic intent/receipt boundary. Safe work recovery, ownership fencing and exact output publication remain necessary where actually consumed; Q24 subsequently excludes explicit demand cancellation/release from M2. A newer ResumeVersion alone does not obsolete work for a still-demanded exact Version.

Intended normative destination: Derived Work demand/target/publication scope and Materials exact-target compatibility. Before final publication, reconcile the actual consumed Candidate Save scope and the plan's current-publication/obsolete-work wording with this decision under the user's authorized writeback process. No plan, Architecture, Acceptance, normative body or readiness ledger is changed in this ordinary round.

<a id="cg04-q18"></a>
### CG04-Q18 — Retained configuration versus present execution support

Status: ACCEPTED. Retain immutable configuration snapshots and exact reads independently of current execution support. Reading a retained configuration does not prove that the current installation can execute it. If required renderer/font/asset support is unavailable, reject new generation rather than selecting another configuration or rewriting the original snapshot.

An existing Artifact is read according to its own permission and payload availability, not automatically invalidated by loss of renderer support. Detailed capability representation, installation/upgrade behavior and error classification remain open.

Intended normative destination: Materials configuration support/admission/read semantics and Storage retained snapshots. Actual writeback: this register only.

<a id="cg04-q19"></a>
### CG04-Q19 — Independent demands with shared compatible work

Status: ACCEPTED. Different new accepted commands retain separate acceptance receipts and demand identities even when targeting the same exact source/configuration/output parameters. Compatible execution work or already-published output may be shared. A replay under the same idempotency key retains the original demand rather than creating another one.

Releasing one demand cannot automatically cancel work still required by another demand; under subsequent Q24 this is a constraint for a future cancellation/release extension, not a required M2 command. Complete demand/work shapes and reuse keys remain open; Q25 subsequently fixes reuse priority. This relationship introduces no universal job framework or Aggregate.

Intended normative destination: Derived Work demand/work/output relationships and Storage receipt/dependency persistence. Actual writeback: this register only.

<a id="cg04-q20"></a>
### CG04-Q20 — Pure material reads and explicit regeneration

Status: ACCEPTED. Material queries and downloads are read-only. Missing or corrupt payloads produce truthful availability/error results; reads do not implicitly persist demand, rerender, replace an Artifact or perform recovery writes. Regeneration requires an explicit command and its applicable new-generation admission rules.

Detailed regeneration/read/download interfaces and failure classifications remain open. This does not make unavailable bytes alter Q10's retained receipt or Q5's original acceptance replay.

Intended normative destination: Materials reads, Derived Work explicit commands and Storage availability. Actual writeback: this register only.

Local consistency review: Q16 refines Q4/Q11/Q12; Q17 narrows an unaccepted proposal while preserving Q1/Q14 exact sources and MAT-003's conditional atomicity; Q18/Q20 preserve immutable identities, payload independence and pure reads; Q19 separates command/demand identity from execution reuse. Only the register changed. No authority/status writeback, sub-agent review or runtime verification was performed for this batch.

## Round 5 — Output Selection, Acceptance, Removal and Minimal Execution Scope

The user accepted Q21–Q25 with Q24 explicitly amended to omit first-release cancellation. Q21/Q22/Q23/Q25 retain their presented decisions. The proposed cancellation command was never accepted as M2 scope.

<a id="cg04-q21"></a>
### CG04-Q21 — Configuration-owned output representation

Status: ACCEPTED. Each RenderConfiguration fixes one output representation. The client selects that exact configuration and does not separately submit output_format. The produced Artifact.media_type agrees with the configuration. Q30 subsequently selects PDF and PNG; concrete format-specific configuration fields remain open for the rendering branch.

Intended normative destination: Materials configuration/output schemas and Derived Work exact target. Actual writeback: this register only.

<a id="cg04-q22"></a>
### CG04-Q22 — Fixed successful acceptance response

Status: ACCEPTED. Successful explicit material acceptance returns exactly three required, non-null fields: `request_id: UuidV4` (the original request), `outcome: ACCEPTED`, and `render_intent_id: UuidV4` (the server-generated independent demand identity). This is the fixed original acceptance snapshot, not an observation of current execution/readiness. The response has the same shape when existing output satisfies the demand immediately.

Matching replay returns the original values. Completion state and published Artifact references are obtained separately through reads. No reserved Artifact ID is exposed. HTTP success status, exact request body/route, full RenderIntent representation and persistence details remain open.

Intended normative destination: Derived Work command result/receipt/read protocol and Storage retained acceptance. Actual writeback: this register only.

<a id="cg04-q23"></a>
### CG04-Q23 — Ordinary removal does not revoke accepted exact demand

Status: ACCEPTED. Ordinary Resume removal rejects new material requests under Q14 but does not revoke an already accepted exact demand. Its work may continue to completion against the original retained Version. An intervening content Save likewise does not retarget or invalidate that exact demand.

Source integrity/availability failures and applicable permission withdrawal retain separate handling. The original proposal mentioned cancellation as another possible cause; Q24 subsequently excludes a user cancellation command from M2. The removal rule does not imply a privacy-revocation bypass, new downstream eligibility or authority to silently replace missing sources. Existing successful receipts remain replayable under Q15.

Intended normative destination: Materials admission and Derived Work accepted-demand execution, consuming Resume lifecycle without an automatic removal-triggered cancellation transaction. Actual writeback: this register only.

<a id="cg04-q24"></a>
### CG04-Q24 — No explicit cancellation in first-release M2

Status: ACCEPTED AS AMENDED by the user. M2 exposes no explicit cancellation command or CANCEL demand outcome. Once accepted, a RenderIntent proceeds through its owned execution/recovery to completion or failure. Do not add cancellation-versus-dispatch/publication arbitration, last-demand cancellation, cancellation receipts or caller release/lifetime controls without a real consumer.

The earlier proposed command is NOT ACCEPTED. The user identifies no current UI/renderer consumer requiring cancellation; assumptions about short deterministic rendering are a scope rationale, not measured performance evidence or a latency guarantee. A later demonstrated long-running renderer or explicit UI requirement can introduce cancellation by render_intent_id through a scoped extension.

Q19's independent demand identities and shared execution remain effective. Its release-isolation rule is retained for future extensions, without implementing release now. Process failure/restart recovery, execution failure, resource limits and source/permission admission are still real work; omission of cancellation does not permit unsafe or unbounded execution.

Intended normative destination: Derived Work command/lifecycle scope. Actual writeback: this register only; no authoritative scope document is changed in this ordinary batch.

<a id="cg04-q25"></a>
### CG04-Q25 — Output-first, then in-flight work, then new execution

Status: ACCEPTED. After new-demand admission, reuse in this order: a compatible, complete, available published Artifact; otherwise compatible in-flight work; otherwise create new execution work. A missing or corrupt file is not a reusable success. Different accepted commands retain their own demand identities/receipts under Q19 even when execution/output is shared.

The selection is part of an explicit demand command, not a side effect of GET/download. No first-release force_rerender parameter is introduced. Exact compatibility keys, concurrency protection, integrity observations, tie-breaking and the full work lifecycle remain open.

Intended normative destination: Derived Work acceptance/reuse and Materials compatibility/availability, persisted under Storage. Actual writeback: this register only.

Local consistency review: Q21 fixes format selection ownership without selecting a renderer/format; Q22 preserves Q5/Q10 replay and Q12 reservation isolation; Q23 separates new admission from accepted exact demand; Q24 removes the unaccepted cancellation branch without changing shared-work identities or safe recovery; Q25 preserves pure reads and requires valid output for reuse. The register's older open references and frontier have been reconciled. No authority/status files, runtime tests or sub-agents were used for this ordinary batch.

## Round 6 — Intent Outcomes and Two Export Formats

The initial response explicitly addressed Q27 and Q30. At that point Q26/Q28/Q29 remained unanswered; omission was not recorded as agreement. Their existing numbers were retained in the next frontier and subsequently accepted in Round 7 below.

<a id="cg04-q27"></a>
### CG04-Q27 — Intent states with explicit terminal results

Status: ACCEPTED with user refinement. RenderIntent states are PENDING, FULFILLED and FAILED. PENDING represents accepted demand without a final result. FULFILLED records successful satisfaction by a published Artifact. FAILED records a terminal failure. Queueing, running and recovery details belong to shared execution work rather than an additional intent RUNNING state. Terminal outcomes do not revert to PENDING; another attempt after a terminal failure requires a new intent rather than changing the original receipt.

FULFILLED must bind exactly one artifact_id identifying the published Artifact that satisfied this intent. No reserved or unpublished Artifact ID can satisfy this requirement. FAILED must retain a stable failure classification/result sufficient for a client to distinguish and present the outcome; a bare state value is insufficient. Q33 subsequently fixes the read fields and state-dependent nullability; the exact failure vocabulary remains open. Successful historical fulfillment is separate from the Artifact payload's current availability, so subsequent file loss does not rewrite the original outcome.

Intended normative destination: Derived Work intent/read/result definitions, Materials published-Artifact reference and Storage terminal-result persistence. Actual writeback: this register only.

<a id="cg04-q30"></a>
### CG04-Q30 — PDF and PNG export support

Status: ACCEPTED AS AMENDED by the user. M2 supports both PDF (application/pdf) and PNG (image/png) export. The PDF-only proposal was NOT ACCEPTED. Each configuration still selects one representation under Q21; supporting both formats does not mean every command eagerly generates both or one intent acquires two successful Artifact references.

The initial format decision left the mapping from a potentially multi-page A4 Resume to PNG output unresolved. Q31 subsequently selects one vertically assembled PNG containing every complete page in order. PNG dimensions, rasterization fidelity and limits remain open. PDF preview and rendering implementation details are not established merely by selecting supported export formats.

Intended normative destination: Materials supported representations/configuration/output rules and corresponding Derived Work consumption; final authorized scope reconciliation must include PNG. Actual writeback: this register only; no Product, Architecture, Acceptance, plan, Contract body or readiness update is made in this ordinary response.

Local consistency review: Q27 preserves Q12's published-only Artifact identity and Q5/Q10's original acceptance snapshot; Q30 preserves Q21's one-representation configuration and Q27's one-Artifact fulfillment while explicitly leaving multi-page PNG representation unresolved. Q16/Q21 now reference the accepted formats. Unanswered Q26/Q28/Q29 remain open. No runtime verification or sub-agent review was performed.

## Round 7 — Request Protocol, Shared Work, PNG Pagination and Atomic Acceptance

The user accepted Q26/Q28/Q29/Q31/Q32 and explicitly refined Q32's new-work branch. All Q1–Q32 now have accepted conclusions; the nonsequential placement of Q26/Q28/Q29 preserves the actual response history and stable locators.

<a id="cg04-q26"></a>
### CG04-Q26 — Explicit render request HTTP operation

Status: ACCEPTED. POST /api/v1/render-intents accepts exactly three required, non-null UuidV4 fields: request_id, resume_version_id and render_configuration_id. Reject additional fields. The internal operation discriminator is RENDER_REQUEST within the Materials per-Workspace (operation, request_id) namespace. Do not add mode, output_format or force_rerender fields.

Return HTTP 200 only after successful acceptance commit, with exactly Q22's request_id/outcome/render_intent_id acceptance snapshot. HTTP 200 establishes acceptance, not rendering completion. Matching replay preserves the original acceptance; current state and published output are separate reads. Raw request limits, canonical fingerprint encoding, detailed errors and read routes remain open.

Intended normative destination: Derived Work HTTP/command protocol, with Common shared types and Storage receipts. Actual writeback: this register only.

<a id="cg04-q28"></a>
### CG04-Q28 — One unfinished Work per exact compatibility key

Status: ACCEPTED. Within one Workspace, the compatible execution key is (resume_version_id, render_configuration_id). At most one unfinished Work exists for a key. Creating or joining Work must enforce this invariant atomically under concurrent commands rather than relying on an unprotected check-then-create sequence.

Each newly accepted command retains its independent Intent and receipt. Terminal historical Work does not occupy the unfinished-work uniqueness constraint. Q21's configuration fixes output representation, so no separate format key is added. Q34 subsequently fixes Work states; the claim/fencing protocol and persistence enforcement remain open. No external queue service is required by this decision.

Intended normative destination: Derived Work compatibility/concurrency and Storage uniqueness/transactions. Actual writeback: this register only.

<a id="cg04-q29"></a>
### CG04-Q29 — Reported rendering failure versus interrupted execution

Status: ACCEPTED. M2 does not automatically retry an explicitly reported rendering failure. The failed Work leads its still-pending dependent Intents to terminal failure with the stable results required by Q27. A subsequent generation attempt requires a new command and Intent; the old receipt and terminal outcome are unchanged.

Process interruption is a separate safe-recovery case. Durable execution/publication evidence determines whether local work can be recovered or re-executed; a known rendering failure must not be disguised as a crash and retried indefinitely. Concrete failure classifications, crash-attempt bounds and recovery/fencing transitions remain open.

Intended normative destination: Derived Work failure/recovery and Storage durable outcome evidence. Actual writeback: this register only.

<a id="cg04-q31"></a>
### CG04-Q31 — One complete multi-page PNG image

Status: ACCEPTED. PNG export produces one PNG Artifact containing every A4 page in document order, arranged vertically into a single image. Preserve each complete page's A4 boundary and content; do not export only the first page, crop later content or silently truncate the document.

Pixel dimensions, scale, maximum height and related rendering/resource limits remain to be defined. Exceeding the supported limits produces an explicit failure rather than partial successful output. This preserves Q27's exactly-one-Artifact fulfillment without introducing per-page Artifacts, archives or a page-selection command. PDF and PNG remain separate configuration-selected representations under Q21/Q30, not automatic dual output.

Intended normative destination: Materials PNG representation/configuration and Derived Work output-validation failures. Actual writeback: this register only.

<a id="cg04-q32"></a>
### CG04-Q32 — Complete atomic acceptance including new Work creation

Status: ACCEPTED with user refinement. A single acceptance database transaction commits the successful receipt and original acceptance snapshot, the independent RenderIntent, and exactly one of these satisfaction/execution branches:

1. Bind an eligible existing published Artifact and fulfill the Intent.
2. Join an existing compatible unfinished Work by creating the Intent dependency.
3. Create a new compatible Work record and its Intent dependency in this same transaction.

The new Work record itself must not be deferred until after acceptance commit. A committed Intent must not depend on a later creation step that can be lost at a crash point, leaving accepted demand without execution work. These branches consume Q25's reuse priority and Q28's concurrency invariant. Any failure before commit leaves no partial successful receipt/Intent/dependency/new Work from that acceptance.

Immediate Artifact reuse may commit the Intent already FULFILLED; the response remains Q22's original acceptance shape. Actual rendering runs after commit. This decision establishes durable execution responsibility, not a guarantee of instantaneous dispatch or immunity from later execution failure. Work discovery/claim/restart recovery and output publication still require their own definitions.

Intended normative destination: Derived Work acceptance application transaction and Storage atomic receipt/intent/work/dependency persistence. Actual writeback: this register only.

Local consistency review: Q26 preserves Q5/Q15/Q22 receipt semantics; Q28 closes compatible-work creation races without merging demand identities; Q29 preserves Q27 terminal results and separates crash recovery; Q31 closes Q30's multi-page representation branch while leaving limits open; Q32 includes all three Q25 branches and new Work creation before successful acceptance. Only this register changed; no authority/status writeback, runtime tests or sub-agents were used.

## Round 8 — Read Objects, Work States, Publication and Shared A4 Layout

The user accepted Q33–Q37, refining Q36's wording to make the two final file organizations explicit. This clarification preserves Q31's single-Artifact PNG model and does not add a multi-PNG output model.

<a id="cg04-q33"></a>
### CG04-Q33 — Closed RenderIntent read object

Status: ACCEPTED. The RenderIntent read object contains exactly eight required fields:

| Field | Representation and nullability |
| --- | --- |
| render_intent_id | non-null UuidV4; independent demand identity |
| resume_version_id | non-null UuidV4; exact source |
| render_configuration_id | non-null UuidV4; exact configuration |
| status | non-null PENDING, FULFILLED or FAILED |
| created_at | non-null Common UtcTimestamp; acceptance creation time |
| finished_at | Common UtcTimestamp; null exactly while PENDING |
| artifact_id | UuidV4; non-null exactly while FULFILLED |
| failure_code | stable enum value; non-null exactly while FAILED |

PENDING has null finished_at/artifact_id/failure_code. FULFILLED has a finished_at and published artifact_id with null failure_code. FAILED has a finished_at and stable failure_code with null artifact_id. Clients map the stable failure code to presentation instead of depending on raw renderer error text. Q38 subsequently fixes the enum vocabulary; detailed timestamp rules remain open. Internal queues, attempts and paths are excluded from this object. Receipt replay still returns Q22's acceptance rather than this live read object.

Intended normative destination: Derived Work read/result schema and Storage retained terminal-result consistency. Actual writeback: this register only.

<a id="cg04-q34"></a>
### CG04-Q34 — Minimal durable Work lifecycle

Status: ACCEPTED, extended by CG04-Q117. Work states are QUEUED, RUNNING, SUCCEEDED and FAILED. QUEUED means durably awaiting a claim; RUNNING means claimed for execution. Normal execution proceeds QUEUED to RUNNING to SUCCEEDED or FAILED. Q117 adds direct QUEUED to FAILED when configuration preflight establishes execution-dependency unavailability, without an intervening claim. SUCCEEDED requires successful Artifact publication; rendering bytes alone is insufficient.

Crash recovery may requeue unfinished Work only after establishing that the previous executor can no longer publish. Terminal Work is not reopened. Q43/Q44, as refined by Q48, define per-claim fencing identity and a policy-controlled claim limit with initial default 3; concrete recovery ownership and exceptional transitions remain open. Do not add separate RENDERED or PUBLISHING business states; necessary internal file preparation does not establish a successful public Artifact.

Intended normative destination: Derived Work lifecycle and Storage state/recovery consistency. Actual writeback: this register only.

<a id="cg04-q35"></a>
### CG04-Q35 — Atomic successful publication and fulfillment

Status: ACCEPTED. One successful publication database transaction commits the Artifact metadata and its RenderManifest, the Work's successful result and Artifact binding, and fulfillment of every still-PENDING dependent RenderIntent with that same Artifact ID.

Artifact bytes must first complete durable preparation and validation. Only the database publication commit makes the Artifact public; precommit files and reserved IDs do not. A crash after file persistence but before database commit is handled by later Storage recovery clauses, not by prematurely exposing the Artifact or declaring Work success. Q41 subsequently fixes acceptance/terminal-commit ordering; its concrete enforcement, physical file ordering and recovery details remain open.

Intended normative destination: Derived Work publication transaction, Materials output identity and Storage file/database recovery. Actual writeback: this register only.

<a id="cg04-q36"></a>
### CG04-Q36 — Shared complete A4 pages with distinct final file organization

Status: ACCEPTED with user refinement. For the same exact source and matching layout-affecting configuration inputs, PDF and PNG preserve identical page content, page order and pagination results. A common A4 layout produces the complete ordered pages before the selected representation is assembled.

- PDF is a normal multi-page A4 document with independent pages and page breaks.
- PNG rasterizes those same complete pages and concatenates them vertically in page order into one long PNG image.
- PNG does not reflow the document, eliminate page boundaries or crop later pages. Preserve each complete page, including its layout boundary, under Q31.

Boundary example: a three-page layout produces a three-page PDF or one PNG containing complete Page 1, Page 2 and Page 3 in that order. This does not require a public multi-PNG Artifact model. A shared internal intermediate representation is allowed but is not automatically a published Artifact. Q46 subsequently fixes page joins/background; rasterization settings, limits and renderer selection remain open. Matching layout does not merge configuration identities or grant cross-configuration Artifact reuse under Q3/Q9.

Intended normative destination: Materials layout, PDF and PNG representation/configuration rules. Actual writeback: this register only.

<a id="cg04-q37"></a>
### CG04-Q37 — Actual byte-integrity verification before Artifact reuse

Status: ACCEPTED. Before an existing Artifact satisfies a new Intent, confirm its payload is readable and verify the complete byte length and SHA-256 against the immutable Artifact metadata. A database row, stored path or file-existence check alone is insufficient reuse evidence.

A candidate failing verification cannot fulfill the new Intent. Continue Q25's selection order through other eligible Artifacts, compatible unfinished Work or new Work. This observation does not guarantee permanent payload availability; subsequent download has its own integrity checks. Exact read/verification race handling and error responses remain open. Corrupt bytes do not rewrite historical fulfillment or the original receipt.

Intended normative destination: Materials reuse/integrity and Storage verified-byte access. Actual writeback: this register only.

Local consistency review: Q33 closes Q27's result fields while preserving receipt/read separation; Q34/Q35 distinguish byte production from committed Artifact publication; Q36 preserves Q21/Q30/Q31 format selection and complete ordered pages without cross-configuration identity reuse; Q37 enforces Q25's available-output condition without promising permanent availability. Only this register changed; no authoritative-document/status writeback, runtime checks or sub-agents were used.

## Round 9 — Failure Vocabulary, Reads and Durable Completion/Discovery

The user accepted Q38–Q42 without amendments.

<a id="cg04-q38"></a>
### CG04-Q38 — Stable terminal Intent failure vocabulary

Status: ACCEPTED. The closed failure_code vocabulary for a FAILED RenderIntent is:

| Value | Meaning |
| --- | --- |
| SOURCE_UNAVAILABLE | An exact historical input actually required for rendering is missing or corrupt; a lineage-only reference does not itself require payload access under Q67 |
| CONFIGURATION_UNAVAILABLE | Required renderer, font or asset support is no longer usable |
| PERMISSION_DENIED | Permissions required for execution are no longer satisfied |
| RENDER_FAILED | Renderer explicitly reports execution failure |
| OUTPUT_INVALID | Output fails required format or integrity validation |
| RESOURCE_LIMIT_EXCEEDED | A specified time, dimension or resource limit is exceeded |
| STORAGE_FAILED | Storage reads or writes required by execution fail; Q125 expands the original Artifact-persistence-only meaning |
| RECOVERY_EXHAUSTED | Interrupted-work recovery reaches its specified limit |
| INTERNAL_ERROR | An unexpected internal failure |

These values describe terminal outcomes after acceptance. They are not automatically HTTP error codes and do not carry raw exception text. Pre-acceptance rejection remains a separate command/HTTP concern. Q125 expands STORAGE_FAILED from the historical Artifact-persistence-only meaning to required execution storage reads/writes; the enum spelling is unchanged. Q108 orders primary versus cleanup failures; no total ordering among every simultaneous failure or numerical limits is inferred from this vocabulary.

Intended normative destination: Derived Work terminal results, consuming Materials/Storage execution failures. Actual writeback: this register only.

<a id="cg04-q39"></a>
### CG04-Q39 — Pure, consistent single-Intent read

Status: ACCEPTED. GET /api/v1/render-intents/{render_intent_id} returns HTTP 200 with Q33's complete object on success. All fields describe one consistent read snapshot; a client cannot observe FULFILLED without its required artifact_id or other impossible state-dependent field combinations.

The operation does not execute, recover or retry Work. After current Workspace access checks, ordinary Resume removal or loss of configuration support for new generation does not hide an accepted Intent's result. Invalid-ID, not-found and other HTTP errors remain subject to later shared protocol definitions. This read does not establish current Artifact byte availability or new-generation permission.

Intended normative destination: Derived Work HTTP reads and Storage consistent retained results, consuming Workspace access. Actual writeback: this register only.

<a id="cg04-q40"></a>
### CG04-Q40 — Atomic failed-Work result propagation

Status: ACCEPTED. One database transaction marks Work FAILED with its stable failure result and marks every still-PENDING dependent Intent FAILED with the corresponding failure classification and terminal time. Do not commit Work failure first and rely on a later step to finish its dependent Intents.

If the database cannot commit, do not claim that the failure result is durable. Subsequent recovery must converge the unfinished state; the original successful acceptance receipt remains unchanged. This rule does not authorize automatic retry of a known rendering failure under Q29. Q45 subsequently fixes uncertain-commit reconciliation; concrete recovery evidence remains open.

Intended normative destination: Derived Work failure transaction and Storage atomic terminal-result persistence. Actual writeback: this register only.

<a id="cg04-q41"></a>
### CG04-Q41 — Acceptance versus terminal-commit arbitration

Status: ACCEPTED. Joining Work and committing its terminal result have a defined concurrent order. If joining commits first, the later success/failure transaction includes the newly committed pending dependency. If the terminal result commits first, the new command repeats selection: bind an eligible published Artifact when reusable, otherwise join another compatible unfinished Work or create new Work.

Never commit a new PENDING Intent attached to an already-terminal Work. The Contract fixes this observable result without selecting a database locking mechanism. Q28's unfinished-work uniqueness and Q32/Q35/Q40 atomic transactions must all hold together. A new command after prior Work failure does not reopen that failed Work or rewrite its existing dependents.

Intended normative destination: Derived Work acceptance/publication concurrency and Storage transaction enforcement. Actual writeback: this register only.

<a id="cg04-q42"></a>
### CG04-Q42 — Durable queued-Work discovery independent of wakeups

Status: ACCEPTED. Persisted Work records are the basis for pending execution. At startup and during operation, the executor can rediscover claimable QUEUED Work. An in-memory queue, notification or post-commit callback may accelerate discovery but cannot be its only source.

A lost wakeup after Q32's successful commit must not permanently strand accepted demand. RUNNING Work still requires the owned interrupted-execution recovery and fencing checks; discovery cannot simply treat it as an ordinary queued task. This decision requires no external message queue and does not choose a polling interval, concurrency level or recovery implementation.

Intended normative destination: Derived Work dispatch/recovery and Storage durable Work discovery. Actual writeback: this register only.

Local consistency review: Q38 keeps terminal results distinct from HTTP rejection; Q39 preserves pure reads and Q33's state-dependent shape; Q40 complements Q35's atomic success without changing original receipts; Q41 closes dependency/terminal races under Q28/Q32; Q42 closes the lost-wakeup gap without bypassing RUNNING ownership. Only this register changed; no authority/status writeback, runtime checks or sub-agent review was performed.

## Round 10 — Claim Fencing, Recovery Bounds, PNG Joins and Configuration Reads

The user accepted Q43–Q47 without amendments.

<a id="cg04-q43"></a>
### CG04-Q43 — Independent claim identity and fenced terminal writes

Status: PARTIALLY SUPERSEDED by CG04-Q117 for the universal scope of the failed-result condition. Historical rule: successful publication and every failed-result commit required matching work_id, attempt_id and RUNNING. That blanket failure condition no longer covers Q117's authorized QUEUED preflight failure, which has no execution claim.

Effective rule: each Work claim generates a new internal attempt_id of type UuidV4 and commits it atomically with QUEUED to RUNNING. Successful publication and failure of a RUNNING execution must match the current work_id, attempt_id and RUNNING state together. The new preflight path does not authorize bypassing this fencing for an already claimed execution.

Once recovery invalidates an old claim, its executor cannot publish an Artifact, mutate Work or finish dependent Intents even if it later returns a result. The attempt identity is not part of the client read object. This establishes the fencing condition without requiring a distributed lease system. Concrete ownership invalidation, recovery-only transitions and file isolation remain open; an attempt token alone does not establish the authority to recover another executor's work.

Intended normative destination: Derived Work claim/publication ownership and Storage conditional atomic transitions. Actual writeback: this register only.

<a id="cg04-q44"></a>
### CG04-Q44 — Policy-bounded execution claims including the first

Status: PARTIALLY SUPERSEDED by CG04-Q48's explicit user correction. Historical accepted rule: each Work had a fixed maximum of three execution claims, including its initial execution. That permanent numeric bound is SUPERSEDED; do not restore it as a Work schema or permanent Contract constraint.

Effective rule: recovery policy supplies max_attempts, initially defaulting to 3 and adjustable later without changing the Work schema. Persist the actual execution-claim count, including the initial claim; restart does not reset it. Claims must respect the applicable policy limit. The last permitted execution may finish normally; reaching the numeric limit alone does not terminate a running attempt. If that execution is interrupted and recovery confirms no committed terminal result, exhaustion produces RECOVERY_EXHAUSTED. Q53 subsequently fixes the applicable limit as a scalar captured on Work creation; changed defaults affect only new Work.

Unchanged scope: this bounds interrupted-execution recovery, not automatic retries of reported rendering failures. Q29 still ends a known rendering failure without using remaining claims. The initial default is a loop-prevention policy, not a measured reliability guarantee. Single-attempt resource limits, concrete recovery evidence and safe handling of prepared files remain open.

Intended normative destination: Derived Work recovery policy and Storage durable claim-count enforcement. Actual writeback: this register only.

<a id="cg04-q45"></a>
### CG04-Q45 — Reconcile uncertain terminal commits before further execution

Status: ACCEPTED. When publication or failure-transaction commit has an uncertain outcome, reread durable Work state before deciding what to do next. If it already succeeded, recognize the committed Artifact/result and do not publish a second output. If it already failed, preserve that terminal result and do not execute again. If it remains unfinished, establish current execution ownership and applicable recovery conditions before continuing.

If the database remains unreadable, retain the unknown-outcome condition; do not assume rollback and rerender. This execution-side reconciliation is distinct from a client's original acceptance receipt replay. It neither adds a public UNKNOWN Work state nor authorizes bypassing Q29 for a known rendering failure whose terminal write is still unresolved.

Intended normative destination: Derived Work execution/recovery and Storage authoritative commit-result reads. Actual writeback: this register only.

<a id="cg04-q46"></a>
### CG04-Q46 — Opaque white PNG pages joined without extra decoration

Status: ACCEPTED. PNG output uses an opaque white page background. Concatenate complete, equal-sized page pixel rectangles vertically in page order. Preserve template page margins; add no inter-page gap, separator line or shadow. Do not crop white margins or stretch pages.

The image's total height is the sum of its page heights. Complete page layouts and dimensions preserve pagination boundaries without an added decorative marker. Resolution, pixel rounding and dimension/resource limits remain open. This refines Q31/Q36's complete-page assembly; it does not alter the PDF's independent A4 pages or introduce additional Artifacts.

Intended normative destination: Materials PNG rasterization/assembly and configuration representation. Actual writeback: this register only.

<a id="cg04-q47"></a>
### CG04-Q47 — Current configuration discovery and retained exact reads

Status: ACCEPTED. Provide GET /api/v1/render-configurations for discovery of configurations currently supporting new generation and GET /api/v1/render-configurations/{render_configuration_id} for a retained exact configuration, including historical configurations no longer supporting new generation.

Present current support separately from the immutable configuration snapshot. Discovery is a point-in-time observation; POST still performs applicable new-request admission, and the client explicitly submits its selected configuration ID. No listing result guarantees that a particular ResumeVersion is admissible. Exact response fields remain open. These are read-only interfaces under Q13 and do not create client configuration mutation or a silent default.

Intended normative destination: Materials configuration HTTP reads/support representation and Storage retained exact snapshots. Actual writeback: this register only.

Local consistency review: Q43 protects the terminal transactions under Q35/Q40; Q44 bounds claims without reviving failed Work or retrying reported renderer failures; Q45 reconciles committed outcomes before recovery and preserves unknown outcomes when Storage is unreadable; Q46 preserves Q36's page content/order/boundaries; Q47 keeps immutable identity, current capability and source admission separate. Only this register changed; no authority/status writeback, runtime checks or sub-agents were used.

## Round 11 — Work Fields and Configurable Recovery Policy

The user refined Q48's attempt_count and explicitly corrected the earlier Q44 bound. At that response Q49–Q52 were not explicitly answered and policy applicability to existing Work remained open. Round 12 subsequently accepts Q49–Q53 and closes those branches.

<a id="cg04-q48"></a>
### CG04-Q48 — Logical Work fields with a policy-controlled attempt limit

Status: ACCEPTED AS AMENDED for the Work-field proposal, subsequently extended by Q53/Q94. The original ten-field proposal gains max_attempts under Q53 and four necessary limit scalars under Q94. The effective logical execution record currently contains these fifteen required fields; additional necessary relationship/storage constraints remain to be closed without adding a public Work API.

| Field | Representation and constraint |
| --- | --- |
| work_id | non-null server-generated UuidV4 |
| resume_version_id | non-null exact source UuidV4 |
| render_configuration_id | non-null exact configuration UuidV4 |
| status | non-null QUEUED, RUNNING, SUCCEEDED or FAILED |
| attempt_count | non-null nonnegative integer; incremented atomically on claim and bounded by this Work's captured max_attempts |
| max_attempts | non-null positive integer under Q54, captured from the current default when Work is created; unchanged for this Work under Q53 |
| max_pages | non-null positive integer, captured at Work creation under Q94 |
| max_png_pixels | non-null positive integer, captured at Work creation; applies to PNG execution under Q94 |
| max_output_bytes | non-null positive integer, captured at Work creation under Q94 |
| timeout_ms | non-null positive integer, captured at Work creation; applies afresh to each attempt under Q94/Q95 |
| current_attempt_id | UuidV4; non-null exactly while RUNNING |
| created_at | non-null Common UtcTimestamp |
| finished_at | Common UtcTimestamp; non-null exactly in a terminal state |
| artifact_id | UuidV4; non-null exactly while SUCCEEDED |
| failure_code | Q38 enum; non-null exactly while FAILED |

Recovery requeue clears the current execution identity but retains the accumulated claim count. Under Q117, direct QUEUED configuration-preflight failure also leaves attempt_count unchanged and current_attempt_id null; FAILED may therefore have attempt_count = 0, or retain claims accumulated before requeue. No fake claim, count reset or new field is required. These are logical execution fields, not an exhaustive physical persistence schema: Storage may retain necessary recovery evidence. No client Work API follows from this record.

The proposed 0–3 structural range was NOT ACCEPTED. The user explicitly replaces Q44's permanent three-claim bound with policy-controlled max_attempts and initial default 3. Changing that default to 2 or 4 must not require changing the Work schema or its permanent structural range. The cumulative count records actual claims and must not be reset or rewritten to conceal history.

The initial open boundary concerned changes to policy defaults after Work creation. Q53 closes it by capturing only max_attempts on each new Work. A lower later default does not invalidate an existing count, change that Work's captured limit, rewrite completed results or introduce live policy switching.

Intended normative destination: Derived Work logical schema/recovery policy and Storage claim/count persistence. Supersession impact: Q44's fixed numeric ceiling, Q34's reference to that ceiling, and future schema/recovery checks; claim fencing, terminal immutability and Q29's no-retry rule remain unchanged. Actual writeback: this register only.

Local consistency review: the count is a nonnegative cumulative fact and max_attempts belongs to policy; default 3 is not a schema ceiling. Q44 preserves its historical accepted scope and explicitly marks the replaced numeric rule. Policy changes affecting existing Work remain unresolved, and Q49–Q52 are not promoted to accepted decisions. No authoritative-document/status writeback, runtime checks or sub-agents were used.

## Round 12 — Read Protocols, Event Times and a Scalar Recovery Snapshot

The user accepted Q49–Q53 and refined Q53 to retain only the scalar needed for recovery bounds. This extends Q48's logical Work fields without introducing a policy identity/version system.

<a id="cg04-q49"></a>
### CG04-Q49 — One server UTC value for each logical transaction event

Status: ACCEPTED. Use one server UTC timestamp value for each logical transaction event. When acceptance creates both Intent and Work, their created_at values match. Immediate Artifact reuse gives the new Intent equal created_at and finished_at values without modifying the existing Artifact's timestamp.

Successful publication gives the Artifact's created_at and the Work's and newly fulfilled Intents' finished_at fields the same value. A failed-result transaction gives the Work and newly failed Intents the same finished_at value. These represent the corresponding logical transaction event, not a claim about the precise database flush instant or when file writing ended. Prior object timestamps are not rewritten when a new demand joins existing work or reuses an Artifact.

Intended normative destination: Derived Work/Materials timestamps and Storage transaction consistency. Actual writeback: this register only.

<a id="cg04-q50"></a>
### CG04-Q50 — Configuration read envelope separates identity and capability

Status: ACCEPTED. A successful single-configuration read contains exactly two required, non-null fields: configuration, the immutable RenderConfiguration object; and can_generate, a boolean describing current configuration execution support.

The list response is an object with an items array containing entries of that same shape, restricted to can_generate = true for the current observation and ordered by configuration ID. No available configuration yields an empty items array. A true capability observation is not permission or exact-source admission for an arbitrary ResumeVersion and does not replace POST checks. The immutable configuration's internal fields remain open.

Intended normative destination: Materials configuration HTTP response/capability schema. Actual writeback: this register only.

<a id="cg04-q51"></a>
### CG04-Q51 — Retained Artifact metadata read independent of payload availability

Status: ACCEPTED. GET /api/v1/artifacts/{artifact_id} returns HTTP 200 with Q16's complete Artifact object after applicable access checks. Legally retained metadata for a published Artifact remains readable even if its payload is later missing.

Metadata-read success does not promise downloadable bytes and does not trigger repair, regeneration or replacement. A reserved but unpublished ID is not readable. Required metadata integrity and permission checks still apply; this is not permission to expose malformed metadata. Detailed HTTP errors remain open.

Intended normative destination: Materials metadata HTTP reads and Storage retained Artifact identity/provenance. Actual writeback: this register only.

<a id="cg04-q52"></a>
### CG04-Q52 — Shared preview/download content operation

Status: ACCEPTED. GET /api/v1/artifacts/{artifact_id}/content has an optional disposition query parameter with exactly two permitted values, inline and attachment; omission defaults to inline. Both variants return the same original persisted Artifact bytes, with the presentation/download distinction expressed through response headers rather than on-demand conversion.

Content-Type matches Artifact.media_type. The filename is artifact-{artifact_id}.pdf for PDF or artifact-{artifact_id}.png for PNG, independent of Resume text. Q55/Q56 subsequently fix verified-snapshot serving and initial full-response/no-store behavior; detailed HTTP error handling remains open. Content reads remain subject to Q20/Q37 and do not generate or repair output.

Intended normative destination: Materials content HTTP protocol and Storage exact-byte serving. Actual writeback: this register only.

<a id="cg04-q53"></a>
### CG04-Q53 — Capture only max_attempts on each new Work

Status: ACCEPTED with user refinement. At Work creation, capture and persist the actual max_attempts scalar from the current recovery default alongside attempt_count. Later default changes apply only to newly created Work; existing Work keeps its captured limit. The initial default is 3 under corrected Q44, not a permanent structural maximum.

Do not introduce recovery_policy_id, a policy version, a complete strategy snapshot or a Policy entity for this limit. No new client parameter or change of RenderConfiguration identity follows from it. The scalar is part of the new Work record created inside Q32's acceptance transaction, not a later enrichment step. Subsequent Q91 extends lifecycle stability to other necessary execution-limit scalars; this decision does not prohibit that scoped extension or require a full policy object.

Boundary example: Work created with max_attempts = 3 keeps that limit after the installation default becomes 2; newly created Work captures 2. Joining the existing Work does not replace its limit. Neither a default increase nor a decrease resets attempt_count or revives a terminal Work. Q54 subsequently fixes positive-integer validation and the atomic claim condition.

Intended normative destination: Derived Work recovery/Work schema and Storage atomic scalar capture. Impact: add max_attempts to Q48's logical fields and close Q44/Q48's policy-applicability branch. Actual writeback: this register only.

Local consistency review: Q49 preserves immutable prior timestamps; Q50 keeps capability outside the immutable snapshot; Q51/Q52 distinguish retained metadata from readable content and preserve pure reads; Q53 captures the minimum recovery scalar atomically without creating a Policy entity or changing configuration/work reuse identity. Q44/Q48 and the current frontier were reconciled. Only this register changed; no authority/status writeback, runtime checks or sub-agents were used.

## Round 13 — Scalar Validation, Verified Serving and Minimal Configuration Shape

The user accepted Q54–Q58 with Q56/Q57 amended. The proposed mandatory Accept-Ranges: none header and speculative assets field were NOT ACCEPTED; neither was an earlier accepted rule requiring supersession.

<a id="cg04-q54"></a>
### CG04-Q54 — Positive captured limit and atomic bounded claim

Status: ACCEPTED. max_attempts is a positive integer. attempt_count starts at zero and obeys 0 <= attempt_count <= max_attempts for that Work's captured limit. A claim transaction may increment the count, create the new execution identity and enter RUNNING only when attempt_count < max_attempts.

Do not silently truncate an invalid recovery default or replace it with 3. This validates the configured scalar without restoring Q44's superseded fixed structural ceiling. Exact installation-error presentation and storage scalar representation remain implementation/interface details to close where consumed.

Intended normative destination: Derived Work recovery scalar/claim invariants and Storage atomic bounded increment. Actual writeback: this register only.

<a id="cg04-q55"></a>
### CG04-Q55 — Serve the same complete verified byte snapshot

Status: ACCEPTED. Before sending successful response headers or body, obtain a stable byte snapshot and verify its full length and SHA-256 against Artifact metadata. Send that same verified snapshot. Do not verify a pathname and then reopen it to stream potentially replaced bytes.

An implementation may use bounded buffering or a temporary snapshot; resource limits and the concrete mechanism remain open. An integrity failure detected by this validation returns an error, not a partial successful Artifact response. This is an exact-byte and check/use consistency guarantee, not a promise that a network connection cannot fail during transfer. It does not authorize material mutation, repair or generation on GET.

Intended normative destination: Materials content integrity and Storage stable snapshot/serving obligations. Actual writeback: this register only.

<a id="cg04-q56"></a>
### CG04-Q56 — Full-content first-release responses with no-store

Status: ACCEPTED AS AMENDED by the user. In M2's first release, Range does not produce a 206 response: ignore it and return the full content with HTTP 200 on a successful content request. Send Cache-Control: no-store. Partial responses and cache validators are not first-release features under the accepted proposal.

Accept-Ranges: none is NOT a required Contract response header. Whether the HTTP implementation sends that advisory header is its choice. The proposed mandatory header was never accepted. The existing RFC research supports the protocol option but does not establish actual browser/PDF-viewer acceptance; that verification remains pending. Other access, validation and integrity failures still return their errors rather than 200.

Intended normative destination: Materials first-release content HTTP response/cache rules. Actual writeback: this register only.

<a id="cg04-q57"></a>
### CG04-Q57 — Six-field immutable configuration without speculative assets

Status: ACCEPTED AS AMENDED by the user. RenderConfiguration has six required, non-null top-level fields:

| Field | Responsibility |
| --- | --- |
| render_configuration_id | Independent immutable identity |
| schema_version | Configuration representation version |
| template | Exact template and version |
| renderer | Exact complete rendering/rasterization pipeline description |
| fonts | Mapping from logical fonts to fixed font assets |
| output | PDF/PNG representation and format-specific parameters |

Do not include assets or an empty assets array for hypothetical future consumers. Fonts are already represented by fonts; no concrete non-font v1 asset consumer has been established. If subsequent focused renderer/template research demonstrates a required logo, fixed image or other non-font asset, revisit that specific scope through a new explicit decision. This does not grant permission to hide output-affecting asset dependencies from configuration provenance.

The proposed seven-field shape was NOT ACCEPTED. Nested fields, exact renderer and actual font assets remain dependent on focused research. can_generate stays outside the immutable configuration under Q50. Q3's requirement to identify relevant rendering dependencies remains effective; Q57 removes an unused generic container, not exact provenance of dependencies actually consumed.

Intended normative destination: Materials immutable configuration schema and dependency provenance. Actual writeback: this register only.

<a id="cg04-q58"></a>
### CG04-Q58 — Stable application-delivered configuration registration

Status: ACCEPTED. Each application-delivered configuration has an explicit fixed UuidV4 assigned in the shipped catalog. Restart or repeat registration preserves that ID. The immutable content for an existing ID must match exactly; changed content requires a new ID while the old snapshot is retained.

If registration encounters the same ID with different immutable content, reject the overwrite and report the conflict. Do not generate new IDs on every startup or derive configuration identity from a content hash. Registration conflict presentation and the final immutable equality encoding remain open; this decision does not add client configuration mutation.

Intended normative destination: Materials configuration publication/identity and Storage idempotent retained registration. Actual writeback: this register only.

Local consistency review: Q54 uses Q53's captured scalar rather than a permanent numeric ceiling; Q55 preserves exact bytes and pure reads; Q56 leaves the advisory header optional; Q57 excludes the unaccepted assets container while retaining actual dependency provenance; Q58 preserves independent immutable configuration identity under Q3/Q13. Only this register changed. One focused read-only renderer/font fact check was requested for the next configuration branch; no broad authority review, implementation, installation or runtime checks were performed.

## Round 14 — Font Fidelity, Controlled Inputs, Empty Output and Validation

The user accepted Q59–Q63 without amendments. Concrete renderer versions, font files, pagination algorithms and resource limits are not selected by these behavioral constraints.

<a id="cg04-q59"></a>
### CG04-Q59 — Explicit font resolution without silent substitution or glyph loss

Status: ACCEPTED. Render using the configuration's specified font mapping. Do not silently substitute host-system fonts or undeclared fallback fonts. Required font unavailability discovered after acceptance is CONFIGURATION_UNAVAILABLE. A font that loads but cannot correctly render required visible glyphs produces OUTPUT_INVALID.

Do not publish a successful Artifact containing replacement boxes, blank substitutions or omitted visible glyphs caused by that failure. Exact font files and supported coverage remain research-dependent. These terminal codes do not by themselves define pre-acceptance HTTP errors. This decision does not introduce a fallback chain or a new asset container.

Intended normative destination: Materials font fidelity/validation and Derived Work terminal failure classification. Actual writeback: this register only.

<a id="cg04-q60"></a>
### CG04-Q60 — Rendering consumes controlled local inputs only

Status: ACCEPTED. Generation does not access the network. It consumes the resolved exact sources, fixed template and configuration-specified local fonts. URLs in Resume content are document data and do not trigger resource fetching.

Content cannot choose arbitrary local filesystem paths and cannot execute as HTML or script. Missing rendering dependencies produce an explicit failure rather than an on-demand network download. The rule governs rendering resource access; it does not authorize implementation of a browser/platform automation capability or change existing source authority.

Intended normative destination: Materials rendering input/resource boundary and Derived Work execution constraints. Actual writeback: this register only.

<a id="cg04-q61"></a>
### CG04-Q61 — Legally empty saved sources produce a complete page

Status: ACCEPTED. A legally empty saved ResumeVersion is eligible for generation subject to the already-owned source/root/configuration/access admission rules. Do not add an undefined content-completeness gate or new mandatory career/contact content.

Render only actually saved content and the fixed template; do not invent example experiences, placeholder facts or fill missing content from other sources. Even if layout has no body content, PDF has at least one complete A4 page and PNG contains the corresponding complete page. This is the output boundary for empty legal input, not a waiver of other generation checks or downstream eligibility rules.

Intended normative destination: Materials empty-source output/admission, consuming legal Resume saved-state semantics. Any high-level owner reconciliation remains subject to the user's explicit writeback process. Actual writeback: this register only.

<a id="cg04-q62"></a>
### CG04-Q62 — Complete flow without silent shrinking or clipping

Status: ACCEPTED. Normal overflow wraps and paginates while preserving the saved font size and line height. Long paragraphs may span pages. Otherwise unbreakable long text uses explicit line-breaking rules instead of being clipped.

If complete presentation cannot fit the supported dimension/resource limits, fail explicitly. Do not silently reduce font size, change line height, truncate content or omit later pages to manufacture success. Precise wrapping and pagination rules remain dependent on template/rendering research; this decision does not choose them or guarantee arbitrary input size can render successfully.

Intended normative destination: Materials layout fidelity/overflow and Derived Work output/resource failures. Actual writeback: this register only.

<a id="cg04-q63"></a>
### CG04-Q63 — Format validation before successful publication

Status: ACCEPTED. Before publication, validate the actual output format independently of its byte hash. PDF must parse completely, be unencrypted, have at least one page and use the required A4 dimensions for every page. PNG must decode completely and have dimensions matching this execution's page count and rasterization result. Both must match the selected configuration and MIME type, be complete and remain within specified limits.

SHA-256 establishes byte integrity rather than format conformance. Format-validation failures produce OUTPUT_INVALID; an exceeded explicit resource limit remains RESOURCE_LIMIT_EXCEEDED under Q38. Format validation is not a substitute for full visual acceptance. Exact validators, dimension tolerances and operational limits remain open; no renderer or browser acceptance was executed by this decision.

Intended normative destination: Materials output conformance and Derived Work pre-publication validation/failure handling. Actual writeback: this register only.

Local consistency review: Q59 uses Q38's accepted terminal categories without silently assigning HTTP rejection codes; Q60 closes default resource-fetch behavior within controlled rendering; Q61 preserves legally empty sources and Q31/Q36's complete-page output; Q62 protects saved settings and content from silent loss; Q63 distinguishes byte integrity, format conformance and visual proof under Q35/Q55. Only this register changed; no authority/status writeback, new agent review, implementation or runtime checks were performed.

## Round 15 — Configuration Descriptors and Actual Rendering Dependencies

The user accepted Q64–Q68 with Q67 explicitly narrowed to actual rendering inputs. The earlier proposal to resolve and validate every bound Profile/Evidence payload at step 3 was NOT ACCEPTED. Q14's general payload-availability wording is narrowed accordingly; saved authority and complete lineage remain unchanged.

<a id="cg04-q64"></a>
### CG04-Q64 — Fixed template descriptor without another entity

Status: ACCEPTED. template contains template_key and template_version, both required nonempty strings. Together they identify a fixed template implementation. A change to template layout rules requires a new template version and a new RenderConfiguration ID.

Do not add a Template UUID or independent template-management API. Exact string syntax/length constraints and the shipped template implementation/version remain open. This descriptor does not permit replacing saved Resume presentation settings with template defaults.

Intended normative destination: Materials template/configuration definition. Actual writeback: this register only.

<a id="cg04-q65"></a>
### CG04-Q65 — Version the complete rendering pipeline

Status: ACCEPTED. renderer contains pipeline_key and pipeline_version, both required nonempty strings. They identify the complete layout, PDF output, applicable page rasterization and PNG assembly implementation, not just one package in that chain.

The version must be traceable to a fixed implementation and dependency combination. Output-affecting implementation or dependency changes require a new pipeline version and RenderConfiguration ID. Do not add a standalone Renderer entity or API. Concrete toolchain/version combinations and exact string validation remain open and research-dependent.

Intended normative destination: Materials renderer/configuration provenance and execution compatibility. Actual writeback: this register only.

<a id="cg04-q66"></a>
### CG04-Q66 — Minimal format-specific output shape

Status: ACCEPTED. PDF output contains media_type = application/pdf. PNG output contains media_type = image/png and a positive integer page_width_px for the complete A4 page. Derive the single-page pixel height from A4 proportions and an explicitly defined rounding rule; total height is that page height multiplied by page count.

Do not add independently competing DPI, scale or client output parameters. Exact pixel defaults, rounding and supported limits remain open for focused rendering research. Q46's opaque white complete-page assembly and Q36's shared pagination remain effective. Format selection is still owned by the exact RenderConfiguration.

Intended normative destination: Materials output/configuration shape and raster dimensions. Actual writeback: this register only.

<a id="cg04-q67"></a>
### CG04-Q67 — Ordered admission checks only actual historical render inputs

Status: ACCEPTED AS AMENDED by the user. After Q15's access/input validation and success-receipt lookup miss, new-request admission proceeds in this order:

1. Resolve the exact ResumeVersion and its owning Resume.
2. Check that the owning Resume is ACTIVE.
3. Resolve and validate only the exact historical sources actually needed for this rendering operation.
4. Resolve the exact RenderConfiguration.
5. Check current execution support for that configuration.
6. Select reusable Artifact, compatible unfinished Work or new Work under Q25/Q32.

Report the first failure encountered in this order; detailed HTTP codes remain open. Step 3 does not re-admit Evidence as ACTIVE/current and does not read or validate every Evidence payload merely because its reference appears in RenderManifest. Resume-local expression is already stored in ResumeVersion; lineage-only inputs must not be promoted to extra execution dependencies. Preserve Q2/Q6's complete deterministic lineage projection without using that projection as justification to reload all fact payloads.

Boundary: this does not declare all Evidence data lineage-only. Current RES-010 keeps structured company/school/role/dates/project_url in the bound exact EvidenceVersion, while PRO-006 supplies fixed contact values from the exact ProfileVersion. Any such fields actually rendered remain required exact inputs. Q69 subsequently fixes the input/dependency mapping. Existing Candidate readers and Save validation are not silently weakened or changed. A needed projection/interface must be specified at its actual producer/consumer boundary rather than inferred from a generic full-payload reader.

Intended normative destination: Derived Work ordered admission and Materials actual render-input dependencies, with only necessary Resume/Profile/Evidence reader interfaces. Refinement impact: Q14's broad payload wording and Q38's SOURCE_UNAVAILABLE interpretation are scoped to actual required inputs. Actual writeback: this register only.

<a id="cg04-q68"></a>
### CG04-Q68 — Finished exact output survives loss of new-generation support

Status: ACCEPTED. A current can_generate = false observation alone does not prevent publication of output already produced by an accepted execution. Publication may succeed when the execution identity remains valid, permissions are satisfied, the output genuinely corresponds to its bound exact configuration, and all required validation passes.

Stopping support for new requests does not retroactively invalidate a previously completed lawful execution. If a required dependency is lost before generation can finish, fail as CONFIGURATION_UNAVAILABLE instead. This distinction does not bypass claim fencing, output provenance/integrity or applicable permission checks.

Intended normative destination: Derived Work publication admission and Materials configuration capability/result distinction. Actual writeback: this register only.

Local consistency review: Q64–Q66 refine descriptors without selecting unverified tools or numeric raster defaults; Q67 narrows material input requirements while preserving full lineage and RES-010/PRO-006 structured/contact ownership; Q68 separates current generation capability from validation of completed exact output. Relevant Resume/Profile clauses were read to identify the dependency boundary. Only this register changed; no authority/status writeback, sub-agent review, implementation or runtime checks were performed.

## Round 16 — Actual Input Mapping, Saved Links, Reuse and Retention

The user accepted Q69–Q73, refining Q70's link-target boundary, and directed ten questions per subsequent round under CG04-S5.

<a id="cg04-q69"></a>
### CG04-Q69 — Exact field ownership defines actual render dependencies

Status: ACCEPTED. Use this render-input mapping:

| Rendered or recorded value | Source |
| --- | --- |
| Local expression, paragraphs/lists/marks, order, optional Header and document settings | ResumeVersion |
| Fixed name, phone and email | Exact ProfileVersion |
| Actually displayed company/school/role/dates/project URL and other owned structured fields | Corresponding fields from the exact EvidenceVersion |
| Manifest lineage | Deterministic projection of ResumeVersion reference relationships |

Do not read Evidence expression content to fill Resume-local content. Do not validate unrelated payload merely because a reference appears in lineage. Close the necessary structured-field reading capability at its actual producer/consumer interface; do not silently change existing Candidate Save or GET behavior. Required ownership/reference checks remain intact. The physical storage read strategy and consumed interface clauses remain to be specified.

Intended normative destination: Materials render-input definition and necessary Resume/Profile/Evidence/Storage interfaces. Actual writeback: this register only.

<a id="cg04-q70"></a>
### CG04-Q70 — Preserve admitted LINK targets without widening schemes

Status: ACCEPTED with user refinement. For a LINK legally saved in ResumeVersion, PDF preserves clickable behavior using its exact admitted target URL, while PNG preserves the same visible text and styling without interactive link behavior. Do not append target URL text merely to compensate for PNG's lack of interaction, and do not fetch links during rendering.

Clickable PDF links are limited to targets already admitted by the Resume LINK Contract. Materials does not widen permitted URL schemes because PDF URI actions can represent additional values; file:, scripts and other targets not admitted by the source Contract remain disallowed. Preserve the saved target without inventing extra normalization or replacement. This decision grants no additional clickable-target surface for unrelated raw document strings or structured fields.

Intended normative destination: Materials PDF/PNG LINK representation consuming RES-006/008 and COM-042, without changing their URL admission. Actual writeback: this register only.

<a id="cg04-q71"></a>
### CG04-Q71 — Stable ordering among eligible reusable Artifacts

Status: ACCEPTED. Among candidate Artifacts for reuse, order by created_at ASC and then canonical artifact_id ASC. Select the first candidate satisfying compatibility, access and full byte-integrity verification. Skip a candidate failing those checks rather than merging identities or relying on incidental database order.

This is a defined selection order, not an inference about source-version chronology or a guarantee that equivalent outputs have equal bytes. Q25's Artifact-before-Work priority and Q37's verification remain effective.

Intended normative destination: Materials compatibility/reuse selection and Derived Work acceptance. Actual writeback: this register only.

<a id="cg04-q72"></a>
### CG04-Q72 — Retain published Artifacts without first-release deletion or TTL

Status: ACCEPTED. M2's first release has no Artifact deletion command, TTL or automatic cleanup of published Artifacts. Ordinary Resume removal and configuration upgrades do not delete them.

Cleanup of unpublished temporary/orphan files belongs to a separate recovery definition. Retention is not a guarantee against physical file loss or corruption; Q20/Q51/Q55 continue to govern truthful reads and integrity. This does not introduce a new erasure, backup or restore product, nor authorize deleting success receipts.

Intended normative destination: Materials published-Artifact retention and Storage managed-file lifecycle/recovery. Actual writeback: this register only.

<a id="cg04-q73"></a>
### CG04-Q73 — Output conformance without a byte-for-byte replay guarantee

Status: ACCEPTED. Require output content, styling and pagination to conform to the fixed exact configuration; do not currently promise byte-for-byte equality across repeated executions of the same exact source/configuration.

Compute each Artifact's SHA-256 from its actual persisted bytes. Equal inputs do not excuse byte-integrity checks or establish an expected hash. A stronger reproducibility guarantee requires later renderer evidence and an explicit decision. This does not relax layout/content fidelity, exact configuration provenance or identity/reuse rules; it distinguishes those guarantees from identical file serialization.

Intended normative destination: Materials output guarantees and Artifact integrity/provenance. Actual writeback: this register only.

Local consistency review: Q69 preserves Q67's actual-input scope and M1 field authority; Q70 consumes admitted LINK targets without extending COM-042; Q71 selects among independent identities without treating sort order as lineage; Q72 separates published retention from unpublished-file recovery; Q73 preserves conformance and actual-byte SHA-256 without an unverified serialization promise. Only this register changed; no authority/status writeback, new agent review, implementation or runtime tests were performed.

## Round 17 — Source Interfaces, Protocol Details and Safe Local Execution

The user accepted Q74–Q83, amending Q82/Q83. A permanent one-Work concurrency limit and unconditional forcible renderer termination were NOT ACCEPTED. The chosen renderer execution model remains open.

<a id="cg04-q74"></a>
### CG04-Q74 — Internal exact rendering-source projection interface

Status: ACCEPTED. Provide an internal Materials source-reading capability for Q69's exact render inputs and complete lineage. It may read only the required structured Evidence projection; unused Evidence expression content must not become an extra validation prerequisite.

Validate the actual versions, ownership and fields consumed. Failure to obtain a required field fails the affected operation. Preserve existing Candidate Save/GET full-validation semantics and introduce no new public HTTP endpoint for this capability. Concrete projection field shapes and persistence access must close both producer and consumer requirements rather than treating a generic full-payload reader as interchangeable.

Intended normative destination: Materials and necessary Resume/Profile/Evidence/Storage internal interfaces. Actual writeback: this register only.

<a id="cg04-q75"></a>
### CG04-Q75 — Configuration descriptor scalar constraints

Status: ACCEPTED. RenderConfiguration.schema_version is integer 1. template_key and pipeline_key match ^[a-z][a-z0-9_]{0,63}$. template_version and pipeline_version match ^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$. Values are compared exactly without trimming or case conversion; version strings need not use SemVer. render_configuration_id uses Common UuidV4.

These representation constraints do not identify an installed implementation or permit changing the immutable meaning of an existing key/version pair. Existing Common wrong-type and invalid-scalar rules remain applicable.

Intended normative destination: Materials configuration scalar definitions consuming Common conventions. Actual writeback: this register only.

<a id="cg04-q76"></a>
### CG04-Q76 — Materials-specific fingerprint prefix with existing value encoding

Status: ACCEPTED. The request fingerprint is lowercase SHA-256 over UTF8("JobHunter:SL02:Materials:1\n") followed immediately by the SAV-010 deterministic value encoding of ["RENDER_REQUEST", null, input]. In this prefix notation \n is exactly one LF byte. input is the admitted object containing exactly resume_version_id and render_configuration_id.

Exclude request_id and all server-generated values. Reuse the existing value encoding rather than inventing JSON-spelling equality. Preserve all existing M1 prefixes, fingerprint values, command namespaces and receipt behavior. The Materials operation/request_id key remains Q5's independent namespace. Shared-encoding ownership/reference placement must be reconciled during authorized publication without changing existing consumers.

Intended normative destination: Derived Work command fingerprint and the consumed shared encoding interface. Actual writeback: this register only.

<a id="cg04-q77"></a>
### CG04-Q77 — Command and metadata-read HTTP error mapping

Status: ACCEPTED. Use the Common error object with these owned mappings and Q15/Q67's applicable processing order:

| Trigger | HTTP and code |
| --- | --- |
| Supplied body source/configuration ID absent | 422 VALIDATION_ERROR with INVALID_REFERENCE at the field |
| Requested GET object absent | 404 NOT_FOUND |
| Owning Resume REMOVED for new generation | 409 INVALID_STATE |
| Existing configuration not currently executable | 409 RENDER_CONFIGURATION_UNAVAILABLE |
| Same command key with different admitted input | 409 REQUEST_CONFLICT |
| Actually detected corrupt required persisted reference | 500 INTERNAL_ERROR |
| Storage write failure with established non-commit | 503 STORAGE_UNAVAILABLE |
| Commit outcome cannot be established | 503 OUTCOME_UNKNOWN |

Do not misclassify a corrupt internal dependency as an invalid client-supplied ID. Proposed new vocabulary receives its formal shared/owner definitions only during authorized normative publication; these are accepted design mappings, not already-published Common clauses. Transport details and remaining validation triggers remain to be completed.

Intended normative destination: Derived Work/Materials HTTP mappings and necessary Common vocabulary. Actual writeback: this register only.

<a id="cg04-q78"></a>
### CG04-Q78 — Distinguish unavailable, corrupt and temporarily unreadable content

Status: ACCEPTED. When Artifact metadata exists, the content operation returns 409 ARTIFACT_UNAVAILABLE for missing payload, 500 ARTIFACT_INTEGRITY_FAILED for byte-length or hash mismatch, and 503 STORAGE_UNAVAILABLE for a temporary storage-read failure.

These errors do not mutate Artifact, Intent or receipt state and do not trigger rerendering. Q51's metadata-read result remains distinct. Use the Common error representation; required vocabulary publication is still pending. Missing Artifact metadata itself follows Q77's requested-object absence rule.

Intended normative destination: Materials content HTTP failures and Storage availability/integrity classification. Actual writeback: this register only.

<a id="cg04-q79"></a>
### CG04-Q79 — Managed local files isolated by execution identity

Status: ACCEPTED. Keep material files inside managed subdirectories of the current data_directory. Isolate temporary files by Work/attempt. Published files bind to their Artifact identity and cannot be overwritten.

Storage chooses actual directory names. Clients cannot supply filesystem paths, and public objects do not expose physical paths. This reuses existing local data-directory ownership rather than defining another Workspace identity or external object store. Directory initialization and concrete file-operation safeguards remain to be closed with the actual persistence implementation requirements.

Intended normative destination: Storage material file placement/isolation and Materials path-free interfaces. Actual writeback: this register only.

<a id="cg04-q80"></a>
### CG04-Q80 — Durable files precede the atomic public database result

Status: ACCEPTED. Write an attempt-private temporary file, completely validate it and establish file durability, place it at its final location without overwriting another file and establish required directory durability, then commit Q35's Artifact/Work/Intent publication transaction.

Temporary and final locations must support the required safe file operations. Before database commit the file remains unpublished and inaccessible through the Artifact API. Do not commit successful public records before completing the file. A crash before commit can leave an unpublished file for Q81's recovery, not a half-published Artifact. Concrete OS/filesystem primitives and durability evidence remain to be checked before implementation readiness.

Intended normative destination: Storage file/database publication order and Derived Work fenced commit. Actual writeback: this register only.

<a id="cg04-q81"></a>
### CG04-Q81 — Discard abandoned unpublished output and rerun within the captured limit

Status: ACCEPTED. First-release recovery does not resume partially rendered files or automatically register an unpublished file as an Artifact. After confirming no terminal result was committed and the old executor has lost publication authority, a Work with remaining claims can be queued for fresh execution; an exhausted Work fails under the existing recovery rules.

Delete old files only after confirming no valid reference and that the old executor is no longer writing those files. Retain files when this is uncertain. Already committed output is recognized under Q45, never discarded as abandoned. Q83 subsequently makes physical termination conditional on the execution model; loss of publication authority alone does not prove file-writer termination or authorize early deletion.

Intended normative destination: Derived Work interrupted execution and Storage unpublished-file recovery. Actual writeback: this register only.

<a id="cg04-q82"></a>
### CG04-Q82 — Default concurrency without a permanent Contract ceiling

Status: ACCEPTED AS AMENDED by the user. The initial executor default is default_concurrency = 1. It is an adjustable execution configuration, not a normative permanent limit of one Work per Workspace and not a Work schema constraint.

Contract invariants must hold when concurrency changes: compatible unfinished-Work uniqueness, independent demand identity, atomic claim counts, attempt fencing and correct terminal/publication transactions. Changing the default to two slots must not require changing those semantics or the Work schema. No external queue follows from configurable concurrency. The original permanent-concurrency proposal was NOT ACCEPTED.

Intended normative destination: Derived Work concurrency invariants; the initial executor default belongs in the implementation transfer/configuration guidance at authorized publication. Actual writeback: this register only.

<a id="cg04-q83"></a>
### CG04-Q83 — Mandatory timeout fencing with model-dependent termination

Status: ACCEPTED AS AMENDED by the user. Execution has a finite time budget. On timeout the current attempt loses publication eligibility and cannot subsequently publish an Artifact or finish an Intent. Timeout classification remains RESOURCE_LIMIT_EXCEEDED. Q85 subsequently fixes the atomic coordinator transaction for revocation and terminal failure.

If rendering runs in an isolatable, terminable process, terminate that execution. Do not unconditionally promise forcible termination for a trusted synchronous/in-process renderer that cannot safely support it. Publication fencing is mandatory across supported models; physical termination is required where the adopted model supports it. M2 has not selected a universally terminable subprocess model, and the earlier blanket requirement was NOT ACCEPTED.

A logically timed-out Work and a physically exited renderer are different facts. Preserve necessary file/resource isolation while a renderer can still write or return; this does not grant a late callback authority to overwrite the owned result. Q86 subsequently fixes continued resource accounting; concrete timeout supervision and timing remain open. This is internal resource control, not a user CANCEL command.

Intended normative destination: Derived Work timeout/publication ownership and implementation-model obligations, with Storage isolation. Actual writeback: this register only.

Local consistency review: Q74 preserves actual-input projection without weakening M1 readers; Q75/Q76 constrain representation and encoding without changing old fingerprints; Q77/Q78 distinguish supplied absence, persisted integrity and commit uncertainty; Q79–Q81 preserve unpublished/published and live-writer boundaries; Q82 keeps a default separate from a structural invariant; Q83 preserves mandatory fencing without assuming killability. Only this register changed; no authority/status writeback, agent review, implementation or runtime checks were performed.

## Round 18 — Coordinator Authority, Bounded Inputs and Stable Execution Constraints

The user accepted Q84–Q93, refining Q84/Q87/Q91. Byte-only renderer output and a permanent 4 KiB request-size ceiling were NOT ACCEPTED. Q91 also excludes silently changing execution constraints between attempts of one Work.

<a id="cg04-q84"></a>
### CG04-Q84 — Renderer produces candidate output; Coordinator owns publication

Status: ACCEPTED with user refinement. Renderer produces attempt-scoped candidate output, either bytes or a controlled temporary file, or reports failure. Coordinator validates the candidate, enforces attempt fencing and owns the terminal/publication transaction.

Renderer cannot directly publish an Artifact, modify Work or finish an Intent. This responsibility split applies to in-process and separate-process implementations without promising OS-level isolation. Do not require all candidate output to reside in memory; Q79/Q80's controlled attempt-scoped files remain valid. Candidate references do not become public Artifact IDs or caller-chosen paths.

Intended normative destination: Derived Work renderer/coordinator interface and Storage candidate isolation. Actual writeback: this register only.

<a id="cg04-q85"></a>
### CG04-Q85 — Atomic timeout failure versus successful publication

Status: ACCEPTED. Coordinator conditionally matches the current work_id, attempt_id and RUNNING state, atomically records RESOURCE_LIMIT_EXCEEDED failure for Work and its pending dependent Intents, and clears the current execution identity on timeout.

Successful publication must also check that the execution time budget has not expired. An already committed successful result cannot be changed by delayed timeout handling. After committed timeout failure, a late candidate cannot publish. Preserve Q45's uncertain-commit reconciliation rather than guessing whether a competing result committed. The timer clock/start boundary remains to be defined.

Intended normative destination: Derived Work timeout/publication arbitration and Storage conditional terminal transactions. Actual writeback: this register only.

<a id="cg04-q86"></a>
### CG04-Q86 — Resource occupancy lasts until actual execution exit

Status: ACCEPTED. A timed-out renderer that has not exited still occupies actual execution resources and retains file isolation. Logical Work failure does not release resource accounting or permit unlimited replacement executions.

Release those resources and clean the attempt's files only after execution exits or is safely terminated, with Q81's reference/ownership checks. This does not restore an unconditional killability requirement for in-process execution. Resource accounting follows physical execution facts, while publication eligibility follows the fenced logical state.

Intended normative destination: Derived Work executor resource accounting and Storage attempt-file lifecycle. Actual writeback: this register only.

<a id="cg04-q87"></a>
### CG04-Q87 — Finite configurable request-body limit and strict transport

Status: ACCEPTED with user refinement. Materials command bodies use UTF-8 application/json without compressed request bodies and must have a finite request-body size limit. The initial implementation may use 4 KiB; that number is a default HTTP configuration, not a permanent business Contract ceiling. Changing it does not change the command's three-field semantic shape.

Malformed JSON, duplicate keys or unsupported encoding produce 400 BAD_REQUEST. Exceeding the configured raw byte limit produces 413 REQUEST_TOO_LARGE. Parseable field/type/value errors produce 422 VALIDATION_ERROR. Materials POST accepts no query parameters. Materials GET accepts no body; only the content operation admits its defined disposition query. Apply raw admission before receipt lookup; preserve existing M1 budgets and behavior. A permanent 4 KiB schema/protocol bound was NOT ACCEPTED.

Intended normative destination: Derived Work/Materials HTTP raw admission and implementation-default guidance. Actual writeback: this register only.

<a id="cg04-q88"></a>
### CG04-Q88 — Five-field durable Materials receipt

Status: ACCEPTED. The receipt contains exactly five required, non-null fields: request_id: UuidV4; operation: RENDER_REQUEST; request_fingerprint: Common Sha256Hex under Q76; schema_version: integer 1; and result_snapshot containing Q22's complete original three-field acceptance.

The snapshot request_id must equal the enclosing receipt's request_id. Do not store current Work/Artifact state in the receipt or add a receipt timestamp. This object uses Q5's namespace, Q10's retention and Q32's atomic acceptance. Matching replay returns the stored original acceptance, not an updated execution result.

Intended normative destination: Derived Work receipt schema and Storage retained acceptance integrity. Actual writeback: this register only.

<a id="cg04-q89"></a>
### CG04-Q89 — Transient render-input projection without a new source authority

Status: ACCEPTED. Q74's render-input projection is temporary execution data, not a new persisted MaterialSourceSnapshot identity or copied fact authority. Recovery that re-executes rendering rereads actually required inputs through the accepted exact IDs.

Do not switch to current sources or turn an old temporary file into a new authority snapshot. This preserves exact immutable source consumption while allowing in-memory/temporary execution representations; it does not weaken source permissions or required-input integrity checks.

Intended normative destination: Materials source projection and Derived Work recovery input interface. Actual writeback: this register only.

<a id="cg04-q90"></a>
### CG04-Q90 — Exact half-up A4 pixel-height rounding

Status: ACCEPTED. page_height_px = floor(page_width_px * 297 / 210 + 0.5), using exact rational arithmetic and half-up rounding rather than floating-point-dependent results. total_height_px = page_height_px * page_count.

This fixes the dimension calculation independently of the as-yet-unselected default pixel width and resource limits. Q46's complete-page assembly and Q63's dimension validation consume these exact dimensions.

Intended normative destination: Materials PNG raster dimensions and validation. Actual writeback: this register only.

<a id="cg04-q91"></a>
### CG04-Q91 — Operational limits separate from output identity but stable for Work

Status: ACCEPTED with user refinement. Runtime page-count, total-pixel, output-byte and execution-time limits come from execution configuration rather than immutable RenderConfiguration. Do not introduce a Policy entity for them. Changing operational defaults cannot change an already published Artifact or silently shrink font size, lower configured PNG width or truncate content to meet a limit.

The same Work's retries/recovery must not silently acquire different result-affecting execution constraints when defaults change. Q94 subsequently fixes capture of max_pages, max_png_pixels, max_output_bytes and timeout_ms at Work creation; do not use live defaults for each attempt. Q53's separately captured max_attempts remains effective, and no complete Policy snapshot/ID/version follows from extending scalar stability.

Initial values and verification requirements must be made explicit in the implementation transfer. This decision separates adjustable defaults from stable per-Work execution constraints, not from enforceable finite bounds.

Intended normative destination: Derived Work execution-limit ownership/stability, Materials resource failures and necessary Storage scalar persistence. Actual writeback: this register only.

<a id="cg04-q92"></a>
### CG04-Q92 — Retain Intent and historical Work records in the first release

Status: ACCEPTED. Retain Intents, terminal Work and necessary dependency records without first-release TTL or automatic record cleanup. Do not replace an old Work merely because a new Work has the same source/configuration key.

Preserve the relationship between original receipts, Intent results and actual execution history. Attempt files still follow Q81's cleanup; record retention does not require keeping abandoned temporary bytes. No history-list API follows from this retention rule.

Intended normative destination: Derived Work historical identity/results and Storage record/dependency retention. Actual writeback: this register only.

<a id="cg04-q93"></a>
### CG04-Q93 — Embedded fonts and textual PDF content

Status: ACCEPTED. PDF embeds the fonts actually used, allowing lawful font subsetting. Body content remains textual rather than whole-page screenshot images embedded as PDF pages.

This supports faithful font presentation and basic text extraction without promising any external ATS result. Chosen-font licensing, embedding and Chinese extraction behavior require renderer validation; the decision itself is not experimental evidence. Q73's absence of a byte-for-byte repeatability guarantee remains unchanged.

Intended normative destination: Materials PDF representation and required renderer/font proof. Actual writeback: this register only.

Local consistency review: Q84 preserves file-backed candidates; Q85/Q86 distinguish logical terminal commitment from actual exit; Q87 keeps a finite bound without freezing its initial default; Q88 preserves original acceptance; Q89 avoids a second source authority; Q90 fixes exact dimensions; Q91 preserves constraints across recovery without a Policy entity; Q92/Q93 preserve audit identity and textual output obligations. Only this register changed. A focused read-only font-source check was requested for the remaining font branch; no full authority review, installation, backend/frontend implementation or rendering experiment was performed.

## Round 19 — Required Mark Support and Research-Based Page Tolerance

The user addressed Q99 and Q100 with narrowing amendments. This response was initially recorded without accepting Q94–Q98/Q101–Q103; the user subsequently clarified that those eight recommendations were also accepted, and Round 20 records them. Q104/Q105 remained unanswered at that point and retained their numbers; Round 21 subsequently records their acceptance.

<a id="cg04-q99"></a>
### CG04-Q99 — Support Resume v1 marks without preauthorizing font synthesis

Status: ACCEPTED AS AMENDED by the user. RenderConfiguration must explicitly ensure support for Resume v1's permitted marks and combinations. Keep the four existing logical font choices; their actual files and rendering support must be verified rather than assuming font familiarity proves all native style variants exist.

Do not introduce a synthetic bold/italic policy as an initial Contract mechanism merely because it might be useful. Only if focused research of the selected fonts establishes that synthesis is needed to fulfill the required marks should deterministic synthesis rules be proposed and explicitly settled. The previous general permission to synthesize styles was NOT ACCEPTED. It is also not a permanent prohibition on a later demonstrated and approved solution.

Q135 subsequently authorizes one researched exception for Source Han Sans 2.005R: deterministic synthetic italic over native Regular or native Bold, subject to fixed pipeline provenance and actual PDF/PNG conformance verification. This is not a general synthesis permission and does not authorize synthetic bold or changes to the other three logical fonts.

This decision does not weaken BOLD, ITALIC, UNDERLINE or LINK support, permit silently dropping marks, change logical font enums, select a replacement font or reopen URL schemes. Q59's prohibition on undeclared font substitution remains effective. Exact selected-file/style proof is still pending.

Intended normative destination: Materials supported-input/conformance requirements; implementation-specific style mechanisms only if later research establishes a need and a decision authorizes them. Actual writeback: this register only.

<a id="cg04-q100"></a>
### CG04-Q100 — Fixed A4 pages without an arbitrary permanent tolerance

Status: ACCEPTED AS AMENDED by the user. All PDF pages must be A4, 210 by 297 mm. Other page sizes or automatic page scaling are not admitted. Preserve Q63's format validation and the saved layout constraints.

The proposed permanent 0.01 pt tolerance was NOT ACCEPTED. Determine any necessary PDF numeric-serialization tolerance from the selected renderer's actual output research before specifying its validation rule; do not invent or silently apply a tolerance now. This does not relax the A4 requirement or change PNG's exact integer dimension rule under Q90.

Intended normative destination: Materials PDF page-size conformance and renderer-based validation evidence. Actual writeback: this register only.

Local consistency review: Q99 keeps required marks and existing font choices while leaving unproven style mechanisms open; Q100 preserves A4 and PNG dimension obligations without freezing an arbitrary PDF tolerance. Focused font facts remain candidate-file observations, not acceptance of replacements or synthesis. Unanswered questions retain their numbers. Only this register changed; no authority/status writeback, agent review, implementation or runtime checks were performed.

## Round 20 — Confirmed Limits, Projection and Rendering Representation Rules

The user clarified acceptance of the other eight questions in Q94–Q103. Q99/Q100 keep their amended conclusions from Round 19; Q104/Q105 were not included in this clarification and remained in the next frontier with Q106–Q113, subsequently answered in Round 21.

<a id="cg04-q94"></a>
### CG04-Q94 — Capture four necessary execution-limit scalars

Status: ACCEPTED. At Work creation, capture max_pages, max_png_pixels, max_output_bytes and timeout_ms as positive integers, in addition to max_attempts. Every recovery attempt of this Work uses the captured values; changed defaults affect only new Work. max_png_pixels applies only to PNG execution.

These scalars belong to Q32's atomically created Work record, not a later enrichment or a new Policy entity. Actual initial deployment values still require explicit handoff/configuration documentation; the structural invariant does not freeze arbitrary operational defaults.

Intended normative destination: Derived Work execution limits and Storage atomic scalar capture. Impact: Q48's effective logical record gains four fields; Q91's stability mechanism is closed. Actual writeback: this register only.

<a id="cg04-q95"></a>
### CG04-Q95 — Per-attempt monotonic execution budget

Status: ACCEPTED. Start the execution budget after the claim transaction succeeds. It covers source reading, rendering, validation and the terminal decision before publication; queued time is excluded. Measure elapsed time with a monotonic clock rather than business UTC timestamps that can move backward.

A recovered new attempt starts its own timer using the Work's unchanged timeout_ms. Q45 still governs uncertain transaction completion; a timer is not evidence that a previous commit rolled back. Logical event timestamps remain governed by Q49.

Intended normative destination: Derived Work deadline/publication checks and execution recovery. Actual writeback: this register only.

<a id="cg04-q96"></a>
### CG04-Q96 — Concrete internal rendering-source projection

Status: ACCEPTED. The internal projection contains resume_version, profile_version and evidence_sources. The first two are the exact saved objects under their existing owners. evidence_sources is an array in Resume member order, with each element containing only evidence_item_id, evidence_item_version_id, kind and fields.

Derive kind from the owning Item and consume its corresponding EVD-003 fields shape. Do not include Evidence content, an independent projection ID or a persistence table for the projection. Q69/Q74's actual-input integrity and ownership checks remain required. Empty formal sections produce no members; the existing Resume schema and ordered lineage projection remain unchanged.

Intended normative destination: Materials internal input DTO and the necessary exact Resume/Profile/Evidence read interface. Actual writeback: this register only.

<a id="cg04-q97"></a>
### CG04-Q97 — Preserve saved whitespace and text semantics

Status: ACCEPTED. Rendering must not silently collapse saved consecutive spaces, NBSP or ideographic spaces through default HTML whitespace behavior. Do not trim again, normalize Unicode or interpret text as Markdown.

Apply owned line-wrapping rules without modifying the saved text to make rendering convenient. This consumes RES-007's preserved text rather than adding a new source canonicalization or private expression rewrite.

Intended normative destination: Materials text fidelity consuming Resume local AST semantics. Actual writeback: this register only.

<a id="cg04-q98"></a>
### CG04-Q98 — List identity and numbering survive pagination

Status: ACCEPTED. Each ORDERED_LIST starts at 1 and continues numbering across pages. Splitting one item across pages does not create another number. A new list block starts numbering at 1 again.

UNORDERED_LIST likewise preserves its item relationships across pagination. Fixed template rules own the visual marker style; pagination does not create new business items, IDs or AST nodes.

Intended normative destination: Materials list rendering consuming the unchanged Resume AST. Actual writeback: this register only.

<a id="cg04-q101"></a>
### CG04-Q101 — Single-face static font files in the first release

Status: ACCEPTED. First-release font assets are fixed individual static TTF/OTF files. Do not introduce font collections, variable axes or their configuration fields in this scope. Verify the selected files' SHA-256 values.

Actual logical-font-to-file mappings remain to be selected and verified; Q99's full mark-support requirement is unchanged. This does not authorize a replacement family, synthesis or host fallback merely because a candidate file format is supported.

Intended normative destination: Materials font asset scope and fixed-file integrity. Actual writeback: this register only.

<a id="cg04-q102"></a>
### CG04-Q102 — Missing rendering dependencies do not disable unrelated capabilities

Status: ACCEPTED. When Workspace and Storage are otherwise healthy, unavailable renderer/font dependencies make the affected configuration can_generate = false and reject related new generation requests. That capability loss alone does not prevent application startup, Candidate APIs or retained Artifact reads.

Corrupt persisted configuration is a separate integrity fault and must not be disguised as an uninstalled dependency. Existing startup ownership, schema recognition and mandatory integrity rules still apply. This decision does not grant execution capability without actual dependency/mark support.

Intended normative destination: Materials configuration capability and runtime admission scope. Actual writeback: this register only.

<a id="cg04-q103"></a>
### CG04-Q103 — Configuration registration compares validated values

Status: ACCEPTED. Compare complete, valid configuration field values rather than serialized JSON bytes. Object key order and formatting do not affect equality. Preserve exact string values and validate field types before equality.

Same ID and equal values permit repeat registration; same ID and unequal values reject overwrite. Distinct IDs remain distinct even for equal values. Do not introduce a configuration fingerprint field for this comparison. This closes Q58's equality rule without changing Q3's independent identity or cross-configuration reuse prohibition.

Intended normative destination: Materials configuration equality and Storage repeat-registration checks. Actual writeback: this register only.

Local consistency review: all Q94–Q103 conclusions are now recorded without changing Q99/Q100 amendments. Q94/Q95 close stable scalar capture and timing; Q96 preserves exact sources without Evidence expression dependency; Q97/Q98 preserve existing AST semantics; Q101 leaves actual files and marks proof open; Q102 separates capability loss from integrity; Q103 preserves identity independently of equality. Only this register changed; no authority/status writeback, agent review, implementation or runtime checks were performed.

## Round 21 — Explicit Font Roles, Registration Boundaries and Durable Relationships

The user accepted Q104–Q113, amending Q106 to require explicit style-role mappings and Q113 to distinguish valid registration from current execution capability. The unlabelled font-hash-list proposal was NOT ACCEPTED. No font synthesis, dependency installation or normative publication is authorized by this batch.

<a id="cg04-q104"></a>
### CG04-Q104 — Client confirmation preserves the original command

Status: ACCEPTED. After a timeout, disconnection or OUTCOME_UNKNOWN, retain and replay the original request_id, resume_version_id and render_configuration_id together. Do not automatically substitute a new request_id and create a second Intent. Once acceptance is confirmed, query the original render_intent_id for current state; an explicit new generation after terminal failure uses a new command.

A temporarily absent observation or later rejection alone does not prove that the original command never committed. Q5/Q10's original acceptance snapshot remains distinct from current fulfillment and payload availability.

Intended normative destination: Derived Work client command/uncertain-outcome obligations. Actual writeback: this register only.

<a id="cg04-q105"></a>
### CG04-Q105 — No MaterialBundle in the M2 consumed scope

Status: ACCEPTED. Single RenderIntent, RenderConfiguration and Artifact relationships suffice for the current preview/export consumer. M2 introduces no MaterialBundle object, ID or API. A future Preparation or other concrete combination consumer may define a bundle in its own scope.

This closes a planned responsibility candidate without treating the Contract Structure inventory as a requirement to implement every named object. Eventual scope/navigation reconciliation remains subject to CG04-S3 and authorized publication.

Intended normative destination: Materials M2 scope and eventual consumed-scope navigation. Actual writeback: this register only.

<a id="cg04-q106"></a>
### CG04-Q106 — Explicit font-file style roles

Status: ACCEPTED AS AMENDED, with the subsequently authorized Q135 exception. fonts maps the four fixed logical keys SOURCE_HAN_SANS, HEITI, SONGTI and KAITI to explicit style-role mappings. Native-file roles use registered static files' Common Sha256Hex values. The default mapping identifies regular, bold, italic and bold_italic; Q135 permits omission of only the affected synthetic italic roles for its scoped candidate. RenderConfiguration together with its fixed pipeline_version must explain how each role is produced; do not infer roles from an unlabelled set of hashes or host font discovery.

At acceptance of Q106, no role omission was authorized; a later researched and explicitly accepted rule under Q99 could authorize the affected omissions. Q135 now supplies that limited exception: Source Han Sans 2.005R retains regular and bold hashes while italic and bold_italic may be omitted when the fixed pipeline provides the approved synthetic italic mappings. All other role omissions remain unauthorized. Do not introduce null, implicit fallback, a synthesis flag or automatic role substitution as an unapproved substitute. The original unlabelled-list proposal and its hash-sorting rule were NOT ACCEPTED, rather than previously accepted rules requiring supersession.

The four logical choices remain unchanged. Actual files, their hashes and complete mark support remain research prerequisites; this structural decision does not establish that native files for all roles have been verified.

Intended normative destination: Materials RenderConfiguration font schema and renderer role-selection obligations. Actual writeback: this register only.

<a id="cg04-q107"></a>
### CG04-Q107 — Recover only under established runtime ownership

Status: ACCEPTED. Before startup recovery, the new Coordinator obtains Storage's existing exclusive runtime ownership of the physical data directory and completes required store recognition. Fence the old attempt before applying interrupted-execution recovery; PID values, lock-file existence or elapsed time alone do not establish that an executor is dead.

Coordinator ownership does not prove that an old renderer child has exited. Q81/Q86's resource occupancy, attempt-file isolation and safe-cleanup conditions continue to apply. Reuse the existing runtime ownership mechanism rather than creating a second lease entity.

Intended normative destination: Derived Work startup recovery consuming Storage runtime ownership. Actual writeback: this register only.

<a id="cg04-q108"></a>
### CG04-Q108 — Cleanup failure does not replace the primary result

Status: ACCEPTED. Preserve the determined primary failure classification when subsequent temporary-file cleanup also fails. For example, timeout remains RESOURCE_LIMIT_EXCEEDED; cleanup failure becomes deferred cleanup and internal diagnostics, not a replacement STORAGE_FAILED terminal result.

This does not claim a durable result when the terminal transaction is uncertain. Q45 still requires reconciliation of the actual committed state. This decision orders primary versus cleanup failures; it does not invent a total ordering for every possible simultaneous cause.

Intended normative destination: Derived Work failure classification and Storage cleanup boundaries. Actual writeback: this register only.

<a id="cg04-q109"></a>
### CG04-Q109 — Recovery cannot reconstruct an uncommitted volatile failure

Status: ACCEPTED. While the Coordinator retains a known renderer failure, terminate Work under Q29 without automatically retrying it. If the process crashes before a reliable terminal result is durable, recovery uses the actual persisted state: an unfinished attempt is an interruption and may execute again within its captured recovery budget. A committed FAILED result is never reopened.

Do not invent a known durable failure from lost in-memory knowledge or introduce a second authoritative failure journal. Q45's uncertain-commit reconciliation still precedes further execution. This clarifies the crash boundary of Q29 without authorizing retries of a known or committed failure.

Intended normative destination: Derived Work reported-failure/interruption boundary and Storage recovery evidence. Actual writeback: this register only.

<a id="cg04-q110"></a>
### CG04-Q110 — Each Intent has at most one execution Work

Status: ACCEPTED. An Intent fulfilled by direct Artifact reuse has no associated Work. An Intent requiring execution is associated with exactly one Work for its lifetime; multiple Intents may share that Work. Recovery changes the attempt of the same Work, not the Intent's Work association. A new generation after terminal failure creates a new Intent.

A nullable internal work_id or equivalent relationship suffices; do not introduce a general many-to-many dependency entity. The public Q33 read shape remains unchanged. Q32's association and Work creation remain part of atomic acceptance, and Q41 prohibits joining a terminal Work.

Intended normative destination: Derived Work Intent/Work cardinality and Storage relationship constraints. Actual writeback: this register only.

<a id="cg04-q111"></a>
### CG04-Q111 — One creating Work per published Artifact

Status: ACCEPTED. Each SUCCEEDED Work creates exactly one Artifact, and each newly published Artifact has exactly one creating Work. Multiple Intents may be fulfilled by that Artifact. Direct Artifact reuse at acceptance creates no synthetic successful Work and never reassigns an existing Artifact to a later creating Work.

Enforce the internal relationship without adding a public Artifact field. UUID identity and byte-level deduplication remain separate under Q4; equal hashes do not merge creation histories.

Intended normative destination: Materials/Derived Work publication result identity and Storage uniqueness. Actual writeback: this register only.

<a id="cg04-q112"></a>
### CG04-Q112 — Managed regular-file payload access

Status: ACCEPTED. Candidate and published payload access uses managed regular files. Do not treat a directory, device or symlink escaping the controlled file scope as Artifact content. Validate the actual opened object and its controlled access, not merely a pathname string.

Preserve Storage's existing physical-directory alias rules: this does not prohibit a legitimate alias for data_directory itself. Q55's stable verified snapshot and Q79/Q80's attempt/publication boundaries still apply. No new client-controlled filesystem path is introduced.

Intended normative destination: Storage Materials file-access boundaries. Actual writeback: this register only.

<a id="cg04-q113"></a>
### CG04-Q113 — Startup registration separates integrity from executability

Status: ACCEPTED AS AMENDED. After exclusive runtime ownership and required store recognition, atomically register newly shipped immutable configurations during controlled startup initialization, before opening request handling and starting workers. A new ID is registered; an equal existing ID is a no-op under Q103; an unequal existing ID rejects overwrite.

An otherwise valid immutable configuration is registered even when its renderer or font runtime dependency is currently missing. Report can_generate = false under Q102; that ordinary capability loss must not prevent the whole application from starting. Registration validates the configuration record and does not pretend that its runtime dependencies have been installed or verified usable.

Same-ID content conflicts, corrupt configuration records and missing configuration records referenced by existing Work, Intent or Artifact are persistence-integrity failures. They prevent normal opening of the affected storage under the applicable Storage rules; do not silently reconstruct missing historical records from the shipped catalog. Distinguish these failures from current execution unavailability, without weakening other established startup/schema/access checks.

Intended normative destination: Materials registration/capability and Storage startup integrity boundaries. Actual writeback: this register only.

Local consistency review: Q106 preserves Q99/Q101 without authorizing synthesis or guessing roles; Q113 preserves Q102 and separates record integrity from missing runtime dependencies. Q107/Q109 retain attempt fencing, real recovery evidence and immutable terminal outcomes; Q110/Q111 retain atomic acceptance/publication and independent identities. The round changes only this register. No authority/status writeback, implementation, dependency installation, runtime tests or independent agent review was performed.

## Round 22 — Layout Pairing, Preflight Failure and Consumer Boundaries

The user accepted Q114–Q123 and amended Q117. Mandatory claim-before-preflight was NOT ACCEPTED. The accepted direct QUEUED failure also narrows Q43's earlier universal failed-result fencing statement; its history and the effective RUNNING condition remain explicit above.

<a id="cg04-q114"></a>
### CG04-Q114 — Identify matching PDF and PNG layout baselines

Status: ACCEPTED. For the same exact ResumeVersion, configurations with equal schema_version, template, renderer and fonts have the same layout baseline. output selects PDF versus PNG file organization and the configured raster dimensions. Keep the common page content, order and pagination under Q36.

Do not introduce configuration_group_id or merge configuration identities. Layout pairing does not authorize cross-configuration Artifact reuse; Q3/Q9 still require the exact configuration ID for that purpose.

Intended normative destination: Materials configuration pairing and cross-format conformance. Actual writeback: this register only.

<a id="cg04-q115"></a>
### CG04-Q115 — Corrupt reuse metadata is not a cache miss

Status: ACCEPTED. When candidate Artifact metadata is valid but its payload is absent or fails byte-integrity verification, continue selection under Q37/Q71. When required Artifact metadata is malformed, its references are broken or its lineage contradicts itself, fail the affected operation with 500 INTERNAL_ERROR instead of skipping it as an ordinary unavailable candidate.

This refines Q37/Q71's skip boundary; new generation must not hide a detected persistence-integrity failure. Missing or corrupt payload still does not rewrite historical fulfillment.

Intended normative destination: Materials reuse errors and Storage metadata integrity. Actual writeback: this register only.

<a id="cg04-q116"></a>
### CG04-Q116 — Persisted target and terminal-result relationships agree

Status: ACCEPTED. An Intent's associated Work has the same exact resume_version_id and render_configuration_id. The Artifact fulfilling that Intent has a Manifest matching the Intent's exact target. An execution-backed Intent's terminal result agrees with its associated Work; direct Artifact reuse has no required Work association under Q110.

A read detecting contradictory required relationships returns an integrity error rather than assembling a superficially valid response or repairing data on GET. Preserve Q33's state-dependent fields and Q35/Q40's atomic terminal propagation.

Intended normative destination: Materials/Derived Work relationship invariants and Storage consistent reads. Actual writeback: this register only.

<a id="cg04-q117"></a>
### CG04-Q117 — Configuration preflight can fail without an execution claim

Status: ACCEPTED AS AMENDED. Before claiming queued Work, check current configuration execution dependencies. If renderer/font support is clearly unavailable, atomically mark Work and all still-PENDING dependent Intents FAILED with CONFIGURATION_UNAVAILABLE, without entering RUNNING or incrementing attempt_count. Retain any count accumulated by prior interrupted attempts; current_attempt_id remains null.

When dependencies are available, a claim may atomically acquire execution eligibility and enter RUNNING under the existing claim/budget rules. If dependencies disappear after a claim, fail that execution with CONFIGURATION_UNAVAILABLE under the current attempt's fencing. A successful preflight is not a guarantee of future availability. Do not strand accepted Work indefinitely in QUEUED merely because capability has disappeared, switch configuration, or treat ordinary Resume removal as revocation.

attempt_count measures successfully acquired execution claims, not pure preflight failures. The proposed mandatory claim before dependency checking was NOT ACCEPTED. This decision extends Q34, partially supersedes Q43 only for unclaimed preflight failure, and clarifies Q48 without adding fields. Atomic arbitration between concurrent preflight failure and claim remains the next explicit concurrency branch; no stale preflight may be used to bypass RUNNING fencing.

Intended normative destination: Derived Work preflight/lifecycle and Storage atomic failure propagation. Actual writeback: this register only.

<a id="cg04-q118"></a>
### CG04-Q118 — Execution limits do not become Artifact compatibility criteria

Status: ACCEPTED. max_pages, max_png_pixels, max_output_bytes and timeout_ms constrain new Work execution, not compatibility of an already published Artifact. A lawful older twelve-page Artifact may still satisfy new demand after the default for new Work becomes ten pages, provided existing admission, permission and byte-verification rules pass.

New Work captures current limits; joining existing Work retains its captured limits. This does not bypass Q67's new-request admission or promise payload availability. Do not invent a limit-based configuration identity change or weaken actual content verification.

Intended normative destination: Materials reuse and Derived Work limit applicability. Actual writeback: this register only.

<a id="cg04-q119"></a>
### CG04-Q119 — Client observations do not regress terminal Intent state

Status: ACCEPTED. Isolate client state by render_intent_id. After observing a terminal state for one Intent, do not let a late PENDING response regress it to generating; another Intent's response must not overwrite the currently selected Intent's state.

FULFILLED records satisfaction by its specified Artifact, not permanent download availability. Display content-read failure separately rather than changing the Intent to FAILED. No public revision field is added for these client obligations.

Intended normative destination: Derived Work/Materials client read and availability semantics. Actual writeback: this register only.

<a id="cg04-q120"></a>
### CG04-Q120 — Six public Materials and demand operations

Status: ACCEPTED. The M2 public surface under /api/v1 consists of POST /render-intents; GET /render-intents/{id}; GET /render-configurations; GET /render-configurations/{id}; GET /artifacts/{id}; and GET /artifacts/{id}/content. Their respective earlier definitions retain exact parameter names, shapes and response rules.

Do not add public Intent/Artifact history lists, Work management, retry, repair or configuration-write endpoints. A new generation uses a new creation command. Internal recovery and source-reading capabilities are not additional public APIs.

Intended normative destination: Materials/Derived Work HTTP operation scope. Actual writeback: this register only.

<a id="cg04-q121"></a>
### CG04-Q121 — Static PDF with only admitted link interaction

Status: ACCEPTED. PDF output is a static resume document with only Q70's admitted link interaction. Exclude scripts, automatic execution actions, forms, embedded attachments and external-program launch actions. Violation of these output constraints is OUTPUT_INVALID.

The PDF format's broader capabilities do not expand Materials scope. Q70's exact saved LINK target restriction remains unchanged. Concrete validation mechanisms and renderer evidence still need to establish this conformance; no implemented validator is claimed here.

Intended normative destination: Materials PDF output conformance. Actual writeback: this register only.

<a id="cg04-q122"></a>
### CG04-Q122 — Output validation remains resource-bounded

Status: ACCEPTED. Validation itself obeys execution resource limits. Check applicable dimensions, page counts and lengths when they can be determined, before unnecessary full allocation/decoding, and continue enforcement during subsequent decoding and verification.

A confirmed applicable limit violation is RESOURCE_LIMIT_EXCEEDED; an unparseable format or invalid structure is OUTPUT_INVALID. Do not freeze a decoder, allocation algorithm or arbitrary numerical threshold here. Concrete bounded-validation proof remains an implementation prerequisite; Q108 still distinguishes primary failure from subsequent cleanup failure.

Intended normative destination: Materials output validation and Derived Work resource enforcement. Actual writeback: this register only.

<a id="cg04-q123"></a>
### CG04-Q123 — Template owns fixed structured-field presentation

Status: ACCEPTED. The fixed template version defines mappings from consumed structured fields to display text, including degree labels, month formats, date ranges and absence semantics. Do not depend on the host locale or ad hoc interpretation. Preserve the existing Evidence distinction between an absent end month and an unknown start month rather than displaying both as ongoing.

Presentation conversion must not change source facts or reintroduce Evidence expression content into Resume-local content. Concrete labels and layout remain part of template research, without adding configuration fields or a new source authority.

Intended normative destination: Materials template presentation consuming Profile/Evidence/Resume semantics. Actual writeback: this register only.

Local consistency review: Q117's direct QUEUED failure is reflected in Q34/Q43/Q48 with explicit scoped supersession and unchanged count/nullability. Q114/Q118 preserve independent configuration identity and existing admission; Q115/Q116 separate data integrity from unavailable bytes; Q119/Q120 preserve snapshot/read and bounded API scope. Q121/Q122 define output obligations without claiming implemented validation. Only this register changed. One bounded read-only checkpoint inspected current storage source and the three affected Work decisions; it performed no broad owner review, edits, runtime tests or database operations.

## Round 23 — Preflight Arbitration, Protocol Completion and Migration Ownership

The user accepted Q124–Q133, amending Q127. A permanent M2 schema-4 Contract target was NOT ACCEPTED. Current source version numbers remain implementation checkpoint information; migration obligations are independent of which version number is next at implementation time.

<a id="cg04-q124"></a>
### CG04-Q124 — Conditional queued-preflight failure arbitration

Status: ACCEPTED. Commit a queued-preflight failure only when work_id, status = QUEUED and the observed attempt_count still match. The same transaction ends Work and all still-PENDING dependent Intents. If the condition loses the race, reread rather than applying an old preflight result to an already claimed execution.

Checking the observed count also detects an intervening claim followed by recovery to QUEUED. No additional revision field is needed. Q41's dependency/terminal ordering and Q43's RUNNING attempt fencing remain effective; Q117's direct failure does not increment the count.

Intended normative destination: Derived Work preflight concurrency and Storage conditional terminal transactions. Actual writeback: this register only.

<a id="cg04-q125"></a>
### CG04-Q125 — Execution storage failures include required reads

Status: ACCEPTED. Expand Q38's STORAGE_FAILED classification from Artifact persistence failure to storage I/O failures in required execution reads or writes. A required exact historical input confirmed missing or corrupt is SOURCE_UNAVAILABLE; temporary inability to read storage or a failed storage write is STORAGE_FAILED; contradictory persisted relationships are INTERNAL_ERROR.

If the failure-result transaction cannot itself be confirmed, Q45 applies: do not claim a durable FAILED result. The existing enum is retained; its Artifact-persistence-only scope is explicitly expanded above. This does not change pre-acceptance HTTP error vocabulary or authorize automatic retries of known terminal failures.

Intended normative destination: Derived Work failure classification consuming Storage error distinctions. Actual writeback: this register only.

<a id="cg04-q126"></a>
### CG04-Q126 — Invalid execution defaults reject only necessary new Work

Status: ACCEPTED. After receipt miss, when selection actually requires creating new Work, validate the necessary default-limit scalars as positive integers. Invalid defaults return 500 INTERNAL_ERROR without committing receipt, Intent or Work; do not silently substitute fallback values.

Original receipt replay, eligible Artifact reuse and an existing Work's valid captured limits remain unaffected. This is not an earlier global admission gate that bypasses Q15/Q25 or rejects reuse merely because defaults for future execution are invalid.

Intended normative destination: Derived Work new-Work admission and atomic acceptance. Actual writeback: this register only.

<a id="cg04-q127"></a>
### CG04-Q127 — Forward migration from the actual implementation-time head

Status: ACCEPTED AS AMENDED. M2 implementation adds a forward migration from the actual migration head at implementation time. Preserve historical migration files, all existing business data and references, receipt contents and fingerprints. Do not backfill Intent, Work or Artifact objects for historical Resume records. Configuration registration remains governed by Q113.

Do not freeze schema 4 as a Materials normative Contract decision. The latest source checkpoint observes schema 3, so an implementation plan or handoff may describe schema 4 as the current expectation, subject to rechecking the head before development. If parallel work advances that head, use the appropriate next version without superseding this Contract decision. The proposed fixed numeric target was NOT ACCEPTED, rather than an accepted requirement later replaced.

Intended normative destination: Storage forward-migration and preservation obligations. Concrete version numbers belong to implementation state/planning and the eventual development handoff, not Materials business semantics. Actual writeback: this register only.

<a id="cg04-q128"></a>
### CG04-Q128 — Runtime output checks and semantic conformance evidence

Status: ACCEPTED. Each execution performs necessary checks of format, page counts/dimensions, resource limits, file integrity and applicable supported output constraints. Establish complete body, mark, pagination, link and field-mapping semantics through the fixed pipeline with focused conformance tests.

Do not require every publication to reverse-extract the entire PDF and prove character-by-character equality with Resume content. Q121 and other output requirements remain mandatory; the absence of that per-execution reverse comparison does not permit lost text or incorrect layout. No renderer or test result is certified by this allocation of proof responsibilities.

Intended normative destination: Materials runtime validation and implementation conformance obligations. Actual writeback: this register only.

<a id="cg04-q129"></a>
### CG04-Q129 — Configuration capability covers all declared logical fonts

Status: ACCEPTED. can_generate = true requires execution support for all four declared logical fonts and their approved style roles. It describes availability of the complete configuration, not accidental support for only one particular Resume's selected font.

This does not promise glyph coverage for every possible source string. Actual visible glyph failures retain Q59's handling. Q99/Q106's requirements remain effective, including only Q135's explicitly approved exception. For that exception, the corresponding configuration cannot report can_generate = true before the final renderer pipeline passes actual PDF/PNG, pagination and mark-combination verification. Missing roles cannot be silently substituted, and that verification does not waive support for the other three logical fonts or current dependency checks.

Intended normative destination: Materials configuration capability and font support. Actual writeback: this register only.

<a id="cg04-q130"></a>
### CG04-Q130 — Renderer capability follows the configured output branch

Status: ACCEPTED. Evaluate renderer dependencies required by the configuration's actual output. If PDF generation dependencies are available but a PNG-only rasterization dependency is missing, the PDF configuration may remain executable while the PNG configuration is not.

A shared pipeline_version does not require every output to use every pipeline component. Both immutable configuration records remain retained. This complements Q129's complete logical-font coverage; it does not change configured identity or silently select another output.

Intended normative destination: Materials output-specific execution capability. Actual writeback: this register only.

<a id="cg04-q131"></a>
### CG04-Q131 — Path and query validation uses shared field errors

Status: ACCEPTED. Invalid-format path UUIDs return 422 VALIDATION_ERROR; a valid-format requested ID with no object returns 404 NOT_FOUND. Invalid or repeated disposition parameters, including repeated equal values, return 422 VALIDATION_ERROR. Prohibited query parameters and GET bodies also return 422 VALIDATION_ERROR.

Use Common error representation and field reasons rather than defining a Materials-specific error object. Malformed JSON and the other transport failures already covered by Q87 retain 400 BAD_REQUEST. The single omitted disposition default remains inline under Q52.

Intended normative destination: Materials/Derived Work HTTP validation consuming Common. Actual writeback: this register only.

<a id="cg04-q132"></a>
### CG04-Q132 — Exact content length without dynamic transformation

Status: ACCEPTED. A successful content GET sends Content-Length equal to Artifact.byte_length and Content-Type equal to Artifact.media_type. Send Q55's verified original bytes without dynamic gzip compression, transcoding or re-encoding; Content-Encoding is absent or identity.

Both disposition variants retain identical length and content. Q56's complete 200 response and Cache-Control: no-store remain effective. This is not a guarantee that the network cannot interrupt transmission.

Intended normative destination: Materials exact-byte HTTP serving. Actual writeback: this register only.

<a id="cg04-q133"></a>
### CG04-Q133 — Receipt identifies its accepted Intent and target fingerprint

Status: ACCEPTED. A receipt's result_snapshot.render_intent_id references the Intent created by that acceptance. Encoding the Intent's exact resume_version_id and render_configuration_id under Q76 yields the receipt's request_fingerprint.

This is a persistence relationship constraint, not a requirement for replay to traverse the full Work/Artifact chain. Replay still returns the original acceptance snapshot without reconstruction from latest execution state. Detected relationship corruption is an integrity error, not a missing receipt that permits new acceptance.

Intended normative destination: Derived Work receipt relationships and Storage integrity. Actual writeback: this register only.

Local consistency review: Q124 preserves no-claim failure and handles intervening claim/requeue; Q125's expanded meaning is reflected in Q38. Q126 preserves replay and reuse ordering, and Q127 separates stable migration obligations from mutable implementation version numbers. Q128 does not weaken output conformance; Q129/Q130 jointly define font/output capability; Q131/Q132 preserve earlier HTTP behavior; Q133 preserves original receipt snapshots. Only this register changed. No authority/status writeback, agent review, implementation, tests or database operations were performed in this round.

## Round 24 — Concrete Catalog Values and Normative Ownership

<a id="cg04-q134"></a>
### CG04-Q134 — Shipped catalog owns concrete configuration values

Status: ACCEPTED. Normative Contracts define RenderConfiguration structure, constraints, identity, registration and execution semantics. The application-delivered versioned catalog supplies concrete fixed configuration UUIDs, actual template/pipeline versions, font-file SHA-256 values for the four logical fonts and their style roles, and the chosen PNG page_width_px.

The development handoff references the verified catalog and dependency evidence rather than permanently fixing those concrete values in business Contract text. Changed immutable configuration content still requires a new configuration ID, and historical records remain retained.

A catalog cannot itself authorize synthesis, waive mark support, change admitted output semantics or bypass any other accepted Contract constraint. Research that requires such a change returns to the affected decision branch for explicit resolution. Moving concrete values to their implementation owner does not establish tested rendering support, close an unresolved semantic branch or authorize implementation/publication.

Intended normative destination: Materials configuration definition and immutable catalog-registration boundary; concrete catalog values and their evidence belong to implementation and the eventual backend development handoff. Actual writeback: this register only.

Local consistency review: Q134 preserves Q3/Q58/Q103's immutable identity/equality rules, Q99/Q106's mark and role obligations, Q127's implementation-state distinction and the pending publication/handoff stage. Only this register changed. No implementation, dependency installation, migration or runtime verification was performed.

## Round 25 — Verified Synthetic Italic for the Researched Source Han Sans Candidate

<a id="cg04-q135"></a>
### CG04-Q135 — Native Regular/Bold bases with explicitly verified synthetic italic

Status: ACCEPTED with user clarification. If the catalog selects the researched Source Han Sans 2.005R candidate, the permitted role mapping is:

| Role | Required production path |
| --- | --- |
| Regular | Native Regular file |
| Bold | Native Bold file |
| Italic | Native Regular plus deterministic synthetic italic |
| BoldItalic | Native Bold plus deterministic synthetic italic |

BoldItalic is not a native BoldItalic font file and is not synthetic bold over Regular. Keep the actual regular and bold file SHA-256 values. Only the affected italic and bold_italic hash fields may be omitted under this rule; the exact registered bases and fixed pipeline_version together determine those roles.

Fix the synthesis path, parameters and dependencies with pipeline_version; do not rely on undeclared system substitution or incidental runtime defaults. The corresponding RenderConfiguration must not report can_generate = true until its final renderer pipeline passes actual PDF/PNG, pagination and supported mark-combination verification. Documentation of a potential synthesis mechanism, native-file availability or this design approval alone cannot satisfy that gate.

This approval is limited to the researched Source Han Sans 2.005R case. It does not authorize synthetic bold, silently extend to HEITI/SONGTI/KAITI, choose an implemented renderer, assign final file hashes or certify a complete executable catalog. Q129 still requires all four logical font choices and their approved roles; Q130 still scopes current renderer dependency checks to the configured output. A future mapping requiring a different synthesis mechanism returns to the affected Contract branch with evidence.

Intended normative destination: Materials font-role resolution, configuration capability and renderer conformance; concrete file hashes and fixed implementation parameters remain catalog/pipeline values under Q134. Actual writeback: this register only.

Local consistency review: Q99 links the researched exception without restoring its rejected general synthesis proposal. Q106 preserves its original no-omission history while recording the specifically approved exception; no unapproved synthesis field or null role was added. Q129 incorporates the actual-output verification gate. Q134's catalog ownership and immutable-identity obligations remain unchanged. Only this register changed; no additional agent review, dependency installation, renderer experiment, backend/frontend implementation or authority/status writeback was performed in this round.

## Session directions and frontier history

<a id="cg04-s1"></a>
### CG04-S1 — Contract-focused interview scope

Status: ACCEPTED user direction. The user explicitly corrected the opening batch: this is a Contract Grill, not a product Grill. Existing Product/Architecture decisions are inputs, not a checklist to reconfirm. The interview focuses on actual owned objects, fields, identities, relationships, command protocols, invariants, transactions, state transitions, persistence, recovery, HTTP/client obligations and proof. A genuinely missing product meaning is raised only at the concrete dependent Contract clause, with its owner and consequence identified. Necessary product clarification remains possible; unresolved semantics are never silently decided in a DTO or schema.

Writeback: this register's session/frontier and owner mapping, plus the current session entries in Progress and traceability. No Product, Architecture, milestone scope or normative clause changes follow from this process correction.

<a id="cg04-opening"></a>
### CG04-OPENING — Withdrawn product-oriented opening

Status: WITHDRAWN, not accepted or rejected product semantics. The assistant withdrew the product-oriented opening batch following CG04-S1. No PDF-only scope, empty-export policy, Save-before-export interaction, demand trigger or history-UI exclusion was accepted. These questions were originally presented as Q1–Q5; CG04-S2 explicitly replaces that numbering arrangement and preserves the withdrawn history under this separate locator. Unresolved format/prerequisite/demand semantics will be addressed only where a concrete Contract branch consumes them.

<a id="cg04-s2"></a>
### CG04-S2 — User-directed numbering and backend development handoff

Status: ACCEPTED user direction. Renumber the previously presented Contract Q6–Q10 as Q1–Q5, respectively. This explicit instruction replaces the earlier no-renumbering arrangement; no accepted business decision or published requirement ID is changed. Future decision locators use CG04-Q1 onward for the Contract interview. The five questions were unanswered at this direction; their subsequent acceptance is recorded in Round 1 above.

The final reviewed development transfer is `docs/development/handoff/sl-02-m2-handoff.md`, directly under `handoff/`, not under `handoff/contract_grill/`. Follow the style and practical backend-first scope of the prior SL-01.M1, SL-01.M2 and SL-02.M1 handoffs. Include actual consumed Contract IDs/revisions, reverified M1 implementation and migration state, required reading, backend scope and exclusions, implementation order, exact interfaces, acceptance/check requirements, and remaining frontend/research/upstream dependencies. Create it after normative publication and review so another conversation can use it directly for backend development; do not create an empty or unreviewed development baseline now. This deliverable does not authorize implementation in the current interview or treat unanswered decisions as approved.

Writeback: this register and current Progress/traceability session state; the development handoff is an explicitly pending final deliverable. Historical handoffs and the original session prompt remain unchanged.

<a id="cg04-s3"></a>
### CG04-S3 — Register-only ordinary rounds and explicitly directed owner writeback

Status: ACCEPTED user direction; SUPERSEDES the earlier session instruction/interpretation that ordinary accepted Contract batches automatically trigger high-level owner reconciliation and Progress/traceability updates. The user explicitly corrected the Round 1 writeback approach. Accepted Q1–Q5 semantics and the unanswered Q6–Q10 frontier are unchanged.

Ordinary rounds update only this single milestone register, following the precedent of the SL-02.M1 Grill record: final conclusions, stable decision locators, useful rationale/boundary examples, intended writeback destinations, supersession and unresolved branches. Recording a future normative destination does not authorize editing that owner now. Perform focused local checks of the conclusions, relevant known constraints and changed references; do not undertake full authority-document or independent multi-agent reviews every round.

Product, Architecture, Acceptance, plans, Contract Structure, Progress and traceability are not routine round-output destinations. If an answer raises an explicit architecture change or important decision requiring owner reconciliation, identify the affected scope and pause dependent definition work as needed. Under the user's stated process, review the relevant owners and provide a concrete writeback plan when explicitly directed; modify them only within the subsequently approved scope. Do not silently resolve a conflict in this register or a future schema, and do not manufacture an owner update merely because a field decision has been accepted.

Progress summarizes actual stage/capability state; traceability records consumed scope and evidence. Neither is a question/batch log. Start, material scope/dependency/readiness changes, authorized scope publication, final closure and implementation/evidence changes are their appropriate update occasions, subject to the user's current direction. Ordinary question acceptance alone changes no readiness. Normative publication still waits for scope closure and authorization, unless the user explicitly authorizes that stage earlier; do not request the same authorization twice.

Preserve superseded history with the replacing decision and affected scope. Do not create per-module decision logs, round reports or alter the session handoff prompt. Final publication reviews and the backend development handoff required by CG04-S2 remain required at their authorized stage.

Actual writeback at this correction: this register only. Earlier owner/status edits were left intact at that moment; the user's subsequent explicit removal instruction is executed under CG04-S4 below. Local verification checked this session instruction, its supersession, stable locators and unchanged unanswered frontier; no runtime checks or independent sub-agent review were required.

<a id="cg04-s4"></a>
### CG04-S4 — Remove premature authority and round-status writeback

Status: ACCEPTED and executed user direction. Remove the earlier Q1–Q5 additions from Architecture §5.4 and Acceptance §4.3, and remove the interview's per-round decision/review logs from Progress/traceability. Retain only the milestone-start/Contract-Pending status and link to this register. Preserve unrelated M1 backend implementation, schema-3 evidence and other concurrent changes.

At this correction Q1–Q5 remained accepted design conclusions and Q6–Q10 were unanswered; their later acceptance is recorded in Round 2 above. Intended normative destinations remain pending, not completed writeback. This action removes premature publication of ordinary-round conclusions, not the conclusions themselves. The prior no-revert disposition in CG04-S3 is superseded only for the explicitly removed owner/status edits. Final publication and the required backend development handoff remain pending their authorized stage.

Historical local checks remain session evidence only: the initial requirement checker reported 178 IDs, and subsequent scoped checks validated decision locators, links and whitespace. Their deletion from Progress/traceability does not create M2 normative readiness or runtime evidence. Current local verification is limited to removal scope, preservation of unrelated changes and register consistency.

<a id="cg04-s5"></a>
### CG04-S5 — Ten questions per subsequent round

Status: ACCEPTED user direction. From the next batch, Q74–Q83, ask ten independent Contract questions per round instead of five. This supersedes only the original question-count instruction in the session handoff and session header. Keep stable numbering, dependency-safe frontiers, explicit user decisions and register-first persistence. Do not add speculative questions simply to fill the quota; unresolved prerequisites remain explicit. All register-only writeback, scoped review and eventual authorized publication/handoff rules remain unchanged.

Q134 closes the ownership of concrete shipped configuration values, and Q135 settles the researched Source Han Sans synthetic-italic permission and its verification gate. No unanswered numbered question remains. This does not declare final Contract completeness, authorize publication or establish executable rendering support. At that checkpoint the next transition required user confirmation of design closure and the concrete normative publication/review scope; the subsequent authorization and completed review are recorded under CG04-PUB. Final decision traceability and cross-document/interface review may identify specific unresolved semantics; those must be resolved rather than silently authored into a Contract.

Concrete catalog mapping, pipeline feasibility, exact font files, operational defaults and actual output evidence remain delivery prerequisites. The other three logical fonts retain the default role requirements; no synthesis extension is assumed. If a selected mapping needs a new exception, research must return that specific choice to the Grill. Separate these unverified implementation prerequisites from the accepted schema/behavior definitions, and keep affected execution readiness Pending. Do not manufacture additional ordinary questions merely to reach ten.

Dependency order after that frontier:

1. Exact source references, object identities, lineage representation and command namespace.
2. Complete rendering input/configuration/output schemas, formats and fidelity guarantees, informed by focused research; identify any genuine product prerequisite gap here.
3. Exact-demand lifetime, compatibility/reuse and historical eligibility/publication; no follow-current target tracking in M2.
4. Explicit-demand command fields/results and atomic intent/receipt acceptance, including idempotency/concurrency and necessary interfaces to saved authority; no speculative Save-coupled intent.
5. Safe local execution states, necessary claim/attempt/fencing, failure/retry and restart recovery; no explicit cancellation in M2.
6. Stored/served bytes, atomic publication, integrity, permissions, retention and missing-file behavior.
7. Complete HTTP/errors/precedence and client polling/download/uncertain outcomes.
8. Schema evolution, conformance/interface review, scoped readiness and eventual development handoff.

At the end of the interview, remaining work concerned concrete renderer/font research, any resulting Contract changes, operational defaults and final conformance/interface review. CG04-PUB subsequently closes the documentary review; actual engineering research and runtime proof remain outstanding. Q127 closes the numeric schema-version question as implementation-time planning information, not a permanently open Materials semantic decision. Durable follow-current subscription and explicit demand cancellation/release are excluded by Q17/Q24, not open M2 branches. Each answered batch reshapes this tree; no fixed round count is promised.

## Research and verification boundaries

Focused native-style and renderer evidence after Q134: the official [Source Han Sans 2.005R SC OTF directory](https://github.com/adobe-fonts/source-han-sans/tree/2.005R/OTF/SimplifiedChinese) lists ExtraLight, Light, Normal, Regular, Medium, Bold and Heavy, with no Italic/BoldItalic file. The versioned [distribution README](https://raw.githubusercontent.com/adobe-fonts/source-han-sans/2.005R/README.md) describes weight-based static packages and Regular/Bold half-width variants. This establishes missing native italic roles in that inspected candidate, not an accepted mapping of RES-012's logical enum to a release.

[Pango FontFace.is_synthesized](https://docs.gtk.org/Pango/method.FontFace.is_synthesized.html), inspected with displayed library version 1.58.2, recognizes synthesized faces including shearing/emboldening. It does not guarantee deterministic synthesis in this project's output pipeline. [WeasyPrint font documentation](https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#fonts), inspected for 70.0, describes matching, embedding and subsetting. Limited inspection of pinned [v70.0 pdf/fonts.py](https://github.com/Kozea/WeasyPrint/blob/v70.0/weasyprint/pdf/fonts.py) and [draw/text.py](https://github.com/Kozea/WeasyPrint/blob/v70.0/weasyprint/draw/text.py) found font-byte embedding and positioned glyph emission without an explicit synthetic shear/emboldening application in the inspected functions. This is an unverified synthesis path, not proof of feasibility or impossibility. Do not infer PDF synthesis merely from Pango's reporting API or CSS style support.

One bounded read-only agent performed this check; no files, binaries, dependencies, renderer prototypes or tests were created. Only the main agent updated this register. Q135 was the resulting scoped semantic question and is subsequently accepted in Round 25; exact catalog mapping, deterministic mechanism and PDF/PNG output evidence remain prerequisites to claiming executable support. No evidence here authorizes synthetic bold or extends a synthesis rule to HEITI, SONGTI or KAITI.

Bounded source checkpoint after Q123: current [Store](../../../backend/src/jobhunter/infrastructure/persistence/sqlalchemy/uow/store.py) serves product schema 3 and recognizes historical schemas 1/2/3. Source migration history has one head, ef03c92ba671, following b720a94fd381 and cd891047a2e6; [the candidate migration](../../../backend/alembic/versions/ef03c92ba671_candidate_authority.py) sets user_version to 3. No M2 Materials/demand persistence was found in the inspected backend source/migrations. The candidate migration remains untracked and Store modified, so this checkpoint establishes working-tree source facts, not committed delivery or any actual database state. STO-018/021/023–026 require preserving earlier histories/receipts and explicit migration ownership. At that checkpoint the next number was brought into the question frontier; Q127 subsequently resolves its ownership: schema 4 is at most the current implementation expectation, while the actual next version follows the implementation-time head and is not frozen in Materials norms. The same narrow check identified Q34/Q43/Q48 as the local reconciliation points for Q117. No tests, database operations, installations or full milestone review were performed.

Focused font-source follow-up after Q93 (read-only; no binary downloads or rendering): official [Source Han Sans 2.005R SC OTF files](https://github.com/adobe-fonts/source-han-sans/tree/2.005R/OTF/SimplifiedChinese) and [Source Han Serif 2.003R SC OTF files](https://github.com/adobe-fonts/source-han-serif/tree/2.003R/OTF/SimplifiedChinese) provide Regular and Bold files. The inspected [LXGW WenKai v1.522 TTF files](https://github.com/lxgw/LxgwWenKai/tree/v1.522/fonts/TTF) provide Light, Regular and Medium, not native Bold/Italic files. These are candidate-file observations, not proof that the selected logical fonts require synthesis or cannot support marks through a valid chosen implementation. Q99 requires mark support and permits deciding a synthesis mechanism only after its necessity is established and accepted; do not silently treat Medium as native Bold or rely on system substitution. The available individual static-file options support investigating a minimal single-face font scope; binary properties, exact hashes, coverage and rendering still need verification after selection.

No logical-font mapping is accepted by that research. In particular, [Adobe's Source Han Sans introduction](https://blog.adobe.com/en/publish/2018/11/19/new-pan-cjk-font-source-han-sans-2-0) establishes its shared design provenance with Noto Sans CJK; do not claim those brands necessarily provide visibly distinct logical-font choices. Official [WeasyPrint font guidance](https://doc.courtbouillon.org/weasyprint/latest/api_reference.html#fonts) describes embedding and default subsetting, but does not establish this project's Chinese text-extraction or layout acceptance. Selected files and their exact accompanying license texts remain an implementation-transfer prerequisite, not an inferred installed capability.

Focused read-only renderer/font check after Q58: [pyproject.toml](../../../pyproject.toml) declares Python >=3.12,<3.13 and no backend WeasyPrint, Playwright Python, Pillow or PDFium dependency; the [backend guide](../../../backend/README.md) also records renderer/PDF/font assets as not installed. Repository file inspection found no font files or current material render/template implementation and no concrete non-font fixed-asset consumer. This does not establish whether the host OS has fonts. The frontend Playwright dependency is E2E tooling, not verified backend rendering capability. RES-012 defines logical font names, not pinned font files or distribution rights; RES-006 excludes image/table input. These facts support deferring speculative assets and do not select an engine or font mapping.

A possible research path is controlled A4 layout to PDF, then page rasterization and PNG assembly. Official [WeasyPrint API](https://doc.courtbouillon.org/weasyprint/latest/api_reference.html) and [font/dependency guidance](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html), together with the [pypdfium2 API](https://pypdfium2.readthedocs.io/en/stable/python_api.html), identify a candidate toolchain to investigate, not an accepted choice or tested compatibility claim. Pinned versions, distribution/licensing, complete glyph/style support, pagination and raster limits remain unresolved. One bounded agent performed this key fact check without edits, installs or renderer experiments; it did not perform a full milestone or authority-document review.

Focused HTTP research preceding Q56: [RFC 9110 §14.2](https://www.rfc-editor.org/rfc/rfc9110.html#section-14.2) permits a server to ignore Range, and [§14.3](https://www.rfc-editor.org/rfc/rfc9110.html#section-14.3) defines Accept-Ranges: none. Q56 subsequently accepts full-content/no-store first-release behavior while leaving that advisory header optional. The RFC evidence is not browser/PDF-viewer verification. No renderer or frontend verification was performed.

Pending factual research: pinned renderer/PDF/PNG behavior and font assets/license/distribution; logical font mappings, glyph coverage, pagination and raster-image limits; local filesystem publication/flush/recovery support; exact M1 runtime availability as concurrent work progresses. Research will use primary sources and distinguish observations from proposed/accepted choices. No first-round question asks the user to supply repository facts.

Initial decision-to-document review maps inherited constraints to their current owners above; no new product recommendation is treated as accepted provenance. Initial cross-document review compares the M1/M2 plan, MAT/SAV/RES/STO interfaces, Product/Architecture and Acceptance demand/recovery boundaries. Historical Inventory/Harness proposals are interpreted with BC3/Q95, not restored as current requirements. Full M2 normative interface review was pending at that checkpoint and is subsequently completed under CG04-PUB.

Routine interview checks remain in this register; the [milestone ledger](../../progress/traceability.md#5-milestone-implementation-and-acceptance-ledger) retains actual scope/readiness state rather than per-round logs. These checks establish documentary integrity only. Runtime tests, renderer experiments, migrations and product acceptance are unexecuted by this session.


<a id="cg04-pub"></a>
## CG04-PUB — Authorized closure, normative publication and development transfer

Status: COMPLETE for Contract work at reviewed revision **2026-09-21.S2M2-r1**. After Q135, the user explicitly requested closure review, necessary writeback and normative publication. That direction authorizes this publication stage without another confirmation; it does not authorize backend/frontend implementation, dependency installation, migration, commit or push. It replaces only the earlier pending-publication disposition, preserving ordinary-round register-only history and every scoped supersession.

**Decision-to-Document Traceability:** all 135 effective CG04-Q decisions have individual normative destinations in the [publication mapping](../../progress/traceability.md#64-sl-02m2-reviewed-scope-and-interface-evidence). Seventy-three new stable IDs are published: COM-043–046, WSP-012, PRO-009, EVD-015, RES-016, SAV-017, MAT-004–030, DRW-001–026 and STO-029–039. The previous 178 IDs and their prior-consumer semantics remain preserved; the SAV-010 value encoder moves by unchanged reference to COM-045. Current totals are 251 IDs across 11 actual normative bodies, with 17 planned destinations. The future-only portions of shared families remain Pending.

**Cross-Document Semantic Consistency:** necessary scoped writeback is complete in Product, Architecture, Acceptance, the global and SL-02 plans, Contract README/index/structure, Progress and traceability. These owners agree on exact-version demand, original acceptance replay, immutable derived identities, historical-source projection, PDF/long-PNG output, atomic durable dispatch/publication, attempt fencing and bounded recovery. Publication preserves the exclusions of follow-current demand, cancellation, MaterialBundle and speculative Save-triggered intent. Concrete catalog values remain implementation-owned; Q135 permits only the documented Source Han Sans italic production path with its unsatisfied actual-output capability gate.

One bounded independent closure audit checked producer/consumer interfaces and both documentary verification seams. It found missing descriptor-version advancement wording, ambiguous initial-default wording and an overly broad reuse/content error reference. MAT-010, DRW-020 and STO-035 were corrected from accepted decisions; Candidate header applicability was clarified. Follow-up review found no remaining actionable issue in the reviewed scope. No new business decision was inferred from these corrections.

The [backend development handoff](../../development/handoff/sl-02-m2-handoff.md) is complete and linked from navigation. It records exact consumed IDs, M1's actual schema-3 working-tree source and separately recorded 294-test evidence, implementation-time migration-head verification, ordered backend work, required checks and unfinished frontend/research obligations. This session did not rerun those 294 tests and does not claim committed M1 delivery from uncommitted files.

Mechanical publication evidence: the maintained `python3 scripts/check_contract_links.py` validates 251 unique anchored IDs, local paths/anchors, all 135 mappings and the 26 Ready / 63 Pending / 89-row scope ledger. Ruff lint/format and Pyright pass for the changed checker. Seven isolated negative fixtures correctly reject duplicate/unknown IDs, missing files/anchors, missing decision mapping, incorrect readiness totals and missing requirement anchors; a restored baseline passes. Supplemental checks cover changed high-level owner links and whitespace, including the newly created files; `git diff --check` passes. These checks establish documentary integrity, not product conformance.

**Current frontier:** no unanswered Contract question or unresolved documentary interface blocks this published scope. Concrete renderer/catalog/font selection and distribution, all four logical-font mark support, deterministic italic implementation, actual PDF/PNG/pagination/text extraction, measured limits and filesystem crash/durability proof remain engineering prerequisites. No RenderConfiguration becomes executable merely through publication. A researched mapping requiring a new synthesis exception or changed behavior must return to its affected owner before implementation. M2 implementation and acceptance are not started; M1 frontend and parent-Slice completion remain outstanding.


<a id="cg04-font-20260923"></a>
## Scoped font-role amendment — 2026-09-23

Status: ACCEPTED by explicit user instruction during backend implementation. Historical Q99/Q101/Q106/Q135 answers above remain historical evidence; this amendment supersedes only their native-four-face requirement, Source Han Sans two-hash omission and restricted synthesis authorization.

SOURCE_HAN_SANS remains Source Han Sans SC 2.005R, using official Regular/Bold and deterministic italic synthesis over the corresponding upright face. HEITI uses Sarasa Gothic SC's released native Regular/Bold/Italic/BoldItalic. SONGTI uses Source Han Serif CN's official Regular/Bold and deterministic italic synthesis. KAITI uses LXGW WenKai 1.522 Regular/Medium for regular/bold logical roles, and deterministic italic synthesis over each corresponding face. Medium is an explicit role mapping, not a claim of native Bold. Every configuration records all four final role-artifact hashes. Family/release, source face hashes, mapping, synthesis rule/dependencies and final artifacts remain fixed and auditable. No synthetic bold, other-family substitution or broader font-policy mechanism was approved.

Writeback: MAT-012 owns the revised roles; MAT-013 retains actual-output capability gating; COM-043 no longer grants omitted role fields. Distribution, deterministic build and real PDF/PNG conformance still require engineering evidence. This decision alone does not make any configuration executable.
