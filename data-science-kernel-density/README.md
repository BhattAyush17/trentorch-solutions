# Kernel Density Estimation

Intermediate | data-science | visualization | distributions

### The problem, from first principles

`01-histogram-bins` showed that a histogram's look depends on where its bins start and how wide they are, and its blocky bars are a poor picture of a smooth quantity. Kernel density estimation gives a smooth curve instead. Place a small bump, a kernel, on every data point and add them up: where data is dense the bumps pile up into a high ridge, and where it is sparse the curve is low. One number, the bandwidth, sets how wide each bump is, and it plays the role the bin width played, trading smoothness against detail. This question builds the estimator, a standard rule for choosing the bandwidth and a check that the result is a valid density.

### From theory to code

Implement `gaussian_kde(x, grid, bandwidth)`, which evaluates the density estimate at a set of points, then `silverman_bandwidth(x)`, a rule-of-thumb bandwidth, then `integrate_density(density, grid)`, which uses the trapezoid rule to check that the curve has total area one. The signatures and docstrings are already in the editor.

### Constraints

- `x` is a 1D float array of at least two values and `grid` is a 1D float array of the points at which to evaluate the density. `bandwidth` is a positive float.
- `gaussian_kde` returns an array the shape of `grid` where entry `j` is `mean_i( N(grid[j] - x[i]; 0, bandwidth) )`, the average of Gaussian bumps of standard deviation `bandwidth` centred on every data point. It raises `ValueError` if `bandwidth <= 0`.
- `silverman_bandwidth` returns `0.9 * min(std, IQR / 1.34) * n ** (-1/5)` as a float, where `std` is the sample standard deviation with `ddof=1`, `IQR` is the interquartile range from `np.percentile` and `n = len(x)`. If the minimum of the two spread measures is zero, it uses whichever is nonzero, and `1.0` if both are zero.
- `integrate_density(density, grid)` returns the trapezoid-rule area under the curve as a float, for a strictly increasing `grid`. Do not call `np.trapz` or `np.trapezoid`.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

A Gaussian bump of width `h` centred at `c` has height `exp(-0.5 * ((t - c) / h) ** 2) / (h * sqrt(2 * pi))` at `t`. Averaging one bump per data point keeps the total area at one.

</details>

<details>
<summary>Hint 2</summary>

Build an array of shape `(len(grid), len(x))` of differences with broadcasting, apply the bump formula and average over the data axis.

</details>

<details>
<summary>Hint 3</summary>

The trapezoid rule adds up, for every pair of neighbouring grid points, the gap between them times the average of the two heights.

</details>
