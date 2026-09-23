# SL-02.M2 Development Handoff — Demanded Preview and Export, Backend First

> English is authoritative. Transfer revision: **2026-09-21.S2M2-r1**, following effective CG04-Q1–Q135 and explicit user authorization for closure review, necessary writeback and normative publication. This is a development entry point, not implementation or renderer evidence. Read [scope review and prerequisites](../../progress/traceability.md#64-sl-02m2-reviewed-scope-and-interface-evidence) before work.

[Milestone plan](../../plans/slices/sl-02-saved-authority-materials.md#sl-02m2-demanded-preview-and-export) · [Contract Index](../../contracts/index.md) · [Decision register](../../design/contract/sl-02-m2-grill.md) · [Acceptance](../../acceptance.md#43-demand-and-safe-derivative-recovery)

## 1. Backend scope and consumed definitions

Implement explicit exact-version material demand, immutable application-delivered configuration, independent RenderIntent/shared Work, contained Manifest/Artifact, original acceptance receipts, managed file publication/read integrity, bounded local recovery and the six declared HTTP operations. Keep Domain rules, Application admission/transactions, persistence/filesystem adapters, HTTP and bootstrap responsibilities in their existing repository layers. Do not introduce a universal job framework or use transport DTOs as business authority.

| Definition owner | M2 additions and necessary preserved scope |
| --- | --- |
| [Common](../../contracts/common.md#com-043) | COM-043–046; referenced naming/scalars/errors COM-001–040, digest COM-032 and LINK COM-042 |
| [Workspace](../../contracts/foundation/workspace.md#wsp-012) | WSP-012; single local user/access/ownership under WSP-001–004/006/008 |
| [Profile](../../contracts/candidate/profile.md#pro-009) | PRO-009; exact shape/display/read semantics PRO-001–008 |
| [Evidence](../../contracts/candidate/evidence.md#evd-015) | EVD-015; typed fields, Item kind, retained versions/ownership EVD-001–014 |
| [Resume](../../contracts/candidate/resumes-grounding.md#res-016) | RES-016; exact document/AST/settings/source/lifecycle RES-001–015 |
| [Candidate Save](../../contracts/candidate/candidate-save.md#sav-017) | SAV-017; preserve SAV-001–016, especially old receipt/codec/HTTP semantics |
| [Materials](../../contracts/applications/materials.md#mat-004) | MAT-004–030 plus preserved MAT-001–003 source/Save boundary |
| [Derived Work](../../contracts/foundation/derived-work.md) | DRW-001–026 |
| [Storage](../../contracts/foundation/storage.md#sto-029) | STO-029–039 plus referenced placement/ownership, durability, migration, earlier receipt/history integrity |

Public routes are POST `/api/v1/render-intents`; GET `/api/v1/render-intents/{render_intent_id}`; GET `/api/v1/render-configurations`; GET `/api/v1/render-configurations/{render_configuration_id}`; GET `/api/v1/artifacts/{artifact_id}`; GET `/api/v1/artifacts/{artifact_id}/content` with optional disposition. Use actual Contracts for complete shapes, status codes and processing order.

No MaterialBundle, follow-current subscription, automatic Save-triggered intent, cancellation/release, force-rerender, public Work/history/retry/repair/configuration-write API, model/platform call, Preparation approval or sending authorization is in scope. Editor-local Draft preview remains M1 frontend work. Current backend task does not include frontend implementation unless separately instructed.

## 2. Actual upstream checkpoint and preservation

At the closure source inspection, current working-tree Store targets product schema **3**, recognizes historical schemas 1/2/3 and the migration source chain is `b720a94fd381 → cd891047a2e6 → ef03c92ba671`. The latter is the candidate-authority migration. Candidate authority, nine POSTs and ten GETs are registered in the source and transferred in [M1 handoff §6](sl-02-m1-handoff.md#6-backend-to-frontend-and-next-consumer-transfer--2026-09-21). [Existing M1 evidence](../../progress/traceability.md#saved-candidate-backend-evidence) records 294 passing backend tests; this Contract-publication task did not rerun them.

Those M1 additions include uncommitted/untracked working-tree files. Preserve them and any unrelated user work. Source presence and inherited test evidence are separate from verifying the actual checkout, migration head or a live database at development entry. The original M1 handoff's schema-2 sections are historical, not the current baseline.

No M2 persistence, coordinator, installed rendering stack, font catalog or rendered output was found. The root manifest contains no backend WeasyPrint/PDFium/Pillow dependency; frontend Playwright tooling is not a backend renderer. M1 frontend/editor/local A4 preview remains unverified here. Do not claim whole-M1 or M2 completion.

Read AGENTS.md, [Development](../../development.md), [repository structure](../repository-structure.md), [technology stack](../technology-stack.md), [backend operation guide](../../../backend/README.md), current `pyproject.toml`/`uv.lock`, affected code and version-specific schema definitions. Reuse the existing strict scalar/Decimal JSON parsing, typed value codec, UoW/transactions, exact source repositories, physical-directory ownership and local Host/Origin checks within their actual applicability.

Add a forward migration from the **actual head when implementation begins**. Schema 4 is only today's expectation from the observed schema-3 baseline, not a Contract constant; parallel development can change it. Do not rewrite historical migrations, call create_all to repair existing storage or run migrations against user data. Preserve all prior Entry/Preferences/candidate data, references and receipts, including receipts whose original mutable Entry was deleted. Keep Materials' command namespace and prefix independent. No historical Resume receives a backfilled Materials object.

## 3. Engineering prerequisites and capability gates

The following are unfinished engineering work, not approved concrete catalog values or successful experiments:

| Prerequisite | Required result before dependent capability is claimed |
| --- | --- |
| Pipeline choice and execution model | Pin applicable layout/PDF/raster/PNG dependencies, assess supported platform/install/distribution and prove needed output behavior; decide actual isolation/termination model without promising in-process killing |
| Font catalog | Select exact static single-face TTF/OTF files and accompanying distribution rights; record hashes and role mappings for all four logical fonts, with glyph/mark evidence |
| Source Han Sans 2.005R exception | Native Regular and Bold; Italic = native Regular + fixed synthetic italic; BoldItalic = native Bold + fixed synthetic italic. BoldItalic is not a native file or synthetic bold. Freeze path/parameters/dependencies with pipeline_version; pass actual PDF/PNG, pagination and mark-combination proof before can_generate=true |
| Other three logical fonts | Their concrete mappings are unselected; default native role requirements remain, and no synthetic-bold/other-font exception is granted. A genuinely needed new mechanism returns to Contract review |
| Template/catalog | Fix labels/date/null semantics, margins/headings/spacing/wrap behavior and concrete PNG width in the versioned implementation/catalog, preserving Resume settings and shared A4 pagination |
| Limits/defaults | Initial max_attempts=3 and concurrency=1; 4 KiB may be the initial finite HTTP body limit. Select and document practical max_pages, max_png_pixels, max_output_bytes and timeout_ms using the actual renderer; capture them per Work, without a policy entity or permanent Contract numbers |
| File protocol | Validate stable-snapshot serving, non-overwriting final placement, flush/directory durability and crash behavior on the supported filesystem; separate logical state from live renderer/file ownership |
| Output conformance | Verify fixed A4 pages, actual PDF numerical serialization tolerance, embedded/textual fonts, permitted links/no active content, complete PNG assembly and failure behavior for unsupported glyphs/limits |

The Grill's [research record](../../design/contract/sl-02-m2-grill.md#research-and-verification-boundaries) supplies primary-source observations. WeasyPrint → PDFium → PNG assembly is a candidate research path, not a selected or tested stack. Pango's synthesis API is not evidence that synthesis survives a PDF path. Do not install an entire proposed stack without the repository's normal component-adoption work in the implementation task.

A structurally valid configuration can register while dependencies are missing, with can_generate=false. Existing artifact reads/Candidate APIs may remain usable. All four logical font choices and applicable output dependencies must meet their gates before advertising true. A false flag is truthful partial availability, not fulfillment of M2's rendering delivery requirement.

Documentary readiness permits starting independently bounded domain/projection/persistence/protocol work using known interfaces. It does not waive research for dependent rendering work or final real-output acceptance. Concrete catalog UUIDs/hashes/versions are not frozen in business Contracts, but changing immutable configuration content requires a new ID and output-affecting implementation changes advance their descriptor versions.

## 4. Implementation order and critical seams

1. **Reverify prerequisites and test boundaries.** Inspect current code/head and determine which upstream readers validate whole Evidence bodies. Implement the explicit Materials projection without weakening full Candidate readers: complete exact Resume/Profile, member-ordered Evidence IDs/Item.kind/typed fields, no unused Evidence.content prerequisite. Plan independent expected examples for retained/retired refs and corrupt unused versus required data.
2. **Domain and protocols.** Implement closed shapes/nullability, exact target identities, configuration equality, original acceptance receipt and Materials fingerprint using the unchanged COM-045 encoder. Validate new command's access/raw/field/fingerprint, replay first, then current new-demand admission; source resolvability alone is not eligibility.
3. **Versioned persistence.** Add forward migration/recognition, relational constraints, immutable configuration registration and retained records. Preserve old namespaces/codec values and explicit offline migration. A missing historically referenced configuration cannot be repaired by startup catalog registration.
4. **Atomic acceptance and reads.** Commit receipt + Intent + exactly one disposition: verified Artifact reuse, existing unfinished Work, or new Work with captured limits and association. Handle same-key and exact-target races, join-versus-terminal arbitration, actual metadata corruption and missing-byte candidate skipping. Expose coherent pure reads without requiring a running renderer.
5. **Verified catalog/pipeline.** Complete the research gates before real rendering integration; implement controlled local candidate output only. Do not let renderer code publish domain state. Add independent conformance cases for all supported text/marks/whitespace/lists/links, structured fields, legal empty output and multi-page layouts.
6. **Coordinator, discovery and recovery.** Persisted queue discovery survives lost wakeups. Queued capability failure compares Work ID/QUEUED/observed count and consumes no claim; actual claim atomically increments count and sets a fresh attempt ID. RUNNING publication/failure is fenced. Reconcile unknown commit before reexecution; captured limits survive restarts; known renderer failure is not automatically retried. Timeout revokes publication; physical resources remain occupied until real exit.
7. **File publication and serving.** Validate candidate/limits, durably prepare bytes, place without overwrite, then atomically publish Artifact/Manifest/Work/all pending Intents. Preserve uncertain or live-writer files. Send the same complete verified snapshot with exact length/type/disposition/no-store, no dynamic conversion; Range does not produce 206.
8. **HTTP integration and evidence.** Reconcile actual OpenAPI/error vocabulary, a derived M2 API guide/navigation and later generated frontend client when routes exist. Do not create a guide claiming planned endpoints are live. Run current backend checks and real temporary-store concurrency/failure cases, update requirement→code/test evidence and report incomplete renderer/frontend scope explicitly.

Save creates no M2 intent or changing target. A newer Resume/current Evidence/Profile or ordinary removal cannot revoke already accepted exact Work; new generation still requires ACTIVE Resume. Readiness is not currentness, receipt replay is not polling, and metadata availability is not download availability. Do not restore superseded CURRENT_RESUME/cancel/fixed-three-attempt/hash-identity/mandatory-Accept-Ranges/0.01-pt policies from historical proposals.

## 5. Verification and completion

Use the maintained backend guide entry: `uv sync --locked` followed by `./scripts/check`. The script supplies the actual Ruff/format/Pyright/pytest/document-check commands; inspect it and the current manifest before running rather than infer targets from this snapshot. Test-first work and naming follow the Development owners. Run migrations only on isolated test stores with the documented explicit migration entry point, not real user data.

Minimum required proof includes the scenarios in [Acceptance §4.3](../../acceptance.md#43-demand-and-safe-derivative-recovery), DRW-026 and MAT-030: all acceptance dispositions; original-snapshot replay after removal/fulfillment/payload loss; namespace/fingerprint compatibility; count-zero preflight failure and races; old-attempt fencing; recovery exhaustion/unknown commits; live-writer resource retention; file-before-DB crash points; strict GET/POST/content errors; and real PDF/PNG/marks/font/output evidence. Fake renderer tests can prove orchestration seams but cannot certify rendering fidelity. Backend checks cannot certify frontend/browser preview/download behavior.

Current publication checks are recorded in the ledger. No runtime tests, dependency installs, schema migration, backend/frontend implementation, real PDF/PNG validation, commit or push were performed by the Contract publication. Update Progress when actual state changes; never mark M2 or parent SL-02 complete from this handoff or Ready Contracts alone.


## Scoped implementation-time font correction — 2026-09-23

The original prerequisite table above is a historical checkpoint. [The accepted font amendment](../../design/contract/sl-02-m2-grill.md#cg04-font-20260923) and current MAT-012 supersede its native-four-face requirement and Source Han Sans-only exception: Sarasa Gothic SC uses four native faces; Source Han Sans SC 2.005R and Source Han Serif CN use official Regular/Bold plus deterministic italic derivatives; LXGW WenKai 1.522 maps Regular/Medium to regular/bold with corresponding italic derivatives. All four final role hashes are required. No rendering capability is established by this correction alone.

## Backend-to-client transfer — 2026-09-23

The backend now targets schema 4 through `a41d7e90c263`, preserving all earlier revision definitions and requiring explicit offline migration. Exact Materials source projection, retained demand/receipts, one fenced execution slot, fixed verified PDF/PNG pipeline and the six public routes are implemented. Read the maintained [backend operation guide](../../../backend/README.md#saved-resume-materials), [derived API guide](../../api/sl-02-m2.md), live `/openapi.json` and [actual requirement/test evidence](../../progress/traceability.md#materials-backend-evidence); this checkpoint supersedes the original “not installed/not implemented” snapshot only for those delivered backend responsibilities.

The fixed renderer currently verifies macOS 26.6.2 arm64, Python 3.12.13 and exact pinned native dependencies. Install reviewed font assets explicitly with `uv run --locked python scripts/install_render_fonts.py`; an unavailable renderer leaves the configuration list empty without disabling unrelated APIs/retained artifacts. The 2026-09-23 user-approved font amendment above is effective; it does not remove actual-output capability gates.

The next frontend consumer must use explicit saved ResumeVersion/configuration IDs, retain original uncertain POST bodies, distinguish acceptance/polling/artifact metadata/content availability, and preserve exact historical results across removal/current-version changes. No generated client, browser preview/download, UI pending-state recovery or overall M2 acceptance was executed in this backend task. No frontend file was edited, real user store migrated, commit or push performed. Do not infer milestone/parent completion from backend test success.
