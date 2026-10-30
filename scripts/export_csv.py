#!/usr/bin/env python3
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "reports")
results = json.load(open(os.path.join(REPORTS, "results.json")))
metrics = json.load(open(os.path.join(REPORTS, "metrics.json")))
from src.data.corpus import QUERIES, QRELS
rows = []
for i, q in enumerate(QUERIES):
    gt = QRELS[q["id"]]
    row = {"query_id": q["id"], "question": q["text"], "ground_truth_id": gt}
    for system in ["BM25", "Dense", "Hybrid"]:
        r = results[system][i]
        retrieved = r["top_k_ids"]
        rank = (retrieved.index(gt) + 1) if gt in retrieved else 0
        row[f"{system}_top10"] = ";".join(retrieved)
        row[f"{system}_rank"] = rank
        row[f"{system}_latency_ms"] = round(r["latency_ms"], 3)
    rows.append(row)
fieldnames = ["query_id", "question", "ground_truth_id"]
for system in ["BM25", "Dense", "Hybrid"]:
    fieldnames += [f"{system}_top10", f"{system}_rank", f"{system}_latency_ms"]
with open(os.path.join(REPORTS, "per_question_results.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
with open(os.path.join(REPORTS, "aggregate_metrics.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["system", "Recall@1", "Recall@5", "MRR@10", "MeanLatencyMs"])
    for system in ["BM25", "Dense", "Hybrid"]:
        m = metrics[system]
        w.writerow([system, m["Recall@1"], m["Recall@5"], m["MRR@10"], m["MeanLatencyMs"]])
print("Wrote CSVs")
