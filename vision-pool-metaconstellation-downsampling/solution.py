def max_pool(matrix: list[list[float]], f: int) -> list[list[float]]:
    """
    Downsample a square feature map with non-overlapping max pooling.
    """
    n = len(matrix)
    m = n // f

    out = []

    for i in range(m):
        row = []

        for j in range(m):
            # Start with the first element of this patch.
            maximum = matrix[i * f][j * f]

            for a in range(f):
                for b in range(f):
                    value = matrix[i * f + a][j * f + b]

                    if value > maximum:
                        maximum = value

            row.append(maximum)

        out.append(row)

    return out
