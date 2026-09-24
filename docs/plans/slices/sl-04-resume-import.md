# SL-04 Reviewed independent Resume import

> Revised by accepted CG03S1-Q26 at **2026-09-24.S2M1S1-r1**. Planning is not implemented capability or whole-file Contract readiness. Earlier source-model/allocation descriptions are superseded.

[Global rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) · [Decisions](../../design/contract/sl-02-m1-supplement-grill.md) · [Progress](../../progress.md)

Replace the former two-stage Knowledge-first product with upload/parse → reviewed temporary Resume draft → one confirmed document Save.

<a id="sl-04m1-reviewed-structural-import"></a>
## SL-04.M1 Reviewed structural import

**Scope:** Parse into the complete RES-018 canonical draft, stable logical IDs and disclosed gaps; user review/correction/cancel; one ordinary SAV-018 document creation. Parser output is not a fact authority. Default selection after Save uses ordinary M1 rules and triggers derivation only when appropriate.

**Upstream/reuse:** Actual SL-02.M1 deterministic document/Save/ID capability and local storage/privacy. Rendering review consumes M2 only if delivered review uses real artifacts; model-assisted parsing consumes actual SL-03.M2 only if selected. No unconditional portrait-success or Knowledge Save prerequisite.

**Required Contracts/blockers:** RES-017–023, SAV-018–025, EVD-016/019, STO-054–058; planned resume-import Contract must still define parser/draft/upload retention/error/confirmation interfaces. No placeholder path is normative readiness. Inspect parser adoption/licensing and source-to-canonical fidelity before implementation.

**Backend/frontend:** First implementation. Build temporary parse/review lifecycle and draft adapter; UI edits the complete independent document and discloses omissions, not a multi-fact confirmation/adoption stage.

**Proof/completion:** Cancellation creates no formal Resume/facts; partial parse is visible; single Save atomicity/replay/uncertainty, invalid IDs and permission failure; successful default Save survives portrait failure. Required import Contract/Eval remains pending.

**Development entry:** [SL-04.M1 handoff](../../development/handoff/sl-04-m1-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

**Parent completion:** One reviewed import milestone with actual parser, review/Save integration and failure proof; no retained stage-one Knowledge outcome.
