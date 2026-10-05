import numpy as np


def variance(targets: np.ndarray) -> float:
    """Population variance of targets. Empty input has variance 0.0 by convention."""
    if targets.size == 0:
        return 0.0

    return float(np.var(targets))


def variance_reduction(
    parent_targets: np.ndarray,
    left_targets: np.ndarray,
    right_targets: np.ndarray,
) -> float:
    """Same shape as information_gain, with variance in place of Gini impurity."""
    parent_var = variance(parent_targets)

    n_parent = len(parent_targets)
    n_left = len(left_targets)
    n_right = len(right_targets)

    weighted_child_var = (
        (n_left / n_parent) * variance(left_targets)
        + (n_right / n_parent) * variance(right_targets)
    )

    return float(parent_var - weighted_child_var)


def find_best_regression_split(
    input: np.ndarray, targets: np.ndarray
) -> tuple[int, float, float] | None:
    """Find the split that maximizes variance reduction."""

    best_split = None
    best_reduction = 0.0

    n_samples, n_features = input.shape

    for feature in range(n_features):
        values = np.unique(input[:, feature])

        # Cannot split if there is only one unique value
        if len(values) < 2:
            continue

        # Midpoints between consecutive unique values
        thresholds = (values[:-1] + values[1:]) / 2.0

        for threshold in thresholds:
            left_mask = input[:, feature] <= threshold
            right_mask = ~left_mask

            left_targets = targets[left_mask]
            right_targets = targets[right_mask]

            reduction = variance_reduction(
                targets,
                left_targets,
                right_targets
            )

            if reduction > best_reduction:
                best_reduction = reduction
                best_split = (
                    feature,
                    float(threshold),
                    float(reduction)
                )

    return best_split


def build_regression_tree(
    input: np.ndarray,
    targets: np.ndarray,
    max_depth: int
) -> dict:
    """
    Recursively builds a regression tree.
    """

    # Leaf prediction = mean target
    prediction = float(np.mean(targets))

    # Base cases
    if (
        max_depth == 0
        or len(targets) < 2
        or variance(targets) == 0.0
    ):
        return {
            "leaf": True,
            "prediction": prediction
        }

    # Find best split
    split = find_best_regression_split(input, targets)

    if split is None:
        return {
            "leaf": True,
            "prediction": prediction
        }

    feature, threshold, reduction = split

    # Partition samples
    left_mask = input[:, feature] <= threshold
    right_mask = ~left_mask

    # Recursively build children
    left_tree = build_regression_tree(
        input[left_mask],
        targets[left_mask],
        max_depth - 1
    )

    right_tree = build_regression_tree(
        input[right_mask],
        targets[right_mask],
        max_depth - 1
    )

    return {
        "leaf": False,
        "feature": feature,
        "threshold": threshold,
        "left": left_tree,
        "right": right_tree
    }


def predict_regression_tree(
    tree: dict,
    input: np.ndarray
) -> np.ndarray:
    """Predict using a trained regression tree."""

    predictions = []

    for row in input:
        node = tree

        while not node["leaf"]:
            if row[node["feature"]] <= node["threshold"]:
                node = node["left"]
            else:
                node = node["right"]

        predictions.append(node["prediction"])

    return np.asarray(predictions, dtype=float)
