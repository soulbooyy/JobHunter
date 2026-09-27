# Grill Records

[Documentation index](../index.md) · [Contract Index](../contracts/index.md)

This is the single navigation entry for retained Grill decisions, session transfers and structural discussion material. These records preserve provenance and scoped supersession; they are not normative Contracts, implementation evidence or a parallel readiness ledger. Read current formal owners first for development, and the relevant record when continuing a Grill or resolving interpretation and supersession. English is authoritative for maintained documentation.

## Architecture provenance

[Architecture decision register](grill-me-design-tree.md) preserves the original Q/S decisions. Later accepted corrections control the clauses they replace, even where an earlier record still says ACCEPTED. The former standalone Harness and Eval source files are no longer present; their historical references do not imply available source documents. Do not reconstruct deleted records or treat a missing source as a new design decision.

## Detailed Contract Grill records

| Discussion | Decision record | Session transfer |
| --- | --- | --- |
| SL-01.M1 — Manual Application Entries and local foundation | [Decisions](contract/sl-01-m1/decisions.md) | No separate Grill transfer retained |
| SL-01.M2 — Preferences | [Decisions](contract/sl-01-m2/decisions.md) | No separate Grill transfer retained |
| SL-02.M1 — Original saved-source and Resume design | [Decisions](contract/sl-02-m1/decisions.md); read the supplement for later replacements | No separate Grill transfer retained |
| SL-02.M1 supplement — Independent Resumes and default-derived portrait | [Decisions](contract/sl-02-m1-supplement/decisions.md) | [Historical fulfilled prompt](contract/sl-02-m1-supplement/handoff.md) |
| SL-02.M2 — Demanded preview and export | [Decisions](contract/sl-02-m2/decisions.md); apply later supplemental corrections | [Source-time session prompt](contract/sl-02-m2/handoff.md) |

A completed interview can still contain effective decisions. Its old launch prompt does not restart the interview or override later decisions. Check the decision register and [current scope ledger](../progress/traceability.md#6-contract-normative-scope-readiness-ledger) before resuming work.

The former SL-03.M1/M2 Grill records and transfers have been deleted, and their former Contract scopes withdrawn for redesign. No archive or replacement session is supplied here. Read the [M1 withdrawal](../progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) and [M2 withdrawal](../progress/traceability.md#66-sl-03m2-reviewed-scope-and-interface-evidence); retained SL-02 consumer clauses do not establish a ready replacement Runtime.

## Contract structure discussion

| Material | Role |
| --- | --- |
| [Prompt](contract/structure/prompt.md) | Source-time instruction to review document organization, not detailed Contract fields |
| [Proposal](contract/structure/proposal.md) | Historical alternatives; its fifteen-Slice and whole-parent gate proposal was not adopted |
| [Handoff](contract/structure/handoff.md) | CS1–CS5 agreement and the transfer to W6, with its original time-specific status |

These materials explain the structural decisions. [Contract Structure](../contracts/structure.md) and the [Implementation Plan](../plans/implementation-plan.md) own maintained organization and planning within their respective responsibilities.

## Preserved architecture inventory

[Contract Design Inventory](contract/contract-design-inventory.md) is a historical coverage checklist. Its examples are not normative fields, schemas, APIs or migration requirements. Apply later decisions and read actual Contract bodies for consumed scope.

## Material lifecycle and handoffs

- Keep each detailed Contract discussion in one `contract/<discussion>/` directory. `decisions.md` records accepted conclusions, open questions, scoped supersession and writeback references; preserve existing decision IDs and anchors.
- Add `handoff.md` only for a real cross-context Grill transfer. It records the task and continuation context, not another decision authority. Create no empty session directories or template files for future milestones.
- Development transfers remain in `docs/development/handoff/`. Read the applicable development handoff before implementation; Grill prompts do not replace it. Routine status belongs in Progress, not a new handoff.
- Older W1–W7 authoring materials remain under `.scratch/`. The three Contract structure discussion files are located here because they are Grill inputs and outputs.
- Use `rg --hidden` when searching this hidden directory. Do not add a second index or per-session README.

## Relocated paths

| Former location | Current location |
| --- | --- |
| `docs/design/grill-me-design-tree.md` | [Architecture register](grill-me-design-tree.md) |
| `docs/design/contract/contract-design-inventory.md` | [Inventory](contract/contract-design-inventory.md) |
| `docs/design/contract/<discussion>-grill.md` or `docs/.grill/contract/<discussion>-grill.md` | `docs/.grill/contract/<discussion>/decisions.md` for retained discussions listed above |
| `docs/development/handoff/contract_grill/<discussion>-contract-grill-handoff.md` | `docs/.grill/contract/<discussion>/handoff.md` for the two retained transfers listed above |
| `.scratch/contract-structure-grill-prompt.md` | [Structure prompt](contract/structure/prompt.md) |
| `.scratch/contract-structure-proposal.md` | [Structure proposal](contract/structure/proposal.md) |
| `.scratch/contract-structure-grill-handoff.md` | [Structure handoff](contract/structure/handoff.md) |
| `docs/design/README.md` and `docs/design/contract/README.md` | This single Grill entry |

Only locations and navigation are reorganized. Decision bodies, IDs, source-time claims and supersession records remain historical evidence; relocation does not renew deleted scope or establish implementation readiness.
