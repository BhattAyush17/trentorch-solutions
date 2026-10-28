def gradient_accumulator(
    theta: float, eta: float, microbatches: list[tuple[int, float]]
) -> tuple[float, float]:
    """
    microbatches: list of (n_j, g_j) pairs, n_j examples with mean
    gradient g_j.

    g = sum(n_j * g_j) / sum(n_j)   (example-weighted mean, NOT the mean
    of the microbatch means).
    theta' = theta - eta * g.

    Return (g, theta_prime).
    """
    # TODO: weight by example count, divide exactly once.
    total_examples = sum(n for n, _ in microbatches)

    weighted_gradient = sum(
        n * g for n, g in microbatches
    )

    g = weighted_gradient / total_examples
    theta_prime = theta - eta * g

    return float(g), float(theta_prime)
