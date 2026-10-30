# Deliverable 5: Recommendation (<= 300 words)

I recommend an **adaptive hybrid retriever** (BM25-first, dense+RRF fallback) as the retrieval backbone for the IEEE challenge, balancing accuracy and efficiency under resource constraints.

Measured on the 20-query IFMIF-DONES set: BM25 achieved Recall@1 0.95, Recall@5 1.00, MRR@10 0.9667 at ~0.32 ms with zero model footprint and low complexity. The dense encoder (multi-qa-MiniLM-L6-cos-v1) reached Recall@1 0.95, Recall@5 1.00, MRR@10 0.975 at ~10.3 ms with a ~90 MB model and moderate complexity, recovering semantic synonyms BM25 misses. A naive RRF hybrid matched dense MRR@10 (0.975) but at ~10-12 ms, adding complexity without latency benefit.

The adaptive hybrid uses BM25 by default and invokes dense+RRF only when BM25 confidence is low (margin < 6.0), triggering dense on ~4/20 queries. It achieves Recall@1 0.95, Recall@5 1.00, MRR@10 0.975 at ~2.6 ms mean latency, ~4x faster than dense alone, while retaining the 90 MB model only on the fallback path. This delivers the semantic accuracy of dense retrieval (fixing BM25's synonym failures such as lifespan/backplate) at a fraction of the cost, avoiding unnecessary neural calls on high-confidence lexical matches.

Given the challenge emphasis on limited resources and accuracy, this adaptive design satisfies both objectives: it keeps the common path fast and dependency-light while preserving dense-level MRR@10. I therefore recommend the adaptive hybrid as the default retrieval strategy.
