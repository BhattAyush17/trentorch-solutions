import numpy as np


def fraud_models_focal_loss(
    logits: np.ndarray, labels: np.ndarray, alpha: float, gamma: float
) -> float:
    """
    logits: array of shape (n,), each in [-20, 20].
    labels: array of shape (n,), binary (0 or 1).
    alpha: class weight in [0, 1].
    gamma: focusing parameter in [0, 5].

    For each example compute p = sigmoid(z), then p_t and alpha_t for the
    TRUE class (p_t = p and alpha_t = alpha when y = 1; p_t = 1 - p and
    alpha_t = 1 - alpha when y = 0). Loss = -alpha_t * (1 - p_t)^gamma *
    log(p_t). Return the mean loss over all examples.
    """
    # TODO: compute per-example focal loss using the true-class p_t/alpha_t,
    # then average.
    logits = np.asarray(logits, dtype=float)
    labels = np.asarray(labels, dtype=int)

  
    p = 1.0 / (1.0 + np.exp(-logits))

    p_t = np.where(labels == 1, p, 1.0 - p)

    alpha_t = np.where(labels == 1, alpha, 1.0 - alpha)

  
    loss = -alpha_t * (1.0 - p_t) ** gamma * np.log(p_t)

    return float(np.mean(loss))
    
    pass
