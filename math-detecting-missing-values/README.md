# Detecting and counting missing values in a dataset

Beginner | data-processing

### The problem, from first principles

Real datasets are never as clean as the small, hand-picked arrays this curriculum's Math & Statistics tracks used, a survey respondent skips a question, a sensor drops a reading, a merge between two tables leaves some rows without a match. Before anything else, `03-mse-gradient`, PCA, a Gaussian's MLE, all assume every entry of the data actually holds a real number, a single missing value silently poisons a mean, a covariance, a gradient, everywhere it touches.

The very first, unglamorous step of any real ML pipeline is knowing exactly where the gaps are, before deciding what to do about them (`02-imputing-missing-values`, the next question, is that "what to do about them" step). This question is purely about detection: finding missing entries reliably, a surprisingly easy thing to get subtly wrong.

### From theory to code

Theory names the standard representation for a missing numeric value (`np.nan`) and flags the single most common bug in detecting it (`== np.nan` never works, by design). Implement a boolean mask using the correct tool, then column-wise counts and fractions built directly from that mask.

Implement `missing_mask(x)`, `missing_count_per_column(x)` and `missing_fraction_per_column(x)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 2D float array, `(num_rows, num_columns)`, missing values represented as `np.nan`.
- Use `np.isnan`, never `== np.nan` (Theory explains exactly why the latter silently fails).
- `missing_fraction_per_column` returns fractions in `[0.0, 1.0]`, one per column.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.isnan(x)` already returns a same-shaped boolean mask directly, no comparison operator needed.

</details>

<details>
<summary>Hint 2</summary>

Once you have the mask, `missing_count_per_column` is `.sum(axis=0)` (summing down each column, over all rows).

</details>
