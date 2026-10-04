import numpy as np


def get_unique_categories(column: np.ndarray) -> np.ndarray:
    """
    Returns every distinct value appearing in `column`, in a fixed,
    reproducible order.
    """
    return np.unique(column)


def one_hot_encode(
    column: np.ndarray,
    categories: np.ndarray | None = None
) -> np.ndarray:
    """
    Converts a categorical column into an (n, k) binary matrix.
    """
    if categories is None:
        categories = get_unique_categories(column)

    return (column[:, None] == categories[None, :]).astype(int)
