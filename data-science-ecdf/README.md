# Empirical CDF

Beginner | data-science | visualization | distributions

### The problem, from first principles

A histogram needs a bin width and a box plot throws away shape. The empirical cumulative distribution function, ECDF, needs no tuning at all: for every value on the horizontal axis it shows the fraction of the data at or below that value. It uses every data point, it makes quartiles and percentiles readable straight off the curve, and putting two ECDFs on one plot shows at once whether one sample sits above, below or crosses the other. The largest vertical gap between two ECDFs is itself a statistic, the Kolmogorov-Smirnov distance, which is how a model's score distributions or a feature before and after a shift get compared. This question builds the curve, evaluates it anywhere and measures that gap.

### From theory to code

Implement `ecdf(x)`, the points of the staircase, then `ecdf_at(x, points)`, the curve's height at arbitrary places, then `ks_distance(x, y)`, the largest vertical gap between the ECDFs of two samples. The signatures and docstrings are already in the editor.

### Constraints

- `x` and `y` are 1D float arrays with at least one value.
- `ecdf(x)` returns `(values, probabilities)`: `values` is `x` sorted ascending and `probabilities[i] = (i + 1) / n`, so the last probability is `1.0`. Repeated values each get their own entry.
- `ecdf_at(x, points)` returns a float array with the fraction of entries of `x` that are less than or equal to each point. It works for any array of query points and does not require them to be in `x`.
- `ks_distance(x, y)` returns `max over all t of |F_x(t) - F_y(t)|` as a float, where `F` is the ECDF of each sample. The maximum only needs to be checked at the values that occur in either sample.
- Do not call `scipy`. Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

`np.searchsorted(sorted_x, points, side="right")` counts how many sorted values are less than or equal to each point, which divided by `n` is the ECDF.

</details>

<details>
<summary>Hint 2</summary>

Between two data points the ECDF is flat, and it only jumps at data values. The largest gap between two such step functions therefore happens at one of those jump locations.

</details>

<details>
<summary>Hint 3</summary>

Evaluate both ECDFs at the pooled values from both samples and take the largest absolute difference.

</details>
