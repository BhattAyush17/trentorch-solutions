import numpy as np


def build_tree_pre_pruned(
    input: np.ndarray,
    labels: np.ndarray,
    max_depth: int,
    min_samples_leaf: int = 1,
) -> dict:
    """
    Builds a decision tree with pre-pruning based on min_samples_leaf.
    """

    # Majority class at this node
    values, counts = np.unique(labels, return_counts=True)
    default = int(values[np.argmax(counts)])

    # Base cases
    if (
        max_depth == 0
        or len(labels) < 2
        or len(values) == 1
    ):
        return {
            "leaf": True,
            "prediction": default,
            "default": default,
        }

    # Find the best split
    split = find_best_split(input, labels)

    if split is None:
        return {
            "leaf": True,
            "prediction": default,
            "default": default,
        }

    feature, threshold, gain = split

    # Partition the data
    left_mask = input[:, feature] <= threshold
    right_mask = ~left_mask

    # Pre-pruning condition
    if (
        np.sum(left_mask) < min_samples_leaf
        or np.sum(right_mask) < min_samples_leaf
    ):
        return {
            "leaf": True,
            "prediction": default,
            "default": default,
        }

    # Recursively build children
    left_tree = build_tree_pre_pruned(
        input[left_mask],
        labels[left_mask],
        max_depth - 1,
        min_samples_leaf,
    )

    right_tree = build_tree_pre_pruned(
        input[right_mask],
        labels[right_mask],
        max_depth - 1,
        min_samples_leaf,
    )

    return {
        "leaf": False,
        "feature": feature,
        "threshold": threshold,
        "left": left_tree,
        "right": right_tree,
        "default": default,
    }


def prune_tree(
    tree: dict,
    input_val: np.ndarray,
    labels_val: np.ndarray
) -> dict:
    """
    Reduced-error post-pruning.
    """

    # Leaf: nothing to prune
    if tree["leaf"]:
        return tree

    feature = tree["feature"]
    threshold = tree["threshold"]

    # Route validation samples through this split
    left_mask = input_val[:, feature] <= threshold
    right_mask = ~left_mask

    left_input = input_val[left_mask]
    left_labels = labels_val[left_mask]

    right_input = input_val[right_mask]
    right_labels = labels_val[right_mask]

    # Bottom-up pruning
    left_tree = prune_tree(
        tree["left"],
        left_input,
        left_labels,
    )

    right_tree = prune_tree(
        tree["right"],
        right_input,
        right_labels,
    )

    pruned_tree = {
        "leaf": False,
        "feature": feature,
        "threshold": threshold,
        "left": left_tree,
        "right": right_tree,
        "default": tree["default"],
    }

    # If no validation samples reach this node,
    # use the training majority class as fallback.
    if len(labels_val) == 0:
        leaf_prediction = tree["default"]
    else:
        values, counts = np.unique(
            labels_val,
            return_counts=True
        )
        leaf_prediction = int(values[np.argmax(counts)])

    # Error made by the recursively-pruned subtree
    if len(labels_val) == 0:
        subtree_error = 0
    else:
        subtree_predictions = predict_tree(
            pruned_tree,
            input_val
        )
        subtree_error = np.sum(
            subtree_predictions != labels_val
        )

    # Error made by replacing the whole subtree with one leaf
    leaf_error = np.sum(
        labels_val != leaf_prediction
    )

    # Prune when leaf is no worse
    if leaf_error <= subtree_error:
        return {
            "leaf": True,
            "prediction": leaf_prediction,
            "default": tree["default"],
        }

    return pruned_tree
