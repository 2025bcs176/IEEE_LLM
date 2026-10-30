"""Hybrid retriever combining BM25 and dense via Reciprocal Rank Fusion."""
import time
from typing import List, Tuple
import numpy as np


class HybridRetriever:
    def __init__(self, bm25, dense, rrf_k: int = 60):
        self.bm25 = bm25
        self.dense = dense
        self.rrf_k = rrf_k

    def search(self, query: str, k: int = 10) -> Tuple[List[str], float]:
        start = time.perf_counter()
        bm25_ids, _ = self.bm25.search(query, k=max(k, 20))
        dense_ids, _ = self.dense.search(query, k=max(k, 20))

        scores = {}
        for rank, did in enumerate(bm25_ids, start=1):
            scores[did] = scores.get(did, 0.0) + 1.0 / (self.rrf_k + rank)
        for rank, did in enumerate(dense_ids, start=1):
            scores[did] = scores.get(did, 0.0) + 1.0 / (self.rrf_k + rank)

        order = sorted(scores.keys(), key=lambda d: scores[d], reverse=True)[:k]
        latency_ms = (time.perf_counter() - start) * 1000.0
        return order, latency_ms
