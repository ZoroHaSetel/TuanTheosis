# Chapter 2 — Literature Review

## Overall idea

The chapter uses prior research to motivate a controlled investigation of Vietnamese legal article retrieval. It asks whether lexical–semantic fusion improves BM25, whether E5-base adds value to an existing BM25+BGE-M3 hybrid, and whether supervised dense adaptation improves the hybrid beyond the development cohort. Earlier studies establish methods and evaluation principles; their scores cannot be transferred directly across languages, jurisdictions, retrieval units, or evaluation protocols.

## Page-by-page summary

### Printed page 6 — PDF page 15

- The chapter introduces the research gap: the incremental value of additional retrieval capacity under the project's legal collection and evaluation constraints. Mathematical definitions are deferred to Chapter 3.
- Section 2.1 distinguishes retrieving judgments, statutes, articles, and passages. COLIEE's Canadian case tasks and Japanese statute tasks clarify the difference between retrieval and entailment but are not interchangeable with Vietnamese article retrieval.
- ALQAC defines relevant articles as provisions usable to answer a question. This supports evaluating retrieval separately from question answering, while acknowledging that the judgments may not contain every defensible supporting provision.
- An illustrative application-deadline question separates topical similarity from evidence that satisfies the question's conditions. Lexical matching can preserve specific terms; semantic matching can connect different expressions of an information need. Neither guarantees legal sufficiency.

### Printed page 7 — PDF page 16

- Section 2.1 completes the distinction between similarity and evidence, then examines article boundaries. Short passages may match a rule closely but omit exceptions or cross-references; full articles preserve context but combine subtopics. Passage predictions must map back to article identifiers when article-level judgments are used.
- Vietnamese word segmentation changes lexical vocabularies and frequency statistics. PhoBERT demonstrates that segmentation matters in Vietnamese NLP, without proving a particular segmenter helps this retriever. Dense input must follow the chosen encoder's preprocessing requirements.
- Retrieval-augmented generation connects retrieval with answer production, but ranking effectiveness does not measure correct interpretation, citation fidelity, or legal answer quality.
- Section 2.2 introduces BM25 as a serious lexical reference. Its probabilistic foundations and competitive legal case-retrieval evidence justify retaining a strong baseline, while leaving Vietnamese article effectiveness unresolved.

### Printed page 8 — PDF page 17

- Section 2.2 explains that BM25 must have explicit preprocessing and article boundaries for a fair comparison. This thesis retains it as the fixed reference and does not claim an untested segmentation contribution. Scoring mathematics and implementation are specified later in Sections 3.2 and 4.4.1.
- Section 2.3 motivates learned query/document representations through Sentence-BERT and Dense Passage Retrieval: document encoding can happen before queries arrive.
- BGE-M3 dense vectors and E5-base are specific evaluated channels. Conclusions cannot automatically extend to BGE-M3's other modes or other E5 checkpoints.
- Single-vector encoding compresses each document before seeing the query. ColBERT's token-level late interaction identifies an alternative design, without proving it fixes this project's failures.
- The unresolved questions are whether neural rankings improve the lexical reference and whether their disagreements add useful evidence after fusion. Standalone rankings cannot establish incremental hybrid value.

### Printed page 9 — PDF page 18

- Section 2.4 distinguishes reciprocal rank fusion, which combines positions, from weighted score fusion, which retains normalized score-distance information. Candidate policies and tuning influence their behavior.
- Complementarity motivates combining lexical and semantic evidence. A second dense channel must add information beyond the existing hybrid, rather than merely perform well by itself.
- Comparing BM25+BGE-M3 with a weight search that also permits E5-base requires unseen-data evaluation. Zero-weight boundaries allow the larger search to ignore E5, so a development gain may reflect search flexibility rather than stable new evidence.
- RQ1 and RQ2 concern the implemented score fusion; other fusion, normalization, and candidate-depth methods need matched experiments before comparison.
- Section 2.5 distinguishes legal language exposure from supervised retrieval adaptation. The intervention is contrastive dense training on query–article groups. Hard-negative sources, refresh policies, corpus, and filtering determine what distinctions the encoder learns; excluding known positives does not prove all remaining articles legally irrelevant.

### Printed page 10 — PDF page 19

- Section 2.5 explains why encoder training loss and dense-only effectiveness do not establish hybrid improvement: adaptation can change overlap with BM25. Locked weights test component replacement; permissible development retuning tests an additional system adjustment. Final-test outcomes must not select weights.
- RQ3 concerns completed fixed-weight hybrid experiments. Study B reports dense-only and locked-weight outcomes, with its different recipe and previously observed test stated explicitly in Section 5.6.3.
- Section 2.6 separates evidence from task definitions, legal benchmark taxonomies, generalization benchmarks, model papers, and optimization studies.
- Table 2.1 begins with ALQAC, Goebel et al./COLIEE, and the vanilla BM25 case-retrieval study. It records each source's task/language scope, intervention, evaluation emphasis, and limits of relevance to this thesis.

### Printed page 11 — PDF page 20

- Table 2.1 continues with BEIR, BGE-M3, multilingual E5, lexical–semantic fusion, and hard-negative research. Each supports a methodological choice while retaining its own scope and limitations.
- The synthesis deliberately avoids comparing incompatible leaderboard values such as case-retrieval F-measure and article-level NDCG. Shared task definitions, relevance sets, and metrics are necessary for numerical comparison.
- BEIR motivates separating development gains from transfer: BM25 is robust, reranking and late interaction can provide strong effectiveness with additional cost, and evaluated dense/sparse methods show generalization limits. Dataset-specific results and selection status should remain visible.
- The page begins the metric discussion: normalized discounted cumulative gain compares observed positional gain with an ideal ranking under the same judgments.

### Printed page 12 — PDF page 21

- Section 2.6 completes the NDCG discussion: binary article labels measure ordering of known relevant evidence, not degrees of legal importance.
- A hit metric asks whether any positive article was found; recall measures the fraction of all labeled positives recovered. They coincide for single-positive queries but can differ for multi-positive queries, so metric names must be checked against evaluator code.
- Missing labeled articles distinguish ranking conditional on corpus coverage from the combined effect of corpus coverage and ranking. Extraction and identifier mapping can change target availability.
- Cross-encoders and ColBERT are relevant alternatives to compressed single-vector representations. Their effectiveness on this project would require fixed candidates, comparable judgments, and computation measurements.
- Section 2.7 positions the contribution as empirical evaluation of established components. It separates initial hybrid gains from extra-channel gains, and dense encoder gains from hybrid gains.

### Printed page 13 — PDF page 22

- Section 2.7 completes the distinction between development-selected performance and unseen-data or cross-dataset evidence. A dataset used for selection cannot simultaneously supply unselected generalization evidence.
- Clean/parsed text, article boundaries, and target mappings are experimental conditions. Differences should not automatically be attributed to parser quality when coverage, content, and normalization populations also change.
- Complementarity, multilingual representation, and difficult negatives are hypotheses whose success must be tested separately. Limited E5 value, dense-only improvement without hybrid benefit, and failure to transfer are valid, interpretable findings under controlled comparisons.
- Chapter 4 supplies concrete pipeline definitions; incomplete fine-tuning evaluations must remain explicitly incomplete.
- Section 2.8 restates the three progressively stricter comparisons and leads into Chapter 3's formal definitions.

## Section-by-section summary

### 2.1 Legal Retrieval and Evidence

Legal retrieval must define both the information need and the unit ranked. ALQAC provides the relevant question-to-article task, whereas COLIEE illustrates different legal retrieval and entailment tasks. Evidential relevance requires more than topical similarity. Article/passage boundaries affect context and must align with judgment identifiers. Vietnamese segmentation affects lexical statistics, while dense preprocessing follows the encoder's contract. Retrieval metrics evaluate ranked evidence independently of a generator's answer quality.

### 2.2 Lexical Retrieval as a Serious Reference

BM25 has established probabilistic foundations and credible legal retrieval results, making it an essential comparator. These results do not predict Vietnamese article performance. The thesis therefore fixes BM25 and specifies its preprocessing and boundaries so that additional neural value can be measured fairly; untested lexical modifications are not presented as contributions.

### 2.3 Multilingual Neural Retrieval

Separate query/document encoding allows advance indexing but compresses documents before the query is known. The chapter motivates the specifically deployed BGE-M3 dense and E5-base channels, with model-family and mode boundaries kept explicit. ColBERT represents a token-level alternative. Local experiments must determine both standalone effectiveness and usefulness inside a hybrid.

### 2.4 Lexical–Semantic and Multi-Retriever Fusion

Rank fusion and normalized weighted score fusion use different information. Complementary lexical and semantic evidence may improve a ranking, but an additional dense channel has to improve an already combined system. Since the enlarged weight space includes zero weights, selection gains need unseen-data confirmation. RQ1/RQ2 are restricted to the implemented score-fusion comparison.

### 2.5 Legal-Domain Adaptation and Hard Negatives

Supervised contrastive retrieval adaptation differs from general legal language modeling. Hard-negative mining is part of the intervention, and unjudged competitors may still contain relevant legal evidence. Adaptation can alter dense/lexical complementarity, so encoder gains and hybrid gains must be evaluated separately. RQ3 uses completed fixed-weight experiments; Study B's recipe and test-selection history are explicit limits on interpretation.

### 2.6 Benchmarks and Evaluation Design

Sources serve distinct roles and cannot supply interchangeable scores. Generalization must be reported separately from development selection. Binary NDCG, hit rate, recall, and corpus answerability estimate different aspects of effectiveness. Candidate coverage and target mappings matter before ranking is evaluated. Alternative architectures require matched experimental and computational comparisons.

**Table 2.1 — Prior research grouped by task, intervention, and evaluation role:**

| Source | Main idea and boundary |
| --- | --- |
| ALQAC Organizers | Direct Vietnamese question-to-statute-article task motivation; local corpus provenance still needs documentation. |
| Goebel et al. | COLIEE distinguishes Canadian case and Japanese statute retrieval/entailment; jurisdiction and retrieval unit differ. |
| Rosa et al. | Competitive vanilla BM25 case retrieval supports a serious lexical baseline without proving Vietnamese article performance. |
| Thakur et al. | BEIR's heterogeneous zero-shot comparison motivates separating generalization from development gains. |
| Chen et al. | BGE-M3 establishes multilingual, multiple-granularity capabilities; dense-only deployment uses a restricted configuration. |
| Wang et al. | Multilingual E5 supplies model/training context; base, large, and instruction-tuned variants remain distinct. |
| Bruch et al. | Convex combination and reciprocal rank fusion motivate explicit tuning/specification; local gains require local evaluation. |
| Zhan et al. | Hard-negative training motivates careful competitor construction; legal label validity is a separate concern. |

### 2.7 Research Gap and Positioning

The contribution is controlled empirical knowledge about established retrieval components in Vietnamese legal collections. The study separately tests fusion, an additional dense channel, and adapted dense retrieval within a hybrid. Selection history, representation, article boundaries, mappings, coverage, and normalization affect interpretation. Negative findings remain useful when those conditions are sufficiently controlled. Concrete pipeline specification belongs to Chapter 4, and unfinished evaluations are not converted into results.

### 2.8 Chapter Summary

Prior work motivates the three comparisons without determining their local outcome: fusion against BM25, another dense channel against an existing hybrid, and development-selected adaptation against the hybrid on unseen data. Chapter 3 provides the formal concepts.

## Coverage check

- Source: `chapters/chapter_2.tex`; page mapping: `main.pdf` PDF pages 15–22, printed pages 6–13.
- Covered all 8 numbered sections (2.1–2.8); the source contains no subsections or subsubsections.
- Covered all 8 pages and Table 2.1, including all 8 source rows. The chapter contains no figures or displayed equations.
- Summaries preserve the source's distinctions between motivating literature, implemented comparisons, and untested alternatives.
