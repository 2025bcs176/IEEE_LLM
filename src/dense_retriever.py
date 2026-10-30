"""Dense retriever using a pretrained sentence-transformer."""
import time
from typing import List, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer, util


class DenseRetriever:
    def __init__(self, corpus: List[dict], model_name: str = "multi-qa-MiniLM-L6-cos-v1"):
        self.corpus = corpus
        self.ids = [c["id"] for c in corpus]
        self.texts = [c["text"] for c in corpus]
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
        self.embeddings = self.model.encode(self.texts, convert_to_tensor=True, show_progress_bar=False)

    def search(self, query: str, k: int = 10) -> Tuple[List[str], float]:
        start = time.perf_counter()
        q_emb = self.model.encode(query, convert_to_tensor=True, show_progress_bar=False)
        scores = util.cos_sim(q_emb, self.embeddings)[0]
        order = np.argsort(scores.cpu().numpy())[::-1][:k]
        ids = [self.ids[i] for i in order]
        latency_ms = (time.perf_counter() - start) * 1000.0
        return ids, latency_ms
