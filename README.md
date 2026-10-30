# IEEE 2026 Technical Challenge: Domain-Specific QA with LLMs

Retrieval baseline and evaluation framework for the IFMIF-DONES target domain.

## Structure
- `src/` - retrievers (BM25, dense, hybrid), pipeline, metrics
- `src/data/corpus.py` - sample corpus, 20 queries, qrels
- `docs/` - literature review, error analysis, recommendation
- `scripts/run_evaluation.py` - runs evaluation, writes reports/
- `reports/` - generated metrics and evaluation report

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
python scripts/run_evaluation.py
```

## Tests
```bash
pytest -q
```

## Submission artifacts
- `reports/per_question_results.csv` - per-query retrieved IDs, ranks, latencies
- `reports/aggregate_metrics.csv` - aggregate metrics
- `docs/research_report.md` / `docs/pdf/research_report.pdf` - consolidated report
- `data/queries.json`, `data/qrels.json`, `data/corpus.jsonl` - labeled test set

## Environment
- Python 3.14, CPU-only (no GPU required)
- Models: sentence-transformers/multi-qa-MiniLM-L6-cos-v1 (~90 MB, Apache-2.0)
- Libraries: rank-bm25 (MIT), numpy
