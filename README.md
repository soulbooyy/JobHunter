# JobHunter

JobHunter is a single-user, local-first personal job-search workspace being designed to help users maintain career facts and resumes, find and assess opportunities, improve application materials, and track real application outcomes.

Its capabilities are independently accessible, each with its own prerequisites. A completed fit analysis is not required before resume advice or application preparation. See the [Product Specification](docs/spec.md) for the authoritative product scope.

## Project status

The SL-01.M1 backend is implemented with reviewed Contracts, a runnable local API and executable checks. Frontend/UI design, browser behavior and full milestone integration remain pending; M1 and SL-01 are Partial. Other planned product capabilities are not implemented. See the backend guide below for installation and run commands.

[Progress](docs/progress.md) records the current review and approval state, Contract readiness, implementation evidence, and next work. The [W7 review handoff](.scratch/w7-joint-review-handoff.md) records the reviewed baseline, corrections, and remaining detailed-design work. Document review does not establish implemented or verified product capabilities.

## Planned capabilities

- Maintain shared career facts and formal resumes, with reviewed imports and explicit saves.
- Maintain independent manual application entries; later browse/screen formal Jobs from authorized collection or refresh.
- Run independent Candidate Fit and Resume Fit analyses against reusable Job requirements.
- Discuss resume improvements with an Advisor and explicitly confirm formal changes.
- Prepare and inspect application materials, then separately authorize external execution.
- Track real application and interview events, including human-reported outcomes.
- Reuse permitted collaboration preferences through independently controlled Memory.

These describe the intended product, not currently available features.

## Documentation

Start at the [documentation index](docs/index.md) for task-oriented navigation and the full ownership map. The [documentation directory guide](docs/README.md) explains the layout. English is authoritative for project documentation.

| Document | Purpose |
| --- | --- |
| [Product Specification](docs/spec.md) | Product scope, behavior, prerequisites, and non-goals |
| [Architecture](docs/architecture.md) | Responsibilities, authority, mechanisms, and architectural boundaries |
| [Implementation Plan](docs/plans/implementation-plan.md) and [Slice plans](docs/plans/slices/README.md) | Macro progression and detailed milestone scope, dependencies, required Contract portions, and completion conditions |
| [Contracts overview](docs/contracts/README.md), [index](docs/contracts/index.md), and [structure](docs/contracts/structure.md) | Four reviewed M1 normative bodies plus planned later definitions |
| [Acceptance](docs/acceptance.md) | Unified product/system scenarios and required proof |
| [Development](docs/development.md) | Delivery sequence, research, test-first work, verification, handoffs, and commit conventions |
| [Progress](docs/progress.md) and [traceability matrix](docs/progress/traceability.md) | Actual status, decision provenance, milestone evidence, and scope readiness |
| [Evaluation documentation](docs/evaluation/README.md) | One entry to the existing Eval architecture, proof, procedure, Contract planning, and design history |
| [Design history](docs/design/README.md) | Original Architecture Grill decisions and detailed design provenance |

This README provides orientation and navigation. The linked owners define product, architecture, planning, proof, process, and status; this file does not introduce another normative authority.

## Continuing development

Follow the [Development workflow](docs/development.md#2-delivery-sequence-and-stage-boundaries). After baseline approval, use the selected milestone's Slice plan to guide its detailed Contract Grill and normative writeback. Complete its consumed Contract scope and necessary interfaces, reconcile affected documents, and establish research and actual upstream readiness before development.

Contract readiness is tracked by consumed scope, not by whole filename or family. Other milestones may remain pending; parent Slice completion separately requires all necessary milestones and integrated proof. The [global plan](docs/plans/implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) and [Progress recording rules](docs/progress/README.md) govern these distinctions.

Cross-context authoring guides, proposals, and handoff snapshots live in [`.scratch/`](.scratch/). Use the latest applicable handoff together with current owning documents; historical proposals and earlier review results do not override the current baseline.

## Backend development

The SL-01.M1 backend is available; frontend design/implementation and integrated milestone acceptance remain pending. See [installation, startup, configuration and checks](backend/README.md) and [actual progress](docs/progress.md#7-sl-01m1-backend-implementation).
