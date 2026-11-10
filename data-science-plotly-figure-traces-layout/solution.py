import plotly.graph_objects as go
import plotly.io as pio


def line_figure(x, y, name: str, title: str, xlabel: str, ylabel: str) -> go.Figure:
    """
    A new Figure with ONE Scatter trace through (x, y), mode "lines+markers",
    called `name`; layout title `title`, axis titles `xlabel` and `ylabel`.
    """
    # TODO: Build the trace, put it in a figure, set the layout.

    trace = go.Scatter(
        x=x,
        y=y,
        mode="lines+markers",
        name=name,
    )

    fig = go.Figure(data=[trace])

    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
    )

    return fig


def add_series(fig: go.Figure, x, y, name: str, color: str) -> go.Figure:
    """Add a lines-only Scatter with this name and line colour. Returns the same figure."""
    # TODO: Append one more trace.

    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="lines",
            name=name,
            line=dict(color=color),
        )
    )

    return fig


def trace_summaries(fig: go.Figure) -> list:
    """[{"name": ..., "type": ..., "n_points": ...}, ...], one dict per trace."""
    # TODO: Read each trace back.

    summaries = []

    for trace in fig.data:
        summaries.append({
            "name": trace.name,
            "type": trace.type,
            "n_points": len(trace.x) if trace.x is not None else 0,
        })

    return summaries


def set_axis_ranges(fig: go.Figure, xrange, yrange) -> go.Figure:
    """Fix the visible range of both axes ([low, high] each). Returns the same figure."""
    # TODO: Update both axes.

    fig.update_xaxes(range=xrange)
    fig.update_yaxes(range=yrange)

    return fig


def json_roundtrip(fig: go.Figure) -> go.Figure:
    """Serialise `fig` to JSON and rebuild a NEW figure from the text."""
    # TODO: Use plotly.io.

    json_text = pio.to_json(fig)
    new_fig = pio.from_json(json_text)

    return new_fig
