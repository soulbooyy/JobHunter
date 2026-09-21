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

## 7. M2 schema, persistence and explicit evolution

Scope revision **2026-09-20.M2-r1**. The original STO-001–013 text and schema-1 definitions are preserved. The additions below apply to the new schema-2 consumer and explicitly qualify supersession; M1 evidence is not schema-2 runtime evidence.

<a id="sto-014"></a>
**STO-014.** M2 MUST use jobhunter.sqlite3, application_id 0x4A484E54 and product schema_version 2 stored as user_version. SQLite's internal schema_version is not product identity. For M2 only, STO-003's two-table-only layout, STO-005's supported-version/initial-revision scope, STO-006's schema-1 initialization scope and STO-011's literal diagnostic version 1 are superseded by STO-015–019. Their nonempty-store recognition, no-auto-upgrade/repair/fallback and atomicity guarantees remain. Schema 1 remains an explicitly recognized migration source, not a store that ordinary M2 runtime may serve. Existing schema-1 initial migration/recognition definitions MUST NOT be rewritten into schema 2. No downgrade or unchanged-M1-binary compatibility is promised.

<a id="sto-015"></a>
**STO-015.** Schema 2 MUST preserve the two M1 tables/constraints/data and add exactly the following required application tables/columns. Required fields are NOT NULL unless explicitly qualified. Names/types below are persistence representation, not extra API fields. Selected migration metadata remains technical.

| Table | Required columns / SQLite representation |
| --- | --- |
| preference_sets | preference_set_id TEXT PRIMARY KEY; singleton_key INTEGER UNIQUE constrained to 1; current_preference_set_version_id TEXT; revision INTEGER; created_at TEXT; updated_at TEXT |
| preference_set_versions | preference_set_version_id TEXT PRIMARY KEY; preference_set_id TEXT; created_at TEXT; configuration TEXT containing a JSON object |
| preference_save_receipts | request_id TEXT PRIMARY KEY; request_fingerprint TEXT; preference_set_id TEXT; preference_set_version_id TEXT; result_revision INTEGER; outcome TEXT |

Configuration MUST persist the complete canonical business value under PRF-002–006; JSON key order/whitespace/serialization bytes MUST NOT determine equality or fingerprint. No keyword/city child table, configuration-copy in receipts, historical sequence or Workspace business table is introduced. Receipt fields follow PRF-014 and have no timestamps. Additional non-semantic indexes/migration metadata are implementation choices, not new authorities.

<a id="sto-016"></a>
**STO-016.** Database constraints MUST enforce singleton/primary/unique/non-null/type and directly expressible value rules: UUID spelling, Sha256Hex spelling, Common Revision bounds, canonical UTC timestamp shape, root.updated_at >= root.created_at, valid receipt outcomes and configuration as a JSON object. Complete calendar/Unicode/choice/canonical validation remains Application admission, not an ORM type declaration. Database foreign-key/constraint enforcement MUST guarantee each version belongs to a root, root current belongs to that same root and receipt references agree on root/version ownership; simple independent references that permit cross-root pairing are insufficient. Composite foreign keys or equivalent constraints MAY implement this, with deferred checks for first-publication cycles. Concrete SQL syntax/indexes are implementation choices; constraints MUST actually be enabled. No uniqueness on configuration, digest or receipt version reference is allowed. Referential actions MUST NOT delete retained versions/receipts or clear their identities.

<a id="sto-017"></a>
**STO-017.** Recognition MUST check application identity, supported product version, required tables/columns/constraints, selected migration metadata agreement, SQLite integrity and required foreign-key/reference consistency. A filename/header/version marker alone is insufficient. Runtime M2 MUST open only complete recognized schema 2; recognized schema 1 MUST fail normal startup with SCHEMA_UNSUPPORTED and a sanitized explanation that explicit offline migration is required. Unknown versions, corrupt/incomplete source or target schemas MUST NOT be stamped, repaired or rebuilt. Shipped version-specific recognition specifications MUST distinguish schema 1 from schema 2. Detected invalid persisted configuration or broken root/current/receipt authority MUST fail rather than become NOT_CONFIGURED, empty history, a substituted version or success. Reads MUST return admitted stored business values; JSON text spelling alone is not corruption when its parsed canonical content is valid.

<a id="sto-018"></a>
**STO-018.** The explicit offline schema-1-to-2 migration MUST acquire the same exclusive physical-directory ownership as runtime, with no business listener and no fallback/create of missing configured storage. It MUST fully recognize its source before mutation. A complete schema 2 MAY return a verified no-upgrade-needed outcome. Schema 1 upgrade MUST atomically commit added schema, product user_version and Alembic metadata in one real transaction, preserving every M1 entry/create receipt (including deleted originals' receipts), identities, content, revisions, timestamps and fingerprints. It MUST NOT create Preference root/version/receipt rows or rewrite the source's initial revision definition. Migration failure MUST NOT publish a partial schema or pretend an uncertain commit rolled back.

After uncertain completion, normal SQLite recovery and version-specific recognition MUST establish complete source or target state before reporting an outcome; if neither can be established, return a sanitized failure, retain the data and require diagnosis. No command replay, automatic repair, downgrade or empty replacement follows uncertainty. Command spelling and successful CLI output layout are implementation choices documented by the implementation; success MUST identify the verified target schema and whether migration occurred or was unnecessary. Failure MUST exit nonzero using the Common sanitized error shape; recognition/access failures retain their established diagnostic meanings, confirmed storage non-commit uses STORAGE_UNAVAILABLE and unresolved completion uses OUTCOME_UNKNOWN. These are CLI diagnostics, not new HTTP resources.

<a id="sto-019"></a>
**STO-019.** WSP-003-eligible fresh M2 initialization MUST commit the complete schema-2 structures/product identity/version/migration metadata in one real transaction; partial source-to-target initialization is not completed first use. Existing nonempty data never gains first-use eligibility through a missing primary file. Successful runtime startup MUST use exactly STO-011's LocalStartupResult fields and INITIALIZED/OPENED meanings with schema_version 2. Explicit offline migration does not invent another LocalStartupResult outcome. No business listener precedes successful initialization/recognition; startup failures retain STO-011's sanitized/nonzero/no-fallback guarantees under schema-2 applicability.

<a id="sto-020"></a>
**STO-020.** M2 MUST apply STO-001/002 placement/ownership, STO-007/008 transaction/confirmed-commit/uncertainty rules, STO-009 consistent-read principle and STO-012/013 durability/filesystem/privacy guarantees to Preferences. Application-owned transactions MUST atomically couple first root/version/current/revision with receipt; later new version/current/revision/time with receipt; or unchanged business state with a no-op receipt. Versions and successful receipts MUST survive restart for Workspace lifetime without automatic expiry/deletion. Application write paths MUST NOT mutate published version content. Save admission and receipt/concurrency races MUST be protected by the transaction/constraints; no hidden business-command reexecution or external calls inside authority transactions. Recognition/serialization failures cannot fabricate rollback or success.

Ordinary logs/errors/traces MUST NOT include Preference text, complete configurations, body values, fingerprints, SQL parameters or transport secrets. Necessary sanitized categories/correlation IDs/result codes and explicit startup diagnostics remain allowed. M2 does not authorize upload, model access, encryption/key-management or a backup/restore product. Existing M1 data/receipt semantics and privacy MUST survive migration and schema-2 Entry operation.

## 8. SL-02.M1 schema-3 authority and retained lineage

Scope revision **2026-09-21.S2M1-r1**. STO-001–020 remain the original published consumer baseline. These clauses extend the S2 binary only; no migration is executed by documentation.

<a id="sto-021"></a>
**STO-021.** S2 MUST use jobhunter.sqlite3, application_id 0x4A484E54 and product user_version 3 (not SQLite internal schema_version), while preserving the application/database identity, directory placement/runtime lock and complete schema-1/2 migration history. Retain STO-001/002 filesystem ownership and STO-012/013 durability/privacy principles; add a new migration rather than modifying published schema.py/Alembic revisions into schema 3. Existing Entry/Preferences values, immutable history, receipts, fingerprint semantics and namespaces MUST survive intact. Their actual behavior MUST remain compatible when hosted by the S2 binary. (Q93/Q94.)

<a id="sto-022"></a>
**STO-022.** Fresh schema-3 initialization and explicit upgrade MUST atomically install schema, required initial records, product metadata and migration metadata. Required seeds are exactly one Profile root/all-null ProfileVersion (PRO-003), one real empty Baseline/current pointer (EVD-009/010) and one DefaultResumeSelection null/revision 1 (WSP-009). No Resume or Preferences root/version is created. S2 objects use schema_version=1 independently of database schema 3. Incomplete schema/seeds/metadata MUST NOT be recognized as a valid empty Workspace. (Q49/Q55/Q72/Q93.)

<a id="sto-023"></a>
**STO-023.** Upgrade MUST use the existing explicit offline migration entry point under exclusive physical-directory ownership, without a runtime listener or concurrent owner. Source schema 1 MUST follow retained migration steps through schema 2 to 3; schema 2 advances through the new step. Normal startup MUST NOT migrate, repair, overwrite or silently recreate required objects. Preserve STO-017–019 complete-source/target recognition and safe failure principles for schema 3, including atomic schema/data/metadata changes and truthful uncertain completion. Unsupported/partial/damaged storage MUST fail opening; no directory/database fallback. For this S2 consumer, preserve STO-011 LocalStartupResult exactly as {outcome: INITIALIZED or OPENED, data_directory: fixed absolute path, schema_version: integer 3}; preserve its failure code meanings and pre-listener failure behavior. Recognized schema 1/2 are migration sources only and MUST fail ordinary S2 startup with SCHEMA_UNSUPPORTED. No new startup outcome is introduced for migration. Concrete Alembic revision ID and SQL syntax are implementation choices within this contract. (Q93.)

<a id="sto-024"></a>
**STO-024.** Identity, lifecycle, concurrency, lineage and constrained exact refs MUST have relational representation. Root/Version metadata, same-owner current refs, Resume Profile/member sources, Baseline members/current pointer, default selection and receipt exact refs MUST NOT exist only inside JSON. Enforce necessary existence/same-owner consistency with actual database constraints, with foreign keys enabled on every relevant connection; concrete composite FK/constraint/table syntax remains implementation choice. Internal membership/order columns MAY exist without creating business IDs. Content JSON MAY hold Evidence fields/content, Resume local AST/Header/document settings and command-time mutable snapshots; JSON bytes/key order/whitespace MUST NOT decide business equality. Domain/Application admission remains necessary beyond database constraints. (Q38/Q94.)

<a id="sto-025"></a>
**STO-025.** Application-owned transactions MUST atomically publish SAV-004–009 participants and enforce root/default revision, capacity, receipt uniqueness and commit-time source eligibility. Evidence publication MUST derive the complete latest ACTIVE/current set without lost concurrent different-Item changes. Receipt namespace uniqueness MUST be scoped per Workspace to SL-02 commands, separate from old namespaces. Concurrent receipt/constraint races MUST follow SAV-011, not duplicate execution or guessed conflict classification. No external/model/render action is permitted inside the transaction. Actual demanded intent joins the Save transaction only when M2 extends the scope under MAT-003. (Q69/Q73/Q84/Q94/Q95/Q99.) SL-02.M2 applicability is now closed by SAV-017: exact-only explicit demand creates no Save-triggered intent; the conditional future-consumer atomicity invariant remains preserved.

<a id="sto-026"></a>
**STO-026.** Published Profile/Evidence/Resume Versions, Baselines, retained roots and SL-02 success receipts MUST remain readable after ordinary retirement/removal and across restart. No ordinary lifecycle action or ACTIVE capacity policy may cascade-delete their lineage. Historical result reconstruction MUST use immutable exact refs plus SAV-009 mutable snapshots, never query current roots to fabricate an old result. Reads requiring root/current pairs or list/projection/selection MUST use one consistent snapshot. No uniqueness rule on content/fingerprint may prevent intentional new identities or A→B→A publication; request_id uniqueness is separate. Physical JSON serialization is implementation detail, not authority. (BC3; Q57/Q64/Q73/Q75/Q77/Q85/Q86/Q91/Q94.)

<a id="sto-027"></a>
**STO-027.** S2 MUST retain STO-007/008's truthful transaction outcome boundary: a response failure after commit does not roll back authority. Limited same-transaction completion recovery MAY occur only when the underlying API guarantees safe semantics without business-command reexecution; otherwise return OUTCOME_UNKNOWN if commit is ambiguous. Proven write non-commit may return STORAGE_UNAVAILABLE. An absent receipt in a transient read or rejection of a later retry alone MUST NOT prove an earlier uncertain attempt failed. Client behavior follows SAV-015. This does not require repeating COMMIT on ambiguous SQLite state. (Q90/Q99.)

<a id="sto-028"></a>
**STO-028.** An ordinarily absent requested object MUST use NOT_FOUND. Actually detected missing/wrong-owner persisted root/current/source/Baseline/member/receipt references or failure to reconstruct mandatory saved authority MUST be treated as internal integrity faults: affected reads return INTERNAL_ERROR, never partial lists, omitted members, substituted current refs, fabricated empty Profile/Baseline or command reexecution. Stop affected writes and safely roll back; commit ambiguity remains OUTCOME_UNKNOWN. Startup-detected missing mandatory records or incomplete storage fails before business listening without repair; no exhaustive historical-body scan on every startup is required. Operational diagnostics MUST be sanitized and MUST NOT expose raw Profile/Evidence/Resume bodies, inline URL values, receipt content, fingerprints, SQL parameters or transport secrets. No cloud upload, new backup/restore/erasure/encryption product is introduced. (Q93/Q100; Architecture §13.)

## 6. SL-02.M2 material persistence and execution boundaries

Scope revision **2026-09-21.S2M2-r1**. Earlier published consumer semantics remain effective within their scope. Provenance: [CG04](../../design/contract/sl-02-m2-grill.md).

<a id="sto-029"></a>
**STO-029.** For the M2-capable binary, extend STO-021–028's target-version applicability by a new forward migration from the actual implementation-time migration head. Preserve jobhunter.sqlite3, application_id 0x4A484E54, physical placement/ownership, published historical migrations and all Entry/Preferences/Profile/Evidence/Baseline/Resume/selection data, references, revisions, timestamps, command namespaces, receipt snapshots and fingerprints. Do not freeze schema 4 as a business Contract value. Concrete next version and Alembic revision belong to the verified implementation/handoff.

Upgrade MUST retain STO-018/023's explicit offline, exclusive-owner, fully recognized source and atomic schema/product-metadata/migration-metadata commit discipline. Normal startup MUST NOT auto-upgrade, repair, erase or fall back. Fresh initialization retains required existing seeds but MUST NOT create historical render demand, Work or Artifact; upgrade MUST NOT backfill them for existing Resumes. A target binary MUST recognize its actual supported schema completely before serving and reject older unsupported runtime schemas with the existing diagnostics. Historical schema-3 recognition remains intact for its original consumer. Q127.

<a id="sto-030"></a>
**STO-030.** Persist immutable configuration records, Artifact/Manifest, Intent, Work, necessary associations and Materials command receipts under their owned shapes in MAT-007/009/014 and DRW-002/003/008. Identities, exact refs, command uniqueness, state/result relations and ordered lineage MUST have enforced persisted integrity, not merely unvalidated JSON or application comments. Enforce (operation, request_id) within the Materials namespace, at most one unfinished Work per exact source/configuration pair, at most one Work per execution-backed Intent, and exactly one creating successful Work per new Artifact. Payload content hashes MUST NOT become business identity or impose uniqueness that merges Artifacts. Physical tables/columns/indexes are implementation choices within these invariants. Q2/Q4/Q28/Q88/Q110/Q111/Q116/Q133.

<a id="sto-031"></a>
**STO-031.** Acceptance MUST durably commit receipt, Intent and its complete disposition in one transaction under DRW-010; a new Work and its captured scalars/association are part of that transaction. Immediate reuse MUST commit a fulfilled Intent without fabricating Work. Receipt uniqueness and exact-target unfinished-Work uniqueness races MUST preserve DRW-011's original committed acceptance semantics. Terminal success/failure and all pending dependent results MUST commit atomically with their coherent event timestamps; no asynchronous completion repair substitutes for the transaction. State/count/attempt/result conditions MUST be checked atomically, including DRW-013's queued preflight condition and DRW-014/015's RUNNING fence. Q32/Q35/Q40/Q41/Q49/Q94/Q117/Q124.

<a id="sto-032"></a>
**STO-032.** After runtime ownership and complete store recognition, application startup MUST atomically register newly shipped configuration records before listeners/workers. Existing equal ID/content is a no-op; unequal content is an integrity conflict and MUST NOT overwrite. Check persisted historical references independently of new catalog insertion: a missing previously referenced configuration MUST NOT be silently repaired by re-registration. Dependency absence alone does not make a structurally valid record corrupt: register it and expose false capability under MAT-011/013 while unrelated application capabilities remain available. Detected conflicts/corruption/missing historical refs prevent normal opening of the affected store using existing sanitized integrity diagnostics. This is configuration registration, not automatic schema migration. Q58/Q102/Q103/Q113.

<a id="sto-033"></a>
**STO-033.** Material payloads MUST reside in managed subdirectories of the selected data_directory. Candidate files MUST be isolated by Work/attempt, and published payloads bind to Artifact identity without overwrite. Access MUST validate the actually opened managed regular file, not just a path string; do not accept directories/devices or follow payload symlinks outside the controlled scope. Preserve STO-002's legitimate physical data-directory alias handling rather than banning all directory aliases. No client-provided file path or public storage path is introduced. Q79/Q80/Q112.

<a id="sto-034"></a>
**STO-034.** Publication MUST order candidate preparation, complete validation, file durability, non-overwriting final placement with necessary directory durability, then the atomic database Artifact/Manifest/Work/Intent transaction. A committed Artifact MUST refer to already durably prepared immutable bytes. A final-looking path or reserved ID before that transaction is not a public Artifact. Implementations MUST verify the adopted filesystem durability/placement mechanism and preserve recoverable uncertainty; do not claim atomicity across file/database stores merely from rename or file existence. Q12/Q35/Q55/Q80.

<a id="sto-035"></a>
**STO-035.** Reuse and content reads MUST verify full actual byte length/hash against valid immutable metadata. Content serving MUST use one stable verified snapshot for both checking and sending, with bounded memory or controlled temporary storage; do not re-open a checked pathname as unverified new content. Current metadata/read success does not guarantee future payload availability. Content serving MUST return MAT-027's owned missing/corrupt/I/O distinctions; reuse MUST instead follow MAT-016's candidate-skipping versus metadata-integrity rules. Neither path may mutate historical results or trigger generation from a GET. Temporary serving snapshots are technical resources, not new Artifacts or a second content authority. Q37/Q51/Q55/Q78/Q115/Q132.

<a id="sto-036"></a>
**STO-036.** Restart recovery MUST retain the actual committed result when present and MUST NOT publish orphaned/partially prepared files as if they were committed Artifacts. After authorized fencing, an interrupted attempt may be retried within captured limits using a fresh attempt and freshly resolved exact source projection. Cleanup MAY remove only provably unpublished/unreferenced files whose prior writer cannot still access them. Unknown commit/reference state or unproven renderer exit requires retention. Do not delete published payloads under temporary-file cleanup, expose reserved IDs, or let stale attempts overwrite shared output. Runtime-lock acquisition alone does not prove a child renderer exited. Q45/Q79–Q81/Q86/Q107/Q109.

<a id="sto-037"></a>
**STO-037.** Retain successful receipts, Intent/terminal Work history, necessary associations, configuration records, Artifact metadata and published payloads under their owners without first-release TTL or ordinary lifecycle cascade. Physical loss/corruption does not retroactively change receipt snapshots or terminal fulfillment. Stable metadata/hash is not recoverable missing content. Ordinary Resume removal, Evidence retirement or configuration replacement MUST NOT cascade-delete exact history. No generic erasure/backup/restore product is introduced. Q10/Q17/Q23/Q72/Q92.

<a id="sto-038"></a>
**STO-038.** The exact internal Materials source interface MUST supply MAT-005/PRO-009/EVD-015/RES-016 from consistent retained identities/fields without current substitution. It MUST validate actual ownership and consumed values while allowing Evidence.content to remain unread/unvalidated when not an input. Existing full Candidate GET/Save validation remains unchanged; implement a distinct projection capability rather than weaken a shared full-reader Contract. Detect required corrupted relations as integrity faults; do not omit members, default fields or reconstruct current sources. Source payload faults during execution are classified under DRW-005, and pre-acceptance persisted-integrity faults under DRW-023. Q67/Q69/Q74/Q89/Q96/Q125.

<a id="sto-039"></a>
**STO-039.** M2 MUST preserve STO-027/028's honest receipt/commit uncertainty and corruption handling. Replays validate the original receipt and its required Intent/target relationship, without requiring the current Work/Artifact chain or payload availability. Detected malformed required metadata/references MUST NOT be reinterpreted as absent objects, cache misses, unsupported optional dependencies or permission to repair. Startup recognizes required schema/metadata/reference integrity without an exhaustive scan of every historical content body or every Artifact byte. Actual file/content verification occurs at the owning boundaries. Existing M1 sources/receipts retain their original checks and outcomes. Q15/Q45/Q77/Q78/Q115/Q116/Q133.
