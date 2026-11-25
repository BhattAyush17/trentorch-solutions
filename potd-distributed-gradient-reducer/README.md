# THE DISTRIBUTED GRADIENT REDUCER

Advanced | distributed-training | gradient-reduction | weighted-means

**Difficulty:** Hard
**Tags:** Distributed Training, Gradient Reduction, Weighted Means

---

### Story

Workers process different numbers of examples before synchronizing
gradients. Averaging worker-local mean gradients equally biases the
global update when worker batch sizes differ. Compute the
example-weighted gradient and one SGD update.

---

### The Math

Worker `i` contributes batch size `n_i` and mean gradient vector `g_i`.
The global mean gradient is:

```
g = sum_i(n_i * g_i) / sum_i(n_i)
```

For parameter vector `theta` and learning rate `eta`, update each
coordinate:

```
theta_j' = theta_j - eta * g_j
```

### Input Format

`theta` (parameter vector), `eta`, `workers`, a list of `(n_i,
gradient_i)` pairs.

### Output Format

`(global_gradient, updated_theta)`, both to 6 decimal places.

### Constraints

- `1 <= k <= 10^4` workers, `1 <= d <= 100`, `1 <= n_i <= 10^6`.
- Gradient and parameter magnitudes at most `10^4`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
theta = [1, 2], eta = 0.1
workers = [(1, [1, 3]), (3, [3, 1])]
```

**Output**

```
([2.500000, 1.500000], [0.750000, 1.850000])
```

**Explanation:** The weighted gradient is `(1*1 + 3*3)/4 = 2.5` and
`(1*3 + 3*1)/4 = 1.5`. Subtracting `0.1 * g` from `theta` gives the
updated parameters.
