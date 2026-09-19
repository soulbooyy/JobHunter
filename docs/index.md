# JobHunter Documentation Index

> English is authoritative. This is the global navigation entry, not a new normative authority or evidence of review, implementation or acceptance. Read [Progress](progress.md) for actual state. W7 document review is recorded; user baseline approval remains pending.

## Start here

For a new task, read this index, the relevant directory README, the current owning documents and the latest applicable handoff. For baseline review and subsequent milestone work, use the [W7 joint-review handoff](../.scratch/w7-joint-review-handoff.md), its preceding [W6 handoff](../.scratch/w6-implementation-plan-handoff.md), and the [English authoring guide](../.scratch/document-authoring-spec.en.md). Handoffs describe their own snapshots; current paths and documents below control navigation. A targeted task need not read every Slice plan; joint baseline review must include all twelve.

## Formal document owners

| Need | Read | Responsibility |
| --- | --- | --- |
| Product behavior and user prerequisites | [Product Specification](spec.md) | Scope, tasks, inputs, visible outcomes and exclusions |
| Architecture and Contract boundaries | [Architecture](architecture.md) | Authority, mechanisms, high-level families and cross-family boundaries |
| Global implementation direction | [Global Implementation Plan](plans/implementation-plan.md) | Macro Slices, common planning rules and progression |
| Detailed Slice or milestone planning | [Slice index](plans/slices/README.md) | One file per Slice, with its milestones inline |
| Contracts Overview | [README](contracts/README.md) | Directory purpose and authority boundary |
| Contract Index | [index.md](contracts/index.md) | Navigation to planned and existing Contract documents |
| Contract Structure | [structure.md](contracts/structure.md) | Non-normative file organization, family mapping and consumer references |
| Product/system acceptance | [Acceptance](acceptance.md) | Unified business/runtime scenarios and required proof |
| Specialized Eval proof | [Eval acceptance](acceptance/evaluation.md) | Evaluation integrity and semantic quality/reliability/efficiency evidence |
| Delivery and maintenance method | [Development](development.md) | Stage order, Contract-ready development, test-first work, source/research discipline, verification routing and handoffs |
| Specialized Eval procedure | [Evaluation guide](development/evaluation.md) | Real-path Eval, experiments, evaluator admission, findings and evidence handling |
| Target code organization | [Repository structure guide](development/repository-structure.md) | Provisional frontend/backend layout, physical responsibility mapping and incremental package creation |
| M1 development entry | [SL-01.M1 handoff](development/handoff/sl-01-m1-handoff.md) | Reviewed Contract scope, integration research, engineering preparation and required proof |
| Target technology choices | [Technology stack](development/technology-stack.md) | Planned backend/frontend tools and progressive adoption; actual versions and installation remain separate |
| Status/readiness/evidence recording rules | [Progress README](progress/README.md) | Traceability, status meanings, parent/milestone reporting and scope-level readiness |
| Actual state and remaining work | [Progress](progress.md) | Parent Slice aggregation and truthful current status |
| Source trace, milestone evidence and Contract scope readiness | [Progress matrix](progress/traceability.md) | Supporting records within the Progress category |

These are seven document categories and six main documents. Slice plans support the Implementation Plan category; Contract Structure supports non-normative organization within Contracts. Eval acceptance supports the Acceptance category, the Eval procedure guide supports Development, and the Progress README owns recording rules within Progress; neither adds a category or competing business/architecture authority. Other index/README files provide navigation. File existence does not establish approved normative scope or capability completion.

## Directory map

| Directory | Entry | Use |
| --- | --- | --- |
| Documentation root | [README](README.md) | Layout and navigation/maintenance rules |
| Implementation planning | [plans/README](plans/README.md) | Global versus Slice responsibilities |
| Slice plans | [plans/slices/README](plans/slices/README.md) | Twelve stable Slice IDs and their detailed files |
| Formal Contracts | [Overview](contracts/README.md), [Index](contracts/index.md), [Structure](contracts/structure.md) | Directory guide, navigation and non-normative organization; four M1 normative scopes exist; other scopes remain pending |
| Acceptance support | [acceptance/README](acceptance/README.md) | Specialized Eval proof criteria; business/runtime scenarios stay unified |
| Development guides | [development/README](development/README.md) | Specialized Eval procedure, target code organization and technology choices under core development discipline |
| Cross-directory Eval navigation | [evaluation/README](evaluation/README.md) | Links Architecture, Acceptance, Development, Contracts and design history without duplicating their content |
| Progress rules and records | [progress/README](progress/README.md) | Recording discipline plus source, child milestone and Contract-scope ledgers |
| Grill design provenance | [design/README](design/README.md) | Original source register and detailed design modules |
| Harness design sources | [design/harness/README](design/harness/README.md) | Budget, Context, Memory, Recovery, Storage and Tools |
| Eval design source | [design/eval/README](design/eval/README.md) | Accepted design provenance, not an installed Eval system |
| Contract design inventory | [design/contract/README](design/contract/README.md) | Non-normative checklist, distinct from formal Contracts |

## Common task routes

- **Plan or refine one Slice:** global planning invariants → owning Slice file → Product/Architecture/Acceptance → relevant current source clauses → affected Progress scope/evidence.
- **Grill a milestone's Contracts after baseline review:** owning Slice required portions → Architecture ownership → Contract Structure/Index → existing normative definitions when available → scope ledger. Complete both sides of needed interfaces; do not require unrelated file/family scope.
- **Implement after readiness:** Development → ready normative scope and actual upstream capabilities/components → owning Slice and Acceptance → Eval procedure where applicable → actual evidence under Progress recording rules.
- **Review or revisit the W7 baseline:** W7 findings, authoring guide and W6 handoff → six main documents, Contract Structure, Eval acceptance, Eval procedure guide, Progress recording rules and all twelve linked Slice plans → complete source matrix and both verification seams.
- **Resolve a source conflict:** owning formal document → relevant original Grill clauses and later controlling corrections. ACCEPTED labels alone do not override partial supersession.

## Path relocation

The former `docs/implementation-plan.md` has moved to [`docs/plans/implementation-plan.md`](plans/implementation-plan.md). Its detailed SL-01–SL-12 and milestone sections now live in the linked Slice files. Current references point directly to their owners. Historical handoffs and original sources retain their snapshot paths; this relocation changes neither Q/S identifiers nor milestone identifiers.

Development 7's detailed Eval procedure now lives in [development/evaluation.md](development/evaluation.md); Development 8's recording rules now live in [progress/README.md](progress/README.md). Historical subsection anchors remain relocation entry points; current references point to the detailed owners.
