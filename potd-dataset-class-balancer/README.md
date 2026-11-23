# THE DATASET CLASS BALANCER

Intermediate | data-science | sampling | imbalanced-data

**Difficulty:** Medium
**Tags:** Data Science, Sampling, Imbalanced Data

---

### Story

A training pipeline computes inverse-frequency class weights to counteract
an imbalanced dataset. A bug divides by the number of classes instead of
the number of examples, scaling the loss incorrectly.

---

### The Math

For `N` examples across `C` classes, with class count `n_c > 0`:

```
w_c = N / (C * n_c)
```

If a class has zero examples, its weight is defined as `0`.

### Input Format

`counts`, a length-`C` list of non-negative class counts whose sum is `N`.

### Output Format

A length-`C` list of weights, each to 6 decimal places.

### Constraints

- `1 <= C <= 10^5`, `0 <= N <= 10^9`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
counts = [5, 3, 2]
```

**Output**

```
[0.666667, 1.111111, 1.666667]
```

**Explanation:** `N = 10`, `C = 3`, so `N/C = 10/3`; dividing by each class
count gives `10/3/5 = 0.666667`, `10/3/3 = 1.111111`, `10/3/2 = 1.666667`.
