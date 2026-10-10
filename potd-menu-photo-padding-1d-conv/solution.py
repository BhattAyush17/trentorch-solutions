import numpy as np


def conv1d(x: np.ndarray, kernel: np.ndarray, mode: str) -> np.ndarray:
    """
    1D cross-correlation ("convolution" in the deep-learning sense: the
    kernel is NOT flipped) with "valid" or "same" zero padding.

    x: shape (n,). kernel: shape (k,), k odd. mode: "valid" or "same".

    "valid": no padding, output length n - k + 1.
    "same": zero-pad x by k // 2 on each side first, output length n.

    Slide the kernel across the (possibly padded) signal without flipping
    it, taking sum(window * kernel) at each position.
    """
    # TODO: build the padded (or unpadded) signal first, then one sliding-window loop.

    n = len(x)
    k = len(kernel)

    if mode == "same":
        pad = k // 2
        signal = np.pad(x, (pad, pad), mode="constant")
    elif mode == "valid":
        signal = x
    else:
        raise ValueError("mode must be 'valid' or 'same'")

    output_length = len(signal) - k + 1
    output = np.empty(output_length, dtype=np.result_type(x, kernel))

    for i in range(output_length):
        window = signal[i:i + k]
        output[i] = np.sum(window * kernel)

    return output
    pass
