import numpy as np


def soft_threshold(x: np.ndarray, threshold: float) -> np.ndarray:
    """
    The soft-thresholding operator, the core building block of Lasso's
    solver: shrinks x toward zero by `threshold`, snapping anything
    within `threshold` of zero to EXACTLY zero.

        soft_threshold(x, t) = sign(x) * max(|x| - t, 0)
    """
    return np.sign(x) * np.maximum(np.abs(x) - threshold, 0)


def lasso_regression_coordinate_descent(
    input: np.ndarray, target: np.ndarray, alpha: float = 1.0, epochs: int = 200
) -> tuple[np.ndarray, np.ndarray]:
    """
    Ridge Regression (L2) has a clean closed form; Lasso's L1 penalty
    does NOT (it's not differentiable at exactly 0), so this uses
    coordinate descent instead: repeatedly update ONE weight at a
    time, holding every other weight fixed, using soft_threshold to
    solve that single-coordinate subproblem exactly, cycling through
    all coordinates for several epochs.

    Center `input` and `target` first (subtract their means) so the
    bias can be recovered afterward without needing to include it in
    the penalized coordinate descent loop at all.

    Returns (weight, bias) in the same (1, in_features)/(1,) shapes
    the other regression questions in this curriculum use.
    """
    input_mean = np.mean(input, axis=0)
    target_mean = np.mean(target)

    X = input - input_mean
    y = target - target_mean

    n_samples, n_features = X.shape
    weight = np.zeros(n_features, dtype=float)

    for _ in range(epochs):
        for j in range(n_features):
            residual = y - X @ weight + X[:, j] * weight[j]
            rho = X[:, j] @ residual
            denominator = X[:, j] @ X[:, j]

            if denominator != 0:
                weight[j] = soft_threshold(
                    rho, n_samples * alpha
                ) / denominator

    bias = np.array([target_mean - input_mean @ weight])

    return weight.reshape(1, -1), bias
