"""Evaluation pipeline: run retrievers over a query set."""
from typing import List, Dict
import numpy as np


def evaluate_retrieval(corpus, queries, bm25, dense, hybrid=None, k: int = 10):
    """Returns dict of system -> list of {query_id, top_k_ids, latency_ms}."""
    systems = {"BM25": bm25, "Dense": dense}
    if hybrid is not None:
        systems["Hybrid"] = hybrid

    out = {name: [] for name in systems}
    for q in queries:
        qid = q["id"]
        text = q["text"]
        for name, retr in systems.items():
            ids, lat = retr.search(text, k=k)
            out[name].append({"query_id": qid, "top_k_ids": ids, "latency_ms": lat})
    return out
