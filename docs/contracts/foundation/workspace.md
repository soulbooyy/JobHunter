# Workspace Contract — Local M1 Startup and Navigation

> **Current applicability — 2026-09-24.S2M1S1-r1.** WSP-008–011 initialization, final-removal and replacement-selection clauses are superseded by WSP-013–015. Local placement, exclusive ownership, loopback and Host/Origin admission survive. The new requirements below are the normative replacement for that scope. Earlier text/IDs remain historical provenance, not a legacy implementation requirement. [Accepted decisions](../../design/contract/sl-02-m1-supplement-grill.md); [current review](../../progress/traceability.md#67-sl-02m1-supplement-reviewed-scope).

> English is authoritative. Normative scope revision: **2026-09-19.M1-r1**. Scope: SL-01.M1 local startup, access and delivered navigation. Resume defaults and later Workspace capabilities remain outside this scope. [Progress](../../progress/traceability.md#6-contract-normative-scope-readiness-ledger) records readiness separately.

[Index](../index.md) · [Common](../common.md) · [Entry](../jobs/manual-application-entries.md) · [Storage](storage.md) · [Decisions](../../design/contract/sl-01-m1-grill.md)

## 1. Workspace meaning and initialization

<a id="wsp-001"></a>
**WSP-001.** M1 MUST provide one default local Workspace for one user, without a Candidate/tenant aggregate, Workspace business table or create/switch/manage-multiple-Workspaces UI. Entry maintenance MUST NOT require Profile, Resume, Preferences, models or formal Jobs. `data_directory` is Storage/infrastructure configuration, not Workspace identity.

<a id="wsp-002"></a>
**WSP-002.** Startup MUST resolve/fix physical placement under STO-001, acquire exclusive runtime ownership under STO-002, determine first-use eligibility under WSP-003, initialize or open under STO-005/006, and complete required checks before announcing readiness or listening for business requests. It MUST NOT silently fall back to a different directory or empty store. The ownership guard remains held while the backend runs; multiple browser pages use ordinary Entry revision admission.

<a id="wsp-003"></a>
**WSP-003.** First initialization MUST follow this decision table. Workspace owns eligibility; Storage owns recognition/completeness/compatibility and errors.

| Selected directory at startup | Behavior |
| --- | --- |
| Default directory absent | May create it with appropriate permissions, then initialize |
| Explicitly configured directory absent | Fail; do not create it or fall back |
| Existing directory completely empty | Treat as first use; initialize |
| Existing directory nonempty | Open only complete recognized supported JobHunter storage; never infer first use from missing database |
| Directory inaccessible or unwritable | Fail explicitly |

Hidden files count toward nonemptiness. Runtime lock coordination MUST NOT introduce files that change this classification. If the user previously removed every item from a directory, the application cannot infer that history; the now-empty directory is eligible for initialization. No forensic recovery capability is promised.

<a id="wsp-004"></a>
**WSP-004.** Startup success/failure MUST use STO-011 diagnostic semantics. Failed initialization/opening MUST terminate startup with nonzero exit status before the business listener starts. Corruption, missing required content, unsupported schema and interrupted initialization MUST NOT be presented as an empty successful Workspace. `LocalStartupResult` MUST NOT be persisted or exposed as an HTTP business resource. A live runtime failure likewise MUST NOT substitute another data store.

## 2. Navigation and local runtime

<a id="wsp-005"></a>
**WSP-005.** The local browser frontend MUST expose the ManualApplicationEntry view through a Job Pool button and keep it separate from formal Jobs and formal Company aggregation. It MUST support the actual delivered create/read/edit/delete/open operations defined by the Entry Contract. Undelivered formal Job or analysis functions MUST NOT appear available merely because navigation exists. Workspace navigation MUST NOT become a second owner of Entry content or reinterpret ordinary opening as execution/application history.

<a id="wsp-006"></a>
**WSP-006.** The backend MUST bind only loopback in M1; the frontend runs in a browser. Runtime admission MUST validate configured local Host and browser Origin before business handling, reject unknown Host/Origin, and MUST NOT grant wildcard cross-origin business access. The actual frontend origin, backend port and any development proxy are fixed startup configuration; `localhost`, IPv4 and IPv6 aliases are allowed only when explicitly configured rather than inferred from untrusted headers.

Browser-origin requests MUST match the local application allowlist. Non-browser requests without Origin MAY be accepted through the validated loopback Host boundary; this does not authorize arbitrary browser origins. JSON command requests MUST use `application/json`; form/text submissions do not bypass admission. Host/Origin rejection MUST perform no business command and return HTTP 403 with COM-029 `code: ACCESS_DENIED` and empty `field_errors`; malformed/non-JSON transport uses Entry's `BAD_REQUEST`. Error text MUST NOT echo supplied header values. No login/account system, network-facing deployment or general remote API is introduced. Browser handoff follows MAE-013, including final opener/referrer properties.

## 3. Interface agreement and exclusions

WSP-002/003 consumes STO-001/002/005/006 without owning database metadata. WSP-004 consumes STO-011 without creating a Workspace resource. WSP-005 consumes MAE-009–017 without creating formal Job eligibility. WSP-006 owns runtime access rejection; MAE-016 owns business-operation error codes. The Common error shape is shared, not redefined.

Provenance: CG01-BC1, Q19, Q24–Q26, Q38, Q43–Q45. Future Resume default-selection scope remains pending. No requirements are retired in this initial revision.

## 4. M2 local runtime applicability

Scope revision **2026-09-20.M2-r1**; WSP-001–006 remain preserved M1 clauses.

<a id="wsp-007"></a>
**WSP-007.** M2 MUST retain WSP-001's single-user/single-default-Workspace meaning and Entry independence, WSP-002/003's fixed placement/exclusive ownership/first-use admission, WSP-004's fail-before-listening/no-default-on-corruption guarantees and WSP-006's loopback/Host/Origin boundary. For the schema-2 consumer only, startup's schema/diagnostic references in WSP-002/004 are superseded by STO-014–019; no runtime auto-upgrade is authorized. Preferences routes MUST apply the same local Host/Origin admission and ACCESS_DENIED shape; PRF-016 owns M2's compatible application/json parameter handling and stricter body admission. M1 Entry parser behavior is not retroactively broadened. Workspace initialization and migration MUST NOT create Preference roots or versions. LocalStartupResult remains a non-persisted startup diagnostic, never a business resource. Preferences UI behavior is owned by PRF-022, without turning navigation into another configuration authority.

## 5. SL-02.M1 initialization and default selection

Scope revision **2026-09-21.S2M1-r1**. WSP-001–007 remain preserved for their original consumers.

<a id="wsp-008"></a>
**WSP-008.** S2 MUST retain WSP-001's single-user/single-default-Workspace meaning and Entry independence, WSP-002/003 placement/exclusive ownership/first-use admission, WSP-004 fail-before-listening/no-repair and WSP-006 configured loopback Host/Origin admission. For the S2 binary only, STO-021–028 supersedes the schema-1/2 target/diagnostic applicability in WSP-002/004/007; existing migration history is preserved. S2 transport follows SAV-012/013, not a retroactive SL-01 parser change. LocalStartupResult remains a non-persisted startup diagnostic. Initialize real Profile, Baseline and selection through their owners, without creating a Resume or lazy Preferences. Baseline pointer ownership stays EVD-009, regardless of physical config-row placement. (Q49/Q55/Q93/Q96.)

<a id="wsp-009"></a>
**WSP-009.** DefaultResumeSelection MUST be a small Workspace-owned object containing exactly default_resume_id: UuidV4 or null and revision: Revision. It MUST have exactly one durable current value, initially null/revision 1. No heavyweight aggregate, generic config framework, history Version or business ID is added. null corresponds to no ACTIVE Resume before first creation; with ACTIVE Resumes it MUST reference an ACTIVE Resume. Selection revision MUST detect ABA changes, independently of all Resume root revisions. (Q72.)

<a id="wsp-010"></a>
**WSP-010.** The first successful ACTIVE Resume creation MUST atomically change selection from null/revision 1 to that Resume/revision 2. Create MUST NOT require a caller selection revision: another concurrently prepared creation may succeed while observing and preserving the already-established default, subject to normal capacity/source admission. On receipt miss under SAV-003, explicit set-default MUST first admit its expected selection revision, then require an ACTIVE target; matching same target is UNCHANGED, stale revision conflicts even after ABA. Real switch increments once; unrelated Resume rename/document changes do not advance selection or publish Versions. Required increment overflow rejects the whole command; valid no-op remains legal. (Q72/Q76/Q84.)

<a id="wsp-011"></a>
**WSP-011.** Remove MUST atomically apply SAV-007 target/selection revision and lifecycle-no-op order. An ACTIVE non-default target requires replacement_resume_id=null and leaves selection unchanged. An ACTIVE default target requires a different ACTIVE replacement; removing the final ACTIVE Resume is forbidden. The frontend MUST use RES-014 list order observed for the confirmation dialog, choose the next ACTIVE item or otherwise previous, and explicitly show that exact replacement before sending its ID. It MUST NOT demand manual replacement selection. Backend MUST NOT choose a different replacement after races; replacement name/document changes alone do not require a replacement-root revision, and list insertion alone does not trigger recalculation. Default removal increments selection once together with root removal; no document Version/source adoption follows. A matching already-REMOVED no-op ignores present selection/replacement eligibility after syntax/receipt/target revision. (Q70–Q72/Q76.)

## 6. SL-02.M2 runtime applicability

Scope revision **2026-09-21.S2M2-r1**. Earlier published consumer semantics remain effective within their scope. Provenance: [CG04](../../design/contract/sl-02-m2-grill.md).

<a id="wsp-012"></a>
**WSP-012.** SL-02.M2 MUST retain WSP-001–004/006's single local user, placement, first-use, exclusive physical-directory ownership and configured loopback Host/Origin boundaries. STO-029–039 supplies the M2 binary's schema/registration applicability, superseding only older literal target-version references for that binary; no automatic migration is authorized. Its six Materials/Derived Work operations use DRW-022 transport, not SAV-012's no-query rule for the content operation or changed SL-01 parsing. Missing render dependencies MUST leave otherwise healthy startup and unrelated delivered APIs usable; configuration/persistence integrity failures remain explicit under STO-032/038. No new Workspace identity, login, general remote API or runtime-lock/lease authority is introduced. Q102/Q107/Q113/Q120/Q127.

## 7. Independent documents and current portrait selection

Scope revision **2026-09-24.S2M1S1-r1**. Provenance: CG03S1-BC1–BC3 and effective Q6–Q41; Q24 is superseded by Q38/Q41.

<a id="wsp-013"></a>
**WSP-013.** Workspace MUST own exactly one DefaultResumeSelection {default_resume_id: UuidV4|null, revision: Revision}, initially null/revision 1. No Candidate root/account/aggregate is added. null means no ACTIVE Resume, including after final removal; it is not restricted to revision 1. First creation while null selects that created Resume atomically and increments the then-current selection revision. Concurrent later creation preserves the established selection. No Profile root or EvidenceBaseline is seeded.

<a id="wsp-014"></a>
**WSP-014.** Set-default MUST check expected selection revision before equality and require an ACTIVE target. Same target is UNCHANGED and does not implicitly refresh; real change increments once and commits SAV-021’s new current build obligation. Default selection commits without waiting for a model. Save of its current document advances portrait source without changing selection revision; non-default Save/rename does not. Source and current-build identity together fence publication, including A→B→A.

<a id="wsp-015"></a>
**WSP-015.** Default removal with other ACTIVE Resumes MUST name a different ACTIVE replacement. The dialog MUST preselect the next Resume in RES-014 canonical list order, otherwise previous, and allow manual replacement selection; show the selected source change before confirmation. Backend MUST validate the submitted replacement and selection revision atomically, never silently choose another. Final removal MUST accept replacement_resume_id=null, clear default and current portrait, and increment selection once. Non-default removal requires null replacement and leaves selection unchanged. SAV-007’s receipt/target-revision/already-removed no-op precedence survives; LAST_RESUME_REQUIRED is retired. Ordinary removal retains exact history and is not physical erasure.
