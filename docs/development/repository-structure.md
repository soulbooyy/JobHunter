# Repository Organization

> English is authoritative. This document defines the required organization for frontend, backend, tests, Eval and supporting tooling. Place implementation and tests in the prescribed responsibility layers from the start of development. Create only the branches with actual consumers; incremental creation does not permit flattening code at the package or tests root. The full tree is not an existing-file inventory or an instruction to create empty packages.

[Development guides](README.md) · [Development discipline](../development.md) · [Global documentation index](../index.md) · [Actual Progress](../progress.md)

## 1. Responsibility and provenance

This supporting Development document owns the target physical file organization and its incremental creation/maintenance principles. [Architecture](../architecture.md#2-system-responsibilities-and-dependency-direction) owns logical responsibilities, dependency direction and runtime authority. [Product](../spec.md) owns behavior; [Contracts](../contracts/index.md) own detailed normative definitions when written; [Acceptance](../acceptance.md) owns proof. A package name or placement cannot override those owners.

[Implementation Plan](../plans/implementation-plan.md) and its [Slice plans](../plans/slices/README.md) own milestone scope, dependencies, required Contract portions and completion conditions. This document does not assign every target directory to a milestone or create another implementation schedule. [Progress rules](../progress/README.md) govern actual readiness/evidence recording; actual values belong in [Progress](../progress.md) and the [matrix](../progress/traceability.md).

**Source:** The user's supplied repository tree and subsequent approval to persist the recommended target-organization/just-in-time creation approach in this document. This is a later user engineering-organization direction, not an original Grill Q-ID, a detailed Contract or a claim of final stack selection. Existing architecture commitments still apply. The current user clarification makes responsibility-layer placement mandatory from first implementation. Document a justified structural change here before applying it; unused branches still need not exist.

The current [CG01-BC1 decision](../design/contract/sl-01-m1-grill.md#cg01-bc1) controls ManualApplicationEntry separation. The tree below makes its target placement explicit without changing that decision. Historical handoffs and original Grill records are preserved.

The later user-supplied [target technology stack](technology-stack.md) records the backend/frontend tool selections, including SQLAlchemy and Alembic. This guide continues to own placement only; exact versions, verified adoption and actual installation are separate from the target tree.

## 2. Target tree

All code, package, test, Eval, script and CI entries below are **targets**, not claims that they exist. Documentation entries show the organization they reference; use the live documentation index for availability. Ellipses abbreviate content and never instruct creation of placeholder files. Python/TypeScript-shaped paths, SQLAlchemy and Alembic names follow the user's selected implementation direction; this tree alone does not choose dependency versions, a complete framework/toolchain, API protocols or a migration scheme.

Adaptations from the supplied tree are limited to explicit ManualApplicationEntry placement, the actual existing Slice filenames, this new guide and the existing `.scratch/` handoff location. Section 4 fixes the single migration history location. Repository-wide Python tooling stays at the root so scripts/check has one locked environment.

```text
JobHunter/
├── backend/
│   ├── src/
│   │   └── jobhunter/
│   │
│   │       ├── domain/
│   │       │   ├── workspace/
│   │       │   ├── profile/
│   │       │   ├── preferences/
│   │       │   ├── evidence/
│   │       │   ├── resume/
│   │       │   ├── manual_application_entries/
│   │       │   ├── jobs/
│   │       │   ├── requirements/
│   │       │   ├── fit/
│   │       │   ├── advisor/
│   │       │   ├── preparation/
│   │       │   ├── execution/
│   │       │   ├── applications/
│   │       │   ├── memory/
│   │       │   └── shared/
│   │       │
│   │       ├── application/
│   │       │   ├── workspace/
│   │       │   ├── candidate/
│   │       │   ├── manual_application_entries/
│   │       │   ├── jobs/
│   │       │   ├── requirements/
│   │       │   ├── fit/
│   │       │   ├── advisor/
│   │       │   ├── preparation/
│   │       │   ├── execution/
│   │       │   ├── applications/
│   │       │   ├── memory/
│   │       │   ├── derived_work/
│   │       │   └── ports/
│   │       │
│   │       ├── agent/
│   │       │   ├── harness/
│   │       │   │   ├── run/
│   │       │   │   ├── context/
│   │       │   │   ├── invocation/
│   │       │   │   ├── tools/
│   │       │   │   ├── budget/
│   │       │   │   ├── recovery/
│   │       │   │   └── runtime/
│   │       │   │
│   │       │   ├── skills/
│   │       │   │   ├── requirement_parse/
│   │       │   │   ├── candidate_job_fit/
│   │       │   │   ├── resume_job_fit/
│   │       │   │   ├── resume_advisor/
│   │       │   │   └── memory_extraction/
│   │       │   │
│   │       │   └── observability/
│   │       │       └── langfuse/
│   │       │
│   │       ├── infrastructure/
│   │       │   ├── persistence/
│   │       │   │   ├── sqlalchemy/
│   │       │   │   │   ├── models/
│   │       │   │   │   ├── repositories/
│   │       │   │   │   ├── mappings/
│   │       │   │   │   └── uow/
│   │       │   │
│   │       │   ├── llm/
│   │       │   │   ├── gateways/
│   │       │   │   └── providers/
│   │       │   │
│   │       │   ├── collectors/
│   │       │   │   └── boss/
│   │       │   │
│   │       │   ├── browser/
│   │       │   │   └── executor/
│   │       │   │
│   │       │   ├── rendering/
│   │       │   │   ├── resume/
│   │       │   │   └── artifacts/
│   │       │   │
│   │       │   ├── files/
│   │       │   │   ├── imports/
│   │       │   │   └── storage/
│   │       │   │
│   │       │   ├── platform_safety/
│   │       │   ├── clock/
│   │       │   └── ids/
│   │       │
│   │       ├── api/
│   │       │   ├── v1/
│   │       │   │   ├── workspace/
│   │       │   │   ├── profile/
│   │       │   │   ├── preferences/
│   │       │   │   ├── evidence/
│   │       │   │   ├── resumes/
│   │       │   │   ├── manual_application_entries/
│   │       │   │   ├── jobs/
│   │       │   │   ├── requirements/
│   │       │   │   ├── fit/
│   │       │   │   ├── advisor/
│   │       │   │   ├── preparations/
│   │       │   │   ├── executions/
│   │       │   │   ├── applications/
│   │       │   │   └── memory/
│   │       │   │
│   │       │   ├── dependencies/
│   │       │   ├── errors/
│   │       │   ├── middleware/
│   │       │   └── schemas/
│   │       │
│   │       ├── bootstrap/
│   │       │   ├── container.py
│   │       │   ├── lifespan.py
│   │       │   └── settings.py
│   │       │
│   │       └── main.py
│   │
│   ├── tests/
│   │   ├── unit/
│   │   │   ├── domain/
│   │   │   ├── application/
│   │   │   └── agent/
│   │   ├── integration/
│   │   │   ├── persistence/
│   │   │   ├── application/
│   │   │   ├── api/
│   │   │   └── harness/
│   │   ├── conformance/
│   │   │   ├── recovery/
│   │   │   ├── permissions/
│   │   │   ├── fencing/
│   │   │   ├── budget/
│   │   │   └── concurrency/
│   │   └── fixtures/
│   │
│   ├── evals/
│   │   ├── tasks/
│   │   │   ├── requirement_parse.py
│   │   │   ├── candidate_job_fit.py
│   │   │   ├── resume_job_fit.py
│   │   │   └── resume_advisor.py
│   │   ├── scenarios/
│   │   │   ├── driver.py
│   │   │   ├── model.py
│   │   │   └── advisor/
│   │   ├── contracts/
│   │   │   ├── authority.py
│   │   │   ├── lineage.py
│   │   │   ├── authorization.py
│   │   │   └── mutation.py
│   │   └── common/
│   │       ├── environment.py
│   │       ├── fixtures.py
│   │       └── langfuse.py
│   │
│   ├── alembic/
│   │   └── versions/
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── router/
│   │   │   ├── providers/
│   │   │   ├── layout/
│   │   │   └── bootstrap/
│   │   │
│   │   ├── pages/
│   │   │   ├── resumes/
│   │   │   ├── candidate-knowledge/
│   │   │   ├── job-pool/
│   │   │   │   └── manual-application-entries/
│   │   │   ├── job-assistant/
│   │   │   └── applications/
│   │   │
│   │   ├── features/
│   │   │   ├── workspace/
│   │   │   ├── profile/
│   │   │   ├── preferences/
│   │   │   ├── evidence/
│   │   │   ├── resume/
│   │   │   │   ├── editor/
│   │   │   │   ├── import/
│   │   │   │   ├── preview/
│   │   │   │   └── selector/
│   │   │   ├── manual-application-entries/
│   │   │   ├── jobs/
│   │   │   │   ├── pool/
│   │   │   │   ├── collection/
│   │   │   │   ├── screening/
│   │   │   │   └── details/
│   │   │   ├── fit/
│   │   │   │   ├── candidate-fit/
│   │   │   │   ├── resume-fit/
│   │   │   │   └── batch/
│   │   │   ├── advisor/
│   │   │   │   ├── chat/
│   │   │   │   ├── suggestions/
│   │   │   │   └── change-proposal/
│   │   │   ├── preparation/
│   │   │   │   ├── materials/
│   │   │   │   ├── greeting/
│   │   │   │   └── approval/
│   │   │   ├── execution/
│   │   │   │   ├── approval/
│   │   │   │   ├── attempt/
│   │   │   │   └── batch/
│   │   │   ├── applications/
│   │   │   │   ├── history/
│   │   │   │   └── progress/
│   │   │   └── memory/
│   │   │       ├── settings/
│   │   │       └── management/
│   │   │
│   │   ├── entities/
│   │   │   ├── profile/
│   │   │   ├── evidence/
│   │   │   ├── resume/
│   │   │   ├── manual-application-entry/
│   │   │   ├── job/
│   │   │   ├── requirement/
│   │   │   ├── fit/
│   │   │   ├── preparation/
│   │   │   ├── application/
│   │   │   └── memory/
│   │   │
│   │   ├── shared/
│   │   │   ├── api/
│   │   │   ├── ui/
│   │   │   ├── hooks/
│   │   │   ├── lib/
│   │   │   ├── types/
│   │   │   ├── utils/
│   │   │   └── constants/
│   │   │
│   │   ├── assets/
│   │   └── main.tsx
│   │
│   ├── tests/
│   │   ├── unit/
│   │   ├── component/
│   │   └── e2e/
│   │
│   ├── package.json
│   └── README.md
│
├── docs/
│   ├── index.md
│   ├── README.md
│   │
│   ├── spec.md
│   ├── architecture.md
│   ├── acceptance.md
│   ├── development.md
│   ├── progress.md
│   │
│   ├── contracts/
│   │   ├── README.md
│   │   ├── index.md
│   │   ├── structure.md
│   │   ├── common.md
│   │   ├── foundation/
│   │   ├── candidate/
│   │   ├── jobs/
│   │   ├── applications/
│   │   ├── agent/
│   │   └── evaluation/
│   │
│   ├── plans/
│   │   ├── README.md
│   │   ├── implementation-plan.md
│   │   └── slices/
│   │       ├── README.md
│   │       ├── sl-01-workspace-jobs-preferences.md
│   │       ├── sl-02-saved-authority-materials.md
│   │       └── ...
│   │
│   ├── acceptance/
│   │   ├── README.md
│   │   └── evaluation.md
│   │
│   ├── development/
│   │   ├── README.md
│   │   ├── evaluation.md
│   │   ├── repository-structure.md
│   │   ├── technology-stack.md
│   │   └── handoff/
│   │       └── sl-01-m1-handoff.md
│   │
│   ├── evaluation/
│   │   └── README.md
│   │
│   ├── progress/
│   │   ├── README.md
│   │   └── traceability.md
│   │
│   └── design/
│       ├── README.md
│       ├── grill-me-design-tree.md
│       ├── harness/
│       ├── eval/
│       └── contract/
│
├── .scratch/                         # Authoring guides and historical handoffs
│
├── scripts/
│   ├── setup
│   ├── check
│   ├── test
│   └── eval
│
├── third-party/
│   └── ...
│
├── .github/
│   └── workflows/
│
├── pyproject.toml
├── uv.lock
├── .python-version
├── README.md
└── .gitignore
```

## 3. Responsibility-to-location mapping

| Target location | Intended responsibility and boundary |
| --- | --- |
| `backend/src/jobhunter/domain/` | Owned business rules and concepts. Folder groupings do not imply one Aggregate, service or universal lifecycle per directory. `shared/` contains only genuinely shared concepts needed by actual consumers. |
| `backend/src/jobhunter/application/` | Use cases, preparation, orchestration, authorized commands and coordinated commits. `candidate/` groups cross-asset coordination; it does not introduce a Candidate Aggregate or duplicate Profile/Evidence/Resume ownership. Ports describe necessary owned boundaries. |
| `backend/src/jobhunter/agent/harness/` | Shared bounded execution, actual Context, invocation admission, Tools, resource accounting and recovery. Separate folders do not create competing Run, invocation or recovery protocol owners. |
| `backend/src/jobhunter/agent/skills/` | The bounded task Skills already defined by Architecture. Collector/Executor workflows do not become Skills merely to reuse infrastructure. |
| `backend/src/jobhunter/infrastructure/` | Concrete persistence, source, provider, browser, rendering and storage adapters behind owned boundaries. ORM models and provider payloads do not become Domain or Contract authority. |
| `backend/src/jobhunter/api/` | Transport entry points and boundary validation for Application use cases. Directory names, including `v1/`, do not freeze routes, payloads or a compatibility policy. |
| `backend/src/jobhunter/bootstrap/` and `main.py` | Composition, startup/lifecycle and settings needed by the delivered application. Their presence in this target chooses no container library or full deployment setup. |
| `agent/observability/langfuse/` and `backend/evals/common/langfuse.py` | Target locations for runtime observation integration and Eval-side platform helpers respectively. Reuse common admitted correlation/masking where applicable; no second business or telemetry authority. |
| `backend/tests/` and `frontend/tests/` | Actual deterministic, integration, conformance, component and interaction proof required by the consuming milestone. Create suites and fixtures when real checks need them. |
| `backend/evals/` | Thin task adapters, Scenario driving, checkers and fixture helpers around real Application/Harness execution. `evals/contracts/` means executable conformance checks consuming normative Contracts, not another source of Contract definitions. |
| `frontend/src/app/` and `pages/` | Composition, navigation and page entry points. A page or route does not own business facts or require an independent Domain Aggregate. |
| `frontend/src/features/` | User interactions and task-specific presentation, consuming owned interfaces. Distinct preparation approval and execution approval remain separate. |
| `frontend/src/entities/` | Client-side representations and presentation helpers for consumed concepts. Do not recreate backend business rules, canonical persistence or a second schema authority here. |
| `frontend/src/shared/` | Demonstrably shared client infrastructure/UI helpers. Populate from actual use; do not prebuild generic wrappers, types or utilities for every imagined consumer. |
| `docs/` and `.scratch/` | Formal owners/navigation and separate authoring/history artifacts. This tree does not rename existing docs or promote scratch proposals into authority. |
| `scripts/`, `.github/workflows/`, `third-party/` | Future real commands/automation and justified research or reused material. Script names select no runner/CI/release policy. Third-party material remains subject to Development research/license discipline. |

The mapping follows Architecture 2–3, 5, 7 and 9–16. In particular, Q53 preserves the absence of a Candidate Aggregate; Q122/Q135 preserve bounded invocation/recovery authority; Q147/Q152 preserve separate safe derived work; Q173–Q187 preserve real-path Eval and canonical business authority. These references explain existing constraints, not provenance for the new path names.

## 4. Placement clarifications

### 4.1 ManualApplicationEntry remains separate

The target uses `manual_application_entries/` within backend Domain, Application and API organization, plus `manual-application-entries/` for the frontend feature and `manual-application-entry/` for its client representation. These are prescribed physical names for the separate responsibility established by CG01-BC1; they define no new fields, route spelling or API payload.

The separate entry view is placed under `pages/job-pool/manual-application-entries/` because Job Pool supplies its navigation entry. That UI placement does not put the record inside the formal Job family. Do not implement it as a Job/JobVersion, an application-history event or an Executor action. In particular, opening its URL remains ordinary explicit user navigation, not automatic application or evidence of success.

Use the current [SL-01.M1 plan](../plans/slices/sl-01-workspace-jobs-preferences.md#sl-01m1-local-workspace-and-manual-application-entries), not the earlier Manual Job scope in historical snapshots. Its existing filename is retained even though its current title and scope have changed.

### 4.2 Migration paths do not establish two sources of truth

`backend/alembic/versions/` is the only authoritative revision-script directory. `backend/alembic/env.py` and `backend/alembic.ini` provide its runner wiring. Do not create an additional `infrastructure/persistence/migrations/` revision history. Runtime schema recognition belongs under `infrastructure/persistence/sqlalchemy/models/`; it does not duplicate migration history or authorize automatic migration of existing storage.

### 4.3 Package grouping does not enlarge a foundation milestone

`run/`, `invocation/`, `recovery/` and `runtime/` are proposed subdivisions of the existing Harness responsibilities. They are not four independent lifecycle designs. Start with the smallest useful grouping and split only where concrete code and maintenance needs justify it. The bounded [SL-03 plan](../plans/slices/sl-03-invocation-requirements.md) controls its actual capability, Contract and proof scope; path availability cannot turn invocation durability into a universal side-effect framework.

The Eval task/Scenario branches shown are not an exhaustive coverage inventory. Absence of a named Memory task file, for example, does not remove required Memory Eval. Add the actual adapters/checks with their consuming milestone under [Eval development procedure](evaluation.md) and [Eval acceptance](../acceptance/evaluation.md), without precreating unused task files now.

## 5. Incremental creation principles

1. **Target does not mean existing.** A documented directory, package, interface or script is neither delivered functionality nor readiness evidence. Keep current status in Progress rather than marking target branches implemented here.
2. **Create for an actual milestone.** Before development, complete that milestone's required normative scope and interfaces and satisfy its research/upstream prerequisites under Development. Place needed files directly in their prescribed layers. Do not create a handoff or edit a Slice plan merely to list routine implementation files. Do not allocate or scaffold the entire tree in advance.
3. **Required placement without empty scaffolding.** Do not generate empty package hierarchies, `.gitkeep` files, unused interfaces, stub adapters, no-op tests or script shells merely to match this tree. Necessary package markers, configuration and test setup may accompany real code or meaningful failing tests for the current milestone.
4. **Keep first-use safeguards complete.** Incremental package creation does not permit skipping privacy, authorization, transaction, recovery or evidence obligations required by the actual consumer. Conversely, reuse of an infrastructure component does not require users to perform an unrelated product workflow.
5. **Keep definitions with their owners.** Directory names and frontend/ORM/transport representations consume the relevant Contracts and architectural boundaries. A filesystem split must not create duplicated normative definitions or conflicting lifecycle owners.
6. **Evolve from evidence.** When implementation demonstrates a better grouping, record the reason and update this target and affected references/plans. Pure path changes do not require inventing a business decision; a real semantic change must follow the existing source/change discipline.

For SL-01.M1, plan only the actual local Workspace and separate ManualApplicationEntry path, its necessary composition/persistence/UI or transport boundaries, and appropriate verification. Formal Job acquisition, Fit, Agent Harness, rendering, execution and Memory are not bootstrap packages required merely because they appear above. The exact package subset remains implementation preparation under the current milestone; this guide neither starts that work nor declares its Contracts ready.

## 6. Maintenance and traceability

Maintain the full target and physical-role clarifications here. Core Development retains the general creation discipline and links here; directory/global indexes navigate. The owning Slice plan records any concrete package allocation needed for its milestone, while Progress/matrix record actual Contract readiness, implemented locations and executed proof. Do not copy this full tree into Architecture, the global Implementation Plan or READMEs.

When a shared implementation boundary changes, check the affected Architecture/Contract owners, consumers and acceptance evidence rather than only adjusting paths. Preserve the distinction between the original user-supplied target, later justified organization changes and actual repository contents. The tree includes future branches; actual implementation and evidence are recorded in Progress, not inferred from this guide.

## 7. Test file naming and placement

Name tests after stable capabilities or responsibilities, not delivery-plan identifiers. Use `test_manual_application_entries.py`, `test_workspace_startup.py`, `test_storage.py`, `test_preferences.py`, `test_requirement_parse.py` and `test_candidate_fit.py`. Do not use `test_m1.py`, `test_m2.py`, `test_sl03.py` or equivalent milestone/Slice numbering. A milestone can change or split without changing a capability's test identity. Keep milestone/requirement associations in `docs/progress/traceability.md`.

Place each suite by the boundary it exercises: isolated rules in `tests/unit/domain/`, Application integration in `tests/integration/application/`, real persistence in `tests/integration/persistence/`, HTTP integration in `tests/integration/api/`, and cross-cutting conformance in `tests/conformance/` with responsibility subdirectories such as `recovery/`. Shared language-neutral inputs belong in `tests/fixtures/` and use semantic filenames too. Avoid generic root-level catch-all test files. When a file mixes unrelated startup, storage and entry responsibilities, split it along those responsibilities; a persistence restart used to verify an entry's durability may remain with that entry scenario.

Current backend placement follows those rules: entry admission/models under `domain/manual_application_entries/`, shared failures under `domain/shared/`, entry use cases under `application/manual_application_entries/`, storage/schema under `infrastructure/persistence/sqlalchemy/`, HTTP routes under `api/v1/manual_application_entries/`, transport schemas/errors/middleware under their `api/` packages, and composition/lifecycle under `bootstrap/`. `main.py` is the executable entry point. Package markers accompany these actual consumers; no unused future subsystem is scaffolded.
