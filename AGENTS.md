# Repository Instructions

These instructions apply to frontend, backend, tests, Eval and documentation work throughout this repository. They define required reading and route agents to the existing authoritative documents; they do not introduce new product behavior or replace those documents.

## Required reading before development

Before editing frontend or backend code, read the following current documents. Read the sections relevant to the selected capability and its shared interfaces; a focused task does not require reading every Slice or every historical Grill record.

1. [Documentation index](docs/index.md) and the relevant directory guides: locate current owners and file paths.
2. [Progress](docs/progress.md) and the relevant [traceability/readiness records](docs/progress/traceability.md): establish the recorded state, consumed Contract scope, available upstream capabilities and remaining proof. Compare these records with actual code and tests; do not mistake uncommitted code or a historical handoff for verified completion.
3. [Global Implementation Plan](docs/plans/implementation-plan.md) and the owning plan from the [Slice index](docs/plans/slices/README.md): identify the milestone, scope/exclusions, required capabilities, reused infrastructure, required Contracts and completion conditions.
4. [Development](docs/development.md), [repository organization](docs/development/repository-structure.md) and [technology stack](docs/development/technology-stack.md): follow delivery discipline, required layers/file placement, test naming and tool-adoption rules. Actual manifests, locks and maintained component instructions establish installed versions and runnable commands.
5. Relevant [Product](docs/spec.md), [Architecture](docs/architecture.md) and [Acceptance](docs/acceptance.md) sections: establish intended behavior, architectural owners/invariants and required positive, negative, concurrency, failure, permission and recovery proof.
6. [Contract Index](docs/contracts/index.md) and the actual normative bodies/clauses consumed by the change. Follow their referenced shared scopes and both sides of necessary interfaces. Use [Contract Structure](docs/contracts/structure.md) to locate planned responsibilities, not as a substitute for normative definitions.
7. The latest applicable milestone handoff under `docs/development/handoff/`, when one exists. Read it automatically without asking for confirmation, then check its snapshot against current owners. Older authoring handoffs under `.scratch/` are contextual inputs, not the default implementation baseline.

Existing milestone entry points include the [SL-01.M1 handoff](docs/development/handoff/sl-01-m1-handoff.md) and [SL-01.M2 handoff](docs/development/handoff/sl-01-m2-handoff.md). Select the handoff for the actual task rather than assuming either remains the latest for all work.

## Authority and conflict handling

| Subject | Definition owner |
| --- | --- |
| Product scope, prerequisites and behavior | `docs/spec.md` |
| Logical responsibilities, permissions, transactions, concurrency and recovery | `docs/architecture.md` |
| Detailed normative definitions and requirement IDs | Reviewed scope in actual `docs/contracts/**/*.md` bodies |
| Slice/milestone scope, dependencies and completion conditions | Global Implementation Plan and the owning Slice plan |
| Required product/system proof | `docs/acceptance.md`, with specialized Eval criteria in `docs/acceptance/evaluation.md` |
| Delivery discipline, code organization and technology selection | `docs/development.md` and its relevant specialized guides |
| Shared frontend visual and interaction system | `docs/ui/DESGIN.md`, within Product/Contract/Acceptance boundaries |
| Status/evidence recording rules | `docs/progress/README.md` |
| Actual recorded readiness, implementation and verification | `docs/progress.md` and `docs/progress/traceability.md` |

Authority is divided by responsibility; there is no blanket rule that an implementation, API example, design screen or newer timestamp overrides every other document. [API guides](docs/api/README.md) are derived integration references. Generated OpenAPI/client code, mocks and screenshots cannot introduce business behavior, fields, permissions or success semantics contrary to the relevant normative owners. Contract README/index/structure files provide navigation or planning, not normative Contract bodies.

Resolve discrepancies using current approved decisions and their scoped writeback. Read the relevant [design provenance](docs/design/README.md) and Contract Grill records when interpretation or supersession matters. Later accepted corrections replace the clauses they address, even if an earlier record still says ACCEPTED. Do not restore REJECTED/SUPERSEDED mechanisms or promote Contract Design Inventory examples into norms. Preserve original Grill history and historical handoff evidence.

If necessary semantics remain unresolved, identify the conflicting or missing clauses and their owner. Do not silently decide them in code, DTOs, fixtures or UI; resolve the affected scope before dependent implementation. A missing detail for one scope does not block unrelated ready work or require reopening the entire Architecture Grill.

## Frontend-specific required reading

In addition to the common reading above:

- Read the [design system](docs/ui/DESGIN.md) before creating or changing pages, components or interaction states. The current filename is **`DESGIN.md`**; use that existing path rather than assuming `DESIGN.md` exists. Follow its shared shell, controls, visual language, UI language and state patterns. Approved page designs are visual references; generated design code is optional implementation input.
- Read the relevant [API integration guide](docs/api/README.md), such as [M1 Manual Application Entries](docs/api/sl-01-m1.md) or [M2 Preferences](docs/api/sl-01-m2.md), together with its normative Contracts. Check actual backend availability and generated OpenAPI before wiring a client. A planned or documented operation is not automatically an available integration.
- For ManualApplicationEntry work, read [its Contract](docs/contracts/jobs/manual-application-entries.md) plus applicable [Common](docs/contracts/common.md) and [Workspace](docs/contracts/foundation/workspace.md) clauses. For Preferences, read [its Contract](docs/contracts/candidate/preferences.md) and the shared scopes it references. Resolve other capabilities through Contract Index instead of guessing paths or schemas.
- Read [frontend/package.json](frontend/package.json), the current frontend lock/configuration, and a frontend README when available for real tools and commands. Use the technology-stack and repository-organization guides for intended choices and placement; do not install the entire target stack or scaffold every planned feature.

Implement the client obligations actually specified by Contracts, including validation, exact value handling, revisions, idempotency, uncertain outcomes and safe browser handoff where applicable. Client validation, cached data, optimistic UI and successful navigation do not establish a canonical commit or application success. Keep UI-only state separate from server-state authority. Follow the generated-client workflow; reconcile generation issues with the owned schema rather than hand-editing generated output into a competing contract.

## Backend-specific required reading

In addition to the common reading above:

- Read [backend/README.md](backend/README.md) for maintained installation, configuration, startup, migration and checking instructions. Inspect the actual backend manifest, lock and affected implementation before choosing commands or extending shared components.
- Read the complete consumed Domain/Application/HTTP scope in the applicable normative Contracts, including relevant [Common](docs/contracts/common.md), [Workspace](docs/contracts/foundation/workspace.md) and [Storage](docs/contracts/foundation/storage.md) clauses. Read the current API guide as a consumer reference when changing an exposed interface.
- Follow Architecture and repository organization for Domain, Application, persistence, API and bootstrap responsibilities. Transport validation and ORM representations do not replace Domain rules or move transaction/authorization ownership into adapters.
- For changes to schema, startup or durable writes, inspect the actual versioned schema and migration history alongside Storage requirements. Follow the documented migration entry point and preservation requirements; do not rewrite a published historical revision to represent a new schema or silently migrate user data as part of unrelated work.
- For Agent/Harness, Context, budget, recovery, Tools, Memory or platform automation, also read the corresponding Architecture sections, consumed Contracts and relevant [Harness design records](docs/design/harness/README.md). Reuse only applicable verified components; framework/SDK defaults cannot bypass owned admission, consent or recovery rules.

When an HTTP boundary changes, reconcile its normative scope, actual routes/DTOs, generated OpenAPI, the affected API guide and frontend consumers. Preserve existing consumers' semantics or record and reconcile an explicitly approved change; test convenience does not authorize a protocol change.

## Verification, status and handoff

- Start development only when the milestone's actually consumed normative scope, necessary interfaces, research and upstream capabilities are ready under Development. Whole-file/family or parent-Slice completion is not a substitute for this scope-level check.
- Use the test-first workflow and applicable Acceptance scenarios. Run the checks documented by the current component tooling; report actual commands, outcomes and unexecuted scope. Backend checks do not establish browser/UI acceptance, and a passing mock UI does not establish backend integration.
- For work requiring Agent Eval, use the [Eval index](docs/evaluation/README.md), [Eval acceptance](docs/acceptance/evaluation.md) and [Eval development procedure](docs/development/evaluation.md). Keep what evidence must prove separate from how it is produced; judges and telemetry do not own business success.
- For documentation/source/interface changes, apply both verification seams in [Development 9.2](docs/development.md#92-two-separate-verification-seams): **Decision-to-Document Traceability** and **Cross-Document Semantic Consistency**. Link checks alone do not establish semantic agreement.
- Update actual status and requirement-to-code/test evidence under [Progress recording rules](docs/progress/README.md). Record backend/frontend subsets, child milestones and parent remainder separately. Do not infer whole-milestone completion from file existence, ready Contracts or one delivered subset.
- Follow [Development guide maintenance rules](docs/development/README.md#documentation-maintenance): maintain the current owners and records, not daily logs or a new completion report for every task. Create or update a handoff only for a real cross-context transfer; preserve historical snapshots.
- Write formal documentation in English; product UI language follows the design system and applicable product decisions. Preserve unrelated working-tree changes. When a commit is requested, follow [Development 3.1](docs/development.md#31-git-commit-message-format): `<type>(<scope>): <subject>`, with optional scope and `*` permitted for multiple scopes.

Keep this file as a stable reading and workflow entry point. Update links when owners move; keep detailed rules, tool versions and volatile completion claims in their existing owning documents.
