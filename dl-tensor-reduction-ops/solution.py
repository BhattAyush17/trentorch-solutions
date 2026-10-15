import numpy as np


def sum_(a: np.ndarray, axis: int | None = None, keepdims: bool = False) -> np.ndarray:
    """Mirrors torch.sum(a, dim=axis, keepdim=keepdims)."""
    return np.sum(a, axis=axis, keepdims=keepdims)


def mean_(a: np.ndarray, axis: int | None = None, keepdims: bool = False) -> np.ndarray:
    """Mirrors torch.mean(a, dim=axis, keepdim=keepdims)."""
    return np.mean(a, axis=axis, keepdims=keepdims)


def max_(a: np.ndarray, axis: int | None = None, keepdims: bool = False):
    """
    Mirrors torch.max(a, dim=axis, keepdim=keepdims):
      - axis=None: returns a single scalar, the max over the whole array.
      - axis given: returns (values, indices), the max value AND its
        index along that axis, both with the same shape (respecting
        keepdims).
    """
    if axis is None:
        return np.max(a)

    values = np.max(a, axis=axis, keepdims=keepdims)
    indices = np.argmax(a, axis=axis)

    if keepdims:
        indices = np.expand_dims(indices, axis=axis)

    return values, indices
