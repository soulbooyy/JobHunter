# Materials Contract — Saved Sources, Preview and Export

> **Current applicability — 2026-09-24.S2M1S1-r1.** MAT-001/002/005/006/007/008 source-join/manifest portions and MAT-014’s manifest/schema applicability change only for independent Resume sources under MAT-031–033. Exact-demand, configuration, verified bytes, rendering, retained history and external-consent boundaries otherwise survive. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../../.grill/contract/sl-02-m1-supplement/decisions.md); [current review](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. MAT-001–003 preserve the SL-02.M1 consumed scope. Sections 2–6 add **2026-09-21.S2M2-r1**; future Preparation/execution consumers remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../.grill/contract/sl-02-m1/decisions.md)

## 1. SL-02.M1 source and currentness scope

<a id="mat-001"></a>
**MAT-001.** Successful Profile/Knowledge/Resume Save MUST establish only its owned formal authority and receipt, not durable rendered preview/PDF/export readiness. Page-local Draft preview MUST remain non-authoritative and MUST NOT be treated as a saved artifact. M1 MUST NOT invent MaterialBundle/Artifact/RenderManifest schemas, renderer configuration, job/intent rows or recovery states without the actual M2 consumer. (UI1; Q95.)

<a id="mat-002"></a>
**MAT-002.** A saved Resume source MUST be read as its exact ResumeVersion plus retained exact Profile/Evidence refs using PRO/EVD/RES readers. A later source root current-pointer movement or ordinary Evidence retirement MUST NOT rewrite that Resume, invalidate its document identity or alone require rerender. Historical source binding MUST NOT be relabeled as latest Knowledge; failures of retained references MUST remain explicit under STO-028. Resume document identity is separate from default selection, management name and current Knowledge. (BC3; Q59/Q60/Q95/Q100.)

<a id="mat-003"></a>
**MAT-003.** M2 MUST define actual demand/configuration/output/readiness and durable work/intent with their consumers. Where existing demand requires intent on a Save, the implementation MUST extend that owning authority transaction atomically; a lossy post-commit notification cannot substitute. Rendering remains post-commit and cannot reverse a successful Save. M1 source boundary alone MUST NOT claim M2 rendered delivery, Preparation approval, execution or application success. Renderer-specific fonts/fallback, layout/export fidelity and actual material currentness beyond this boundary remain M2 scope. (Q95.) SL-02.M2 applicability is now closed by SAV-017: exact-only explicit demand creates no Save-triggered intent; the conditional future-consumer atomicity invariant remains preserved.

## 2. SL-02.M2 exact sources and provenance

Scope revision **2026-09-21.S2M2-r1**. Provenance: [CG04 decisions](../../.grill/contract/sl-02-m2/decisions.md). [Derived Work](../foundation/derived-work.md) owns demand/execution; [Storage](../foundation/storage.md#sto-029) owns durable relations/files.

<a id="mat-004"></a>
**MAT-004.** M2 MUST provide explicitly demanded saved-source PDF and PNG preview/export. Demand MUST name one exact resume_version_id and render_configuration_id under DRW-006; it MUST NOT follow a moving current pointer. A caller wanting the latest Resume first reads its current version and submits that exact ID. No MaterialBundle object/ID/API, CURRENT_RESUME mode, eager all-format rendering, forced rerender flag, user configuration CRUD or Preparation approval is introduced. MAT-003's Save-plus-intent obligation remains conditional for future actual consumers; SAV-017 closes the present exact-only interface. Q17/Q21/Q24/Q30/Q105.

<a id="mat-005"></a>
**MAT-005.** Materials MUST consume the internal source projection supplied by PRO-009, EVD-015 and RES-016, not a new persisted source authority:

| Field | Exact value |
| --- | --- |
| resume_version | Complete requested RES-002 immutable ResumeVersion |
| profile_version | Complete exact PRO-002 ProfileVersion referenced by that ResumeVersion |
| evidence_sources | Array in Resume section/member traversal order; each entry has exactly evidence_item_id: UuidV4, evidence_item_version_id: UuidV4, kind: EVD-001 enum, fields: corresponding complete EVD-003 shape |

The projection MUST derive Item.kind from its owner, preserve Item/version ownership and include each member even if its local content is empty. It MUST NOT copy Evidence.content, substitute current versions, create a MaterialSourceSnapshot ID/table or require validation of unused Evidence expression. It is transient execution data; a new attempt rereads the exact retained inputs. The existing full Candidate GET/Save validation obligations remain unchanged. Q1/Q67/Q69/Q74/Q89/Q96.

<a id="mat-006"></a>
**MAT-006.** After successful receipt replay has been ruled out, new demand MUST resolve the exact ResumeVersion and owning root, require that Resume to be ACTIVE, validate only actually required historical rendering inputs and then resolve/check the exact configuration under DRW-009. Historical resolvability alone is not new-demand eligibility. It MUST NOT require referenced Evidence roots/versions to remain ACTIVE/current or elevate lineage-only payloads into render dependencies. Rendered expression comes from Resume-local content; fixed contacts come from exact Profile and displayed structured facts from exact Evidence fields. An accepted exact demand MUST survive ordinary Resume removal/new Save, Evidence retirement or Profile/current-pointer movement; actual access, required-source availability and execution validity still apply. Q14/Q23/Q67–Q69.

<a id="mat-007"></a>
**MAT-007.** RenderManifest MUST be an immutable contained value of exactly one published Artifact, with these seven required non-null fields:

| Field | Type/value |
| --- | --- |
| schema_version | integer 1 |
| resume_id | UuidV4 |
| resume_version_id | UuidV4 |
| profile_version_id | UuidV4 |
| source_sections | Ordered array of the section projection below; may be empty |
| render_configuration_id | UuidV4 |
| artifact_id | UuidV4; its containing Artifact |

Each source_sections entry MUST contain exactly kind (RES-005/EVD-001 section enum) and evidence_refs (ordered array). Each evidence_refs entry MUST contain exactly evidence_item_id and evidence_item_version_id, both UuidV4. Existing Resume rules, including nonempty saved sections, remain applicable. No Manifest ID, separate update operation, source body or client-supplied provenance is allowed. Q2/Q6/Q8/Q11.

<a id="mat-008"></a>
**MAT-008.** The Manifest MUST be a deterministically derived provenance record, never a second source authority. Its Resume/root/Profile identities and section kinds/order/member reference order MUST exactly match the requested ResumeVersion; local empty content MUST NOT drop a member's ref. Its configuration and Artifact IDs MUST match the actual result. Clients MUST NOT supply or mutate provenance to change source identity. Source/target disagreement is integrity failure, not permission to reconstruct from current facts. Q1/Q2/Q6/Q116.

## 3. Immutable configuration and execution capability

<a id="mat-009"></a>
**MAT-009.** RenderConfiguration MUST be a retained immutable value with exactly six non-null top-level fields:

| Field | Type/shape |
| --- | --- |
| render_configuration_id | Fixed UuidV4 |
| schema_version | integer 1 |
| template | Exactly template_key and template_version, both strings |
| renderer | Exactly pipeline_key and pipeline_version, both strings |
| fonts | Four logical-font mappings under MAT-012 |
| output | One of the two closed objects below |

PDF output MUST be exactly {media_type: "application/pdf"}. PNG output MUST be exactly {media_type: "image/png", page_width_px: positive integer}. The request has no output_format, default configuration or alternate representation selector. The pipeline identifies the complete applicable layout/PDF/raster/assembly dependency path, not merely one library name. No assets array, Template/Renderer business ID, policy object or speculative asset field is introduced. Q3/Q7/Q13/Q21/Q57/Q64–Q66.

<a id="mat-010"></a>
**MAT-010.** template_key and pipeline_key MUST match ^[a-z][a-z0-9_]{0,63}$. template_version and pipeline_version MUST match ^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$. Strings MUST compare exactly without trim/case conversion; versions need not be SemVer. Configuration equality compares complete validated values, ignoring JSON object-key ordering/formatting. Same ID/equal values permits repeated registration; same ID/different values MUST reject overwrite. Equal values with distinct IDs MUST remain distinct: canonical equality is not identity or a cross-ID compatibility policy. No configuration fingerprint is added. Output-affecting template layout changes MUST advance template_version and configuration identity; output-affecting pipeline implementation or dependency changes MUST advance pipeline_version and configuration identity. An implementation MUST NOT change the output-affecting meaning behind an unchanged descriptor. Q3/Q9/Q58/Q64/Q65/Q75/Q103.

<a id="mat-011"></a>
**MAT-011.** The application-delivered catalog MUST assign stable configuration IDs and concrete template/pipeline versions, font-file hashes and PNG width. Content changes require a new ID while old snapshots remain retained. Registration MUST follow STO-032 before request handling/workers; a legal record MUST be registered even when its dependencies are missing, with can_generate false. Runtime dependency loss alone MUST NOT disable unrelated startup/Candidate APIs/retained Artifact reads. Same-ID conflicts, corrupt records or missing historically referenced configurations are integrity failures, not absent optional dependencies or permission for catalog repair. Catalog values MUST NOT silently change Contract semantics or grant synthesis. Q13/Q18/Q58/Q102/Q113/Q134.

<a id="mat-012"></a>
**MAT-012.** *(Scoped user-approved amendment: 2026-09-23; see CG04-FONT-20260923.)* fonts MUST contain exactly SOURCE_HAN_SANS, HEITI, SONGTI and KAITI. Each map MUST contain exactly regular, bold, italic and bold_italic, identifying logical rendering roles rather than requiring four native faces. Each value is the Common Sha256Hex of the final registered single-face static TTF/OTF artifact supplying that role. Verify the actual final files against these hashes; no collection index, variable axes, host fallback or guessed role from an unordered hash set is allowed.

The approved mappings are: SOURCE_HAN_SANS = Source Han Sans SC 2.005R, official Regular/Bold with deterministic Italic/BoldItalic synthesized respectively from those upright faces; HEITI = Sarasa Gothic SC, official Regular/Bold/Italic/BoldItalic faces from one fixed release; SONGTI = Source Han Serif CN, official Regular/Bold from one fixed release with deterministic Italic/BoldItalic synthesized respectively from those upright faces; KAITI = LXGW WenKai 1.522, official Regular for regular and official Medium for the logical bold role, with deterministic Italic/BoldItalic synthesized respectively from Regular/Medium. The Medium mapping MUST NOT be described as native Bold or synthetic bold.

Concrete family/release, original face/hash, role mapping, synthesis path/parameters/dependencies and final artifact/hash MUST be fixed and auditable under the configuration's pipeline version. Newly synthesized font files MUST respect their distribution licenses. No runtime font substitution, synthetic bold, other family substitution, null role or additional synthesis mechanism is authorized. This scoped user-approved amendment supersedes Q135's two-hash omission and its restriction against synthesis for the other three logical fonts; HEITI continues to use native faces. See [CG04-FONT-20260923](../../.grill/contract/sl-02-m2/decisions.md#cg04-font-20260923). Q59/Q99/Q101/Q106/Q135.

<a id="mat-013"></a>
**MAT-013.** can_generate MUST describe current capability separately from immutable configuration. True requires support for all four logical fonts and approved style roles, plus dependencies actually used by that configuration's output. Missing PNG-only raster dependencies need not disable an otherwise supported PDF configuration sharing the pipeline version. For MAT-012's approved role mappings, the corresponding configuration MUST NOT claim true before the final pipeline has passed actual PDF/PNG, pagination and permitted mark-combination verification. This design authorization is not that evidence. True is a point-in-time capability observation, not source admission or a guarantee for every glyph; POST performs its own checks. Loss of current new-generation support MUST NOT invalidate already correct completed bytes eligible for fenced publication under DRW-014. Q18/Q47/Q50/Q68/Q102/Q129/Q130/Q135.

## 4. Artifacts, reuse and representation

<a id="mat-014"></a>
**MAT-014.** Artifact MUST have exactly seven required non-null fields:

| Field | Type/value |
| --- | --- |
| artifact_id | UuidV4 |
| schema_version | integer 1 |
| manifest | MAT-007 RenderManifest |
| media_type | application/pdf or image/png, matching configuration.output |
| byte_length | Exact integer 1–9007199254740991; actual persisted complete file length |
| sha256 | Sha256Hex of the actual complete persisted bytes |
| created_at | UtcTimestamp under DRW-012 |

No mutable readiness/status, payload path, download URL or updated_at is added. Operational output caps are separate from this structural byte_length range. Q4/Q16.

<a id="mat-015"></a>
**MAT-015.** Artifact identity MUST be independent of its byte hash. Equal bytes MUST NOT merge lineage, creating Work, receipts or readiness identities; underlying content deduplication MAY preserve those identities. An Artifact exists externally only after successful publication; reserved internal IDs and precommit files MUST NOT be readable, referenceable or represented as already existing Artifacts. Each newly published Artifact has exactly one creating successful Work under DRW-004. Q4/Q8/Q12/Q111.

<a id="mat-016"></a>
**MAT-016.** Reuse MUST require the same exact resume_version_id and render_configuration_id, applicable access and verified readable complete bytes matching length/hash. Consider candidate Artifacts by created_at ascending, then canonical artifact_id ascending; select the first eligible candidate. Missing/corrupt payload permits trying another candidate, then compatible unfinished Work, then new Work. Required malformed metadata, broken refs or contradictory lineage MUST fail with INTERNAL_ERROR rather than masquerade as a cache miss. Current execution limits for new Work MUST NOT become historical Artifact compatibility criteria. Verification does not promise permanent availability; new-demand admission still precedes reuse. Q9/Q25/Q37/Q71/Q115/Q118.

<a id="mat-017"></a>
**MAT-017.** Published Artifacts and their immutable metadata MUST be retained for the Workspace lifetime in this first scope: no deletion command, TTL or automatic published-payload GC is introduced. Ordinary Resume removal/configuration upgrade MUST NOT delete them. This retention rule is not a guarantee against physical loss/corruption. Existing fulfillment and original receipts MUST remain unchanged when payload later becomes unavailable. Unpublished temporary/orphan cleanup follows Storage separately. Q10/Q51/Q72/Q92/Q119.

<a id="mat-018"></a>
**MAT-018.** PDF and PNG MUST share complete A4 layout, content order and pagination for the same Resume and matching schema_version/template/renderer/fonts values. A4 is 210 × 297 mm on every PDF page; no other page size or automatic page scaling is permitted. The template MUST produce at least one page, including a legally empty Resume, without adding invented facts or a completeness gate. PDF is a normal multi-page document. PNG MUST join every complete page vertically into one opaque-white long image, preserving all page margins, with no added gap/shadow/border, cropping, page loss, stretching or reflow.

For configured integer width w, each page's raster height MUST be floor(w × 297 / 210 + 0.5), computed exactly; total PNG height is that height times page count. Layout pairing adds no group ID and permits no cross-configuration Artifact reuse. PDF numerical serialization tolerance and concrete shipped PNG width belong to verified pipeline/catalog evidence, not an arbitrary fixed 0.01 pt business bound. Q30/Q31/Q36/Q46/Q61/Q90/Q100/Q114.

<a id="mat-019"></a>
**MAT-019.** Rendering MUST preserve Resume section/member/block/run order, local text and permitted marks/combinations. Preserve saved spaces including ASCII/NBSP/full-width spaces; do not trim, normalize Unicode, collapse HTML whitespace or interpret Markdown. Normal overflow MUST wrap/paginate without shrinking saved font size/line height, clipping or truncating; fixed pipeline rules handle long unbreakable text. Each ORDERED_LIST starts at 1, continues numbering across pages, and splitting one item MUST NOT create a new number; a new list restarts. Fixed template mappings own structured labels/date formats/null meanings and MUST NOT depend on host locale, alter facts or import Evidence expression. Distinguish absent end month from unknown start month under EVD-005. Exceeding applicable limits fails explicitly. Q62/Q69/Q97/Q98/Q123.

<a id="mat-020"></a>
**MAT-020.** PDF MUST preserve clickable behavior only for exact LINK targets already admitted in ResumeVersion under RES-006/008 and COM-042; Materials MUST NOT expand URL schemes or add clickable targets from unrelated text/structured fields. PNG preserves visible link text/styling without interaction or appended URL text. Rendering MUST NOT fetch URLs. PDF MUST embed used fonts (lawful subsetting is allowed) and retain textual body content rather than whole-page screenshots; no external ATS result is promised. Unsupported visible glyphs MUST fail OUTPUT_INVALID instead of publishing boxes, blank replacement or dropped text. Q59/Q70/Q93.

<a id="mat-021"></a>
**MAT-021.** Rendering MUST use admitted exact sources, the fixed template and configuration-specified local font inputs without network access, arbitrary paths, executable user HTML/script or system-font substitution. The renderer MAY produce attempt-scoped candidate bytes or a controlled temporary file. It MUST NOT publish Artifact metadata, mutate Work or finish Intents; the Coordinator owns validation, fencing and publication. Trusted in-process execution is not automatically an OS sandbox or a killable process. Q60/Q80/Q83/Q84.

<a id="mat-022"></a>
**MAT-022.** Before publication, validate actual candidate bytes and required format/constraints: parseable complete unencrypted PDF with at least one A4 page; or a fully decodable PNG with the required page-assembly dimensions. PDF MUST contain no scripts, automatic execution actions, forms, embedded attachments or external-program launch actions; only MAT-020's admitted link interaction is supported. Verify applicable page/pixel/byte/time limits without unbounded validation allocation: inspect sizes when available and enforce limits throughout processing. Confirmed excess is RESOURCE_LIMIT_EXCEEDED; malformed/invalid output is OUTPUT_INVALID. Format/hash checks alone MUST NOT be presented as proof of full visual/text semantics. Fixed-pipeline conformance tests establish body/mark/pagination/link/field-mapping behavior; per-publication reverse extraction/character-by-character PDF comparison is not required. Q63/Q121/Q122/Q128.

<a id="mat-023"></a>
**MAT-023.** Output MUST conform to its exact source/configuration, but equal inputs MUST NOT imply guaranteed byte-for-byte repeated serialization. Each Artifact hash records its actual bytes, not a Resume/configuration business fingerprint. The runtime MUST NOT silently reduce PNG width, font size, line height or output completeness to meet Work limits. Q4/Q73/Q91.

## 5. Read and content HTTP surface

<a id="mat-024"></a>
**MAT-024.** GET /api/v1/render-configurations MUST return 200 with exactly {items: [...]}; each item is exactly {configuration: MAT-009 value, can_generate: boolean}, non-null, and the list includes only currently true entries ordered by canonical configuration ID. Empty availability returns an empty array. GET /api/v1/render-configurations/{render_configuration_id} MUST return 200 with the same single-item envelope for retained exact configurations, including can_generate false. No user configuration-write route exists. Both reads are pure and use DRW-022/023 HTTP rules. Q13/Q47/Q50.

<a id="mat-025"></a>
**MAT-025.** GET /api/v1/artifacts/{artifact_id} MUST return 200 with the complete MAT-014 value for a published retained Artifact after access/metadata integrity checks, even when payload is unavailable. Unpublished IDs are not readable. Reads MUST NOT generate demand, rerender, repair data, update readiness or substitute a different Artifact. Metadata success is not a byte-availability promise. Q12/Q20/Q51.

<a id="mat-026"></a>
**MAT-026.** GET /api/v1/artifacts/{artifact_id}/content MUST accept only optional disposition=inline|attachment, default inline. Both variants send the same original bytes from a stable complete snapshot verified against immutable length/hash before success headers/body; do not verify a path and reopen different bytes. Bounded buffers or controlled temporary snapshots MAY implement this under STO-035.

Successful responses MUST use full HTTP 200, Content-Type matching media_type, Content-Length equal to byte_length, Cache-Control: no-store and Content-Disposition carrying the selected value and filename artifact-{artifact_id}.pdf or .png. Ignore Range rather than produce 206; Accept-Ranges: none is optional. No cache validators, dynamic gzip/transcoding/re-encoding or content conversion are introduced; Content-Encoding is absent or identity. A network interruption is not prevented by prior integrity checking. Q52/Q55/Q56/Q132.

<a id="mat-027"></a>
**MAT-027.** Content errors MUST use COM-029 with empty field_errors when not field-specific: missing requested metadata uses 404 NOT_FOUND; retained metadata with missing payload uses 409 ARTIFACT_UNAVAILABLE; byte length/hash mismatch uses 500 ARTIFACT_INTEGRITY_FAILED; temporary storage-read failure uses 503 STORAGE_UNAVAILABLE; detected malformed required metadata uses 500 INTERNAL_ERROR. These failures MUST NOT rewrite Intent, receipt or Artifact state or trigger regeneration. Other path/query/access rules remain DRW-022/023. Q77/Q78/Q115.

<a id="mat-028"></a>
**MAT-028.** Clients MUST distinguish accepted demand, terminal fulfillment, Artifact metadata and actual content availability. Use DRW-024 to handle uncertain command outcomes and out-of-order Intent responses; show content-read failure separately from immutable fulfillment. A newer current Resume, ordinary removal or changed configuration capability MUST NOT relabel an old Artifact as a newer document, rewrite its result or conceal readable history. Saved-source preview and download consume Artifact bytes; editor-local Draft preview remains RES-015's separate non-authoritative surface. Q5/Q10/Q17/Q20/Q23/Q39/Q51/Q104/Q119.

<a id="mat-029"></a>
**MAT-029.** The public M2 surface MUST be limited to the six operations in DRW-006/021 and MAT-024–026. No Work management, history-list, retry, repair, cancel, MaterialBundle or configuration-write API is created by internal persistence needs. A user-requested new generation after terminal failure uses a new render command; successful command replay is not retrying Work. Q24/Q105/Q120.

## 6. Execution evidence boundary

<a id="mat-030"></a>
**MAT-030.** Concrete catalog files, font rights/distribution, logical-font mappings, glyph/mark combinations, template field/label/wrapping behavior, PDF embedding/text extraction, PDF serialization tolerance, PNG assembly and practical execution/default limits MUST have explicit engineering evidence before the corresponding execution capability is declared usable. Research that needs a new source substitution/synthesis/output semantic exception MUST return to its Contract owner; implementation defaults MUST NOT silently supply authority. This normative publication itself supplies no installed renderer, font assets, runtime test, migration or frontend acceptance. Q99/Q100/Q123/Q128/Q134/Q135.

## 7. Independent Resume material source

Scope revision **2026-09-24.S2M1S1-r1**. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="mat-031"></a>
**MAT-031.** The complete exact schema-2 ResumeVersion MUST be the sole candidate source of rendered materials: owned contacts, Header, ordered sections/entries/fields/canonical text and presentation. No independent Profile/Evidence version joins, portrait readiness, default identity or semantic model input is a render prerequisite. Rendering does not read generated capability text. Logical entry/block IDs are provenance, not visible output. RES-018–023 value/AST rules and existing renderer layout/privacy/link behavior apply.

<a id="mat-032"></a>
**MAT-032.** RenderManifest schema_version MUST be 2 and contain exactly schema_version, resume_id, resume_version_id, render_configuration_id and artifact_id. Derive all values server-side from the exact accepted source/configuration/publication. No profile_version_id or Evidence source_sections remains. Artifact retains MAT-014’s seven fields with schema_version:2 and this manifest. Source/configuration/Artifact ownership must agree; a manifest cannot override content. Old-model data is reset under STO-054, not served through fake schema-2 lineage.

<a id="mat-033"></a>
**MAT-033.** New demand still requires an ACTIVE owning Resume; accepted exact demand and published historical material survive ordinary removal/new versions/default/portrait changes. Reuse requires exact ResumeVersion/configuration and verified bytes under MAT-016. Preview/download, Preparation selection, viewed-material confirmation and execution consent MUST NOT be retargeted or invalidated solely by default switch/portrait rebuild. Keep Draft preview separate from saved-source artifacts and material readiness separate from Save/portrait success.
