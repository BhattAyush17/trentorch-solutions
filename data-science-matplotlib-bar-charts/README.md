# Bar Charts: Simple, Grouped & Stacked

Intermediate | data-science | visualization | matplotlib | bar

### The problem, from first principles

A bar chart compares quantities across categories, and it is the chart most often drawn wrongly. Matplotlib does not know that your x values are categories: it places each bar at a numeric **position** (0, 1, 2, ...) and you then tell it what text to print under each position. A _grouped_ chart puts several bars side by side inside one category, so each bar's position has to be shifted by hand. A _stacked_ chart puts bars on top of each other, so each bar needs to know where the one below it ends.

The geometry is simple but unforgiving, and since every bar is a `Rectangle` with an `x`, a `width`, a `y` (its bottom) and a `height`, you can check every one of them. This question builds the three charts and the labelling step that puts each value on top of its bar.

### From theory to code

Implement `bar_chart(labels, values)`, `grouped_bars(labels, series)`, `stacked_bars(labels, series)` and `annotate_bars(ax)`. The signatures and docstrings are already in the editor.

### Constraints

- `labels` is a list of `n` category names; `values` and each list in `series` have `n` non-negative numbers. `series` is a dict mapping a series name to its list of `n` values; iterate it in insertion order.
- `bar_chart(labels, values)` returns `(fig, ax)`: bars **centred at positions `0..n-1`**, each of width `0.8` (the default), x tick positions `0..n-1` labelled with `labels`, and the bottom of the y axis at `0`.
- `grouped_bars(labels, series)` returns `(fig, ax)`. With `k` series, each bar has width `0.8 / k`. Bar `j` of group `i` is centred at `i + (j - (k - 1) / 2) * width`. Ticks are at `0..n-1` labelled with `labels`. The legend lists the series names.
- `stacked_bars(labels, series)` returns `(fig, ax)`. Every series draws bars of width `0.6` centred at `0..n-1`; the bar of series `j` starts (`y`) where the bars of the series before it end. Ticks and legend as above.
- `annotate_bars(ax)` writes the height of every bar (`ax.patches`) as text, formatted with `f"{height:g}"`, centred horizontally above the top of that bar (`y + height`), and returns the list of those strings in the order of `ax.patches`.

### Hints

<details>
<summary>Hint 1</summary>

`ax.bar(x, height, width=..., bottom=...)` takes numeric positions. Tick labels are a separate step: `set_xticks` then `set_xticklabels`.

</details>

<details>
<summary>Hint 2</summary>

For grouped bars, the offset of series `j` from the group centre is `(j - (k - 1) / 2) * width`, which centres the whole group on its tick.

</details>

<details>
<summary>Hint 3</summary>

For stacked bars, keep a running array of bottoms and add each series' values to it after drawing.

</details>
