from typing import List


def replay_buffer_sampler(priorities: List[float], alpha: float) -> List[float]:
    """
    priorities: non-negative priorities p_i.
    alpha: exponent >= 0.

    weight_i = 1 for every i if alpha == 0, else p_i**alpha.
    If all weights are 0 (only possible when alpha > 0), return a uniform
    distribution. Otherwise return weight_i / sum(weights).
    """
    # TODO: build weights, handle alpha==0 and the all-zero fallback, normalize.
    if alpha == 0:
        weights = [1.0] * len(priorities)
    else:
        weights = [p ** alpha for p in priorities]

    total = sum(weights)

    if total == 0:
        n = len(priorities)
        return [1.0 / n] * n if n > 0 else []

    return [w / total for w in weights]
    pass
