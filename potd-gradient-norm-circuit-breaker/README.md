# THE GRADIENT-NORM CIRCUIT BREAKER

Intermediate | optimization | gradient-clipping

**Difficulty:** Medium
**Tags:** Optimization, Gradient Clipping, Numerical Stability

---

### Story

A training service clips the entire gradient vector by its L2 norm. An
implementation clips each coordinate independently instead, changing the
gradient's direction. Compute global-norm clipping and return the
clipped vector.

---

### The Math

For gradient `g` (in `R^n`):

```
||g||_2 = sqrt(sum_i g_i^2)
```

For threshold `c > 0`:

```
g_tilde = g                  if ||g||_2 <= c
g_tilde = g * (c / ||g||_2)  if ||g||_2 > c
```

### Input Format

`g` (length `n`), `c`.

### Output Format

The original norm, then the `n` clipped components, 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `0 < c <= 10^6`, `|g_i| <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
g = [3, 4, 12], c = 5
```

**Output**

```
13.000000 1.153846 1.538462 4.615385
```

**Explanation:** The norm is `sqrt(9 + 16 + 144) = 13`, so every component
is scaled by `5 / 13`.
