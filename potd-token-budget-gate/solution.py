def token_budget_gate(p: int, r: int, c: int) -> tuple[int, bool]:
    """
    p: prompt-token count.
    r: requested generation-token count.
    c: context limit.

    r_max = max(0, c - p)
    fits = (p + r <= c)

    Returns (r_max, fits).
    """
    # TODO: compute the remaining budget and whether the request fits,
    # using plain integer arithmetic (no truncation of p or r).
    r_max = max(0, c - p)
    fits = (p + r <= c)

    return r_max, fits
    pass
