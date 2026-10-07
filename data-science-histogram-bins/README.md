# Histogram Bins

Beginner | data-science | visualization | distributions

### The problem, from first principles

A histogram is the first plot anyone draws of a numeric column, and everything it shows depends on a choice made before any ink is spent: how wide the bins are. Too few bins and a two-humped distribution looks like one hump. Too many and the picture is a comb of single-row spikes that shows noise instead of shape. A chart is a drawing of numbers, so what can be tested is the numbers behind it: the bin edges and the count in each bin. This question builds both, and two standard rules for choosing how many bins there should be.

### From theory to code

Implement `sturges_bins(n)`, the bin count from Sturges' rule, then `freedman_diaconis_bins(x)`, the bin count from the Freedman-Diaconis rule, then `bin_edges(x, n_bins)`, the equal-width edges spanning the data, then `histogram_counts(x, edges)`, how many values fall in each bin. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 1D float array with at least two values and at least two distinct values. `n` is the number of values.
- `sturges_bins(n)` returns `ceil(log2(n)) + 1` as an int, for `n >= 1`.
- `freedman_diaconis_bins(x)` uses bin width `2 * IQR / n ** (1/3)`, where `IQR` is the difference between the 75th and 25th percentiles (linear interpolation, as `np.percentile` does by default). It returns `ceil((max - min) / width)` as an int, and at least `1`. If the IQR is zero it falls back to `sturges_bins(len(x))`.
- `bin_edges(x, n_bins)` returns `n_bins + 1` equally spaced edges from `min(x)` to `max(x)` inclusive.
- `histogram_counts(x, edges)` returns an integer array of length `len(edges) - 1`. A value `v` belongs to bin `i` when `edges[i] <= v < edges[i + 1]`, except that the last bin is closed on the right, so `v == edges[-1]` counts in the last bin. Values outside `[edges[0], edges[-1]]` are ignored. Do not call `np.histogram`.

### Hints

<details>
<summary>Hint 1</summary>

The edges split the range into pieces of equal width, so `np.linspace` gives them. The half-open rule means a value sitting exactly on an inner edge goes to the bin on its right.

</details>

<details>
<summary>Hint 2</summary>

`np.searchsorted(edges, x, side="right") - 1` gives the bin index of every value in one step. The maximum value then needs to be moved from the nonexistent bin past the end into the last bin.

</details>

<details>
<summary>Hint 3</summary>

Freedman-Diaconis uses the IQR instead of the standard deviation, so a few extreme values do not stretch the bins.

</details>
