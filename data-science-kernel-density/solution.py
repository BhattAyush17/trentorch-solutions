import numpy as np


def gaussian_kde(x: np.ndarray, grid: np.ndarray, bandwidth: float) -> np.ndarray:
    """
    x: 1D data array
    grid: 1D array of points at which to evaluate the density
    bandwidth: standard deviation of each Gaussian bump (> 0)

    Returns:
        KDE evaluated at every point in grid.
    """
    if bandwidth <= 0:
        raise ValueError("bandwidth must be greater than 0")

    x = np.asarray(x)
    grid = np.asarray(grid)

    diff = (grid[:, None] - x[None, :]) / bandwidth

    kernel = (
        np.exp(-0.5 * diff ** 2)
        / (bandwidth * np.sqrt(2 * np.pi))
    )

    return np.mean(kernel, axis=1)


def silverman_bandwidth(x: np.ndarray) -> float:
    """
    Returns Silverman's rule-of-thumb bandwidth.
    """
    x = np.asarray(x)
    n = len(x)

    std = np.std(x, ddof=1)

    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    iqr_scaled = iqr / 1.34

    # Use the non-zero spread if one of them is zero.
    if std == 0:
        spread = iqr_scaled
    elif iqr_scaled == 0:
        spread = std
    else:
        spread = min(std, iqr_scaled)

    # Completely degenerate data.
    if spread == 0:
        return 1.0

    return float(0.9 * spread * n ** (-1 / 5))


def integrate_density(density: np.ndarray, grid: np.ndarray) -> float:
    """
    Returns the trapezoid-rule area under density over grid.
    """
    density = np.asarray(density)
    grid = np.asarray(grid)

    widths = grid[1:] - grid[:-1]
    heights = (density[:-1] + density[1:]) / 2

    return float(np.sum(widths * heights))
