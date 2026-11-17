import numpy as np


def smo_fit(
    X: np.ndarray,
    y: np.ndarray,
    C: float,
    tol: float,
    max_passes: int,
) -> tuple[np.ndarray, float]:

    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)

    n = len(X)

    alpha = np.zeros(n, dtype=float)
    b = 0.0
    passes = 0


    K = X @ X.T

    while passes < max_passes:
        num_changed = 0

        for i in range(n):

          
            f_i = np.sum(alpha * y * K[:, i]) + b
            E_i = f_i - y[i]

           
            violates_kkt = (
                (y[i] * E_i < -tol and alpha[i] < C)
                or
                (y[i] * E_i > tol and alpha[i] > 0)
            )

            if not violates_kkt:
                continue

       
            j = (i + 1) % n

            f_j = np.sum(alpha * y * K[:, j]) + b
            E_j = f_j - y[j]

            alpha_i_old = alpha[i]
            alpha_j_old = alpha[j]

         
            if y[i] != y[j]:
                L = max(0.0, alpha_j_old - alpha_i_old)
                H = min(C, C + alpha_j_old - alpha_i_old)
            else:
                L = max(0.0, alpha_i_old + alpha_j_old - C)
                H = min(C, alpha_i_old + alpha_j_old)

            if L == H:
                continue

          
            eta = 2.0 * K[i, j] - K[i, i] - K[j, j]

            if eta >= 0:
                continue

         
            alpha_j_new = (
                alpha_j_old
                - y[j] * (E_i - E_j) / eta
            )

            alpha_j_new = np.clip(alpha_j_new, L, H)

            if abs(alpha_j_new - alpha_j_old) < 1e-5:
                continue

        
            alpha_i_new = (
                alpha_i_old
                + y[i] * y[j] * (alpha_j_old - alpha_j_new)
            )

         
            b1 = (
                b
                - E_i
                - y[i] * (alpha_i_new - alpha_i_old) * K[i, i]
                - y[j] * (alpha_j_new - alpha_j_old) * K[i, j]
            )

            b2 = (
                b
                - E_j
                - y[i] * (alpha_i_new - alpha_i_old) * K[i, j]
                - y[j] * (alpha_j_new - alpha_j_old) * K[j, j]
            )

          
            if 0 < alpha_i_new < C:
                b = b1
            elif 0 < alpha_j_new < C:
                b = b2
            else:
                b = (b1 + b2) / 2.0

         
            alpha[i] = alpha_i_new
            alpha[j] = alpha_j_new

            num_changed += 1

    
        if num_changed == 0:
            passes += 1
        else:
            passes = 0

    return alpha, float(b)


def svm_decision_function(
    X: np.ndarray,
    y: np.ndarray,
    alpha: np.ndarray,
    b: float,
    queries: np.ndarray,
) -> np.ndarray:

    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    alpha = np.asarray(alpha, dtype=float)
    queries = np.asarray(queries, dtype=float)

    #Lin smv
    scores = queries @ X.T @ (alpha * y) + b

    return scores
