# JobHunter Progress

> English is authoritative. Summary reconciled on 2026-09-27 from the maintained records below. This page records current scope and remaining work; detailed executions and historical checkpoints live in [traceability](progress/traceability.md). A documentation change is not a new test run or milestone acceptance.

## 1. Current state and task

SL-01 and SL-02 remain **Partial**. Manual Application Entries and Preferences have recorded backend/frontend proof. Independent Resumes, deterministic Entry-scoped portrait planning/reuse and the revised frontend are delivered within their recorded scope. Production model-generated portrait execution and semantic Eval remain pending.

SL-03.M1/M2 have been withdrawn for redesign. The old Runtime implementation, detailed Contract scopes, Grill records and transfers are not a current development baseline. Replacement Contracts and cross-owner interface review must precede dependent implementation; separately approved SL-02 consumer clauses remain effective. See the [M1 withdrawal](progress/traceability.md#65-sl-03m1-reviewed-scope-and-interface-evidence) and [M2 withdrawal](progress/traceability.md#66-sl-03m2-reviewed-scope-and-interface-evidence).

The [backend operations guide](../backend/README.md#preferences-and-explicit-schema-evolution) now identifies schema 8 after removal of the retired Invocation storage. Existing schema-6/7 test executions in the matrix remain dated evidence, not verification of the current checkout. This summary does not rerun or extend their claims.

## 2. Documentation and review state

- Current formal owners are reached through the [documentation index](index.md). [Contract Index](contracts/index.md) distinguishes actual bodies from planned destinations; [scope readiness](progress/traceability.md#6-contract-normative-scope-readiness-ledger) is tracked per consumed portion.
- [CG03S1 source-model and Entry-scoped review](progress/traceability.md#67-sl-02m1-supplement-reviewed-scope) records the effective r1/r2 publication, supersession and consumer impact. A Ready consumer clause does not make the withdrawn Runtime ready.
- [W7](../.scratch/w7-joint-review-handoff.md), [CG01-BC1](progress/traceability.md#21-later-user-change-cg01-bc1) and the individual [Contract reviews](progress/traceability.md#61-sl-01m1-reviewed-scope-and-interface-evidence) retain their original review scope. No earlier PASS is a blanket approval of later changes.
- Only SL-01, SL-02 and SL-03 Slice plan files currently exist. SL-04–SL-12 remain historical planning locators in the global plan and ledger; their deleted files are not available execution plans. Retained Grill sources are listed in the [Grill entry](.grill/README.md).

## 3. Implementation and verification baseline

| Milestone | Status and Contract boundary | Recorded capability / proof | Remaining work |
| --- | --- | --- | --- |
| SL-01.M1 | Partial; consumed scope Ready | Backend and Manual Applications frontend; [backend](progress/traceability.md#7-sl-01m1-backend-implementation-evidence) and [browser evidence](progress/traceability.md#frontend-foundation-evidence) | Final visual/milestone acceptance |
| SL-01.M2 | Partial; consumed scope Ready | Preferences backend/frontend; [backend](progress/traceability.md#8-sl-01m2-backend-implementation-evidence) and [browser evidence](progress/traceability.md#m2-frontend-evidence) | Final visual/milestone acceptance |
| SL-02.M1 | Partial; reviewed r2 consumer scope Ready; replacement Runtime Pending | Independent Resume foundation, Entry-scoped deterministic planning/reuse and revised frontend; [backend](progress/traceability.md#entry-incremental-backend-foundation) and [frontend evidence](progress/traceability.md#independent-resume-frontend-evidence) | Protected model execution/publication/recovery, real model-generated READY/FAILED integration, semantic Eval and final visual/milestone acceptance |
| SL-02.M2 | Partial; reviewed surviving Materials/source scope Ready | Renderer and direct Resume-source adaptation; [renderer checkpoint](progress/traceability.md#materials-backend-evidence) and [source adaptation](progress/traceability.md#independent-resume-backend-foundation) | Saved preview/export frontend, browser and integrated acceptance |
| SL-03.M1/M2 | Planned; previous scope withdrawn, replacement Pending | No current Runtime capability established by the historical M1 results | Fresh design, normative/interface review, implementation and acceptance |
| SL-03.M3 | Planned; scope Pending | No implementation/acceptance recorded | Required Job/runtime capabilities and reviewed consumer scope |

Detailed Contract, implementation and acceptance dimensions remain in the [milestone ledger](progress/traceability.md#5-milestone-implementation-and-acceptance-ledger). Backend proof does not establish browser acceptance; deterministic proof does not establish model execution or semantic quality.

### 3.1 Parent Slice aggregation

| Parent | Aggregate status | Accepted milestones | Remaining required work / integrated acceptance |
| --- | --- | --- | --- |
| SL-01 | Partial | 0 / 2 | M1/M2 final acceptance and parent integration |
| SL-02 | Partial | 0 / 2 | M1 semantic consumer/final acceptance; M2 frontend/integration |
| SL-03 | Planned | 0 / 3 | Replacement S3 design and all milestone acceptance |
| SL-04 | Planned | 0 / 1 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-05 | Planned | 0 / 2 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-06 | Planned | 0 / 2 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-07 | Planned | 0 / 2 current | M1/M2 pending; M3 explicitly Deferred |
| SL-08 | Planned | 0 / 2 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-09 | Planned | 0 / 1 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-10 | Planned | 0 / 1 current | M1 pending; M2 explicitly Deferred |
| SL-11 | Planned | 0 / 2 | Historical allocation; no implementation/integrated acceptance recorded |
| SL-12 | Planned | 0 / 2 | Historical allocation; no implementation/integrated acceptance recorded |

These retained allocations do not recreate deleted Slice files or approve replacement plans. No parent is complete. The [supplemental allocation review](progress/traceability.md#67-sl-02m1-supplement-reviewed-scope) records the explicit apply/adopt-back deferrals.

### 3.2 Milestone and normative-scope records

Use the [milestone ledger](progress/traceability.md#5-milestone-implementation-and-acceptance-ledger) for child status and the [scope ledger](progress/traceability.md#6-contract-normative-scope-readiness-ledger) for independently consumed Contract portions. Requirement mappings, executed commands, outcomes and limitations stay in the matrix. Follow [recording rules](progress/recording-rules.md); file existence and parent status cannot substitute for scope readiness or child proof.

## 4. Gaps and prerequisites

1. **Replacement runtime:** SL-03 design and scope review remain prerequisites for the dependent production portrait consumer. Do not inherit withdrawn readiness or silently define the missing interface in code.
2. **Incomplete delivery:** SL-01 final acceptance, SL-02.M1 semantic execution/Eval and SL-02.M2 frontend/integration remain independently scoped work.
3. **Future capabilities:** Later consumers need their own current plans, Contracts, research and actual upstream capabilities. Unrelated scope need not wait for a whole file/family or parent Slice.
4. **Documentation integrity:** Deletions and relocations have left unresolved historical/source/plan references. Prior link-check PASS results describe their original snapshots, not the present tree. Missing records must not be reconstructed as approved decisions.

## 5. Verification scope and next step

For the next selected task, read its current Slice, actual consumed Contracts, applicable development handoff and linked evidence. Resolve missing scope or stale readiness before dependent work; no replacement Runtime implementation is authorized by this summary.

Maintain this page as the current summary. Put new requirement-to-code/test mappings, exact check commands/results and evidence limits in [traceability](progress/traceability.md), and update this page only when capability availability, blockers, parent remainder or next work changes. Historical schema and test-count narratives remain in their existing evidence sections rather than being copied here.
