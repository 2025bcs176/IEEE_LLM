import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.metrics import calculate_retrieval_metrics

def test_metrics_basic():
    res = [['doc_010','doc_042','doc_099','doc_105','doc_200'],
           ['doc_018','doc_029','doc_034','doc_112','doc_142'],
           ['doc_100','doc_101','doc_102','doc_103','doc_104']]
    gt = ['doc_042','doc_018','doc_115']
    m = calculate_retrieval_metrics(res, gt)
    assert m['Recall@1'] == round(1/3,4)
    assert m['Recall@5'] == round(2/3,4)
    assert m['MRR@10'] == round((1/2+1/1+0)/3,4)
