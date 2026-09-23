# Evaluation and Observability Contract — Deterministic M1 Boundaries

> English is authoritative. Normative scope revision: **2026-09-23.S3M1-r1**. This body specifies required deterministic evidence, not executed acceptance. Semantic quality, production Provider SDKs, judge independence, telemetry integration and broader Eval remain pending under their consuming milestones.

[Index](../index.md) · [Decision source](../../design/contract/sl-03-m1-grill.md) · [Runtime](../agent/execution-runtime.md) · [Acceptance](../../acceptance.md#92-crash-and-cancellation-boundaries) · [Eval procedure](../../development/evaluation.md)

<a id="evo-001"></a>
**EVO-001.** **Real component evidence.** M1 acceptance MUST exercise the actual Runtime and persistence components with controlled adapters, temporary stores and deterministic fault injection. Pure mocks of the Runtime are insufficient. Controlled data-only formats require golden logical-object→exact UTF-8/length/hash fixtures covering their actual Unicode, number, key-order and escaping rules. A fixture format is not the production Provider schema. Count actual adapter calls and prove no hidden retry/fallback within this boundary; real production SDK verification is M2 work.

Decision sources: CG05-Q1, CG05-Q56, CG05-Q77, CG05-Q88, CG05-Q90, CG05-Q116.

<a id="evo-002"></a>
**EVO-002.** **Authority and uncertain dispatch proof.** Exercise first grant, revoke without increment, regrant, overflow refusal, stale revoke and competing grants. Prove an original live winner with confirmed intent commit and no adapter entry may continue after acknowledgement uncertainty, while crash/restart, copied context, another path or lost proof cannot reuse that intent. Include grant acknowledgement uncertainty: matching persisted owner/generation alone cannot authorize a second path. Assert stale/new generations cannot first-publish the original generation's response, and PREPARED proven undispatched recovery uses fresh current authority.

Decision sources: CG05-Q5, CG05-Q15, CG05-Q27, CG05-Q28, CG05-Q31, CG05-Q66, CG05-Q77, CG05-Q85, CG05-Q112, CG05-Q113, CG05-Q126.

<a id="evo-003"></a>
**EVO-003.** **Response publication and byte proof.** Inject faults around response receipt, atomic persistence, acknowledgement and local processing. Prove one immutable response, complete-byte verification, deterministic format rejection, Invocation-derived format authority and exactly the original four-field publication result on confirmation. Verify same-byte confirmation after ending/revocation/deadline, different-byte conflict, and corruption/absent-reader distinctions without confirmation-side writes. Exercise competing identical/different publishers and uncertain commits against real durable state; never repair by another remote request.

Decision sources: CG05-Q8, CG05-Q10, CG05-Q19, CG05-Q39, CG05-Q45, CG05-Q46, CG05-Q56, CG05-Q89, CG05-Q91, CG05-Q92, CG05-Q93, CG05-Q94, CG05-Q118, CG05-Q125, CG05-Q130.

<a id="evo-004"></a>
**EVO-004.** **Ending and recovery proof.** Exercise cancellation/response races, first-ending arbitration, whole-Run consumer completion, sibling fencing, ownerless coordination versus concurrent claim and already-committed business results without unnecessary response access. Distinguish permitted bounded postdeadline local recovery from forbidden new remote dispatch/late first publication. Inject missing/corrupt payload, missing reader/consumer, format-invalid bytes, storage unreadability and failed ending persistence; assert correct convergence or honest unresolved outcome, no replay, no unrelated application failure and no fictitious terminal state. Include OPEN with no Invocation and consumer UNRESOLVED/DENY mappings; missing denial mapping must prevent enabling that recovery path.

Decision sources: CG05-Q30, CG05-Q35, CG05-Q36, CG05-Q58, CG05-Q62, CG05-Q63, CG05-Q64, CG05-Q69, CG05-Q71, CG05-Q72, CG05-Q73, CG05-Q74, CG05-Q82, CG05-Q83, CG05-Q95, CG05-Q104, CG05-Q105, CG05-Q111, CG05-Q127, CG05-Q128.

<a id="evo-005"></a>
**EVO-005.** **Size and incomplete-remote evidence.** Show full serialized-envelope size accounting at the captured limit. Confirmed complete remote termination plus oversized serialized response must produce atomic FAILED/RESPONSE_TOO_LARGE and rejection evidence without a body. An early buffer cutoff before terminal evidence must preserve remote uncertainty and null rejection marker. Cancellation or another ending that won first must remain unchanged. No unbounded draining, truncated durability, replay or zero-usage assumption may be used to pass these cases. Bounded reception is permitted; obtaining terminal evidence must not require continuing beyond resource limits.

Decision sources: CG05-Q48, CG05-Q68, CG05-Q76, CG05-Q87, CG05-Q99, CG05-Q101, CG05-Q102.

<a id="evo-006"></a>
**EVO-006.** **Controlled Tool proof.** Instantiate one typed controlled exact-version local-read action agreement with exact inputs, current permission, completion/result evidence, required dependency failures and replay conditions. Prove valid result reuse, safe unfinished same-Invocation re-execution under fresh qualification and immutable inputs, and refusal for missing permission/required sources or unknown action recovery. Prove the action performs no hidden Ensure, remote parse or business write, and lineage-only refs do not become extra payload dependencies. No production Tool catalog or universal side-effect mechanism is required.

Decision sources: CG05-Q70, CG05-Q116, CG05-Q121, CG05-Q122, CG05-Q123, CG05-Q124.

<a id="evo-007"></a>
**EVO-007.** **Storage and evidence accounting.** Prove forward migration from the actual preceding head preserves prior consumer data/receipts and introduces no historical Run/Invocation backfill. Test OPEN payload protection, terminal retention in M1, ownership recovery, rollback/commit uncertainty and wall-clock rollback without fabricated ordering. Run maintained applicable prior-consumer regression checks. Record requirement→code/test mappings and actual commands/outcomes separately from Contract review; normative publication alone MUST NOT claim executed migrations, Runtime acceptance, semantic capability or parent-Slice completion.

Decision sources: CG05-Q49, CG05-Q51, CG05-Q80, CG05-Q88, CG05-Q119.
