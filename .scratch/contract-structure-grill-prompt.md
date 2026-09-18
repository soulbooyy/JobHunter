# Prompt: Contract Document Structure Review from the W6 Macro Slice Draft

Use this prompt in the separate conversation that will discuss Contract structure. English is authoritative for repository artifacts. Discussion may follow the user's preferred language.

---

Work in `/Users/soulboy/projects/JobHunter`. Help me conduct a **structure-only Contract Grill** using the current macro Slice draft. The immediate goal is to turn Architecture's eleven candidate responsibility families into a clear prospective Contract document structure that W6 can reference precisely.

This is part of W6 planning, before its final Implementation Plan and W7 joint review. It is not the later per-Slice detailed field/interface Contract Grill, a reopening of Architecture Grill, or authorization to implement product code.

## 1. Read the actual inputs automatically

Read applicable repository instructions, then:

- `.scratch/document-authoring-spec.en.md`, particularly Implementation Decisions 18 and Further Notes F.
- `.scratch/w5-progress-handoff.md`, particularly the process revision and current W6 entry; distinguish its preserved historical checks from current directions.
- `.scratch/w6-macro-slice-draft.md` in full. SL-01 through SL-12 are provisional planning proposals, not accepted product architecture or completed capabilities. F01–F11 are local aliases for the existing eleven families, not normative Contract IDs.
- Actual `docs/spec.md`, `docs/architecture.md` (especially 16.1–16.3), `docs/acceptance.md`, `docs/development.md`, `docs/progress.md` and `docs/progress/traceability.md`.
- `docs/design/grill-me-design-tree.md` Purpose/Session State, Q4/Q22/Q26/Q32/S24.2/S37.1/S38.1, and original controlling topic clauses for every proposed boundary. Read the relevant six Harness modules and detailed Eval record where responsibilities cross.
- `docs/design/contract/contract-design-inventory.md` only as a non-normative checklist, never a finalized schema or independent decision source.

The later user-approved delivery direction controls over the older global Contract-stage ordering: macro plan and structural review within W6 → W7 joint/user review → each Slice's required detailed Contract Grill/writeback/reconciliation → that Slice's development. Completing unrelated families or later portions of a shared family is not a prerequisite.

If this conversation already contains agreed structural decisions, compare them with these current files and retain valid decisions rather than restarting. Report any genuine conflict with exact clauses and scope.

## 2. Resolve structure and ownership only

Start from Architecture 16's eleven families. Use actual ownership, consumer/reference and change boundaries to propose documents. Do not force eleven files, one object per file, one family per Slice, or a universal shared foundation that requires the entire system's detailed design first.

For each proposed document, identify:

1. A proposed filename/path or stable structural locator, clearly distinguished from a normative requirement ID.
2. Its single responsibility and the concepts/invariants it exclusively defines.
3. Explicit exclusions and the other document that owns each adjacent meaning.
4. Documents it references and why; reference direction must not grant cross-domain write authority.
5. Which original candidate families it derives from and why any split or regrouping is justified.
6. Which provisional Slices consume it and which required scope each consumer needs.
7. Relevant controlling Q/S sources and actual Product/Architecture/Acceptance destinations.
8. What detailed questions remain for the later Slice Contract Grill.

Document boundaries should be clear enough for precise Slice references. They need not pretend to be permanently indivisible. Where a boundary depends on unresolved detailed design, state a bounded provisional choice or a focused open question rather than freezing invented semantics.

A shared Contract can accumulate completed scope across Slices. Required scope must be coherent before its consuming Slice develops; creating a file or finishing one section does not mean the whole document/family is complete.

## 3. Use the draft to examine actual consumers

Produce a Slice-to-document matrix that distinguishes:

- Required normative scope before development.
- Shared scope the Slice expects to reuse versus scope it introduces or extends.
- Cross-document interface agreements that must be reconciled together.
- Necessary implemented upstream capabilities versus Contract/research prerequisites.
- Work that can remain pending for later Slices and the reason.
- Conditional paths, including any optional model-assisted import step; do not silently turn a conditional choice into a mandatory feature.

Reused scope means planned reuse unless actual Contracts exist; inspect the repository instead of assuming anything is already frozen.

Review the draft's broad SL-02, SL-03 and SL-07 boundaries and its component-level dependencies. Suggest smaller or reordered delivery groupings only when a real boundary warrants them. Keep a mapping from the existing SL identifiers and explain consumer/acceptance consequences. The macro Slice order is a proposal, not a reason to distort Contract ownership.

Preserve independent Candidate/Resume Fits, Advisor without a Fit prerequisite, human-reported applications without fabricated automated history, and ordinary Preparation without requiring users to run Advisor. Development integration dependencies must not become new product prerequisites.

## 4. Reconcile Architecture 16.3 explicitly

Account for all seven cross-family boundary groups:

- Evidence/Profile Save, all-affected Resume propagation and durable demanded-work intent.
- Resume/Proposal, Session, generating Run completion, exact confirmation and deletion arbitration.
- Requirements/Fit/Harness, parse producer ownership, freeze points, repair, current publication and revocation.
- Materials/Preparation, execution consent and shared platform safety.
- Context/Memory/Storage, actual visibility, checkpoints, current Recall and historical/deleted-source behavior.
- Budget/Runtime/Recovery, reservation/dispatch/response/settlement, unknown exposure and fencing.
- Eval's isolated real paths, admitted evidence and independent judgment versus local business authority.

Identify the single definition owner and necessary consuming references for each. A reciprocal reference is not automatically a runtime dependency cycle; separate shared interface agreement from sequencing.

## 5. Conduct the discussion without adding product decisions

Derive answers already settled by the repository rather than asking me to decide them again. For unresolved structural choices, present a focused recommendation, the alternative, the consumer impact and source constraints, then use the Contract Grill discussion to resolve the choice. Do not ask an exhaustive batch of field-design questions.

Later corrections override earlier clauses even when the parent is still ACCEPTED. REJECTED/SUPERSEDED content cannot be restored. Do not invent a KnowledgeConfirmation, private Resume facts, Coverage authority, Advisor working draft, implicit consent, silent replay, RAG fallback, cooldown-only strong-risk restoration or Eval-owned business success.

Do not define fields, types, enums, state-transition tables, API payloads, database schemas, validation errors, migration procedures, exact budget/retention values, numerical release thresholds, CI policy or production enablement. Do not mint normative Contract requirement IDs. Existing accepted invariants may be cited to explain document ownership without finalizing their representation.

## 6. Required result and permitted writeback

First present a reviewable proposed document catalog, family-to-document map, Slice-to-document required-scope matrix, cross-document reference/ownership map and unresolved structural questions. Discuss and resolve the structural choices with me.

After those choices are agreed:

- Update `docs/architecture.md` section 16 with the agreed structural responsibilities and references, preserving its design authority and traceability to the original eleven families. Other sections need changes only if necessary to reconcile the agreed structural wording; do not alter product/runtime decisions.
- Write an English structural handoff at `.scratch/contract-structure-grill-handoff.md`. Include sources read, agreed versus still-provisional boundaries, document paths/locators (marked planned), family mapping, every SL identifier's required scope and dependencies, any proposed Slice changes, cross-boundary reconciliations, remaining later-Grill questions, and separate findings for both seams.
- Update Progress/matrix only for actual structural work performed and its pending boundaries, if needed. Preserve earlier completion evidence as historical.
- Leave `docs/implementation-plan.md` finalization to the W6 authoring task, which will consume the structural handoff. Do not claim W6/W7 or user review of the full main-document baseline is complete merely because the structure discussion is complete.

Do not create normative `docs/contracts/*` bodies or empty placeholder files, code, executable tests, a W6 completion handoff, external issues or commits in this structure-only task. Do not modify original Grill records, the Chinese authoring reference or historical W1–W5 delivery/check evidence. Do not rename sources or treat the Inventory as a Contract.

## 7. Report the two existing verification seams separately

**Decision-to-Document Traceability Seam:** Each proposed/agreed owner and boundary has controlling source provenance and a consuming Slice or justified shared purpose. Cover all eleven original families and all twelve draft Slice identifiers, retaining any split/regrouping correspondence. Distinguish structural decisions agreed in this conversation from original Q/S records; do not fabricate old IDs.

**Cross-Document Semantic Consistency Seam:** The proposed document structure agrees with Product behavior, Architecture ownership/invariants, Acceptance proof, Development's per-Slice readiness process and actual Progress. Required shared interfaces have one definition owner, and partial Contract readiness is not presented as full-family completion.

State actual agreement, open questions and review limits. Link the structural handoff and changed Architecture sections. The W6 author can then bind each Slice to precise planned documents and required sections without waiting for all detailed Contracts to be completed.
