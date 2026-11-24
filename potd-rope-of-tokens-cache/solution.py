from typing import List, Tuple


def rope_of_tokens_cache(
    queries: List[Tuple[int, int, int, int]]
) -> List[Tuple[int, int]]:
    """
    queries: list of (B, T, W, C) tuples.
        B: concurrent sequences.
        T: total generated-plus-prompt length.
        W: sliding window size.
        C: per-token cache cost in bytes (all layers, K and V included).

    For each query compute r = min(T, W) and m = B * C * r. Return a list
    of (r, m) tuples, one per query, in the same order.
    """
    # TODO: for each query, take the min before multiplying.
    results = []
    for B, T, W, C in queries:
        r= min(T,W)
        m= B* C*r
            
        results.append((r, m))
    return results
    pass
