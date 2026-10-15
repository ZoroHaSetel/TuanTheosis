# Chapter 6 — Conclusion and Future Work

Source: `chapters/chapter_6.tex`. Page references follow `main.pdf`: printed pages 44–47, corresponding to PDF pages 53–56. Source headings and text take precedence over PDF extraction artifacts.

## Overall idea

Vietnamese legal retrieval benefits from combining lexical and semantic evidence in the evaluated collections, but an extra retriever or a better adapted dense encoder does not necessarily improve the complete hybrid system. Conclusions must distinguish gains over BM25, gains beyond an existing hybrid, and transfer of dense-only adaptation gains into hybrid retrieval. The chapter synthesizes the findings, identifies three contributions, bounds the claims by corpus coverage and evaluation validity, and proposes stronger prospective, corpus-quality, and complete-RAG evaluations.

## Page-by-page summaries

### Printed page 44 · PDF page 53

- The introduction separates the three levels of evidence: improvement over BM25, incremental hybrid improvement, and transfer from dense adaptation to a complete system.
- **6.1 Summary of Findings / 6.1.1 Hybrid Retrieval over the Lexical Baseline:** BM25+BGE-M3 and BM25+BGE-M3+E5 improve NDCG@10 over the fixed BM25 reference across the reported ALQAC and Zalo conditions. BCA's combined descriptive view points in the same direction. This supports hybridization for these collections and representations; it does not establish transfer of a particular weight setting, corpus policy, or architecture to other legal corpora.
- **6.1.2 Incremental Contribution of E5:** Adding E5 yields its clearest benefit on parsed Zalo, about +0.0130 NDCG@10. ALQAC has small negative differences, clean Zalo a small positive difference, and BCA no reliable small-component advantage. Three-way retrieval is therefore not universally better than a strong two-way reference.
- **6.1.3 Effect of Legal-Domain Adaptation, opening:** Study A gains substantially during development selection but regresses in its corrected hybrid evaluation on data unseen during training and selection. The numerical results continue on the next page.

### Printed page 45 · PDF page 54

- **6.1.3 Effect of Legal-Domain Adaptation, continuation:** Study A's mean NDCG@10 falls by 0.0520 for the two-way hybrid and 0.0249 for the three-way hybrid. Study B improves dense BGE-M3 by 0.0189, but that gain largely disappears in locked-weight hybrids. Encoder improvement is not sufficient evidence of a meaningful complete-system improvement.
- **6.2 Research Contributions:** The three contributions are a controlled comparison of lexical, dense, two-way, and three-way retrieval across Vietnamese legal collections and corpus representations; assessment of BGE-M3 adaptation at both dense and hybrid levels, preserving negative and non-transfer results; and construction/evaluation of BCA from public questions and published answer citations, including target coverage and component-aware analysis.
- **6.3 Discussion and Limitations, opening:** Aggregate scores can hide weak marginal components, newly introduced query failures, and dependence between legal components despite a large query count. Legal retrieval needs specific provisions, not merely topical similarity. E5 adds diversity and fusion choices, but its benefit depends on the collection and representation; the comparison continues on the next page.

### Printed page 46 · PDF page 55

- **6.3 Discussion and Limitations, continuation:** Parsed Zalo benefits most clearly from E5, while ALQAC does not, motivating local validation. Development gains can mislead: Study A regresses on its corrected evaluation, whereas Study B demonstrates that dense fine-tuning can help the encoder. Fusion weights, lexical evidence, and score calibration may absorb, dilute, or counteract those improvements, but the experiments do not isolate the dominant mechanism.
- Public supervised Vietnamese legal retrieval data remain limited. More diverse, carefully validated query–article pairs could broaden topic and relevance coverage, but their benefit is an untested future-work hypothesis.
- BCA contains absent targets and partially covered answerable queries. End-to-end scores consequently reflect corpus construction and target mapping as well as ranking; a model cannot retrieve missing evidence.
- Validity is limited to the evaluated Vietnamese collections and recorded judgments. The study does not establish multilingual or cross-jurisdiction transfer, legal-answer correctness, current legal validity, user satisfaction, latency, throughput, or deployment cost. Study A's corrected evaluation is post-hoc because a flawed preliminary analysis had already examined that fold. Study B uses a fixed-corpus benchmark with prior test observation and is not a pristine prospective confirmation.
- Non-significant intervals do not establish equivalence; statistically detectable differences do not necessarily matter practically. Mean change, practical thresholds, and uncertainty must remain distinct.
- **6.4 Future Work, opening:** Run a prospectively controlled evaluation on untouched queries, fixing corpus construction, model selection, fusion configuration, and statistical procedures before examining final test results.

### Printed page 47 · PDF page 56

- **6.4 Future Work, continuation:** Improve corpus quality, especially BCA, through version-aware legal-document mapping. Sample and annotate query failures with a defined rubric to distinguish missing evidence, annotation limitations, lexical mismatch, semantic confusion, and fusion-related ranking errors.
- Extend evaluation to complete RAG systems, measuring answer correctness, citation support, legal sufficiency, latency, throughput, and computational cost. Retrieval metrics cannot substitute for direct assessment of generated legal answers and deployed performance.
- **6.5 Closing Remarks:** Hybridization helps in the evaluated setting, while additional components and improved dense scores offer no automatic guarantee of a better complete system. Tie claims to the exact corpus, target coverage, selection boundary, and evaluated system level. Disciplined negative findings are valuable when they prevent unsupported deployment claims.

## Section-by-section summaries

### 6.1 Summary of Findings

The findings distinguish hybrid gains over a lexical baseline from the marginal value of E5 and from the ability of adaptation gains to transfer into the deployed retrieval pipeline.

#### 6.1.1 Hybrid Retrieval over the Lexical Baseline

Both two-way and three-way lexical–semantic hybrids outperform BM25 in the reported ALQAC and Zalo conditions, with the same direction in BCA's combined descriptive view. These are collection-specific empirical results, not guarantees that weights, corpus construction, or architecture transfer unchanged elsewhere.

#### 6.1.2 Incremental Contribution of E5

E5's marginal value depends on corpus conditions: approximately +0.0130 NDCG@10 on parsed Zalo, small negatives on ALQAC, a small positive on clean Zalo, and no reliable small-component advantage on BCA. Any extra retriever needs validation against a strong two-way baseline in the target setting.

#### 6.1.3 Effect of Legal-Domain Adaptation

Study A's development-selection gains fail to transfer: corrected evaluation yields −0.0520 NDCG@10 for the two-way hybrid and −0.0249 for the three-way hybrid. Study B yields +0.0189 for dense BGE-M3, but little meaningful improvement after integration into locked-weight hybrids. Adaptation can improve an encoder without materially improving the full lexical–semantic system.

### 6.2 Research Contributions

1. **Controlled hybrid evaluation:** Compare BM25, BGE-M3, E5, and two-way/three-way fusion across Vietnamese legal collections and representations, separating lexical-baseline gains from gains beyond a strong hybrid.
2. **Adaptation at two system levels:** Evaluate legal-domain BGE-M3 adaptation as both a dense retriever and a hybrid component, retaining negative and non-transfer results because deployment concerns the pipeline.
3. **BCA dataset and evaluation:** Construct a collection from public questions and published answer citations, analyze target coverage, and evaluate with awareness of legal-component dependence. Corpus availability and query dependence affect metric interpretation.

### 6.3 Discussion and Limitations

Aggregate improvements can coexist with negligible component contributions, newly introduced failures, and fewer independent legal components than the query count suggests. Legal retrieval must recover specific provisions. E5's contrasting parsed-Zalo and ALQAC results favor local validation over model-count assumptions.

Development selection does not guarantee unseen-data gains. Hybrid interactions among weights, lexical evidence, and calibration can dilute or counteract dense improvement; the experiments do not identify which mechanism dominates. More diverse, validated query–article supervision may help under the limited public-data setting, but this intervention was not tested.

BCA's missing targets and partial coverage limit achievable retrieval independently of model ranking. Scores describe the complete pipeline, including corpus construction and target mapping. Generalization and deployment claims remain unestablished for multilingual retrieval, other jurisdictions, downstream answer correctness, current legal validity, user satisfaction, latency, throughput, and cost.

Study A's corrected evaluation on data unseen during training and selection remains **post-hoc** after a flawed preliminary analysis of the same fold. Study B's fixed-corpus benchmark includes **prior test observation**, so it is not pristine prospective confirmation. Non-significance does not prove equivalence, and statistical detectability does not prove practical importance; mean effects, practical thresholds, and uncertainty must be distinguished.

### 6.4 Future Work

- Conduct a new prospective evaluation on an untouched query set. Fix corpus construction, model selection, fusion configuration, and statistical procedures before inspecting final test outcomes.
- Improve corpus quality, especially BCA coverage, with version-aware legal-document mapping.
- Systematically sample and annotate query-level failures using a defined rubric that separates missing evidence, annotation limitations, lexical mismatch, semantic confusion, and fusion-related ranking errors.
- Evaluate the complete RAG system for answer correctness, citation support, legal sufficiency, latency, throughput, and computational cost, rather than relying on retrieval metrics alone.
- The additional suggestion in Section 6.3 is to investigate more diverse, carefully validated query–article training pairs spanning broader legal topics and relevance relations. Its effectiveness remains a hypothesis.

### 6.5 Closing Remarks

Lexical–semantic hybridization is useful for the evaluated Vietnamese legal retrieval conditions, but more components and higher dense-only scores do not guarantee full-system improvement. Claims should specify corpus, target coverage, selection boundary, and system level. Negative results can prevent unsupported deployment conclusions and are therefore substantive findings.

## Coverage check

Covered all 4 chapter pages, all 5 sections, and all 3 subsections from the source. Included the chapter introduction, all three contributions, both adaptation caveats, statistical versus practical interpretation, and every future-work suggestion (including the untested supervision-data hypothesis in Section 6.3).
