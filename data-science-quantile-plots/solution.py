import math

import numpy as np


def normal_ppf(p: float) -> float:
    """
    Returns the standard normal quantile of p (the z with Phi(z) = p),
    accurate to at least 1e-9, for 0 < p < 1.
    """
    if not 0.0 < p < 1.0:
        raise ValueError("p strictly between 0 & 1")

    def normal_cdf(z):
        return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))

 
    lo = -10.0
    hi = 10.0

  
    for _ in range(100):
        mid = (lo + hi) / 2.0

        if normal_cdf(mid) < p:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2.0


def plotting_positions(n: int) -> np.ndarray:
    """Returns the array (i - 0.5) / n for i = 1 .. n."""
    return (np.arange(1, n + 1, dtype=float) - 0.5) / n


def qq_points(x: np.ndarray) -> tuple:
    """
    Returns (theoretical, sample): sample is x sorted ascending and
    theoretical[i] = normal_ppf(plotting_positions(n)[i]).
    """
    sample = np.sort(np.asarray(x)).astype(float)

    n = len(sample)
    positions = plotting_positions(n)

    theoretical = np.array(
        [normal_ppf(p) for p in positions],
        dtype=float
    )

    return theoretical, sample


def qq_line(theoretical: np.ndarray, sample: np.ndarray) -> tuple:
    """
    Returns (slope, intercept) of the line through the points at the
    25th and 75th percentiles of the two arrays.
    """
    t25, t75 = np.percentile(theoretical, [25, 75])
    s25, s75 = np.percentile(sample, [25, 75])

    slope = (s75 - s25) / (t75 - t25)
    intercept = s25 - slope * t25

    return float(slope), float(intercept)


def qq_correlation(x: np.ndarray) -> float:
    """
    Returns the Pearson correlation between theoretical and sample.
    """
    theoretical, sample = qq_points(x)

    correlation = np.corrcoef(theoretical, sample)[0, 1]

    return float(correlation)
