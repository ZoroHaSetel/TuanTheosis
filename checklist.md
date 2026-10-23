# Checklist luận văn

Các tiêu đề theo thứ tự hiện tại trong `main.tex`, gồm cả mục con không đánh số. Abstract và các phụ lục đang được comment nên không đưa vào checklist. Không bao gồm caption của bảng và hình.

- [ ] HYBRID RETRIEVAL AND LEGAL-DOMAIN ADAPTATION FOR VIETNAMESE LEGAL INFORMATION RETRIEVAL
- [x] Acknowledgements and Declaration of Authorship
  - [x] Acknowledgements
  - [x] Declaration of Authorship
- [ ] Table of Contents
- [ ] List of Abbreviations
- [ ] List of Figures
- [ ] List of Tables

- [ ] 1 Introduction
  - [x] 1.1 Research Context
  - [x] 1.2 Research Gap and Approach
  - [x] 1.3 Research Objectives
  - [x] 1.4 Research Contributions
  - [x] 1.5 Scope of the Thesis
  - [x] 1.6 Thesis Organization

- [ ] 2 Literature Review
  - [ ] 2.1 Legal Retrieval and Evidence
  - [ ] 2.2 Lexical Retrieval and BM25
  - [ ] 2.3 Dense Retrieval and Multilingual Embeddings
  - [ ] 2.4 Hybrid Retrieval and Score Fusion
  - [ ] 2.5 Fine-Tuning for Legal Retrieval and Hard Negatives
  - [ ] 2.6 Research Gap and Positioning
  - [ ] 2.7 Chapter Summary

- [x] 3 Theoretical Background
  - [x] 3.1 Queries, Articles, and Relevance
    - [x] Example of an article-level record.
  - [ ] 3.2 Lexical Scoring with BM25
    - [ ] 3.2.1 Term Frequency and Inverse Document Frequency
    - [ ] 3.2.2 BM25
  - [ ] 3.3 Dense Retrieval and Vector Similarity
    - [ ] 3.3.1 BGE-M3
    - [ ] 3.3.2 Multilingual-E5-base
  - [ ] 3.4 Score Normalization and combination weights
    - [ ] 3.4.1 Hybrid Retrieval
    - [ ] 3.4.2 Score Normalization
    - [ ] 3.4.3 Weighted Score Fusion
      - [ ] Example of Score Fusion.
  - [ ] 3.5 Fine-Tuning and Negative Sampling
    - [ ] 3.5.1 Contrastive Learning
    - [ ] 3.5.2 Negative Sampling
    - [ ] 3.5.3 Hard-Negative Mining
  - [ ] 3.6 Target Matching and Evaluation Metrics
    - [x] Normalized discounted cumulative gain.
    - [x] Hit and recall.
    - [x] Mean reciprocal rank.
    - [x] Mean average precision.
  - [x] 3.7 Chapter Summary

- [ ] 4 Research Methodology
  - [ ] 4.1 Research Design and Retrieval Task
  - [ ] 4.2 Datasets and Corpus Preparation
    - [ ] 4.2.1 ALQAC and Zalo Datasets
    - [ ] 4.2.2 Article Extraction and Identifier Alignment
  - [ ] 4.3 BCA Dataset Construction
    - [ ] 4.3.1 Motivation and Research Value
    - [ ] 4.3.2 Data Sources and Record Selection
    - [ ] 4.3.3 Text Cleaning and Reference Extraction
      - [ ] Text cleaning and retriever inputs.
      - [ ] Legal reference extraction.
    - [ ] 4.3.4 Target Mapping and Corpus Coverage
    - [ ] 4.3.5 Example of Query and Target Construction
  - [ ] 4.4 Overview of Retrieval Experiments
  - [ ] 4.5 Retrieval Models and Implementation
    - [ ] 4.5.1 BM25
    - [ ] 4.5.2 BGE-M3 and Multilingual-E5-base
  - [ ] 4.6 Score Normalization and Fusion
  - [ ] 4.7 BGE-M3 Fine-Tuning
    - [ ] 4.7.1 Model Selection Based on Hybrid Retrieval
      - [ ] Training Data and Negative Examples
      - [ ] Training Objective and Configuration
      - [ ] Model Selection and Evaluation
    - [ ] 4.7.2 Model Selection Based on Standalone Dense Retrieval
      - [ ] Training Data and Configuration
      - [ ] Training Objective
      - [ ] Model Selection and Hybrid Evaluation
  - [ ] 4.8 Evaluation Design and Statistical Analysis
    - [ ] 4.8.1 Query Grouping and Data Splits
    - [ ] 4.8.2 Evaluation Metrics and Comparisons
    - [ ] 4.8.3 Statistical Analysis
  - [ ] 4.9 Experimental Environment and Reproducibility
  - [ ] 4.10 Research Ethics and Data Use
  - [ ] 4.11 Chapter Summary

- [ ] 5 Experiments and Evaluation
  - [ ] 5.1 Experimental Conditions
  - [ ] 5.2 Benchmark & Evaluation Procedure
  - [ ] 5.3 Experimental Results & Analysis
    - [ ] 5.3.1 BCA Dataset Results
      - [ ] Collected Records and Target Coverage
      - [ ] Observed Problems in Public-Service Questions
      - [ ] Retrieval Benchmark on BCA
    - [ ] 5.3.2 BGE-M3 Fine-Tuning Results
      - [ ] Selected Fine-Tuning Configurations
      - [ ] Fine-Tuning for Hybrid Retrieval
        - [ ] Selecting the settings.
      - [ ] Fine-Tuning for Standalone Dense Retrieval
        - [ ] Selecting the settings.
        - [ ] Standalone test results.
        - [ ] Hybrid test results.
      - [ ] Changes in Individual Queries
      - [ ] Summary of Fine-Tuning Results
    - [ ] 5.3.3 Overall Retrieval Benchmark
      - [ ] Benchmark Conditions
      - [ ] Lexical and Hybrid Retrieval
      - [ ] Contribution of E5
      - [ ] Highest-Scoring Retrieval Configurations
    - [ ] 5.3.4 Summary of Results

- [x] 6 Conclusion and Future Work
  - [x] 6.1 Summary of Findings
    - [x] 6.1.1 Hybrid Retrieval over the Lexical Baseline
    - [x] 6.1.2 Incremental Contribution of E5
    - [x] 6.1.3 Effect of Legal-Domain Adaptation
  - [x] 6.2 Research Contributions
  - [x] 6.3 Discussion and Limitations
  - [x] 6.4 Future Work
  - [x] 6.5 Closing Remarks

- [ ] References



- [ ] check logic
  - [ ] check lại data valid
  - [ ] check lại reference
  - [ ] check lại citation
  - [ ] check lại experiment finetunening
  - [ ] 