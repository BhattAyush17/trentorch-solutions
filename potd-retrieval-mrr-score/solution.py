from typing import List


def retrieval_mrr_score(rankings: List[List[int]]) -> float:
    """
    rankings: list of queries, each a list of 0/1 relevance labels in
    rank order (rank 1 is index 0).

    For each query, find the first relevant result's 1-indexed rank j
    and its reciprocal rank 1/j; if none, reciprocal rank is 0. Return
    the mean reciprocal rank over all queries.
    """
    # TODO: compute each query's reciprocal rank, then average over all queries.
    if not rankings:
        return 0.0

    reciprocal_ranks = []

    for ranking in rankings:
        reciprocal_rank = 0.0

        for index, relevance in enumerate(ranking, start=1):
            if relevance == 1:
                reciprocal_rank = 1.0 / index
                break

        reciprocal_ranks.append(reciprocal_rank)

    return sum(reciprocal_ranks) / len(rankings)
    pass
