import numpy as np


def closed_form_linear_regression(
    input: np.ndarray,
    target: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """
    Solves linear regression exactly using the Normal Equation
    and the pseudoinverse.
    """

    # Add a column of ones for the bias term
    augmented_input = np.column_stack([
        input,
        np.ones(input.shape[0])
    ])

    # Solve for [weights..., bias]
    theta = np.linalg.pinv(augmented_input) @ target

    # Return in the same shapes as the gradient-descent version
    weight = theta[:-1].reshape(1, -1)
    bias = np.array([theta[-1]])

    return weight, bias
