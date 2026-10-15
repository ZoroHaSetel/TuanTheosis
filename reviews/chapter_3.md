# Chapter 3 — Theoretical Background

Source: `chapters/chapter_3.tex`. Page references follow `main.pdf`: printed pages 14–20, corresponding to PDF pages 23–29. Source headings and text take precedence over PDF extraction artifacts.

## Overall idea

The chapter establishes the theory needed to compare lexical retrieval, dense retrieval, hybrid fusion, and supervised adaptation for Vietnamese legal article retrieval. It links model scores to explicit evaluation rules: relevance targets can be articles or entire laws, each target earns credit only once, and a missing corpus target cannot be recovered by better ranking. Fusion and training choices must be evaluated under documented candidate, normalization, supervision, and data-selection boundaries. Chapter 4 supplies implementation details; Chapter 5 interprets statistical results.

## Page-by-page summaries

### Printed page 14 · PDF page 23

- The chapter introduction identifies retrieval models, fusion, training objectives, and evaluation metrics as its scope.
- **3.1 Queries, Articles, and Relevance:** An ordered corpus `D`, query population `Q`, and deduplicated target set `R_q` define the task. Outputs are ranked article identities. Corpus availability and ranking quality are distinct; no scoring method can retrieve an absent target. Article-level and law-level annotations each receive at most one unit of credit.
- **3.2 Lexical Scoring and BM25 / 3.2.1 TF–IDF as a Conceptual Starting Point:** TF–IDF emphasizes within-document term occurrences and discounts collection-wide common terms. It motivates BM25 but is not an experimental baseline here.
- **3.2.2 BM25, opening:** The BM25 equation combines term rarity, saturating term frequency, and document-length normalization. `k_1` controls frequency saturation; `b` controls length normalization. Indexed document length and average corpus length enter the score. Implementation-specific IDF conventions are deferred to Chapter 4.

### Printed page 15 · PDF page 24

- **3.2.2 BM25, continuation:** Repetition has diminishing returns. Parsing can raise scores by removing unrelated text or lower them by removing matching terms; it does not uniformly reduce lexical scores. BM25 is a credible legal-retrieval baseline, supported by a second-place vanilla submission in COLIEE 2021 case retrieval. Its limitations motivate complementary dense evidence: lexical overlap does not directly capture unrepresented paraphrases or prove legal applicability.
- **3.3 Dense Representations and Similarity:** Bi-encoders encode queries and documents separately, permitting precomputed document vectors. Dot product and cosine similarity coincide for unit-normalized nonzero vectors. Encoder revision, pooling, normalization, and truncation still independently define the representation. Sentence-BERT and DPR are precedents with different original tasks. Single-vector findings do not generalize to token-level late-interaction architectures such as ColBERT.
- **3.3.1 BGE-M3:** BGE-M3 supports multilingual dense, sparse, and multi-vector retrieval and up to 8,192 input tokens; this thesis uses only its dense representation. BM25 plus BGE-M3 dense retrieval is distinct from combining BGE-M3’s own modes. A model’s maximum supported length is not necessarily the experimental length. Actual effectiveness and complementarity require target-collection measurement.

### Printed page 16 · PDF page 25

- **3.3.2 Multilingual-E5:** The selected `intfloat/multilingual-e5-base` checkpoint has 12 layers, 768-dimensional embeddings, attention-mask-aware mean pooling, normalized vectors, and a 512-token input limit. Retrieval uses `query: ` and `passage: ` prefixes even for non-English text. Contrastive pretraining and supervised fine-tuning underlie the model. Its additional value must be tested against BM25+BGE-M3; two encoders can share errors, and tokenization/truncation differences can confound semantic comparisons.
- **3.4 Normalization and Fusion / 3.4.1 Lexical–Semantic Hybrid Retrieval:** Hybrid retrieval tests whether lexical and semantic signals improve the combined ranking. Full-corpus fusion scores every document in every channel; candidate-union fusion is limited to first-stage results. Candidate depth and score combination are separate choices, since fusion cannot recover a target excluded by all candidate lists.
- **3.4.2 Multi-Retriever Fusion:** A convex weighted sum combines normalized BM25, BGE-M3, and E5 scores. Nonnegative weights sum to one. Setting E5’s weight to zero recovers the two-way system with otherwise identical settings. Including that boundary guarantees the search’s optimal development score is no worse than the two-way subset, but says nothing guaranteed about unseen data. Zero E5 weight means the channel is unused. Useful complementarity needs metric evidence, not merely positive weights.

### Printed page 17 · PDF page 26

- **3.4.3 Score Normalization and Fusion:** Min–max scaling uses each channel’s minimum and maximum over candidate set `C_q`; a nonconstant score range is required, with a deterministic fallback such as all zeros for constant scores. Z-score scaling uses the candidate mean and positive standard deviation and is not restricted to `[0,1]`. Both depend on the candidate population, so adding documents can change normalized values even if existing raw scores remain fixed.
- Reciprocal rank fusion sums `1/(c + rank)` over rankings containing a document. Ranks are one-based and `c > 0` smooths their effects. RRF avoids comparing raw score scales but still depends on ranking depth and parameters. No universal fusion winner follows from results in particular settings; normalization, weights, candidate depth, and selection data must be specified.
- **3.5 Contrastive Adaptation and Negative Sampling, introduction:** Legal-domain language-model pretraining and supervised retrieval fine-tuning are different interventions. LEGAL-BERT’s adaptation to legal language and DPR’s relevance-supervised ranking illustrate that knowing legal prose is insufficient evidence of retrieval effectiveness.

### Printed page 18 · PDF page 27

- **3.5.1 Contrastive Learning:** An InfoNCE-style loss encourages a labeled positive to outrank negative competitors. Temperature changes sensitivity to score differences, and the negative set/batch defines the competitors. Reduced training loss does not ensure better unseen-query retrieval. Multiple positives can use a set-positive numerator or averaged positive-specific losses with other positives masked; these are distinct objectives whose precise policies appear in Chapter 4.
- **3.5.2 Negative Sampling:** Random negatives do not need high ranks, in-batch negatives reuse other examples’ passages, and hard negatives are high-ranking candidates lacking positive labels. Known-positive exclusion avoids contradictions but does not prove unjudged articles irrelevant. Choosing one positive must not expose another known positive as an unmasked negative. Explicit filtering, in-batch masking, and semantic review are distinct safeguards.
- **3.5.3 Hard-Negative Mining:** Static mining fixes competitors; dynamic mining refreshes them during learning. Reproduction needs the miner checkpoint, corpus snapshot, rank range, filters, and refresh schedule. Adaptation must be tested alone and in hybrid systems because it can overlap with BM25 or reduce useful disagreement. Fixed pretrained fusion weights test component substitution; permitted development-data retuning tests the adapted whole system.

### Printed page 19 · PDF page 28

- **3.6 Target Matching and Evaluation Metrics:** The evaluator partially partitions scores to select ten candidates, then sorts them. Each article matches only previously unmatched targets. Empty article identifiers or `toanvan` signify a whole-law wildcard; other targets require matching law and article identifiers. Multiple articles from one law cannot repeatedly earn credit for one law-level target.
- NDCG@10 discounts matches by rank and divides by ideal gain based on up to ten annotated targets. Queries without targets score zero. Absent corpus targets stay in the ideal denominator, so the measure includes coverage limitations; mixed target types also depend on implemented matching order.
- Hit@1/5/10 measures whether any target appears. Recall measures the fraction of targets recovered; the two coincide only for single-target queries in the stated setting. The canonical baseline aggregate does not report true target recall, including Recall@100.
- MRR@10 rewards the first matching rank; no match contributes zero. AP@10 accumulates precision at matching ranks and divides by `max(1, min(target count, 10))`; MAP averages these AP values. This truncated denominator can differ from other implementations. Aggregate metrics use query-macro means, including zero-score queries, unless explicitly restricted to an answerable-only cohort. They evaluate annotated recovery, not exhaustive legal relevance.

### Printed page 20 · PDF page 29

- **3.7 Grouped Evaluation and Statistical Interpretation:** Queries sharing target laws form connected components, including connections through multi-law queries. Keeping each component in one fold prevents reference-law overlap between fusion selection and evaluation. It neither splits the searchable corpus nor establishes that encoders never encountered the legal texts.
- Query-, component-, and fold-macro averaging can differ with unequal group sizes. Confidence intervals must state the resampling unit. Training-seed variability is different from uncertainty over a new query population. An interval spanning zero neither establishes equivalence nor removes the observed difference; Chapter 5 applies these interpretation boundaries.
- **3.8 Chapter Summary:** Lexical and dense models produce scores, fusion combines them, and contrastive learning adapts dense representations. Target-aware evaluation and grouping assess these interventions within explicit corpus and selection limits.

## Section-by-section summaries

### 3.1 Queries, Articles, and Relevance

Retrieval ranks article identities against deduplicated article- or law-level targets. Corpus coverage limits what can be recovered; ranking determines where available targets appear. Each target counts once, preventing whole-law annotations from becoming multiple independent article judgments.

### 3.2 Lexical Scoring and BM25

This section introduces sparse lexical matching and the BM25 baseline, including the consequences of term frequency, rarity, document length, and preprocessing.

#### 3.2.1 TF–IDF as a Conceptual Starting Point

TF–IDF rewards frequent terms within a document while discounting terms common throughout the collection. Its role here is to explain the foundation of BM25; the thesis does not evaluate TF–IDF as a separate baseline.

#### 3.2.2 BM25

BM25 sums query-term contributions weighted by IDF, using saturating frequency and length normalization. Its equation explains why repeated words eventually add little and why parsing can either increase or decrease scores. BM25’s strong legal-retrieval precedent supports its baseline status, while paraphrase and applicability limits motivate dense retrieval. Chapter 4 specifies the IDF implementation.

### 3.3 Dense Representations and Similarity

Separate query and document encoders produce vectors `u` and `v`. Similarity is either `uᵀv` or `uᵀv/(||u||₂ ||v||₂)`; the equations define how embeddings produce rankings and when dot product equals cosine. Pooling, normalization, truncation, and encoder revision are still separate experimental choices. Bi-encoder examples do not imply that single-vector results characterize all neural retrieval, including ColBERT’s token-level late interaction.

#### 3.3.1 BGE-M3

The thesis uses the dense channel of a model also capable of sparse and multi-vector retrieval. Its 8,192-token capability is a model limit rather than proof of the chosen experimental length. Multilingual support alone cannot establish collection-specific effectiveness or complementarity with BM25.

#### 3.3.2 Multilingual-E5

E5-base provides a second dense signal through a 12-layer encoder with 768-dimensional, normalized mean-pooled embeddings, a 512-token limit, and required query/document prefixes. Its contribution must be measured beyond BM25+BGE-M3 because correlated errors can limit gains. Different tokenization and truncation also affect the inputs seen by the models.

### 3.4 Normalization and Fusion

Fusion combines retrieval channels, but its interpretation requires explicit candidate populations, score transformations, weights, and selection data.

#### 3.4.1 Lexical–Semantic Hybrid Retrieval

Hybrid retrieval hypothesizes improvement from complementary evidence. Full-corpus scoring and candidate-union scoring define different reachable document sets. Weights cannot overcome missing candidates, so candidate depth must be distinguished from the fusion rule.

#### 3.4.2 Multi-Retriever Fusion

The equation `S = w_b S̃_b + w_g S̃_g + w_e S̃_e`, with nonnegative weights summing to one, defines the three-way convex combination. The `w_e = 0` boundary nests the two-way system. A development search including it cannot have a worse optimum than that subset, but generalization gains remain empirical. Metrics should distinguish early precision, first-hit position, and target recovery; weights alone are insufficient evidence of complementarity.

#### 3.4.3 Score Normalization and Fusion

Min–max scaling computes `(S_j − a_j)/(b_j − a_j)` over `C_q`, mapping a nonconstant channel into a common range. Constant channels need a deterministic handling rule. Z-score scaling computes `(S_j − μ_j)/σ_j` for positive standard deviation and yields unbounded standardized scores. The candidate set changes either transformation. RRF instead sums inverse smoothed ranks, `Σ 1/(c + r_j)`, over rankings containing the document. This avoids score-scale comparisons but retains depth and parameter dependencies; no fusion rule is universally superior on the evidence described.

### 3.5 Contrastive Adaptation and Negative Sampling

Retrieval adaptation learns relevance-based ranking, which is distinct from general adaptation to legal language. Training objectives and competitor selection jointly determine the intervention.

#### 3.5.1 Contrastive Learning

The single-positive loss is the negative logarithm of the positive’s temperature-scaled exponential similarity divided by the positive-plus-negatives sum. It encourages relative separation from competitors. Temperature and batch composition govern the learning pressure. Set-positive and masked positive-specific objectives treat multiple positives differently and must be reported precisely. Better training loss does not guarantee stronger test retrieval.

#### 3.5.2 Negative Sampling

Random, in-batch, and hard negatives differ in how competitors are chosen. Known-positive filtering and masking prevent contradictory supervision, but unjudged documents may still be relevant. Explicit filtering, batch masks, and semantic checks address different risks and require separate reporting.

#### 3.5.3 Hard-Negative Mining

Static mining fixes a competitor set; dynamic mining updates it as the model evolves. Checkpoints, corpus snapshots, rank ranges, filters, and schedules make this reproducible. Dense-only and hybrid results answer different questions. Holding fusion weights fixed measures component replacement; retuning on permitted development data measures the complete adapted system.

### 3.6 Target Matching and Evaluation Metrics

Top-ten selection and one-time target matching underpin all metrics. Whole-law wildcards use an empty article identifier or `toanvan`; article targets require both identifiers. The binary indicator `y_(q,r)` records a newly matched target at rank `r`.

- **NDCG@10:** divides logarithmically discounted matched-target gain by ideal gain for `min(|R_q|, 10)` targets. It measures ranking quality with unavailable targets retained in the denominator and gives targetless queries zero.
- **Hit@k:** an indicator that at least one new target occurs by rank `k`, reported for 1, 5, and 10. It measures any successful recovery.
- **Recall@k:** `Σ y_(q,r)/|R_q|` for nonempty target sets. It measures the fraction recovered, differs from hit for multi-target queries, and is absent from the canonical baseline aggregate, including Recall@100.
- **MRR@10:** averages the reciprocal first-hit rank within ten results, assigning zero to no hit. It measures first-match position.
- **Precision and AP@10:** precision at rank `r` is matches through `r` divided by `r`; AP sums this precision at matching ranks and divides by `max(1, min(|R_q|, 10))`. The exact truncated denominator matters for comparisons.
- **MAP@10:** the query mean of AP@10. Like other aggregates here, it includes zero-score queries unless an answerable-only cohort is explicitly declared.

Mixed law/article matching depends on implemented order, and these measures represent annotated target recovery rather than complete legal relevance.

### 3.7 Grouped Evaluation and Statistical Interpretation

Connected components of shared target laws remain within folds to prevent reference-law leakage between fusion selection and evaluation. The searchable corpus remains available, and this grouping says nothing definitive about encoder pretraining exposure. Macro averaging units and confidence-interval resampling units must be stated. Seed variability and population uncertainty differ; an interval crossing zero does not prove equivalence or negate the observed effect.

### 3.8 Chapter Summary

BM25, bi-encoders, fusion, and contrastive adaptation define the retrieval interventions. Deduplicated target matching, ranking metrics, and grouped evaluation define how to assess them under explicit corpus and selection boundaries.

## Coverage verification

- All **7 pages**, **8 sections**, and **10 subsections** are covered above in source order with their exact heading names and inferred Chapter 3 numbering.
- All **11 display-math blocks** are explained: BM25; dot/cosine similarities; convex fusion; min–max normalization; z-score normalization; RRF; contrastive loss; NDCG; hit; MRR; and the precision/AP/MAP block. The inline recall formula is also covered.
- The source contains **no figures or tables**.
