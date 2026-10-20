# Quantile-Quantile Plots

Intermediate | data-science | visualization | distributions

### The problem, from first principles

Whether a column is normally distributed decides which statistical tests are fair, whether a linear model's errors are well behaved and whether a log transform from `04-skew-transforms` worked. A histogram lets the eye judge bell-shapedness badly. A quantile-quantile plot makes the question a straight-line check: sort the data, pair each sorted value with the value a perfect normal sample would have in the same position, and plot one against the other. If the data is normal the points fall on a line, and the way they bend away from it says exactly how the distribution differs: heavy tails, skew, a flat top. This question builds the numbers behind that plot, including the inverse of the normal CDF that supplies the reference values.

### From theory to code

Implement `normal_ppf(p)`, the value below which a standard normal falls with probability `p`, then `plotting_positions(n)`, the probabilities assigned to the `n` sorted values, then `qq_points(x)`, the two coordinate arrays of the plot, then `qq_line(theoretical, sample)`, the reference line through the quartiles, then `qq_correlation(x)`, one number that summarizes how straight the plot is. The signatures and docstrings are already in the editor.

### Constraints

- `normal_ppf(p)` returns the standard normal quantile of `p` as a float, accurate to at least `1e-9`, for `0 < p < 1`. It raises `ValueError` for any other `p`. Do not use `scipy`. Use `math.erf` and bisection (or another method you write).
- `plotting_positions(n)` returns the array `(i - 0.5) / n` for `i = 1 .. n`.
- `qq_points(x)` returns `(theoretical, sample)`: `sample` is `x` sorted ascending and `theoretical[i] = normal_ppf(plotting_positions(n)[i])`, both 1D float arrays of length `n`.
- `qq_line(theoretical, sample)` returns `(slope, intercept)` of the line through the points at the 25th and 75th percentiles of the two arrays (`np.percentile`, linear interpolation): `slope = (s75 - s25) / (t75 - t25)` and `intercept = s25 - slope * t25`.
- `qq_correlation(x)` returns the Pearson correlation between `theoretical` and `sample` from `qq_points(x)`, as a float.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

The normal CDF is `0.5 * (1 + erf(z / sqrt(2)))` and is strictly increasing, so its inverse can be found by narrowing an interval around the answer, halving it each time.

</details>

<details>
<summary>Hint 2</summary>

The `- 0.5` in the plotting positions keeps the probabilities strictly inside `(0, 1)`, so no sorted value is paired with an infinite quantile.

</details>

<details>
<summary>Hint 3</summary>

If the data is exactly `mean + std * z` for normal `z`, the sample quantiles are a straight function of the theoretical ones, with slope equal to the standard deviation and intercept equal to the mean.

</details>
