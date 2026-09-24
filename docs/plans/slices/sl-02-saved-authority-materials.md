# SL-02 Independent Resumes, portrait and materials

> Revised by accepted CG03S1-Q26 at **2026-09-24.S2M1S1-r1**. Planning is not implemented capability or whole-file Contract readiness. Earlier source-model/allocation descriptions are superseded.

[Global rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) · [Decisions](../../design/contract/sl-02-m1-supplement-grill.md) · [Progress](../../progress.md)

Source authority is complete independent Resume content. Default selects one current source for a read-only portrait; materials consume the explicitly selected document. No independent Knowledge/Profile fact editing or two-way synchronization remains.

<a id="sl-02m1-complete-saved-authority-and-atomic-save"></a>
## SL-02.M1 Independent document Save and default-derived portrait

**Scope:** Resume-owned contacts/structured fields/canonical AST; stable entry/block IDs; independent version chains and page-local preview; default/final removal with user replacement selection; read-only portrait/unavailable/refresh; durable async Evidence/Profile paired publication and exact history.

**Upstream/order:** Existing SL-01.M1 local Workspace/persistence → deterministic schema/document/Save/backend + ID-preserving frontend → production SL-03.M2 protected invocation → semantic portrait/Eval + integrated UI. Deterministic valid Save is independently deliverable before provider integration; full M1 completion requires the actual protected model capability. M1 and SL-03.M2 have no business dependency cycle: the latter supplies infrastructure, not a Resume workflow.

**Required scope:** COM-050–051, WSP-013–015, RES-017–024, EVD-016–023, PRO-010–016, SAV-018–025, STO-054–058 and their explicitly reused scalar/contact/AST/receipt/access clauses; CTX-016/TOL shared admission, PRO-014 and EVO-027 for semantic consumer. Existing SL-03.M1/M2 foundations must actually be implemented/adopted before invocation. Material execution remains M2, not a Save prerequisite.

**Reuse/replace:** Reuse command admission/receipts, local persistence, canonical run validation and editor layout. Replace shared Profile/Evidence/Baseline owners, current-source joins/adoption, TipTap adapters that drop IDs and independent Knowledge CRUD UI. New target API generation follows backend composition, never hand-edit generated clients. Explicit offline full development reset; no legacy data/request adaptation.

**Completion/proof:** Acceptance §4.1–4.2/§8–10 and EVO-027: exact IDs/text, privacy/support, one-call/zero-call reuse, atomic obligation, ABA/late publication/refresh/final removal, honest unavailable UI and actual Frames. No code/provider/browser acceptance is claimed by documentary Ready. No autosave, partial-Evidence screen, assistant apply or model retry/fallback.

**Development entry:** [SL-02.M1 handoff](../../development/handoff/sl-02-m1-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

<a id="sl-02m2-demanded-preview-and-export"></a>
## SL-02.M2 Demanded preview and export

**Scope:** Preserve explicit exact-version RenderIntent, immutable configurations, manifests/artifacts, shared work, verified bytes and bounded local renderer/recovery; direct schema-2 Resume source and manifest replace Profile/Evidence joins.

**Upstream:** M1’s actual deterministic document/read/persistence capability, not portrait/SL-03 model readiness or whole M1 acceptance. Reuse implemented Materials/Derived Work Coordinator, exact-demand receipts, storage and certified renderer as compatible.

**Required scope:** MAT-031–033, RES-018–024, STO-058 plus surviving MAT-004–030/DRW-001–026/COM-043–046/WSP-012/SAV-017. Old PRO-009/EVD-015/RES-016 joins and MAT-007 manifest shape are historical, not required adapters.

**Backend/frontend:** Adapt source reader/template/manifest/API/test fixtures; existing backend has prior render evidence only for the old source. Frontend saved-source preview/export is first implementation, separate from M1 local Draft preview. Recheck configuration identity for output-affecting changes and actual fonts/native capability. No automatic Save render demand, follow-current subscription, public Work/repair/history API or model dependency.

**Completion/proof:** Acceptance §4.3, MAT/DRW proof for exact/new/removed/default-switched source, faults/concurrency/recovery and real PDF/PNG/browser download. Rendering a populated B works with empty default A.

**Development entry:** [SL-02.M2 handoff](../../development/handoff/sl-02-m2-handoff.md). Reverify actual code and commands; do not infer implementation from this plan.

**Parent completion:** Both current milestones require their own backend/frontend and integrated proof. Historical old-model tests do not prove the replacement. No separate Knowledge Save remains.
