# THE SOFTMAX OVERFLOW INCIDENT

Intermediate | deep-learning | softmax

**Difficulty:** Medium
**Tags:** Deep Learning, Softmax, Numerical Stability

---

### Story

A classifier emits large logits after a mixed-precision refactor. The
naive exponential implementation overflows even though the correct
probabilities are well-defined. Compute stable softmax probabilities for
each supplied row.

---

### The Math

For logits `z_1, ..., z_d`:

```
p_i = exp(z_i) / sum_j exp(z_j)
```

For numerical stability, subtract the row maximum `m = max_j z_j` from
every logit before exponentiating:

```
p_i = exp(z_i - m) / sum_j exp(z_j - m)
```

Rows are independent.

### Input Format

`logits` (`n x d`).

### Output Format

`n` rows of `d` probabilities, 6 decimal places.

### Constraints

- `1 <= n <= 10^4`, `1 <= d <= 1000`, `|z_i| <= 10^4`.
- Time limit: 2.0 seconds. Memory: 128 MB.

---

### Example

**Input**

```
logits = [[1000, 1001, 999], [0, 0, 0]]
```

**Output**

```
0.244728 0.665241 0.090031
0.333333 0.333333 0.333333
```

**Explanation:** Subtracting the row maximum keeps the exponentials
bounded without changing the normalized probabilities.
