import numpy as np


def find_best_split(
    input: np.ndarray, labels: np.ndarray
) -> tuple[int, float, float] | None:
    """
    input:  shape (n_samples, n_features)
    labels: shape (n_samples,)

    Searches every feature and every candidate threshold (the midpoint
    between each pair of consecutive sorted unique values).
    """
    parent_gini = gini_impurity(labels)

    best_split = None
    best_gain = 0.0

    n_samples, n_features = input.shape

    for feature in range(n_features):
        values = np.unique(input[:, feature])

        # Need at least two distinct values to make a split
        if len(values) < 2:
            continue

        # Midpoints between consecutive unique values
        thresholds = (values[:-1] + values[1:]) / 2.0

        for threshold in thresholds:
            left_mask = input[:, feature] <= threshold
            right_mask = ~left_mask

            left_labels = labels[left_mask]
            right_labels = labels[right_mask]

            gain = information_gain(
                labels,
                left_labels,
                right_labels
            )

            if gain > best_gain:
                best_gain = gain
                best_split = (
                    feature,
                    float(threshold),
                    float(gain)
                )

    return best_split


def build_tree(input: np.ndarray, labels: np.ndarray, max_depth: int) -> dict:
    """
    Recursively builds a decision tree.
    """
    # Majority class
    values, counts = np.unique(labels, return_counts=True)
    prediction = int(values[np.argmax(counts)])

    # Base cases
    if (
        max_depth == 0
        or len(labels) < 2
        or len(values) == 1
    ):
        return {
            "leaf": True,
            "prediction": prediction
        }

    split = find_best_split(input, labels)

    if split is None:
        return {
            "leaf": True,
            "prediction": prediction
        }

    feature, threshold, gain = split

    left_mask = input[:, feature] <= threshold
    right_mask = ~left_mask

    left_tree = build_tree(
        input[left_mask],
        labels[left_mask],
        max_depth - 1
    )

    right_tree = build_tree(
        input[right_mask],
        labels[right_mask],
        max_depth - 1
    )

    return {
        "leaf": False,
        "feature": feature,
        "threshold": threshold,
        "left": left_tree,
        "right": right_tree
    }


def predict_tree(tree: dict, input: np.ndarray) -> np.ndarray:
    """
    Predict the class for each row by walking the tree.
    """
    predictions = []

    for row in input:
        node = tree

        while not node["leaf"]:
            if row[node["feature"]] <= node["threshold"]:
                node = node["left"]
            else:
                node = node["right"]

        predictions.append(node["prediction"])

    return np.array(predictions)
