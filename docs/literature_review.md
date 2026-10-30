# Deliverable 1: Dense Passage Retrieval (DPR) Literature Review

## Architecture
DPR uses a **dual-encoder** architecture: two independent BERT networks.
- **Passage encoder** maps text passages into a continuous vector space.
- **Question encoder** maps user queries into the same vector space.

Representations for both passages and questions are taken from the **[CLS] token** of their respective encoders.

## Scoring
Similarity between a question and a passage is the **dot product** of their dense vectors. This enables efficient **maximum inner-product search (MIPS)** over millions of offline-indexed passages.

## Training
DPR uses **contrastive training**: minimize distance between a question and its relevant passage, maximize distance from irrelevant passages.

Negative sampling strategies:
- **In-batch negatives**: reuse positive passages of other questions in the same batch as negatives, increasing efficiency without extra compute.
- **Hard negatives**: passages that rank highly in sparse retrieval (e.g., BM25) but do not contain the answer, forcing semantic relevance over lexical overlap.

## Comparison with BM25
- **DPR**: captures deep semantic relationships via dense vectors.
- **BM25**: relies on exact lexical matching, tf-idf weighting, and document-length normalization.

## Domain-specific failure modes
1. **Out-of-Vocabulary (OOV) Jargon**: pretrained dense encoders may lack embeddings for highly specific technical acronyms or part numbers, missing nuance that BM25's exact keyword matching captures.
2. **Semantic Drift in Technical Contexts**: a general dense encoder may overweight general semantic overlap, retrieving topically relevant but non-answering passages, whereas BM25 stays tethered to query terminology.
