# Figures, Traces & Layout

Beginner | data-science | visualization | plotly

### The problem, from first principles

Plotly draws in a browser, so a plotly figure is not a picture. It is a **description**: a plain structure, a list of `data` (the _traces_, each one a scatter, a bar, a heatmap) and a `layout` (titles, axes, legend, size), which the plotly.js library in the browser turns into pixels. That is why a figure can be saved as JSON, sent anywhere, and rebuilt, and why it is interactive for free: hover, zoom and toggling a trace in the legend are plotly.js features working from the description.

The consequence for code is pleasant: building a figure is building a structure, and every property is addressable by a path like `fig.layout.xaxis.title.text`. This question builds a figure from scratch with `plotly.graph_objects`, adds a second trace, reads the structure back, sets axis ranges, and round-trips the whole figure through JSON.

### From theory to code

Implement `line_figure(x, y, name, title, xlabel, ylabel)`, `add_series(fig, x, y, name, color)`, `trace_summaries(fig)`, `set_axis_ranges(fig, xrange, yrange)` and `json_roundtrip(fig)`. The signatures and docstrings are already in the editor.

### Constraints

- Use `plotly.graph_objects` (`import plotly.graph_objects as go`). Do not call `fig.show()`.
- `line_figure` returns a new `go.Figure` with **one** `Scatter` trace through `(x, y)` drawn with `mode="lines+markers"` and the given `name`, with the layout title `title`, x axis title `xlabel` and y axis title `ylabel`.
- `add_series(fig, x, y, name, color)` adds one more `Scatter` trace (lines only, `mode="lines"`) to `fig` with that `name` and line colour, and returns the **same** figure object.
- `trace_summaries(fig)` returns a list with one dict per trace, in order: `{"name": ..., "type": ..., "n_points": ...}`, where `type` is the trace type (such as `"scatter"`) and `n_points` is the number of `x` values.
- `set_axis_ranges(fig, xrange, yrange)` fixes the visible range of the x axis and of the y axis (each a `[low, high]` pair) and returns the same figure.
- `json_roundtrip(fig)` serialises the figure to a JSON string and rebuilds a **new** figure from it with `plotly.io`, which it returns.

### Hints

<details>
<summary>Hint 1</summary>

`go.Figure(data=[go.Scatter(...)])` builds a figure; `fig.update_layout(title=..., xaxis_title=..., yaxis_title=...)` sets the layout; `fig.add_trace(...)` appends a trace.

</details>

<details>
<summary>Hint 2</summary>

`fig.update_xaxes(range=[...])` and `fig.update_yaxes(range=[...])` set axis ranges.

</details>

<details>
<summary>Hint 3</summary>

`plotly.io.to_json(fig)` and `plotly.io.from_json(text)` are a matched pair.

</details>
