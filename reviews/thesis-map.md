# Thesis-Level Map

## Scope and Source of Truth

**Thesis:** *Hybrid Retrieval and Legal-Domain Adaptation for Vietnamese Legal Information Retrieval*.

This map describes the current working-tree LaTeX manuscript in `TuanTheosis`, not an earlier proposal or a reconstructed manuscript. The README explicitly identifies the revised LaTeX as authoritative and the Markdown in `source/thesisproposalTuan.md` as preserved historical material (`README.md:1–3,29–33`). Assembly is defined by `main.tex:107–134`.

**Read in full:** `main.tex`; acknowledgements/declaration; abstract/abbreviations; Chapters 1–6; the research-overview figure; references; and Appendix A–G source files. The appendices were read as supporting material, but **are not included in the current document assembly**: all appendix inputs and `\appendix` are commented out (`main.tex:127–134`). `README.md` and `QA.md` were also consulted for provenance/context; neither is thesis evidence. The existing PDF was not used as authority or rebuilt, so this is a complete source-level map, not a PDF-layout review.

No `THESIS.md`, chapter contracts, or chapter-validation reports were found in this workspace. This is a mapping exercise, not a declaration that chapters have passed validation or that the thesis is defense-ready. Reported experiment results are mapped from the manuscript; training, score caches, and statistical analyses were not rerun. The experiment directories referenced by the appendices are not supplied in this workspace or its immediate parent.

All evidence references below use project-relative `path:line` ranges. Source files were not edited.

## 1. Research Problem

**Operational problem:** Given a Vietnamese legal question, we want to run a benchmark combining lexical retrieval using BM25 model + BGE for vector model and also combine multilingual-E5-base to find in what condition does these combination of model contribute. we want to know if BM25 model + BGE for vector model or BM25 model + BGE for vector model+ multilingual-E5-base perform better than BM25 as base reference. Everyday question phrasing, similar provisions with legally decisive differences, and unavailable/misidentified targets make this difficult (`chapters/chapter_1.tex:5–11`; `chapters/chapter_4.tex:5–19`).

**Research problem:** Determine which benefits are actually supported when lexical retrieval, semantic retrieval, additional dense channels, and legal-domain adaptation are compared under fixed corpora, recorded judgments, and explicit selection boundaries. Improvement over BM25, improvement over an existing hybrid, and improvement after fine-tuning are different claims (`chapters/chapter_1.tex:9–19`).

**Scope boundary:** Retrieval effectiveness and dataset generation, not generated-answer correctness, legal advice, temporal legal validity, multilingual evaluation, cross-jurisdiction generalization, or deployment performance (`chapters/chapter_1.tex:53–59`). Corpus availability is part of end-to-end retrieval effectiveness; ranking cannot recover absent targets.

## 2. Research Gap

The gap is **local benchmark and methodological**, not the absence of Vietnamese legal benchmarks or the invention of hybrid retrieval:

1. What do BM25, BGE-M3 dense, E5-base dense, and their hybrids achieve on these Vietnamese legal collections Zalo, ALQAC, BCA under comparable evaluation?
2. Does E5 contribute beyond a strong BM25+BGE-M3 system rather than merely beyond BM25 on selected dataset Zalo, ALQAC, BCA?
3. Do fine-tuning gains on testing apply to out of bound validation?

The introduction states the gap directly (`chapters/chapter_1.tex:13–19`); the literature review separates component addition, adaptation, and selection/generalization (`chapters/chapter_2.tex:103–117`). Established algorithms are explicitly not claimed as new (`chapters/chapter_4.tex:1–3`). The thesis does not prove a comprehensive absence of all prior comparable studies; its safest novelty claim remains this particular controlled comparison and BCA construction/evaluation.

## 3. Research Questions and Traceability

| RQ | Introduced | Operationalized | Experiment/result answering it | Discussion and conclusion | Boundary |
|---|---|---|---|---|---|
| **RQ1:** What improvement over lexical retrieval is supported by lexical–semantic hybrids? | `chapters/chapter_1.tex:33–35` | Common corpora, normalized component scores, grouped fusion selection: `chapters/chapter_4.tex:21–25,199–259` | Standalone/hybrid OOF table and BM25 comparisons: `chapters/chapter_5.tex:42–122`; BCA views: `160–211` | `chapters/chapter_5.tex:490`; `chapters/chapter_6.tex:7–9,29` | Positive observed differences over the **fixed** BM25 baseline; BCA combined evidence is descriptive, not equivalent to an independent multi-component confirmation. |
| **RQ2:** Does adding pretrained multilingual-E5-base improve BM25+BGE-M3 across collections/conditions? | `chapters/chapter_1.tex:37–39` | Nested two-/three-way grids and unseen-data comparison: `chapters/chapter_4.tex:199–217` | Condition-specific incremental results: `chapters/chapter_5.tex:124–158`; BCA component-sensitive findings: `207` | `chapters/chapter_5.tex:490`; `chapters/chapter_6.tex:11–13,31` | Clearest gain on Zalo parsed-with-fallback; no universal three-way advantage. Larger selection search and query dependence remain relevant. |
| **RQ3:** Do BGE-M3 fine-tuning improve BM25+BGE-M3 model evaluation metric | `chapters/chapter_1.tex:41–43` | Study A training/selection/evaluation and Study B different objective: `chapters/chapter_4.tex:261–373` | Development, corrected Study A hybrid results, Study B dense and locked-weight hybrid results: `chapters/chapter_5.tex:223–486` | `chapters/chapter_5.tex:480–490`; `chapters/chapter_6.tex:15–17,33–41` | Post-hoc evaluation, previous test observation, different recipes, and locked weights. No causal A-versus-B ablation or established cross-collection adaptation. |

**Traceability judgment:** All three RQs persist through results and conclusion. BCA construction is an objective/contribution rather than a separately numbered RQ (`chapters/chapter_1.tex:25–27,51`). This is not necessarily a defect, but the author should decide whether this explicit supporting branch is sufficient or whether an additional dataset/evaluation RQ is warranted.

### Evaluation-condition map

| Branch | Queries | Corpus units | Selection/evaluation identity |
|---|---:|---:|---|
| ALQAC A, clean | 811 | 3,363 | Grouped baseline OOF; shares queries with B |
| ALQAC B, parsed | 811 | 3,381 | Grouped baseline OOF; changed corpus construction |
| Zalo A, clean | 3,196 | 61,425 | Grouped baseline OOF; shares queries with B |
| Zalo B, parsed-with-fallback | 3,196 | 61,425 | Grouped baseline OOF; not a pure parsing ablation |
| BCA canonical | 546 | 14,789 | Giant component plus smaller-component OOF; combined descriptive view |
| Study A adaptation | 640 evaluation queries | Zalo parsed fold-0 corpus | Pilot selection on fold 1; final training on folds 1–4; corrected post-hoc fold 0 |
| Study B adaptation | 640 official queries | Separate fixed-corpus benchmark | Dense-oriented selection; three seeds; pretrained-locked hybrid comparisons |

Evidence: `chapters/chapter_4.tex:64–95,334,365–373`; `chapters/chapter_5.tex:288–290,368–390`. Query equality between Study A and Study B is **not established by equal counts**. Appendix A explicitly warns that a shared “Zalo test” label is insufficient to identify the population (`appendices/appendix_a.tex:6–8`). Clean/parsed populations, seeds, and answerable-only views must not be summed as independent evidence.

## 4. Claimed Contributions and Evidence

| Contribution | Establishing chapters | Supporting evidence | Limits |
|---|---|---|---|
| **C1. Controlled empirical evaluation of Vietnamese lexical–semantic retrieval**, separating BM25 gains from incremental E5 value | Introduction claim: `chapters/chapter_1.tex:47`; method: Chapter 4; evidence: Chapter 5; synthesis: `chapters/chapter_6.tex:21` | ALQAC/Zalo standalone and hybrid tables, condition-specific E5 comparisons, BCA descriptive/component views (`chapters/chapter_5.tex:65–158,177–211`) | No new ranking algorithm; fixed lexical tokenizer/reference; no universal optimal hybrid, isolated parser effect, or deployment claim. |
| **C2. Dense- versus whole-hybrid adaptation evaluation**, preserving negative/non-transfer findings | `chapters/chapter_1.tex:49`; `chapters/chapter_4.tex:261–373`; `chapters/chapter_6.tex:23` | Study A mean hybrid changes −0.0520/−0.0249; Study B dense gain +0.0189 and locked-weight hybrid changes −0.0043/+0.0009 (`chapters/chapter_5.tex:304–357,382–417`) | Prior test exposure; Study A intervals span zero; separate recipes; no retuned-hybrid results; no identified causal mechanism. |
| **C3. BCA dataset and evaluation contribution**, including coverage and dependence analysis | `chapters/chapter_1.tex:51`; construction: `chapters/chapter_4.tex:95–159`; conclusion: `chapters/chapter_6.tex:25` | 652 source records; 546 retained queries; 440 with represented targets, 106 without, including 229 partial cases; giant component 484 queries and 49 smaller components with 62 queries (`chapters/chapter_5.tex:207–211`) | Answer citations are heuristic/non-exhaustive relevance evidence; dataset release, licensing, versioning, and independent annotation audit are not demonstrated here. |

The distinction between **empirical novelty** and **algorithmic novelty** is coherent across Chapters 1, 2, 4, and 6. Contribution C3 requires an author decision about what tangible dataset package readers will receive.

## 5. Role of Each Chapter

| Part | Role in the research argument | Required output to later parts |
|---|---|---|
| Abstract | Compress problem, comparisons, principal findings, and post-hoc boundary | Claims must match Chapter 5 and retain system-level distinctions (`chapters/frontmatter.tex:3–9`). |
| **1. Introduction** | Establish problem, local gap, objectives, RQs, contributions, scope | A bounded contract: retrieval only; three different comparison questions; BCA supporting contribution. |
| **2. Literature Review** | Justify serious lexical comparison, semantic channels, incremental fusion, contrastive adaptation, and careful evaluation | Motivation and boundaries, not transferred numerical evidence; novelty positioned as controlled empirical investigation. |
| **3. Theoretical Background** | Define scoring, normalization, contrastive objectives, target matching, metrics, and grouping | Shared mathematical vocabulary and estimands for implementation and interpretation. |
| **4. Proposed Methodology** | Instantiate corpora, BCA construction, exhaustive scoring, weight selection, grouped evaluation, and two adaptation studies | Reproducible comparison identities and selection boundaries sufficient to interpret Chapter 5. |
| **5. Experimental Evaluation** | Answer RQs, diagnose BCA coverage/dependence, distinguish development from test observations and dense from hybrid gains | Numerical evidence, uncertainty, query-level transitions, limits on causality. This is the evidential center. |
| **6. Conclusion and Future Work** | Integrate findings/contributions and validity limits; propose fresh evaluation, corpus repair, and downstream RAG work | Conclusions no stronger than measured retrieval evidence; prospective work remains unperformed. |
| References | Identify the literature supporting motivation and definitions | Literature provenance, not a substitute for local experiment artifacts. |

### Supporting appendix roles (currently excluded from assembly)

- **A — Dataset Details:** ordered identity hashes, cohort distinctions, coverage/annotation boundaries.
- **B — Full Hyperparameter Search Space:** fold-specific weights, tie selection, adaptation-screening provenance.
- **C — Complete Verified Metric Tables:** baseline extra cutoffs, Study A seed endpoints, seed variability.
- **D — Fine-Tuning Configurations:** Study A executed configuration and distinction from Study B specifications.
- **E — Failure-Case Examples:** purposive examples of E5-related recovered/lost/persistent top-ten outcomes, not expert legal-error prevalence.
- **F — Reproducibility Instructions:** external research-repository artifacts, reaggregation versus retraining, historical assembly instructions.
- **G — Additional Result Maps:** categorical E5 and Study A development/evaluation outcome diagrams.

## 6. Major Argument Flow

```text
Vietnamese questions require specific supporting legal provisions
    ↓
Lexical mismatch, semantic near-matches, and missing targets complicate retrieval
    ↓
Local gap: component promises do not establish complete-system effectiveness
    ↓
RQ1: lexical–semantic hybrid versus fixed BM25
RQ2: additional E5 versus existing BM25+BGE-M3 hybrid
RQ3: development-selected adaptation versus matched pretrained system
    ↓
Fixed corpus identities + explicit target matching + grouped selection
    ↓
ALQAC/Zalo representation comparisons ── BCA coverage/dependence branch
    ↓
Study A: development gains → corrected post-hoc hybrid regressions
Study B: dense gains → little/no practically sufficient locked-weight hybrid gain
    ↓
System-level gains cannot be inferred from component count or dense-only scores
    ↓
Bounded conclusions + untouched evaluation / corpus repair / RAG evaluation
```

Evidence: `chapters/chapter_1.tex:11–19`; `chapters/chapter_5.tex:480–494`; `chapters/chapter_6.tex:43–53`.

**Strong links:** RQ2 has the correct incremental comparator; RQ3 directly evaluates complete hybrids; coverage is separated from rankability; negative outcomes remain central.

**Weak links:** Implementation specificity is incomplete; Study B cohort/recipe details are thinner than Study A; the epoch-selection rule is not transparent; BCA component-aware inference is asserted without its numerical inferential summary in Chapter 5; appendix evidence promised by the narrative is excluded from assembly. Failure diagnosis motivates adaptation but does not establish the cause adaptation would repair.

## 7. Dependencies Between Chapters

| Dependency | Why it matters | Failure if unresolved |
|---|---|---|
| Chapter 1 → Chapters 4–5 | Each RQ must retain its comparator and system level | BM25 improvement could be substituted for E5's incremental value, or dense gain for hybrid gain. |
| Chapter 2 → Chapters 3–4 | Literature motivates explicit units, preprocessing, fusion, and supervision | Generic model-family claims could mask the particular dense mode/checkpoint evaluated. |
| Chapter 3 → Chapters 4–5 | Metrics require identical targets, matching rules, cutoff, and denominator | Hit could be mistaken for target recall; wildcard credit or absent targets could alter interpretation. |
| Chapter 4 corpus construction → Chapter 5 A/B interpretation | ALQAC changes article universe; Zalo retains fallback | An association could be misreported as a causal parsing effect. |
| Chapter 4 grouping → Chapter 5 inference | Law components define separation and dependence | Query-level p-values could be treated as fully independent legal evidence. |
| Chapter 4 adaptation boundaries → Chapter 5 Study A/B → Chapter 6 | Different recipes, cohort identities, locked weights, and prior observation determine claim scope | A/B could be presented as a controlled causal ablation or prospective confirmation. |
| BCA construction in Chapter 4 → coverage/results in Chapter 5 | Answer-derived targets and mapping define what can score | Missing evidence could be blamed on model weakness; answerable-only scores could conceal partial availability. |
| Chapter 5 → Abstract/Chapter 6 | Principal claims must inherit all material caveats | Observed regressions could become established population-level harm or universal fine-tuning failure. |
| Appendices A–G → Chapters 4–5 and examiner verification | Weights/configurations/examples support traceability and reproducibility | The assembled thesis currently omits promised evidence. |

## 8. Potential Contradictions and Evidence Gaps

These are mapping findings, not instructions to edit sources. “Potential” means an author clarification or underlying artifact may resolve the issue.

| ID | Status / priority | Evidence and issue | Required resolution |
|---|---|---|---|
| **M1** | Confirmed assembly inconsistency / high | README claims enabled appendices (`README.md:13,27`), and Chapters 1/5 refer to them (`chapters/chapter_1.tex:65`; `chapters/chapter_5.tex:219`), but `main.tex:127–134` comments out every appendix. | Decide whether appendices belong in the submission or a separately accessible supplement. |
| **M2** | Unclear selection rationale / high | Selected Study A recipe uses two epochs and is called the best-supported restricted point (`chapters/chapter_5.tex:250–262`). At learning rate 2e-5, the three-way pilot scores 0.7923 at epoch 2 and 0.7958 at epoch 3; two-way scores favor epoch 2. The combined decision rule is not stated. Appendix B distinguishes separate pilot/batch evidence but does not fully explain the epoch criterion (`appendices/appendix_b.tex:58–62`). | Specify the predeclared primary selection objective, tradeoff/guardrail, and decisive artifact. This is not proof that the selected epoch is wrong. |
| **M3** | Cohort identity unresolved / high | Study A uses parsed Zalo fold 0; Study B uses 640 “official” queries and a separate fixed-corpus recipe (`chapters/chapter_5.tex:288–290,368–390`). Baseline hybrid scores differ between studies (`304,327,409–410`), while Appendix A warns that names/counts are insufficient (`appendices/appendix_a.tex:6`). | State query-ID overlap, corpus/text identities, eligibility, and weights for each study. Do not assume equal counts imply identical test queries or that differing scores are a numerical error. |
| **M4** | Insufficient inference detail / important | Chapter 5 asserts no established BCA component-aware E5 advantage (`chapters/chapter_5.tex:207`) but supplies no component-aware effect/interval/test table. Query-level tests are supplied for ALQAC/Zalo and cluster statistics for Study A (`154,349–357`). | Identify BCA estimator, resampling unit, interval/test, and effective independent components; decide whether additional cluster-sensitive baseline analysis is needed. |
| **M5** | Implementation promise not fulfilled / important | Chapter 2 promises tokenizer and implementation in Section 4.4.1 (`chapters/chapter_2.tex:25`); Chapter 3 promises BM25 implementation identity (`chapters/chapter_3.tex:23`). Chapter 4 gives whitespace preprocessing but no subsection 4.4.1 or concrete BM25 package/version, IDF convention, or k1/b (`chapters/chapter_4.tex:161–197`). | Establish actual implementation settings and correct the reference in a later authorized revision. |
| **M6** | Reproduction portability gap / high | Appendix F explicitly describes an external research repository, not this workspace (`appendices/appendix_f.tex:3–17`); linked experiment directories are unavailable here. Its assembly text says the manuscript is one Markdown file with Mermaid (`51–53`), unlike the revised LaTeX assembly. | Separate historical research reproduction from current document-build instructions; identify an accessible immutable evidence bundle. |
| **M7** | Under-specified Study B / important | Chapter 4 names a larger true contrastive batch requirement; Appendix D states minimum/preference rather than actual executed batch (`chapters/chapter_4.tex:365–373`; `appendices/appendix_d.tex:43–47`). Dense/hybrid results are nevertheless completed. | Provide actual training population, executed batch, optimization settings, selected checkpoint and fusion weights, not just requirements. |
| **M8** | Practical threshold provenance / important | +0.01 NDCG@10 determines practical interpretation and “Fail” gates (`chapters/chapter_5.tex:357,407–415`), without a clear rationale or timing of threshold choice. | State origin, selection timing, and meaning of the gate. Failure to demonstrate a gain is not proof of equivalence or impossibility of a useful retuned hybrid. |
| **M9** | Negative-label safeguard gap / important | Study A filters explicit known positives, but its loss treats all non-selected batch passages as negatives (`chapters/chapter_4.tex:267,292–297`). Chapter 3 warns about known positives becoming in-batch negatives (`chapters/chapter_3.tex:111–113`). | Clarify cross-query/A–B duplicate-positive masking in the executed Study A implementation. Treat false negatives as an unquantified threat unless audited. |

### What is consistent

- The 20 ALQAC/Zalo baseline method rows in Chapter 5 agree with Appendix C for NDCG@10, MRR@10, MAP@10, and Hit@10; this was checked programmatically against the displayed source values.
- BCA giant/small query totals and answerable totals reconcile; Study A and Study B query-change partitions each reconcile to their stated evaluation population. These checks establish internal arithmetic only, not experiment validity.
- Abstract, Introduction contributions, Chapter 5, and Conclusion agree on the principal observed directions: hybrid-over-BM25 gains; condition-dependent E5 value; Study A hybrid regression; Study B dense improvement without practically sufficient locked-weight hybrid improvement.
- The conclusion explicitly retains both studies' previous-test-observation caveats (`chapters/chapter_6.tex:39`). The abstract explicitly retains Study A's caveat but does not comparably qualify Study B's previously observed benchmark (`chapters/frontmatter.tex:9`). This is a qualification imbalance, not contradictory result values.

## 9. Terminology Inconsistencies and Ambiguities

| Term pair / usage | Evidence | Mapping rule / author decision |
|---|---|---|
| **Parsed** versus **parsed-with-fallback** | Short-form “parsed Zalo” occurs in summaries; the construction is qualified in `chapters/chapter_4.tex:88–93` and `chapters/chapter_5.tex:156`. | Prefer “Zalo parsed-with-fallback” wherever attributing representation effects. |
| **Unseen data** versus **previously unobserved test** | `chapters/frontmatter.tex:9`; `chapters/chapter_4.tex:334`; `chapters/chapter_6.tex:39` | “Unseen during training and selection” does not mean no prior test observation. Preserve the qualifier for post-hoc studies. |
| **Article-level retrieval** versus **law-level target** | `chapters/chapter_1.tex:5`; `chapters/chapter_3.tex:7–9,123–129` | Retrieval units are articles, but target matching can include whole-law wildcards. Clarify target-level credit and mixed-target matching order. |
| **Answerable** versus **fully covered** | `chapters/chapter_5.tex:209`; `appendices/appendix_a.tex:38` | Answerable means at least one represented target; partial cases remain included. It does not establish complete legal-answer sufficiency. |
| **BGE**, **BGE-M3**, **BGE-M3 dense** | BCA/appendix tables shorten names (`chapters/chapter_5.tex:179–202`; `appendices/appendix_c.tex:21–37`). | Define BGE as shorthand for the evaluated BGE-M3 dense configuration; distinguish pretrained/adapted state. |
| **BCA / MPS** | `chapters/frontmatter.tex:38` versus BCA throughout results | Use BCA as the canonical dataset label; MPS is the institutional English translation, not a second dataset. |
| **Combined OOF** versus **combined descriptive view** | Table rows use “Combined OOF” (`chapters/chapter_5.tex:195–202`); prose uses descriptive (`207`). | Label the combined giant-holdout/small-OOF view explicitly; do not imply ordinary homogeneous independent CV. |
| **Recall** versus **Hit** | Baseline metrics distinguish them (`chapters/chapter_3.tex:131–149`); Study B separately reports Recall@100 (`chapters/chapter_5.tex:370–390`). | Preserve actual metric definitions and denominators across separate evaluators. Absence of baseline Recall@100 is not a contradiction with Study B reporting it. |
| **Specification** versus **verified execution** | Study A table says verified (`chapters/chapter_4.tex:304–330`); Study B appendix describes requested batch settings (`appendices/appendix_d.tex:45`). | Label actual executed values separately from requirements/preferences. |
| **Multilingual** versus **Vietnamese evaluation** | `chapters/chapter_1.tex:57`; `chapters/chapter_3.tex:43–53` | Multilingual denotes pretrained model capability, not cross-language validation in this thesis. |

## 10. Areas Requiring Author Decisions

| Decision | Priority | Specific question to settle |
|---|---|---|
| **D1 — Submission evidence boundary** | High | Will Appendix A–G be included, submitted separately, or deliberately excluded? How will every in-text appendix reference resolve? (M1) |
| **D2 — Canonical experiment identities** | High | What immutable manifests identify baseline OOF, Study A fold 0, and Study B official queries/corpora? What overlap is permitted and disclosed? (M3) |
| **D3 — Adaptation selection rule** | High | Why epoch 2 rather than epoch 3 when pilot objectives disagree? Which objective/guardrail selected the final candidate? (M2) |
| **D4 — Reproduction delivery** | High | Which code, data/rights documentation, scores, query IDs, model revisions, checkpoints, and statistics will examiners actually receive? Which remain unavailable? (M6–M7) |
| **D5 — Statistical claim level** | Important | Which claims are descriptive, query-paired, component-aware, or prospective? What is the numerical BCA inference and how is baseline dependence handled? (M4) |
| **D6 — Practical significance** | Important | What justifies +0.01 and the pass/fail gates? Will conclusions explicitly stay within locked-weight substitution rather than all possible hybrid adaptation? (M8) |
| **D7 — BCA contribution contract** | Important | Is BCA an introduced collection, an openly released dataset, or an independently validated benchmark? What citation/mapping audit and licensing support that designation? |
| **D8 — Relevance/negative semantics** | Important | How are whole-law/article mixed targets matched and known in-batch positives protected? What is audited versus unresolved? (M9) |
| **D9 — Objective/RQ alignment** | Optional structural choice | Keep BCA construction as a supporting objective/contribution, or add a distinct dataset/evaluation RQ? Existing RQs themselves do not disappear. |
| **D10 — Terminology and claim qualifiers** | Important | Standardize Zalo parsed-with-fallback, BGE dense/state labels, BCA combined-view names, and prior-observation qualifications—including Study B in the abstract. |

## Overall Map Assessment

The thesis already forms a coherent bounded research argument: **lexical–semantic hybridization improves the fixed baseline, but extra retrievers and dense-only adaptation do not automatically improve the complete system**. Its contributions are empirical comparison, system-level adaptation evidence, and BCA construction/evaluation—not algorithm invention.

The largest unresolved links concern evidence accessibility and assembly, experiment identities, transparent selection rules, implementation specificity, and inferential detail. Resolving those author decisions would strengthen traceability without requiring routine rewriting or replacing the thesis's substantive negative findings.
