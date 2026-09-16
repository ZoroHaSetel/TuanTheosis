# Master's thesis report

The report uses `source/thesisproposalTuan.md`, the manuscript actually present in this workspace. There is no `source/thesisproposal.md`. The source Markdown is preserved unchanged.

## Build the PDF

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document supports pdfLaTeX, including Vietnamese text through T5 font encoding. The source files contain six chapters, seven appendices, 42 tables (including unnumbered abbreviation and case-detail tables), six native TikZ diagrams, mathematical notation, and 21 bibliographic entries. The seven appendix inputs are currently commented out in `main.tex` and remain excluded from the PDF. The bibliography is included directly from `ref/references.tex`; no BibTeX database or Mermaid renderer is required.

## Edit or regenerate

Edit `main.tex` for the title page, formatting, and report assembly. Edit the files in `chapters/`, `appendices/`, or `ref/references.tex` for the report text.

The original converter can reconstruct content from Markdown, but it does not reproduce the later citation review:

```sh
python tools/build_thesis.py
```

The converter uses the already-available `markdown_it` package. A guard now stops regeneration while `tools/citation-audit.json` exists, because regeneration would discard the reviewed citations. Edit the LaTeX sources directly; remove the guard record only after preserving this revision and intentionally choosing to discard the citation edits. Regeneration **overwrites** the generated chapter, appendix, and reference files, but not `main.tex`. `tools/conversion-report.json` records the source SHA-256 and checks preservation of table/cell and fenced-block counts. The compiler's contents, figure list, and table list replace the manuscript's manually maintained lists. The converter also restores visibly corrupted mathematical markup in the source’s multi-positive loss equation and variable definitions, without changing the stated objective, and normalizes Appendix E heading levels. Native diagrams preserve the source nodes and directed edges, with print-oriented layouts.

## Evidence and submission status

The original report is a conversion of the supplied manuscript. The subsequent citation review checks literature attribution against primary sources; project evidence remains documented in the text without bibliographic self-citations; it is not a new experiment or independent verification of the unavailable project artifacts. Numerical results are retained from the supplied manuscript. Links to experiment artifacts and historical scripts refer to the original research repository, which is not included here. In particular, the historical assembly instructions in Appendix F describe that repository; use the commands above for this workspace.

The source-provided Declaration of Authorship and completed acknowledgements are included. No signature is added. Retained scientific evidence requirements and prior test-exposure qualifications remain visible; final university formatting and signature requirements still need confirmation.

## Source synchronization: 16 September 2026

This update incorporates the source's author name, Declaration of Authorship, acknowledgements, expanded three-column glossary, revised RAG motivation and retrieval-only scope, and research workflow. Source-deleted Appendix G.2–G.4 and the former evidence-reading front-matter section are removed from the compiled report. Duplicate empty headings and an editorial instruction are not reproduced. The workflow is rendered as grouped native TikZ stages; development data select the recipe, consistently with the detailed training-fold protocol.

Experimental tables, references, and the reported 12 September 2026 evidence-audit date are unchanged. The Markdown source is not edited by the synchronization. `tools/source-sync-report.json` records validation and the actual PDF page count.

**Version boundary:** this workspace contains the older six-chapter, seven-appendix report, not the previous eight-chapter 59-page revision. The original synchronized PDF had 162 pages and did **not** satisfy the earlier 80-page target. This source update preserves the current document rather than silently reconstructing or replacing it with a different version.

## Linked citation review: 16 September 2026

All six chapters, front matter, figures, tables, and appendix sources were reviewed for citation coverage. Author–year markers are replaced with numbered `\cite{key}` commands, linked by `hyperref` to matching `\bibitem{key}` entries in `ref/references.tex`. Existing external links and legacy reference anchors remain available. The 21 entries comprise the 18 inherited literature/documentation sources and three added evaluation/statistical sources. The five self-authored project entries and all citations to them have been removed, including from mixed citation groups, captions, and disabled appendix sources.

Published sources support methodological claims. The thesis reports its own configurations, results, and failure analyses directly, without citing the author or project as a bibliographic source. Existing artifact paths remain provenance notes; their underlying experimental files are unavailable here. Illustrations, deductions, hypotheses, personal statements, and proposed future work are not disguised as externally established findings. Original experimental table cells, displayed equations, and the Markdown source are preserved.

`tools/citation-audit.json` records source integrity, citation resolution, and PDF-link checks. The current PDF page count is recorded in that audit; appendix inputs remain disabled. The earlier 80-page target is not achieved by this citation-only revision. No BibTeX run or `.bib` database is required.