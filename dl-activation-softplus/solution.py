import numpy as np


def softplus(x, beta=1.0):
    """Compute softplus activation, smooth approximation to ReLU.

    Args:
        x: Input array of any shape.
        beta: Positive steepness parameter.

    Returns:
        Output array with same shape as x, always positive.
    """
    if beta <= 0:
        raise ValueError("beta must be positive")

    x = np.asarray(x, dtype=float)
    z = beta * x

    return np.logaddexp(0, z) / beta
    pass
