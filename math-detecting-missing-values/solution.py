import numpy as np


def missing_mask(x: np.ndarray) -> np.ndarray:
    """
    Missing numeric values are represented as np.nan.
    """
    return np.isnan(x)


def missing_count_per_column(x: np.ndarray) -> np.ndarray:
    """
    x is a 2D array, (rows, columns). Returns a length-`num_columns`
    array: how many missing values each column has.
    """
    return np.sum(np.isnan(x), axis=0)


def missing_fraction_per_column(x: np.ndarray) -> np.ndarray:
    """
    Same as missing_count_per_column, but as a fraction of the total
    row count.
    """
    return np.mean(np.isnan(x), axis=0)
