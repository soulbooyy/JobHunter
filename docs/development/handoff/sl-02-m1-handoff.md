# SL-02.M1 Development Handoff — Saved Authority, Backend First

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
