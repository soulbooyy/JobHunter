# Target Technology Stack

> English is authoritative. This document records the user's planned frontend/backend technology choices. Selection does not establish installation, version compatibility, Contract readiness, implementation or passed acceptance. Introduce dependencies only for the milestone that actually needs them.

[Development guides](README.md) · [Development discipline](../development.md) · [Target repository organization](repository-structure.md) · [Global documentation index](../index.md)

## 1. Responsibility and decision provenance

This supporting Development document owns the target technology selection and its adoption boundaries. The target [repository organization](repository-structure.md) owns physical placement; [Implementation Plan](../plans/implementation-plan.md) and its [Slice plans](../plans/slices/README.md) own delivery scope, dependencies and completion. [Architecture](../architecture.md) retains logical ownership, runtime mechanisms and invariants. Technology choices implement those boundaries rather than redefining them.

[Product](../spec.md), [Contracts](../contracts/index.md) and [Acceptance](../acceptance.md) retain their behavior, normative-definition and proof responsibilities. [Progress](../progress.md) and the [matrix](../progress/traceability.md) record actual readiness, installed/implemented scope and verification evidence under [Progress recording rules](../progress/README.md). This file is not an environment inventory or a new formal-document category.

**Source:** The user's explicit technology-stack table and request to persist it. Python 3.12+, Pydantic v2, SQLAlchemy 2.x and Pyright strict retain the requested qualifiers. Zustand remains conditional. SQLite, LangGraph and self-hosted Langfuse also preserve existing Architecture 2.1/15 commitments. Other selections are later user engineering direction, not decisions retroactively attributed to the original Grill.

The table records target choices, not independently researched claims about current releases or verified SDK behavior. Exact resolved versions and relevant integration behavior must be checked at adoption under [Development research discipline](../development.md#4-research-and-integration-preparation). No dependencies, manifests, lockfiles, services or code are created by this documentation step.

## 2. Backend, Agent and engineering tools

| Layer | Target technology | Intended responsibility and boundary |
| --- | --- | --- |
| Backend language | Python 3.12+ | Backend, Agent and Eval implementation. Choose and verify the actual supported interpreter at bootstrap; the range is not a promise that every future Python version works. |
| Backend framework | FastAPI | HTTP API, request dependency wiring and SSE/streaming transport. Composition follows the bootstrap/Application boundaries; request handling does not own Domain rules or durable invocation outcomes. |
| Validation | Pydantic v2 | API DTOs, configuration and boundary validation. Domain invariants and authorization remain with their existing owners; transport schemas do not become canonical persistence models by implication. |
| ORM | SQLAlchemy 2.x | Persistence adapters, mappings, repositories and transaction integration. ORM entities do not replace Domain/Contract definitions. |
| Database | SQLite | Local-first canonical persistence and the existing short local authority-transaction boundary. This does not assign SQLite to every external service in the stack. |
| Migration | Alembic | Application schema migration tooling. Exact schema, revision layout, migration procedures and evolution requirements remain consumer-specific Contract/implementation work. |
| Python package tooling | uv | Dependency, virtual-environment and lock management. Resolve dependencies actually required by the selected milestone. |
| Agent orchestration | LangGraph | Skill execution and bounded workflow mechanics under Application/Harness ownership. It does not replace runtime admission, business commits or recovery authority. |
| LLM integration | Provider SDKs + JobHunter ModelGateway | OpenAI or other selected Provider transport adapters. ModelGateway remains behind the unique business ModelInvocationRuntime boundary; no direct Skill-to-SDK bypass. |
| Agent observability and Eval platform | Self-hosted Langfuse | Traces, datasets, experiments and evaluation facilities with thin JobHunter task/Scenario integration. Exports and judges do not determine canonical business success. |
| Browser automation | Playwright Python | Authorized BOSS collection and application-executor adapters, subject to shared safety and separate execution consent. Ordinary user URL navigation is not this automation capability. |
| HTTP client | httpx | Non-browser HTTP adapters behind the relevant owned boundaries. This choice grants no generic model HTTP Tool or permission to access a platform. |
| Backend tests | pytest | Unit, integration and conformance checks against actual consumed requirements. Tests remain subject to Acceptance's evidence boundaries. |
| Python lint and format | Ruff | Python linting and formatting. Exact configuration is established with the real project tooling. |
| Python type checking | Pyright strict | Strict static checking for the backend scope. Actual checking configuration and dependency/stub compatibility must be verified; strict mode is the selected target, not a passed check. |

## 3. Frontend and interaction verification

| Layer | Target technology | Intended responsibility and boundary |
| --- | --- | --- |
| Frontend | React + TypeScript | Product UI and typed client code. Backend authority, permissions and canonical facts remain server-owned. |
| Build tool | Vite | SPA development and build tooling. Actual runtime requirements and build configuration are verified when introduced. |
| UI primitives | shadcn/ui + Radix UI | Reusable UI primitives/components. Their use does not by itself prove accessibility or product interaction acceptance. |
| CSS | Tailwind CSS | Styling. Exact version and build integration remain to be pinned. |
| Server state | TanStack Query | API cache, queries, mutations and request state. Cached or optimistic values are not proof of a committed mutation or a second canonical store. |
| Forms | React Hook Form + Zod | Form state and client-side input validation. Server validation, current revisions and authorization remain required at the actual write boundary. |
| Routing | React Router | Page and contextual navigation. Routes do not create new product entries or Domain owners. |
| Local UI state | React state; Zustand only when needed | UI-only state such as local interaction choices. Introduce Zustand only for a demonstrated shared UI-state need; do not duplicate server-state ownership. |
| API client | OpenAPI-generated TypeScript client | Typed transport integration derived from the implemented API description and reconciled with normative Contracts. The generator/tool and regeneration workflow are not selected here. |
| Frontend unit/component tests | Vitest + Testing Library | Hooks, components and observable interaction behavior. Test assertions follow actual Acceptance obligations. |
| End-to-end tests | Playwright | User-visible behavior through the delivered application. E2E automation is distinct from the Python production browser adapter and grants no live recruiting-account access. |
| Frontend lint and format | ESLint + Prettier | TypeScript/React lint and formatting discipline. Concrete shared configuration is introduced with the consuming frontend scope. |
| Icons | Lucide React | UI icons for the selected component approach. Icon installation or rendering does not establish feature availability. |

## 4. Integration boundaries

### 4.1 Normative Contracts and generated interfaces

Normative Contract clauses determine the intended business and interface semantics. Backend API DTOs and routes implement the reviewed consumed scope; their OpenAPI description supplies the generated TypeScript transport client. Reconcile this chain whenever the interface changes:

`Reviewed Contract scope → API DTOs/routes → OpenAPI description → generated TypeScript client → consuming UI`

OpenAPI and generated types do not express every transaction, authorization, recovery or business invariant, and cannot substitute for Contract review or behavior checks. Pydantic and Zod serve their respective server/client boundaries; hand-written frontend validation cannot silently define a different business rule. Do not choose fields, enums, payloads or validation errors merely to satisfy a generator.

The exact generator, client transport, generation command, output path, checked-in artifact policy and drift checks remain implementation preparation for the first API consumer. Streaming framing, events, disconnect handling and reconnection semantics remain with their relevant Contracts; selecting FastAPI or a generated client does not settle those interfaces.

### 4.2 Controlled execution and external effects

LangGraph, Provider SDKs and ModelGateway remain subject to Architecture 9–12. Every actual business Provider request passes the owned invocation admission, accounting and durable-response boundary. Configure and verify transport retries/fallbacks so they cannot hide a second request or replay an unknown outcome. A graph checkpoint, HTTP response or stream fragment is not a canonical business receipt.

Playwright Python and httpx remain concrete adapters. Shared platform safety, exact execution authorization, action-specific recovery and honest unknown results continue to apply. The [current ManualApplicationEntry decision](../design/contract/sl-01-m1-grill.md#cg01-bc1) permits explicit ordinary browser navigation; it does not make Playwright automation a prerequisite of SL-01.M1.

Self-hosted Langfuse remains derived infrastructure under Architecture 15. Verify actual version/deployment requirements, callbacks, explicit observations, masking and independent judge configuration when adopted. Its own deployment dependencies are not chosen by the application's SQLite decision. Use the [Eval development guide](evaluation.md) and [Eval acceptance](../acceptance/evaluation.md) for procedure and proof respectively.

### 4.3 Persistence and migration organization

SQLAlchemy and Alembic are the selected target tools. Their adoption must preserve the existing local transaction, exact history and current-use boundaries; it does not create a legacy-system migration requirement. The two migration-related paths in [Repository organization 4.2](repository-structure.md#42-migration-paths-do-not-establish-two-sources-of-truth) still need concrete role allocation. Select one authoritative revision-script location when the first real migration needs it, and remove or justify the other target path without duplicating migration history.

## 5. Progressive adoption and unresolved setup

Apply the [incremental creation principles](repository-structure.md#5-incremental-creation-principles). A target-stack table is not an instruction to install everything, create empty packages, wire every provider or deploy the Eval platform at project bootstrap. Introduce the subset required by the current milestone's implementation and meaningful proof after its Contract/research/upstream prerequisites are satisfied.

For current SL-01.M1, assess only the local Workspace/ManualApplicationEntry application path, necessary persistence and API/UI integration, and its actual quality checks. Agent orchestration, model providers, Langfuse, automated recruiting-browser workflows and Zustand are not prerequisites merely because they appear in this document. Do not change milestone dependencies through a tooling installation shortcut.

| Still to resolve at the actual consumer | Existing target constraint |
| --- | --- |
| Exact dependency versions, supported runtimes and compatibility | Preserve Python 3.12+, Pydantic v2, SQLAlchemy 2.x and Pyright strict; pin and verify concrete versions with actual manifests/locks |
| Frontend package manager, Node.js version and lock policy | React/TypeScript/Vite are selected; the supplied table does not select these setup details |
| OpenAPI generator and regeneration/verification workflow | Generated TypeScript client is selected; normative Contracts and real behavior remain controlling |
| Database session/transaction wiring and Alembic revision/configuration locations | Preserve short authority transactions and one authoritative migration history; concrete schema/protocol detail follows the consuming Contracts |
| Specific Providers, SDK packages, models and settings | Provider SDKs adapt through ModelGateway and the existing runtime; no default model, quota or hidden retry policy is selected |
| Deployment topology, launch commands and service setup | The product is local-first; self-hosted Langfuse is selected, but no deployment has been installed or verified |
| Tool rules, scripts and automation integration | pytest/Ruff/Pyright strict and the named frontend tools are targets; runnable commands and CI configuration require actual implementation |

These are bounded setup or detailed-interface matters, not reasons to reopen all accepted architecture or finish every Contract family before development. Research any proposed replacement at its actual consumer, record the reason and reconcile affected owners before changing the selected stack. Default enablement, release thresholds and CI release consequences remain separately governed; tool selection does not decide them.

## 6. Maintenance and actual-state reporting

Keep the selection table here, physical paths in the repository-organization guide and concrete milestone scope in the Slice plans. Core Development links to these specialized guides; indexes remain navigation. Once real tooling exists, record exact dependencies/configuration in their actual manifests and locks, document verified commands in the relevant component guide, and update Progress/matrix with actual scope and evidence.

This initial writeback records all supplied technology choices and their existing-authority boundaries. It adds no dependency installation, lockfile, API schema, normative Contract, executable test, runtime behavior or implementation completion claim.
