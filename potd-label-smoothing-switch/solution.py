import numpy as np


def label_smoothing(logits: np.ndarray, y: int, eps: float) -> tuple[np.ndarray, float]:
    """
    Build the label-smoothed target distribution over C = len(logits)
    classes and compute its cross-entropy loss against logits.

    q[c] = 1 - eps + eps/C for c == y, else eps/C.
    loss = -sum(q * log_softmax(logits)).

    Return (q, loss).
    """
    logits = np.asarray(logits, dtype=float)
    C = len(logits)

    # Give every class eps/C probability.
    q = np.full(C, eps / C, dtype=float)

    # Add the remaining probability mass to the true class.
    q[y] += 1.0 - eps

    # Numerically stable log-softmax.
    max_logit = np.max(logits)
    log_sum_exp = max_logit + np.log(
        np.sum(np.exp(logits - max_logit))
    )
    log_softmax = logits - log_sum_exp

    loss = -np.sum(q * log_softmax)

    return q, float(loss)
