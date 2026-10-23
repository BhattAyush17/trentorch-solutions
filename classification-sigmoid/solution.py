import numpy as np


def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    z: any shape of real numbers.
    Returns elementwise sigmoid, same shape as z, values strictly in (0, 1).
    """
    # TODO: Implement the sigmoid function from Theory.
    # Clip z before exponentiating so large |z| never overflows or
    # returns nan.
    z = np.asarray(z,dtype=float)

    z= np.clip(z,-709,700)
    return 1.0/(1.0+np.exp(-z))
    pass
