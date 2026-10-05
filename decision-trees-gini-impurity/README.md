# Gini Impurity for a split

Beginner | classical-ml | decision-trees | splitting-criteria

### The problem, from first principles

A tree needs a way to tell whether the labels arriving at a node agree. Pure nodes need no more splitting; mixed nodes may benefit from it. Gini impurity summarizes that label mixture without assuming class labels are consecutive integers.

### From theory to code

Implement `gini_impurity(labels)` by counting each distinct label, converting counts to proportions, and applying the impurity formula. Theory also defines the empty-node convention used by later split logic.

### Constraints

- `labels` is a one-dimensional array of arbitrary integer class labels.
- Return a Python `float` in `[0, 1)`.
- Return exactly `0.0` for an empty array and for a pure node.
- Count distinct labels with `np.unique(..., return_counts=True)`.
- Use vectorized NumPy reductions; do not loop through labels.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Only class frequencies matter; label values such as `5` and `7` are no different from `0` and `1`.

</details>

<details><summary>Hint 2</summary>

Divide counts by `labels.size`, square every proportion, sum them, then subtract from one.

</details>
