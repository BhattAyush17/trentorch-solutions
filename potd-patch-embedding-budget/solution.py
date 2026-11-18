from typing import Optional, Tuple


def patch_embedding_budget(
    h: int, w: int, p: int, c: int, d: int
) -> Optional[Tuple[int, int]]:
    """
    h, w: image height and width.
    p: square patch size.
    c: input channel count.
    d: embedding dimension.

    If h is not divisible by p or w is not divisible by p, return None
    (reject rather than floor-divide). Otherwise return (patch_count,
    param_count) where patch_count = (h // p) * (w // p) and
    param_count = p**2 * c * d.
    """
    # TODO: validate divisibility, then compute patch count and params.
    if h % p != 0 or w % p != 0:
        return None

    patch_count = (h // p) * (w // p)
    param_count = p**2 * c * d

    return patch_count, param_count
    pass
