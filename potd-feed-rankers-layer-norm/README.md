# THE FEED RANKER'S LAYER NORM

Intermediate | deep-learning | normalization

**Difficulty:** Medium
**Tags:** Deep Learning, Layer Normalization, Numerical Stability

---

### Story

A feed-ranking transformer processes user and item features with wildly
different scales. Its layer-normalization kernel must normalize each
token's feature vector independently, using population variance and a
small epsilon.

---

### The Math

For a feature vector `x` of length `d`:

```
mu = mean(x)
v  = mean((x - mu)^2)       (population variance, divide by d not d-1)
xhat_i = (x_i - mu) / sqrt(v + eps)
```

Use the supplied `eps > 0`. There are no learnable scale or bias
parameters.

### Input Format

`x` (length `d`), `eps`.

### Output Format

The `d` normalized values, 6 decimal places.

### Constraints

- `1 <= d <= 10^5`, `10^-12 <= eps <= 1`, `|x_i| <= 10^6`.
- Time limit: 1.0 second. Memory: 64 MB.

---

### Example

**Input**

```
x = [1, 2, 3], eps = 0.000001
```

**Output**

```
-1.224744 0.000000 1.224744
```

**Explanation:** The mean is `2`, population variance is `2/3`, and the
epsilon-adjusted standard deviation is `sqrt(2/3 + 1e-6)`.
