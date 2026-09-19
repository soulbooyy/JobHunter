# Storage Contract — Local M1 Persistence

> English is authoritative. Normative scope revision: **2026-09-19.M1-r1**. Scope: local Workspace/ManualApplicationEntry persistence, startup, receipts and privacy. This is not completion of immutable assets, Harness recovery, retention policies or later storage consumers. Review/readiness is recorded in [Progress](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger).

[Index](../index.md) · [Common](../common.md) · [Workspace](workspace.md) · [Entry](../jobs/manual-application-entries.md) · [Decisions](../../design/contract/sl-01-m1-grill.md)

## 1. Placement and runtime ownership

<a id="sto-001"></a>
**STO-001.** `data_directory` MUST resolve to a stable local per-user location independent of source checkout and process working directory. Startup MAY explicitly configure it; the selected absolute physical location MUST be fixed for the run. Explicit missing, non-directory, unreadable or unwritable locations MUST fail, without creating the missing configured directory or substituting another one. Default absence and existing emptiness follow WSP-003. The platform default and startup configuration mechanism MUST be documented by the implementation; they are infrastructure choices, not Workspace identities. M1 supports local filesystems, not shared/network data-directory semantics.

<a id="sto-002"></a>
**STO-002.** Before recognition/initialization, the backend MUST acquire and hold exclusive runtime ownership keyed by resolved physical directory identity. A concurrent owner MUST cause `DATA_DIRECTORY_IN_USE` startup failure, including owners on different ports. Multiple browser clients remain permitted. Symlink/path aliases MUST NOT evade exclusion. Process exit/death MUST permit subsequent reacquisition; filename/PID presence alone MUST NOT be the live-owner test. Lock coordination MUST remain outside the selected data directory or otherwise leave WSP-003's emptiness decision unaffected. No business listener precedes successful ownership and startup checks.

## 2. Application schema and recognition

<a id="sto-003"></a>
**STO-003.** The primary file MUST be `jobhunter.sqlite3`. The two required application tables MUST contain the following non-null columns; no Workspace/click/version table is introduced. SQL text uses case-sensitive binary comparison for identity and canonical time ordering. Alembic MAY maintain its own technical metadata; it does not replace product schema identity/version.

| Table | Column | SQLite storage representation |
| --- | --- | --- |
| `manual_application_entries` | `manual_application_entry_id` | TEXT PRIMARY KEY, explicitly NOT NULL; COM-027 |
| | `company_name` | TEXT NOT NULL; MAE-003 |
| | `role_title` | TEXT NOT NULL; MAE-003 |
| | `application_url` | TEXT NOT NULL; MAE-004 |
| | `revision` | INTEGER NOT NULL; COM-028 |
| | `created_at` | TEXT NOT NULL; COM-017 |
| | `updated_at` | TEXT NOT NULL; COM-017/MAE-006 |
| `manual_application_entry_create_receipts` | `request_id` | TEXT PRIMARY KEY, explicitly NOT NULL; COM-027 |
| | `request_fingerprint` | TEXT NOT NULL; COM-032/MAE-008 |
| | `manual_application_entry_id` | TEXT NOT NULL UNIQUE; original identity, COM-027 |

<a id="sto-004"></a>
**STO-004.** Storage MUST enforce primary/unique/non-null constraints and directly expressible value constraints: stored string/integer types; company/role lengths 1–200; URL length 1–8192; revision 1–9007199254740991; UUID spelling/length; lowercase 64-hex digest; canonical fixed-width UTC timestamp representation and `updated_at >= created_at`. Implementations MAY use STRICT tables or equivalent explicit `typeof`/CHECK constraints. Complete calendar, Unicode, trim, URL and operation semantics MUST still be admitted through Common/Entry rules; ORM column types alone do not provide that admission.

There MUST NOT be content/fingerprint uniqueness. Receipt original identity MUST NOT have a foreign key/action that prevents business deletion, cascades receipt deletion or clears the identity. Its uniqueness also fences historical entry-ID reuse. Indexes MAY support reads without changing these rules.

<a id="sto-005"></a>
**STO-005.** Recognized M1 storage MUST have SQLite `application_id = 0x4A484E54` and application `schema_version = 1`, mapped to SQLite `user_version`. SQLite's internal `schema_version` MUST NOT be used as product format authority. Recognition MUST check the primary file, application identity, supported version, required tables/columns/constraints, necessary selected migration metadata and database integrity, not just a filename or header marker. Integrity checks do not replace schema checks. A plain SQLite database from another application is not recognized JobHunter storage.

Existing-store opening MUST NOT create a missing primary file, run `create_all`, stamp a migration version or auto-upgrade/repair a schema. An implementation using Alembic MUST provide one authoritative initial revision and a versioned schema-recognition specification shipped with the implementation; this is a schema-check definition, not a separate manifest file in `data_directory`. The product version and tool metadata MUST agree. Extra indexes/SQLite auxiliary files do not justify accepting missing required structure.

<a id="sto-006"></a>
**STO-006.** Only WSP-003-eligible first use MAY run initialization. Required application schema, recognition metadata and selected Alembic metadata MUST commit in one real SQLite transaction; partial DDL success is not completed initialization. Normal SQLite journal/WAL recovery MAY run for an existing store before recognition. Auxiliary files MUST NOT be deleted or labeled failed initialization solely because they exist. If required identity/structure is absent after recovery, fail without rebuilding. Initialization residue remaining after a failed attempt is nonempty existing data on the next startup, not permission to auto-start again.

## 3. Transactions, read consistency and receipts

<a id="sto-007"></a>
**STO-007.** Application-owned short transactions MUST atomically couple entry/create receipt, or update content/revision/time, or physical deletion as required by MAE-007/010/011. Validation/read/admission and conditional write MUST be protected against stale writes and concurrent create replays. A write MUST NOT be acknowledged as successful before confirmed commit. Network access, model calls and browser interaction MUST NOT occur inside authority transactions. Storage MUST NOT re-execute a business command as an invisible recovery action.

<a id="sto-008"></a>
**STO-008.** If transaction completion is uncertain, the storage implementation MAY perform finite recovery of the same transaction-completion process only when the underlying API guarantees safe retry semantics without re-executing the business command. If safe completion does not establish the commit outcome, it MUST return command outcome `OUTCOME_UNKNOWN`; confirmed non-commit is handled separately below. This permission MUST NOT be interpreted as a requirement to execute `COMMIT` again after an ambiguous result. A known rollback/non-commit caused by storage failure maps to `STORAGE_UNAVAILABLE`; uncertain commit maps to `OUTCOME_UNKNOWN`, both HTTP 503 at the Entry boundary. Session/connection object state alone is not proof of a prior command's outcome. A confirmed commit followed by response failure MUST NOT be relabeled a definite non-commit; return recoverable authoritative success or require caller verification without re-executing the command. Neither code is a persisted Entry state.

<a id="sto-009"></a>
**STO-009.** Read results MUST contain consistent committed rows: a record's identity, content, revision and timestamps come from the same observation; list assembly MUST NOT mix partial mutations or silently omit rows. URL resolution MUST check revision and return URL from one consistent observation. Read transactions MUST end before browser navigation. These guarantees do not reserve the record against later writes or imply indefinite snapshot leases.

<a id="sto-010"></a>
**STO-010.** Successful-create receipts MUST survive for the Workspace lifetime without automatic expiry in M1 and MUST survive physical entry deletion. Entry deletion MUST remove its business row without a hidden current/history copy; receipts retain only MAE-008's three fields. No update/delete receipt ledger, recycle bin, persisted pending-command queue or automatic receipt cleanup is introduced. The retained digest is private operational data, not a substitute for deleted content or a proof of anonymous retention.

## 4. Startup diagnostics

<a id="sto-011"></a>
**STO-011.** Successful startup MUST emit one non-persisted `LocalStartupResult` with exactly `outcome` (`INITIALIZED` or `OPENED`), `data_directory` (the fixed absolute path) and integer `schema_version` (`1`). These are infrastructure diagnostics, not an HTTP business resource or Workspace identity. Before listener startup, failures MUST emit a sanitized COM-029 error with empty `field_errors`, then exit nonzero.

| Startup code | Meaning |
| --- | --- |
| `DATA_DIRECTORY_UNAVAILABLE` | Selected location missing when explicit, not a directory, inaccessible or unwritable |
| `DATA_DIRECTORY_IN_USE` | Another backend holds runtime ownership |
| `STORAGE_NOT_RECOGNIZED` | Nonempty directory lacks complete recognized application storage, including missing primary file/identity/schema or interrupted-init residue |
| `SCHEMA_UNSUPPORTED` | Recognized application identity has an unsupported product format version |
| `STORAGE_CORRUPT` | SQLite recovery/integrity validation identifies corruption |
| `INITIALIZATION_FAILED` | An eligible first initialization did not complete successfully |
| `STORAGE_UNAVAILABLE` | Other storage access/I/O failure prevents opening |

Diagnostics MUST NOT claim an exact physical cause that cannot be established. Identity recognition precedes version admission; integrity/open failure can precede either when metadata cannot be read. No startup error grants overwrite, auto-repair or fallback permission. A startup failure is not reported as a successful business command or a ready listener.

## 5. Durability and privacy

<a id="sto-012"></a>
**STO-012.** SQLite settings MUST explicitly support durable acknowledged commits across process crash/power loss on the supported, correctly functioning local filesystem/device. Implementations MUST verify effective settings rather than rely on defaults. Normal recovery MUST preserve committed entry/receipt coupling and atomic updates/deletion. Hardware damage, manual file removal or devices falsely reporting flush are outside this guarantee. M1 introduces no application encryption/key-management, backup/restore or network-filesystem product; physical business deletion is not a comprehensive media/backup erasure promise.

<a id="sto-013"></a>
**STO-013.** The data directory/database and necessary auxiliary files MUST use appropriate current-user filesystem access permissions. M1 MUST NOT automatically upload entries or diagnostics. Ordinary logs MAY retain necessary operation category, correlation IDs, duration and result codes; they MUST NOT retain company/role text, full URLs, raw request bodies, SQL parameters, fingerprints or transport secrets. Startup's explicitly defined diagnostic path/version is permitted; it MUST NOT become a repeated business-payload dump. Frontend errors, access logs and SQL/ORM debug logging MUST obey the same boundary. Local availability does not authorize model/provider exposure.

## 6. Definition ownership and implementation latitude

Entry owns content, fingerprint bytes and operation semantics; Storage owns physical representation, recognition, atomicity, retention and diagnostics. Workspace owns eligibility and runtime admission. Common owns shared types/error shape. The sole backend and transaction guarantees apply to the actual M1 consumer; immutable history, Harness recovery, remote telemetry retention and later asset storage remain pending.

Implementation preparation selects one migration-script location, concrete SQL checks/indexes, safe driver mode, journal/synchronization settings, permission/lock adapters and supported platform defaults. Those choices implement these clauses; they cannot weaken first-use recognition, commit outcomes or browser/user intent. Provenance: CG01-Q14–Q17, Q19, Q22–Q26, Q33, Q36, Q38, Q41–Q44. No requirements are retired in this initial revision.
