import numpy as np


def feature_map(x: np.ndarray) -> np.ndarray:
    """
    The element-wise positive feature map applied to both Q and K:

        phi(x) = max(x, 0) + 1
    """
    return np.maximum(x, 0) + 1


def linear_attention_row_sums(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
    """
    Linear attention without materializing an N x N matrix.
    """
    Q_prime = feature_map(Q)
    K_prime = feature_map(K)

   
    M = K_prime.T @ V

   
    Z = np.sum(K_prime, axis=0)


    numerator = Q_prime @ M

   
    denominator = Q_prime @ Z


    output = np.sum(
        numerator / denominator[:, None],
        axis=1
    )

    return output
