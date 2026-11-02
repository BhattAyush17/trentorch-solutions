import numpy as np


def leaky_relu_dead_unit_check(
    x: np.ndarray, alpha: float
) -> tuple[np.ndarray, np.ndarray]:
    """
    x: input values.
    alpha: negative slope, 0 <= alpha <= 1.

    f(x)  = x       if x > 0,  else alpha * x
    f'(x) = 1       if x > 0,  else alpha

    x == 0 belongs to the non-positive branch (f'(0) = alpha).

    Return (activations, derivatives).
    """
    # TODO: pick the branch with x > 0, not x >= 0.
    x =np.asarray(x, dtype=float)
    activations = np.where(x>0, x, alpha*x)
    derivatives = np.where(x>0, 1.0, alpha)
    return activations, derivatives
    pass
