import math


def is_valid_pmf(probabilities):
    """
    probabilities: list/tuple of floats, one per outcome of a discrete
        random variable.

    Returns:
        True if `probabilities` is a valid probability mass function:
        every value is non-negative AND they sum to 1 (within 1e-9).
    """
    return (
        all(p >= 0 for p in probabilities)
        and math.isclose(sum(probabilities), 1.0, abs_tol=1e-9)
    )


def expected_value_discrete(outcomes, probabilities):
    """
    outcomes: list/tuple of numbers, the values a discrete random
    variable X can take.
    probabilities: list/tuple of floats, P(X = outcomes[i]) for each i,
        same length as outcomes.

    Returns:
        E[X] = sum(outcome * probability), from Theory.
    """
    return sum(
        outcome * probability
        for outcome, probability in zip(outcomes, probabilities)
    )


def binomial_pmf(n, p, k):
    """
    n: number of independent trials (positive int)
    p: probability of success on each trial (float in [0, 1])
    k: number of successes to compute the probability of (int in [0, n])

    Returns:
        P(X = k) for X ~ Binomial(n, p), from Theory.
    """
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def uniform_pdf(x, a, b):
    """
    x: point to evaluate the density at
    a, b: the interval's lower and upper bounds (a < b)

    Returns:
        The value of the continuous Uniform(a, b) density at x: 1/(b-a)
        inside [a, b], and 0 outside it.
    """
    if a <= x <= b:
        return 1 / (b - a)

    return 0.0
