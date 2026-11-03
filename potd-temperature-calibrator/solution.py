import numpy as np


def temperature_calibrator(z: np.ndarray, tau: float) -> np.ndarray:
    """
    z: logits.
    tau: temperature, tau > 0.

    p = softmax(z / tau), using an overflow-safe softmax (subtract the
    max before exponentiating). Divide by tau, never multiply.

    Return p.
    """
    z = np.asarray(z, dtype=float)

    if tau <= 0:
        raise ValueError("tau must be greater than 0")

    scaled = z / tau
    shifted = scaled - np.max(scaled)

    exp_scores = np.exp(shifted)
    p = exp_scores / np.sum(exp_scores)

    return p
