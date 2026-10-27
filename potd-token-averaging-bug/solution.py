import numpy as np


def valid_token_mean_loss(losses: np.ndarray, mask: np.ndarray) -> float:
    """
    losses: B x T array of per-token losses.
    mask: B x T array of 0/1 validity flags (same shape as losses).

    L = sum(mask * losses) / sum(mask)

    If sum(mask) == 0, return 0.0 (no division by zero).

    Return L as a float.
    """
    # TODO: sum only over valid tokens, in both numerator and denominator.
    valid_count = np.sum(mask)

    if valid_count == 0:
        return 0.0

    total_loss = np.sum(losses*mask)
    return float(total_loss/valid_count)
    pass
