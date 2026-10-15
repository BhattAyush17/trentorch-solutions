import numpy as np


def add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Mirrors torch.add(a, b) / a + b."""
    return np.add(a,b)
    pass


def sub(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Mirrors torch.sub(a, b) / a - b."""
    return np.subtract(a,b)
    pass


def mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Mirrors torch.mul(a, b) / a * b."""
    return np.multiply(a,b)
    pass


def div(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Mirrors torch.div(a, b): TRUE division, always -- even when both a
    and b are integer tensors, the result is floating-point, never
    truncated toward zero the way `//` would.
    """
    # TODO: np.true_divide, not a plain `/` on integer arrays and not `//`.
    return np.true_divide(a,b)
    pass


def power(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Mirrors torch.pow(a, b) / a ** b."""
    return np.power(a,b)
    pass
