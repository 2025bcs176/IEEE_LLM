# Deliverable 4: Error Analysis (Lexical vs. Dense Retrieval)

## Case 1: Lexical Superiority on Out-of-Vocabulary (OOV) Jargon
- Query (q_09): How are the material samples actively cooled within the High Flux Test Module (HFTM)?
- Expected passage: doc_093
- Top-ranked: BM25 doc_093 (Rank 1); Dense doc_122 (Rank 6) [illustrative]
- Hypothesis: BM25 succeeds through exact matching on the rare acronym "HFTM". The dense encoder lacks a specific embedding for "HFTM", falling back on general terms and retrieving a cooling-related but wrong passage.

## Case 2: Dense Superiority on Semantic Synonyms
- Query (q_18): What is the designed lifespan of the lithium target backplate before it requires replacement due to radiation damage?
- Expected passage: doc_122 ("...operational cycle of 11 months before dpa-induced embrittlement necessitates component swap.")
- Top-ranked: BM25 doc_201 (Rank 8) [illustrative]; Dense doc_122 (Rank 1)
- Hypothesis: BM25 fails due to near-zero lexical overlap (lifespan/backplate/replacement vs. operational cycle/structural support/swap). Dense maps the semantic meaning of component replacement timelines correctly.

## Case 3: Dense Semantic Drift on Technical Nuance
- Query (q_04): How does the neutron energy spectrum of DONES compare to the spectrum expected in the DEMO fusion reactor?
- Expected passage: doc_088
- Top-ranked: BM25 doc_088 (Rank 1); Dense doc_012 (Rank 1) [illustrative]
- Hypothesis: doc_012 discusses the general DEMO spectrum at length. The dense model over-weights the concept "DEMO spectrum" and retrieves a passage that never mentions DONES. BM25 enforces the exact term "DONES".

## Case 4: Dense Comprehension of Multi-Term Concepts
- Query (q_08): What are the safety containment protocols for managing the radioactive tritium produced within the lithium loop?
- Expected passage: doc_201
- Top-ranked: BM25 doc_045 (Rank 4) [illustrative]; Dense doc_201 (Rank 1)
- Hypothesis: BM25 over-indexes on frequency of "tritium"/"lithium", retrieving doc_045 (lithium-tritium reactions). Dense captures the broader intent "safety containment protocols", prioritising security/extraction passages.

## Case 5: BM25 Dominance in Long Queries with Critical Entities
- Query (q_14): Which specific variants of reduced-activation ferritic/martensitic (RAFM) steels are prioritized for the first testing phase?
- Expected passage: doc_158
- Top-ranked: BM25 doc_158 (Rank 1); Dense doc_115 (Rank 5) [illustrative]
- Hypothesis: In a long sentence the dense encoder averages the representation, diluting the critical entity "RAFM". It retrieves a general steel-testing passage. BM25 gives rare token "RAFM" high IDF weight, surfacing the exact match.

Note: ranks labelled [illustrative] follow the assignment's mock analysis; measured ranks on the sample corpus are recorded in reports/metrics.json.
