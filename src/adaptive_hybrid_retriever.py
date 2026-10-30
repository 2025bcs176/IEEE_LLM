"""Adaptive hybrid retriever: BM25-first, dense+RRF only when BM25 confidence is low."""
import time
from typing import List, Tuple
from collections import defaultdict
import numpy as np


class AdaptiveHybridRetriever:
    def __init__(self, bm25, dense, rrf_k: int = 60, margin_threshold: float = 6.0):
        self.bm25 = bm25
        self.dense = dense
        self.rrf_k = rrf_k
        self.margin_threshold = margin_threshold

    def _bm25_margin(self, query: str) -> float:
        scores = self.bm25.bm25.get_scores(query.lower().split())
        order = np.argsort(scores)[::-1]
        return float(scores[order[0]] - scores[order[1]])

    def search(self, query: str, k: int = 10) -> Tuple[List[str], float]:
        start = time.perf_counter()
        bm25_ids, bm25_lat = self.bm25.search(query, k=max(k, 20))

        if self._bm25_margin(query) >= self.margin_threshold:
            latency_ms = (time.perf_counter() - start) * 1000.0
            return bm25_ids[:k], latency_ms

        dense_ids, dense_lat = self.dense.search(query, k=max(k, 20))
        scores = defaultdict(float)
        for rank, did in enumerate(bm25_ids, start=1):
            scores[did] += 1.0 / (self.rrf_k + rank)
        for rank, did in enumerate(dense_ids, start=1):
            scores[did] += 1.0 / (self.rrf_k + rank)
        order = sorted(scores.keys(), key=lambda d: scores[d], reverse=True)[:k]
        latency_ms = (time.perf_counter() - start) * 1000.0
        return order, latency_ms
