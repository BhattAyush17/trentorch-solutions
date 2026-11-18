import numpy as np


def auc_pair_counter(scores: np.ndarray, labels: np.ndarray) -> float:
    """
    scores: array of shape (n,), finite, |s_i| <= 1e9.
    labels: array of shape (n,), binary (0 or 1).

    Return the ROC AUC using the pairwise definition with half credit for
    ties: AUC = (1 / (n_pos * n_neg)) * sum over positive/negative pairs of
    [1(s_pos > s_neg) + 0.5 * 1(s_pos == s_neg)]. If either class is empty,
    return 0. Must run in O(n log n), not O(n^2).
    """
   
    scores = np.asarray(scores, dtype=float)
    labels = np.asarray(labels, dtype=int)

    n_pos = np.sum(labels == 1)
    n_neg = np.sum(labels == 0)

    if n_pos == 0 or n_neg == 0:
        return 0.0

    order = np.argsort(scores, kind="mergesort")
    sorted_scores = scores[order]
    sorted_labels = labels[order]

    rank_sum = 0.0
    i = 0
    rank = 1

    while i < len(scores):
        j = i + 1

        while j < len(scores) and sorted_scores[j] == sorted_scores[i]:
            j += 1

        group_size = j - i
        average_rank = (rank + rank + group_size - 1) / 2.0

        rank_sum += average_rank * np.sum(sorted_labels[i:j] == 1)

        rank += group_size
        i = j

    auc = (rank_sum - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)

    return float(auc)
    pass
