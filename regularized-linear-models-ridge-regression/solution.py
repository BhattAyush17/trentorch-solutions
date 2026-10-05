import numpy as np


def ridge_regression_closed_form(
    input: np.ndarray, target: np.ndarray, alpha: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """
    `Stretch: L2 Regularization (Ridge)` derived ridge's GRADIENT for
    use with gradient descent. Ridge regression also has a closed
    form, a small modification of `Linear Regression: closed form
    (Normal Equation)`'s own formula:

        theta = (X^T @ X + alpha * I) @ X^T @ y

    where `I` is the identity matrix EXCEPT with a `0` in the last
    diagonal entry, corresponding to the bias term, which is
    conventionally never regularized (see Theory for why).
    """
    augmented_input = np.column_stack([
        input,
        np.ones(input.shape[0])
    ])

    identity = np.eye(augmented_input.shape[1])
    identity[-1, -1] = 0

    theta = np.linalg.pinv(
        augmented_input.T @ augmented_input + alpha * identity
    ) @ augmented_input.T @ target

    weight = theta[:-1].reshape(1, -1)
    bias = np.array([theta[-1]])

    return weight, bias
