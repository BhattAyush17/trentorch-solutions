import numpy as np

R_H = 1.097373e7  # m^-1, fixed by the problem -- do not substitute a different value


def rydberg_wavelength_nm(n1: int, n2: int) -> float:
    """
    Theoretical vacuum wavelength in nanometers for transition n2 -> n1.
    """
    inverse_lambda = R_H * (
        1.0 / (n1 ** 2) - 1.0 / (n2 ** 2)
    )

    wavelength_m = 1.0 / inverse_lambda

    return wavelength_m * 1e9


def gp_calibrate(
    training: list[tuple[int, int, float]],
    sigma_f: float,
    l: float,
    sigma_n: float,
    queries: list[tuple[int, int]],
) -> np.ndarray:
    """
    Exact Gaussian Process regression using Cholesky decomposition.
    """

    # No training data.
    if not training:
        return np.empty((len(queries), 2), dtype=float)

    # ------------------------------------------------------------
    # 1. Build training inputs x and calibration residuals y
    # ------------------------------------------------------------
    x = np.array(
        [rydberg_wavelength_nm(n1, n2) for n1, n2, _ in training],
        dtype=float
    )

    y = np.array(
        [
            measured - rydberg_wavelength_nm(n1, n2)
            for n1, n2, measured in training
        ],
        dtype=float
    )

    # ------------------------------------------------------------
    # 2. RBF kernel matrix
    # ------------------------------------------------------------
    diff = x[:, None] - x[None, :]

    K = sigma_f ** 2 * np.exp(
        -(diff ** 2) / (2.0 * l ** 2)
    )

    # Add observation noise
    A = K + (sigma_n ** 2) * np.eye(len(x))

    # ------------------------------------------------------------
    # 3. Cholesky solve
    # ------------------------------------------------------------
    L = np.linalg.cholesky(A)

    # L @ z = y
    z = np.linalg.solve(L, y)

    # L.T @ alpha = z
    alpha = np.linalg.solve(L.T, z)

    # ------------------------------------------------------------
    # 4. Predictions
    # ------------------------------------------------------------
    results = []

    for n1, n2 in queries:
        x_star = rydberg_wavelength_nm(n1, n2)

        # Kernel vector between training points and query
        diff_star = x - x_star

        k_star = sigma_f ** 2 * np.exp(
            -(diff_star ** 2) / (2.0 * l ** 2)
        )

        # Posterior mean of calibration residual
        mu = k_star @ alpha

        # L @ v = k_star
        v = np.linalg.solve(L, k_star)

        # Posterior variance
        variance = sigma_f ** 2 - v @ v

        # Guard against tiny negative floating-point errors.
        variance = max(variance, 0.0)

        uncertainty = np.sqrt(variance)

        predicted_wavelength = x_star + mu

        results.append(
            (predicted_wavelength, uncertainty)
        )

    return np.asarray(results, dtype=float)
