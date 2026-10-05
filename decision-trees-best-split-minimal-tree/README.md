# Decision Tree best split (assemble a minimal tree)

Advanced | classical-ml | decision-trees | tree-building

### The problem, from first principles

`01-gini-impurity` scores a node and `02-information-gain` scores one proposed split. A usable tree must search all meaningful splits, choose the strongest improving one, then repeat independently on the two groups it creates. It also needs clear stopping rules so it does not keep memorizing smaller and smaller groups.

### From theory to code

Implement `find_best_split`, `build_tree`, and `predict_tree`. Theory maps candidate midpoints to the gain search, the recursive nested-dictionary representation, and the traversal rule used at inference.

### Constraints

- `input` is `(n_samples, n_features)` and `labels` is `(n_samples,)`.
- Search each feature's midpoints between consecutive unique values; use `<= threshold` for the left child.
- Return `(feature, threshold, gain)` only for a strictly positive best gain; otherwise return `None`.
- Stop recursion at `max_depth == 0`, fewer than two labels, a pure node, or no improving split.
- Leaves use the majority class; split nodes contain `feature`, `threshold`, `left`, and `right`.
- `predict_tree` returns an integer label per input row; tree construction and prediction may loop because they follow data-dependent branches.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Only a boundary between two distinct observed feature values can change which samples reach each child.

</details>

<details><summary>Hint 2</summary>

Initialize the best gain to `0.0`; update all three best-split fields only when a candidate is strictly better.

</details>

<details><summary>Hint 3</summary>

At a leaf, return the label whose count is largest. At a split, reuse its stored feature and threshold to create the two recursive calls and later to route a prediction.

</details>
