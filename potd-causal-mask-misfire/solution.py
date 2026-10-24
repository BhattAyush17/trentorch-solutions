import numpy as np


def causal_mask_misfire(scores: np.ndarray) -> np.ndarray:
    """
    Row-wise, numerically stable softmax under a causal mask: for query
    row i, only key columns j <= i are visible. Forbidden entries (j > i)
    must be exactly 0.0 in the output.

    scores: shape (n, n).
    """
    scores = np.asarray(scores, dtype=float)

    n = scores.shape[0]
    mask = np.triu(np.ones((n, n), dtype=bool), k=1)

    masked_scores = np.where(mask, -np.inf, scores)

    row_max = np.max(masked_scores, axis=1, keepdims=True)
    shifted = masked_scores - row_max

    exp_scores = np.exp(shifted)
    exp_scores[mask] = 0.0

    normalizer = np.sum(exp_scores, axis=1, keepdims=True)

    return exp_scores / normalizer
