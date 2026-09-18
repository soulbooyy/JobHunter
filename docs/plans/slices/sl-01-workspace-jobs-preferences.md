# SL-01 Local Workspace, Manual Jobs and Preferences

> English is authoritative. This Slice plan is part of the Implementation Plan category and has completed W7 document review; user baseline approval remains pending. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Provide a useful local Job Pool and explicit search intent without requiring model calls or recruiting-site access.

**Scope:** Workspace/navigation responsibilities for delivered entry points; Manual Job roots including no-JD cases, complete immutable JobVersions, local browsing and Company read view, global hard Preferences, deterministic metadata-only QuickScreen, explicit observation/current-history distinctions. Introduce local identity/reference/persistence and privacy requirements only for these consumers.

**Out of Scope:** BOSS access, Requirement parsing, Fit, Resume editing, application execution and new bookmark/search-profile features. Undelivered entry points cannot appear implemented.

**Already-decided capabilities and provenance:** Q1, Q6–Q8, Q12–Q13, Q17, Q44–Q45, Q48, Q50, Q53, Q55–Q56, Q110, S5.1, S17.1–S17.3, S9.1. Actual behavior/mechanism owners: [P2](../../spec.md#2-workspace-and-task-organization); [P4](../../spec.md#4-jobs-preferences-and-collection); [A3](../../architecture.md#3-authority-identity-and-evolution); [A4](../../architecture.md#4-jobs-screening-collection-and-platform-access). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F05, F10.

**Test / Eval categories:** Local persistence and source-identity checks, Manual root versus complete-version admission, metadata-only screening, uncertainty, latest local Preferences without remote fetch, read-view consistency and minimal diagnostics. Required proof destinations: [V3](../../acceptance.md#3-workspace-jobs-screening-and-collection); [V10](../../acceptance.md#10-privacy-storage-and-honest-history). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-01.M1](#sl-01m1-local-workspace-and-manual-job-authority), [SL-01.M2](#sl-01m2-hard-preferences-and-local-screening). Dependencies are implemented components, not completion of upstream parents.

## SL-01.M1 Local Workspace and Manual Job authority

**Goal/value:** Make a local Job Pool usable before remote or model integration.

**Scope:** Local Workspace configuration; Manual roots with or without JD; complete immutable JobVersions; source identity, observations, honest availability/history, flat Job and Company read views, and delivered navigation.

**Out of scope:** Preferences screening is M2; platform acquisition and application history are separate consumers.

**Required upstream capability:** None.

**Reused component/infrastructure:** None; select the actual minimal local setup during implementation preparation.

**Required Contract portions before development:** `workspace.md` — local initialization/configuration; `jobs-screening.md` — Manual admission, complete versions, observations and local views. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Common identity/history and storage privacy agree with Manual-root versus complete-version admission. Later BOSS admission must reuse JobVersion meaning without removing the Manual exception.

**Research / unresolved Grill detail:** Select and verify the minimum local persistence, UI and checking setup; no bootstrap or full stack is selected by this plan.

**Tests / Eval:** V3, V10: identity/admission, missing JD, persistence, honest observations and read-view consistency. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real local maintenance and reads preserve exact history and distinguish missing content from unavailable Jobs. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-01.M2 Hard Preferences and local screening

**Goal/value:** Filter local opportunities by explicit search intent without paid inference or site access.

**Scope:** One global hard Preferences version and deterministic metadata-only QuickScreen; latest local filters/views independent of any frozen collection input.

**Out of scope:** Requirement parsing, Candidate data, soft model judgments and saved search-profile products.

**Required upstream capability:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-job-authority) — persisted Job metadata and local views

**Reused component/infrastructure:** [SL-01.M1](#sl-01m1-local-workspace-and-manual-job-authority) — local persistence/reference handling

**Required Contract portions before development:** `preferences.md` — hard intent and immutable versions; `jobs-screening.md` — deterministic screening, uncertainty and temporary views. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Preferences authority versus view filters; screening consumes Job metadata only. Collection later translates a frozen version and must not replace current local filtering.

**Research / unresolved Grill detail:** Resolve required metadata and missing-input behavior in Contract Grill; numeric/default policy is not inferred.

**Tests / Eval:** V3: deterministic predicates, unknown metadata, no Candidate/Requirement/model access, immediate local refiltering. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Real screening uses current local intent without remote fetch or a second screening authority. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** A user can maintain local Manual Jobs and Preferences through the real boundary, with honest missing JD/unknown availability and persistent exact history. Screening neither calls a model nor acquires Candidate/Requirement authority. Required deterministic evidence and mappings exist. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover local persisted Jobs with current Preferences/read views. Parent completion is separate from rollout/production enablement.
