# THE DELIVERY-TIME REGRESSOR

Intermediate | classical-ml | linear-algebra

**Difficulty:** Medium
**Tags:** Classical ML, Linear Algebra, Least Squares

---

### Story

A delivery operations team needs a baseline model to estimate travel time
from several numeric features. Historical features can be collinear, so
directly inverting the normal-equation matrix can fail. Fit the
minimum-norm least-squares solution and predict for new orders.

---

### The Math

Add an intercept column to the training matrix `X` (an `n x d` matrix of
features). Find:

```
w = X+ y
```

where `X+` is the Moore-Penrose pseudoinverse of the intercept-augmented
`X`. For each query feature row `q`, predict:

```
yhat = w_0 + sum_j w_j * q_j
```

Use an SVD-based pseudoinverse or a numerically robust least-squares
solver. Do not explicitly invert `X^T X`.

### Input Format

`X` (`n x d`), `y` (length `n`), `queries` (`m x d`).

### Output Format

`(intercept, coefficients)`, then `m` predictions, all to 6 decimal places.

### Constraints

- `1 <= n <= 2000`, `1 <= d <= 20`, `1 <= m <= 100`.
- Absolute input values at most `10^4`.
- Time limit: 2.0 seconds. Memory: 256 MB.

---

### Example

**Input**

```
X = [[1], [2], [3]], y = [5, 7, 9], queries = [[4], [5]]
```

**Output**

```
intercept = 3.000000, coefficients = [2.000000]
predictions = [11.000000, 13.000000]
```

**Explanation:** The data follows `y = 2x + 3`, so the fitted intercept
and slope are `3` and `2`.
