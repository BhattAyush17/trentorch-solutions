import numpy as np


def mse_loss(
    input: np.ndarray,
    target: np.ndarray,
    reduction: str = "mean"
) -> float | np.ndarray:
    """
    input:     shape matching target, any shape
    target:    shape matching input, any shape
    reduction: 'mean' | 'sum' | 'none'
    """
    squared_error = (input - target) ** 2

    if reduction == "mean":
        return float(np.mean(squared_error))

    elif reduction == "sum":
        return float(np.sum(squared_error))

    elif reduction == "none":
        return squared_error

    else:
        raise ValueError(f"Unknown reduction: {reduction}")
