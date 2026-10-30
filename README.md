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
