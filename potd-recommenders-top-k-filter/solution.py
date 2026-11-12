def recommenders_top_k_filter(ids: list[int], scores: list[float], k: int) -> list[int]:
    """
    ids: unique candidate IDs.
    scores: scores[i] is the score for ids[i].
    k: number of top candidates to return.

    Sort by descending score, breaking ties by ascending ID. Return the
    first k IDs in that order.
    """
    # TODO: sort by (-score, id), then take the first k IDs.
    ranked = sorted(
        zip(ids, scores),
        key=lambda item: (-item[1], item[0])
    )

    return [item[0] for item in ranked[:k]]
    pass
