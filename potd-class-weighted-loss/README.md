# THE CLASS-WEIGHTED LOSS

Intermediate | deep-learning | cross-entropy

**Difficulty:** Medium
**Tags:** Deep Learning, Multiclass Classification, Cross-Entropy

---

### Story

A product classifier trains on imbalanced categories. Each example has a
class-specific weight. The implementation must compute mean weighted
negative log likelihood with the reduction convention explicitly defined
by the training team.

---

### The Math

For each example `i`, logits `z_i` (length `C`), true class `y_i`, and
class weight `w_{y_i}`:

```
p_ic = softmax(z_i)_c
L = -(1/n) * sum_i w_{y_i} * log(p_i,y_i)
```

Do not divide by the sum of class weights; divide by `n`.

### Input Format

`logits` (`n x C`), `labels` (length `n`, 0-based), `weights` (length
`C`).

### Output Format

The scalar loss, 6 decimal places.

### Constraints

- `1 <= n <= 10^4`, `2 <= C <= 100`, `|z_ic| <= 10^3`, `0 <= w_c <= 100`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
logits = [[2, 0], [0, 2]], labels = [0, 1], weights = [1, 3]
```

**Output**

```
0.253856
```

**Explanation:** Each row's unweighted negative log-likelihood is
`log(1 + e^-2) ~= 0.126928`. The class weights are 1 and 3, so the mean
weighted loss is `(0.126928 + 3*0.126928) / 2 ~= 0.253856`.
