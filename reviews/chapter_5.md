# Chapter 5: Experimental Evaluation

Source: `chapters/chapter_5.tex`. Page coverage: printed pages 32–43, PDF pages 41–52 of `main.pdf` (PDF page numbers are one-based). Numerical values follow the source; reported deltas were calculated before display rounding. Table numbers below follow the rendered PDF. From Table 5.6 onward, the source labels are one number higher than the rendered table numbers; each is identified explicitly to avoid ambiguity.

## Overall idea

Legal retrieval must be evaluated as a complete system. BM25 combined with semantic retrieval improves the lexical baseline in the evaluated collections, but adding E5 helps only some corpus conditions. BCA reveals that absent targets and shared legal references limit both attainable scores and statistical interpretation. Legal-domain fine-tuning produces large development gains in Study A and improves standalone dense ranking in Study B, yet neither result guarantees a meaningful improvement in the complete hybrid. The chapter preserves these negative results and limits causal claims to what the experiments actually establish.

## Page-by-page summaries

### Printed page 32 — PDF page 41

The chapter introduces its progression through hybrid performance, E5's incremental contribution, BCA evaluation, and legal-domain adaptation. Section 5.1 sets NDCG@10 as the primary endpoint and uses Hit@10, MRR@10, and MAP@10 to distinguish retrieval success from ordering quality. ALQAC/Zalo clean and parsed conditions share query identities; they are paired representations rather than independent datasets. BCA requires separate component-aware analysis. Table 5.1 begins by distinguishing fixed BM25, adapted BGE-M3, and frozen E5.

### Printed page 33 — PDF page 42

Table 5.1 concludes with two-way BM25+BGE-M3 and three-way BM25+BGE-M3+E5; only BGE-M3 changes during adaptation. Scores from different populations, folds, corpora, or adaptation recipes must not be pooled. Section 5.2 starts Table 5.2's pretrained comparisons: ALQAC A hybrid NDCG is 0.8805/0.8784 versus BM25 0.7986; ALQAC B is 0.7067/0.7055 versus 0.6479. The page also begins clean Zalo's standalone results.

### Printed page 34 — PDF page 43

Table 5.2 concludes: clean Zalo hybrids score 0.6805/0.6818 versus BM25 0.5264; parsed Zalo scores 0.7214/0.7344 versus 0.5620. BGE-M3 is the strongest standalone retriever in all four conditions, and both hybrids exceed it. Table 5.3 shows hybrid gains over BM25, strongest in Zalo. These results support system-level complementarity without isolating linguistic causes. The table begins BCA's descriptive comparison.

### Printed page 35 — PDF page 44

Table 5.3 finishes with BCA three-way NDCG 0.2297 versus BM25 0.1687. RQ1 is supported within the evaluated conditions, subject to corpus-specific limits. Section 5.3 and Table 5.4 isolate adding E5 to the existing two-way system: ALQAC A/B change by −0.0021/−0.0012, Zalo A by +0.0013, and Zalo B by +0.0130. Zalo B's stored paired Wilcoxon p is 5.1598×10⁻⁷. Query dependence and multiple conditions still require care. Opposite A/B patterns in ALQAC and Zalo do not isolate parsing's causal effect.

### Printed page 36 — PDF page 45

The parser discussion concludes that construction, mapping, fallback behavior, and article universe differ; no matched no-fallback ablation isolates fallback's effect. RQ2 therefore has a conditional answer. Section 5.4 and Table 5.5 report BCA giant, small-component OOF, and combined views for all and answerable queries. The reference graph has a giant component of 484/546 queries and 49 smaller components totaling 62. Combined all-query two-/three-way NDCG is 0.2283/0.2297, while small-component OOF is 0.2346/0.2309.

### Printed page 37 — PDF page 46

BCA's combined descriptive E5 gain is not supported by component-aware inference. Of 546 questions, 440 are answerable, 106 have no represented target, and 229 answerable questions have only partial target coverage. Scores reflect evidence presence, correct identity mapping, and ranking. Section 5.5 distinguishes corpus/mapping failures, misses beyond rank ten, and demotions within the top ten. E5 repairs some hits and loses others. The analysis does not establish legal-reasoning explanations such as exception or temporal-validity errors; a legally adjudicated taxonomy was not performed.

### Printed page 38 — PDF page 47

Section 5.6 introduces the six adaptation analyses. Section 5.6.1 reports Study A's passage-length-512 learning-rate/epoch pilot in Table 5.6 and batch/accumulation ablation in Table 5.7. The selected recipe uses learning rate 0.00002 and two epochs, with batch/accumulation 4/8 yielding development NDCG 0.7781/0.7934 versus pretrained 0.7172/0.7245. Selection is bounded by the restricted search and rule; it is not a global optimum claim.

### Printed page 39 — PDF page 48

Study A's development improvements of +0.060945/+0.068882 justify testing but do not prove generalization. Section 5.6.2 evaluates 640 Zalo parsed fold-0 queries with pretrained-selected fusion weights locked during encoder replacement: 0.2/0.8/0.0 for two-way and 0.2/0.5/0.3 for three-way. A flawed preliminary analysis exposed the fold, so this is corrected post-hoc evaluation on queries unseen in training/selection rather than a pristine first-use test. Tables 5.8–5.9 show all seeds reduce NDCG: two-way mean 0.6995 versus 0.7516; three-way mean 0.7346 versus 0.7595. Three-way seed 44 increases Hit@10 slightly while decreasing rank-sensitive metrics.

### Printed page 40 — PDF page 49

Table 5.10 reports 640 queries in 106 clusters; both confidence intervals cross zero, raw p is 0.7480, and Holm p is 1.0000. Observed regressions do not establish population-level harm; non-significance also does not establish equivalence. Neither hybrid meets the +0.01 practical improvement threshold. Section 5.6.3 and Table 5.11 show Study B improves dense-only mean NDCG from 0.6740 to 0.6928 (+0.018866), with all three seeds improving, but Recall@100 falls by 0.009115. Section 5.6.4 begins the question of hybrid transfer under locked weights.

### Printed page 41 — PDF page 50

Table 5.12 shows Study B's two-way NDCG falls from 0.7526 to 0.7483 (−0.004295); three-way rises only from 0.7467 to 0.7476 (+0.000898). Both fail the practical gate; Recall@100 decreases. Calibration changes, evidence overlap, and pretrained-selected weights are possible mechanisms, not established causes. Section 5.6.5 and Table 5.13 show Study A seed-42 query outcomes: improved/worse/tied counts are 102/210/328 for two-way and 102/163/375 for three-way. Repairs/new misses are 23/48 and 16/24, respectively; transition rows overlap the NDCG partition rather than adding to it.

### Printed page 42 — PDF page 51

Table 5.14 shows Study B's dense comparison improves/worsens/ties 127/96/417 queries, whereas two-way gives 81/93/466 and three-way 85/86/469. Section 5.6.6 connects development gains, Study A hybrid regression, Study B dense improvement, and weak hybrid transfer. Cross-collection adaptation is unestablished; secondary retuned fusion results are unavailable; a fresh untouched cohort would strengthen confirmation. Section 5.7 begins the final research-question synthesis.

### Printed page 43 — PDF page 52

Section 5.7 concludes: hybrids improve BM25 in the evaluated settings; E5's added value is conditional, clearest in parsed Zalo; adaptation can improve dense ranking without improving the complete hybrid meaningfully. BCA demands visible reporting of missing/partial evidence and component dependence through end-to-end and answerable-only views. Systems must be tested at their intended level of use, with controlled comparisons and cautious causal interpretation.

## Section-by-section summaries

### 5.1 Datasets and Experimental Setup

ALQAC and Zalo each use clean (A) and parsed (B) corpus conditions sharing the same queries; Zalo B includes fallback. Corpus sizes are referenced to Chapter 4's Table 4.1 rather than restated here. NDCG@10 is primary; Hit@10 measures top-ten recovery, MRR@10 first-relevant ordering, and MAP@10 multiple-target ranking. Query-paired ALQAC/Zalo inference must remain distinct from BCA's component-aware inference. Values use four decimal places; deltas precede rounding.

**Table 5.1 — System identities and comparison boundaries** (`tab:5.1`): BM25 stays fixed; BGE-M3 starts pretrained and is the adapted component; E5 remains frozen. Both two-way and three-way hybrids are evaluated with pretrained and adapted BGE-M3. Comparisons stay within their own population and protocol.

### 5.2 Lexical and Hybrid Retrieval

**Table 5.2 — Pretrained standalone and hybrid results, query-macro OOF population** (`tab:5.2`): the NDCG summary below includes every method and condition. The original table also reports MRR, MAP, and Hit at ten.

| Condition | BM25 | BGE-M3 | E5 | Two-way | Three-way |
|---|---:|---:|---:|---:|---:|
| ALQAC A | 0.7986 | 0.8437 | 0.8126 | 0.8805 | 0.8784 |
| ALQAC B | 0.6479 | 0.6684 | 0.6510 | 0.7067 | 0.7055 |
| Zalo A | 0.5264 | 0.6424 | 0.5640 | 0.6805 | 0.6818 |
| Zalo B | 0.5620 | 0.6889 | 0.6259 | 0.7214 | 0.7344 |

BGE-M3 is consistently the best individual component; hybrid scores exceed both BM25 and BGE-M3. For Zalo B, two-way/three-way MRR is 0.6767/0.6913, MAP 0.6705/0.6845, and Hit 0.8789/0.8889. This establishes complementarity at the system level without proving the linguistic mechanism.

**Table 5.3 — Hybrid NDCG@10 changes relative to fixed BM25** (`tab:5.3`):

| Condition | Two-way absolute / relative gain | Three-way absolute / relative gain |
|---|---:|---:|
| ALQAC A | +0.0819 / +10.2590% | +0.0798 / +9.9970% |
| ALQAC B | +0.0588 / +9.0690% | +0.0576 / +8.8910% |
| Zalo A | +0.1541 / +29.2760% | +0.1554 / +29.5210% |
| Zalo B | +0.1594 / +28.3680% | +0.1724 / +30.6830% |
| BCA combined descriptive | +0.0597 / +35.3820% | +0.0610 / +36.1760% |

BCA's BM25/two-/three-way scores are 0.1687/0.2283/0.2297. These gains answer RQ1 positively within the tested conditions; BCA remains descriptive and coverage-limited, and unchanged transfer to other corpora is not established.

### 5.3 Incremental Contribution of E5

**Table 5.4 — Incremental E5 contribution on the canonical ALQAC and Zalo populations** (`tab:5.4`) tests three-way against two-way, rather than E5 against BM25:

| Condition | NDCG change | Relative change | Stored paired Wilcoxon p |
|---|---:|---:|---:|
| ALQAC A | −0.0021 | −0.2380% | 0.4498 |
| ALQAC B | −0.0012 | −0.1630% | 0.7449 |
| Zalo A | +0.0013 | +0.1900% | 0.1548 |
| Zalo B | +0.0130 | +1.8030% | 5.1598×10⁻⁷ |

Parsed Zalo gives the clearest useful E5 increment, including higher MRR and Hit. Clean Zalo's gain is tiny and unsupported; ALQAC does not improve. Stored paired p-values do not resolve multiplicity or possible query dependence. ALQAC parsed scores are lower than clean scores, while Zalo parsed-with-fallback scores are higher; different construction, mapping, fallback, and article universes prevent attributing the difference to parsing itself. No matched no-fallback ablation measures fallback independently. RQ2 is condition-dependent.

### 5.4 BCA Coverage and Component-Aware Evaluation

**Table 5.5 — Compact BCA protocol and coverage views** (`tab:5.5`) covers three protocols, two cohorts, and four methods, with NDCG/MRR/MAP/Hit@10. The condensed NDCG view preserves all 24 method/cohort combinations:

| Protocol / cohort | N | BM25 | BGE-M3 | Two-way | Three-way |
|---|---:|---:|---:|---:|---:|
| Giant / all | 484 | 0.1670 | 0.2153 | 0.2275 | 0.2295 |
| Giant / answerable | 394 | 0.2051 | 0.2645 | 0.2795 | 0.2819 |
| Small OOF / all | 62 | 0.1817 | 0.2015 | 0.2346 | 0.2309 |
| Small OOF / answerable | 46 | 0.2449 | 0.2715 | 0.3162 | 0.3112 |
| Combined OOF / all | 546 | 0.1687 | 0.2137 | 0.2283 | 0.2297 |
| Combined OOF / answerable | 440 | 0.2093 | 0.2652 | 0.2833 | 0.2850 |

For combined all queries, adding E5 raises Hit from 0.5330 to 0.5495, while MRR falls from 0.3358 to 0.3348 and MAP from 0.1606 to 0.1589. Answerable-only combined Hit is 0.6614/0.6818, MRR 0.4167/0.4154, and MAP 0.1993/0.1972. Small-component Hit is unchanged by E5: 0.3871 for all queries and 0.5217 for answerable queries.

The graph's 484-query giant component dominates the descriptive aggregate, while the remaining 62 queries form 49 components. E5's slight combined advantage reverses in small-component OOF; component-aware inference does not establish an advantage. Of 546 queries, 106 have no indexed target, 440 have at least one, and 229 of those are partial-target cases. Unanswerable questions cannot yield positive Hit under the fixed corpus. Thus evaluation measures evidence existence, legal-identity mapping, and ranking together; ranking changes address only the last unless corpus construction changes.

### 5.5 Failure Analysis

Missing evidence needs corpus/mapping repair; available evidence outside the top ten needs ranking/fusion improvement; within-top-ten demotion reduces NDCG/MRR even if Hit stays fixed. BCA's 106 target-absent queries cannot be repaired by changing weights, encoders, or fusion. Partial coverage also penalizes methods for absent relevant targets despite retrieving available ones.

ALQAC/Zalo boundary examples show E5 both gains and loses hits, with representative cases preserved in Appendix E. Neither mean improvement nor mean regression applies uniformly to every query. Findings describe retrieval failures—absence, transitions at ten, within-law demotion, persistent misses—not adjudicated legal-reasoning causes. A legal taxonomy would need full-text review, sampling, annotation rules, and reviewer agreement; this was not performed.

### 5.6 Legal-Domain Adaptation

The section separates development selection, corrected Study A hybrid evaluation, Study B dense-only effects, hybrid transfer, query outcomes, and interpretation. The central question is generalization beyond development selection and usefulness within the complete hybrid.

#### 5.6.1 Development Selection

**Table 5.6 — Passage-512 learning-rate and epoch pilot: development NDCG@10** (source `tab:5.7`) compares three learning rates and three epochs:

| Learning rate | Epoch | Two-way | Three-way |
|---|---:|---:|---:|
| 5×10⁻⁶ | 1 | 0.7470 | 0.7685 |
| 5×10⁻⁶ | 2 | 0.7603 | 0.7785 |
| 5×10⁻⁶ | 3 | 0.7647 | 0.7815 |
| 1×10⁻⁵ | 1 | 0.7509 | 0.7816 |
| 1×10⁻⁵ | 2 | 0.7658 | 0.7873 |
| 1×10⁻⁵ | 3 | 0.7628 | 0.7897 |
| 2×10⁻⁵ | 1 | 0.7440 | 0.7757 |
| 2×10⁻⁵ | 2 | 0.7691 | 0.7923 |
| 2×10⁻⁵ | 3 | 0.7689 | 0.7958 |

The selected learning rate is 0.00002 with two epochs, under the restricted selection rule; the largest three-way pilot cell is not itself the selected recipe or proof of a global optimum.

**Table 5.7 — Batch ablation at the selected learning rate and epoch** (source `tab:5.8`): pretrained baseline is 0.7172/0.7245; batch/accumulation 1/32 yields 0.7725/0.7869, 2/16 yields 0.7693/0.7924, and 4/8 yields 0.7781/0.7934. The selected development gains are +0.060945 and +0.068882 (displayed +0.0609/+0.0689). These motivate unseen-data evaluation without establishing generalization.

#### 5.6.2 Corrected Hybrid Evaluation on Unseen Data

Study A evaluates Zalo parsed fold 0's 640 queries. Fusion is trained on permitted training-side folds with pretrained BGE-M3 and locked during replacement. BM25/BGE/E5 weights are 0.2/0.8/0.0 and 0.2/0.5/0.3. Because preliminary flawed analysis already exposed the fold, the corrected result is post-hoc, despite the queries being unseen during training and selection.

**Table 5.8 — Corrected Zalo fold-0 two-way hybrid evaluation** (source `tab:5.9`): pretrained NDCG/MRR/MAP/Hit is 0.7516/0.7015/0.6985/0.9141. Fine-tuned NDCG for seeds 42/43/44 is 0.7005/0.7005/0.6977; mean is 0.6995, a −0.052045 change. Mean MRR/MAP/Hit is 0.6453/0.6430/0.8766. All three seeds regress on NDCG, and all secondary mean metrics decline.

**Table 5.9 — Corrected Zalo fold-0 three-way hybrid evaluation** (source `tab:5.10`): pretrained metrics are 0.7595/0.7077/0.7048/0.9266. Seed NDCG is 0.7320/0.7340/0.7378; mean 0.7346, displayed delta −0.0249. Mean MRR/MAP/Hit is 0.6779/0.6754/0.9208. Regression is smaller than two-way but remains negative against its own matched comparator. Seed 44 Hit 0.9281 slightly exceeds baseline despite worse NDCG and MRR.

**Table 5.10 — Corrected paired statistics for NDCG@10** (source `tab:5.11`): both comparisons use 640 queries and 106 clusters. Two-way mean delta −0.0520 has 95% cluster CI [−0.0919, +0.1076]; three-way −0.0249 has CI [−0.0542, +0.0938]. Both raw p-values are 0.7480 and Holm-adjusted p-values 1.0000. Intervals include zero, so population-level harm is not statistically established. Non-significance is not equivalence, and neither result meets the +0.01 practical threshold. The supported conclusion is failure to demonstrate hybrid improvement under this protocol.

#### 5.6.3 Study B: Dense-Oriented Adaptation

**Table 5.11 — Study B post-hoc dense benchmark on 640 official queries** (source `tab:5.12`) distinguishes standalone dense effects from fusion effects. Pretrained NDCG/MRR/Recall@100 is 0.6740/0.6213/0.9617. Seeds 42/43/44 yield NDCG 0.6932/0.6925/0.6928 and MRR 0.6448/0.6431/0.6437. Mean metrics are 0.6928/0.6438/0.9526. All seeds improve NDCG; exact mean gain is +0.018866, while Recall@100 decreases by 0.009115. Fine-tuning therefore improves top-ten dense ranking on this fixed-corpus benchmark with a deeper-recall tradeoff.

#### 5.6.4 Transfer of Dense Improvements into Hybrid Retrieval

**Table 5.12 — Study B primary fusion outcomes under pretrained-locked weights** (source `tab:5.13`):

| Hybrid | Pretrained NDCG | Fine-tuned mean | Displayed delta | Relative delta | Recall@100 delta | Positive seeds | Gate |
|---|---:|---:|---:|---:|---:|---:|---|
| Two-way | 0.7526 | 0.7483 | −0.0043 | −0.5707% | −0.0057 | 0/3 | Fail |
| Three-way | 0.7467 | 0.7476 | +0.0009 | +0.1203% | −0.0031 | 2/3 | Fail |

Exact NDCG changes are −0.004295 and +0.000898, both below the +0.01 improvement threshold. Dense improvement does not produce a practically useful hybrid gain. Possible score-calibration changes, overlapping evidence, and pretrained-selected fusion weights remain unisolated hypotheses.

#### 5.6.5 Query-Level Analysis

**Table 5.13 — Query-level changes after fine-tuning, corrected seed 42** (source `tab:5.14`):

| Outcome | Study A two-way | Study A three-way |
|---|---:|---:|
| Higher NDCG@10 | 102 | 102 |
| Lower NDCG@10 | 210 | 163 |
| Unchanged NDCG@10 | 328 | 375 |
| Previously missing at ten, now retrieved | 23 | 16 |
| Previously retrieved at ten, now missing | 48 | 24 |
| Missing at ten in both systems | 32 | 31 |

Only the first three rows partition all 640 queries; hit-transition rows are additional overlapping descriptions. New misses exceed repairs, by more than two to one in two-way. Three-way buffers some losses but still introduces more misses than it repairs. Individual repaired examples do not overturn aggregate regression, which is also not uniform deterioration.

**Table 5.14 — Study B NDCG changes by query, using mean fine-tuned seed metric minus pretrained** (source `tab:5.15`): dense improved/worse/tied counts are 127/96/417; two-way 81/93/466; three-way 85/86/469. Each totals 640. Dense has a favorable balance that hybrids do not preserve, consistent with the weak aggregate transfer.

#### 5.6.6 Overall Interpretation

Study A development gains are followed by corrected unseen-query hybrid regressions; Study B establishes dense improvement followed by weak locked-weight hybrid transfer. Development or dense-only scores cannot substitute for end-to-end evaluation. The findings support dense fine-tuning's potential while showing that usefulness inside a hybrid must be measured separately.

Cross-collection adaptation to ALQAC/BCA is not established. Secondary retuned-weight results were unavailable, so the chapter does not rule out benefits under another fusion policy. A fresh untouched cohort is needed for cleaner confirmation. Observed negative transfer remains meaningful within these boundaries.

### 5.7 Experimental Synthesis

RQ1: hybrids improve the BM25 reference in evaluated ALQAC/Zalo conditions and descriptive BCA results. RQ2: E5's incremental value depends on the condition, clearest in parsed Zalo; ALQAC and component-aware BCA evidence do not support a universal three-way advantage. RQ3: adaptation improves development and can improve standalone dense retrieval without a meaningful complete-hybrid gain.

BCA demonstrates that evidence availability, mapping, partial coverage, and connected-component dependence shape score interpretation. End-to-end and answerable-only results should both remain visible. The chapter's overarching principle is evaluation at the level of actual system use, with controlled comparisons, explicit negative results, and limited causal claims.

## Coverage check

- All 12 pages covered: printed 32–43 / PDF 41–52.
- All 7 sections and 6 subsections covered with exact source heading text and rendered numbering.
- All 14 source tables covered: rendered Tables 5.1–5.14; source labels `tab:5.1`–`tab:5.5` and `tab:5.7`–`tab:5.15`. The source contains no `tab:5.6`.
- Clean/parsed and fallback boundaries, BCA descriptive/component distinction, target coverage, Study A post-hoc status and inferential limits, Study B dense/locked-hybrid distinction, and unavailable confirmatory/retuned evidence are retained.
