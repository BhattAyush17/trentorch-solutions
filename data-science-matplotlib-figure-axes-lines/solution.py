import matplotlib.pyplot as plt


def line_chart(x, y, title: str, xlabel: str, ylabel: str):
    """
    New Figure with one Axes holding one line through (x, y); title, axis
    labels and grid on. Returns (fig, ax). Do not call plt.show().
    """
    # TODO: Create the figure and axes and draw the line on the axes.
    fig, ax = plt.subplots()

    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)

    return fig, ax
    pass


def add_line(ax, x, y, label: str, color: str):
    """
    Draw another line on `ax` with this label and colour, show a legend (it lists
    labelled lines only) and return the new Line2D.
    """
    # TODO: Plot on the given axes and show the legend.
    line, = ax.plot(x, y, label=label, color=color)
    ax.legend()

    return line
    pass


def line_data(ax) -> list:
    """[(xs, ys), ...] for every line on `ax`, in drawing order; xs, ys are lists."""
    # TODO: Read the data back from the line objects.
    return [
        (line.get_xdata().tolist(), line.get_ydata().tolist())
        for line in ax.get_lines()
    ]
    pass


def style_line(line, color: str, linestyle: str, linewidth: float, marker: str):
    """Change those four properties of an existing line (no new line); return it."""
    # TODO: Use the line's setters.
    line.set_color(color)
    line.set_linestyle(linestyle)
    line.set_linewidth(linewidth)
    line.set_marker(marker)

    return line
    pass
