# Progress Recording Rules and Navigation

> English is authoritative. This file owns Progress recording discipline within the existing Progress category: traceability, status/evidence meanings, parent/milestone reporting and scope-level Contract readiness records. It is intentionally more than a navigation README. It does not own product behavior, runtime state, planned delivery scope or actual completion claims.

[Global documentation index](../index.md) · [Progress summary](../progress.md)

## 1. Responsibility and record locations

[Development](../development.md) owns the general delivery sequence and requires ready Contracts before development. [Implementation Plan](../plans/implementation-plan.md), including its linked Slice plans, owns concrete decomposition, dependencies, required Contract scope and completion conditions. This file defines how that scope and the resulting evidence are recorded; it cannot change the plan or declare an unresolved interface ready. [Acceptance](../acceptance.md), including [Eval acceptance](../acceptance/evaluation.md), owns required proof; [Evaluation development and evidence](../development/evaluation.md) owns specialized Eval evidence production/handling. Contract bodies later supply actual normative definitions and IDs.

| Record | Use |
| --- | --- |
| [Progress summary and parent aggregation](../progress.md#31-parent-slice-aggregation) | Current task, documentation/implementation state, parent remainder, blockers and next work |
| [Source-clause matrix](traceability.md#2-existing-record-coverage-and-effective-destinations) | Q/S provenance, controlling supersession, formal owners, proof destinations and planning locators |
| [Milestone implementation and acceptance](traceability.md#5-milestone-implementation-and-acceptance-ledger) | Consumed-Contract readiness, actual implementation, checks and evidence for each child |
| [Normative-scope readiness](traceability.md#6-contract-normative-scope-readiness-ledger) | Independently identified owned portions, completed/open clauses and interface evidence |

Sections 2–5 preserve the former Development 8.1–8.4 rules and their controlling sources. Keep volatile values in the linked records, detailed requirement prose in its normative owner and actual planning scope in Implementation Plan's owning Slice file. Navigation or planning edits alone establish no implemented capability. This relocation does not create a new status vocabulary, Contract lifecycle, schema or evidence of readiness.

## 2. Preserve the chain without inventing completed artifacts

Before detailed Contracts exist, map effective Grill clauses to their actual Product/Architecture owner, acceptance destination, pending/exclusion reason and current document state. Keep Contract IDs explicitly pending. A source Q-ID or a named acceptance scenario is not an invented normative Contract ID, implementation path, test file or execution receipt.

Later Contracts assign stable IDs to important requirements. The [matrix](traceability.md) currently records design-to-document mappings with Contract IDs pending. As planning and individual Contract scopes become available, add actual Slice planning identifiers and real Contract IDs alongside remaining pending scope, then map implementation, tests/Eval, evidence and status as they genuinely exist. Keep the requirement prose in its normative owner rather than copying it into matrix rows. Retain relevant Q-ID provenance and controlling supersession so changes remain auditable. Each independently delivered milestone updates affected rows with its parent Slice, actual Contract references and proof; final Slice aggregation also records integrated acceptance.

Progress is the concise current-state summary: current task/Slice, documentation and implementation state, major gaps/blockers and next step. The supporting matrix carries detailed mappings inside the same category. Neither becomes another design authority outside the Progress category. For a partial implementation, map and describe the actual demonstrated subset and its remaining gaps; avoid a capability-wide completion label based on one successful path.

**Sources:** Q22, Q26, Q32, S37.1, S38.1; Acceptance 1; [Development 9.2](../development.md#92-two-separate-verification-seams); English authoring spec, Further Notes B–D.

## 3. Status requires evidence

Q26/Q32's implementation labels retain the following evidence discipline. These are Progress meanings, not a new Domain lifecycle or a field schema for Contracts.

| Status | Evidence discipline |
| --- | --- |
| Planned | Accepted target without sufficient implemented capability; document the real prerequisites and remaining work rather than treating authored design as code |
| Deferred | Explicitly postponed scope with its controlling decision, reason and later boundary; an unimplemented current requirement is not automatically a product deferral |
| Partial | Actual implemented subset with corresponding verification evidence and explicit incomplete/unverified scope; prose, stubs or a planned test alone cannot support it |
| Implemented | Actual capability satisfies its claimed scope and required acceptance proof, with traceable implementation and verification evidence; file existence or old-repository results cannot establish it |

Record authored drafts, scoped author review, joint review and user approval separately from implementation status. A document review pass is not product acceptance. Preserve failed, incomplete, unavailable and unexecuted checks in evidence descriptions without inventing runtime result encodings or inferring release readiness. A later change can invalidate earlier evidence for the affected scope; update the mapping and gap explanation rather than retaining a stale completion claim.

**Sources:** Q4, Q26, Q32, Q175, Q179, S37.1; Acceptance 2; [Development 9.2](../development.md#92-two-separate-verification-seams).

## 4. Planned unified checks

Q32 calls for a later unified `./scripts/check` entry covering stable requirement-ID uniqueness, valid matrix references and required mappings. It does not establish that the script, underlying test tools or a CI pipeline exists now. Document-time identifier/link/structure checks are scoped authoring evidence, not execution of that future entry.

When the later tooling is implemented, preserve the distinction between current Q-ID design mappings and completed-Contract IDs, and between planned destinations and real evidence. Checks must not demand fabricated Contract IDs or mark a capability Implemented because a referenced file exists. Semantic clause coverage, two-seam review and Slice acceptance remain necessary beyond mechanical checks. Exact command composition, runner integration, CI wiring and release policy are still later work; no runnable setup instructions are supplied here.

**Sources:** Q26, Q32, Q175, S38.1; English authoring spec, Implementation 17 and Testing Decisions.

## 5. Two-level progress and scope-level Contract readiness

Maintain parent Slice and milestone records separately in the Progress category. The parent reports aggregate Planned / Partial / Implemented / Deferred status, accepted milestone scopes, remaining required milestones and cross-milestone integration evidence. Each milestone reports its required normative scopes and readiness, actual implementation availability, acceptance/check outcome, evidence references and outstanding work. A parent remains incomplete while an accepted child capability is independently available; partial code does not establish parent completion.

Retain the Q26/Q32 implementation vocabulary from section 3. Contract readiness, work started/code written, and acceptance verified/passed are separate observations. “Verified” is an evidence dimension, not another implementation status. Written code with unexecuted acceptance cannot be reported as an accepted or Implemented milestone. Current pending/not-started/not-executed observations are descriptive reporting, not a new Contract state machine.

**Contract file existence ≠ Contract family complete; section complete ≠ document complete.** Track each consumed normative scope by its definition-owning document and responsibility portion, then its real section/requirement IDs and reviewed revision after writeback. Record the covered/pending clauses, necessary interface agreement, affected consumers and review evidence. A section with mixed completeness must be split into independently identifiable scopes for this record. A filename or broad family label cannot stand in for readiness.

For example, Candidate Fit, Resume Fit, shared assessment/scoring, explicit rescore and each task's batch/orchestration scopes can have different readiness in the same planned `fit-analysis.md`. A single-target Candidate milestone needs its complete applicable shared and Candidate scopes; unrelated Resume/batch scope may remain pending. These are planning responsibilities, not frozen Contract anchors or an assertion that any scope is ready now.

Keep live records in [Progress](../progress.md) and its [matrix](traceability.md), with the parent summary separate from the milestone and Contract-scope ledgers. Future normative documents define their rules and IDs; volatile readiness/implementation evidence belongs to Progress. Any shared-scope revision triggers an impact check for prior consumers rather than preserving stale readiness.

**Sources:** Q26/Q32 and current user W6 review clarification; Q118/Q147/Q152 for Save versus rendering; Q122 for bounded invocation recovery. This reporting refinement adds no product prerequisite or normative field/schema.
