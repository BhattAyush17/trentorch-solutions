import matplotlib.pyplot as plt
import numpy as np


def bar_chart(labels: list, values: list):
    """
    Bars centred at 0..n-1 (width 0.8), ticks at 0..n-1 labelled with `labels`,
    y axis starting at 0. Returns (fig, ax).
    """
    # TODO: Draw the bars at numeric positions, then label the ticks.
    
    positions = np.arange(len(labels))

    fig, ax = plt.subplots()
    ax.bar(positions, values, width=0.8)

    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_ylim(bottom=0)

    return fig, ax
    pass


def grouped_bars(labels: list, series: dict):
    """
    k series side by side per category: width 0.8/k, series j offset by
    (j - (k - 1) / 2) * width. Ticks 0..n-1 with labels; legend of series names.
    Returns (fig, ax).
    """
    # TODO: Offset each series within its group.
    positions = np.arange(len(labels))
    k = len(series)
    width = 0.8 / k

    fig, ax = plt.subplots()

    for j, (name, values) in enumerate(series.items()):
        offset = (j - (k - 1) / 2) * width
        ax.bar(positions + offset, values, width=width, label=name)

    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.legend()

    return fig, ax
    pass


def stacked_bars(labels: list, series: dict):
    """
    Bars of width 0.6 at 0..n-1; each series starts where the previous ones
    end. Ticks 0..n-1 with labels; legend of series names. Returns (fig, ax).
    """
    # TODO: Track the running bottom.
    positions = np.arange(len(labels))
    bottom = np.zeros(len(labels))

    fig, ax = plt.subplots()

    for name, values in series.items():
        ax.bar(
            positions,
            values,
            width=0.6,
            bottom=bottom,
            label=name,
        )
        bottom += np.asarray(values)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.legend()

    return fig, ax
    pass


def annotate_bars(ax) -> list:
    """
    Write each bar's height (f"{height:g}") centred above its top, and return
    those strings in ax.patches order.
    """
    # TODO: Add a text label to every patch.
    labels = []

    for patch in ax.patches:
        height = patch.get_height()
        text = f"{height:g}"

        ax.text(
            patch.get_x() + patch.get_width() / 2,
            patch.get_y() + height,
            text,
            ha="center",
            va="bottom",
        )

        labels.append(text)

    return labels
    pass
