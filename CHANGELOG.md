# Changelog

Full history, including releases before this file existed: https://velofy.co/terbium/changelog/

## 0.10.1 (2026-10-26)

The first PyPI release since 0.9.7. 0.10.0 was published on GitHub only, so `pip install terbium-parse` now brings everything listed under 0.10.0 as well as the fixes below.

### Fixed

- No more `FutureWarning: The fitz API is deprecated` on every import and every command run with PyMuPDF 2.0. terbium imports PyMuPDF as `pymupdf`, and falls back to `fitz` only on PyMuPDF 1.24.0 to 1.24.2, which predate that name.
- Resume lines that mention a section word are kept. A line such as "Led a team with deep Python experience" was read as a heading: it was dropped from the content and started a new section. A heading is now a line that is exactly a section word, or a line of at most four words that names a section as a whole word or phrase, such as "Work Experience". Bulleted lines are always content.
- The image manifest's `dominant_color` no longer uses `Image.getdata`, which Pillow 13 deprecates and Pillow 14 removes. On Pillow 14 the colour would have come back empty with no error.

### Documentation

- The README leads with the terbium app tile, names NodeMaven as primary sponsor with the October tracking links, and no longer says that PyPI serves 0.9.7.
- The `parse` and `build_catalog` docstrings and the developer notes in `docs/` (DESIGN, ROADMAP, TAXONOMY) now match the code.

### Known issues

- The 0.10.0 known issues below still apply.
- `build_catalog(..., ocr=True)` without Tesseract prints the advice for an OCR pass that already ran, so it points at the vision lane instead of telling you to install Tesseract. Leave `ocr="auto"`.
- `build_catalog(..., ai=True)` skips the AI fill for photo rows; pass `terbium.AI()`.
- A phone number written `(555) 123-4567` comes out as `555) 123-4567`.

## 0.10.0 (2026-09-30)

First tagged GitHub release, published on GitHub only; PyPI went from 0.9.7 to 0.10.1.

### Added

- Document classification (`terbium.classify`): catalog, lookbook, transaction, resume, table, deck or unknown, which picks the schema. `--type` and `doc_type=` override it.
- Transaction schema for invoices, bills, receipts, purchase orders and quotes, with summary and line item records.
- Resume schema with a candidate header and sectioned records.
- CSV, self-contained HTML and terminal table output for every lane. New CLI flags `--type`, `--html` and `--open`; the CLI routes invoices and resumes to the records view.
- Image adapter for PNG, JPG, JPEG, WEBP and TIFF through local Tesseract OCR.
- Picture-heavy catalogues: per-page lookbook detection, proximity-scored captions, dense grids and one-photo pages. The catalog table gains a Dimensions column.
- AI providers GPT (OpenAI), Kimi (Moonshot) and Grok (xAI) through the OpenAI-compatible client, with extras `openai`, `kimi` and `grok`. Claude stays the default when several keys are set.
- Exports `terbium.records_to_csv`, `terbium.render_html`, `terbium.render_terminal_table`.

### Fixed

- The invoice and receipt AI step now runs. It looked for `header` records while the parser emits `summary` records, so it never filled anything. It now fills missing summary fields, adds a summary when there is none, and adds AI line items only when the parser found none.
- `ParsedDocument.used_ai` is True only when a model call returned a response. Before, any transaction parse with a key set reported AI use.
- Terminal tables truncate header cells to the column width, truncated cells no longer run two characters past their column, and column widths are budgeted for the box borders, so columns line up.
- The catalog message no longer tells you to run with `ocr=True` when Tesseract is not installed; it says to install Tesseract or use the AI vision lane.
- OpenAI o-series models (the `opus` tier maps to `o3-mini`) are called with `max_completion_tokens` instead of `max_tokens`, which the openai SDK documents as incompatible with o-series models. The `openai`, `kimi`, `grok` and `ai` extras now require `openai>=1.45`, the first SDK version with that parameter.

### Known issues

- The `opus` tier on OpenAI (`o3-mini`) may still reject image input for the vision lane; not verified against the API.
- Model IDs for each provider are taken from source and not verified against the provider APIs.
- The Gemini lane uses `google-generativeai`, which Google has superseded with `google-genai`.
