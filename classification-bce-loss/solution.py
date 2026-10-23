import numpy as np


def bce_loss(p: np.ndarray, y: np.ndarray) -> float:
    """
    p: predicted probabilities, shape (n_samples,)
    y: true labels (0 or 1), shape (n_samples,)
    Returns a single scalar.
    """
    # TODO: Implement Binary Cross-Entropy, as derived in Theory.
    # Clip p away from exactly 0 or 1 before taking a log, and return
    # a plain Python float, not a NumPy scalar.
    p = np.asarray(p, dtype=float)
    y= np.asarray(y, dtype=float)

    eps=1e-15
    p= np.clip(p, eps,  1.0-eps)
    loss = -np.mean(y*np.log(p)+ (1.0-y)*np.log(1.0-p))
    return float(loss)
    pass
