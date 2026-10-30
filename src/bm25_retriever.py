"""BM25 lexical retriever."""
import time
from typing import List, Tuple
import numpy as np
from rank_bm25 import BM25Okapi


class BM25Retriever:
    def __init__(self, corpus: List[dict]):
        self.corpus = corpus
        self.ids = [c["id"] for c in corpus]
        self.texts = [c["text"] for c in corpus]
        self.tokenized = [t.lower().split() for t in self.texts]
        self.bm25 = BM25Okapi(self.tokenized)

    def search(self, query: str, k: int = 10) -> Tuple[List[str], float]:
        start = time.perf_counter()
        toks = query.lower().split()
        scores = self.bm25.get_scores(toks)
        order = np.argsort(scores)[::-1][:k]
        ids = [self.ids[i] for i in order]
        latency_ms = (time.perf_counter() - start) * 1000.0
        return ids, latency_ms
