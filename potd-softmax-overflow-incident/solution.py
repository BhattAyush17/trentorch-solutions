import numpy as np


def softmax_overflow_incident(logits: np.ndarray) -> np.ndarray:
    """
    logits: array of shape (n, d). Rows are independent.

    Returns an array of shape (n, d): the stable, max-subtracted softmax
    of each row.
    """
    # TODO: subtract each row's max before exponentiating, then
    # normalize each row by its own sum.
    logits = np.asarray(logits, dtype=float)

    shifted = logits - np.max(logits, axis=1, keepdims=True)

    exp_values = np.exp(shifted)

    return exp_values / np.sum(exp_values, axis=1, keepdims=True)
    pass
