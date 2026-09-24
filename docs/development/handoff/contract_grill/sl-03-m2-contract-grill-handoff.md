# SL-03.M2 Contract Grill Handoff and Session Prompt

> English is authoritative. This is a user-requested cross-conversation prompt, not a normative Contract, a new milestone plan or implementation evidence. Execute the interview in Chinese and write formal documentation in English. The user's specific workflow below controls over generic skill defaults and older handoff procedures.

[Milestone plan](../../../plans/slices/sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) · [Contract ownership](../../../contracts/structure.md) · [Actual progress](../../../progress.md) · [M1 review](../../../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) · [M1 decisions](../../../design/contract/sl-03-m1-grill.md) · [M1 development handoff](../sl-03-m1-handoff.md)

## 1. Execute this task in the new conversation

Work in `/Users/soulboy/projects/JobHunter`. Use `$grill-me` to start **SL-03.M2 — Protected semantic invocation and evidence Contract Grill**. Read `/Users/soulboy/.codex/skills/grill-me/SKILL.md` and the underlying `grilling` skill it invokes. Apply the actual available skills, repository instructions and this session-specific workflow.

The interview concerns the detailed Contract consumed by M2: authority, data shapes, identities, exact references, inputs/results/errors, admission, atomicity, concurrency, recovery, persistence and verification obligations. It is not a fresh product-discovery interview. Do not repeatedly ask whether the user wants already-approved capabilities or reopen M1 decisions without a concrete conflict.

Start the already-requested interview after the required reading and factual checks. Do not stop at a plan or ask permission to read documents, create the sole Grill register or ask the first questions. Start with ten questions, Q1–Q10, under section 5. This prompt does not itself authorize implementation or final normative publication.

Read-only repository inspection and necessary scoped research are authorized. Do not implement backend/frontend features, install dependencies, scaffold a framework, execute user-data migrations, run live Provider/platform actions, deploy services, commit or push. Those actions require their own applicable user authorization. A skill's generic wording does not expand the task into sending messages or taking external actions.

## 2. Required reading and entry verification

Begin with applicable AGENTS.md instructions, `git status --short`, current HEAD, and the relevant source/test/migration inventory. Preserve unrelated changes and other conversations' work. Inspect both committed and uncommitted state; neither a file's existence nor a historical handoff proves verified capability.

Read the following before presenting the first questions. Read relevant sections and both ends of needed interfaces; do not scan the entire repository or reread every historical Grill by default.

1. **Navigation and authority:** `docs/index.md`, `docs/contracts/README.md`, `docs/design/README.md`, `docs/design/contract/README.md`.
2. **Actual state:** `docs/progress.md`, `docs/progress/README.md`, and `docs/progress/traceability.md`, especially the milestone ledger, scope readiness, SL-03.M1 review and any newer actual implementation evidence.
3. **Scope and dependencies:** `docs/plans/implementation-plan.md`, `docs/plans/slices/README.md`, and all three milestone boundaries in `docs/plans/slices/sl-03-invocation-requirements.md`. M1, M2 and M3 must remain distinguishable.
4. **Product and architecture:** applicable `docs/spec.md` sections on independent capabilities, controlled execution/privacy, recovery and evidence; `docs/architecture.md` sections 9–13, 15 and relevant Contract ownership in 16. Locate current headings rather than relying on old line numbers. Read business sections only where the actual consumer interface needs them.
5. **Required proof:** `docs/acceptance.md` sections 8–10 and its Eval routing; `docs/acceptance/evaluation.md`; `docs/evaluation/README.md`. Separate future required proof from recorded executed results.
6. **Normative bodies and planned ownership:** `docs/contracts/index.md`, `docs/contracts/structure.md`, `docs/contracts/agent/execution-runtime.md`, `docs/contracts/evaluation/evaluation-observability.md`, and applicable `docs/contracts/common.md`, `docs/contracts/foundation/storage.md`, `docs/contracts/foundation/workspace.md`. Check whether `agent/tools.md`, `agent/context.md` and `foundation/budget.md` now exist. If absent, use their Structure entries as planned responsibility maps, not normative definitions. Do not create empty placeholders.
7. **M1 transfer and effective decisions:** `docs/development/handoff/sl-03-m1-handoff.md`, any newer applicable transfer, and `docs/design/contract/sl-03-m1-grill.md`, including its accepted decisions, partial supersessions, deferred interfaces and publication checkpoint. Current normative clauses govern detailed definitions; history explains interpretation and scoped changes.
8. **Relevant preserved provenance:** `docs/design/harness/README.md` and its `recovery.md`, `context.md`, `budget.md`, `tool.md`, `storage.md`; `docs/design/eval/README.md` and `agent-evaluation.md`. Follow relevant references into `docs/design/grill-me-design-tree.md` or `docs/design/contract/contract-design-inventory.md` only when needed. Historical examples and inventory proposals are not finalized schemas. Memory detail belongs to later consumers unless a present boundary requires checking it.
9. **Delivery and research discipline:** `docs/development.md`, especially section 9.2; `docs/development/README.md`, `docs/development/repository-structure.md`, `docs/development/technology-stack.md`, and `docs/development/evaluation.md`.
10. **Actual engineering facts:** `backend/README.md`, current `pyproject.toml`/`uv.lock`, relevant bootstrap, Domain/Application/persistence implementations, migration head and maintained tests. Inspect installed tools only where necessary. Do not install or run a full backend suite merely to prepare the interview.

### Source checkpoint at prompt preparation

SL-03.M1 Contract work was committed as **683fc3f**, `docs(contracts): publish SL-03.M1 durability and recovery contracts`, at revision **2026-09-23.S3M1-r1**. It added EXR-001–034, COM-047–048, STO-040–045 and EVO-001–007. At that publication checkpoint the repository had 300 requirements and 30 Ready / 63 Pending scope rows. These are historical counts, not future constants.

The publication handoff inspected a committed schema-4 baseline without an Invocation Runtime. **By preparation of this prompt, the working tree had changed:** modified bootstrap/Store files and untracked invocation Domain/Application/persistence code, harness tests and `backend/alembic/versions/d092ea64bf17_invocation_durability.py` were present. Those changes were not authored, tested or accepted by this prompt-writing task. Do not repeat “M1 has no implementation” as a current fact, assume the new code is complete, or freeze a schema number from its filename. Reverify actual code, migration head, commit state and evidence at new-conversation entry. Preserve all concurrent work.

M1 implementation availability does not block independent M2 Contract discussion. It remains a genuine dependency before M2 implementation uses that infrastructure. Distinguish Contract reviewed, source present, code committed, checks executed and capability accepted.

## 3. Goal, document responsibility and scope

Close the complete first-use Contract for a real protected semantic invocation: bounded Skill/Run execution, actual Model/Tool boundaries, exact headless Context, current permission and revocation, capacity, operation/Run budget, reservation/settlement, durable evidence and admitted telemetry. M1 supplies the existing execution-authority/durability foundation; M2 supplies its actual protected semantic consumer agreements.

| Destination under docs/contracts/ | Expected M2 work | Scope limit |
| --- | --- | --- |
| `agent/execution-runtime.md` | Extend Skill/Run semantic admission, real request/response and Gateway/stream interfaces, and actual integration with M1 | Do not create another recovery protocol or a universal business lifecycle |
| `agent/context.md` | Introduce actual initial ContextPackage, immutable sent ContextFrame, exact inputs, headless capacity and protected-input revocation | Interactive compaction and Memory integration remain with their first consumers |
| `agent/tools.md` | Introduce capability/permission intersection, owned typed action admission, source checks and returned-content admission | No speculative complete future action catalog or hidden Ensure/model call inside a read |
| `foundation/budget.md` | Introduce foreground/operation ownership, Run limits, atomic reservation, counters, settlement and unknown exposure | Do not move business results or platform risk into budget accounting |
| `foundation/storage.md` | Extend actual semantic payload/evidence integrity, availability and retention agreements | M1's deferred purge does not automatically become a mandatory generic cleanup subsystem |
| `evaluation/evaluation-observability.md` | Extend isolated real-path infrastructure, exact fixtures/configuration, complete checks, independent judge resources, retained evidence, re-evaluation and derived export | No second Eval platform; task-specific evaluator meaning belongs to its first semantic consumer |
| `common.md` | Extend only actually shared scalar/reference/error expression | Reuse existing conventions; avoid a universal base entity or duplicate authority |

The owning Slice plan defines milestone scope. Structure defines document ownership. Reviewed Contract bodies define detailed norms. Product, Architecture, Acceptance and Progress keep their own responsibilities; no newer timestamp overrides all owners.

Exclude RequirementSet meaning and RequirementParse/Ensure implementation (M3), Candidate/Resume Fit scoring, Advisor Session/Proposal workflows, interactive compaction, Memory learning, platform execution and unrelated future consumers. Do not infer a public HTTP API, new UI workflow, generic policy entity or permanent numerical default without an actual present consumer and an accepted decision.

LangGraph, Provider SDK and self-hosted Langfuse research must verify applicable selected versions, sources/licenses, retry behavior, serialization, callbacks, masking, judge resources and export boundaries when the relevant question depends on them. Use official sources and actual code for facts. Distinguish observed behavior, proposed design and accepted Contract. Do not present old research as current deployment or pin implementation constants simply to fill a schema.

## 4. M1 agreements to inherit

Read the actual EXR/COM/STO/EVO clauses; this list is an orientation, not a substitute or second authority.

- Run identity survives safe recovery. Generation advances on grant/regrant only; revocation clears current qualification. A future Run-level retry is distinct from same-Run recovery and consumer-specific Invocation repair.
- A durable dispatch intent is not a transferable sending permit. The original still-live winner may reconcile its uncertain acknowledgement only with proof of its own committed intent, no adapter entry and valid authority; crash/replacement cannot reuse it.
- First response publication requires original-path/current-authority and dispatch-generation checks. Read-only confirmation of an identical existing durable response precedes new-write eligibility and can remain legal after ending/revocation/expiry.
- Preparation derives owning run_id from qualification. Publication derives response_format_key from Invocation. Do not restore independently submitted duplicate authority.
- Response format determines stable UTF-8 serialized bytes. Integrity is measured against actual stored bytes, with atomic response/metadata/phase publication and truthful storage uncertainty.
- Deadline timing belongs to the actual consumer. Expiry forbids new remote effects/late first publication; already durable responses may support explicitly admitted finite local recovery with lawful authority. No deadline reset or reopening an ended Run.
- Consumer-confirmed whole-Run completion can avoid unnecessary payload access, but Run ending still needs lawful qualification or ownerless atomic coordination. One committed result is not automatically whole-Run completion.
- A complete oversized response and reception stopped before remote termination have different evidence/outcome semantics. Unknown remote work does not become zero cost or permit silent replay.
- M1 protects all response payloads of OPEN Runs and retains terminal payloads because no purge consumer is delivered. It does not create Pin entities, retention enums, response timestamps or retry lineage without consumers.
- Controlled pure-read Tool recovery does not authorize MODEL replay, hidden Ensure or business writes. Exact lineage alone does not make every source payload a required rendering/recovery input.
- Runtime failure causes, operation rejections and consumer business outcomes stay distinct. Do not restore the rejected generic RECOVERY_NOT_ADMITTED fallback.
- Actual required production admission, formats, Tool agreements, budget and evidence must close in their consumer. M1 readiness is not blanket M2 readiness.

## 5. First response and question rounds

After reading and verification, give a concise Chinese orientation with the goal/exclusions, actual M1 checkpoint, owner-to-document map, dependency-ordered outline and factual research gaps. Then ask **Q1–Q10** immediately. Do not repeat a request to begin.

Each ordinary round has **ten questions**. Number them continuously: Q1–Q10, Q11–Q20, and so on. Each question identifies a concrete Contract choice, its owner/boundary and a recommended answer with a short reason or necessary counterexample. Use the skill's question/recommendation format, in Chinese. Clearly distinguish a proposal from an already accepted rule.

Only ask questions whose prerequisites are settled. Do not assume an answer to another still-open question in the same batch. If a research fact blocks one branch, advance independent ready branches. Never pad a final round with artificial questions: if fewer than ten genuine unresolved choices remain, say why and ask only those remaining choices. A genuine critical ambiguity may require a focused clarification before its dependent batch.

Suggested order is consumer/Skill boundaries → Context/Tools → Budget → real Provider/stream and integrated recovery → Eval/observability → complete operation/error/storage/interface review. Reorder when accepted answers change dependencies. The preparation estimate was **20–26 ten-question rounds**, not a quota or promise. Reuse accepted decisions and report scope-driven estimate changes honestly.

Do not turn inspectable repository/SDK facts into questions for the user. Use sub-agents sparingly for bounded critical factual checks or necessary closure review, not every round and not a routine whole-repository audit. Agents may supply evidence and identify conflicts; the user's decisions remain theirs.

## 6. Interpret answers and execute the same round workflow

The user's usual answer is “all agreed” followed by amendments to selected questions. Interpret that as acceptance of the round's other recommendations, with the specified refinements applied to the named questions. Do not require ten separate confirmations. An explicit correction controls the affected proposal; it does not silently replace unrelated accepted decisions.

If the user comments only on a subset without accepting the rest, do not invent blanket agreement. Resolve only the ambiguity that matters. If a suggested amendment conflicts with another effective decision or leaves multiple materially different meanings, explain the precise conflict and ask a focused question; do not quietly choose a policy or manufacture acceptance. A factual assertion in an answer may still require verification.

After **every answered round**, perform this sequence before presenting the next questions:

1. **Review the answer.** Resolve acceptance and amendments against the exact recommendations, effective previous decisions and applicable current clauses. Identify rejected proposal fragments, remaining branches and affected dependencies. Do not merely append “all agreed.”
2. **Determine scope of impact.** Ordinary field/interface refinements remain in the Grill register. For an explicit architecture change or important decision requiring owner reconciliation, follow section 7; do not silently broaden the write set.
3. **Persist the effective decisions.** Update the single `docs/design/contract/sl-03-m2-grill.md` before moving on. Check that file and existing namespaces at entry; use CG06-Qn only if CG06 is free, otherwise select an unused stable namespace without renumbering existing records. Preserve exact question identity throughout.
4. **Record conclusions in English.** Include accepted meaning, necessary rationale/boundary examples, intended normative owner/landing clause, unresolved branches, and actual writeback location. Record decisions, not verbatim question transcripts or duplicated conversation summaries. Pending destinations must not look like published requirements.
5. **Preserve supersession.** Keep historical decisions and mark a fully or partially displaced clause SUPERSEDED/PARTIALLY SUPERSEDED, with the replacement decision, exact affected fragment and impact scope. Do not leave a superseded rule looking effective or delete its provenance.
6. **Perform a local check.** Verify amendments actually landed, no direct conflict with relevant current rules, IDs/anchors/references are valid and whitespace is clean. Check only the affected branch and necessary shared interface. Do not repeat full Architecture/Acceptance/readiness reviews or entire test suites every round.
7. **Report and continue.** Briefly state what was persisted, significant refinement or unresolved issue, then ask the next ten ready questions. A failed write or unresolved prerequisite must not be hidden by moving to dependent questions. On “retry,” inspect what actually persisted and resume without duplicating decisions or renumbering.

When resuming after interruption or context compaction, recover the last accepted/persisted round and open branches from the register and current user messages. Do not restart the interview, re-ask answered batches or treat an unfinished assistant recommendation as user acceptance.

## 7. Document mutation discipline during the interview

The user's later explicit correction controls: **ordinary rounds update only the milestone's single Grill record.** Do not mechanically write every answer into spec, Architecture, Acceptance, plans, Contract bodies, Progress or traceability.

At initial start, create/reuse the single register and add its necessary design-navigation entry. A one-time factual stage update in Progress/traceability is allowed where needed to record that the Grill began, with readiness still Pending. Do not create another progress document. Subsequent status changes follow actual events, not round count.

For a user-identified architecture change or important decision, explain which current owners/interfaces would change, why, and the proposed scoped writeback. The user will explicitly direct that review/update. Do not infer blanket owner-writeback permission from acceptance of ordinary recommendations. If an existing Ready scope is discovered to be invalid, record the concrete issue, stop relying on that scope, and present the needed correction plan rather than ignoring the defect or silently rewriting owners. Resolve necessary architecture choices before asking dependent field questions. An already-authorized scoped update need not be reconfirmed.

Formal Contract bodies are not scratchpads for undecided suggestions. Keep accepted design in the register until the relevant scope is closed and publication is authorized. Do not prepublish incomplete schemas or advance readiness because a batch was accepted.

Do not create per-round `storage-decisions.md`, summary reports, completion reports, extra review registers, placeholder Contracts or duplicate handoffs. Do not rewrite this prompt after each answer. Research facts and unresolved implications should stay in the relevant register branch or an already-owned necessary research destination.

The user expressly permitted temporary repository retention of the existing `scripts/check_contract_links.py` for repeated Contract Grills. Keep it until **all** Contract Grills finish; do not delete it at the end of M2. Update it only when publication changes maintained ID/mapping checks. Put new ad hoc audit/helper scripts in temporary/cache storage outside the project. Do not promise that sandbox caches are durable across new conversations.

## 8. Closure audit and publication authorization

An empty question frontier means the interview is ready for closure; it does not itself establish published readiness. Explain remaining closure work and obtain the user's explicit agreement for the necessary owner writeback and normative publication, as in the M1 conversation. If the user has already authorized that stage in the new conversation, proceed without asking again. M1's publication/commit authorization does not authorize M2 publication or Git operations.

During authorized closure, complete both Development section 9.2 verification seams and the necessary interface review:

1. **Decision-to-Document Traceability:** map every effective decision to actual normative clauses or an explicit future boundary; every new norm needs an accepted source or a clearly identified representation-only authoring arrangement. Audit partial supersessions so old mechanisms do not return through a later summary.
2. **Cross-Document Semantic Consistency:** compare relevant Product, Architecture, Contracts, plans, Acceptance and actual status for authority, exact versions, permission, admission, transactions, concurrency, failure/recovery and scope. Link existence does not prove agreement.
3. **Producer/consumer closure:** review Skill/Application → Context/Tool admission → budget reservation → Runtime/Gateway dispatch → durable response → usage settlement/local recovery → consumer business commit, plus evidence/storage/judge/export consumers. Canonical commits and settlement must not depend on telemetry. Do not close only the producer half.
4. **Normative completeness:** verify field/type/required/null constraints, exact equality and format bytes, enums/transitions, complete operation inputs/results, error distinctions/precedence, execution authority, immutability/revision where applicable, idempotency, storage/migration and actual caller obligations. Do not invent HTTP/client protocols without an accepted consumer.
5. **Compatibility:** review M1 and any other actually affected existing consumers. Preserve their stable IDs, receipts, recovery semantics and evidence boundaries unless a specifically approved change is reconciled. A deferred concrete consumer must not be reported Ready.
6. **Mechanical verification:** check requirement uniqueness/references, Markdown files/anchors, decision mappings and readiness counts; run `python3 scripts/check_contract_links.py` and `git diff --check`, including equivalent whitespace/link checks for new files. If modifying the checker, run its applicable maintained lint/format/type checks and meaningful isolated negative fixtures. Use real available commands; do not claim tests that were not run. Check the staged diff separately if a later commit is authorized.
7. **Truthful readiness:** separately record reviewed specification, available upstream implementation, actual code/test delivery and accepted behavior. Document-only publication does not prove migration execution, installed SDK/Langfuse, model calls, semantic quality, frontend acceptance or milestone completion.

Consolidation may fill representation-only details implied by accepted decisions, but must not silently decide a new policy, permission, lifecycle or failure behavior. If a real semantic choice remains, record the exact gap and ask a focused follow-up before publishing that affected scope. Do not invent additional question rounds merely to repeat the completed review.

## 9. Closure write set and development transfer

Write only files whose owned scope actually changes. The expected closure destinations are:

| File or owner | Required closure work |
| --- | --- |
| `docs/design/contract/sl-03-m2-grill.md` | Close resolved branches, preserve supersession, record authorization, normative destinations, actual checks and remaining external/consumer dependencies |
| Actual consumed Contract bodies from section 3 | Publish complete English definitions with stable owner-prefixed requirement IDs; reference Common instead of duplicating shared rules |
| `docs/contracts/README.md`, `index.md`, `structure.md` | Synchronize real bodies, ID ranges, responsibilities and milestone consumption; keep future portions distinct |
| `docs/spec.md` | Update only approved changes to user-visible behavior, scope or prerequisites; leave untouched when none changed |
| `docs/architecture.md` | Reconcile approved changes to authority, responsibilities, references, transactions, concurrency and recovery |
| `docs/acceptance.md`, applicable `docs/acceptance/evaluation.md` | Reconcile changed required success/rejection/race/failure and evidence scenarios; do not label them executed |
| Owning SL-03 plan; global Implementation Plan only where affected | Reconcile scope, dependencies, delivery order or completion conditions that actually changed |
| `docs/progress/traceability.md` | Record reviewed scope/revision/IDs, per-decision mapping, interface review, actual verification and remaining Pending portions |
| `docs/progress.md` | Record Contract-stage completion and real next prerequisites; keep M2 implementation and parent-Slice completion separate |
| `docs/development/handoff/sl-03-m2-handoff.md` | Create the concrete backend development handoff after publication/review, not an empty early placeholder |
| Necessary navigation and existing checker | Add useful real entry points and maintain changed checks; no unrelated cleanup |

The backend handoff must let a new development conversation proceed by reading it: include exact consumed Contract scope and authoritative reading; reverified current HEAD/dirty state/source/migration/test evidence; available M1 components and limitations; dependency/research gates; implementation order and layer boundaries; required deterministic/semantic evidence; maintained commands; deferred features and unresolved external prerequisites. Source research is not installed capability. Inherited tests are not rerun results. Migration instructions must start from the actual head at implementation time, not a fixed schema number selected during this interview.

Preserve historical handoff snapshots, original design provenance, unrelated implementation work and all unaffected owners. No new standalone completion report is needed. Summarize the published outcome and actual checks in Chinese, link the development handoff, and state remaining implementation/acceptance work. Commit or push only after a separate applicable user instruction.

## 10. Begin

Execute sections 1–5 now: read and verify the current state, establish the single register and necessary one-time entry navigation/status, then provide the concise orientation and Q1–Q10. After each answer, follow sections 6–7 before advancing. Follow sections 8–9 for the eventual explicitly authorized closure.
