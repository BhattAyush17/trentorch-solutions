import numpy as np


def dropout_inference_mismatch(
    activations: np.ndarray, mask: np.ndarray, mode: str, p: float
) -> np.ndarray:
    """
    activations: array of shape (n,), |x_i| <= 1e6.
    mask: array of shape (n,), binary (0 or 1).
    mode: "train" or "infer".
    p: drop probability, 0 <= p < 1.

    In "infer" mode, return activations unchanged (ignore mask). In "train"
    mode, let q = 1 - p and return mask * activations / q (inverted
    dropout).
    """
    # TODO: branch on mode; apply inverted dropout only in "train" mode.
    activations = np.asarray(activations, dtype=float)

    if mode == "infer":
        return activations.copy()

    if mode == "train":
        q = 1.0 - p
        mask = np.asarray(mask, dtype=float)
        return mask * activations / q

    raise ValueError("mode must be 'train' or 'infer'")

    pass
