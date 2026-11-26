from typing import List


def rnn_gradient_fade(hidden_states: List[float], a: float) -> float:
    """
    hidden_states: already-computed h_1, ..., h_T.
    a: recurrent weight.

    Compute the exact product over t of a * (1 - h_t**2), i.e. dh_T/dh_0
    for the recurrence h_t = tanh(a*h_{t-1} + x_t). Do not average the
    per-step derivatives; return their exact product.
    """
    # TODO: multiply the per-step local derivatives together.
    gradient = 1.0

    for h in hidden_states:
        gradient *= a * (1.0 - h**2)

    return gradient
