# SL-03.M1 Development Handoff — Invocation Durability and Recovery Foundation

> English is authoritative. Transfer revision: **2026-09-23.S3M1-r1**, following accepted CG05-Q1–Q130 and explicit user authorization for closure review, necessary writeback and normative publication. Contract readiness is separate from implementation and executed acceptance. This handoff transfers a real backend task; it does not authorize a production model integration.

[Milestone plan](../../plans/slices/sl-03-invocation-requirements.md#sl-03m1-invocation-durability-and-recovery-foundation) · [Review/evidence](../../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) · [Decision register](../../design/contract/sl-03-m1-grill.md#cg05-pub) · [Contract Index](../../contracts/index.md)

## 1. Consumed scope and required reading

Implement the internal Run/Invocation durability and recovery foundation in the repository's existing Domain, Application, persistence and bootstrap layers. The minimum AgentRun is execution control, not a universal business lifecycle. Canonical business writes remain with their consumers. No frontend or new public HTTP API is part of this milestone.

| Definition owner | Consumed scope |
| --- | --- |
| [Execution Runtime](../../contracts/agent/execution-runtime.md) | EXR-001–034: Run/Invocation shapes; owner/grant/ending/deadline; dispatch/response; consumer/Tool seams; internal operation results and uncertainty |
| [Common](../../contracts/common.md#com-047) | COM-047–048 plus applicable naming/scalars COM-001–024, UUIDv4 COM-027 and SHA-256 COM-032; no inherited Entry-specific timestamp ordering or HTTP mapping by accident |
| [Storage](../../contracts/foundation/storage.md#sto-040) | STO-040–045 and applicable existing layout/physical ownership, explicit migration, UoW/atomicity and honest transaction-outcome rules; prior consumer receipts and Materials files retain their own scopes |
| [Workspace](../../contracts/foundation/workspace.md) | Existing local physical ownership/access and startup applicability; no new Workspace field/configuration surface |
| [Deterministic evidence](../../contracts/evaluation/evaluation-observability.md) | EVO-001–007, required future actual-component fault/concurrency proof |

Read AGENTS.md, [documentation index](../../index.md), [Progress](../../progress.md), [Development](../../development.md), [repository organization](../repository-structure.md), [technology stack](../technology-stack.md), [backend README](../../../backend/README.md), current manifest/lock and relevant code. Read [Architecture §12](../../architecture.md#12-durable-execution-and-recovery), [Storage responsibilities](../../architecture.md#13-storage-retention-and-audit), [Acceptance §9.2](../../acceptance.md#92-crash-and-cancellation-boundaries), [Recovery provenance](../../design/harness/recovery.md) and the effective CG05 supersessions when interpretation matters.

## 2. Reverified source checkpoint

Read-only source inspection on **2026-09-23**, HEAD **1277e2af7180f9765c0542c92c1fb4d1ffb44800** (`feat(materials): add durable resume rendering and artifact delivery`). Candidate Authority was committed by 2cff572. The older Grill entry at 362ff36/schema 3 remains a historical snapshot, not the current development baseline.

- [Store](../../../backend/src/jobhunter/infrastructure/persistence/sqlalchemy/uow/store.py) targets schema **4**. The source migration chain is b720a94fd381 → cd891047a2e6 → ef03c92ba671 → [a41d7e90c263](../../../backend/alembic/versions/a41d7e90c263_materials.py). Ordinary startup requires explicit upgrade for recognized historical schemas; no actual user database was inspected or migrated here.
- [Composition](../../../backend/src/jobhunter/bootstrap/container.py) supplies Entry, Preferences, CandidateAuthority and Materials Runner/Coordinator. Materials' attempts/queue/renderer subprocess/fencing are distinct consumer semantics, not an existing AgentRun implementation.
- Source/test inventories found no AgentRun, Model/ToolInvocationRuntime, Gateway/provider adapter or invocation startup reconciliation. Manifest/lock contain no provider SDK, LangGraph or Langfuse dependency. Do not assume target technology is installed or useful for M1.
- Existing physical-directory lock, explicit SQLite BEGIN/BEGIN IMMEDIATE, UoW and transaction-outcome handling are reusable within their real scope. Inspect [transaction outcome tests](../../../backend/tests/conformance/recovery/test_transaction_outcomes.py) and [Materials storage tests](../../../backend/tests/integration/persistence/test_material_storage.py), without treating them as model-dispatch proof.
- [Inherited backend evidence](../../progress/traceability.md#materials-backend-evidence) records 330 passing tests and real PDF/PNG checks on 2026-09-23. This publication did not rerun those tests. M1 Runtime implementation and runtime acceptance remain **Not started / Not executed**.

Recheck git status, actual head, installed tools and migration head before implementation. Preserve unrelated user changes, including untracked files. Add a forward migration from the then-current head; schema 5 is only an expectation from today's schema 4, never a normative constant. Preserve existing data/refs/receipts and published migrations. Do not backfill historical Run/Invocation objects or migrate a user's real database as part of development checks.

## 3. Implementation sequence and engineering gates

1. Establish typed Domain shapes and internal Application ports from EXR-003/012/017/020/024/029/033. Instantiate a controlled versioned response format with deterministic serialization and one typed pure exact-version local-read proof consumer. Its completion criteria, exact inputs, permission/dependency outcomes, recovery bounds and denial mappings must close before execution; do not invent a general business DTO.
2. Add explicit forward migration, persistence mappings/repositories and transactional predicates using temporary stores. Implement exact byte preservation, metadata/reference integrity, all-OPEN-Run payload protection and terminal retention. M1 supplies no purge, Pin service or retention enum.
3. Implement current-instance grants, revocation, run-wide cancellation, write-once deadlines and ownerless ending coordination. Generations increment on grants only. Exercise races/uncertain commits before dependent dispatch code; do not treat matching persisted authority as proof that a particular live path won.
4. Implement atomic validated descriptor/intent publication and the unique non-transferable live sending context. Separate original-path acknowledgement reconciliation from crash/takeover no-replay. Controlled adapter calls must be countable and free of hidden retry/fallback.
5. Implement complete-response publication, actual-byte integrity and immutable result confirmation. Preserve the existing-response-first read-only branch, Invocation-derived format key and original dispatch-generation/path restriction for first publication. Capture finite response size before dispatch; distinguish complete oversized output from an interrupted stream.
6. Implement startup fencing and consumer completion/admission/local-resume protocol, scoped dependency failure convergence, no-Invocation startup handling and permitted bounded postdeadline local recovery. Confirm whole-Run completion, not merely one result. Instantiate controlled same-Invocation pure-read recovery without Ensure, parsing, remote effects or business writes.
7. Execute EVO-001–007 against actual components with controlled adapters, temporary databases, deterministic clocks/faults and process boundaries where needed; then maintained prior-consumer regression checks. Record exact code/test mappings, actual commands/results and unresolved scope.

Engineering preparation must confirm actual SQLite commit/rollback uncertainty and transaction serialization, process/Workspace ownership, live-path arbitration, clock behavior and finite resource limits. Pin only dependencies actually needed by this foundation. Do not substitute framework checkpointing for owned recovery/fencing. Physical interruption is best effort when supported; logical publication fencing is mandatory. Production SDK serialization/hidden-retry verification and complete protected call admission belong to M2, not to this controlled proof.

## 4. Verification and reporting

Use test-first delivery under Development. [Backend README](../../../backend/README.md) owns current installation/check commands; inspect it and current scripts rather than assuming this snapshot is permanent. The maintained root command is `UV_CACHE_DIR=/tmp/jobhunter-uv-cache ./scripts/check`, covering lint/format, Pyright, pytest, Contract links and whitespace. Dependency setup (`uv sync --locked`) is engineering preparation when actually required, not something executed by this handoff.

Required proof includes exact serialization golden bytes; dispatch/response crash boundaries and call counts; stale/competing owner races; response-first idempotent confirmation after ending; corruption versus unavailable storage; failed terminal-write uncertainty; bounded deadline recovery without new remote work; complete versus interrupted oversize; cancellation/sibling fencing; safe controlled Tool recovery; forward migration preservation and no invented history. Existing tests are regression evidence only until these new Runtime cases execute.

Update Progress and requirement-to-code/test traceability with actual backend evidence. No frontend, semantic quality Eval, parser/collector/sender capability or parent-Slice completion follows from a passing foundation suite. Do not mark M2 interfaces Ready without their own consumed review.

## 5. Remaining scope and next consumers

Production Provider formats/SDKs, full Skill/Context/Tool/Budget admission, late usage, semantic Eval and telemetry are M2. RequirementParse/Ensure is M3. Run-level Retry/lineage, payload purge/disposition and concrete business-consumer recovery bounds/denial mappings wait for actual consumers. Collector/Executor reuse requires an explicit applicable interface agreement; Save, Materials, platform consent/risk and business outcomes keep their owners.

This publication created no implementation, installed no dependency, executed no migration or Runtime acceptance suite, and made no Git commit. The existing `scripts/check_contract_links.py` remains temporarily in the repository under the user's express instruction until all Contract Grills finish; new authoring helpers used for this closure stayed in temporary storage.
