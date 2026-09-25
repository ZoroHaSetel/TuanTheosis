# Master's thesis report

This workspace contains the revised LaTeX source for the Master's thesis, assembled from `main.tex`, `chapters/`, `appendices/`, `figures/`, and `ref/references.tex`. The original Markdown source in `source/thesisproposalTuan.md` is preserved unchanged; the revised thesis should be edited directly in the LaTeX files.

## Build the PDF

Use a local LaTeX installation with `latexmk`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document is configured for pdfLaTeX, including Vietnamese text through T5 font encoding. The current assembly includes six main chapters, seven appendices, native TikZ figures, mathematical notation, and a direct `thebibliography` file. No BibTeX database is required.

## Revision Summary

The current revision restructures the thesis around the scientific argument rather than the internal experiment trail. The main chapters now emphasize problem, method, experimental design, results, interpretation, and limitations. Low-level reproduction details, exact paths, hashes, and audit-oriented material are retained in appendices where appropriate.

Major changes include:

- Shortened and rewritten abstract and introduction.
- Consolidated research contributions into three stronger contributions.
- Rewritten Chapter 4 to describe methodology rather than implementation internals.
- Rebuilt Chapter 5 around RQ1, RQ2, BCA coverage, failure analysis, and a single coherent RQ3 adaptation narrative.
- Rewritten Chapter 6 as synthesis, contributions, limitations, future work, and closing remarks.
- Standardized bibliography entries and removed source-quality commentary from the bibliography.
- Enabled appendices in `main.tex` so the audit trail remains available outside the main thesis narrative.

## Editing Notes

Edit `main.tex` for document assembly and title-page formatting. Edit files in `chapters/`, `appendices/`, and `ref/references.tex` for thesis content.

Avoid regenerating the thesis from `tools/build_thesis.py` unless you intentionally want to discard the revised LaTeX prose. The converter reconstructs content from the preserved Markdown source and may overwrite chapter, appendix, and reference files.

## Verification Performed

In this environment, `latexmk`, `pdflatex`, `xelatex`, and `lualatex` were not available, so a PDF compile could not be completed here. Source-level checks were performed for:

- missing LaTeX labels;
- duplicate labels;
- missing citation keys;
- remaining editorial placeholders;
- stale Chapter 5 references;
- internal project paths in main chapters.

Run the `latexmk` command above on a machine with a LaTeX distribution installed to produce the final PDF and inspect page layout.
