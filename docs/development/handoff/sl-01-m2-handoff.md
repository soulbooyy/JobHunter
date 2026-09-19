# SL-01.M2 Development Handoff — Preferences Backend First

> English is authoritative. Target Contract revision: **2026-09-20.M2-r1**. Decisions through CG02-Q40 are accepted. Sections 1–4 retain the preparation-time baseline; the implemented backend transfer and remaining UI scope are in section 5. Actual reviewed scope is in [Progress 6.2](../../progress/traceability.md#62-sl-01m2-reviewed-scope-and-interface-evidence).

[Milestone plan](../../plans/slices/sl-01-workspace-jobs-preferences.md#sl-01m2-collection-preferences-and-immutable-versions) · [Decisions](../../design/contract/sl-01-m2-grill.md) · [Conformance](../../acceptance.md#32-sl-01m2-contract-conformance)

## 1. Scope to implement

Implement Preferences backend configuration, lazy immutable publication, current/exact-version reads, canonical Save, concurrency, durable successful receipts and explicit schema-1-to-2 migration. Consume [Preferences](../../contracts/candidate/preferences.md) PRF-001–023, [Common](../../contracts/common.md) COM-033–037 plus reused baseline clauses, [Workspace](../../contracts/foundation/workspace.md) WSP-007 and [Storage](../../contracts/foundation/storage.md) STO-014–020. PRF-022's actual UI implementation waits for UI design; include its data/API needs without creating UI now.

No QuickScreen, Job production, source admission/query mapping, BOSS/Provider calls, candidate facts, history listing/restoration or alternate Workspace is required. M1 backend is the usable dependency; full M1 frontend is not a prerequisite. M2 remains Planned until code/evidence is supplied; backend completion cannot establish full milestone/parent acceptance.

## 2. Observed baseline and required impact

The current implementation is schema 1 only. It uses Alembic initial revision b720a94fd381 at `backend/alembic/versions/b720a94fd381_initial.py`; initialization shares a bootstrap-owned connection. The store recognizer in `backend/src/jobhunter/infrastructure/persistence/sqlalchemy/uow/store.py` checks product version, required DDL and migration metadata. The initial revision imports the schema-1 definition in `backend/src/jobhunter/infrastructure/persistence/sqlalchemy/models/schema.py`; do not change those definitions into schema 2 retroactively.

Read the actual [backend setup](../../../backend/README.md) and current dependency lock before implementation. At handoff inspection, Alembic 1.20.0 and SQLAlchemy 2.0.54 are pinned; version-specific recognition and the explicit migration entry point still need implementation. Current parser behavior does not enforce the new M2 raw-body/duplicate-key/nested-path rules. Apply stricter M2 behavior without silently changing M1's published boundary. Shared exception handling must retain sanitized Common errors.

Schema 2 preserves M1 Entry/create receipts, adds the three Preference tables and deliberately rejects ordinary startup on schema 1 until explicit offline migration. The unchanged M1 binary will reject schema 2. Migration is not `create_all`, a silent startup upgrade, a replacement empty database or a redefinition of the original Alembic revision.

## 3. Suggested backend work order

1. Build authoritative value admission/canonicalization, exact binary fingerprint and success/error DTOs. Verify raw numeric equality, code-point ordering, fixed enum ordering, nested paths and incompatible choice errors with independent fixtures. JSON serialization is not equality.
2. Extend version-specific schema recognition and fresh initialization; add explicit locked offline migration with atomic metadata/DDL and preservation tests. Verify foreign-key/singleton constraints actually reject invalid ownership. Do not start business listeners during migration.
3. Implement application transactions and repositories for lazy first Save, later changes/no-op, matching/differing receipt races, lifetime history and consistent current/exact reads. Test real temporary SQLite files and process restart/fault boundaries, not mocks alone.
4. Add the three declared HTTP operations, strict M2 transport budgets/admission, generated OpenAPI and precise Common errors. Validate same-ID replay after a later Save returns original success without resetting current. No inferred rollback after response failure.
5. Run the applicable conformance suite and M1 regression paths against schema 2. Update requirement-to-code/test evidence, actual migration commands and residual limitations in Progress. Leave UI/browser acceptance pending until designed and implemented.

Implementation chooses the CLI spelling, SQL constraint syntax, indexes and test/module layout within these Contracts. It must document supported runtime and actual install/start/migrate/check commands. No additional product decision is currently required for this backend scope; surface a concrete contradiction if implementation discovers one rather than silently changing a Contract.

## 4. Review and reporting

[Acceptance 3.2](../../acceptance.md#32-sl-01m2-contract-conformance) is the proof checklist. Report backend checks separately from UI and overall M2 acceptance. Preserve M1 Entry semantics including deleted-original receipt replay and original fingerprints. Do not claim working Collection, a populated formal Job Pool or an implemented parent Slice from Preferences backend tests.

User approval of Grill decisions and documentary interface review do not mean tests have run. No dependencies are installed, no real data migrated and no code/commit/push performed by this handoff.


## 5. Backend-to-frontend integration handoff

The backend described above is now implemented; actual requirement/test evidence and check results live in [traceability §8](../../progress/traceability.md#8-sl-01m2-backend-implementation-evidence), with rolling status in [Progress](../../progress.md#9-sl-01m2-backend-implementation). The preparation-time statements about missing code/schema-1-only runtime do not describe the current binary. Runtime versions remain pinned as recorded in the [backend README](../../../backend/README.md); its explicit offline migration command is the only supported schema-1 upgrade entry point. No user data was migrated by development.

For UI/client work, consume the [Preferences API guide](../../api/sl-01-m2.md), generated `/openapi.json` and [derived Save input](../../../backend/tests/fixtures/preference_save.json). The normative Contracts remain authoritative. Configure the actual frontend Origin explicitly; do not bypass Host/Origin checks. Keep null first-save preconditions, canonical set/Unicode semantics, original submitted error indices and original request preservation after uncertainty. An old successful replay can describe a historical version and must not be displayed as proof of current state.

PRF-022 UI, client generation/browser validation, client recovery and full M2 integration remain outside this backend completion. Concurrent frontend work has not been verified by this task. M1 frontend is not a prerequisite for this backend; neither M2 nor SL-01 is marked complete. No new handoff/summary file or automatic commit/push was created.
