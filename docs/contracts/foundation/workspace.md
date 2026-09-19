# Workspace Contract — Local M1 Startup and Navigation

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
