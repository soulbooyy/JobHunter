# Contract Design Navigation

[Global documentation index](../../index.md) · [Design provenance](../README.md)

## Detailed Contract Grill records

| Milestone | Working record |
| --- | --- |
| SL-01.M1 — Local Workspace and Manual Application Entries | [Decision register and current frontier](sl-01-m1-grill.md) |
| SL-01.M2 — Collection Preferences and immutable versions | [Decision register and current frontier](sl-01-m2-grill.md) |

The decision register follows the Architecture Grill register: conclusions, status, rationale, scoped supersession, formal writeback and the current open frontier. It omits question transcripts and proposed answers. These records support continuity and later normative writeback; they do not establish Contract readiness or implementation.

All accepted SL-01.M1 decisions are maintained only in the [decision register](sl-01-m1-grill.md), including common conventions, Workspace, ManualApplicationEntry, storage and scoped architecture supersession. Do not create separate module decision records. The four [M1 normative bodies](../../contracts/index.md#existing-normative-contracts) now own the formal definitions. Interview decisions through Q45 are complete; scope readiness and development work remain separately recorded in Progress.

SL-01.M1 controlling architecture revision: [CG01-BC1 — ManualApplicationEntry](sl-01-m1-grill.md#cg01-bc1). It supersedes the old Manual Job portions in the preserved Inventory and earlier Q2–Q5 answers; formal Job completeness and immutable snapshots remain effective.

SL-01.M2 is controlled by [CG02-BC1](sl-01-m2-grill.md#cg02-bc1), [Q6–Q10](sl-01-m2-grill.md#cg02-q6) and [CG02-S1](sl-01-m2-grill.md#cg02-s1): complete six-dimensional future acquisition intent and immutable versions; Collection mapping/admission and independent Job Pool queries remain separate. Earlier Q1/Q2/Q3/Q5 clauses are explicitly superseded where affected. M2 QuickScreen is removed; the completed consumed bodies and readiness are linked below.

[CG02-Q11–Q15](sl-01-m2-grill.md#cg02-q11) fixes six canonical field names, structured explicit inputs, five UNLIMITED choices, unordered-value equality, keyword trim and lazy atomic root/version creation. Only the keywords disallow UNLIMITED. Q12 replaces the earlier keyword field name without changing acquisition ownership. [CG02-Q16–Q20](sl-01-m2-grill.md#cg02-q16) completes dimension choice/value, numeric, education and canonical-set decisions; [CG02-Q21–Q25](sl-01-m2-grill.md#cg02-q21) adds complete saved objects, publication/replay/history and unconfigured-read meaning. [CG02-Q26–Q30](sl-01-m2-grill.md#cg02-q26) settles Save/read HTTP operations, replay-stable results, publication times and lifetime success receipts. Q29 explicitly rejects temporal ordering by UUIDv4 and adds no historical sequence. [CG02-Q31–Q35](sl-01-m2-grill.md#cg02-q31) adds strict UTF-8/media-type admission, the small nested error-path grammar, uncertain Save recovery, processing precedence and raw request limits. Shared error vocabulary belongs to Common; Preferences owns triggers. [CG02-Q36–Q40](sl-01-m2-grill.md#cg02-q36) settles fingerprints, receipts, representation, explicit evolution and final error mappings. The decision frontier is closed. [Preferences](../../contracts/candidate/preferences.md), Common/Workspace/Storage additions and [M2 scope review](../../progress/traceability.md#62-sl-01m2-reviewed-scope-and-interface-evidence) now supply normative IDs and documentary readiness; backend/UI implementation remains pending.

## Preserved architecture inventory

The [Contract Design Inventory](contract-design-inventory.md) is a preserved non-normative checklist of candidate responsibilities, known semantics, invariants and sources. It does not define exhaustive fields, types, enums, transitions, API payloads, database schema, validation errors or migrations.

For architectural ownership, read [Architecture 16](../../architecture.md#16-contract-document-structure-and-responsibility-plan); for planned file organization, read [Contract Structure](../../contracts/structure.md). For planned/existing normative documents, use [Contract Index](../../contracts/index.md). For actual readiness, use the [scope ledger](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger). Inventory entries or examples cannot make a missing scope ready.
