# Minimum Evaluation Report

| System | Recall@1 | Recall@5 | MRR@10 | Mean Query Latency (ms) |
|---|---:|---:|---:|---:|
| BM25 | 0.9500 | 1.0000 | 0.9667 | 0.32 |
| Dense | 0.9500 | 1.0000 | 0.9750 | 10.29 |
| Hybrid | 0.9500 | 1.0000 | 0.9750 | 2.60 |

Hybrid = adaptive (BM25-first, dense+RRF fallback when BM25 margin < 6.0).
Model: multi-qa-MiniLM-L6-cos-v1 (dense encoder, 384-dim, ~90 MB).
Corpus: 40 IFMIF-DONES passages. Queries: 20 expert-style questions.