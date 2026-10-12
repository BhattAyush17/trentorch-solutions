import numpy as np




def clip_grad_norm(g: np.ndarray, tau: float) -> np.ndarray:
    """
    Global-norm gradient clipping.

    g: shape (d,). tau: the clip threshold, tau > 0.

    If ||g||_2 > tau (strict), return g * (tau / ||g||_2). Otherwise
    return g unchanged.
    """
    norm = np.linalg.norm(g)

    if norm > tau:
        return g * (tau / norm)

    return g
    

    norm = np.linalg.norm(g)

    if norm > tau :
        return g * (tau/norm)
    

    pass
