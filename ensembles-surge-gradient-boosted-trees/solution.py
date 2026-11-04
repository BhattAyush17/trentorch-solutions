import numpy as np


def build_regression_tree(
    X: np.ndarray,
    g: np.ndarray,
    h: np.ndarray,
    lam: float,
    gamma: float,
    max_depth: int,
    depth: int = 0,
) -> dict:
    """
    Grows one regularized regression tree using exact greedy split finding.
    """
    X = np.asarray(X, dtype=float)
    g = np.asarray(g, dtype=float)
    h = np.asarray(h, dtype=float)

    G = np.sum(g)
    H = np.sum(h)

    leaf_weight = -G / (H + lam)


    if depth >= max_depth or len(X) < 2:
        return {
            "leaf": True,
            "weight": float(leaf_weight),
        }

    best_gain = -np.inf
    best_feature = None
    best_threshold = None

    parent_score = (G ** 2) / (H + lam)

    
    for j in range(X.shape[1]):
        unique_values = np.unique(X[:, j])

     
        for i in range(len(unique_values) - 1):
            threshold = (
                unique_values[i] + unique_values[i + 1]
            ) / 2.0

            left_mask = X[:, j] <= threshold
            right_mask = ~left_mask

            if not np.any(left_mask) or not np.any(right_mask):
                continue

            GL = np.sum(g[left_mask])
            HL = np.sum(h[left_mask])

            GR = np.sum(g[right_mask])
            HR = np.sum(h[right_mask])

            gain = 0.5 * (
                (GL ** 2) / (HL + lam)
                + (GR ** 2) / (HR + lam)
                - parent_score
            ) - gamma

         
            if gain > best_gain:
                best_gain = gain
                best_feature = j
                best_threshold = threshold

   
    if best_gain <= 0 or best_feature is None:
        return {
            "leaf": True,
            "weight": float(leaf_weight),
        }

   
    left_mask = X[:, best_feature] <= best_threshold
    right_mask = ~left_mask

    left_tree = build_regression_tree(
        X[left_mask],
        g[left_mask],
        h[left_mask],
        lam,
        gamma,
        max_depth,
        depth + 1,
    )

    right_tree = build_regression_tree(
        X[right_mask],
        g[right_mask],
        h[right_mask],
        lam,
        gamma,
        max_depth,
        depth + 1,
    )

    return {
        "leaf": False,
        "feature": int(best_feature),
        "threshold": float(best_threshold),
        "left": left_tree,
        "right": right_tree,
    }


def gbdt_predict(
    X: np.ndarray,
    y: np.ndarray,
    T: int,
    lam: float,
    gamma: float,
    eta: float,
    max_depth: int,
    base_score: float,
    queries: np.ndarray,
) -> np.ndarray:
    """
    Trains T rounds of gradient-boosted regression trees and predicts queries.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    queries = np.asarray(queries, dtype=float)

    n = len(X)

  
    train_pred = np.full(n, base_score, dtype=float)

    trees = []

  
    def predict_tree(tree, row):
        node = tree

        while not node["leaf"]:
            feature = node["feature"]
            threshold = node["threshold"]

            if row[feature] <= threshold:
                node = node["left"]
            else:
                node = node["right"]

        return node["weight"]


    for _ in range(T):
       
        g = train_pred - y
        h = np.ones(n, dtype=float)

     
        tree = build_regression_tree(
            X,
            g,
            h,
            lam,
            gamma,
            max_depth,
        )

        trees.append(tree)


        for i in range(n):
            leaf_weight = predict_tree(tree, X[i])
            train_pred[i] += eta * leaf_weight

    
    predictions = np.full(
        len(queries),
        base_score,
        dtype=float,
    )

    for tree in trees:
        for i in range(len(queries)):
            leaf_weight = predict_tree(tree, queries[i])
            predictions[i] += eta * leaf_weight

    return predictions
