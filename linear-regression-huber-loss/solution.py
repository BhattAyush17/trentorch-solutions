import numpy as np


def huber_loss(
    input: np.ndarray, target: np.ndarray, delta: float = 1.0, reduction: str = "mean"
) -> float | np.ndarray:
    """
    Mirrors torch.nn.functional.huber_loss(input, target, delta=delta,
    reduction=reduction): quadratic (MSE-like) for small errors,
    linear (L1-like) for large ones, splitting at |error| == delta.

        elementwise = 0.5 * error^2                    if |error| <= delta
                    = delta * (|error| - 0.5 * delta)   otherwise
    """
    input = np.asarray(input, dtype=float)
    target = np.asarray(target, dtype=float)

    if delta <= 0:
        raise ValueError("delta must be greater than 0")

    if reduction not in ("mean", "sum", "none"):
        raise ValueError("reduction must be 'mean', 'sum', or 'none'")

    error = input - target
    abs_error = np.abs(error)

    elementwise = np.where(
        abs_error <= delta,
        0.5 * error**2,
        delta * (abs_error - 0.5 * delta),
    )

    if reduction == "mean":
        return float(np.mean(elementwise))
    elif reduction == "sum":
        return float(np.sum(elementwise))
    else:
        return elementwise
