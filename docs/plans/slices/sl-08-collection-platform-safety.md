# SL-08 BOSS collection and shared platform safety

> English is authoritative. This Slice plan is part of the Implementation Plan category and completed W7 review in its earlier form. Its affected scope/dependencies now reflect user-approved [CG01-BC1](../../design/contract/sl-01-m1-grill.md#cg01-bc1); scoped review is recorded in Progress. See [Progress](../../progress.md) for current review state. It does not establish Contract readiness, implementation or acceptance. Its 2 milestones remain in this document.

[Documentation index](../../index.md) · [Slice index](README.md) · [Global Implementation Plan](../implementation-plan.md) · [Actual Progress](../../progress.md)

The [global readiness and dependency rules](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) apply to every entry below. This file owns this Slice's detailed scope, required upstream capability, reused infrastructure, conditional integration, Contract portions and completion conditions. Product/Architecture/Acceptance retain their existing authority; actual readiness and evidence belong to Progress. Edit this file for local planning changes; reconcile other owners only when their real scope, shared interfaces, dependencies or evidence are affected.

**Goal and business value:** Acquire eligible complete Jobs without unnecessary detail access or unsafe platform activity, and establish safety shared with later execution.

**Scope:** User-authorized initial/explicit collection and refresh; metadata screening before full details, complete Job+version admission, local browsing, aggregate rejection audit, exact source observations, frozen collection Preferences versus latest local filtering; stop/partial results and persistent account/platform safety with explicit strong-risk restoration.

**Out of Scope:** Requirement parsing as part of collection, model-autonomous browsing, recoverable rejected-content datasets, cross-platform merge, background polling/Monitor, cooldown-only strong-risk reset, default numeric quotas.

**Already-decided capabilities and provenance:** Q3, Q27, Q44–Q45, Q48–Q50, Q55–Q56, Q110, Q122, Q160–Q161, Q164, S9.1. Actual behavior/mechanism owners: [P4](../../spec.md#4-jobs-preferences-and-collection); [P8.2](../../spec.md#82-batch-behavior-and-shared-platform-safety); [A4](../../architecture.md#4-jobs-screening-collection-and-platform-access); [A8](../../architecture.md#8-preparation-execution-and-application-events); [A12](../../architecture.md#12-durable-execution-and-recovery); [A13](../../architecture.md#13-storage-retention-and-audit); [A15](../../architecture.md#15-eval-and-observability). These Q-IDs support the capabilities and exclusions; milestone placement/order is this plan's proposed delivery arrangement.

**Dependent Contract families:** F01, F02, F05, F10, F11.

**Test / Eval categories:** No detail fetch on definite rejection, no rejected-content persistence, strict complete formal Job admission and ManualApplicationEntry isolation, local changes without fetch, mid-collection Preferences edits and cancellation, risk persistence/restart, ordinary failure versus strong risk and no implicit execution permission after restoration. Required proof destinations: [V3](../../acceptance.md#3-workspace-jobs-screening-and-collection); [V7](../../acceptance.md#7-preparation-execution-platform-safety-and-application-history); [V9.2](../../acceptance.md#92-crash-and-cancellation-boundaries); [V10](../../acceptance.md#10-privacy-storage-and-honest-history); [Eval acceptance 2.1](../../acceptance/evaluation.md#21-isolation-exact-inputs-and-declared-experiment-scope). These are future obligations, not existing tests or results.

**Upstream and required Contracts:** See the independent entries below and [global Plan 4](../implementation-plan.md#4-contract-document-and-joint-interface-map). Required parent milestones: [SL-08.M1](#sl-08m1-shared-recruiting-platform-safety), [SL-08.M2](#sl-08m2-boss-collection-and-explicit-refresh). Dependencies are implemented components, not completion of upstream parents.

## SL-08.M1 Shared recruiting-platform safety

**Goal/value:** Make recruiting access subject to one persistent risk and capacity authority.

**Scope:** Shared platform/account admission, persistent strong-risk blocking and explicit restoration interface consumable by Collector and Executor.

**Out of scope:** Actual collection/execution, cooldown-only unblock, consent to send, mandatory Monitor and assumed numeric quotas.

**Required upstream capability:** None.

**Reused component/infrastructure:** [SL-03.M1](sl-03-invocation-requirements.md#sl-03m1-invocation-durability-and-recovery-foundation) — applicable invocation outcome persistence/recovery primitives; platform risk policy stays local to its owner

**Required Contract portions before development:** `jobs/platform-safety.md` — capacity/risk/block/restoration; `agent/execution-runtime.md` — applicable access outcome evidence; `foundation/storage.md` — retained risk and diagnostic privacy; `evaluation/evaluation-observability.md` — controlled shared-safety checks. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Define the necessary Collector/Executor-facing admission/outcome agreement now without requiring either full workflow. Safety restoration never creates ExecutionApproval.

**Research / unresolved Grill detail:** Research actual platform/session/risk surfaces before required detail; no live account access is performed by planning.

**Tests / Eval:** V3, V7, V9.2, V10: controlled shared admission, risk persistence across restart, explicit restoration and no implicit consent. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Both intended consumer interfaces can use one verified safety component; no successful collection or sending is claimed. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

## SL-08.M2 BOSS collection and explicit refresh

**Goal/value:** Populate useful local Jobs under user-selected acquisition scope and shared safety.

**Scope:** First formal Job producer: canonical identity, complete immutable JobVersion admission, exact history/persistence, formal Job and Company local read views; frozen Preferences/search translation, two-stage transient screening, source observations/freshness, aggregate audit, stop/partial results and explicit refresh. Integrate newest-Preferences local filtering independently of frozen collection inputs. All formal Job semantics are defined by `jobs/jobs-screening.md`; this milestone implements and consumes them rather than owning them.

**Out of scope:** Rejected-content persistence, cross-platform merge, background Monitor, Candidate-based QuickScreen, and collection success as execution consent.

**Required upstream capability:** [SL-01.M2](sl-01-workspace-jobs-preferences.md#sl-01m2-hard-preferences-and-pure-screening) — saved hard Preferences and the pure metadata screening component, not existing formal Jobs; [SL-08.M1](#sl-08m1-shared-recruiting-platform-safety) — shared platform/account risk admission

**Reused component/infrastructure:** [SL-03.M1](sl-03-invocation-requirements.md#sl-03m1-invocation-durability-and-recovery-foundation) — applicable durable invocation/outcome evidence; collector workflow is not moved into a generic runtime

**Required Contract portions before development:** `jobs/collection.md` — adapter/search/frozen input/refresh/stop/audit; `jobs/jobs-screening.md` — complete canonical Job/JobVersion identity, admission, exact references/history, observations, formal local views and filtering integration; `jobs/platform-safety.md` — collection consumer agreement; `agent/execution-runtime.md`, `foundation/storage.md` — actual platform effect/retention scope; `evaluation/evaluation-observability.md` — controlled source fixtures and workflow evidence. Applicable common/storage scope from [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning) also applies.

**Joint agreement:** Frozen remote collection uses its own intent while local views use current Preferences. `jobs/jobs-screening.md` alone owns formal Job/JobVersion meaning; Collection maps/adopts source content under it, and SL-08.M2 is only the first implemented producer. Entries never become Job inputs. Risk and durable outcomes use existing owners.

**Research / unresolved Grill detail:** Verify BOSS/channel feasibility and adapter mapping against researched sources and observed admitted behavior; resolve unsupported cases before development.

**Tests / Eval:** V3, V7 safety, V9.2, V10, applicable V12: controlled source admission, rejected transient data, partial stop, stale observations, risk and unknown outcome. V denotes the corresponding section of [Acceptance](../../acceptance.md); the parent's links locate that proof. These are required future checks, not results.

**Milestone completion:** Actual collection/refresh yields correctly sourced complete immutable Job content and honest audit. Formal Job/Company reads and current-Preferences refiltering work on real saved Jobs, without bypassing shared blocking or persisting rejected content. Component fixtures alone do not establish a working producer or user Job Pool. Record actual evidence under [global Plan 2](../implementation-plan.md#2-milestone-readiness-completion-and-dependency-meaning); no current completion is claimed.

**Parent completion and remaining work:** Actual collection and refresh preserve complete Jobs, bounded operational evidence and shared safety; local reads cause no platform access. Controlled tests prove the relevant risk/stop boundaries; tests do not themselves authorize live account access or certify source quotas. Each milestone's necessary Contract scope must have been written and reconciled before its development; completion needs actual acceptance evidence and Progress/matrix updates. No completion is claimed now. All 2 listed milestones must be accepted. Any accepted subset leaves the other listed scopes pending. Integrated proof must cover formal Job admission/history, actual collection/refresh through the one persistent safety/effect boundary, and local read/refilter behavior with current Preferences while collection retains frozen intent. Parent completion is separate from rollout/production enablement.
