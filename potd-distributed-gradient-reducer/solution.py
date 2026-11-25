from typing import List, Tuple


def distributed_gradient_reducer(
    theta: List[float], eta: float, workers: List[Tuple[int, List[float]]]
) -> Tuple[List[float], List[float]]:
    """
    theta: current parameter vector.
    eta: learning rate.
    workers: list of (batch_size, mean_gradient_vector) pairs.

    global_gradient_j = sum_i(n_i * g_i_j) / sum_i(n_i)
    updated_theta_j = theta_j - eta * global_gradient_j
    Return (global_gradient, updated_theta).
    """
    # TODO: weight each worker's gradient by its batch size before averaging.
    total_samples = sum(batch_size for batch_size, _ in workers)

    if total_samples == 0:
        global_gradient = [0.0] * len(theta)
    else:
        global_gradient = [
            sum(batch_size * gradient[j] for batch_size, gradient in workers)
            / total_samples
            for j in range(len(theta))
        ]

    updated_theta = [
        param - eta * grad
        for param, grad in zip(theta, global_gradient)
    ]

    return global_gradient, updated_theta
    pass
