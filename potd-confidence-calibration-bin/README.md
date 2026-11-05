# THE CONFIDENCE-CALIBRATION BIN

Intermediate | model-evaluation | calibration

**Difficulty:** Medium
**Tags:** Model Evaluation, Calibration, Statistics

---

### Story

A risk model's calibration dashboard groups predicted probabilities into
equal-width bins. Boundary handling must be consistent: each bin
includes its left edge and excludes its right edge, except the final
bin, which also includes `1`.

---

### The Math

For `K` bins and probability `p` in `[0, 1]`, assign:

```
b(p) = min(K - 1, floor(K * p))
```

For each nonempty bin, compute the mean predicted probability and the
empirical positive rate. For empty bins, output `0` for both.

### Input Format

`probs` (length `n`), `labels` (length `n`, 0/1), `K`.

### Output Format

`K` rows of `(count, mean_prob, positive_rate)`, metrics to 6 decimal
places.

### Constraints

- `1 <= n <= 10^5`, `1 <= K <= 1000`, `p` in `[0, 1]`, labels binary.
- Time limit: 1.0 second.

---

### Example

**Input**

```
probs = [0.0, 0.5, 1.0], labels = [0, 1, 1], K = 2
```

**Output**

```
1 0.000000 0.000000
2 0.750000 1.000000
```

**Explanation:** Probability `0.5` belongs to the second bin, and
probability `1.0` is explicitly clamped into the final bin.
