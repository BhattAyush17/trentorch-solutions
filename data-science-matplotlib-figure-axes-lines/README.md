# Figures, Axes & Line Plots

Beginner | data-science | visualization | matplotlib

### The problem, from first principles

Every matplotlib chart is a small tree of objects. A **Figure** is the canvas. It holds one or more **Axes**, each of which is one plotting area with its own x and y axis. Each Axes holds the things drawn on it: **Line2D** objects for lines, patches for bars, collections for scatter points, **Text** for labels. When you write `plt.plot(...)` you are using a shortcut that quietly creates a Figure and an Axes for you and draws into "the current one". That is fine for a notebook cell and a recipe for confusing bugs in a function that draws more than one chart.

This question uses the _object_ interface, where you hold the Figure and the Axes yourself and call methods on them. Because a chart is a tree of objects with numbers inside, you can read those numbers back, which is also how it is tested: no pixels, just `ax.lines[0].get_ydata()`.

### From theory to code

Implement `line_chart(x, y, title, xlabel, ylabel)`, `add_line(ax, x, y, label, color)`, `line_data(ax)` and `style_line(line, color, linestyle, linewidth, marker)`. The signatures and docstrings are already in the editor.

### Constraints

- Create figures with `plt.subplots()` and draw through the returned `Axes`. Do not call `plt.show()`.
- `line_chart` returns `(fig, ax)`: a new `Figure` with exactly one `Axes` holding exactly one line through the points `(x, y)`, with the given title, x label and y label, and the grid switched on.
- `add_line` draws one more line on `ax` through `(x, y)` with the given `label` and `color`, shows a legend listing the **labelled** lines, and returns the new `Line2D`.
- `line_data(ax)` returns a list with one `(xs, ys)` pair for every line on `ax`, in drawing order, where `xs` and `ys` are Python lists of numbers.
- `style_line(line, color, linestyle, linewidth, marker)` changes those four properties of an existing line (it does not draw a new one) and returns the line.

### Hints

<details>
<summary>Hint 1</summary>

`plt.subplots()` returns a `(figure, axes)` pair. `ax.plot(x, y)` returns a list of lines, so `line, = ax.plot(...)` unpacks the one you made.

</details>

<details>
<summary>Hint 2</summary>

Lines created without a `label` are left out of the legend automatically.

</details>

<details>
<summary>Hint 3</summary>

Every property you can pass to `plot` has a `set_` method on the line: `set_color`, `set_linestyle`, `set_linewidth`, `set_marker`.

</details>
