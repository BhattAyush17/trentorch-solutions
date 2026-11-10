import numpy as np


def attention_firewall(
    q: np.ndarray, keys: np.ndarray, values: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    q: array of shape (d,), the query for the final position.
    keys: array of shape (n, d).
    values: array of shape (n, dv).

    s_j = (q . keys[j]) / sqrt(d)
    p = softmax(s) (numerically stable, max-subtracted)
    o = sum_j p_j * values[j]

    Returns (p, o): the attention probabilities (shape (n,)) and the
    output vector (shape (dv,)).
    """
    # TODO: scale the dot products by 1/sqrt(d), softmax them stably,
    # then take the weighted sum over values.

    q = np.asarray(q, dtype=float)
    keys = np.asarray(keys, dtype=float)
    values = np.asarray(values, dtype=float)

    # Scaled dot-product attention scores
    d = q.shape[0]
    scores = (keys @ q) / np.sqrt(d)

    # Numerically stable softmax
    shifted_scores = scores - np.max(scores)
    exp_scores = np.exp(shifted_scores)
    probabilities = exp_scores / np.sum(exp_scores)

    # Weighted sum of value vectors
    output = probabilities @ values

    return probabilities, output
    pass
