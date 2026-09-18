# Evaluation Development and Evidence

> English is authoritative. This supporting Development document owns the Eval implementation and evidence-handling procedure formerly in Development 7. It adds no product/runtime authority, normative Contract detail, release policy or claim of an installed Eval system.

[Development overview](README.md) · [Development discipline](../development.md) · [Global documentation index](../index.md)

## 1. Responsibility and use

[Development](../development.md) owns stage order, Contract-ready development, test-first work, source/research discipline, verification routing and handoffs. This guide supplies the specialized Eval procedure under that discipline. [Architecture 15](../architecture.md#15-eval-and-observability) owns Eval/runtime boundaries; [Eval acceptance](../acceptance/evaluation.md) owns the specialized required proof and limits on conclusions within unified Acceptance. Later normative Contracts own detailed interfaces and requirements. This guide implements those obligations in the development process without becoming another business, architecture or acceptance owner.

[Implementation Plan](../plans/implementation-plan.md), including its linked Slice plans, identifies the consuming milestone and its required Contract scope. [Progress recording rules](../progress/README.md) own status/readiness representation and traceable evidence records; actual records live in [Progress](../progress.md) and its [matrix](../progress/traceability.md). This guide owns how Eval evidence is produced, admitted, compared, retained and reassessed, not whether a capability can be marked complete.

The four sections below carry the execution responsibilities formerly in Development 7.1–7.4 and preserve their controlling Q/S references. Repeated proof criteria now resolve to Eval acceptance; this guide owns procedure, not an independent definition of isolation, admission, evidence completeness or acceptable quality. The original [Eval design record](../design/eval/agent-evaluation.md) remains provenance; scoped procedure documentation is not executed acceptance. Detailed evaluator interfaces and deferred rollout decisions remain pending with their existing owners.

## 2. Real paths, isolation, and exact experiments

Prepare the selected thin JobHunter task adapters, domain-aware checks, fixture hydration and authored Scenario driving around the selected Langfuse facilities and existing Application/Domain/Repository/Harness boundaries. Apply [Architecture 9/15](../architecture.md#9-shared-harness-skills-and-controlled-actions) for runtime ownership and the [general research discipline](../development.md#4-research-and-integration-preparation) for actual version/integration verification; this does not select a runner or create a second Eval platform.

For the chosen case, assemble the fixture, Dataset references, authored events/expectations and execution/evaluator configuration, then execute on the declared path and capture actual state/call evidence. Use [Eval acceptance 2.1](../acceptance/evaluation.md#21-isolation-exact-inputs-and-declared-experiment-scope) as the checklist for isolation, exact inputs, reproducibility and measured scope. Select the ready-Requirements or composed Fit path and the ordinary Advisor or explicit Memory-learning setup that matches the intended claim; retain the configuration and actual stage/background evidence needed by that checklist.

**Sources:** Q120–Q122, Q140, Q173, Q177, Q186–Q187, S35.1; Architecture 9/15; [Eval acceptance 2.1](../acceptance/evaluation.md#21-isolation-exact-inputs-and-declared-experiment-scope).

## 3. Scenario integrity and evaluator admission

Choose a localized N+1 case or complete authored Scenario according to the proof requested in [Eval acceptance 2.2](../acceptance/evaluation.md#22-n1-and-complete-scenarios). Hydrate the corresponding boundary or initial fixture, drive authored events at logical checkpoints through the real interfaces and collect the reached inputs, actual Proposal matching/confirmation, trajectory and canonical post-state for its assertions. Evaluate the result against those criteria rather than adding driver shortcuts to repair an unmet precondition.

Prepare Agent inputs, evaluation references and Scenario control separately; prepare each checker/judge's admitted evidence and configuration using [Eval acceptance 2.3](../acceptance/evaluation.md#23-evaluator-inputs-authority-and-conclusions). Run deterministic checks and separately configured judges against captured evidence, retaining actual checker inputs and findings for review. The linked criteria own visibility, trusted-control, authority and cost boundaries; this procedure does not redefine them or assume that platform judges inherit business Runtime guarantees.

**Sources:** Q158, Q173, Q176, Q178, Q180, Q183–Q185; Architecture 15.2–15.3; [Eval acceptance 2.2–2.3](../acceptance/evaluation.md#22-n1-and-complete-scenarios).

## 4. Findings, comparison, and release-policy boundary

Collect task results, deterministic findings, judge findings/errors and evidence availability, then prepare the checked-scope report under [Eval acceptance 2.3](../acceptance/evaluation.md#23-evaluator-inputs-authority-and-conclusions) and the [Progress recording rules](../progress/README.md). Those owners define admissible conclusions and status; producing a report does not itself establish acceptance.

Use the selected development/holdout inputs and declared comparison configuration to run the relevant capability checks, human calibration and comparisons in [Eval acceptance 3](../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence). Assemble actual sample/attempt counts, source/input/configuration references, semantic review, task/background/judge observations and limitations needed by those criteria. They own semantic alternatives, contamination, single-attempt versus repeated-Trial interpretation, separate quality/reliability/efficiency claims and deferred rollout boundaries; this guide sets no competing pass formula, threshold or release rule.

**Sources:** Q82, Q117, Q168, Q174–Q180, Q184, Q186–Q187, S17.1; [Acceptance 2](../acceptance.md#2-evidence-and-interpretation-rules) and [Eval acceptance 3](../acceptance/evaluation.md#3-semantic-quality-reliability-and-efficiency-evidence); Eval sections 8–10, 18–20 and 26.

## 5. Privacy, regression retention, and re-evaluation

Apply [Eval acceptance 2.4](../acceptance/evaluation.md#24-telemetry-regression-retention-and-re-evaluation) when promoting a production case, retaining regression evidence or reassessing an existing Trial. Conduct the human review, prepare the admissible sanitized/synthetic fixture, reconcile its references and verify that it still exercises the reviewed failure mechanism. Record available evidence and any resulting coverage gap under Progress rules; the linked criteria own retention and completeness requirements.

For evaluator/rubric reassessment, locate the retained actual Trial evidence, run the selected evaluation against it and preserve earlier evaluation history plus the new configuration/lineage. Use the same section's distinction between re-evaluation and intentional new Trial execution when choosing the procedure and recording cost. Its prohibition on silently recreating unavailable original evidence remains controlling.

At telemetry integration, verify the selected callback and explicit SDK paths with controlled export/admission/correlation cases from section 2.4 and the [privacy/history scenarios](../acceptance.md#10-privacy-storage-and-honest-history). Collect actual exported samples and canonical evidence for those checks. Architecture and Eval acceptance retain ownership of local authority, masking/admission, evaluator privacy and limits on telemetry conclusions.

**Sources:** Q125, Q136, Q174, Q176, Q178–Q179, Q181–Q184; Architecture 13/15.4–15.5; [Acceptance 10](../acceptance.md#10-privacy-storage-and-honest-history) and [Eval acceptance 2.4](../acceptance/evaluation.md#24-telemetry-regression-retention-and-re-evaluation).
