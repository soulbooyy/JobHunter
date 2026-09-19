# Development Guides

[Global documentation index](../index.md) · [Core development discipline](../development.md)

The main Development document is the stable authority for delivery sequence, Contract-ready development, test-first work, source/research discipline, verification routing and handoffs. This directory contains specialized procedures, required code organization and technology selections within the same Development category.

Milestone-specific development handoffs live in `handoff/`; their Contract references point to the current grouped paths in [Contract Structure](../contracts/structure.md#directory-layout).

| Guide | Responsibility |
| --- | --- |
| [Evaluation development and evidence](evaluation.md) | Real-path Eval, experiments/Scenarios, evaluator admission, findings, regression retention and re-evaluation |
| [Target repository organization](repository-structure.md) | Required responsibility layers, semantic test naming and incremental creation without empty scaffolding |
| [SL-01.M1 development handoff](handoff/sl-01-m1-handoff.md) | Original research plus actual backend implementation handoff; frontend/browser work remains pending |
| [Backend README](../../backend/README.md) | Maintained installation, runtime configuration, API entry points and check commands |
| [Target technology stack](technology-stack.md) | Planned backend/frontend tools, adoption boundaries and unresolved setup; not an installed dependency inventory |

Use [Implementation Plan](../plans/implementation-plan.md) and its linked Slice plans for actual decomposition, dependencies and required Contract scope. Use [Progress recording rules](../progress/README.md) for status/readiness and evidence records. Architecture and Acceptance retain their mechanism/proof authority; [Eval acceptance](../acceptance/evaluation.md) is the specialized proof owner consumed by the execution guide; this directory guide is navigation only and supplies no implementation or review evidence.

## Documentation maintenance

- Roll routine development status forward in `docs/progress.md`; do not create a daily log or a per-milestone status document.
- Finishing a milestone does not automatically create `backend-mX.md`, `summary.md` or another completion report. Implementation evidence and requirement/test mappings belong in `docs/progress/traceability.md`.
- Create a handoff only when a real cross-conversation, cross-agent or cross-stage transfer needs one. Keep one handoff per milestone by default and update that existing handoff when such a transfer is needed; it is not a routine activity log.
- Let Git history retain fine-grained implementation history. Do not duplicate commit-by-commit work, intermediate failures or abandoned implementation attempts in Markdown.
- Update durable owning documentation when its actual rules, interfaces or commands change. Keep test naming and file placement in `repository-structure.md`, runnable backend instructions in `backend/README.md`, and detailed verification evidence in traceability. These owner updates do not require a new summary or handoff.

Existing historical handoffs retain their historical evidence. These rules govern new work and the maintenance of current records; they do not authorize rewriting original design history.
