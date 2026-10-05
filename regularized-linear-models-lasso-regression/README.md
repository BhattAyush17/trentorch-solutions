# Lasso Regression (L1), contrasted against Ridge

Intermediate | classical-ml | regression

### The problem, from first principles

`Ridge Regression (L2)` shrinks every weight toward zero, but rarely all the way TO zero, a feature that's only weakly useful still ends up with a small, nonzero coefficient. Sometimes what you actually want is different: not just "smaller weights," but genuine feature SELECTION, automatically zeroing out the features that don't matter at all, leaving a sparse, more interpretable model. Swapping Ridge's squared penalty (`sum(weight^2)`) for an absolute-value penalty (`sum(|weight|)`) produces exactly this behavior, and this swap is precisely the difference between Ridge and Lasso.

The cost of that swap: unlike Ridge, Lasso's penalty has no smooth derivative at exactly zero (the whole point, its kink AT zero is what makes weights land exactly there), which means the elegant closed-form Normal-Equation-style solution Ridge enjoys simply doesn't exist for Lasso. A different algorithm, coordinate descent, is needed instead.

### From theory to code

Theory introduces the soft-thresholding operator (the exact solution to a ONE-coordinate version of the Lasso problem), then coordinate descent: repeatedly solve for one weight at a time, holding all others fixed, cycling through every coordinate for several passes until the weights settle.

Implement `soft_threshold(x, threshold)` first, then `lasso_regression_coordinate_descent(input, target, alpha=1.0, epochs=200)` on top of it.

### Constraints

- Center `input` and `target` (subtract their means) before the coordinate descent loop; recover the bias afterward, don't penalize it directly.
- `soft_threshold` must produce EXACT zeros for inputs within `threshold` of zero, not just small values.
- Return `(weight, bias)` in the same `(1, in_features)`/`(1,)` shapes the other regression questions use.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`soft_threshold(x, t) = np.sign(x) * np.maximum(np.abs(x) - t, 0.0)`, a direct translation of the formula.

</details>

<details>
<summary>Hint 2</summary>

For each coordinate `j`, compute the PARTIAL residual (target minus the prediction from every OTHER coordinate), correlate it with feature `j`, and soft-threshold that correlation by `alpha` to get the new `weight[j]`.

</details>
