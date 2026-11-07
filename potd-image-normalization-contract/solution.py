import numpy as np


def image_normalization_contract(
    x: np.ndarray, mu: np.ndarray, sigma: np.ndarray
) -> np.ndarray:
    """
    x: array of shape (3,), the raw RGB pixel values.
    mu: array of shape (3,), per-channel means.
    sigma: array of shape (3,), per-channel standard deviations, each > 0.

    Returns an array of shape (3,): z_c = (x_c - mu_c) / sigma_c for each
    channel, using that channel's own mean and standard deviation.
    """
    # TODO: normalize each channel with its own mean and std.
    x = np.asarray(x, dtype=float)
    mu = np.asarray(mu, dtype=float)
    sigma = np.asarray(sigma, dtype=float)

    return (x - mu) / sigma
    pass
