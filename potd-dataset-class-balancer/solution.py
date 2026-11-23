from typing import List


def dataset_class_balancer(counts: List[int]) -> List[float]:
    """
    counts: non-negative class counts, length C, summing to N.

    For each class c with count n_c > 0, return N / (C * n_c). A class
    with n_c == 0 gets weight 0 (and so does every class if N == 0).
    """
    # TODO: compute N and C, then the inverse-frequency weight per class.
    total = sum(counts)
    num_classes = len(counts)

    if total == 0 or num_classes == 0:
        return [0.0] * num_classes

    return [
        total / (num_classes * count) if count > 0 else 0.0
        for count in counts
    ]

    pass
