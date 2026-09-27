# Repository Instructions

Applies to code, tests, Eval and documentation. This file defines required reading and working discipline; current behavior, plans, status and tool commands belong to their linked owners.

## Start each task

1. Read the [documentation index](docs/index.md), [current Progress](docs/progress.md) and relevant [readiness/evidence records](docs/progress/traceability.md). Check recorded claims against the actual checkout when implementation is involved.
2. For milestone work, read the [global plan](docs/plans/implementation-plan.md), owning Slice and latest applicable transfer in `docs/development/handoff/`. Read an existing applicable handoff automatically; historical snapshots do not override current owners.
3. Read the relevant [Product](docs/spec.md), [Architecture](docs/architecture.md), [Acceptance](docs/acceptance.md) and actual normative scope reached through [Contract Index](docs/contracts/index.md), including necessary shared interfaces. Navigation, planned catalogs and API examples are not normative Contracts.
4. Follow [Development](docs/development.md), [repository organization](docs/development/repository-structure.md) and [technology selection](docs/development/technology-stack.md). Read only relevant scope; a focused task does not require every Slice or historical record.

## Additional reading by task

| Task | Required inputs |
| --- | --- |
| Frontend | [Design system](docs/ui/DESGIN.md), relevant [API guide](docs/development/api/README.md), consumed Contracts, frontend README and actual manifest/lock/configuration |
| Backend | Backend README, actual manifest/lock/configuration, affected code and Contracts; versioned schema/migration history when changing durable storage |
| Eval | [Evaluation criteria](docs/evaluation.md#2-evaluation-acceptance-criteria) and [workflow](docs/evaluation.md#3-evaluation-workflow), plus the capability's Acceptance and consumed Contracts |
| Grill or decision interpretation | Relevant [Grill record](docs/.grill/README.md) and its session transfer; use `rg --hidden` to include `.grill/` |

Use maintained component instructions for runnable commands and installed versions. Target layouts and technology lists do not authorize empty scaffolding or installing every planned dependency.

## Work and verification

- Respect authority by responsibility. Resolve conflicts through approved decisions and scoped supersession, not timestamps or implementation convenience. Do not restore rejected/withdrawn mechanisms or turn unresolved semantics into code, DTOs, UI or fixtures; resolve affected scope before dependent work.
- Begin implementation only when its consumed normative scope, necessary interfaces, research and upstream capabilities are ready. File/family or parent-Slice completion is not the readiness unit.
- Follow test-first development and required Acceptance. Preserve Domain/Application ownership; generated clients, mocks and SDK defaults cannot override owned semantics. Reconcile exposed interface changes with Contracts, actual API/schema, integration guidance and consumers. Do not hand-edit generated output into a competing contract or rewrite published migrations to represent new schemas.
- Run applicable checks from current component tooling. Report actual commands, outcomes and unexecuted scope; do not infer full acceptance from a passing subset.
- For documentation/source/interface changes, apply both [verification seams](docs/development.md#92-two-separate-verification-seams): Decision-to-Document Traceability and Cross-Document Semantic Consistency. Link checks alone do not prove semantic agreement.
- Update actual status and evidence under [Progress recording rules](docs/progress/recording-rules.md). Follow [documentation maintenance](docs/development/README.md#documentation-maintenance): maintain existing owners; create handoffs only for real transfers, not routine completion reports.
- Preserve unrelated working-tree changes and retained historical evidence. Do not reconstruct deleted records as approved decisions. Formal documentation is English; UI language follows the design system.
- When committing is requested, follow [commit conventions](docs/development.md#31-git-commit-message-format): `<type>(<scope>): <subject>`, with scope optional and `*` permitted for multiple scopes.

Keep this entry stable. Maintain milestone details, implementation results, readiness, versions and commands in their owning documents; update this file when routing or repository-wide discipline changes.
