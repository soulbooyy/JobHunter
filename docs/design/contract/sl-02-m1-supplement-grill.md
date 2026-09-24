# SL-02.M1 Supplemental Grill — Knowledge and Resume Independence

> English is authoritative. This is the user-requested separate supplemental decision record, not normative Contract text or implementation evidence. Preserve the original SL-02.M1 register; record accepted conclusions here without question transcripts or unaccepted recommendations.

[Design navigation](README.md) · [Original M1 decisions](sl-02-m1-grill.md) · [Resume Contract](../../contracts/candidate/resumes-grounding.md) · [Profile Contract](../../contracts/candidate/profile.md) · [Progress](../../progress.md)

## Purpose and session state

- Started: 2026-09-24, following the user's report of confusing Knowledge/Resume coupling during SL-02.M1 frontend implementation.
- Scope: clarify what a Resume owns after adding Knowledge, allowed edit/write directions, Profile exceptions, source-selection races, visible source-management controls and necessary downstream interfaces.
- Namespace: CG03S1-Qn for supplemental provenance, distinct from original CG03-Q1–Q100 and normative requirement IDs. Conversation numbering starts at Q1; ordinary rounds contain five independent questions.
- Last answered batch: Q42–Q46 accepted with the controlling Q42/Q43/Q44 clarifications below. Effective Q6–Q46 and BC1–BC3 are closed; Q24/Q16 supersession and Q29 option A remain as recorded. Initial Q1–Q5 were withdrawn unanswered.
- The initial pasted recommendation was discussion input, not blanket acceptance. The user's subsequent explicit replacement architecture and diagram are accepted within CG03S1-BC2 below; unresolved protocol, migration, automatic-retry and merge choices are not inferred from them.
- Session: Q6–Q41 published at 2026-09-24.S2M1S1-r1; Q42–Q46 and their consumer interface publish at 2026-09-24.S2M1S1-r2. Historical open/writeback notes describe their original checkpoints; the current mapping resolves them. This continuation changes no product implementation or real data.
- Ordinary rounds maintain this record. Progress/traceability change only at actual phase, scope, dependency or readiness changes; no per-round status log is required.

## Observed baseline and problem boundaries

- RES-001/013 already prohibit Knowledge updates or retirement from implicitly changing saved Resumes; EVD/PRO saves and Resume saves have separate owners. The reported UX concern does not itself prove runtime cross-object corruption.
- RES-005/010 give a Resume its own local body, but structured company/school/role/dates/project URL values still come from its exact EvidenceVersion. Making those fields independently editable would change the saved model and its consumers.
- RES-011 requires newly introduced/switched Evidence references to remain active/current at commit; retained published historical bindings may survive. This can reject a draft selected before a later Knowledge update.
- PRO-006/008 require exact Profile contact reuse with no private override. Profile publication and Resume adoption are separate actions; changing Profile does not automatically update saved Resumes.
- SAV-015 retains an uncertain operation's exact request/key and specifies explicit retry. Automatic confirmation/retry and merge are candidate topics, not accepted capabilities.
- S2M2 now has published material projections (including PRO-009/RES-016). A source-model change must also review rendering, exact historical output, storage evolution and later Fit/Advisor/Import consumers; the old M1 publication snapshot is not the current implementation baseline.
- The initial transfer observed concurrent documentation and untracked Candidate frontend work. On resumption after Q6–Q10, HEAD is `66e2bb8dfd081a44b3a28873d5b992805ce46d56`; those frontend paths are now tracked and no implementation changes appear in `git status --short`. SL-03.M2 has also closed Q217–Q219 and records all eight consumed portions Ready. Preserve the current baseline rather than restoring the transfer snapshot. No historical runtime test was rerun by this supplement.

## Accepted decisions

<a id="cg03s1-bc1"></a>

### CG03S1-BC1 — One default Resume supplies Workspace Knowledge

- **Status:** ACCEPTED architecture direction by the user's latest 2026-09-24 instruction. Detailed semantics and formal writeback remain pending.
- **Decision:** Keep multiple independent Resumes. Exactly one selected default Resume is the Workspace's user-portrait source when a default exists. Agent user-portrait information comes from Knowledge extracted from that default Resume. Switching the default rebuilds Knowledge to form the new portrait. Do not combine other Resumes into that portrait or infer capabilities absent from the source Resume.
- **Source direction:** Resume content supplies derived Knowledge. The old independently maintained Evidence-to-Resume model requires explicit scoped supersession; a hidden two-way synchronization mechanism is not the selected replacement.
- **Latest clarification:** This replaces the intervening proposed route in which each task's arbitrarily selected Resume supplied the portrait. A non-default Resume can remain an independent document; selecting it for an operation does not itself switch the Workspace default or portrait. Operation-specific document inputs versus default-derived context still require consumer design.
- **Scope limits:** This does not yet settle structured member/contact representation, removal of CandidateProfile/Evidence/Baseline objects, extraction technology, save/update triggers, rebuild timing/failure/publication, no-default state, Fit product shape, or physical retention/erasure. Do not infer those choices from the direction alone.
- **Screenshot:** The supplied nowclaw screenshot illustrates categorized Knowledge, source labels and an edit-Resume entry. It does not establish nowclaw's backend behavior or authorize chat Memory, local-file Knowledge ingestion, interview records or every visible feature.
- **Transfer:** The user requests completion of the supplemental Grill and approved formal writeback in a new conversation, followed by a backend/frontend implementation-impact map per actual Slice milestone and actionable updates to their existing development handoffs. Product implementation and Git submission are not requested by this transfer.
- **Actual writeback now:** This record, its session handoff, navigation and scoped status/impact notices only. Current normative bodies and implementation are not yet revised.

<a id="cg03s1-q6"></a>

### CG03S1-Q6 — Complete independent Resume content

- **Status:** ACCEPTED.
- **Decision:** Each Resume owns its structured experience fields and rich body. Company, school, role, dates and project links are edited directly in that Resume and saved together with its content; creating or modifying an independently maintained EvidenceItem is no prerequisite. Editing A does not change B.
- **Supersession:** Replaces the source-owned structured-field and first-save-Knowledge portions of CG03-BC3/A3, RES-005/010/011/015 and EVD-012 for the new model. Exact old readers and migration remain open; no published requirement is silently repurposed.
- **Writeback/proof:** Product §3; Architecture §3/5; Resume/Evidence/Save Contracts; SL-02.M1, SL-04.M1 and Materials source interfaces. Prove independent edits, atomic document Save and no cross-Resume writes.

<a id="cg03s1-q7"></a>

### CG03S1-Q7 — Resume-owned contacts

- **Status:** ACCEPTED.
- **Decision:** Each Resume independently saves its name, phone and email values. New editing does not require the shared CandidateProfile or a separate Profile Save/adoption. Different Resumes may use different values. Existing default model-invisibility/privacy remains effective.
- **Supersession:** Replaces CG03-A1 and PRO-001/006/008's shared contact ownership and mandatory reference/adoption for new documents; historical Profile data and readers require explicit migration/compatibility decisions. CandidateProfileProjection in BC2 is a capability index, not a renamed three-contact authority.
- **Writeback/proof:** Product §3/9; Architecture §3/5/13; Profile/Resume/Save, Materials and Storage interfaces; SL-02.M1/M2. Prove per-document contacts, no propagation and unchanged privacy admission.

<a id="cg03s1-q8"></a>

### CG03S1-Q8 — Read-only Knowledge

- **Status:** ACCEPTED.
- **Decision:** Knowledge has no independent user fact-create/edit/delete workflow. Show source attribution and an edit-default-Resume route; corrections change the source Resume or, under BC2, explicitly rederive erroneous projections. Neither route establishes a second editable fact authority.
- **Writeback/proof:** Product §3; Architecture §3/5; Evidence/Profile/Resume/Save interfaces, UI/API guides and SL-02.M1. Prove that editing derived output cannot bypass source authority. Rederivation identity, failure and retry rules remain open.

<a id="cg03s1-q9"></a>

### CG03S1-Q9 — Exclude Header from portrait extraction

- **Status:** ACCEPTED USER AMENDMENT; the proposed inclusion of career-like Header text was not accepted.
- **Decision:** Ignore Header content when deriving the portrait. Education comes from formal education experience; user job intent is maintained in Preferences. Do not promote Header degree, work-years or desired-role text into capability evidence. This does not itself remove existing Header presentation controls or expand Preferences' published field schema.
- **Writeback/proof:** Product §3/5; Architecture §5/6/10; Resume and projection definitions plus SL-02/05 consumers. Prove that contradictory or additional Header assertions cannot add portrait facts and that preferences remain independently maintained.

<a id="cg03s1-q10"></a>

### CG03S1-Q10 — Saved default content triggers derivation

- **Status:** ACCEPTED, interpreted with Q9's source exclusion.
- **Decision:** A successful Save changing portrait-relevant content of the current default automatically triggers an update. Dirty drafts do not; non-default Saves do not. Pure typography/color changes and management rename do not require semantic re-extraction. Switching the default retains BC1's rebuild requirement.
- **Boundary:** Exact source provenance when a presentation-only Save creates a new ResumeVersion, no-op handling, publication timing, failure and safe reuse are still to be resolved. This decision does not authorize mislabeling an old source as the new current version.
- **Writeback/proof:** Product §3; Architecture §5; Resume/Save/Workspace and derived-work/Storage agreement; SL-02.M1. Cover saved versus draft, default versus non-default and semantic versus presentation changes.

<a id="cg03s1-bc2"></a>

### CG03S1-BC2 — Two derived projections, one DeepFit result and independent optimization

- **Status:** ACCEPTED architecture direction from the user's explicit replacement description and accompanying diagram after Q6–Q10. Detailed execution and representation remain open.
- **Independent documents:** Each Resume has its own immutable version chain. No Master/Application Resume type or mandatory derivation from the default exists. The default selects the Resume whose current eligible content supplies the global portrait; selecting a document for application or optimization does not change that selection.
- **Two projections:** CandidateProfileProjection is a lightweight structured capability index; CandidateEvidenceProjection provides addressable evidence units with provenance to the exact source ResumeVersion and source spans. Both are read-only derived views, never independently editable fact authorities. Capability entries must have source support; extraction is not independent verification of a person's claims. Q9 excludes Header. Unit segmentation, storage, identity, extraction technique and paired publication are not yet frozen.
- **Separate intention:** User-authored, versioned Preferences describe desired work and are not copied into the capability profile. DeepFit combines the selected intent version with candidate and Job inputs at execution time. PreferenceSetVersion already matches PRF-007's actual name; the user's examples still require reconciliation with PRF-002's six fields (which include a required-education ceiling but no work-mode field). They do not settle new field schemas, enum values or migrations. Other legitimate Preferences consumers, including Collection, are not removed.
- **Single analysis:** DeepFit uses exact JobVersion/derived RequirementSet, Preferences, and the default-derived profile/evidence. It starts with the capability index and progressively obtains exact evidence through a controlled Evidence Tool to ground Requirement-to-Evidence conclusions; it does not require putting the entire Resume into its initial model input. It produces one core CandidateJobFitAnalysis that may include Preference Fit, Capability Fit, strengths, gaps and evidence citations. There are no parallel CandidateFit/ResumeFit analyses. This supersedes CG03-BC3/A4's two-analysis product and internal architecture. Assessment meanings, retrieval coverage, score policy and failure outcomes remain to be settled for this new scope.
- **Independent optimization:** Generic Optimization reads any explicitly targeted ResumeVersion and improves wording, structure, action orientation, grammar and information density without inventing facts. Missing useful quantities are suggestions for user supplementation, not fabricated achievements. Job-targeted Optimization additionally uses the specified JobVersion and RequirementSet to select, order and emphasize supported content. The diagram names ResumeOptimizationAnalysis as its intermediate result; result schema and relationship to existing Advisor Suggestions remain open. Q14 subsequently limits the current capability to suggestions: assistant application is later work. Future applied optimization advances the same Resume's version chain, never an Application Resume subtype; the original diagram's arrow does not authorize a current write path.
- **Default consequence and history:** Updating a non-default Resume leaves the global portrait unchanged; a portrait-relevant new current version of the default triggers derivation under Q10. Switching A to B derives from B rather than unioning A and B. Existing analyses retain their original exact input lineage and are not rewritten. Behavior for in-flight work and current-result eligibility remains open.
- **Diagram interpretation limits:** Candidate is the conceptual user context in the supplied image; whether it requires a new persisted aggregate instead of the existing Workspace selection remains unresolved. Preferences, JobVersion and RequirementSet are independent input branches as described in the user's prose; vertical diagram placement does not make Preferences the source of JobVersion. A new general source-ingestion, Memory fact store, automatic Save approval, or physical data-erasure policy is not implied.
- **Writeback destinations:** Product §3/5/6/7/10; Architecture §3/5/6/7/10/13/14/16; Acceptance §4–11 and applicable Eval; Candidate/Workspace/Storage/Materials and consumer Context/Tools interfaces; global Plan, SL-01.M2 interface impact, SL-02.M1/M2, SL-03 consumer scopes, SL-04.M1, SL-05.M1/M2, SL-06.M1/M2, SL-07.M1–M3 and downstream SL-10/11/12 plans/handoffs. Future Contract paths remain planned until their real consumed scope is authored. Milestone redistribution is not yet approved or published.
- **Required proof:** Source-only capability provenance, no Header/Memory/other-Resume leakage, read-only projections, exact progressive reads, bounded and honest retrieval conclusions, separate preference/capability meanings within one result, supported same-Resume optimization, preserved exact history and no retargeting of application materials.

<a id="cg03s1-q11"></a>

### CG03S1-Q11 — Deterministic Evidence and schema-constrained semantic Profile

- **Status:** ACCEPTED USER DEFINITION.
- **Decision:** CandidateEvidenceProjection is primarily deterministically parsed from one exact ResumeVersion. Preserve original sections, entries, bullets and their source text, with stable Evidence IDs and source locations. Model rewrites, summaries and inferred text cannot become evidence authority. The Resume remains the source authority; Evidence is an exact traceable derived representation.
- **Profile:** CandidateProfileProjection is generated from these Evidence Units using schema-constrained model structured output. Each semantic capability must reference one or more concrete evidence_ref values and must be supported by them; structural validity or an existing citation alone does not establish semantic support. No unsupported capability upgrade is allowed.
- **Save boundary:** Valid ResumeVersion publication is independent of projection success. Model output/parsing failure leaves Profile missing or awaiting retry; it cannot block or roll back the already saved Resume. Q9's Header exclusion and existing contact/model privacy remain effective.
- **Open:** Evidence ID stability scope and precise source addressing, source-text projection, model schema and semantic validation, budgets/recovery/retry, and presentation-only version reuse. Q12 defines complete-pair current publication, not whether independently built Evidence can be browsed during Profile failure.
- **Writeback/proof:** Product §3; Architecture §5/10/11/12; Evidence/Profile/Resume/Save/Storage and consumed Context/Tools/Eval scope; SL-02.M1 and actual invocation prerequisites. Prove exact source preservation, traceable references, unsupported-claim rejection and durable successful Save despite model failure. Model-based derivation cannot be treated as safe deterministic Materials replay.

<a id="cg03s1-q12"></a>

### CG03S1-Q12 — Immediate default selection and asynchronous paired publication

- **Status:** ACCEPTED.
- **Decision:** Default selection commits immediately, with rebuilding in the background. The UI identifies the new selected source and rebuilding state. Publish Profile and Evidence as one coherent ready pair; never combine different source versions. A new analysis cannot use the old pair while presenting it as the new default's portrait.
- **Failure/history:** Failure preserves the newly selected default and exposes failure/retry. Old projections may remain explicitly identified historical records; they are not silently promoted to current. A saved Resume/default change is distinct from successful portrait generation.
- **Open:** Durable scheduling/publication fencing, retry admission and partial Evidence viewing still need concrete agreement; no implicit provider-call retry is approved.
- **Writeback/proof:** Product §3; Architecture §5/12; Workspace/Save/projection/Storage agreement and SL-02.M1 frontend state. Prove pending/failed states, no mixed source pair, no rollback of selected default and no old-as-current analysis.

<a id="cg03s1-q13"></a>

### CG03S1-Q13 — Frozen running analysis and historical results

- **Status:** ACCEPTED.
- **Decision:** An already-started DeepFit continues with its frozen complete exact inputs when the default switches or its Resume gains a new version. Do not swap evidence, implicitly restart or repeat costs. Its result retains the old source and remains historical rather than being advertised as a compatible current-portrait result. New analyses use the updated ready projection.
- **Boundary:** Actual permission revocation or required-source unavailability retains separate admission/failure handling. The initial freeze point, same-Resume semantic-equivalence compatibility and later new-turn Advisor policy remain to be resolved; this decision covers an already-started DeepFit.
- **Writeback/proof:** Product §5; Architecture §6/10/12; future Fit and actual Context/Tools/projection interfaces; SL-05 and applicable Eval. Exercise A3-to-A4 and A-to-B during execution, retained results, no latest substitution and independent revocation.

<a id="cg03s1-q14"></a>

### CG03S1-Q14 — Current optimization is suggestion-only

- **Status:** ACCEPTED USER AMENDMENT. The proposal to deliver a current confirmed-application flow was not accepted.
- **Decision:** Current Resume Optimization produces suggestions only. Assistant help to directly apply modifications is postponed to later implementation. Suggestion generation creates no formal ResumeVersion and therefore triggers no portrait rebuild. Users retain ordinary manual Resume editing/Save; accepted Q10 applies if they save a portrait-relevant change to the default.
- **Supersession:** Narrows BC2's diagram/result-to-new-version flow for present delivery. Future assistant application must still target the same Resume, but its detailed confirmation, proposal and concurrency protocol is not frozen by this answer.
- **Writeback/proof:** Product §6; Architecture §7; SL-06/07 ownership and SL-10.M2 adopt-back dependencies need revised allocation, explicit future scope and handoffs. Do not keep an unimplemented assistant-apply requirement inside current completion criteria merely to preserve old milestone counts. Prove useful supported suggestions and absence of automatic formal writes/default or material changes.

<a id="cg03s1-q15"></a>

### CG03S1-Q15 — Retrieval misses are not proven capability gaps

- **Status:** ACCEPTED.
- **Decision:** A failed initial retrieval establishes only that support has not yet been found. Before concluding that the default Resume does not express a required capability, broaden inspection as necessary, including complete coverage of that exact version's permitted Evidence when needed. Failure, capacity or budget limits that prevent sufficient inspection require an uncertain conclusion rather than an invented absence.
- **Meaning:** Even adequately supported absence is bounded to what the source Resume expresses; it cannot establish that the person lacks the real-world ability. Profile omission alone is not negative evidence. This does not require the full Resume in the initial model Frame or relax privacy boundaries.
- **Open:** Exact coverage evidence, assessment/score representation and bounded consumer limits remain future consumed Fit/Eval detail; no numeric limit or universal all-evidence-per-positive-match gate is selected.
- **Writeback/proof:** Product §5; Architecture §6/10; Fit/Tools/Context/Eval consumed scopes and SL-05. Cover a capability omitted from Profile but present in a bullet, unsuccessful retrieval, incomplete inspection and honest source-bounded negatives.

<a id="cg03s1-q16"></a>

### CG03S1-Q16 — Evidence identity is exact-version scoped

- **Status:** ACCEPTED WITH LATER SCOPED SUPERSESSION by BC3. Exact-version Evidence binding survives; the absence of cross-version logical entry/block identity does not.
- **Decision:** Evidence identity remains stable for repeat parsing of the same exact ResumeVersion under the same parsing rules. No cross-version identity preservation or automatic fuzzy alignment is promised. A new version has its own evidence references even if a bullet remains at the same position; historical consumers keep the original exact references.
- **Boundary:** Source locations must resolve preserved structured fields/text under the versioned parsing rules. Concrete ID encoding and addressing belong to the revised Contract; stability does not require a new independently editable Assertion graph.
- **Later correction:** BC3 requires stable logical entry_id/block_id that may persist across ResumeVersions. Each Evidence reference still includes its exact ResumeVersion and never overwrites an old binding. BC3 replaces position-only/no-persistent-ID interpretations, not the separation between logical continuity and immutable evidence identity.
- **Writeback/proof:** Evidence/Resume/projection/Storage interfaces; SL-02.M1, future Evidence Tool and Eval. Exercise repeat parsing, reordered/changed bullets, rule-version changes and old analysis references.

<a id="cg03s1-q17"></a>

### CG03S1-Q17 — Unavailable portrait UI and explicit refresh entry

- **Status:** ACCEPTED USER AMENDMENT. The proposed partial-Evidence browsing interface was not accepted.
- **Decision:** When a complete usable portrait is unavailable, the user-portrait page directly shows that it is unavailable and offers a refresh button. Clicking DeepFit reports that the current portrait is unavailable; it does not silently start a task with old or partial projections. Do not introduce a special browse-partial-Evidence screen for Profile generation failure.
- **Boundary:** This UI does not require deleting successfully built internal Evidence, changing saved Resume authority or disabling independent document editing. Refresh's read-versus-rebuild behavior, duplicate-click handling and no-source behavior still require agreement. Q12's rebuild/failure/source information remains applicable without exposing internal stage details as a separate user workflow.
- **Writeback/proof:** Product §3/5; UI/API consumer guides and SL-02.M1/SL-05. Prove unavailable page, refresh affordance, clear DeepFit rejection and no hidden fallback/dispatch.

<a id="cg03s1-q18"></a>

### CG03S1-Q18 — Last Resume removal and no-current-portrait state

- **Status:** ACCEPTED.
- **Decision:** Allow explicitly confirmed removal of the final active Resume. Clear the default selection and make the current portrait unavailable; direct the user to create or import a Resume. Preferences and Manual Application Entries remain independently usable.
- **Supersession:** Replaces RES-003/WSP-011's last-active-Resume prohibition and the corresponding SAV-014 LAST_RESUME_REQUIRED behavior for the revised scope. WSP-009/010 must also admit return to null selection and later creation without assuming null always has initial revision 1. Selection concurrency still needs to prevent stale work from publishing a current portrait after removal.
- **Boundary:** Ordinary removal is not automatically physical erasure. Historical retention, removal while tasks run, replacement when other Resumes remain and first-create selection require the surviving rules or later scoped decisions.
- **Writeback/proof:** Product §3; Architecture §5/13; Workspace/Resume/Save/projection/Storage; SL-02.M1 and unaffected-entry/preferences regression. Exercise final removal, empty state and subsequent creation.

<a id="cg03s1-q19"></a>

### CG03S1-Q19 — Reviewed document import replaces Knowledge-first import

- **Status:** ACCEPTED.
- **Decision:** Upload and parsing produce a temporary Resume draft for user review/correction. One confirmed document Save creates an independent formal Resume; successful upload/parse alone creates neither a formal Resume nor independent career facts. Cancellation before Save leaves no independently saved Knowledge. If the saved document becomes default, derive its portrait through the ordinary accepted default-source path.
- **Failures:** Unparsed content must be disclosed rather than silently omitted while claiming complete import. No automatic conflict merge, source invention or model-success requirement is added to the formal document Save.
- **Supersession:** Replaces CG03-BC3/A5's two explicit Knowledge-then-Resume product stages and SL-04.M1's corresponding dependency/acceptance clauses. Temporary-file retention and concrete import schema remain its actual consumer scope, not inferred here.
- **Writeback/proof:** Product §3.2; Architecture §5; Acceptance §4; SL-04.M1, Save/Resume/projection shared interface and planned Import Contract. Prove review/cancel, disclosed parse gaps, atomic document Save and conditional subsequent derivation.

<a id="cg03s1-q20"></a>

### CG03S1-Q20 — Reuse the existing six Preferences fields

- **Status:** ACCEPTED; no field expansion now.
- **Decision:** Retain PRF-002's six existing fields: target_job_keywords, accepted_cities, minimum_salary, recruitment_types, excluded_companies and max_required_education. Do not add work-mode/remote/hybrid/on-site fields in this supplement. The required-education ceiling remains user intent about a Job's requirement, not the candidate's educational attainment.
- **Boundary:** DeepFit adds a consuming interface, not a second Preference authority or implicit wire/storage rename. Missing configuration, input freeze, comparisons, unknown Job values and hard-versus-advisory intent remain decisions for the new consumer. Existing Collection interpretation is not silently replaced.
- **Writeback/proof:** Preferences consumer clause and SL-01.M2 impact review; Product §4/5; Architecture §6; SL-05 and its future Fit Contract. Preserve existing Save/version/fingerprint semantics while proving separate intention and capability inputs.

<a id="cg03s1-q21"></a>

### CG03S1-Q21 — Explicit refresh rebuilds; ordinary reads do not

- **Status:** ACCEPTED.
- **Decision:** The portrait refresh action requests rebuilding from the current default's current source. If matching work is already in progress, observe that work instead of dispatching another model call. After failure, another explicit refresh requests retry. Ordinary page refresh/read only reads status and cannot dispatch a model. With no default, direct the user to create/import a Resume.
- **Boundary:** Each remote invocation remains subject to controlled admission, budget and honest outcome/recovery. This is not permission for hidden SDK retries, automatic replay of an uncertain call, or unlimited work through repeated clicks. Concrete command identity/concurrency and bounded invocation policy require the revised interface.
- **Writeback/proof:** Product §3; projection/Save/Context/Runtime/Storage and UI/API interfaces; SL-02.M1. Cover duplicate requests, running versus failed state, browser reload, no-default and no hidden dispatch from GET.

<a id="cg03s1-q22"></a>

### CG03S1-Q22 — Durable rebuild obligation and obsolete-result fencing

- **Status:** ACCEPTED.
- **Decision:** A result may become the current portrait only if it still belongs to the current rebuilding request. Late obsolete work cannot overwrite current publication, including A→B→A or a newer Save of A. Returning to the same Resume identity alone does not reauthorize an older task. Retained obsolete results may support history, not implicit currentness.
- **Durability:** Commit the source/default change together with its required durable rebuilding obligation, so a crash cannot lose the update. Model execution follows commit outside the authority transaction. This is separate from Q13's right for an already-frozen DeepFit to finish its historical analysis.
- **Writeback/proof:** Architecture §5/12; Workspace/Save/projection/Storage and applicable Runtime interfaces; SL-02.M1. Cover Save/switch crash windows, source/version/request races, A→B→A, removal and stale completion without duplicate authority publication.

<a id="cg03s1-q23"></a>

### CG03S1-Q23 — Provenance-preserving reuse after presentation-only Save

- **Status:** ACCEPTED.
- **Decision:** When only presentation changes, deterministically establish the new exact ResumeVersion's Evidence references and reuse the existing supported capability interpretation with references mapped to the new Evidence. Permit this only when every portrait input is demonstrably unchanged and parsing rules are compatible; record the reuse provenance rather than claim a fresh model extraction.
- **History/failure:** A3→A4 font-only editing needs no new model call, but the current pair references A4; historical consumers remain bound to A3. If input equivalence or safe mapping cannot be established, perform normal rebuilding. Do not reuse cross-version Evidence IDs contrary to Q16 or replace old result lineage.
- **Writeback/proof:** Resume/projection/Save/Storage and currentness interfaces; SL-02.M1 plus Materials separation. Cover exact equivalence, changed meaningful text, incompatible parsing, complete reference mapping, reuse provenance and historical input preservation.

<a id="cg03s1-q24"></a>

### CG03S1-Q24 — Forward migration preserves old exact content and unreferenced data

- **Status:** SUPERSEDED by Q38 for transition from the old development data model. The following bullets preserve the earlier accepted decision as history, not current migration requirements.
- **Decision:** Use a forward migration preserving old identities, immutable versions, receipts and materials. For each still-active old Resume, publish a new independently owned content version from the exact contacts, structured fields and local body that actually constituted that saved document. Never substitute the latest shared Profile/Evidence, import unused source narrative into local wording, or rewrite the old immutable version in place.
- **Legacy data:** Retain old library-only information read-only. Do not silently erase it or add it to the default-derived portrait. Existing exact history/readers and receipt semantics remain available under their own permissions; a derived migration result must not invent a past user action/model analysis.
- **Execution boundary:** Migration itself performs no model invocation. The new derivation path generates the portrait afterward. This session authorizes documentation of migration work only, not running a migration or changing published historical migration files.
- **Writeback/proof:** Storage/Resume/Profile/Evidence/Save/Materials/API compatibility and SL-02.M1/M2 handoffs. Cover old current versus pinned sources, local/source-body divergence, unreferenced facts, preserved outputs/receipts and explicit restart/recovery.

<a id="cg03s1-q25"></a>

### CG03S1-Q25 — Preferences are optional for manual DeepFit

- **Status:** ACCEPTED WITH USER CLARIFICATION.
- **Decision:** Manual DeepFit may assess capability without configured Preferences. In the same CandidateJobFitAnalysis, report Preference Fit as not configured/not assessed. Absence is not UNLIMITED and cannot be filled from Header, chat or portrait. Later Preferences Save does not rewrite existing analysis; a new analysis consumes the new intent.
- **Automatic consumers:** Configuration is required for intent-dependent automatic functions such as automatic Job recommendation, acquisition scope and Shortlist. This records the prerequisite boundary, not a request to add those unplanned features to this supplement or pretend their Contracts/implementation exist. Existing Collection scope remains governed by its actual plan.
- **Writeback/proof:** Product §4/5; Preferences consuming interface and SL-01.M2 compatibility; SL-05/08 planning where actually consumed. Prove capability-only manual result, explicit missing-intent state, no inferred configuration and preserved historical analysis after preference changes.

<a id="cg03s1-q26"></a>

### CG03S1-Q26 — Revised milestone allocation

- **Status:** ACCEPTED.
- **Decision:** SL-02.M1 owns independent saved Resumes/default selection and portrait derivation/refresh. Deliver deterministic saved-document capability before integrating the model derivation portion; the latter requires the actual applicable protected invocation capability from SL-03.M2. Do not make legal document Save depend on model readiness.
- **Analysis/optimization:** SL-05.M1 owns single-Job DeepFit; SL-05.M2 owns multi-Job analysis/result management. Repurpose SL-06.M1 to Generic Optimization suggestions and SL-06.M2 to Job-targeted Optimization suggestions, replacing both old Resume Fit milestones. SL-07.M1/M2 own durable ordinary/Job-context conversation and reuse the optimization capability rather than duplicate it.
- **Later scope:** SL-07.M3 assistant application and SL-10.M2 related adopt-back are explicitly later implementation. Reconcile their completion/dependency records as postponed scope; do not pretend the user has approved their detailed future write protocol or claim current delivery from preserved old plan text.
- **Writeback/proof:** Global Plan/Slice index; SL-02/03/05/06/07/10 plans; consumer maps, Acceptance/Eval, Progress and owning development handoffs. Retain stable planning IDs with explicit changed meanings/provenance; historical completion evidence is never reassigned to a replacement capability. Clarify deterministic versus model-dependent delivery and verify reuse at the real consumer.

<a id="cg03s1-q27"></a>

### CG03S1-Q27 — Candidate remains conceptual; Workspace owns default selection

- **Status:** ACCEPTED.
- **Decision:** The diagram's Candidate represents the current local user. Retain the existing single-user Workspace-owned default selection; do not introduce a Candidate account table, multi-user relationships or a second default pointer. CandidateProfileProjection and CandidateEvidenceProjection remain the accepted projection names.
- **Writeback/proof:** Architecture §3/5/16; Workspace/Storage/projection interfaces and SL-02.M1. Prove one selection authority and retain existing local Workspace scope.

<a id="cg03s1-q28"></a>

### CG03S1-Q28 — Strict selected-Resume optimization context

- **Status:** ACCEPTED USER AMENDMENT; stricter than the recommendation's supplementary cross-source hints.
- **Decision:** Resumes are fully independent. When the user specifies a Resume for optimization in the assistant, the candidate-content context contains only that Resume. Do not inject default-derived Profile/Evidence, another Resume, remembered career facts or conversational career assertions as supplementary candidate material. In particular A's Kafka experience cannot enter B's optimization, including through hidden summaries or retrieval.
- **Scope:** Preserve the previously accepted Generic/Job-targeted distinction; Job/Requirement inputs describe the target, not additional candidate facts. Task-control instructions and source-grounded questions about missing information do not become another career-fact source. This is the present implementation boundary, not a new multi-source optimization workflow.
- **Writeback/proof:** Product §6; Architecture §7/10; SL-06/07 and their future optimization/Session/Context/Tools/Eval interfaces. Verify actual model inputs, not merely source declarations; test target switches, summaries and absent capabilities without cross-Resume leakage.

<a id="cg03s1-q29"></a>

### CG03S1-Q29 — Empty career source is not a usable portrait

- **Status:** ACCEPTED, including the subsequent explicit option-A clarification.
- **Decision:** An empty Resume or one containing only contacts/Header can be saved and selected as default. With no extractable career content, show portrait unavailable and request additional information; do not call a model to generate an empty portrait or run DeepFit. Do not turn missing material into a claim that the person has no abilities.
- **User addition:** If the user attempts optimization with an empty portrait, the assistant should directly report unavailability and ask for additional information.
- **Accepted clarification:** Optimize a nonempty explicitly selected B even if default A is empty or its global portrait is unavailable. Optimization admission checks B's usable content alone. If B is empty, respond directly that the current Resume has no content available for optimization and request additional information; do not describe this as a dependency on global portrait readiness. No model dispatch is needed for this prerequisite message. DeepFit still requires the default-derived usable portrait.
- **Writeback/proof:** Product §3/5/6; projection admission and SL-02/05/06/07. Test contact/Header-only source, no model dispatch, actionable unavailable state, empty A/nonempty B and nonempty A/empty B to prove the two prerequisites remain separate.

<a id="cg03s1-q30"></a>

### CG03S1-Q30 — Preference mismatch does not block manual DeepFit

- **Status:** ACCEPTED.
- **Decision:** A configured intent mismatch, including city, salary or excluded company, does not prohibit a user-requested DeepFit. Report intent conflicts separately from capability findings within the single result; do not turn Preference mismatch into Capability mismatch. Unknown Job data is indeterminate, not guessed satisfaction or conflict.
- **Boundary:** Automatic Collection and other actual automatic consumers retain their own filtering/admission rules. This adds neither an aggregate score formula nor literal keyword-title matching; detailed comparison/assessment policy remains the Fit consumer's scope.
- **Writeback/proof:** Preferences consumer interface, Product §4/5, Architecture §6, SL-05 and applicable Eval. Prove manual admission despite intent mismatch, independent dimensions and honest unknown values.

<a id="cg03s1-q31"></a>

### CG03S1-Q31 — Explicit refresh invalidates current new-analysis admission

- **Status:** ACCEPTED.
- **Decision:** Accepting an explicit refresh marks the current portrait as updating and stops admission of new DeepFit work, even when the source Resume is unchanged. Success publishes the new pair; failure leaves portrait unavailable with refresh offered, without automatic fallback. Previously started DeepFit keeps its frozen inputs under Q13.
- **Writeback/proof:** Projection/refresh state and consumer admission; SL-02.M1/SL-05. Cover ready-to-refresh, concurrent DeepFit admission, failed refresh and continued historical tasks.

<a id="cg03s1-q32"></a>

### CG03S1-Q32 — Invalid Profile output fails the complete candidate

- **Status:** ACCEPTED.
- **Decision:** If a generated Profile contains invalid entries, nonexistent evidence references or detected unsupported claims, reject the complete candidate Profile. Do not prune erroneous entries or substitute approximate references and report success. Saved Resume and valid deterministic Evidence remain intact; the complete current portrait remains unavailable until successful rebuilding.
- **Boundary:** Semantic support requires its own validation/Eval evidence; a schema-valid reference is not proof that every generated claim is supported. This decision neither adds a hidden judge call nor promises a deterministic entailment oracle.
- **Writeback/proof:** Profile/projection admission and actual Eval scope; SL-02.M1. Prove whole-candidate rejection, no silent omission/repair and independent durable document state.

<a id="cg03s1-q33"></a>

### CG03S1-Q33 — One model request per rebuild attempt

- **Status:** ACCEPTED.
- **Decision:** The current derivation attempt admits at most one model request, with no automatic repair or remote retry. Invalid output, admission failure or uncertain remote outcome leaves the portrait unavailable; explicit user refresh starts a new bounded attempt when admitted. No SDK retry/fallback can bypass this limit.
- **Local recovery:** A complete durably retained response may resume local processing without another Provider request. Q23's validated deterministic reuse needs no model request. Persisted admission, finite resource limits and original uncertain outcomes remain owned by the controlled Runtime/Budget interfaces.
- **Writeback/proof:** Profile derivation/Context/Runtime/Budget/Storage and SL-02.M1 consuming interface. Verify dispatch counts, uncertain response, rejected output, restart/local completion and no hidden model call.

<a id="cg03s1-q34"></a>

### CG03S1-Q34 — No legacy request-format support in local development

- **Status:** ACCEPTED USER AMENDMENT. The receipt-only legacy-command compatibility recommendation was not accepted as implementation scope.
- **Decision:** This is a local development project with no old-format callers to support. Update backend and frontend to the revised protocol together; do not build old request-format parsing, adaptation, old command replay endpoints or backwards-write support. New contracts/API guides must clearly identify their target protocol and coordinated client regeneration rather than claim backwards compatibility.
- **Data boundary:** Q38 subsequently also removes Q24's old-development-data migration/compatibility obligation. New-protocol receipt/revision/uncertain-outcome and post-transition exact-history guarantees remain effective; do not interpret a discarded old receipt as a new-command result.
- **Supersession/writeback:** SAV/COM/Storage/API guides and SL-02.M1/M2 handoffs omit legacy request adapters and, under Q38, legacy data conversion/archive support. Existing independent Entry/Preferences protocol meanings are unaffected. Tests cover revised clients, the agreed development reset and new-model history/recovery, not fabricated legacy caller or old-database upgrade support.

<a id="cg03s1-q35"></a>

### CG03S1-Q35 — Editable explicit default replacement on removal

- **Status:** ACCEPTED USER AMENDMENT.
- **Decision:** When deleting the default while other active Resumes remain, preselect the next item in the observed canonical list, or the previous item if no next exists, but let the user manually choose another active replacement. The confirmation identifies the actual selected replacement and resulting portrait rebuild. Commit only that explicit selection.
- **Concurrency:** Preserve the required target/default-selection admission and fail on conflicting default/replacement availability rather than silently pick another target. Last-Resume removal remains Q18's null/default-unavailable case.
- **Supersession/writeback:** Replace WSP-011/CG03-Q70's prohibition on requiring/manual replacement selection to permit the selector while retaining its convenient initial value. Product §3, Workspace/Save/UI/API, SL-02.M1 and browser proof must cover overridden preselection, races and the displayed exact consequence.

<a id="cg03s1-q36"></a>

### CG03S1-Q36 — Retain links for provenance without admitting hidden targets to the model

- **Status:** ACCEPTED.
- **Decision:** Preserve source link values in deterministic Evidence/provenance, but exclude hidden inline hyperlink targets and the structured project URL from model-facing portrait input. Use original visible text and admitted career fields. Do not fetch linked pages or infer repository/project capabilities from an address. Visible source wording remains subject to ordinary privacy/input admission.
- **Writeback/proof:** Evidence/Profile/model-projection/Context/Tools and Resume link semantics; SL-02.M1 and downstream consumers. Distinguish retained source from model-visible projection, prove no URL fetching and no capability claims from hidden link targets.

<a id="cg03s1-q37"></a>

### CG03S1-Q37 — Minimal semantic capability index

- **Status:** ACCEPTED.
- **Decision:** Each Profile capability entry contains a name, a short description and one or more concrete evidence_ref values. This can represent education, skills, experience domains and project abilities without a second copy of Resume content. Do not add automatic proficiency levels, capability scores or personality labels. DeepFit still inspects exact source evidence for its own conclusions.
- **Writeback/proof:** Profile representation/admission and consumer interface; SL-02.M1/SL-05. Check required references, bounded descriptions, absence of unsupported scoring fields and source-supported semantic summaries.

<a id="cg03s1-q38"></a>

### CG03S1-Q38 — Development-stage data reset replaces legacy preservation

- **Status:** ACCEPTED USER SUPERSESSION. The proposed read-only legacy archive was rejected.
- **Decision:** Old development data may be deleted and affected table structures rebuilt for the new model. Do not implement Q24's legacy data migration, old library archive or compatibility readers merely to preserve disposable development state. This supplements Q34's exclusion of old request-format handling.
- **Scope/time:** This session remains documentation-only: no database, table, artifact payload or code is actually deleted or rebuilt. The implementation handoff must define the explicit reset/fresh-initialization path and its affected data scope; startup/read must not silently erase data. Preserve historical design/verification documents as evidence of the old baseline, not as current compatibility requirements.
- **Future history:** The reset concession applies to the transition from the old development model. It does not weaken exact immutable Resume/Evidence/analysis/material references created under the new model, permit cross-version overwrite, or turn ordinary Resume removal into physical erasure.
- **Writeback/proof:** Storage/Save/Materials/Common/API target applicability, Development handoffs and acceptance. Replace legacy migration tests with scoped reset/fresh-initialization and new-model durable-history/recovery proof. Resolve the reset extent before instructing an implementer to discard unrelated development records.

<a id="cg03s1-bc3"></a>

### CG03S1-BC3 — Two-level deterministic Evidence with stable logical source IDs

- **Status:** ACCEPTED final Evidence direction supplied alongside Q36–Q38. Exact editor identity-transition and serialized representation rules remain to be closed.
- **Authority:** Resume remains the user-maintained source. CandidateEvidenceProjection is a read-only deterministic projection of the default Resume's exact current version, not a separately maintained library. The editor's structured experience fields and paragraph/list-item AST boundaries determine extraction; no model guesses bullet segmentation or manufactures evidence text.
- **Entry level:** Provide one Entry-level Evidence unit for a complete project, work experience, education experience or other admitted entry. Preserve its complete structured source and user-authored body for whole-experience context. Privacy/model projection applies separately to what may be transmitted; Q36 remains effective.
- **Block level:** Provide Block-level Evidence for each valid paragraph or list item, preserving exact original visible text and its parent entry. A project's four bullets yield four block units. Do not count a listItem and its internal paragraph twice as separate semantic evidence. Other unsupported editor node types are not silently introduced into the owned Resume format.
- **Stable logical addresses:** Assign stable logical entry_id and block_id values rather than relying solely on mutable ProseMirror character offsets or array positions. Bind evidence to the exact resume_version_id plus entry identity, and block identity where applicable. A logical block may continue into a new ResumeVersion, but that version creates a different exact Evidence binding; it never replaces historical text or existing analysis references. ID format, allocation, copy/split/merge and cross-entry movement rules still require agreement.
- **Profile separation:** LLM abstraction produces only Q37's lightweight capability index with evidence references. A supported semantic label such as Redis cache practice belongs to Profile; the original Redis sentence remains the Evidence. No summary/rewrite/inference replaces source text in either evidence level.
- **Progressive use:** DeepFit begins with Profile and fetches relevant Block evidence, expanding to Entry-level context or additional Evidence when needed. Q15 still prevents a retrieval miss or budget-limited inspection from becoming an unsupported negative. Initial whole-Resume model loading is not required for DeepFit; the independently owned Profile derivation scope retains Q33's bounded invocation policy.
- **Scoped supersession:** Extend Q11's deterministic source representation and supersede Q16's lack of cross-version logical identities while preserving exact-version evidence. RES-005/006's no-entry/block-business-ID assumptions and current editor adapters need explicit new-schema clauses; there is still no user-editable Evidence/Assertion authority. Q23 must map validated same-content reuse through the stable logical IDs into a new exact-version binding.
- **Writeback/proof:** Resume/Evidence/Profile/Save/Common/Storage source interfaces; editor adapter and UI guidance; Materials consumed AST; SL-02.M1/M2, SL-04 import, SL-05 Evidence Tool and SL-06/07 source-scoped suggestions. Cover stable edit/reorder identity, new identities for genuinely new content, exact history, parent relationships, no duplicate list-item evidence, plain text fidelity, progressive expansion and no model-authored Evidence.

<a id="cg03s1-q39"></a>

### CG03S1-Q39 — Stable logical identity through editing

- **Status:** ACCEPTED.
- **Decision:** Text/mark edits, reordering and paragraph/list-item conversion retain IDs. New, copied or pasted content receives new IDs. Splitting keeps the first block ID and allocates a new second ID; merging keeps the first and removes the other from the current version. Draft undo/redo restores the associated content and IDs. Whole-Resume copying produces a new root and new entry/block IDs without derivation relationships. The editor allocates logical IDs; backend admission validates and preserves them rather than reconstructing identity from positions or text equality.
- **Writeback/proof:** RES-017–024, EVD-016–023, COM-050, SAV-018–025; adapter round trips, split/merge/paste/undo/reorder and historical reference tests.

<a id="cg03s1-q40"></a>

### CG03S1-Q40 — Canonical AST adapter remains authoritative

- **Status:** ACCEPTED.
- **Decision:** Retain TipTap → canonical Resume AST → saved ResumeVersion. Stable IDs survive conversion in both directions. Deterministic Evidence consumes the persisted canonical AST; a top-level paragraph or one list item is a Block, not the list item's internal paragraph a second time. Native editor JSON/plugins are not a competing persistence protocol.
- **Writeback/proof:** Resume/Evidence/Materials and editor implementation guidance; prove exact text, marks, ID and order round trips through the actual adapter.

<a id="cg03s1-q41"></a>

### CG03S1-Q41 — Full development-store reset is permitted

- **Status:** ACCEPTED.
- **Decision:** The later implementation may explicitly reset the complete development database and associated generated materials, including old Candidate data, runtime records, Preferences and Manual Application Entries used as test data. Preserve source code, Git and configuration files. No selective old-data migration or archive is required. Reset/fresh initialization is an explicit development operation, never automatic startup/read behavior.
- **Scope:** Documentation only in this session; no actual data deletion or schema execution. Preserve immutable history generated after the new baseline and historical repository decision/evidence records.
- **Writeback/proof:** STO-054–058, source/client handoffs and fresh/reset acceptance; verify path containment, runtime exclusion and no reset on ordinary startup.

<a id="cg03s1-publication"></a>

## Authorized publication — completed

Published **2026-09-24.S2M1S1-r1** after the accepted Q39–Q41 closure. The user already requested formal writeback and per-milestone backend/frontend handoffs; no implementation, reset, installation, commit or push is included.

New stable scopes: COM-050–051; WSP-013–015; RES-017–024; EVD-016–023; PRO-010–016; SAV-018–025; STO-054–058; MAT-031–033; PRF-024; CTX-016; TOL-015; EVO-027. Existing IDs retain historical definitions with explicit applicability/supersession; unchanged value/AST/material/runtime rules are referenced rather than inverted. Product/Architecture/Acceptance, consumer plans and source/runtime API distinctions are rewritten to match effective decisions. Q26 governs milestone allocation; Q34/Q38/Q41 remove legacy request/data compatibility, not new-model history guarantees. Final verification must report both Development §9.2 seams, mechanical checks and unexecuted runtime/browser/reset scope.

## Read-only implementation observations

- `backend/src/jobhunter/application/candidate/authority.py`: Profile publication and Evidence update/retirement do not publish Resume versions; new/switched source admission still enforces the current/active checks described above.
- `frontend/src/features/resume/editor/resume-editor.tsx` and `preview/draft-preview.tsx`: member bodies are local; structured values are read from exact Evidence fields. Explicit source adoption can retain local content or separately reset it. Creating Evidence inside the editor first saves Knowledge.
- The editor's Profile dialog saves the shared Profile, then separately applies the saved source to the Resume draft. `frontend/src/features/candidate/use-command.ts` retains uncertain requests for explicit replay; static inspection found no automatic polling or merge capability there.
- Existing backend lifecycle and transaction tests describe retained historical sources and new-reference races. They were inspected, not rerun. Candidate frontend directories/tests were untracked at transfer but are tracked at the Q6–Q10 resumption checkpoint above; neither observation substitutes for new-model delivery or browser verification.

## Current decision frontier

Closed for the consumed supplemental scope after Q39–Q41. Q1–Q5 remain withdrawn; Q24 and the stated Q16 portions are superseded. Exact business schemas and finite registered model-admission interfaces below are the concrete expression of accepted choices, not new scoring, cross-source optimization or legacy compatibility features. Future Fit scoring, business retrieval execution, Import parsing and conversational/optimization task protocols remain at their actual milestone Grill. Authorized publication and both documentary review seams are complete; downstream task-specific protocols remain explicitly outside this supplemental frontier.

## Writeback ownership

| Concern | Maintained owner |
| --- | --- |
| User behavior and visible edit boundaries | Product and the applicable UI/API guides |
| Authority, transaction, lineage and recovery changes | Architecture; Profile, Evidence, Resume and Candidate Save Contracts |
| Snapshot rendering and exact-source consumption | Materials, Profile/Resume material projections and affected storage/worker interfaces |
| Persisted representation and existing data | Storage, explicit development reset/new-schema initialization and preserved migration source history |
| Required proof, delivery scope and interfaces | Acceptance; SL-02 plan and affected future consumer plans |
| Effective readiness and implementation evidence | Progress and traceability, only after actual changes or reviewed closure |

Identify exact affected sections/IDs and present the architecture writeback plan before replacing published invariants. Do not repurpose published requirement IDs or rewrite historical migration definitions. Keep unreviewed replacement semantics out of implementation.

## Verification checkpoint

Documentary closure: Decision-to-Document Traceability and Cross-Document Semantic Consistency reviewed, with the actual mappings/findings resolved in [Traceability §6.7](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope). The maintained Contract checker passes 453 unique IDs, all current-owner/transfer local links, 36 supplemental Q mappings plus BC1–BC3 and unchanged historical CG04/CG05/CG06 coverage; readiness is 40 Ready / 60 Pending / 100 current scopes. Ruff check/format and git diff --check pass. Five injected checker defects (duplicate ID, bad anchor, missing supplemental decision, readiness drift and missing historical decision) were correctly rejected using in-memory test overrides.

No backend/frontend product code, generated API schema, original tracked Grill body, migration/database/reset, dependency installation, live model call, commit or push was changed/executed. Runtime/browser/provider acceptance was not rerun; historical counts remain limited to their original revision. The only non-document change is the maintained documentation validation script’s expanded strict coverage.

## Publication destinations

The effective decision-to-ID/owner/proof map and per-milestone backend/frontend transfer are maintained in [Traceability §6.7](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope). Current normative applicability notices preserve old IDs without restoring opposite authority semantics. Profile schema v1 business fields are name, description and evidence_refs; source/generation state is separate metadata. New source ResumeVersion, Candidate receipt and Materials manifest/Artifact use their explicitly published schema 2.

<a id="cg03s1-profile-entry-naming"></a>

## Profile entry naming amendment — 2026-09-24

- **Status:** ACCEPTED user correction after publication: rename the Profile collection field from `capabilities` to `entries`.
- **Current expression:** `CandidateProfileProjection.entries: ProfileIndexEntry[]`. Each entry retains `name`, `description` and `evidence_refs`; Profile schema remains v1. PRO-013’s model-output collection also uses `entries`, while its local evidence-ID representation and backend expansion remain unchanged.
- **Writeback:** PRO-011–013, Product §3.3, the SL-02.M1 target API guide and development handoff. This is a naming correction to the unimplemented replacement schema, with no legacy alias, data migration or product code change.

<a id="cg03s1-entry-incremental"></a>

## Entry-level incremental portrait amendment — 2026-09-24

- **Status:** ACCEPTED user architecture direction after the Profile naming amendment; now refined and closed by Q42–Q46 below. Q42 supersedes the initial allowance for cross-Entry Profile refs. Earlier proposed recursive closure was rejected.
- **Semantic unit:** Resume Experience Entry is the main semantic rebuild unit, rather than an isolated changed bullet. Any Block Evidence addition, modification or deletion makes its owning Entry dirty. Model input for that Entry includes its complete admitted structured background and all current original Evidence. EVD-019 privacy exclusions still apply; “complete” does not admit contacts, Header, hidden links or project URLs.
- **Incremental result:** Regenerate or revise the dirty Entry's corresponding ProfileIndexEntry collection. Reuse unaffected Entries' supported Profile entries and rebind their references to the new exact ResumeVersion. Expand beyond dirty Entries only for cross-Entry capability references or changed portrait-relevant global fields. This does not introduce a new global field or make excluded Header/contact data semantic input.
- **Preserved boundaries:** Evidence remains deterministic original source, Profile remains read-only, old exact references remain immutable, and valid source Save does not depend on model success. Paired publication, current-build fencing, actual Runtime admission and no uncertain remote replay continue to apply. This direction alone does not authorize one Provider call per Entry.
- **Scoped supersession:** Presentation-only reuse is no longer the entire target reuse policy. PRO-012/013, EVD-023 and CTX-016 need scoped replacement for mixed generation/reuse, subset output and Entry-context admission; the existing all-or-nothing forms must not be used to implement this amendment. SAV-021–023 and STO-056/057 require the corresponding exact-plan, dependency and recovery agreement. No generic Runtime redesign is implied.
- **Resolved frontier:** Q42–Q46 below settle Entry locality, baseline versus currentness, the current single-request policy and explicit full refresh. PRO-011–014/017–020, EVD-023/024, SAV-022/026, STO-059, CTX-016 and EVO-028 publish the corresponding identity, grouped output, merge/provenance and recovery interface. Empty group and deletion representation follow the retained no-fabrication/whole-pair rules; they are not authorization to infer absent capabilities.
- **Transfer:** The new consumer Contract is ready for implementation under the updated SL-02.M1/SL-03.M2 handoffs, with actual protected-invocation adoption still required. Adapt the existing Profile DTO/validators and build trigger/refresh matching to r2. Deterministic source/Materials remain independently usable; no implementation, browser/provider acceptance or data reset is claimed by this publication.

<a id="cg03s1-q42"></a>

### CG03S1-Q42 — Entry-scoped semantic index without dependency expansion

- **Status:** ACCEPTED USER REPLACEMENT of the proposed recursive closure.
- **Decision:** Each ProfileIndexEntry belongs to one source_entry_id and all its Evidence refs belong to that Entry. A Block or background-field change rebuilds the complete owning Entry and replaces that Entry's Profile group. Shared Blocks within one Entry cannot expand beyond it. Equal skill labels in different Entries remain independent. No stored capability combines multiple Entries; DeepFit performs cross-Entry aggregation only at runtime.
- **Writeback:** PRO-011/013/017/019/020; EVD-024; CTX-016; Product §3; Architecture §5/6; Acceptance §4; EVO-028. The schema applies to all existing structured Entry kinds, not a newly invented Experience type. Current schema introduces no global career-fact field. User-explicit source_entry_id becomes derived source identity on ProfileIndexEntry; its three descriptive fields and entries collection remain.

<a id="cg03s1-q43"></a>

### CG03S1-Q43 — Same-Resume baseline is distinct from current portrait

- **Status:** ACCEPTED with the user's currentness clarification.
- **Decision:** Choose the latest successful compatible same-Resume portrait as incremental baseline despite failed intervening versions. Compare that baseline's exact ResumeVersion against the target and reuse only proven unchanged Entries. Switching back to an unchanged exact source permits compatible historical-pair reattachment through current publication admission. A different source version requires a newly assembled exact pair; the old pair is only a baseline. No compatible successful baseline means full first generation.
- **Writeback:** PRO-018–020, EVD-024, SAV-026, STO-059. Exact reattachment records current build qualification without rewriting the old pair; source/config integrity, permissions and stale/ABA fences survive. Durable derivation ordering and retained plans make selection/recovery unambiguous.

<a id="cg03s1-q44"></a>

### CG03S1-Q44 — One request is the current consumer policy

- **Status:** ACCEPTED with the user's version-scope limitation.
- **Decision:** Current implementation sends the complete context of all dirty Entries in one model request. Capacity excess fails closed; no truncation, silent split, batching or hidden additional call. Do not freeze one request as an eternal Domain invariant. Future controlled batching requires a separately reviewed consumer version with budgets/recovery/publication while preserving Entry semantics.
- **Writeback:** PRO-014, CTX-016, SAV-026, STO-059 and EVO-028. Current requests retain original no-repair/no-retry/uncertain-no-replay policy and protected invocation boundaries.

<a id="cg03s1-q45"></a>

### CG03S1-Q45 — Deletion cannot propagate through cross-Entry references

- **Status:** ACCEPTED user's clarification that cross-Entry Evidence refs do not exist in this model.
- **Decision:** Deleting an Entry removes its derived group without invalidating another Entry. Deleting a Block in a surviving Entry dirties that whole Entry under Q42. No recursive dependency mechanism remains.
- **Authoring consequence:** With no surviving dirty Entry, deletion and rebinding are deterministic zero-call work. Grouped model output explicitly represents a surviving Entry with no supported result as entries:[]; missing requested groups are invalid, never implicit empty results. Only the assembled whole Profile determines readiness under the preserved no-fabrication and nonempty-portrait rules. This is a necessary representation of Entry replacement, not a claim that the user's short Q45 answer separately approved additional capability semantics.
- **Writeback:** PRO-013/019/020, EVD-024, SAV-026, STO-059, Acceptance §4 and EVO-028.

<a id="cg03s1-q46"></a>

### CG03S1-Q46 — Explicit refresh fully regenerates

- **Status:** ACCEPTED.
- **Decision:** Explicit user refresh regenerates all current admitted Entries, even if Resume content did not change, so it can correct extraction. Automatic source/default updates use incremental reuse. Existing unavailable/paired publication, failure and explicit retry behavior survives.
- **Necessary interface:** Active automatic work is not the same request as full refresh. Matching active FULL work deduplicates; otherwise refresh creates a new FULL build/fence, preserving earlier Invocation outcome/cost truth. A repeat of the same receipt never creates another build. No client mode field or background call loop is introduced.
- **Writeback:** PRO-018/019, SAV-020/022/026, STO-059, CTX-016; frontend refresh expectations and both implementation handoffs.

### Incremental publication — 2026-09-24.S2M1S1-r2

The [r2 traceability review](../../progress/traceability.md#entry-incremental-review) owns decision-to-document and cross-document verification. Added IDs are PRO-017–020, EVD-024, SAV-026, STO-059 and EVO-028; existing schema, input and provenance clauses are amended within this scope. No broader Runtime, Materials, optimization, Job or deferred assistant-apply behavior is changed. This is documentation and checker maintenance, not executed product acceptance or a Git submission.
