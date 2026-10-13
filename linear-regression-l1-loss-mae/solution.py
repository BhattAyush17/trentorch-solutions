import numpy as np


def l1_loss(
    input: np.ndarray,
    target: np.ndarray,
    reduction: str = "mean"
) -> float | np.ndarray:
    """
    input, target: same shape, any shape.
    reduction: "mean" (default), "sum", or "none".
    """
    loss = np.abs(input - target)

    if reduction == "mean":
        return float(np.mean(loss))
    elif reduction == "sum":
        return float(np.sum(loss))
    elif reduction == "none":
        return loss
    else:
        raise ValueError("reduction must be 'mean', 'sum', or 'none'")
