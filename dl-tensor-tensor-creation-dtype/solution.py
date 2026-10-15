import numpy as np


def make_tensor(data, dtype: np.dtype | None = None) -> np.ndarray:
    """
    Mirrors torch.tensor(data, dtype=dtype)'s dtype-inference rule.
    """
    arr = np.array(data)

    # Explicit dtype: use it directly
    if dtype is not None:
        return arr.astype(dtype)

    # PyTorch defaults floating-point tensors to float32
    if np.issubdtype(arr.dtype, np.floating):
        return arr.astype(np.float32)

    # Integers and bools keep NumPy's inferred dtype
    return arr


def zeros(shape: tuple[int, ...], dtype: np.dtype = np.float32) -> np.ndarray:
    """Mirrors torch.zeros(shape, dtype=dtype)."""
    return np.zeros(shape, dtype=dtype)


def ones(shape: tuple[int, ...], dtype: np.dtype = np.float32) -> np.ndarray:
    """Mirrors torch.ones(shape, dtype=dtype)."""
    return np.ones(shape, dtype=dtype)


def arange(
    start: float,
    stop: float,
    step: float = 1,
    dtype: np.dtype | None = None
) -> np.ndarray:
    """Mirrors torch.arange(start, stop, step, dtype=dtype)."""
    arr = np.arange(start, stop, step)

    # Explicit dtype
    if dtype is not None:
        return arr.astype(dtype)

    # Float values -> PyTorch-style float32
    if np.issubdtype(arr.dtype, np.floating):
        return arr.astype(np.float32)

    # Integers -> preserve inferred dtype
    return arr
