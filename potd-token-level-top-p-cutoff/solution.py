import numpy as np


def token_level_top_p_cutoff(probs: np.ndarray, r: float) -> np.ndarray:
    """
    Keep the smallest prefix of tokens whose cumulative probability
    reaches or exceeds the nucleus threshold r.
    """
    probs = np.asarray(probs, dtype=float)

  
    indices = np.lexsort((np.arange(len(probs)), -probs))

    sorted_probs = probs[indices]

 
    cumulative = np.cumsum(sorted_probs)
    cutoff = np.searchsorted(cumulative, r, side="left") + 1

   
    kept_indices = indices[:cutoff]

    result = np.zeros_like(probs)
    result[kept_indices] = probs[kept_indices]

   
    result /= np.sum(result)

    return result
