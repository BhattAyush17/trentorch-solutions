def avg_pool(matrix: list[list[float]], f: int) -> list[list[float]]:
    """
    Downsample a square demand grid with non-overlapping average pooling.
    """
    n = len(matrix)
    m = n // f


    out = []

    for i in range(m):
        row = []

        for j in range(m):
            total = 0.0

            # Sum the f × f patch
            for a in range(f):
                for b in range(f):
                    total += matrix[i * f + a][j * f + b]

            # Divide by total number of cells
            row.append(total / (f * f))

        out.append(row)

    return out
