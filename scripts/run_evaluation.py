#!/usr/bin/env python3
"""Run BM25 / Dense / Adaptive-Hybrid retrieval evaluation."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.corpus import CORPUS, QUERIES, QRELS
from src.bm25_retriever import BM25Retriever
from src.dense_retriever import DenseRetriever
from src.adaptive_hybrid_retriever import AdaptiveHybridRetriever
from src.pipeline import evaluate_retrieval
from src.metrics import calculate_retrieval_metrics, per_query_ranks

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    bm25 = BM25Retriever(CORPUS)
    dense = DenseRetriever(CORPUS)
    hybrid = AdaptiveHybridRetriever(bm25, dense, margin_threshold=6.0)

    results = evaluate_retrieval(CORPUS, QUERIES, bm25, dense, hybrid, k=10)

    gt_ids = [QRELS[q["id"]] for q in QUERIES]

    report = {}
    for system, rows in results.items():
        retrieved = [r["top_k_ids"] for r in rows]
        m = calculate_retrieval_metrics(retrieved, gt_ids)
        latencies = [r["latency_ms"] for r in rows]
        m["MeanLatencyMs"] = round(sum(latencies) / len(latencies), 3)
        m["Ranks"] = per_query_ranks(retrieved, gt_ids)
        report[system] = m
        print(f"{system}: Recall@1={m['Recall@1']} Recall@5={m['Recall@5']} MRR@10={m['MRR@10']} MeanLatencyMs={m['MeanLatencyMs']}")

    out_dir = os.path.join(ROOT, "reports")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w") as f:
        json.dump({s: [{k: v for k, v in r.items()} for r in rows] for s, rows in results.items()}, f, indent=2)
    with open(os.path.join(out_dir, "metrics.json"), "w") as f:
        json.dump(report, f, indent=2)

    lines = []
    lines.append("# Minimum Evaluation Report\n")
    lines.append("| System | Recall@1 | Recall@5 | MRR@10 | Mean Query Latency (ms) |")
    lines.append("|---|---:|---:|---:|---:|")
    for system in ["BM25", "Dense", "Hybrid"]:
        m = report[system]
        lines.append(f"| {system} | {m['Recall@1']:.4f} | {m['Recall@5']:.4f} | {m['MRR@10']:.4f} | {m['MeanLatencyMs']:.2f} |")
    lines.append("")
    lines.append("Hybrid = adaptive (BM25-first, dense+RRF fallback when BM25 margin < 6.0).")
    lines.append("Model: multi-qa-MiniLM-L6-cos-v1 (dense encoder, 384-dim, ~90 MB).")
    lines.append("Corpus: 40 IFMIF-DONES passages. Queries: 20 expert-style questions.")
    with open(os.path.join(out_dir, "evaluation_report.md"), "w") as f:
        f.write("\n".join(lines))
    print("Wrote reports/evaluation_report.md")


if __name__ == "__main__":
    main()
