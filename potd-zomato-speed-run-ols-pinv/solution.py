import numpy as np


def ols_fit_predict(X: np.ndarray, y: np.ndarray, Q: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Fit ordinary least squares by the normal equation and predict on Q.
    """
    # Add intercept column
    X_aug = np.column_stack((np.ones(X.shape[0]), X))
    Q_aug = np.column_stack((np.ones(Q.shape[0]), Q))

    # Moore-Penrose pseudo-inverse
    w = np.linalg.pinv(X_aug) @ y

    # Predictions
    predictions = Q_aug @ w

    return w, predictions
