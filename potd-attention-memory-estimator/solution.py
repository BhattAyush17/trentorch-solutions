from typing import Tuple


def attention_memory_estimator(
    b: int, h: int, tq: int, tk: int, bytes_per_score: int
) -> Tuple[int, float]:
    """
    b: batch size.
    h: number of attention heads.
    tq: query length.
    tk: key length.
    bytes_per_score: bytes per score element (2, 4, or 8).

    Compute total bytes = b * h * tq * tk * bytes_per_score (exact integer
    product), and mib = bytes / 2**20. Return (bytes, mib).
    """
    # TODO: compute the exact byte count, then convert to MiB (2**20 bytes).
    total_bytes = b * h * tq * tk * bytes_per_score
    mib = total_bytes / (2 ** 20)

    return total_bytes, mib
    pass
