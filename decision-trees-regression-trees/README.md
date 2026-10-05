# Regression trees: splitting on variance reduction instead of Gini

Intermediate | classical-ml | decision-trees | regression

### The problem, from first principles

Classification trees group labels; regression trees group real-valued targets. A good numeric leaf is one whose targets can be represented by a single useful number, so this version measures spread rather than class mixing. The split search and recursion stay familiar, but leaves must predict means and predictions must remain floating-point values.

### From theory to code

Implement `variance`, `variance_reduction`, `find_best_regression_split`, `build_regression_tree`, and `predict_regression_tree`. Theory translates each classification-tree operation into its continuous-target counterpart.

### Constraints

- `targets` are real-valued; empty `targets` have variance `0.0`.
- Weight child variances by their sample counts when computing reduction.
- Search every feature's adjacent-unique-value midpoint and return `None` without a positive reduction.
- Stop building at depth zero, fewer than two targets, zero variance, or no valid split.
- A leaf stores `float(np.mean(targets))`, never a class vote.
- Return a float prediction array and traverse each row using the stored inclusive threshold.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Everything about candidate thresholds is the same as the classification tree; only the node-quality measure changes.

</details>

<details><summary>Hint 2</summary>

`np.var` gives the population variance required here. For an empty input, return before calling it.

</details>
