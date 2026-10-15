import numpy as np

# import numpy as np


# def reshape(a: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
#     """Mirrors torch.reshape(a, shape). shape may contain one -1, inferred from the total element count."""
#     return np.reshape(a, shape)


# def transpose(a: np.ndarray, dim0: int, dim1: int) -> np.ndarray:
#     """Mirrors torch.transpose(a, dim0, dim1): swaps exactly these TWO dimensions, leaves every other dimension in place."""
#     axes = list(range(a.ndim))
#     axes[dim0], axes[dim1] = axes[dim1], axes[dim0]
#     return np.transpose(a, axes)


# def permute(a: np.ndarray, dims: tuple[int, ...]) -> np.ndarray:
#     """Mirrors torch.permute(a, dims): reorders ALL dimensions according to dims (a full permutation, not a two-dimension swap)."""
#     return np.transpose(a, dims)






def reshape(a: np.ndarray, shape: tuple[int, ...]) -> np.ndarray:
    """Mirrors torch.reshape(a, shape). shape may contain one -1, inferred from the total element count."""
    return np.reshape(a, shape)
    pass


def transpose(a: np.ndarray, dim0: int, dim1: int) -> np.ndarray:
    """Mirrors torch.transpose(a, dim0, dim1): swaps exactly these TWO dimensions, leaves every other dimension in place."""
    axes = list(range(a.ndim))
    axes[dim0], axes[dim1] = axes[dim1], axes[dim0]
    return np.transpose(a, axes)
    pass


def permute(a: np.ndarray, dims: tuple[int, ...]) -> np.ndarray:
    """Mirrors torch.permute(a, dims): reorders ALL dimensions according to dims (a full permutation, not a two-dimension swap)."""
    return np.transpose(a, dims)
    pass
