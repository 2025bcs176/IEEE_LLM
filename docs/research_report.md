# Research Report: Dense Passage Retrieval for Domain-Specific QA

## 1. Literature Review (DPR)

DPR uses a dual-encoder architecture: two independent BERT networks (passage encoder, question encoder). Representations are the [CLS] token. Similarity is dot product enabling MIPS. Training is contrastive with in-batch and hard negatives. Compared to BM25 (lexical tf-idf), DPR captures semantics. Domain failure modes: OOV jargon; semantic drift.

## 2. Baseline Implementation

Repeatable pipeline: `src/bm25_retriever.py`, `src/dense_retriever.py`, `src/adaptive_hybrid_retriever.py`, `src/pipeline.py`. Same 40 chunks and 20 questions for all.

## 3. Evaluation

See `reports/aggregate_metrics.csv` and `reports/per_question_results.csv`.

| System | Recall@1 | Recall@5 | MRR@10 | Mean latency (ms) |
|---|---:|---:|---:|---:|
| BM25 | 0.95 | 1.00 | 0.9667 | 0.32 |
| Dense | 0.95 | 1.00 | 0.9750 | 10.29 |
| Hybrid (adaptive) | 0.95 | 1.00 | 0.9750 | 2.60 |

Model: sentence-transformers/multi-qa-MiniLM-L6-cos-v1 (384-dim, ~90 MB, Apache-2.0). BM25: rank-bm25 (MIT). Corpus: synthetic IFMIF-DONES passages (40). Hardware: CPU only, no GPU. Python 3.14. Repeatability: deterministic BM25; dense deterministic given cached model.

## 4. Error Analysis

See `docs/error_analysis.md` (5 cases).

## 5. Recommendation

See `docs/recommendation.md` (adaptive hybrid).

## Licenses
- sentence-transformers / multi-qa-MiniLM-L6-cos-v1: Apache-2.0
- rank-bm25: MIT
- Code in this repo: MIT (unless otherwise noted)
