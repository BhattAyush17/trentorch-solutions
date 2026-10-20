import numpy as np


def ecdf(x: np.ndarray) -> tuple:
    """
    Returns (values, probabilities): x sorted ascending and
    probabilities[i] = (i + 1) / n. Repeated values each get an entry.
    """
    # TODO: Sort the data and pair it with the staircase heights.
    values = np.sort(x)
    n = len(values)

    probabilities = np.arange(1, n + 1, dtype=float) / n

    return values, probabilities
    pass


def ecdf_at(x: np.ndarray, points: np.ndarray) -> np.ndarray:
    """
    Returns a float array: for each query point, the fraction of entries
    of x that are less than or equal to it.
    """
    # TODO: Count the sorted values at or below each point.
    values = np.sort(x)
    n = len(values)

    counts = np.searchsorted(values, points, side="right")

    return counts / n

    pass


def ks_distance(x: np.ndarray, y: np.ndarray) -> float:
    """
    Returns max over t of |F_x(t) - F_y(t)|, with F the ECDF of each
    sample, as a float. Only the pooled sample values need checking.
    """
    # TODO: Compare the two ECDFs at every pooled value.
    pooled = np.sort(np.concatenate((x, y)))

    fx = ecdf_at(x, pooled)
    fy = ecdf_at(y, pooled)

    return float(np.max(np.abs(fx - fy)))
    pass
