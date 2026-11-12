import numpy as np


def gradient_norm_circuit_breaker(g: np.ndarray, c: float) -> tuple[float, np.ndarray]:
    """
    g: array of shape (n,), the gradient vector.
    c: clipping threshold, c > 0.

    Returns (norm, g_tilde): the original L2 norm of g, and the
    globally rescaled vector (unchanged if norm <= c, otherwise scaled
    by c / norm so every component shrinks by the same factor).
    """
    # TODO: compute the L2 norm, then rescale the whole vector by a
    # single scalar factor if it exceeds c.
    g = np.asarray(g, dtype=float)

  
    norm = float(np.linalg.norm(g))

    
    if norm > c:
        g_tilde = g * (c / norm)
    else:
        g_tilde = g.copy()

    return norm, g_tilde
    pass
