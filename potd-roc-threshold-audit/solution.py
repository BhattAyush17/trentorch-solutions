def roc_threshold_audit(
    probs: list[float], labels: list[int], tau: float
) -> tuple[int, int, int, int, float, float]:
    """
    probs: predicted probabilities.
    labels: binary true labels (0 or 1), same length as probs.
    tau: decision threshold. Predict positive iff p_i >= tau.

    Returns (TP, FP, TN, FN, precision, recall).
    precision = TP / (TP + FP), or 0 if that denominator is 0.
    recall = TP / (TP + FN), or 0 if that denominator is 0.
    """
    # TODO: tally the confusion matrix, then compute precision and recall.
    TP = FP = TN = FN = 0

    for p, label in zip(probs, labels):
        prediction = 1 if p >= tau else 0

        if prediction == 1 and label == 1:
            TP += 1
        elif prediction == 1 and label == 0:
            FP += 1
        elif prediction == 0 and label == 0:
            TN += 1
        else:
            FN += 1

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0

    return TP, FP, TN, FN, float(precision), float(recall)
