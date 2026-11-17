# THE LOG-SUM-EXP GUARD

Intermediate | numerical-stability | probability | loss-functions

**Difficulty:** Medium
**Tags:** Numerical Stability, Probability, Loss Functions

---

### Story

A probabilistic model computes a log partition function. Directly exponentiating
large scores overflows, so the stable log-sum-exp trick (subtracting the max
before exponentiating) must be used instead.

---

### The Math

For scores `x_1, ..., x_n`:

```
LSE(x) = log(sum_i e^{x_i}) = m + log(sum_i e^{x_i - m}),  m = max_i x_i
```

### Input Format

`scores` (length `n`).

### Output Format

`LSE(x)`, 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `|x_i| <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
scores = [1000, 1001, 999]
```

**Output**

```
1001.407606
```

**Explanation:** The result is `1001 + log(1 + e^-1 + e^-2)`.
