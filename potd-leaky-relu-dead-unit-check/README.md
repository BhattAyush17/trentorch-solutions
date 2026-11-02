# THE LEAKY-RELU DEAD-UNIT CHECK

Intermediate | deep-learning | activation-functions

**Difficulty:** Medium
**Tags:** Deep Learning, Activation Functions, Autograd

---

### Story

A neural ranking model uses Leaky ReLU to reduce dead units. The backward
kernel incorrectly uses the positive-branch derivative for negative
inputs. Compute forward values and local derivatives, using the stated
convention at zero.

---

### The Math

For negative slope `alpha`:

```
f(x)  = x        if x > 0
        alpha*x  if x <= 0

f'(x) = 1        if x > 0
        alpha    if x <= 0
```

Zero belongs to the non-positive branch by this convention: `f(0) = 0`
and `f'(0) = alpha`.

### Input Format

`x` (length `n`), `alpha`.

### Output Format

Two sequences of length `n`: activations, then derivatives, 6 decimal
places.

### Constraints

- `1 <= n <= 10^5`, `0 <= alpha <= 1`, `|x_i| <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
x = [-2, 0, 3, -0.5, 1.5], alpha = 0.1
```

**Output**

```
activations = [-0.200000, 0.000000, 3.000000, -0.050000, 1.500000]
derivatives = [0.100000, 0.100000, 1.000000, 0.100000, 1.000000]
```

**Explanation:** Zero belongs to the non-positive branch under the
specified convention, so its derivative is `alpha`.
