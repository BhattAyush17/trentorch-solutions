import numpy as np


def delivery_time_regressor(
    x: np.ndarray, y: np.ndarray, queries: np.ndarray
) -> tuple[float, np.ndarray, np.ndarray]:
    """
    x: n x d training feature matrix.
    y: length-n training targets.
    queries: m x d feature matrix to predict for.

    Fit w = pinv(X_aug) @ y, where X_aug prepends a column of ones to x
    (intercept term). Use an SVD-based pseudoinverse or lstsq, never an
    explicit inverse of X^T X, so collinear / rank-deficient features
    don't blow up.

    Return (intercept, coefficients, predictions), where coefficients has
    shape (d,) and predictions has shape (m,).
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    queries = np.asarray(queries, dtype=float)

    
    X_aug = np.column_stack((np.ones(x.shape[0]), x))

    
    weights = np.linalg.pinv(X_aug) @ y

    intercept = weights[0]
    coefficients = weights[1:]


    queries_aug = np.column_stack(
        (np.ones(queries.shape[0]), queries)
    )

    predictions = queries_aug @ weights

    return float(intercept), coefficients, predictions
