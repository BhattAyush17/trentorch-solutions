import numpy as np


def feature_importances(
    tree: dict,
    input: np.ndarray,
    labels: np.ndarray,
    n_features: int,
) -> np.ndarray:
    """
    Compute total sample-weighted information gain for each feature.
    """

    importances = np.zeros(n_features, dtype=float)
    total_samples = input.shape[0]

    def walk(node: dict, node_input: np.ndarray, node_labels: np.ndarray):
        if node["leaf"]:
            return

        feature = node["feature"]
        threshold = node["threshold"]

        # Recreate the same split used when building the tree
        left_mask = node_input[:, feature] <= threshold
        right_mask = ~left_mask

        left_labels = node_labels[left_mask]
        right_labels = node_labels[right_mask]

        # Information gain at this node
        gain = information_gain(
            node_labels,
            left_labels,
            right_labels
        )

        # Weight by fraction of total training samples reaching this node
        weight = node_labels.size / total_samples
        importances[feature] += weight * gain

        # Continue down both branches
        walk(
            node["left"],
            node_input[left_mask],
            left_labels
        )

        walk(
            node["right"],
            node_input[right_mask],
            right_labels
        )

    walk(tree, input, labels)

    # Normalize to sum to 1
    total_importance = np.sum(importances)

    if total_importance > 0:
        importances /= total_importance

    return importances
