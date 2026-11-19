from typing import Tuple


def training_step_estimator(n: int, b: int, e: int) -> Tuple[int, int]:
    """
    n: number of examples.
    b: batch size.
    e: number of epochs.

    Steps per epoch retains the final partial batch, so it is the integer
    ceiling of n / b (computed with exact integer arithmetic, not
    floating-point division). Total steps = e * steps_per_epoch. Return
    (steps_per_epoch, total_steps).
    """
    # TODO: compute ceil(n / b) via integer arithmetic, then multiply by e.
    steps_per_epoch = (n + b - 1) // b
    total_steps = e * steps_per_epoch

    return steps_per_epoch, total_steps
    pass
