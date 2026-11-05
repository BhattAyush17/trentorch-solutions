def confidence_calibration_bin(
    probs: list[float], labels: list[int], k: int
) -> list[tuple[int, float, float]]:
    """
    Group probabilities into k equal-width bins.

    Return (count, mean_prob, positive_rate) for each bin.
    Empty bins return (0, 0.0, 0.0).
    """
    counts = [0] * k
    prob_sums = [0.0] * k
    positive_sums = [0] * k

    for p, label in zip(probs, labels):
        bin_idx = min(k - 1, int(k * p))

        counts[bin_idx] += 1
        prob_sums[bin_idx] += p
        positive_sums[bin_idx] += label

    result = []

    for i in range(k):
        count = counts[i]

        if count == 0:
            result.append((0, 0.0, 0.0))
        else:
            mean_prob = prob_sums[i] / count
            positive_rate = positive_sums[i] / count

            result.append((count, mean_prob, positive_rate))

    return result
