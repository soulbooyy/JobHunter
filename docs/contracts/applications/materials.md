# Materials Contract — Saved Source Boundary

> English is authoritative. Normative scope revision: **2026-09-21.S2M1-r1**. This body defines only the SL-02.M1 consumed scope; future consumer scopes remain pending. Readiness and implementation are recorded separately in [Progress](../../progress/traceability.md#63-sl-02m1-reviewed-scope-and-interface-evidence).

[Index](../index.md) · [Common](../common.md#com-038) · [Decisions](../../design/contract/sl-02-m1-grill.md)

## 1. SL-02.M1 source and currentness scope

<a id="mat-001"></a>
**MAT-001.** Successful Profile/Knowledge/Resume Save MUST establish only its owned formal authority and receipt, not durable rendered preview/PDF/export readiness. Page-local Draft preview MUST remain non-authoritative and MUST NOT be treated as a saved artifact. M1 MUST NOT invent MaterialBundle/Artifact/RenderManifest schemas, renderer configuration, job/intent rows or recovery states without the actual M2 consumer. (UI1; Q95.)

<a id="mat-002"></a>
**MAT-002.** A saved Resume source MUST be read as its exact ResumeVersion plus retained exact Profile/Evidence refs using PRO/EVD/RES readers. A later source root current-pointer movement or ordinary Evidence retirement MUST NOT rewrite that Resume, invalidate its document identity or alone require rerender. Historical source binding MUST NOT be relabeled as latest Knowledge; failures of retained references MUST remain explicit under STO-028. Resume document identity is separate from default selection, management name and current Knowledge. (BC3; Q59/Q60/Q95/Q100.)

<a id="mat-003"></a>
**MAT-003.** M2 MUST define actual demand/configuration/output/readiness and durable work/intent with their consumers. Where existing demand requires intent on a Save, the implementation MUST extend that owning authority transaction atomically; a lossy post-commit notification cannot substitute. Rendering remains post-commit and cannot reverse a successful Save. M1 source boundary alone MUST NOT claim M2 rendered delivery, Preparation approval, execution or application success. Renderer-specific fonts/fallback, layout/export fidelity and actual material currentness beyond this boundary remain M2 scope. (Q95.)
