"""Retrieval evaluation metrics."""
from typing import List, Dict


def calculate_retrieval_metrics(retrieval_results: List[List[str]],
                               ground_truth_ids: List[str]) -> Dict[str, float]:
    """Compute Recall@1, Recall@5, MRR@10.

    Args:
        retrieval_results: top-k retrieved passage IDs per query.
        ground_truth_ids: single correct passage ID per query.
    """
    metrics = {'Recall@1': 0.0, 'Recall@5': 0.0, 'MRR@10': 0.0}
    num_queries = len(ground_truth_ids)
    if num_queries == 0:
        return metrics

    for i in range(num_queries):
        retrieved = retrieval_results[i] if i < len(retrieval_results) else []
        correct_id = ground_truth_ids[i]

        if correct_id in retrieved[:1]:
            metrics['Recall@1'] += 1
        if correct_id in retrieved[:5]:
            metrics['Recall@5'] += 1
        if correct_id in retrieved[:10]:
            rank = retrieved[:10].index(correct_id) + 1
            metrics['MRR@10'] += 1.0 / rank

    for key in metrics:
        metrics[key] = round(metrics[key] / num_queries, 4)
    return metrics


def per_query_ranks(retrieval_results: List[List[str]],
                    ground_truth_ids: List[str]) -> List[int]:
    """Return 1-based rank of the ground truth in top-10 (0 if absent)."""
    ranks = []
    for retrieved, correct in zip(retrieval_results, ground_truth_ids):
        if correct in retrieved[:10]:
            ranks.append(retrieved[:10].index(correct) + 1)
        else:
            ranks.append(0)
    return ranks
