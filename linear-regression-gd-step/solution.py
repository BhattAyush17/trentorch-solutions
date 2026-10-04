import numpy as np


def gd_step(
    weight: np.ndarray,
    bias: np.ndarray | None,
    grad_weight: np.ndarray,
    grad_bias: np.ndarray | None,
    lr: float,
) -> tuple[np.ndarray, np.ndarray | None]:
    """
    Apply one gradient-descent update.

    Returns:
        updated_weight, updated_bias
    """
    updated_weight = weight - lr * grad_weight

    if bias is None:
        updated_bias = None
    else:
        updated_bias = bias - lr * grad_bias

    return updated_weight, updated_bias
