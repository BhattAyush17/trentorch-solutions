import numpy as np


def circuit_output(x: np.ndarray, theta: np.ndarray, n: int, L: int) -> float:
    """
    Simulates the hardware-efficient variational circuit and returns
    the Pauli-Z expectation value on qubit 0.
    """
    x = np.asarray(x, dtype=float)
    theta = np.asarray(theta, dtype=float)

    num_states = 2 ** n
    state = np.zeros(num_states, dtype=float)
    state[0] = 1.0

    indices = np.arange(num_states)

   
    def apply_ry(state, qubit, angle):
        c = np.cos(angle / 2.0)
        s = np.sin(angle / 2.0)

        bit = 1 << qubit

        zero_indices = indices[(indices & bit) == 0]
        one_indices = zero_indices | bit

        a0 = state[zero_indices].copy()
        a1 = state[one_indices].copy()

        state[zero_indices] = c * a0 - s * a1
        state[one_indices] = s * a0 + c * a1

    
    for i in range(n):
        apply_ry(state, i, x[i])

   
    for l in range(L):

       
        for i in range(n - 1):
            control_bit = 1 << i
            target_bit = 1 << (i + 1)

           
            swap_indices = indices[
                ((indices & control_bit) != 0)
                & ((indices & target_bit) == 0)
            ]

            partner_indices = swap_indices | target_bit

            
            temp = state[swap_indices].copy()
            state[swap_indices] = state[partner_indices]
            state[partner_indices] = temp

       
        for i in range(n):
            apply_ry(state, i, theta[l, i])

    
    qubit0_is_zero = (indices & 1) == 0

    p0 = np.sum(state[qubit0_is_zero] ** 2)
    p1 = np.sum(state[~qubit0_is_zero] ** 2)

    return float(np.clip(p0 - p1, -1.0, 1.0))


def train_and_predict(
    X: np.ndarray,
    y: np.ndarray,
    n: int,
    L: int,
    theta_init: np.ndarray,
    eta: float,
    T: int,
    queries: np.ndarray,
) -> np.ndarray:
    """
    Trains the variational circuit using full-batch gradient descent
    and the exact parameter-shift rule.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    queries = np.asarray(queries, dtype=float)

    theta = np.asarray(theta_init, dtype=float).reshape(L, n).copy()

    n_train = len(X)

    if T > 0 and n_train == 0:
        raise ValueError("Training data must not be empty.")

   
    def predict_rows(rows, params):
        return np.array(
            [circuit_output(row, params, n, L) for row in rows],
            dtype=float,
        )

   
    for _ in range(T):

        
        predictions = predict_rows(X, theta)
        errors = predictions - y

        gradient = np.zeros_like(theta)

       
        for l in range(L):
            for i in range(n):

                theta_plus = theta.copy()
                theta_minus = theta.copy()

                theta_plus[l, i] += np.pi / 2.0
                theta_minus[l, i] -= np.pi / 2.0

             
                plus_predictions = predict_rows(X, theta_plus)
                minus_predictions = predict_rows(X, theta_minus)

              
                dp = (plus_predictions - minus_predictions) / 2.0

               
                gradient[l, i] = (
                    (2.0 / n_train) * np.sum(errors * dp)
                )

       
        theta -= eta * gradient

   
    return predict_rows(queries, theta)
