def best_f1_threshold(scores: list[float], y: list[int]) -> tuple[float, float]:
    """
    The score threshold that maximizes F1 (predict positive if score >= t).

    scores: n predicted scores. y: n true labels, each 0 or 1.

    For each distinct value in scores, using it as threshold t, compute
    F1(t) over the whole dataset. Return (best_threshold, best_f1).

    Ties for the best F1 are broken by the LARGER threshold. A threshold
    where precision or recall is undefined (a zero denominator) can never
    win. Sort once and sweep with running TP/FP counts, O(n log n), not
    a from-scratch recompute per threshold.
    """
    # TODO: sort by score descending, group equal scores together (they
    # share one threshold), and only update the best on a STRICT improvement.
     # Sort by score descending
    pairs = sorted(zip(scores, y), reverse=True)

    total_positive = sum(y)
    tp = 0
    fp = 0

    best_threshold = None
    best_f1 = -1.0

    i = 0
    n = len(pairs)

    while i < n:
        threshold = pairs[i][0]

        # Add every example having this score
        while i < n and pairs[i][0] == threshold:
            if pairs[i][1] == 1:
                tp += 1
            else:
                fp += 1
            i += 1

        fn = total_positive - tp

        precision_den = tp + fp
        recall_den = tp + fn

        # Undefined precision or recall cannot win
        if precision_den == 0 or recall_den == 0:
            continue

        precision = tp / precision_den
        recall = tp / recall_den

        f1_den = precision + recall
        if f1_den == 0:
            continue

        f1 = 2 * precision * recall / f1_den

        # Strict improvement automatically preserves the larger
        # threshold when ties occur because we sweep descending.
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    return best_threshold, best_f1
    pass
