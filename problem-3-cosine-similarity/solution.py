import numpy as np


def solve(a, b):
    """Implement Cosine Similarity from the mathematical contract in README.md."""
    
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors.")

    return float(np.dot(a, b) / (norm_a * norm_b))
