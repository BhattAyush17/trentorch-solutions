import numpy as np


def expectation(values, probabilities):
    """
    values: 1D array-like, the outcomes a discrete random variable X can take
    probabilities: 1D array-like, P(X = values[i]) for each i

    Returns:
        E[X], as a float, from Theory.
    """
    values = np.asarray(values, dtype=float)
    probabilities = np.asarray(probabilities, dtype=float)

    return float(np.sum(values * probabilities))


def variance(values, probabilities):
    """
    values, probabilities: same as `expectation`

    Returns:
        Var(X) = E[(X - E[X])^2], as a float, from Theory.
    """
    values = np.asarray(values, dtype=float)
    probabilities = np.asarray(probabilities, dtype=float)

    mean = expectation(values, probabilities)
    return float(np.sum((values - mean) ** 2 * probabilities))


def pmf_covariance(x_values, y_values, joint_probabilities):
    """
    x_values: 1D array-like, the outcomes X can take
    y_values: 1D array-like, the outcomes Y can take
    joint_probabilities: 2D array-like, joint_probabilities[i, j] =
        P(X=x_values[i], Y=y_values[j])

    Returns:
        Cov(X, Y) = E[(X - E[X])(Y - E[Y])], as a float, from Theory.
    """
    x_values = np.asarray(x_values, dtype=float)
    y_values = np.asarray(y_values, dtype=float)
    joint_probabilities = np.asarray(joint_probabilities, dtype=float)

    # Marginals from the joint distribution.
    p_x = np.sum(joint_probabilities, axis=1)
    p_y = np.sum(joint_probabilities, axis=0)

    mean_x = expectation(x_values, p_x)
    mean_y = expectation(y_values, p_y)

    centered_x = x_values - mean_x
    centered_y = y_values - mean_y

    return float(
        np.sum(
            joint_probabilities
            * centered_x[:, None]
            * centered_y[None, :]
        )
    )


def sample_mean(x: np.ndarray) -> float:
    """
    The sample mean estimates a distribution's expectation E[X]:
    simply the average of the observed values.
    """
    return float(np.mean(x))


def sample_variance(x: np.ndarray, ddof: int = 0) -> float:
    """
    The sample variance estimates a distribution's Var(X). `ddof`
    ("delta degrees of freedom") controls the divisor: ddof=0 divides
    by n (the biased/population estimator), ddof=1 divides by n-1
    (Bessel's correction, the unbiased estimator). See Theory for why
    the distinction matters.
    """
    return float(np.var(x, ddof=ddof))


def covariance(x: np.ndarray, y: np.ndarray, ddof: int = 0) -> float:
    """
    Covariance measures whether x and y tend to move together (positive),
    move oppositely (negative), or show no consistent relationship
    (near zero):

        cov(x, y) = (1/(n - ddof)) * sum((x_i - mean(x)) * (y_i - mean(y)))

    Same ddof convention 05-expectation-covariance's sample_variance uses
    (in fact, covariance(x, x, ddof) is exactly sample_variance(x, ddof)).
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    x_centered = x - np.mean(x)
    y_centered = y - np.mean(y)

    return float(
        np.sum(x_centered * y_centered) / (len(x) - ddof)
    )


def correlation(x: np.ndarray, y: np.ndarray) -> float:
    """
    Correlation rescales covariance into a unitless number in [-1, 1],
    by dividing out each variable's own spread:

        corr(x, y) = cov(x, y) / (std(x) * std(y))
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    cov_xy = covariance(x, y)
    std_x = np.std(x)
    std_y = np.std(y)

    return float(cov_xy / (std_x * std_y))
