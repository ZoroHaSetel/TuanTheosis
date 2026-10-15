# Front Matter — Summary

Source: `chapters/frontmatter.tex`. Page references use printed thesis page numbers, followed by the PDF page number.

## Overall idea

The front matter introduces a thesis on retrieving the Vietnamese legal articles needed to support question answering. It previews the comparison of lexical, dense, and hybrid retrieval, explains the limits of corpus coverage and legal-domain adaptation, and defines the terminology used throughout the thesis. Its central message is that hybrid retrieval improves the fixed BM25 reference, but adding another encoder or improving an encoder through fine-tuning does not automatically improve the complete retrieval system.

## Page-by-page summaries

### Page iv (PDF page 5) — Abstract

- **Problem and research questions:** Reliable legal question answering requires retrieving supporting provisions. The thesis evaluates article-level retrieval using fixed corpora and recorded relevance judgments, asking whether hybrids improve BM25, whether multilingual-E5-base adds value beyond BM25+BGE-M3, and whether adapting BGE-M3 to the legal domain improves complete hybrids beyond development selection.
- **Data and methods:** ALQAC and Zalo are studied in clean and parsed representations. A new Bộ Công an (BCA) collection comes from public-service questions and citations in published answers. Comparisons include BM25, pretrained BGE-M3, pretrained E5, two-way BM25+BGE-M3 fusion, and three-way BM25+BGE-M3+E5 fusion. NDCG@10 is the primary metric. BCA receives coverage analysis and a component-aware evaluation because multiple questions share legal targets.
- **Hybrid findings:** Hybrid retrieval improves the fixed BM25 reference in the reported conditions. E5's additional value depends on the condition: parsed Zalo gives the clearest positive gain, ALQAC has small negative differences, and BCA does not demonstrate a reliable advantage on small components.
- **Coverage limitation:** Some BCA legal targets are missing or only partly represented in the corpus. Better ranking alone cannot fix those retrieval failures.
- **Adaptation findings and caveat:** Study A: Hybrid-Oriented Adaptation achieves substantial development-selection gains but loses mean NDCG@10 by **0.0520** in the two-way hybrid and **0.0249** in the three-way hybrid on data unseen during training and selection. The corrected evaluation is nevertheless **post-hoc**, because preliminary analysis had already exposed the evaluation fold. Study B: Dense-Oriented Adaptation improves the dense encoder's mean NDCG@10 by **0.0189**, but the gain largely disappears in the full hybrids. Dense-model improvement therefore does not guarantee system improvement.
- **Keywords:** Vietnamese legal retrieval; BM25; BGE-M3; multilingual-E5; hybrid retrieval; contrastive fine-tuning; NDCG; legal-domain adaptation.

### Page v (PDF page 6) — List of Abbreviations

This page establishes the vocabulary for datasets, retrieval models, model status, evaluation procedures, and ranking metrics. It states that terminology follows the retrieval literature and the task definitions in Chapters 3–4. It contains eleven entries: **ALQAC, BCA / MPS, BM25, BGE-M3, CV, E5, FT / PT, IR, MAP, MRR, and NDCG**. Together, these terms distinguish the data sources and lexical/dense components and explain how their ranking performance is evaluated. Each entry is explained in the section summary below.

### Page vi (PDF page 7) — List of Abbreviations (continued)

The table concludes with four entries: **OOF, RAG, RQ, and SD**. They clarify how results can be produced outside fitting folds, how retrieval relates to generation, how empirical questions are named, and how variation around a mean is described. Each entry is explained below.

## Section-by-section summaries

### Abstract

The abstract presents the thesis's problem, empirical scope, methods, principal results, and limitations. It frames legal retrieval as finding supporting articles under controlled corpus and relevance conditions. It contrasts lexical BM25 with dense models and two- and three-component hybrids, then reports that hybrid gains are more consistent than E5's incremental gains. It also identifies corpus coverage as a separate barrier to retrieval success. The two adaptation studies demonstrate the difference between development-selection gains, dense-encoder gains, and gains in the complete hybrid system, with the explicit post-hoc qualification for Study A. The quantitative changes and keywords are preserved in the page iv summary.

### List of Abbreviations

The section standardizes terminology using retrieval literature and the task definitions introduced in Chapters 3–4. All fifteen abbreviation rows are covered below.

| Abbreviation | Meaning | Idea and use in the thesis |
|---|---|---|
| ALQAC | Automated Legal Question Answering Competition | A benchmark and competition for evaluating legal question answering and information retrieval systems. |
| BCA / MPS | Bộ Công an / Ministry of Public Security collection | A legal question–document collection derived from public questions and published answers associated with Vietnam's Ministry of Public Security. |
| BM25 | Best Matching 25 lexical ranking function | A term-based retrieval method that ranks documents using query-term matches, term frequency, and document length. |
| BGE-M3 | BGE-M3 multilingual embedding model | The multilingual embedding model used as a dense retrieval component in this thesis. |
| CV | Cross-validation | A procedure that partitions data into subsets for model selection and performance estimation. |
| E5 | E5 text-embedding model family | A family of dense embedding models; the evaluated variant is `multilingual-e5-base`. |
| FT / PT | Fine-tuned / Pretrained | Labels that distinguish a task-adapted model from its original pretrained version. |
| IR | Information Retrieval | Retrieving and ranking documents relevant to a user's information need. |
| MAP | Mean Average Precision | A ranking metric that averages precision across relevant results and then across queries. |
| MRR | Mean Reciprocal Rank | A ranking metric based on the reciprocal rank of the first relevant result for each query. |
| NDCG | Normalized Discounted Cumulative Gain | A ranking metric that rewards relevant documents appearing higher in the result list. |
| OOF | Out-of-fold | Predictions or results for samples excluded from the corresponding fitting fold. |
| RAG | Retrieval-Augmented Generation | An architecture that retrieves external information before or during text generation. |
| RQ | Research Question | A specific question investigated empirically by the thesis. |
| SD | Standard Deviation | A statistical measure of dispersion around the mean. |
