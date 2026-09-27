# Documentation Directory

Start at the [global index](index.md) to select the relevant owner and task route. English is authoritative. This README and indexes are navigation aids. [Progress recording rules](progress/recording-rules.md) defines status and evidence recording separately from navigation. No additional product or Contract authority is created.

The root contains Product, Architecture, Acceptance, Development and the actual Progress summary. [plans/](plans/README.md) contains the global Implementation Plan and individual Slice plans. The Contracts directory has a [Contracts Overview](contracts/README.md), [Contract Index](contracts/index.md) and non-normative [Contract Structure](contracts/structure.md), alongside later actual normative definitions. [Evaluation](evaluation.md) keeps specialized acceptance criteria and their execution workflow in separate sections. [development/](development/README.md) contains engineering guides, API integration references and development handoffs. [progress/](progress/recording-rules.md) contains recording rules and supporting traceability/readiness/evidence records. [.grill/](.grill/README.md) groups retained Grill decisions, their session transfers, the historical Inventory and Contract structure discussion. Implementation handoffs remain under `development/handoff/`; deleted Grill sources are not recreated.

[Development API guides](development/api/README.md) contains derived interface guides for frontend design and integration; [SL-01.M1](development/api/sl-01-m1.md) documents the current local entry API without creating another Contract authority.

The [Eval related-document map](evaluation.md#4-related-documents) links Architecture, Contracts, Progress and retained Grill provenance without duplicating their authority.

## Maintenance

Keep detailed planning in its owning Slice file, shared planning invariants in the global plan, behavior/mechanisms/proof in their formal owners, and real readiness/implementation evidence in Progress. Update navigation when files or locators change. Update cross-document consumers when semantics or shared interfaces actually change; directory organization does not waive that reconciliation.

Read the relevant current documents and latest handoff before work. Original Grill files and historical handoffs are preserved; do not rewrite their history merely to modernize paths. The index records the former Implementation Plan path and current location. Current review/implementation state belongs to [Progress](progress.md).
