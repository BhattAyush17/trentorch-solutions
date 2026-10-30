import numpy as np


def feed_ranker_layer_norm(x: np.ndarray, eps: float) -> np.ndarray:
    """
    x: length-d feature vector.
    eps: small positive constant.

    mu = mean(x)
    v = population variance of x (divide by d, not d - 1)
    xhat_i = (x_i - mu) / sqrt(v + eps)

    No learnable scale or bias. Return xhat.
    """
    x = np.asarray(x, dtype=float)

    mu = np.mean(x)
    v = np.mean((x - mu) ** 2)

    xhat = (x - mu) / np.sqrt(v + eps)

    return xhat
