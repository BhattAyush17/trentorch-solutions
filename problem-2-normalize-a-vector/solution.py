import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""

    norm = np.linalg.norm(x)

    if norm == 0:
        raise ValueError("Cant normalize a zero vector.")

    return x / norm
