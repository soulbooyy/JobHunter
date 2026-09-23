# API integration guides

These guides describe implemented HTTP interfaces for frontend design and integration. They are derived references, not new normative Contracts, milestone summaries or implementation-status ledgers. English is authoritative; [Contracts](../contracts/index.md) own semantics and [Progress](../progress.md) records availability and verification.

| Guide | Interface |
| --- | --- |
| [SL-01.M1 — Local Workspace and Manual Application Entries](sl-01-m1.md) | Local access configuration, entry CRUD, revision/idempotency, URL resolution and frontend recovery obligations |
| [SL-01.M2 — Preferences](sl-01-m2.md) | Complete configuration, immutable versions, Save/replay, nested errors and client recovery |
| [SL-02.M1 — Saved Profile, Evidence and Resume](sl-02-m1.md) | Exact sources, nine atomic commands, historical receipts, default selection and client integration boundaries |

The running backend serves generated OpenAPI at `/openapi.json`. Keep each guide aligned with its owning Contracts, actual routes and generated schemas; do not use examples to introduce additional fields or behavior. Installation and startup commands live in [backend/README.md](../../backend/README.md).
