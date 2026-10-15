# Chapter 1: Introduction

## Overall idea

This chapter frames Vietnamese legal retrieval as an evidence-ranking problem: relevant legal provisions must be retrievable and ranked highly before a downstream RAG system can use them. It establishes controlled comparisons between BM25, BGE-M3, multilingual-E5-base, their hybrid combinations, and legal-domain BGE-M3 adaptation. Its central distinction is between beating a lexical baseline, adding value to an existing hybrid, and transferring dense-model improvements into a complete hybrid system. Collection coverage, corpus representation, query dependence, and protected evaluation boundaries determine what the results can support.

## Page-by-page summaries

### Printed page 1 — PDF page 10

**Covered section: 1.1 Research Context.** RAG depends on external evidence, so fluent answers can still rest on incomplete or incorrect provisions. The thesis studies retrieval rather than answer generation. Vietnamese legal questions create a gap between everyday language and formal statutes; similar provisions can differ in decisive legal details, while absent or incorrectly mapped targets cannot be recovered by any ranking model. BM25 supplies a strong lexical reference, BGE-M3 and E5 supply semantic retrieval, and two-way and three-way hybrids combine their scores. The motivating questions concern supported empirical gains, especially whether E5 adds value beyond BM25+BGE-M3 and whether fine-tuning gains survive fusion.

### Printed page 2 — PDF page 11

**Covered sections: 1.2 Research Gap and Approach; 1.3 Research Objectives.** Existing work motivates the methods but does not establish their behavior on these Vietnamese collections. The study therefore compares methods under consistent boundaries. ALQAC and Zalo each use clean and parsed corpus representations; BCA is constructed from published Bộ Công an questions and answers and receives coverage and component-aware analysis; adaptation is tested both independently and inside a hybrid. The investigation progresses from baseline comparison to E5's incremental contribution, failure diagnosis, and adaptation. Four objectives cover fair method comparison, E5's added value, transfer from development-selected adaptation to unseen data and hybrids, and BCA construction/evaluation. NDCG@10 is primary, with Hit@10, MRR@10, and MAP@10 explaining other ranking behaviors. Negative and condition-dependent outcomes are valid findings.

### Printed page 3 — PDF page 12

**Covered item: Figure 1.1, Research investigation overview.** The diagram connects eight stages: compare the two-way and three-way pretrained hybrids; normalize scores per query and fit weights before unseen-data evaluation; report collection-specific evidence; analyze BCA's giant-component holdout and grouped smaller components; distinguish target absence, incomplete coverage, missed retrieval, and low rank; train and select BGE adaptation using permitted training/development data and replace BGE under fixed fusion weights on the designated Zalo fold; report three seeds separately; and interpret corrected outputs while disclosing prior test access and unfinished extensions. The caption clarifies that component analysis applies only to BCA and development selection does not replace the protected training/evaluation split.

### Printed page 4 — PDF page 13

**Covered sections: 1.4 Research Questions; 1.5 Research Contributions (beginning).** RQ1 asks what improvement hybrid retrieval supports over BM25 in the evaluated conditions. RQ2 uses BM25+BGE-M3 as the comparator to isolate E5's incremental value by collection and representation. RQ3 separates development selection, corrected unseen hybrid evaluation in Study A, and dense-only versus hybrid-transfer evidence in Study B. The contributions introduced here are controlled method comparisons, condition-dependent E5 gains with the clearest gain on parsed Zalo, and adaptation evidence showing that Study A's development gains do not persist and Study B's dense gains largely disappear after fusion. The page begins the third contribution, the BCA dataset and evaluation design, which continues on the next page.

### Printed page 5 — PDF page 14

**Covered sections: 1.5 Research Contributions (continued); 1.6 Scope of the Thesis; 1.7 Thesis Organization.** BCA contributes construction from public-service questions and answer citations, coverage analysis, component-aware evaluation, and reproducible comparison boundaries while acknowledging missing evidence. Retrieval scores measure agreement with recorded targets, not legal correctness of generated answers. The scope excludes generation quality, advice quality, satisfaction, document currency, latency, and professional sufficiency; it also excludes unsupported generalization across languages, jurisdictions, future corpora, or RAG systems. BCA citations provide targets rather than exhaustive expert relevance judgments, and absent-target queries remain informative. The chapter maps Chapters 2–6 and the appendices to literature, theory, methods, experiments, synthesis, and reproduction details.

## Section-by-section summaries

### 1.1 Research Context

The retrieval component of legal RAG must rank relevant articles or indexed documents for Vietnamese questions. Everyday/statutory wording differences, near-duplicate legal topics, and corpus construction errors complicate this task. BM25 handles lexical overlap, while BGE-M3 and E5 address semantic correspondence. The chapter motivates evaluating the two-way BM25+BGE-M3 hybrid and the three-way hybrid with E5 separately, and distinguishing improvements to a dense encoder from improvements to the complete fused system.

### 1.2 Research Gap and Approach

The gap is empirical and methodological within the studied collections: prior work does not settle the behavior of these models, fusion methods, and adaptation procedures under the same Vietnamese evaluation conditions. Three evaluation families address this gap: paired clean/parsed ALQAC and Zalo conditions, coverage- and component-aware BCA evaluation, and dense/hybrid adaptation evaluation with development selection separated from unseen-data evaluation. The main narrative prioritizes method, results, and interpretation; appendices retain reproduction details.

**Figure 1.1 — Research investigation overview:** The eight-stage flow runs from pretrained hybrid comparison through comparable fusion, collection evidence, BCA dependence analysis, failure diagnosis, supervised BGE replacement, seed-specific conclusions, and interpretation boundaries. It specifies per-query normalization, fitting-query weight selection, giant-component holdout and grouped smaller BCA components, fixed fusion weights during adaptation replacement, permitted folds, three separate seeds, corrected outputs, prior-test-access disclosure, and unfinished-extension disclosure. Its caption limits BCA component analysis to BCA and preserves the protected split despite development-based recipe selection. Although included here in the source, the figure occupies printed page 3 / PDF page 12.

### 1.3 Research Objectives

The overall objective is to determine the effectiveness and limits of lexical–semantic hybrid retrieval and legal-domain BGE-M3 adaptation. The four operational aims are:

1. Compare lexical, dense, and fused retrieval on identical query populations and judgments.
2. Measure E5's incremental value beyond BM25+BGE-M3.
3. Test whether development-selected fine-tuning improves unseen dense and complete-hybrid retrieval.
4. Construct and evaluate BCA with attention to coverage, citation mapping, and query dependence.

NDCG@10 is the primary endpoint. Hit@10, MRR@10, and MAP@10 contextualize first-hit and multiple-target behavior. Objectives permit negative, condition-specific, and non-transfer outcomes.

### 1.4 Research Questions

**RQ1. What improvement over lexical retrieval is supported by lexical–semantic hybrid retrieval on the evaluated Vietnamese legal collections?** Compare BM25, dense retrievers, and hybrids against the fixed lexical reference under each condition; do not presume every hybrid beats every standalone retriever.

**RQ2. Does adding pretrained multilingual-E5-base improve BM25+BGE-M3 across legal collections and corpus conditions?** Compare the three-way hybrid with the two-way hybrid to isolate the second dense retriever's contribution, and report by collection and representation rather than treating a local gain as a universal advantage.

**RQ3. Do development improvements from legal-domain BGE-M3 fine-tuning transfer to retrieval on unseen data and to the complete hybrid system?** Distinguish development selection and corrected unseen hybrid evaluation in **Study A: Hybrid-Oriented Adaptation**, then standalone dense and hybrid-transfer evidence in **Study B: Dense-Oriented Adaptation**. Determine whether improvement in isolation remains useful after integration with BM25 and E5.

### 1.5 Research Contributions

The first contribution is a controlled comparison of BM25, BGE-M3, E5, and both hybrid combinations across ALQAC, Zalo, and BCA. The reported overall finding is hybrid improvement over the fixed BM25 reference, with E5's extra value depending on conditions and being clearest on parsed Zalo.

The second contribution evaluates BGE-M3 adaptation at dense and complete-hybrid levels. Study A's development gains fail to persist in corrected unseen hybrid evaluation; Study B's dense improvement largely vanishes after fusion. These results demonstrate that a better dense encoder does not necessarily improve its surrounding hybrid.

The third contribution is BCA dataset construction and evaluation from published questions and cited answers, including coverage, component structure, and limitations from absent or partial evidence. Its novelty is in the collection, evaluation design, and reproducible comparison boundaries rather than routine provenance records.

### 1.6 Scope of the Thesis

The thesis measures ranking effectiveness for Vietnamese legal question answering against available judgments. It does not assess generated answers, legal advice quality, satisfaction, document currency, deployment latency, or professional legal sufficiency. Multilingual names describe pretrained models; the evaluation does not cover multiple languages or jurisdictions. Generalization to other legal systems, future corpora, and downstream RAG systems needs additional evidence. BCA answer citations are operational targets rather than exhaustive expert judgments, and missing-target queries expose corpus limitations.

### 1.7 Thesis Organization

Chapter 2 reviews legal retrieval, lexical and dense methods, fusion, adaptation, and evaluation. Chapter 3 supplies theory and metrics. Chapter 4 specifies retrieval, corpus construction, fusion selection, BCA construction, and adaptation methods. Chapter 5 answers the research questions and examines BCA coverage/components, failure modes, development-to-unseen regressions, and dense-to-hybrid transfer. Chapter 6 synthesizes findings, contributions, limitations, and future work. Appendices retain search spaces, full metrics, cases, configurations, and reproduction information.

## Coverage record

Reviewed the complete `chapters/chapter_1.tex` source, its included `figures/research_overview.tex`, and PDF pages 10–14 (printed pages 1–5). Coverage includes all **7 sections**, **3 research questions**, **4 operational objectives**, **3 contributions**, and **1 figure with all 8 stages**. The source contains **0 subsections, 0 tables, and 0 displayed equations**. Section numbering and names follow the source; page boundaries follow the supplied PDF text.
