import numpy as np


def gini_impurity(labels: np.ndarray) -> float:
    """
    labels: 1-D array of class labels (any integers, not necessarily
    0..k-1 or contiguous), one per sample in a single tree node.

    Returns:
        the Gini impurity of this set of labels, a float in [0, 1).
    """
    if labels.size == 0:
        return 0.0

    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / labels.size

    return float(1.0 - np.sum(probabilities ** 2))
