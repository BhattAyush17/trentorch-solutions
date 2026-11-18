# THE AUC PAIR COUNTER

Advanced | evaluation-metrics | ranking | classification

**Difficulty:** Hard
**Tags:** Evaluation Metrics, Ranking, Classification

---

### Story

A binary classifier is evaluated by ROC AUC. The evaluation implementation
sorts scores but mishandles tied positive-negative pairs. Compute AUC using
the pairwise definition, including half credit for ties, in better than
quadratic time.

---

### The Math

For positive scores `s_i^+` and negative scores `s_j^-`:

```
AUC = (1 / (N_+ * N_-)) * sum_i sum_j [ 1(s_i^+ > s_j^-) + 0.5 * 1(s_i^+ == s_j^-) ]
```

If either class is absent, return `0`.

### Input Format

`scores` (length `n`), `labels` (length `n`, binary).

### Output Format

AUC, 6 decimal places.

### Constraints

- `1 <= n <= 2*10^5`, finite scores with `|s_i| <= 10^9`.
- Time limit: 2.0 seconds. A quadratic pairwise implementation is too slow.

---

### Example

**Input**

```
scores = [0.9, 0.8, 0.5, 0.5], labels = [1, 0, 1, 0]
```

**Output**

```
0.625000
```

**Explanation:** There are four positive-negative pairs: the score `0.9`
beats both negatives, the score `0.5` (positive) loses to `0.8` and ties the
other `0.5` (negative) for half credit. AUC is `(2 + 0.5) / 4 = 0.625`.
