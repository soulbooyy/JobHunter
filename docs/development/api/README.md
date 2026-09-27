# API integration guides

These guides distinguish implemented HTTP interfaces from explicitly labeled revised target interfaces for frontend integration and internal Python interfaces for backend consumers. They are derived references, not new normative Contracts, milestone summaries or implementation-status ledgers. English is authoritative; [Contracts](../../contracts/index.md) own semantics and [Progress](../../progress.md) records availability and verification.

| Guide | Interface |
| --- | --- |
| [SL-01.M1 — Local Workspace and Manual Application Entries](sl-01-m1.md) | Local access configuration, entry CRUD, revision/idempotency, URL resolution and frontend recovery obligations |
| [SL-01.M2 — Preferences](sl-01-m2.md) | Complete configuration, immutable versions, Save/replay, nested errors and client recovery |
| [SL-02.M1 — Independent Resume and portrait](sl-02-m1.md) | Implemented schema-7 Resume/ID/Save/default/Evidence plus Entry-scoped frozen planning and zero-call reuse; protected model consumer and revised frontend remain pending |
| [SL-02.M2 — Saved Resume Materials](sl-02-m2.md) | Direct-source/schema-2 manifest target; surviving exact demand, verified PDF/PNG and polling/replay integration |

The running backend serves generated OpenAPI at `/openapi.json`. OpenAPI describes HTTP routes only; the former internal Invocation guide has been deleted with its withdrawn scope. Keep each guide aligned with its owning Contracts and actual interface definitions; do not use examples to introduce additional fields or behavior. Installation and startup commands live in [backend/README.md](../../../backend/README.md).
