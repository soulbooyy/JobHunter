# Fixed rendering assets

These are implementation artifacts under MAT-009–013/030, not another specification. The [approved role amendment](../../../docs/design/contract/sl-02-m2-grill.md#cg04-font-20260923) owns permitted mappings.

- `catalog.json`: immutable application-assigned PDF/PNG configurations. Content changes require new IDs and appropriate descriptor versions.
- `font-sources.json`: fixed official download URLs and exact hashes, including the Sarasa archive and original licenses.
- `font-manifest.json`: original face/hash, final role file/hash and deterministic outline-transform provenance. Source Han Sans SC 2.005R and Source Han Serif SC/CN 2.003R use official Regular/Bold plus derived italic faces; Sarasa Gothic SC 1.0.40 uses four official faces; LXGW WenKai 1.522 maps Regular/Medium to regular/bold and derives the corresponding italic roles.
- `licenses/`: upstream SIL Open Font License texts. Modified fonts retain copyright/license information and use JobHunterDerived family/style names; native faces retain their original names. Redistribution must include the applicable licenses. The fonts may not be sold by themselves.
- `pipeline.json`: exact Python/native dependency/platform checkpoint and actual conformance gate. It is capability data separate from a retained configuration record.
- `fontconfig.xml`: no system font search directories. The renderer registers only four explicit local faces for the selected logical family and refuses unsupported visible glyphs.
- `fonts/`: ignored reproducible binary installation, about 330 MB; never downloaded during rendering.

Install from the repository root with `uv run --locked python scripts/install_render_fonts.py`. The script uses fixed official sources, validates every download, extracts only the four named Sarasa files and invokes `build_render_fonts.py`. To verify/rebuild already downloaded inputs, run `uv run --locked python scripts/build_render_fonts.py /absolute/source-directory`. The latter stages a new build, compares every final hash to the maintained manifest and installs only on equality; it does not generate new catalog values.

Synthetic italic is an offline fontTools 4.65.0 outline transform `(1, 0, 0.2125565616700221, 1, 0, 0)`, fixed at a 12° slant, with fixed derived naming and modified timestamp. It does not depend on whether Pango/WeasyPrint supports CSS synthesis and does not synthesize bold. Conformance checks inspect embedded font programs and their italic metadata; WeasyPrint 70 currently writes a zero PDF descriptor ItalicAngle even when the embedded outlines/font metadata are italic, so that descriptor alone is not used as style evidence.

Primary implementation references: [WeasyPrint installation](https://doc.courtbouillon.org/weasyprint/latest/first_steps.html), [fontTools affine pen](https://fonttools.readthedocs.io/en/latest/pens/transformPen.html), [PDFium process/thread constraints](https://pypdfium2.readthedocs.io/en/stable/python_api.html#incompatibility-with-threading). Actual pinned sources and executable tests, rather than these moving documentation pages, establish this implementation's behavior. Evidence is maintained in [traceability](../../../docs/progress/traceability.md#materials-backend-evidence).
