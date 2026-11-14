import numpy as np


def solve(A, x):
    """Implement Matrix-Vector Product from the mathematical contract in README.md."""
    A = np.asarray(A)
    x = np.asarray(x)

    return A @ x
