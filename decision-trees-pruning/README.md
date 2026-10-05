# Pruning (pre-pruning, post-pruning)

Intermediate | classical-ml | decision-trees | regularization

### The problem, from first principles

Growing every positive-gain split can create branches that memorize a few training examples. Pre-pruning rejects suspiciously small children while building; post-pruning removes branches that do not earn their complexity on held-out data. This exercise implements both controls around the tree from `03-best-split-minimal-tree`.

### From theory to code

Implement `build_tree_pre_pruned` and `prune_tree`. Theory explains the extra child-size condition and the bottom-up comparison between a recursively pruned subtree and one fallback leaf.

### Constraints

- `build_tree_pre_pruned` follows the previous tree's depth, sample-count, purity, and no-split stop rules.
- Reject a candidate split when either child has fewer than `min_samples_leaf` samples.
- Every returned node stores the training-label majority class in `default`.
- `prune_tree` returns a new tree and never mutates its `tree` argument.
- Route validation data by each node's stored `feature` and inclusive `threshold` before recursing.
- Replace a subtree when the fallback leaf's validation error is less than or equal to the subtree error; use `default` if no validation label reaches a node.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Compute the node's majority class before any early return: both leaves and split nodes need it.

</details>

<details><summary>Hint 2</summary>

Prune children first. Only then does a parent compare its best already-pruned subtree with one leaf.

</details>
