# Implementation Planning

[Global documentation index](../index.md) · [Documentation overview](../README.md)

| Document | Owns |
| --- | --- |
| [Global Implementation Plan](implementation-plan.md) | Macro coverage, shared readiness/dependency invariants and recommended progression |
| [Slice index](slices/README.md) | Navigation to the twelve independently maintained Slice documents |
| Each linked Slice plan | Its goal/scope, controlling sources, milestone dependencies, required Contract portions, research, tests/Eval and completion |

Keep milestone plans inside their parent Slice file. Split a milestone only when its size justifies a separate document; preserve its ID and an explicit parent link, and reconcile references. No current milestone requires that further split.

For a local Slice edit, change its owning file. Update the global plan only when macro coverage, shared rules or cross-Slice direction changes. Do not duplicate milestone dependency tables or Contract portions in navigation files. Slice plans belong to the Implementation Plan category and do not introduce new business or Contract authority.

[Architecture](../architecture.md) owns high-level Contract boundaries; [Contract Structure](../contracts/structure.md) maintains the subordinate file organization; [Development](../development.md) owns delivery discipline; [Acceptance](../acceptance.md) owns proof; [Progress recording rules](../progress/README.md) owns status/readiness/evidence representation and [Progress](../progress.md) owns actual state. A planned milestone or existing Contract filename is not evidence of readiness or implementation.
