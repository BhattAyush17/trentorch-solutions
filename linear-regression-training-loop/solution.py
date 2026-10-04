import numpy as np


def train_linear_regression(
    input: np.ndarray,
    target: np.ndarray,
    lr: float,
    epochs: int,
) -> tuple[np.ndarray, np.ndarray]:

    # Initialize parameters
    weight = np.zeros((1, input.shape[1]))
    bias = np.zeros(1)

    # Target must be (batch_size, 1)
    target = target.reshape(-1, 1)

    for _ in range(epochs):
        # Compute gradients
        grad_weight, grad_bias = mse_gradient(
            input,
            weight,
            bias,
            target
        )

        # Update parameters
        weight, bias = gd_step(
            weight,
            bias,
            grad_weight,
            grad_bias,
            lr
        )

    return weight, bias
