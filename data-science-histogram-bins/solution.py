import numpy as np


def sturges_bins(n: int) -> int:
    """Returns ceil(log2(n)) + 1 as an int, for n >= 1."""
    # TODO: Implement Sturges' rule.
    return int(np.ceil(np.log2(n))+1)
    pass


def freedman_diaconis_bins(x: np.ndarray) -> int:
    """
    Bin width h = 2 * IQR / n ** (1/3), with IQR the difference between
    the 75th and 25th percentiles (np.percentile, linear interpolation).
    Returns ceil((max - min) / h) as an int, at least 1. If the IQR is
    zero, returns sturges_bins(len(x)).
    """
    # TODO: Implement the Freedman-Diaconis rule.

    n = len(x)
    q75= np.percentile(x,75)
    q25 = np.percentile(x,25)
    iqr = q75-q25
    if iqr == 0:
     return sturges_bins(n)

    h = 2 * iqr / (n ** (1 / 3))
    bins = int(np.ceil((np.max(x) - np.min(x)) / h))

    return max(1, bins)
    pass


def bin_edges(x: np.ndarray, n_bins: int) -> np.ndarray:
    """Returns n_bins + 1 equally spaced edges from min(x) to max(x)."""
    # TODO: Space the edges evenly across the data range.
    return np.linspace(np.min(x), np.max(x), n_bins + 1)
    pass


def histogram_counts(x: np.ndarray, edges: np.ndarray) -> np.ndarray:
    """
    Returns an int array of length len(edges) - 1. Value v is in bin i
    when edges[i] <= v < edges[i + 1]; the last bin also includes its
    right edge. Values outside [edges[0], edges[-1]] are ignored. Do not
    call np.histogram.
    """
    # TODO: Find each value's bin and count them.

    counts = np.zeros(len(edges) - 1, dtype=int)

    for value in x:
        if value < edges[0] or value > edges[-1]:
            continue

        
        i = np.searchsorted(edges, value, side="right") - 1

       
        if i == len(counts):
            i -= 1

        counts[i] += 1

    return counts
    pass
