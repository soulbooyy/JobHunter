# Backend development and operation

## Installation and supported runtime

Run commands from the repository root. Supported and verified host: macOS 26.6.2, arm64; uv 0.11.23; uv-managed CPython 3.12.13; bundled SQLite 3.53.1; Homebrew ICU 78.1. Other operating systems/filesystems are not certified. The supported launcher below uses a single process, no reloader/workers. Do not deploy this API to a network interface.

The environment needs uv, Xcode command-line build tools and Homebrew `icu4c@78` (already installed on the verified host). The ICU binding compiles during installation. Run:

```sh
cd /Users/soulboy/projects/JobHunter
export CMAKE_PREFIX_PATH="$(brew --prefix icu4c@78)"
export ICU_ROOT="$CMAKE_PREFIX_PATH"
uv sync --locked
uv run --locked python -m jobhunter.main
```

`.python-version` selects Python 3.12.13. `uv.lock` locks all resolved dependencies; direct dependencies are pinned in `pyproject.toml`. Final adopted versions: FastAPI 0.135.1, Starlette 0.52.1, Pydantic 2.13.5 / pydantic-core 2.46.5, SQLAlchemy 2.0.54, Alembic 1.20.0, Uvicorn 0.53.0, urlstd 2023.7.26.1, icupy 0.22.0, AnyIO 4.12.1. Development: pytest 9.1.1, httpx 0.28.1, Ruff 0.16.8, Pyright 1.1.414. Installed package metadata declares MIT except Uvicorn, Starlette and httpx (BSD-3-Clause). No external project source was copied.

The binding needs the ICU build paths above. A sandboxed runner may need permission to download dependencies and bind loopback; do not skip real HTTP tests. Set `UV_CACHE_DIR` to a writable cache location if the default cache is unavailable.

## Startup configuration

| Variable | Default and meaning |
| --- | --- |
| `JOBHUNTER_DATA_DIRECTORY` | Absent: `~/Library/Application Support/JobHunter`; absent default may be created. Explicit value must name an existing absolute directory. Relative/missing/unavailable explicit locations fail. |
| `JOBHUNTER_BIND` | `127.0.0.1`; only this or `::1` is accepted. |
| `JOBHUNTER_PORT` | `8765` |
| `JOBHUNTER_ALLOWED_HOSTS` | Exact bind authority including port, e.g. `127.0.0.1:8765`; comma-separated explicit local aliases only. |
| `JOBHUNTER_ALLOWED_ORIGINS` | Empty; no browser Origin admitted until explicitly configured. Comma-separated exact local HTTP(S) origins; no wildcard. Non-browser requests may omit Origin. |

A temporary workspace can be started without touching user data:

```sh
data_dir="$(mktemp -d)"
JOBHUNTER_DATA_DIRECTORY="$data_dir" uv run --locked python -m jobhunter.main
```

Startup prints one JSON diagnostic with outcome, physical directory and schema version, or a sanitized Contract error followed by exit 1. No business listener starts before storage checks. No startup HTTP resource exists. Port binding failure is not workspace recovery and never selects another store. Stop with Ctrl-C. The ownership guard stays held through server shutdown; the last process holding its inherited file description releases it on exit. Lock files live in `/tmp/jobhunter-locks-<uid>/`, keyed by physical device/inode, and are deliberately not unlinked on release (unlinking could split ownership). Directory and database permissions are 0700/0600; the launcher uses umask 0077.

An existing nonempty directory must pass integrity, application ID, product version, exact versioned application-table constraints and Alembic metadata checks. Extra indexes are allowed. Ordinary runtime opening never creates a missing database or runs migration/repair. Failed initialization leaves residue that must be inspected separately; restarting does not auto-initialize it. Do not delete unknown contents to make startup work. The only revision history is `backend/alembic/versions/`; initial revision is `b720a94fd381`. Standalone Alembic execution is disabled: its environment requires the bootstrap-owned connection.

## Application and interface entry points

Source and tests follow the [required repository organization](../docs/development/repository-structure.md). `jobhunter.main` composes the local backend through `bootstrap/`; business admission, Application use cases, persistence and HTTP adapters live in their respective layers.

The six Contract operations are at `/api/v1/manual-application-entries`: POST create, GET complete list, GET/PUT `/{manual_application_entry_id}`, POST `/{manual_application_entry_id}/delete` and POST `/{manual_application_entry_id}/resolve-url`. All successful operations return HTTP 200 with the exact Contract object. OpenAPI is served at `/openapi.json` under the same Host/Origin admission. Interactive Swagger/ReDoc pages are disabled.

```sh
curl http://127.0.0.1:8765/openapi.json
curl http://127.0.0.1:8765/api/v1/manual-application-entries
```

OpenAPI is generated from the actual routes/DTOs, not a second specification or a hand-maintained client. Raw request numbers are decoded with Decimal before Pydantic admission; integer-valued spellings such as `1.0` work without accepting rounded fractions. Input text schemas describe post-trim limits using `x-post-trim-maxLength`; a raw `maxLength` would incorrectly reject legal padded input. Result schemas retain canonical length constraints. URL validation preserves admitted spelling and uses urlstd's validation-error reporting plus Contract checks, including strict IPv4 spelling that the parser alone failed to enforce. No target request, DNS lookup, redirect following or browser action is performed.

Derived language-neutral cases: `backend/tests/fixtures/manual_application_entry_admission.json`, exercised by `backend/tests/conformance/test_admission_fixtures.py`. These are examples under the Contracts, not exhaustive normative definitions. Future clients must preserve exact integer semantics, Unicode scalar/code-point semantics, trim behavior and URL spelling; generator defaults cannot override them.

## Transactions, uncertainty and privacy

The driver uses `isolation_level=None` with explicit SQL `BEGIN IMMEDIATE` for writes and bootstrap, and `BEGIN` for reads. This follows the [SQLAlchemy SQLite transaction guidance](https://docs.sqlalchemy.org/en/20/dialects/sqlite.html#serializable-isolation-savepoints-transactional-ddl) while keeping the Application transaction boundary explicit. Alembic shares the bootstrap connection; DDL, both application PRAGMAs and its revision row commit together. Tests interrupt every initialization stage and inspect the actual SQLite file.

Initialization explicitly selects DELETE journaling; connections verify it and set/read back synchronous EXTRA and fullfsync ON. The supported store uses these settings; unsupported manually changed journal configurations fail rather than silently weaken durability. See [SQLite synchronous documentation](https://www.sqlite.org/pragma.html#pragma_synchronous). Acknowledged commits are tested across process exit, not destructive hardware power-loss experiments.

Create entry/receipt and revision checks are serialized inside one short transaction. There is no automatic command replay or COMMIT retry. Failure before commit with confirmed rollback returns STORAGE_UNAVAILABLE. Failed COMMIT with SQLite's documented BUSY result is explicitly rolled back through the driver and returns STORAGE_UNAVAILABLE; wrapper transaction state is not treated as evidence. Other ambiguous completion failures and post-commit response failures require verification via OUTCOME_UNKNOWN. [SQLite transaction semantics](https://www.sqlite.org/lang_transaction.html) support the BUSY distinction. Read/current state cannot reconstruct edit history.

Ordinary access/SQL debug logs are disabled in the launcher; validation and error responses never include values, exception text or unknown field names. urlstd validity objects disable parser logging and remain transient. No network adapter, telemetry upload, model SDK or browser executor is installed by M1.

## Checks and evidence limits

```sh
uv sync --locked
./scripts/check
```

The unified entry runs Ruff lint/format, Pyright strict (source, migration, tests and scripts), pytest including real loopback subprocess HTTP, requirement-ID/matrix-reference checks and `git diff --check`. Use temporary local directories only. See [Progress evidence](../docs/progress/traceability.md#7-sl-01m1-backend-implementation-evidence) for final results and exact requirement mappings.

Tests establish the executed boundaries recorded in traceability, not arbitrary hardware-failure immunity or browser behavior. Configure any future browser origin explicitly, e.g. `JOBHUNTER_ALLOWED_ORIGINS=http://localhost:5173` only if that is the selected origin. Contract documents remain the normative source; this README maintains operating instructions, not milestone status or implementation history.

## Preferences and explicit schema evolution

The current runtime initializes and serves **schema 5**, retaining Entry and Preferences behavior. Schemas 1, 2, 3 and 4 are recognized but ordinary startup fails with `SCHEMA_UNSUPPORTED`; stop the backend and explicitly migrate the selected existing directory:

```sh
uv run --locked python -m jobhunter.bootstrap.migrate \
  --data-directory "/absolute/existing/data-directory"
```

Migration uses the runtime's physical-directory lock, without a listener or directory/database creation. Success prints `outcome: MIGRATED` or `UNCHANGED`, the resolved `data_directory` and `schema_version: 5`. Failure prints the sanitized Common error and exits nonzero. The migration fully recognizes source/target structure, preserves Entry/Preferences rows and receipts, adds no Preference business rows, atomically seeds Profile/empty Evidence Baseline/default selection, and advances DDL/product/Alembic metadata in one explicit transaction. Uncertain completion is resolved by reopening and recognizing the complete source or target; it never replays the upgrade. Do not use standalone Alembic, downgrade, delete residue or stamp metadata to bypass recognition. The schema-1 definitions and revision `b720a94fd381` remain frozen; `cd891047a2e6` adds schema 2 and remains frozen too. Revision `ef03c92ba671` adds schema 3 in the same revision directory; `a41d7e90c263` adds Materials schema 4 without backfilled demand. Revision `d092ea64bf17` adds schema 5 for internal invocation durability without backfilling historical Runs or Invocations. Schema 1 upgrades through all later revisions in one outer transaction.

Every connection enables and verifies `foreign_keys=ON` before beginning a transaction. Deferred composite references enforce root/current/version/receipt ownership, including the cyclic first publication. SQLite requires this per-connection admission and checks deferred references at commit; see [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html). Recognition also runs `foreign_key_check` and admits stored business values. JSON formatting/key order is representation only. The supported runtime/dependency versions above were rechecked unchanged for this consumer; no new dependency was needed.

Preferences exposes only:

- `GET /api/v1/preferences`: unconfigured or one consistent root/current-version observation.
- `POST /api/v1/preferences/save`: complete Save with `request_id`, explicit nullable `revision`, and six-field `configuration`.
- `GET /api/v1/preferences/versions/{preference_set_version_id}`: retained exact version.

See the [Preferences API integration guide](../docs/api/sl-01-m2.md), generated `/openapi.json`, and derived [Save fixture](tests/fixtures/preference_save.json). Domain admission is under `domain/preferences/`, application coordination under `application/candidate/`, SQL under `infrastructure/persistence/sqlalchemy/repositories/`, and HTTP under `api/v1/preferences/`. Shared Common scalars now live in `domain/shared/values.py`; Entry URL rules remain Entry-owned.

Preferences transport enforces a streaming 1 MiB body budget, duplicate decoded object-key rejection, compatible UTF-8 JSON media type and identity-only Content-Encoding. The stricter transport is isolated from M1. Input OpenAPI arrays describe the 1000-item raw budget with canonical-capacity extensions; output schemas describe canonical capacities. Save equality/fingerprints share canonical admission; JSON serialization is not equality. Lifetime receipts include no-op outcomes. A retry returns the original success, even after later publications, and never resets current. Preserve the full original request after uncertain outcomes; only an explicit retry with that same request establishes its result. Current reads do not establish a prior request's outcome.

No Collection, QuickScreen, history-list/restore/reset or frontend behavior is supplied by these operations. Backend conformance and M1 regression evidence lives in [traceability §8](../docs/progress/traceability.md#8-sl-01m2-backend-implementation-evidence); browser/client generation and whole-milestone acceptance remain separate.

## Saved candidate authority

The backend now exposes Profile, six-kind Evidence/Baseline, Resume exact history and default selection. See the [candidate API guide](../docs/api/sl-02-m1.md) and live OpenAPI for all nine commands and ten reads. Implementations are in `domain/profile`, `domain/evidence`, `domain/resume`, `domain/workspace`, `application/candidate/authority.py`, `api/v1/candidate` and the candidate SQL models/repository. The Materials extension below adds isolated rendering; no AI invocation or frontend dependency is installed.

Schema 3 initializes exactly one Profile with an all-null first Version, a real empty Evidence Baseline/current pointer and null default selection/revision 1. Mandatory records are checked before listening and never synthesized by reads. Retained Versions, relational source memberships and receipt exact references survive retirement/removal. Content JSON never replaces constrained lineage. Command-time root/selection snapshots preserve replay results independently of current state. New/switched source currentness, root/selection revisions, capacities and successful receipts share a short `BEGIN IMMEDIATE` transaction. No-op publishes only a receipt.

The candidate HTTP parser independently adds the specified streaming byte limits and parse-time depth/node budgets; existing Entry/Preferences parser protocols are preserved. Raw numbers remain Decimal until admission. The language-neutral [fingerprint example](tests/fixtures/candidate_fingerprint.json) is a derived example, not a second Contract. Tests cover real SQLite/Application/HTTP boundaries, migration/process interruption, publication/receipt failures, replay, concurrency, capacities, exact references and sanitization. Current evidence and frontend limitations are in [traceability](../docs/progress/traceability.md#saved-candidate-backend-evidence).

No real user directory was migrated during development. For an existing schema-1/2/3 directory, stop the owning backend, run the explicit migration command above, then restart with `uv run --locked python -m jobhunter.main`. Use configured loopback Host/Origin values unchanged; frontend origin admission remains explicit.

## Saved Resume Materials

Schema **4** adds retained RenderConfigurations, exact RenderIntents, private fenced Work, Artifacts/provenance and the independent Materials receipt namespace. Six operations and client obligations are documented in the [Materials API guide](../docs/api/sl-02-m2.md). Source ownership remains unchanged: the renderer consumes exact Resume local content, exact Profile and ordered Evidence structured fields, not unused Evidence expression. Existing schema 1/2/3 is recognized but never silently migrated.

```sh
uv sync --locked
# Explicit one-time official font download + verified deterministic build (several minutes):
uv run --locked python scripts/install_render_fonts.py
# Existing data only: stop its backend, then use the existing explicit migration entry:
uv run --locked python -m jobhunter.bootstrap.migrate --data-directory /absolute/existing/directory
# Start using the default local data directory, or set JOBHUNTER_DATA_DIRECTORY explicitly:
uv run --locked python -m jobhunter.main
```

Fresh explicitly selected directories must already exist and be empty. No real user data was opened or migrated during this implementation. Backend binding remains `127.0.0.1:8765`, with the existing explicit Host/Origin environment settings. For example, add `JOBHUNTER_ALLOWED_ORIGINS=http://localhost:5173` only when that is the actual frontend origin.

The verified renderer is WeasyPrint 70.0 → PDFium via pypdfium2 5.13.0 → Pillow 12.3.0, with fontTools 4.65.0 and pypdf 6.19.0. Rendering is currently certified only for macOS 26.6.2 arm64 / Python 3.12.13 and the exact Homebrew native-library hashes in [pipeline.json](assets/rendering/pipeline.json). Existing Pango/Harfbuzz/Fontconfig/Freetype libraries were reused; this task did not install system packages. The worker supplies `/opt/homebrew/lib` explicitly and uses an isolated Fontconfig file with no host font directories. Updating output-affecting dependencies/platform requires validation and a new pipeline/configuration identity, not editing a retained configuration in place. Missing or changed dependencies make configurations unavailable; they do not disable the rest of the API. PDFium is PNG-only; Pillow is also imported by WeasyPrint and is required for both formats.

Font binaries are separately installed under ignored `backend/assets/rendering/fonts/`. Reviewed source URLs, original/final SHA-256 values, role mappings, deterministic 12° outline shear and licenses are versioned under [rendering assets](assets/rendering/README.md). Installation verifies official inputs and reconstructed final hashes; it never rewrites the catalog. The final 16-role build was reconstructed and compared to the manifest. Fonts are not fetched by startup, requests or rendering. Network links in documents remain inert data except for admitted PDF link annotations. Exact original URI values are written into final annotations after layout to prevent the renderer library from normalizing Unicode addresses.

Initial captured Work defaults: 3 attempts, 50 pages, 100,000,000 PNG pixels, 50,000,000 output bytes, 60,000 ms; concurrency is 1. Actual multi-page/all-font fixtures complete within this budget on the verified host. A4 is 210×297 mm, margins 18 mm; body size/line-height and heading theme color come from Resume. Template v1 uses English section/header/degree labels, stored structured-field order, supplied date bounds only (null never invents “Present”), and preserved local whitespace/marks. PNG stacks every full page at 1120×1584 per page, with opaque white background. Unsupported visible glyphs fail rather than falling back.

The lifespan worker discovers the durable queue, claims a fresh attempt and launches one isolated subprocess. The child inherits the Workspace ownership lock: parent death does not let a replacement process overlap the still-live renderer. Timeout revokes the attempt, terminates/kills and waits for real exit before releasing the slot. Startup recovers abandoned RUNNING work only after acquiring that ownership. Known failures terminate the Work; only abandoned attempts consume captured recovery opportunities. An uncertain claim/terminal commit stops that execution epoch; restart reacquires ownership, validates durable state and reconciles before further execution. It never replays the user command automatically.

The Coordinator independently validates the final returned bytes after renderer exit. It places bytes without overwriting, flushes/fsyncs them (including macOS fullfsync for the file and directory syncs), then commits Artifact, Work and all pending Intents in one database transaction. Reads verify an opened regular file into a private stable snapshot before success headers. Orphans from failed/uncertain publication are retained conservatively; automatic payload deletion/GC is not implemented. They are not public Artifacts and cannot be discovered through API guesses. Hardware power-loss behavior has not been destructively tested.

Run `./scripts/check` for lint/format, strict typing, real SQLite/process/HTTP and real renderer tests. The rendering tests require the installed fixed fonts and verified native runtime; a dependency-free checkout can serve non-render APIs but cannot pass actual renderer conformance. Frontend client generation, browser preview/download and whole-milestone acceptance remain separate work.


## Internal invocation durability and recovery

See the [internal API integration guide](../docs/api/sl-03-m1.md) for operation signatures, typed results, controlled consumer agreements and an executable temporary-Workspace example.

The bootstrap composes one `jobhunter.agent.harness.runtime.Runtime` per owned Store lifetime, with a fresh UUIDv4 runtime instance. Startup fences former execution owners before announcing readiness, reconciles OPEN Runs and keeps unresolved affected operations stopped. Missing historical consumers/readers are scoped failures. No Run/Invocation HTTP routes, frontend, production Provider SDK, scheduler, LangGraph or telemetry integration is installed. Materials retains its separate runner, attempt and subprocess lifecycle.

Internal operations return `Success`, `Rejected` or `Unresolved`; callers must inspect the variant and code. `OUTCOME_UNKNOWN` preserves a stable identity and never authorizes command or remote replay. The SQLite adapter performs one fresh read to reconcile an uncertain write, without retrying the command or COMMIT. A live grant/intent winner carries local arbitration evidence; reading matching authority is insufficient. Use `Runtime.model_path` around intent and send: its context is unique, thread/task-bound, noncopyable and lost on exit. A later path cannot consume an existing intent. Adapter entry occurs at most once and rechecks current authority. Physical interruption is best effort; logical fences govern publication.

Controlled agreements are defined in `application/invocation/controlled.py` and `domain/invocation/format.py`:

- `controlled.model.v1` permits at most two MODEL Invocations and completes only after **both** exact responses pass local validation and the controlled proof commits. One saved response is insufficient.
- `controlled.read.v1` permits one `controlled.response-read.v1` TOOL. It retains the exact source Invocation and optional audit-only lineage, reads already-durable local bytes, and records their verified digest/length. It performs no Ensure, parsing, business write or network request. An unfinished read may recover the same Invocation; valid committed results are reused.
- Both require an established deadline before execution. The controlled local recovery window ends at the original deadline plus 30 seconds, across restarts; a live monotonic floor also prevents wall-clock rollback from renewing elapsed time. No new dispatch or first response publication is allowed after the original deadline. No protection against arbitrary clock changes across restart is claimed.
- Permission denial, unavailable source and unknown action use their explicit controlled failure mappings; malformed stored records are persistence integrity failures. Unknown reads remain unresolved. These are controlled proof agreements, not defaults for future business consumers.
- `controlled.response.v1` stores exactly `terminal`, `text`, `ordinal` in that order: compact UTF-8 JSON, scalar text, JSON escaping, exact nonnegative safe integer, no BOM/trailing newline/duplicate keys. `STOP` and `LIMIT` are complete terminal outcomes. The snapshotted byte limit includes the entire representation; finite reception holds at most `2 * max_response_bytes + 256` bytes and admits at most `max_response_bytes + 1` frames, checking deadline/authority between frames. A cutoff before terminal evidence stays unknown. Complete oversized output retains only rejection evidence and the atomic failure, never the body.

Captured byte limits use exact decimal text in SQLite, preserving values beyond its signed 64-bit INTEGER range without REAL rounding. Domain projections still expose exact integers. Response BLOBs, actual SHA-256/length and phase publish atomically. Identical historical confirmation is a read-only byte comparison even after ending, expiry or reader removal. All OPEN and terminal payloads are retained; no purge or Pin subsystem exists. Raw reads never repair data or end Runs. Runtime diagnostics and returned failures contain no submitted payload, SQL parameters or transport exceptions.

Use the same startup and explicit offline migration commands above. The maintained verification command is:

```sh
UV_CACHE_DIR=/tmp/jobhunter-uv-cache ./scripts/check
```

Checks use temporary stores, controlled clocks/adapters and real SQLite/process boundaries. Real loopback HTTP regression requires local socket permission. [Invocation evidence](../docs/progress/traceability.md#invocation-backend-evidence) records executed commands, outcomes and the production/semantic boundaries that remain unimplemented.
