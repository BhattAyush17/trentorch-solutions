import numpy as np


def bce_loss(y: np.ndarray, yhat: np.ndarray) -> float:
    """
    Binary cross-entropy loss.

    y: true labels, shape (n,), each 0 or 1.
    yhat: predicted probabilities, shape (n,), guaranteed in [1e-7, 1 - 1e-7].

    L = -(1/n) * sum( y*log(yhat) + (1-y)*log(1-yhat) )
    """
    n = len(y)

    loss = -(1 / n) * np.sum(
        y * np.log(yhat) + (1 - y) * np.log(1 - yhat)
    )

    return float(loss)
