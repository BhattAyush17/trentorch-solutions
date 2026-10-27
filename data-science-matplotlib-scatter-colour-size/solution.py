import matplotlib.pyplot as plt
import numpy as np


def scatter_chart(x, y, sizes, values, label: str):
    """
    New figure with one scatter of (x, y): marker areas `sizes`, coloured by
    `values` with the "viridis" colormap, plus a colourbar labelled `label`.
    Returns (fig, ax, points) where points is the scatter collection.
    """
    fig, ax = plt.subplots()

    points = ax.scatter(
        x,
        y,
        s=sizes,
        c=values,
        cmap="viridis",
    )

    colorbar = fig.colorbar(points, ax=ax)
    colorbar.set_label(label)

    return fig, ax, points


def fit_line(ax, x, y):
    """
    Draw the least-squares line as one red segment from min(x) to max(x),
    label "fit". Returns (slope, intercept) as Python floats.
    """
    x = np.asarray(x)
    y = np.asarray(y)

    slope, intercept = np.polyfit(x, y, 1)

    x_min = np.min(x)
    x_max = np.max(x)

    ax.plot(
        [x_min, x_max],
        [slope * x_min + intercept, slope * x_max + intercept],
        color="red",
        label="fit",
    )

    return float(slope), float(intercept)


def highlight_outliers(ax, x, y, k: float) -> int:
    """
    Second scatter (red, area 80) of the points with |y - mean(y)| > k * std(y)
    (population std). Returns how many; draws nothing if there are none.
    """
    x = np.asarray(x)
    y = np.asarray(y)

    mean_y = np.mean(y)
    std_y = np.std(y)

    mask = np.abs(y - mean_y) > k * std_y

    if np.any(mask):
        ax.scatter(
            x[mask],
            y[mask],
            s=80,
            color="red",
        )

    return int(np.sum(mask))
