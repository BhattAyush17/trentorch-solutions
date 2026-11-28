import numpy as np

def solve(coeffs):
    """Solve the system a*x + b*y = e and c*x + d*y = f, where coeffs is [a,b,c,d,e,f]. A singular system raises ValueError."""
    a, b, c, d, e, f = coeffs

    A = np.array([[a, b],
                  [c, d]])

    B = np.array([e, f])

    if np.linalg.det(A) == 0:
        raise ValueError(" no unique solution")

    return np.linalg.solve(A, B)
    pass
