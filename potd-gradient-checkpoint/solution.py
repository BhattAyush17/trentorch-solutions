def gradient_checkpoint(
    x: float, y: float, w1: float, b1: float, w2: float, b2: float
) -> tuple[float, float, float, float]:
    """
    Two-layer scalar network: h = ReLU(w1*x + b1), yhat = w2*h + b2,
    L = 0.5 * (yhat - y)^2.

    Return (h, yhat, loss, dL_dw1), where dL_dw1 is computed by the chain
    rule, using ReLU'(z) = 1 if z > 0 else 0 on the pre-activation z.
    """
    # TODO: evaluate the ReLU gate on the pre-activation, not on h.

    z = w1 * x + b1
    h = max(0.0, z)

    yhat = w2 * h + b2
    error = yhat - y
    loss = 0.5 * error ** 2

    relu_grad = 1.0 if z > 0 else 0.0
    dL_dw1 = error * w2 * relu_grad * x

    return float(h), float(yhat), float(loss), float(dL_dw1)
    pass
