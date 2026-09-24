# SL-03.M2 — Protected Semantic Invocation Development Handoff

## Current development transfer — 2026-09-24.S2M1S1-r1

**Classification:** First production protected-invocation implementation. This addendum controls the replaced source scope; any older body below is a historical snapshot. [Owning plan](../../plans/slices/sl-03-invocation-requirements.md) · [Accepted supplement](../../design/contract/sl-02-m1-supplement-grill.md) · [Current scope/evidence](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

**Consumed scope:** Existing 2026-09-24.S3M2-r1 eight Ready portions; CTX-016/PRO-013–014/EVO-027 business interface. Read the actual Contract bodies through [Contract Index](../../contracts/index.md); indexes/planned paths are not norms. Read Product/Architecture/Acceptance, AGENTS.md and maintained component guides before implementation. Old shared Profile/Evidence/Baseline authority, Knowledge-first Save, parallel Fits and mandatory current assistant apply are superseded only as recorded in those owners.

**Observed baseline:** HEAD `66e2bb8dfd081a44b3a28873d5b992805ce46d56`; backend runtime schema 5, migration head `d092ea64bf17_invocation_durability.py` after `a41d7e90c263`. Existing SL-02.M1 backend/frontend and M2 backend implement the old model. Runtime M1 is implemented; production SL-03.M2 and later consumers are not. Current documentation publication changes no product code, database, dependency or generated client. Recheck git status and preserve unrelated edits; historical test counts below are not rerun evidence.

**Backend delta:** Implement the already-reviewed protected Context/Tools/Budget/Gateway foundations and adoption proof. Register portrait as a separate typed business adapter/result validator, with complete admitted deterministic Evidence, one-request/no-repair policy and durable-response local recovery. Do not repurpose the EVO conformance exercise format or weaken existing outcome reasons.

**Frontend delta:** No standalone M2 UI is required by this supplement; SL-02 portrait consumes status through its owned API.

**Upstream and order:** Actual M1 runtime → M2 adoption/configuration/guarded invocation → SL-02 semantic portrait. Deterministic source Save proceeds independently.

**Data/API transition:** Q38/Q41 permits later explicit offline reset of the complete configured development DB/generated materials, including test Preferences/Entries/Runtime records, while preserving source/Git/configuration. Never reset on startup or during this documentary transfer. No legacy request adapter/data conversion/archive reader is required. Preserve published migration source history and post-transition immutable source/result/receipt histories. Coordinate changed backend schemas with generated clients; do not fabricate target availability from this handoff.

**Invocation integration gate:** Register and prove PRO-014’s own complete derivation-decision reconciliation, Runtime ending mapping, frozen deadline/local-recovery bounds and finite configuration values. Do not inherit conformance-only ending/grace policies. A ready document source is not proof this executable integration exists.

**Required proof and open blockers:** Production provider/model, finite input/output limits, SDK retry disablement, structured-output behavior and protected real invocation remain implementation/research proof. No dependencies installed/live call performed here. Do not mark M2 implemented or portrait complete from conformance-only success. This is required future evidence. Ready replacement Contracts do not establish runtime/browser/model acceptance; unrelated Pending future scopes remain blocked until their own consumer definitions and upstream capabilities are ready.

**Maintained verification entry:** [Backend guide](../../../backend/README.md), [frontend guide](../../../frontend/README.md), [Development](../../development.md), [UI system](../../ui/DESGIN.md). From repository root, inspect then use `UV_CACHE_DIR=/tmp/jobhunter-uv-cache ./scripts/check`, `npm --prefix frontend run api:generate`, `npm --prefix frontend run check` and `npm --prefix frontend run test:e2e` as consumed. Rendering requires the actual certified native/font environment; invocation requires its reviewed provider/configuration. For docs run `python3 scripts/check_contract_links.py` and `git diff --check`. Report executed commands and unexecuted scope; backend tests never substitute browser acceptance.

## Historical handoff snapshot

> English is authoritative. Transfer checkpoint: 2026-09-24. The consumed M2 normative scope is **Ready** after accepted CG06-Q1–Q219 and scoped closure review. This transfers published Contracts and inspected source facts, not implemented capability. Executable model/configuration, dependency adoption and required tests remain gates before integration acceptance.

[Milestone](../../plans/slices/sl-03-invocation-requirements.md#sl-03m2-protected-semantic-invocation-and-evidence) · [Scope/decision mapping](../../progress/traceability.md#66-sl-03m2-reviewed-scope-and-interface-evidence) · [Decision register](../../design/contract/sl-03-m2-grill.md#cg06-pub) · [Contract index](../../contracts/index.md)

## 1. Authorization and first action

The user accepted CG06-Q1–Q219 with their recorded amendments and explicitly authorized normative owner writeback with “同意授权”. That authorizes this documentation/review work, not feature implementation, dependency installation, live API calls, deployment, migration of user data, commit or push. A subsequent development request establishes its own actual scope.

Q217–Q219 are accepted with their scope/ownership/recovery amendments. EVO-022–026 and EXR-057 now close the exercise's typed input, completion, rejection and bounded local recovery. Do not re-ask the same publication authorization or inherit M1 proof-consumer completion/concurrency/grace values.

Eight consumed portions, including the concrete exercise agreement, are documentary Ready. Begin any authorized implementation from the current source, precise consumed interfaces and outstanding adoption gates. Readiness is not dependency adoption, a passing live composition test, a model-quality promise or milestone completion.

## 2. Required authoritative reading

Read [AGENTS.md](../../../AGENTS.md), [documentation index](../../index.md), [Progress](../../progress.md), the linked scope ledger, [Implementation Plan](../../plans/implementation-plan.md), owning milestone, [Development](../../development.md), [repository organization](../repository-structure.md), [technology stack](../technology-stack.md) and [backend instructions](../../../backend/README.md). Inspect current manifest/lock/source rather than using this checkpoint as a version pin.

Consume Architecture 9–13/15, Product 9/11 and Acceptance 8–10/12 together with [Acceptance 9.4](../../acceptance.md#94-sl-03m2-protected-invocation-conformance), [Eval acceptance](../../acceptance/evaluation.md#25-sl-03m2-infrastructure-proof), [Eval procedure](../evaluation.md) and the applicable [Harness provenance](../../design/harness/README.md). The original [Grill handoff](contract_grill/sl-03-m2-contract-grill-handoff.md) remains historical session guidance; this transfer does not rewrite it.

| Actual consumed Contract | Scope and limits |
| --- | --- |
| [Common](../../contracts/common.md#com-049) | COM-049 and referenced preserved UUID/UTC/hash/Unicode/COM-045 encoding/generation rules; no speculative HTTP envelope |
| [Execution Runtime](../../contracts/agent/execution-runtime.md#exr-035) | EXR-035–057 plus preserved EXR-001–034: start/Skill/purpose binding, capacity/admission, one-request Gateway, DeepSeek response and recovery boundaries |
| [Context](../../contracts/agent/context.md) | CTX-001–015: immutable initial scope versus exact actual Frame, provenance, capacity and historical reads; CTX-003 consumes EVO-022's exact exercise input |
| [Tools](../../contracts/agent/tools.md) | TOL-001–014: static typed registry, model-origin locator, one request/Invocation, exact-target read projection, completion/result distinction and action-specific replay |
| [Budget](../../contracts/foundation/budget.md) | BUD-001–025: foreground allocation, required Run ceilings, exact CNY/checked counters, atomic reservation, absolute metering and unresolved exposure |
| [Storage](../../contracts/foundation/storage.md#sto-046) | STO-046–053 plus referenced preserved Storage/Workspace clauses: atomic associations, exact retained payloads, migration and integrity |
| [Eval](../../contracts/evaluation/evaluation-observability.md#evo-008) | EVO-008–026 plus preserved EVO-001–007: isolated real path, retained evidence, evaluator resources, allowed observations and proof; EVO-022–026 supply the concrete exercise protocol |

## 3. Reverified source checkpoint and evidence limits

Inspected HEAD: **2c5c69687ea7d43ddb79b5c89828bf54c159440b**, `docs(runtime): record invocation operations and verification evidence`. The worktree contains this M2 document/checker work plus concurrent frontend, API, SL-02 plan/Grill, technology/design-system and Progress changes. Preserve all unrelated changes and recheck status before editing or committing. No commit/push was requested for this publication.

M1 is now implemented and recorded as verified, not the uncommitted state described by the initial M2 Grill snapshot. [M1 executed evidence](../../progress/traceability.md#invocation-backend-evidence) records 416 passing tests, Ruff/format/strict Pyright and actual subprocess/SQLite proof. These are inherited recorded results; publication did not rerun that suite. The internal [M1 API guide](../../api/sl-03-m1.md) is a derived integration reference, not a replacement Contract.

| Reusable component | Actual path / limitation |
| --- | --- |
| Run/Invocation models and controlled format | `backend/src/jobhunter/domain/invocation/models.py`, `format.py`; retain M1 identity, positive payload length, immutable bytes and format rules |
| Runtime authority, intent, response and startup | `backend/src/jobhunter/agent/harness/runtime.py`; original live-path ownership and no-replay predicates must survive extension |
| Consumer protocols and controlled read | `backend/src/jobhunter/application/invocation/ports.py`, `controlled.py`; existing MODEL proof expects two responses/concurrency up to two, while its read consumer treats one Tool result as whole-Run completion |
| Composition | `backend/src/jobhunter/bootstrap/invocation.py`; current read-recovery path is coupled to ControlledConsumer and needs deliberate interface refactoring with regression proof, not changed historical key meaning |
| Persistence | `backend/src/jobhunter/infrastructure/persistence/sqlalchemy/models/invocation.py`, corresponding repositories/UoW; preserve short owned transactions, physical Workspace lock and unknown-commit rules |
| Migration | Current source head `d092ea64bf17_invocation_durability.py` follows `a41d7e90c263`; runtime serves schema 5. Select the next revision from the actual implementation-time head, never edit published migrations or assume a fixed new schema number |

At inspection, `pyproject.toml` requires Python >=3.12,<3.13 and has HTTPX 0.28.1 as a development dependency. No LangGraph, Langfuse or model SDK dependency was present. Using HTTPX in production requires deliberate dependency placement/lock reconciliation during implementation; publication did not install or move it. No user database was opened/migrated, service deployed or live model invoked.

## 4. Concrete scope and implementation ownership

The production chain is **ModelInvocationRuntime → ModelGateway → DeepSeekAdapter → official DeepSeek Chat Completions**. Semantic role/schema mapping occurs before Frame freeze. Afterward Gateway/transport may serialize/authenticate without altering model-visible meaning. Use one production adapter, no arbitrary base_url, provider plugin platform, hidden retry/fallback or automatic model change.

Static Skill registration declares typed bounded input, semantic structure and allowed actions. It does not maintain a parallel resource balance. Semantic-start uses the caller's stable start_request_id and original complete request; history confirmation precedes fresh permissions/source/configuration/Budget admission. Initial Run/Package/binding publication and later Frame/reservation/intent publication are separate atomic boundaries. Neither grants a portable replay token.

Package declares initial allowed scope. Frame retains exact Provider-effective semantic input and attached provenance. Use COM-045 for the owned closed Package/Frame formats; the DeepSeek terminal response has its separately specified fixed-order JSON encoding. Do not conflate either with network-byte hashing. Historical reads and current permission to send content again remain separate. Candidates before PREPARED are discardable local work.

Budget owns opaque operation_id allocations, not an Operation business aggregate. Optional Operation call/token/CNY dimensions intersect required finite Run call/token/deadline ceilings. No Run money wallet or shared Tool-count wallet is delivered. One estimator evaluation supplies Context and Budget; their margins/pricing assumptions remain independently owned. Preserve exact usage, pre-rounding calculated cost, conservative ledger debit, unresolved dimensions and overflow obstruction across restart. Usage remains outside response equality and may settle after Run ending.

ToolInvocationRuntime executes one Skill-selected model request from a durable same-Run response. The exact historical read target may belong to a different fixture Run and must match Package scope. TOL-011's model-visible `source_sha256`/`source_byte_length` are a projection of existing `result_sha256`/`result_byte_length`, not a migration or semantic rename. Completion evidence remains true when result encoding/admission fails.

The minimal conformance Skill proves MODEL → TOOL → MODEL over those actual components. EVO-023 requires the actual one-Tool/two-MODEL evidence and exact final JSON; model behavioral failure is a Trial semantic failure, not proof of broken infrastructure. EVO-024/EXR-057 retain owner-defined failure causes. EVO-025 permits only bounded existing-evidence local recovery from the original deadline, with consumer-bound grace; expiry grants no new recovery qualification and erases no completed facts. It is not a permanent product Skill, mandatory universal Agent loop, two-call rule for all Skills or response-browser capability. No M3 parsing, generic validation/repair binding, interactive compression, Memory or generic semantic Judge is added.

## 5. Adoption gates before executable integration

| Gate | Required closure |
| --- | --- |
| Controlled DeepSeek profile | Exact supported model/mode/parameters, stream setting, output cap, limits, estimator applicability, immutable price basis and response-format binding. Verify actual documented wire/layout/error behavior and finite parser/receive bounds; model strings/fingerprint are observations, not immutable weight identity |
| HTTP transport | First implementation uses existing HTTPX without a model SDK. Realize controlled routing, TLS validation, no redirects/environment-route inheritance/hidden retry/fallback, deadline/cancellation and one-request counting. Library-specific settings are implementation choices under stable invariants |
| LangGraph | Research candidate 1.2.12 / release short commit 49cce0c, MIT, is not a pin. Use a small static graph of production Harness calls. Prove no node replay/retry/checkpointer path sends another model request; `checkpointer=False` can prevent inherited checkpoints where chosen. Node trace filtering alone does not cover root/child traces |
| Langfuse SDK/server | Research candidate SDK v4.15.4 / 6c3842a and server v4.42.0 are not selected deployments. Verify exact license scope/resolved transitive dependencies. Stock callbacks can expose raw data and create extra generations; late masking alone cannot establish pre-SDK admission |
| CNY / counting | Native Langfuse cost fields are USD/float; retain exact CNY/certainty in admitted representations, prevent misleading inferred-cost authority and duplicate generations. Ended-span update is not assumed; permitted correlated non-generation late-accounting events retain original Invocation identity |
| Bounded export | Prove actual queue/retry/flush/shutdown/atexit behavior under loss and blockage; source inspection did not establish a total shutdown bound. No outbox or exactly-once obligation; export cannot block canonical transactions or alter business outcomes |
| Fixtures/evaluators | First representation may be JSON bundles with a controlled hydrator; format/version and deterministic reconstruction are the stable semantics. Replay never falls back to live. Retain actual post-state; independent evaluator attempts/resources do not debit the tested Agent. No mandatory quality judge |

The [CG06-R1–R8 research](../../design/contract/sl-03-m2-grill.md#cg06-r7) contains source identities and limitations. Recheck current official source when adopting temporally changing protocol/configuration. Current publication authorizes neither live credentials use nor deployment. A live Trial requires its explicitly allowed configuration and applicable user authorization.

## 6. Development order once its consumed scope is ready

1. Implement the accepted exercise agreement against its exact producer/consumer input/result/error/deadline mappings. Choose executable configuration and dependency versions only after applicable source/license research.
2. Define owned typed domain representations and internal Application ports, including semantic-start, immutable bindings/Package/Frame, action association and Budget evidence. Preserve M1 consumer contracts and avoid public HTTP scaffolding without a consumer.
3. Add forward persistence migration and repositories/UoW with constraints and short transactions. Prove earlier data/receipts preservation and no fictitious backfill. Integrate unknown-commit confirmation before effects.
4. Implement deterministic Context/Provider semantic mapping, one shared estimator basis, static action registry/projection and authoritative action/result admission. Prove exact bytes/provenance with golden fixtures.
5. Integrate exclusive capacity qualification, reservation/intent atomicity, one-request transport and independently admitted usage. Extend recovery through consumer interfaces without changing existing controlled consumer meaning.
6. Exercise the actual path with isolated fixtures/replay and retained evidence. Add the minimal LangGraph integration and separately verified admitted observability/evaluator infrastructure; implement export only within its reviewed bounds.
7. Execute scoped fault/concurrency/conformance and maintained regressions, then separately authorized live/SDK evidence where required. Update requirement-to-code/test mappings and actual readiness/completion. A passing isolated path is not semantic product quality or parent-Slice completion.

## 7. Required proof and maintained commands

Use test-first development and the maintained backend instructions. Required cases include same-ID start race/lost acknowledgement, historical confirmation after revoked fresh permission, one active Invocation, last-unit resource/capacity contention, exact source mismatch, protected capacity/revocation, current stream terminal variants, no hidden retry, actual byte/hash corruption, complete oversize versus interrupted unknown, action completion versus rejected projection, late usage, unknown exposure, overflow, crash recovery and original-result re-evaluation. EVO-019–021/026 and Acceptance 9.4 own the full obligations.

```sh
uv sync --locked
./scripts/check
```

Run from repository root during authorized development. Use temporary Workspaces, not user data; select a writable UV_CACHE_DIR if required. The maintained command includes Ruff, formatting, strict Pyright, pytest with actual loopback/subprocess cases, Contract checking and whitespace. Network/socket restrictions are not grounds for silently skipping required tests. Preserve M1 regressions and prior migration history.

For this document/checker publication, use `python3 scripts/check_contract_links.py`, scoped Ruff/format/Pyright and isolated negative fixtures for the modified checker; the actual final results are in the [publication verification record](../../design/contract/sl-03-m2-grill.md#cg06-pub). Retain that checker until all Contract Grills finish. Do not claim backend/browser/live/SDK proof from these checks.
