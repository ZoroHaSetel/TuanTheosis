# Chapter 4 — Proposed Methodology

Source: `chapters/chapter_4.tex`. Page references use the current `main.pdf`: printed pages 21–31, PDF pages 30–40 (both numbered from 1). Source headings and content are authoritative.

## Overall idea

The chapter specifies a controlled experiment for Vietnamese legal **article retrieval**. It compares BM25, pretrained BGE-M3, pretrained multilingual-E5-base, and weighted combinations; constructs clean/parsed corpus conditions and a public-question BCA collection; and tests two distinct BGE-M3 adaptation recipes. Its contribution is dataset construction, experimental comparison, and careful interpretation rather than a new ranking algorithm. Reliable interpretation depends on preserving document identities, separating model/weight selection from evaluation, accounting for shared-law dependencies, and recognizing missing or incomplete targets.

## Page-by-page summary

### Printed page 21 — PDF page 30

**Chapter introduction; 4.1 Problem Formulation.** The searchable corpus is an ordered collection of legal articles with normalized legal identifiers. A question has recorded law–article relevance targets; each configuration returns a ranking evaluated primarily at ten results. Configuration selection maximizes mean NDCG@10 on a designated selection population. Labels guide selection and evaluation, while retrieval receives only query text and the indexed corpus. Corpus absence makes a target unretrievable regardless of model quality. Ranking quality also does not establish generated legal-answer correctness.

### Printed page 22 — PDF page 31

**4.2 Retrieval and Evaluation Pipeline; opening of 4.3 Datasets and Corpus Construction; Table 4.1 begins.** BM25 supplies lexical scores and BGE-M3/E5 supply dense scores over the same ordered corpus. Per-query normalization precedes weighted fusion and top-ten evaluation. The two-way hybrid uses BM25+BGE-M3; the three-way adds E5. The experiment isolates first-stage retrieval without reranking, routing, query expansion, approximate candidate filtering, or generation. ALQAC and Zalo each have paired clean and parsed conditions sharing the same questions; these conditions are dependent representations, not independent datasets. Table 4.1 lists their sizes and boundaries.

### Printed page 23 — PDF page 32

**Table 4.1 completes; 4.3 continues; 4.3.1 BCA Target Construction; opening of 4.3.2 Worked BCA Example.** ALQAC parsing can change article boundaries and article counts. Zalo replaces reference text only where aligned parsed text exists and otherwise retains reference text; its A/B contrast therefore measures this particular parsed-with-fallback construction. BCA begins with 652 public question–answer records and retains 546 with at least one extracted law reference. Questions become queries; answers supply citation evidence only. Law and article references are normalized into corpus identities. The collection captures natural legal information needs, but heuristic extraction, non-exhaustive citations, and unavailable provisions limit its labels. A fire-prevention question introduces the worked transformation.

### Printed page 24 — PDF page 33

**Figures 4.1 and 4.2.** Figure 4.1 connects preserved article/query identities to BM25, BGE-M3, and E5 score matrices, per-query normalization, law-component grouping, training-side fusion selection, locked fold weights, unseen top-ten rankings, and query-level metrics/paired comparisons. Figure 4.2 connects cleaned public question–answer records to citation extraction and identity normalization, alongside construction of the searchable legal corpus. The branches meet at target coverage and component validation before component-aware evaluation. These diagrams make both the scoring flow and the evaluation boundaries explicit.

### Printed page 25 — PDF page 34

**Table 4.2; 4.3.2 completes; opening of 4.4 Lexical and Dense Representations.** The worked BCA question concerns mandatory fire-prevention equipment in apartment buildings. Answer citations provide decree and article candidates, normalized into law-plus-article targets; only the question and candidate article text enter the retriever. The example demonstrates dataset construction without claiming complete legal relevance judgments. BM25 preprocessing lowercases, treats non-word punctuation as separators, and splits on whitespace. Dense similarity is a dot product of L2-normalized query/article vectors, with a small norm floor to avoid division by zero.

### Printed page 26 — PDF page 35

**Table 4.3; 4.4 completes; opening of 4.5 Score Normalization and Fusion.** BGE-M3 has 1,024-dimensional embeddings and E5 has 768; both use a baseline 512-token input limit. Only BGE-M3 is adapted. Exhaustive corpus scoring means an available mapped target outside the top ten is a scoring/fusion failure, rather than loss in an approximate candidate stage; this experiment does not establish production latency. Each channel is min–max normalized independently per query across the full corpus. Weighted two-way and three-way scores are defined with nonnegative weights summing to one; the grid advances in 0.1 steps.

### Printed page 27 — PDF page 36

**4.5 completes; 4.6 Evaluation Design; Algorithms 4.1 and 4.2.** The grids contain 11 two-way and 66 three-way candidates, including zero-weight boundaries. Training-side NDCG@10 selects weights, then fixes them for unseen evaluation. Since the three-way grid includes the two-way boundary, better selection-set fit alone cannot establish E5's added value. Law-connected query components stay together across folds, and out-of-fold results evaluate a selection procedure rather than one universal weight vector. Algorithm 4.1 selects the first maximally scoring candidate per fold and aggregates unseen query metrics; Algorithm 4.2 normalizes, combines, and returns the ten highest-scoring articles with locked weights. BCA needs separate giant-component holdout, small-component out-of-fold, and combined descriptive views because shared legal targets create dependence.

### Printed page 28 — PDF page 37

**4.7 Legal-Domain Fine-Tuning; 4.7.1 Training Pairs and Negatives; Table 4.4; opening of 4.7.2 Training Objective and Configuration.** Adaptation changes only BGE-M3, leaving BM25/E5 fixed. Study A uses Zalo positives available in both clean and parsed views and creates paired examples. Mined lexical/dense negatives exclude known positives, duplicates, missing articles, and evaluation-reserved laws. Pilot training uses 1,917 queries/3,834 A/B groups from folds 2–4, protecting folds 0–1 and 258 laws. Final training uses 2,556 queries/5,112 groups from folds 1–4, protecting fold 0 and 110 laws. Both show zero law overlap, which protects identities without proving different concepts, language, or legal systems. The single-positive contrastive objective compares each query's selected positive with all passages in its actual batch, including explicit and in-batch negatives.

### Printed page 29 — PDF page 38

**Table 4.5; 4.7.2 continues; opening of 4.7.3 Study B: Dense-Oriented Adaptation.** Study A's locked configuration is full BGE-M3 adaptation for two epochs at learning rate 2×10⁻⁵, four-query contrastive batches, eight accumulation steps, effective optimizer batch 32 groups, one positive/seven explicit negatives, query/passage limits 256/512 tokens, temperature 0.02, first-token pooling, L2 normalization, and seeds 42–44. Pilot folds 2–4 train; fold 1 selects recipe settings by hybrid NDCG@10; final folds 1–4 retrain. Fold 0 is unseen in corrected training/selection, but previous flawed analysis exposed it, so the corrected result is post-hoc rather than pristine. Study B instead prioritizes dense retrieval, uses an all-positive mask and five explicit negatives, requires a larger true contrastive batch, and evaluates three seeds on the same 640 official queries used for dense/fusion comparisons.

### Printed page 30 — PDF page 39

**Figure 4.3.** The evidence flow runs from pilot training on folds 2–4, learning-rate/epoch candidates, fold-1 checkpoint selection and batch ablation, through a locked recipe and three-seed final training on folds 1–4. Initial fold-0 evaluation is followed by discovery of a document-identity error, corrected weight selection on folds 1–4, and the post-hoc corrected fold-0 comparison. The diagram preserves the history relevant to interpreting evaluation independence.

### Printed page 31 — PDF page 40

**4.7.3 completes; 4.8 Method Summary.** Study B's multi-positive objective maximizes the aggregate probability mass of all recognized positive candidates against all candidates in the contrastive batch. It is distinct from Study A's one-selected-positive recipe and asks whether dense-only improvement transfers to complete hybrids. The closing summary emphasizes article identities, explicit selection boundaries, lexical/dense fusion, and BCA coverage/component limitations; Chapter 5 supplies effectiveness, failure analysis, and adaptation outcomes.

## Section-by-section summary

### 4.1 Problem Formulation

For ordered corpus D and query q, recorded relevance set Rq consists of law–article targets. A configuration θ produces a ranked list πq(θ), primarily evaluated at k=10. The selection equation chooses θ maximizing mean NDCG@10 over Qsel; candidates include fusion weights and adaptation recipes. Relevance labels never enter query-time retrieval. Missing corpus targets and the distinction between article retrieval and legal-answer correctness bound the study's claims.

### 4.2 Retrieval and Evaluation Pipeline

All components score the identical ordered corpus: BM25 is lexical, BGE-M3 and multilingual-E5-base are dense. Normalize each score channel per query, add weighted scores, and evaluate the top ten by legal identity. Compare individual components, BM25+BGE-M3, and BM25+BGE-M3+E5. Figure 4.1 additionally shows law-component grouping feeding training-side selection before locked unseen evaluation and paired metric comparisons. The restricted architecture isolates first-stage lexical–semantic retrieval.

### 4.3 Datasets and Corpus Construction

Table 4.1 fixes the five canonical conditions:

| Condition | Queries | Articles | Evaluation/construction boundary |
|---|---:|---:|---|
| ALQAC A, clean | 811 | 3,363 | Law-component grouped out-of-fold evaluation; preserve reference identities |
| ALQAC B, parsed | 811 | 3,381 | Same ordered questions; independently parsed article boundaries |
| Zalo A, clean | 3,196 | 61,425 | Law-component grouped out-of-fold evaluation; clean reference corpus |
| Zalo B, parsed with fallback | 3,196 | 61,425 | Same questions; aligned parsed text replaces reference text where available |
| BCA, canonical evaluation | 546 | 14,789 | Giant-component holdout plus small-component out-of-fold evaluation |

A/B conditions are paired, and Zalo's fallback preserves availability while making parsing effects inseparable from the fallback construction. BCA retains 546 of 652 source records based on extracted law-reference availability; subsequent coverage analysis distinguishes answerable, partially answerable, and unavailable targets.

### 4.3.1 BCA Target Construction

Cleaned question text becomes the retrieval query; answers only generate law/article citation targets. Normalize law names to corpus legal identifiers and article identifiers separately, ensuring identity-based matching. Figure 4.2 links this process with corpus construction, coverage checks, and component validation. Citations are heuristic, may be incomplete, and may point outside the corpus; they are not exhaustive legal relevance judgments.

### 4.3.2 Worked BCA Example

Table 4.2 follows an apartment-building fire-prevention question through answer-reference extraction, standardized decree identity, canonical law-plus-article target identity, and query/article retriever inputs. The example explains transformation and label provenance while acknowledging that supporting provisions may be omitted and extracted citations may need legal review.

### 4.4 Lexical and Dense Representations

BM25 uses fixed lowercase/punctuation-separation/whitespace preprocessing. The dense equation computes cosine-like normalized dot products with norm floors of 10⁻¹⁰. Table 4.3 distinguishes BGE-M3 (1,024 dimensions, primary dense component, adapted later) from E5 (768 dimensions, additional dense component, always frozen), both capped at 512 baseline tokens. Exhaustive scoring removes approximate candidate-generation recall as an explanation for missed available top-ten targets, but supplies no production-latency claim.

### 4.5 Score Normalization and Fusion

Per-query, per-channel full-corpus min–max normalization is `(score − minimum) / max(maximum − minimum, ε)`. Two-way fusion is `wb × BM25 + (1 − wb) × BGE-M3`; three-way fusion adds E5 with nonnegative `wb + wg + we = 1`. Grid increments of 0.1 yield 11 and 66 settings, respectively, including boundaries. Select by training-side mean NDCG@10 and lock weights for unseen data. Only unseen comparison supports E5's incremental value because three-way selection includes the two-way model as a candidate.

### 4.6 Evaluation Design

Keep queries linked through reference-law components together, reducing shared-law leakage between weight selection and evaluation. Algorithm 4.1 evaluates each grid candidate on the training-side queries, selects the first tied maximum, applies it to unseen queries, and aggregates out-of-fold rows. Algorithm 4.2 normalizes all corpus scores, computes the locked weighted sum per article, and returns ten results. BCA reports dominant-component performance, smaller-component performance, and a combined descriptive view separately because they answer different questions and ordinary query-level treatment would overstate reliability.

### 4.7 Legal-Domain Fine-Tuning

Test legal supervision by replacing pretrained BGE-M3 with adapted BGE-M3; BM25/E5 remain fixed, and hybrid fusion policy must remain explicit. Keep Study A: Hybrid-Oriented Adaptation separate from Study B: Dense-Oriented Adaptation because their objectives, recipes, and research questions differ.

### 4.7.1 Training Pairs and Negatives

Study A builds clean/parsed paired examples from Zalo queries with an available common positive. Mine negatives from lexical/dense rankings while excluding positives, duplicates, unavailable documents, and protected laws. Table 4.4 records pilot/final counts and zero protected-law overlap. This check establishes identifier separation, not absence of conceptual or linguistic similarities or transfer to unfamiliar legal systems.

### 4.7.2 Training Objective and Configuration

The single-positive in-batch loss is the negative mean log probability of selected positive index yi=iG among BG passages, using normalized dot products divided by τ=0.02 and G=8 (one positive/seven explicit negatives). Table 4.5 locks the full-encoder training parameters described above. Four queries form the actual contrastive batch; eight-step gradient accumulation creates a 32-group optimizer effective batch without making all 32 groups simultaneous contrastive candidates.

Recipe selection uses fold 1 after pilot training on folds 2–4; final seeds 42, 43, and 44 train on folds 1–4. Figure 4.3 records the initial evaluation, discovered document-identity error, and corrected fusion-weight selection on folds 1–4 before the corrected fold-0 comparison. Earlier exposure of fold 0 requires the post-hoc qualification even though corrected training and selection exclude it.

### 4.7.3 Study B: Dense-Oriented Adaptation

Use an all-positive mask, five explicit negatives, a larger actual contrastive batch requirement, and a Zalo-only first passing data stage. Three final seeds evaluate the selected setting on the shared 640 official queries. The multi-positive equation is negative mean `[log sum exp over positives − log sum exp over all candidates]`; it rewards total positive probability rather than one selected positive. The question is whether gains in BGE-M3 dense retrieval survive integration into full hybrids. The chapter does not specify Study B's complete numerical configuration, so Study A's values should not be transferred to it.

### 4.8 Method Summary

The design combines identity-preserving article retrieval, lexical/dense comparison, explicitly selected fusion weights, and separated adaptation studies. BCA contributes natural-question dataset construction and exposes target-coverage and component-dependence constraints. The next chapter reports results and failures within these boundaries.

## Coverage check

- All 11 pages covered: printed 21–31 / PDF 30–40.
- All 8 sections and 5 subsections covered with their exact source heading names and numbering.
- All 3 figures, 5 tables, and 2 algorithms summarized.
- All 8 displayed mathematical definitions/objectives covered: ranked list, NDCG selection, dense similarity, min–max normalization, two-way fusion, three-way fusion, Study A loss, and Study B loss.

