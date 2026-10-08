def one_hot_encode(categories: list[str]) -> tuple[list[str], list[list[int]]]:
    """
    One-hot encode a categorical column, alphabetical column order.

    categories: n category strings, may repeat, case-sensitive.

    Return (distinct, rows):
      distinct: the k distinct categories present, sorted alphabetically.
      rows: n rows, each length k, a 1 at the column matching that row's
        category and 0 elsewhere.

    Column order is alphabetical, not order of first appearance. "Wifi" and
    "wifi" are distinct categories: no case normalization.
    """
    # TODO: sorted(set(categories)) gives the alphabetical column order directly.

    distinct = sorted(set(categories))

    index = {category: i for i, category in enumerate(distinct)}

    rows = []

    for category in categories:
        row = [0] * len(distinct)
        row[index[category]] = 1
        rows.append(row)

    return distinct, rows
    pass
