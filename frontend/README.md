# Frontend development

This is the SL-01.M1 Manual Applications frontend: list, create, edit, delete, explicit recovery and safe browser handoff, backed by the actual local API. It creates no Job or application-success fact. The SL-01.M2 Preferences page provides complete six-field editing, explicit unlimited choices, revision conflict recovery and identical uncertain-Save replay. SL-02.M1 adds saved Profile, six Evidence kinds and Resume editing/management with live local A4 preview. Materials rendering/export and later capabilities remain outside this frontend implementation. Full milestone sign-off remains separate from the executable evidence below.

## Install and run

Verified on macOS arm64 with Node **26.5.0** and npm **11.17.0**. `.node-version`, `engines` and `packageManager` record this adopted toolchain; `.npmrc` enforces engines and exact direct versions. Commit `package-lock.json` and use `npm ci` for reproducible installs. Versions are pinned in `package.json`; this is not a promise of compatibility with arbitrary Node/npm releases.

After completing [backend installation](../backend/README.md), install frontend dependencies and start both services from the repository root:

```sh
npm --prefix frontend ci
./scripts/dev
```

Open <http://127.0.0.1:5173>. Ctrl-C stops both owned process groups; if either service exits, the other is stopped. Occupied ports fail before startup and existing services are never terminated or reused. The launcher requires Node and uv on PATH; it does not install frontend dependencies, migrate storage or delete data.

`./scripts/dev` binds both services to loopback and explicitly sets the matching backend Host/Origin admission. It preserves `JOBHUNTER_DATA_DIRECTORY` and other non-network backend configuration. Optional `JOBHUNTER_DEV_PORT` (frontend, default 5173) and `JOBHUNTER_PORT` (backend, default 8765) update both admission and the Vite proxy target together. Preview Origin 4173 is also admitted. Example: `JOBHUNTER_DEV_PORT=15173 JOBHUNTER_PORT=18765 ./scripts/dev`.

The browser calls same-origin `/api`; Vite forwards it with the original Origin preserved. `JOBHUNTER_API_TARGET` is server-only Vite configuration, set by the launcher. No wildcard CORS is enabled. For frontend-only development, `npm run dev` in `frontend/` remains available with a separately configured API.

For temporary integration data, first create an empty directory with `mktemp -d` and supply its absolute path as `JOBHUNTER_DATA_DIRECTORY`. Do not seed or migrate a real workspace for a UI check. Existing schema migration remains an explicit backend operation.

Vite proxies `/api` to `http://127.0.0.1:8765`, rewriting Host and preserving Origin. The backend must explicitly admit `http://127.0.0.1:5173`; no wildcard, token, CORS bypass or frontend workspace creation is introduced. `localhost` is not an interchangeable origin. A stopped backend produces a read error, never a successful empty list.

`npm run build` creates `dist/`. `npm run preview` serves that build on `http://127.0.0.1:4173`, with the same API proxy; `./scripts/dev` admits this exact Origin as well. Preview is a local verification server, not production hosting. Production packaging and SPA fallback/API hosting remain future work.

## Structure and progressive adoption

Follow [repository-structure.md](../docs/development/repository-structure.md) and the selected [technology stack](../docs/development/technology-stack.md). Only actual consumers exist:

- `src/app/`: startup, Query provider, router, layout and shared theme tokens.
- `src/pages/job-pool/`: the Job Pool navigation entry and separate Manual Applications and Preferences pages.
- `src/features/manual-application-entries/`: typed operations, shared create/edit form, deletion, recovery and list presentation.
- `src/features/preferences/`: generated type aliases, response/admission validation, six-field editor and explicit Save recovery.
- `src/entities/manual-application-entry/`: generated entry type alias and read-response validation. No duplicate business authority.
- `src/pages/candidate-knowledge/` and `src/pages/resumes/`: Knowledge, Profile and Resume routes.
- `src/features/candidate/`: common command recovery, source-aware block editor, errors, read states and management dialogs. `features/evidence/`, `features/profile/` and `features/resume/` supply their actual editors and preview.
- `src/entities/profile/`, `src/entities/evidence/` and `src/entities/resume/`: generated aliases and consumed response/admission checks.
- `src/shared/api/`: generated Manual Applications, Preferences and Candidate transport types, typed `openapi-fetch` client and strict result classification.
- `src/shared/ui/` and `src/shared/lib/`: consumed page header, table, state panel, skeleton, form field, notices, buttons, Radix dialogs/menu and class-name helper.
- `tests/unit/`, `tests/component/`, `tests/e2e/`: admission/result rules, controlled recovery interactions and real backend Chromium flows.
- `scripts/generate-api.mjs`: reproducible OpenAPI generation and drift check.

React Router and TanStack Query have real consumers. Tailwind v4 uses its Vite plugin. `components.json` places shadcn-style primitives in the shared layer. React Hook Form with Zod and Radix Dialog/AlertDialog/DropdownMenu support the actual M1 forms and actions. Add/edit share one form; edit/delete share the saved-record summary; list states share presentational primitives. Zustand, Jobs, Fit, Agent and Application History are not scaffolded.

## Design references

The authoritative checked-out file is currently named [`docs/ui/DESGIN.md`](../docs/ui/DESGIN.md), although its own text calls it `DESIGN.md`. Preserve one authority; do not create a second design specification. Repository organization is currently named `repository-structure.md`, not `repository-architecture.md`.

Stitch project: **JobHunter Manual Applications UI**, ID `2149071149393619064`. Nine screen states were listed through its read-only MCP. The populated-list reference `0b12ea51e0e9435fac7e53f0ecfcc340` was inspected as a screenshot and HTML for shell/table proportions. Add, conflict, uncertain-result and delete screenshots were also inspected. The implementation maps the frozen grayscale, typography, 6–8px radii, quiet borders and localized state patterns into `src/app/bootstrap/styles.css`. Stitch assets, sample companies, credentials and generated page scripts are not shipped. The application uses local system fonts and Lucide icons, with no font/CDN requests.

Business/Contract/API authority takes precedence over visual examples. Future navigation/actions shown in Stitch are not offered as working features. Final visual sign-off and browser coverage beyond the recorded checks remain separate.

## Generated API and safeguards

```sh
npm run api:generate
npm run api:check
```

The generator imports the actual backend route composition using the root `.venv/bin/python`; run the backend's locked setup first. It composes the actual backend inside automatically removed temporary storage, without opening or migrating user data or starting a listener. ManualApplicationEntry, Preferences and the 19 saved Candidate authority paths with their reachable schemas are selected from the real OpenAPI document. `openapi-typescript` generates the checked-in `src/shared/api/schema.d.ts`; `openapi-fetch` supplies the typed transport. Changes to shared schemas are still detected. `api:check` compares regenerated content without writing; never hand-edit the generated file.

Zod checks success envelopes and editable fields. Client admission counts Unicode code points, uses the fixed Contract whitespace set, checks prohibited scalars and URL preconditions, and preserves submitted URL spelling. The backend remains the authority for full pinned WHATWG parsing. Server list order is preserved.

Query defaults disable automatic retries and focus/reconnect refetch; local requests use `networkMode: 'always'`. No draft or command is persisted. Each intentional create gets a request ID; an uncertain create can only be explicitly retried with the same in-memory ID and original fields. Unknown edits/deletes require reading current state. Conflicts preserve draft fields; adopting the current revision and saving are separate actions. Current absence does not prove which delete succeeded. Dirty/uncertain form dismissal requires confirmation, and interrupted-page guidance asks users to inspect the list.

Opening a URL creates a neutral context synchronously on the click, detaches its opener and installs a no-referrer policy before resolving the saved ID/revision. A noreferrer self-navigation uses only the resolved URL. A closed, blocked or user-navigated context is not replaced automatically; stale resolution never falls back to the cached URL. The UI reports navigation initiation, not remote loading or application success.

## Checks

```sh
npm run check
```

This runs API drift, strict TypeScript, ESLint, Prettier, Vitest/Testing Library and production build. `npm run format` formats maintained files; generated schema and lockfile are excluded. Backend checks remain at `./scripts/check` from the root and are separately owned.

The 80 unit/component cases cover read states, strict response classification, shared URL fixtures, Unicode admission, inline validation, draft retention, explicit revision adoption, identical uncertain-create retries and truthful deletion recovery, complete Preferences admission, nested original-index errors, explicit unlimited controls, retained input, historical replay and confirmed-Save/read-failure separation.

For the real backend/browser suite, install the locked backend environment first, then from `frontend/` run:

```sh
npx playwright install chromium
npm run test:e2e
```

The suite owns a temporary schema-5 workspace and loopback ports 15173 (Vite), 18765 (backend) and 18865 (destination/referrer probe); these ports must be free. It explicitly admits the test Origin, never reuses an existing server, and removes its temporary workspace on shutdown. Thirty-one Chromium tests include nine Manual Applications cases covering CRUD/reload, stale revisions, committed-but-lost create/update/delete responses, successful no-opener/no-referrer handoff, stale resolution and unavailable/closed waiting contexts. Six Preferences cases additionally cover first publication/reload/no-op, invalid and unadded input, concurrent Save, lost committed response with historical replay, follow-up read failure and dirty navigation. Sixteen Candidate cases cover all six Evidence kinds, Profile Save, exact-source initialization, preserved local expressions, retired historical sources, explicit conflict rebase, identical uncertain replay, atomic default replacement, fact persistence after draft discard and rich-text/Header ordering and all-or-nothing rejection of a source retired between selection and Save. They also cover direct Resume navigation, shared Profile modal publication followed by explicit Resume adoption, caret mark inheritance, whole-line list conversion and list continuation with persisted styled content. No external destination is visited. `playwright.config.ts` retains traces/screenshots only on failure; output is gitignored.

Manual 1280×720 inspection covered the populated list, add and delete dialogs with no warning/error logs. These checks do not certify all browsers, assistive technologies or final visual acceptance. See [current evidence](../docs/progress/traceability.md#frontend-foundation-evidence).

## Adoption sources

- [Vite guide](https://vite.dev/guide/): runtime/build and development setup.
- [shadcn Vite setup](https://ui.shadcn.com/docs/installation/vite): aliases, Tailwind and component placement.
- [OpenAPI TypeScript](https://openapi-ts.dev/introduction): generated TypeScript schemas.
- [TanStack Query defaults](https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults): explicit cache/refetch/retry policy.

Installed dependency versions and compatibility were verified by the checks above. Direct package metadata reports MIT licenses, except TypeScript, class-variance-authority and Playwright (Apache-2.0) and Lucide React (ISC). No external project source was copied wholesale; the local Button follows the documented shadcn composition approach.

## Preferences integration and visual evidence

The route is `/job-pool/preferences`. The editor follows PRF-001–023 and COM-033–037, using actual generated backend types. For an unconfigured workspace, company exclusions initially show UNLIMITED; saved configurations retain their stored choice. This UI default does not save automatically. Every Save sends all six choices and a fresh request identity; uncertain retries retain the identical original request. Current reads do not settle an earlier uncertain command. Historical success acknowledgements are followed by a separate current read; failed current reads preserve confirmed success. Explicit in-place abandonment of an uncertain request first requires a successful current read. No reset, history list, automatic Collection or local Job filter is exposed.

All seven Preferences references in Stitch project `2149071149393619064` were read through MCP: configured, unconfigured, validation, loading, read failure, revision conflict and uncertain Save. HTML supplied readable references where remote screenshots were blank. Shared Input, TagInput and ViewTabs extend existing primitives without new dependencies or speculative directories. Manual 1280×720 browser inspection covered unconfigured, validation and saved forms, six sections and the sticky action bar, with no horizontal overflow. Final visual acceptance and broader browser/accessibility coverage remain separate. See [M2 frontend evidence](../docs/progress/traceability.md#m2-frontend-evidence).

## Knowledge and Resume integration

The routes are `/candidate-knowledge`, `/candidate-knowledge/profile`, `/candidate-knowledge/evidence/new/:kind`, `/candidate-knowledge/evidence/:id/edit`, `/resumes`, `/resumes/new` and `/resumes/:id/edit`. Add/edit reuse the same six-kind Evidence form. Profile and Resume editors share controls, errors, dirty navigation and explicit command recovery; plain Evidence and rich Resume expressions share one continuous Tiptap/ProseMirror editor. The required MIT-licensed Tiptap packages are pinned to 3.31.3; no empty future feature directories were introduced. Route-level lazy loading keeps editor code out of unrelated initial page loads.

All 68 additional Candidate design states were enumerated through Stitch MCP and their HTML references inspected. Variants use one consistent filter, form and dialog system under DESGIN.md. Unsupported screenshot controls do not become business operations. Manual browser inspection covered empty Knowledge, source selection, creating a fact within Resume, saved editing and scaled preview at 1280 pixels, with overflow checks at 1280 and 900 pixels and no console warning/error during the inspected flow. This is not pixel approval of every reference or certification of all browsers/assistive technologies.

Candidate commands retain an immutable request for explicit uncertain replay. Later rejection/current equality does not settle an earlier unknown result. Confirmed command success survives follow-up read failure. Exact Profile/Evidence references feed the preview; new source adoption preserves local wording/marks/links unless replacement is explicitly selected. Source updates do not propagate automatically. New facts commit to Knowledge before inclusion, so discarding a Resume does not undo them. Default removal displays the next/previous replacement from the observed ordered list and sends both revisions. The local preview uses the browser's available fonts and fixed A4 width/template; it is not the Materials PDF renderer and makes no export-ready claim.

Resume rows open editing directly. The outline “编辑个人信息” action opens the shared Profile form without leaving the draft. Saving publishes Profile to Knowledge; “应用到当前简历” explicitly selects that saved version for the Resume draft, which still requires Resume Save. Font, size, line spacing and color controls share a compact row above the preview.

The full-width continuous editor shows inline marks and flat lists while typing. Toolbar controls preserve selection, support undo/redo, and apply list changes to whole selected lines. Evidence remains plain text with flat lists; only Resume expressions allow bold/italic/underline and selected links. The adapter round-trips the owned AST, keeps literal text, ignores empty editing placeholders, and never sends editor HTML/JSON to the API. Clipboard content is inserted as plain text. Adapter tests cover these transport boundaries. See the [official React setup](https://tiptap.dev/docs/editor/getting-started/install/react) and [StarterKit options](https://tiptap.dev/docs/editor/extensions/functionality/starterkit) for the consumed editor setup.

[Candidate frontend evidence](../docs/progress/traceability.md#candidate-frontend-evidence) records scope and remaining acceptance. No backend source or user data was changed by this frontend task.
