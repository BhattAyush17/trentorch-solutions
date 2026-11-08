# THE ROC THRESHOLD AUDIT

Intermediate | classification | evaluation-metrics

**Difficulty:** Medium
**Tags:** Classification, Evaluation Metrics, Thresholding

---

### Story

A fraud team chooses a decision threshold from predicted probabilities. The
monitoring job must count true positives, false positives, true negatives,
and false negatives without treating a score equal to the threshold
inconsistently.

---

### The Math

Predict positive iff `p_i >= tau`. For binary label `y_i`, compute `TP`,
`FP`, `TN`, `FN`. Then:

```
precision = TP / (TP + FP)
recall = TP / (TP + FN)
```

If a denominator is zero, define that metric as `0`.

### Input Format

`probs` (length `n`), `labels` (length `n`, 0/1), `tau`.

### Output Format

`(TP, FP, TN, FN)`, then `(precision, recall)` to 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `0 <= p_i, tau <= 1`, `y_i` in `{0, 1}`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
probs = [0.5, 0.2, 0.9, 0.7], labels = [1, 0, 1, 0], tau = 0.5
```

**Output**

```
2 1 1 0
0.666667 1.000000
```

**Explanation:** A score exactly equal to tau (`0.5`) counts as a predicted
positive, so the first example is a true positive.
