# Information Gain for a split

Beginner | classical-ml | decision-trees | splitting-criteria

### The problem, from first principles

Once a node is mixed, a tree must compare proposed partitions. A useful split leaves its children more label-consistent than their parent; a useless split merely moves the same mixture around. Information gain measures that reduction while ensuring a tiny child cannot count as much as a large one.

### From theory to code

Implement `information_gain(parent_labels, left_labels, right_labels)` using the existing `gini_impurity` helper and a child-size-weighted average.

### Constraints

- `left_labels` and `right_labels` partition `parent_labels`.
- Return a Python `float` gain.
- Weight each child impurity by its size divided by `parent_labels.size`.
- Empty children remain valid because `gini_impurity` returns `0.0` for them.
- Reuse `gini_impurity`; do not reimplement its class counting.

### Hints

Open one at a time. Each gives away a little more than the last.

<details><summary>Hint 1</summary>

Start from the parent's impurity, then ask what impurity remains after routing samples into children.

</details>

<details><summary>Hint 2</summary>

The remaining impurity is not an even average: multiply each child's impurity by `child.size / parent.size` first.

</details>
