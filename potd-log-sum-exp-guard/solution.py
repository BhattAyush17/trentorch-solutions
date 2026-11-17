import numpy as np


def log_sum_exp_guard(scores: np.ndarray) -> float:
    """
    scores: array of shape (n,), each |x_i| <= 1e6.

    Compute log(sum(exp(scores))) using the numerically stable form:
    m + log(sum(exp(scores - m))), where m = max(scores). Never exponentiate
    the raw scores directly.
    """
    # TODO: subtract the max before exponentiating, then add it back.
    scores = np.asarray(scores, dtype=float)

    m = np.max(scores)
    result = m + np.log(np.sum(np.exp(scores - m)))

    return float(result)
    pass
