# Expectation, Variance & Covariance

Intermediate | probability | foundations

### The problem, from first principles

**Summary statistics as operators**

`01-random-variables` already introduced `E[X]` as a weighted sum over a PMF. This question completes the trio of summary statistics that describe a distribution's _shape_, expectation (where its center of mass is), variance (how spread out it is), and covariance (how two variables move together), defined here as **operators on the population-level distribution itself**, not estimated from a finite sample. This distinction matters: the Bayesian Inference track's existing "expectation and variance from a sample" question computes an _estimator_ of these quantities from observed data; this question defines what that estimator is actually trying to estimate. Every loss function that's "the expected value of something" (expected reward in RL, expected negative log-likelihood in supervised learning) is built directly on this `E[\cdot]` operator.

**From a sample**

"What's the average test score" and "how spread out were the scores" are two different questions about the same list of numbers, and they're both estimates: you're using the students who actually took the test to guess something about "students in general," a quantity you can never observe directly. The average of your actual data is your best guess at the expectation; how far the data typically strays from that average is your best guess at the variance.

The subtlety worth catching early: there are two slightly different ways to compute "typical spread" from a sample, and using the wrong one for the wrong purpose silently biases every downstream calculation that depends on it, standard errors, confidence intervals, t-tests, all built later in this curriculum.

**Covariance & correlation**

Do people who spend more time studying tend to score higher on tests? Answering that isn't about either variable alone, `05-expectation-covariance`'s mean and variance describe study time and test scores separately, it's about whether they move together: when study time is above its own average, is score usually above its own average too? Covariance is the number that answers exactly that question, and correlation is the same idea, rescaled so its size doesn't depend on which units you happened to measure in (hours vs minutes, percent vs raw score).

This exact computation, "do these two variables move together," is what a covariance matrix full of, one entry per pair of features, and PCA (later, in Unsupervised Learning) literally finds its most informative directions by eigendecomposing exactly that matrix.

### From theory to code

**Summary statistics as operators**

Implement `expectation(values, probabilities)`, `variance(values, probabilities)`, and `pmf_covariance(x_values, y_values, joint_probabilities)`. The signatures and docstrings are already in the editor.

**From a sample**

Theory gives the mean as a direct average, and variance as average squared deviation from that mean, with one adjustable parameter (`ddof`) controlling which of the two standard divisors gets used.

Implement `sample_mean(x)` and `sample_variance(x, ddof=0)` against that reasoning. The signatures and docstrings are already in the editor.

**Covariance & correlation**

Theory defines covariance as the average product of each variable's deviation from its own mean, and correlation as covariance divided by both variables' standard deviations. Implement covariance first (reusing the same `ddof` convention `05-expectation-covariance` established), then correlation directly in terms of it.

Implement `covariance(x, y, ddof=0)` and `correlation(x, y)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

**Summary statistics as operators**

- `values`, `probabilities`, `x_values`, `y_values` are 1D array-likes; `probabilities` sums to 1.
- `joint_probabilities` is a 2D array-like where `joint_probabilities[i, j] = P(X=x_values[i], Y=y_values[j])`.
- Implement `variance` using `expectation` rather than duplicating its summation logic.

**From a sample**

- `x` is a 1D array of numeric samples.
- `sample_variance` must respect `ddof`: `ddof=0` divides by `n`, `ddof=1` divides by `n-1`.
- Both functions return a plain Python `float`.

**Covariance & correlation**

- `x` and `y` are 1D arrays of the same length.
- `covariance(x, x, ddof)` must equal `05-expectation-covariance`'s `sample_variance(x, ddof)`, they're the same formula with `y` set to `x`.
- `correlation`'s result must always fall in `[-1, 1]` (up to floating-point tolerance).

### Hints

**Summary statistics as operators**

<details>
<summary>Hint 1</summary>

`expectation` is the same weighted sum from `01-random-variables`: `np.sum(values * probabilities)`.

</details>

<details>
<summary>Hint 2</summary>

`variance` calls `expectation` to get the mean, then computes `np.sum(probabilities * (values - mean)**2)`, the probability-weighted average squared distance from that mean.

</details>

<details>
<summary>Hint 3</summary>

`pmf_covariance` needs each variable's own marginal first (`joint_probabilities.sum(axis=1)` for X, `axis=0` for Y, exactly as in `03-joint-independence`) to get `mean_x` and `mean_y`, then sums `joint_probabilities[i,j] * (x_i - mean_x) * (y_j - mean_y)` over every `(i, j)` pair.

</details>

**From a sample**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.mean` and `np.var` already exist and already accept a `ddof` argument, you are wrapping them, not deriving the formulas from a loop.

</details>

<details>
<summary>Hint 2</summary>

Don't hardcode `ddof=0` inside your implementation, pass the parameter straight through to `np.var`.

</details>

**Covariance & correlation**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Covariance is `mean((x - mean(x)) * (y - mean(y)))`, with the same `n` vs `n-ddof` divisor choice `05-expectation-covariance` uses.

</details>

<details>
<summary>Hint 2</summary>

`correlation` doesn't need its own formula from scratch, it's `covariance(x, y)` divided by `np.std(x) * np.std(y)`.

</details>
