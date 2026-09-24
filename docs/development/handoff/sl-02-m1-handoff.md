# SL-02.M1 Development Handoff — Saved Authority, Backend First

## Current development transfer — 2026-09-24.S2M1S1-r1

**Classification:** Existing backend/frontend require source-model replacement. This addendum controls the replaced source scope; any older body below is a historical snapshot. [Owning plan](../../plans/slices/sl-02-saved-authority-materials.md) · [Accepted supplement](../../design/contract/sl-02-m1-supplement-grill.md) · [Current scope/evidence](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

**Profile naming:** Implement `CandidateProfileProjection.entries: ProfileIndexEntry[]`; each entry is `{name, description, evidence_refs}`. The model-output collection is also `entries`, with PRO-013’s local-ID-to-EvidenceRef conversion preserved. Profile schema remains v1.

**Consumed scope:** COM-050–051; WSP-013–015; RES-017–024; EVD-016–023; PRO-010–016; SAV-018–025; STO-054–058; CTX-016/EVO-027 plus explicitly surviving shared values. Read the actual Contract bodies through [Contract Index](../../contracts/index.md); indexes/planned paths are not norms. Read Product/Architecture/Acceptance, AGENTS.md and maintained component guides before implementation. Old shared Profile/Evidence/Baseline authority, Knowledge-first Save, parallel Fits and mandatory current assistant apply are superseded only as recorded in those owners.

**Observed baseline:** HEAD `66e2bb8dfd081a44b3a28873d5b992805ce46d56`; backend runtime schema 5, migration head `d092ea64bf17_invocation_durability.py` after `a41d7e90c263`. Existing SL-02.M1 backend/frontend and M2 backend implement the old model. Runtime M1 is implemented; production SL-03.M2 and later consumers are not. Current documentation publication changes no product code, database, dependency or generated client. Recheck git status and preserve unrelated edits; historical test counts below are not rerun evidence.

**Backend delta:** Replace shared Profile/Evidence/Baseline sources with schema-2 Resume-owned contacts/fields/AST and logical-ID validation/persistence. Preserve strict raw admission, receipt ordering, revision/no-op and uncertainty handling under the new six-command surface/fingerprint. Add atomic default/source/current-state/build obligation and fenced async paired Evidence/Profile publication, one-call attempts and exact reuse. Remove old candidate routes/data readers; use an explicit offline full development reset, not legacy conversion.

**Frontend delta:** Adapt features/resume/editor/resume-editor.tsx, candidate/editor-document.ts and block-editor.tsx, candidate/use-command.ts, entities and pages. Preserve entry_id/block_id through TipTap conversion, split/merge/copy/undo; no new editor. Replace separate contacts/facts Save/adopt UI with direct document editing and read-only portrait. Implement unavailable/refresh, final removal and user-selectable next/previous default replacement. Regenerate API schema only after backend target exists.

**Upstream and order:** 1 deterministic schema/source/Save; 2 canonical-ID editor and client; 3 actual SL-03.M2 consumer adapter/model; 4 paired lifecycle/Eval/browser acceptance. Rendering is separate.

**Data/API transition:** Q38/Q41 permits later explicit offline reset of the complete configured development DB/generated materials, including test Preferences/Entries/Runtime records, while preserving source/Git/configuration. Never reset on startup or during this documentary transfer. No legacy request adapter/data conversion/archive reader is required. Preserve published migration source history and post-transition immutable source/result/receipt histories. Coordinate changed backend schemas with generated clients; do not fabricate target availability from this handoff.

**Invocation integration gate:** Register and prove PRO-014’s own complete derivation-decision reconciliation, Runtime ending mapping, frozen deadline/local-recovery bounds and finite configuration values. Do not inherit conformance-only ending/grace policies. A ready document source is not proof this executable integration exists.

**Required proof and open blockers:** Acceptance §4.1–4.2/§8–10 and EVO-027. Prove exact IDs/text, exclusion/privacy, unsupported whole-output rejection, ≤1 request per attempt, zero-call reuse, atomic crash obligation, ABA/stale publish/duplicate refresh/final delete. Full semantic completion awaits actual SL-03.M2 implementation and concrete provider/schema/capacity configuration evidence; deterministic Save must not wait for it. This is required future evidence. Ready replacement Contracts do not establish runtime/browser/model acceptance; unrelated Pending future scopes remain blocked until their own consumer definitions and upstream capabilities are ready.

**Maintained verification entry:** [Backend guide](../../../backend/README.md), [frontend guide](../../../frontend/README.md), [Development](../../development.md), [UI system](../../ui/DESGIN.md). From repository root, inspect then use `UV_CACHE_DIR=/tmp/jobhunter-uv-cache ./scripts/check`, `npm --prefix frontend run api:generate`, `npm --prefix frontend run check` and `npm --prefix frontend run test:e2e` as consumed. Rendering requires the actual certified native/font environment; invocation requires its reviewed provider/configuration. For docs run `python3 scripts/check_contract_links.py` and `git diff --check`. Report executed commands and unexecuted scope; backend tests never substitute browser acceptance.

## Historical handoff snapshot

> English is authoritative. Target normative revision: **2026-09-21.S2M1-r1**, following accepted CG03-Q1–Q100 and the Q98 missing-target clarification. This is a cross-context development transfer, not implementation evidence. [Reviewed scope](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence) records documentary readiness; no S2 runtime work has been performed.

[Milestone plan](../../plans/slices/sl-02-saved-authority-materials.md#sl-02m1-complete-saved-authority-and-atomic-save) · [Contract Index](../../contracts/index.md) · [Decisions](../../design/contract/sl-02-m1-grill.md) · [Acceptance](../../acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts)

## 1. Backend scope to implement

Implement the backend for three-field versioned Profile, six-kind Evidence/current Baseline, independently versioned Resume expression/presentation with exact Profile/Evidence references, default Resume selection, nine atomic commands, successful receipts, consistent current/exact/list readers, strict HTTP admission and explicit schema-3 initialization/migration.

Consume all of these reviewed portions and their explicit shared references:

| Owner | IDs |
| --- | --- |
| [Common](../../contracts/common.md#com-038) | COM-038–042 |
| [Workspace](../../contracts/foundation/workspace.md#wsp-008) | WSP-008–011 |
| [Profile](../../contracts/candidate/profile.md) | PRO-001–008 |
| [Evidence/Baseline](../../contracts/candidate/evidence.md) | EVD-001–014 |
| [Resume/manual lineage](../../contracts/candidate/resumes-grounding.md) | RES-001–015 |
| [Candidate Save/HTTP](../../contracts/candidate/candidate-save.md) | SAV-001–016 |
| [Materials source boundary](../../contracts/applications/materials.md) | MAT-001–003 |
| [Storage](../../contracts/foundation/storage.md#sto-021) | STO-021–028 |

Frontend implementation remains deferred until UI design. Include its server-side data/admission/recovery needs now; do not create a Resume UI or claim local A4 preview delivered. Render demand/intent/jobs/configuration, PDFs/exports and renderer/font asset research belong SL-02.M2. Import multi-Item confirmation, Advisor/AI grounding, Candidate/Resume Fit and DeepFit are later consumer scopes. No new model/network dependency is required by manual Save.

## 2. Observed upstream baseline

At this handoff's read-only inspection, actual backend runtime is **schema 2**, with maintained startup/access/persistence, ManualApplicationEntry and Preferences. Read [backend README](../../../backend/README.md), root manifests/lock and the affected source before choosing commands. Prior evidence records 160 passing backend tests plus lint/type checks; this task did not rerun them. Current frontend evidence belongs SL-01 and does not implement S2.

Preserve `backend/alembic/versions/b720a94fd381_initial.py`, `cd891047a2e6_preferences.py` and their version-specific definitions. The schema-1 module is deliberately frozen; the current Store targets schema 2. Add a new migration and explicit schema-3 recognition rather than rewriting historical definitions or calling create_all against existing data. Existing offline entry is:

```sh
uv run --locked python -m jobhunter.bootstrap.migrate --data-directory "/absolute/existing/data-directory"
```

Its current binary upgrades only through schema 2. Extend it to schema 3 under the same physical-directory lock; do not run it on user data during development. Ordinary S2 startup must refuse recognized schema1/2 until explicit migration, and never repair missing initial records. Preserve Entry/Preferences data, namespaces, receipts and parser semantics.

Reusable infrastructure includes Common scalar/URL validation, Decimal JSON parsing, strict Preferences transport, explicit read/write transactions, foreign-key enforcement, physical-directory ownership, Host/Origin middleware and sanitized transaction errors. S2 still needs node/depth budgets, its three request-byte limits, new Domain/Application/HTTP modules, typed content, receipt codec/results and schema3 storage. Reuse infrastructure within the existing [layer organization](../repository-structure.md); framework DTOs/ORM cannot own Domain equality or transaction semantics.

## 3. Critical invariants for implementation

- Knowledge owns facts. Evidence/Profile updates or retirement never automatically update Resumes or clear local text/marks/links. New/switched Resume refs must be active/current at commit; an unchanged previously published exact binding may remain historical/retired.
- Evidence source content is plain semantic AST; Resume local content uses text runs/marks. Raw-run validity precedes canonical merge; local whitespace is preserved. Short fields trim before remaining-character validation; Evidence body rejects controls before trim. JSON bytes are not semantic equality.
- Evidence Update reads immutable target Item.kind after envelope admission, before type-specific validation/fingerprint/receipt. Missing target returns404 before receipt even for a previously used key. This read never moves mutable revision/lifecycle admission before replay.
- A successful receipt preserves command-time mutable root/selection and exact immutable refs. Replay cannot reconstruct from current state. Evidence no-op records completion-time Baseline; Create/Remove preserves completion-time default selection.
- Revision admission precedes equality on new execution. Two distinct Evidence writes build a complete latest Baseline without a client global revision. Create root/version/baseline/selection/receipt participants commit together; no cross-Resume transaction or hidden business reexecution.
- Default selection has its own revision for ABA. ACTIVE removal checks both target and selection tokens; a matching already-REMOVED no-op skips current selection/replacement checks. First-create concurrency preserves the first committed default without requiring a caller selection token.
- Failed/uncertain writes are different. A post-commit response failure does not undo authority; later rejected retry does not prove the first attempt uncommitted. Broken persisted lineage is internal failure, not partial success or current substitution.

These points are navigation aids; the referenced normative clauses own exact payloads, limits, ordering and errors.

## 4. Suggested backend delivery order and proof

1. Build Domain schemas/value admission/canonicalization for Profile, six Evidence fields and both ASTs, Resume settings/refs, root/default lifecycle. Use independent positive/negative examples for code-point and Unicode/control rules, null/empty distinctions, month intervals, URL spelling, raw-before-merge and numeric half-point semantics.
2. Implement the exact SAV-010 fingerprint and SAV-008/009 immutable reconstruction/mutable snapshots. Verify known byte/digest vectors independently, Unicode byte lengths, boolean tags, negative zero, semantic-equal inputs and distinct command/target/revision inputs. Do not derive expected values using the production codec itself.
3. Add versioned schema3, fresh atomic seeds, existing-store recognition and explicit offline migration. Use real temporary SQLite files to verify enabled same-owner/exact-ref constraints, schema1→2→3 preservation, failed initialization/migration, restart and exclusive ownership. Do not edit prior migrations or real user data.
4. Implement separate Application commands and consistent readers. Test same/different-Item races, receipt races, capacity edges, no-op/max revision, clock rollback, first-default creation, default ABA/removal races, historical source retention and mutable snapshot replay after later changes.
5. Expose nine POSTs and defined GETs with exact DTOs, access/transport/body/node/depth checks and error mapping. Reconcile generated OpenAPI with normative schemas; document the actual S2 integration interface after it exists. No fake availability or hand-written generated client substitute.
6. Inject lost-response/commit/reconstruction failures and prove no duplicated command, partial Baseline, automatic Resume change or invented rollback. Run required conformance plus existing Entry/Preferences regression checks against schema3 using maintained backend commands.
7. Update requirement-to-code/test evidence and actual API/schema availability in Progress. Report commands/results and unexecuted frontend/browser/rendering scope separately. Backend completion leaves local editor/A4 preview and whole-M1 acceptance pending; parent SL-02 also requires M2.

Manual backend work does not require a semantic-model Eval. It does require the deterministic, concurrency, fault/recovery and privacy proof in [Acceptance §4](../../acceptance.md#4-saved-facts-resumes-grounding-and-derived-artifacts) and [§10](../../acceptance.md#10-privacy-storage-and-honest-history). Tests and actual component preparation follow the current [Development guide](../../development.md), not a promise that this handoff has executed them.

## 5. Transfer status

The effective decisions and consumed interfaces have documentary review. No known M1 semantic blocker remains. Concrete SQL/index/migration revision, modules and test fixtures are implementation choices within the norms. Surface a real contradiction if found; do not silently invent business fields, broaden old protocols or reopen the superseded propagation/QuickScreen/private-fact mechanisms.

No schema3 implementation, dependency install, migration, user-data modification, commit or push occurred during this Contract publication. The current user's scoped authorization does not assert historical global baseline approval or product acceptance. A new development task can start the backend subset from these owners; frontend work waits for UI design.

## 6. Backend-to-frontend and next-consumer transfer — 2026-09-21

The sections above preserve the Contract-publication snapshot. The backend subset is now implemented on schema 3; current checks and requirement mappings are maintained in [Progress](../../progress.md#12-sl-02m1-backend-authority-and-schema-3) and [traceability](../../progress/traceability.md#saved-candidate-backend-evidence), not duplicated as a new milestone summary. Start from the [candidate API guide](../../api/sl-02-m1.md), live `/openapi.json`, [backend operation guide](../../../backend/README.md), and [derived codec fixture](../../../backend/tests/fixtures/candidate_fingerprint.json).

Use `uv run --locked python -m jobhunter.main` from the repository root. Existing recognized schema 1/2 requires the explicit offline migration command in section 2, now extended atomically through revision `ef03c92ba671`/schema 3. Source revisions and their definitions are unchanged. No real user store was migrated during development. No dependency change was needed; supported macOS/Python/SQLite/framework versions were rechecked and recorded in the evidence owner.

Available interfaces are nine POSTs and ten GETs for the saved-authority scope. First-use seeds are real durable objects; Profiles and Baselines are never fabricated by reads. Future clients must distinguish immutable source snapshots from command-time mutable result snapshots and current reads. Preserve exact original requests across uncertain outcomes. Evidence Update takes its field schema from the existing Item; Resume source freshness is rechecked at commit. Default selection has its own ABA-sensitive revision, and removal requires both tokens. Configure the actual frontend Origin explicitly; no wildcard or frontend-only CORS assumption.

No frontend file, generated TypeScript client, browser conformance, visual editor, source-reset UX or local A4 preview was implemented/verified here. Shared OpenAPI error vocabulary/version expanded; future client generation must consume the actual selected interfaces and reconcile drift. Backend/manual saved settings do not imply installed rendering fonts, a material request, a PDF or grounding success. M1 and parent SL-02 remain Partial. M2 backend can use this verified upstream subset without waiting for M1 frontend, subject to its own scope/research readiness; M2 rendering/durable intent/export is still absent.
