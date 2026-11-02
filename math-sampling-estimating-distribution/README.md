# Sampling & Estimating Distributions

Beginner | probability

### The problem, from first principles

Every weight in a freshly-created neural network starts at a random value, drawn from some chosen distribution (a later question in Deep Learning: Training covers exactly which one, and why). Every dropout mask, every data augmentation, every train/test split shuffle, all of it is sampling: producing concrete numbers from a distribution you never see directly, only through the numbers it happens to hand you.

You can't inspect a distribution's true shape directly, you only ever get to see samples FROM it. So the practical skill this question builds is: draw samples reproducibly, then reconstruct an approximate picture of the distribution those samples came from, purely from the numbers themselves.

### From theory to code

Theory names the tool for reproducible sampling (a seeded random generator, not global mutable random state) and the tool for approximating a distribution's shape from samples (a histogram: bucket values into bins, count how many land in each).

Implement `sample_normal(mean, std, size, seed=None)` and `empirical_histogram(samples, bins=10)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- Use `np.random.default_rng(seed)`, not the legacy `np.random.seed`/`np.random.normal` global-state functions.
- The same `seed` must always produce the same samples (reproducibility is the entire point).
- `empirical_histogram` returns `(counts, bin_edges)`, matching `np.histogram`'s own return shape.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.random.default_rng(seed)` returns a generator object. Call `.normal(...)` on that object, not on the `np.random` module directly.

</details>

<details>
<summary>Hint 2</summary>

`np.histogram` already does exactly the counting-into-buckets work this question describes, in one call.

</details>
