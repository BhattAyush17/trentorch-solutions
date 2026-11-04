import numpy as np


def class_weighted_loss(
    logits: np.ndarray, labels: np.ndarray, weights: np.ndarray
) -> float:
    """
    logits: n x C logits.
    labels: length-n 0-based true class indices.
    weights: length-C per-class weights.

    p_ic = softmax(logits_i)_c
    L = -(1/n) * sum_i weights[labels[i]] * log(p_i, labels[i])

    Divide by n, NOT by sum(weights[labels]). Return L.
    """
    # TODO: stable log-softmax per row, weight by true-class weight,
    # sum, divide by n.

    logits = np.asarray(logits, dtype=float)
    labels = np.asarray(labels, dtype=int)
    weights = np.asarray(weights, dtype=float)

   
    row_max = np.max(logits, axis=1, keepdims=True)
    shifted = logits - row_max

    log_probs = shifted - np.log(
        np.sum(np.exp(shifted), axis=1, keepdims=True)
    )

    true_log_probs = log_probs[np.arange(len(labels)), labels]

  
    sample_weights = weights[labels]

    loss = -np.sum(sample_weights * true_log_probs) / len(labels)

    return float(loss)
    pass
