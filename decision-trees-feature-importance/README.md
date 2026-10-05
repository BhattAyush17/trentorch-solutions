# Feature importance from a fitted tree

Intermediate | classical-ml | decision-trees | interpretability

### The problem, from first principles

A fitted tree reveals which feature questions reduced label uncertainty, but a feature may appear at several depths. Feature importance collects that evidence into one comparable score per original input feature while giving broad, high-level splits more credit than tiny late branches.

### From theory to code

Implement `feature_importances(tree, input, labels, n_features)`. Re-route the original training data through the stored tree, compute each split's gain, accumulate its sample-weighted credit, and normalize the result.

### Constraints

- `tree` was fit on the supplied `input` and `labels`; `n_features` is the full input width.
- Return shape `(n_features,)`.
- Recreate each node's subsets using its stored feature, threshold, and inclusive left rule.
- Add `(node_labels.size / total_samples) * information_gain(...)` to the split feature.
- Normalize only when the sum is positive; a single leaf returns all zeros.
- Reuse `information_gain` and do not mutate the tree or data.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

The tree stores split decisions, not the data that reached them; carry a data subset through a recursive walk.

</details>

<details><summary>Hint 2</summary>

At a split node, form `left_mask` from that node's feature and threshold, recurse on both masked subsets, and credit the current feature before recursing.

</details>
