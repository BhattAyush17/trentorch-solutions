import numpy as np


def information_gain(
    parent_labels: np.ndarray,
    left_labels: np.ndarray,
    right_labels: np.ndarray,
) -> float:
    """
    parent_labels: labels of every sample in the node before splitting.
    left_labels, right_labels: parent_labels partitioned by the
    candidate split, every sample in exactly one of the two.

    Returns:
        how much the split reduces Gini impurity, a float.
    """
    parent_gini = gini_impurity(parent_labels)

    n_parent = len(parent_labels)
    n_left = len(left_labels)
    n_right = len(right_labels)

    weighted_child_gini = (
        (n_left / n_parent) * gini_impurity(left_labels)
        + (n_right / n_parent) * gini_impurity(right_labels)
    )

    return float(parent_gini - weighted_child_gini)
