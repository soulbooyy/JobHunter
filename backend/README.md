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

Startup prints one JSON diagnostic with outcome, physical directory and schema version, or a sanitized Contract error followed by exit 1. No business listener starts before storage checks. No startup HTTP resource exists. Port binding failure is not workspace recovery and never selects another store. Stop with Ctrl-C. The ownership guard stays held through server shutdown; process death releases it. Lock files live in `/tmp/jobhunter-locks-<uid>/`, keyed by physical device/inode, and are deliberately not unlinked on release (unlinking could split ownership). Directory and database permissions are 0700/0600; the launcher uses umask 0077.

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

The current runtime initializes and serves **schema 2**, retaining M1 Entry behavior. Schema 1 is recognized but ordinary startup fails with `SCHEMA_UNSUPPORTED`; stop the backend and explicitly migrate the selected existing directory:

```sh
uv run --locked python -m jobhunter.bootstrap.migrate \
  --data-directory "/absolute/existing/data-directory"
```

Migration uses the runtime's physical-directory lock, without a listener or directory/database creation. Success prints `outcome: MIGRATED` or `UNCHANGED`, the resolved `data_directory` and `schema_version: 2`. Failure prints the sanitized Common error and exits nonzero. The migration fully recognizes source/target structure, preserves M1 rows and receipts, adds no Preference business rows, and advances DDL/product/Alembic metadata in one explicit transaction. Uncertain completion is resolved by reopening and recognizing the complete source or target; it never replays the upgrade. Do not use standalone Alembic, downgrade, delete residue or stamp metadata to bypass recognition. The schema-1 definitions and revision `b720a94fd381` remain frozen; `cd891047a2e6` adds schema 2 in the same revision directory.

Every connection enables and verifies `foreign_keys=ON` before beginning a transaction. Deferred composite references enforce root/current/version/receipt ownership, including the cyclic first publication. SQLite requires this per-connection admission and checks deferred references at commit; see [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html). Recognition also runs `foreign_key_check` and admits stored business values. JSON formatting/key order is representation only. The supported runtime/dependency versions above were rechecked unchanged for this consumer; no new dependency was needed.

Preferences exposes only:

- `GET /api/v1/preferences`: unconfigured or one consistent root/current-version observation.
- `POST /api/v1/preferences/save`: complete Save with `request_id`, explicit nullable `revision`, and six-field `configuration`.
- `GET /api/v1/preferences/versions/{preference_set_version_id}`: retained exact version.

See the [Preferences API integration guide](../docs/api/sl-01-m2.md), generated `/openapi.json`, and derived [Save fixture](tests/fixtures/preference_save.json). Domain admission is under `domain/preferences/`, application coordination under `application/candidate/`, SQL under `infrastructure/persistence/sqlalchemy/repositories/`, and HTTP under `api/v1/preferences/`. Shared Common scalars now live in `domain/shared/values.py`; Entry URL rules remain Entry-owned.

Preferences transport enforces a streaming 1 MiB body budget, duplicate decoded object-key rejection, compatible UTF-8 JSON media type and identity-only Content-Encoding. The stricter transport is isolated from M1. Input OpenAPI arrays describe the 1000-item raw budget with canonical-capacity extensions; output schemas describe canonical capacities. Save equality/fingerprints share canonical admission; JSON serialization is not equality. Lifetime receipts include no-op outcomes. A retry returns the original success, even after later publications, and never resets current. Preserve the full original request after uncertain outcomes; only an explicit retry with that same request establishes its result. Current reads do not establish a prior request's outcome.

No Collection, QuickScreen, history-list/restore/reset or frontend behavior is supplied by these operations. Backend conformance and M1 regression evidence lives in [traceability §8](../docs/progress/traceability.md#8-sl-01m2-backend-implementation-evidence); browser/client generation and whole-milestone acceptance remain separate.
