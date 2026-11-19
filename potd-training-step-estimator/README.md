# THE TRAINING-STEP ESTIMATOR

Intermediate | training-systems | epochs | batch-sizes

**Difficulty:** Medium
**Tags:** Training Systems, Epochs, Batch Sizes

---

### Story

A training scheduler estimates optimizer steps per epoch. The final partial
batch is retained, but a floor-division implementation underestimates the
schedule length.

---

### The Math

For `N` examples and batch size `B`, with incomplete final batches retained,
steps per epoch are:

```
S = ceil(N / B)
```

For `E` epochs, total optimizer steps are `E * S`.

### Input Format

`N`, `B`, `E`.

### Output Format

`(steps_per_epoch, total_steps)`.

### Constraints

- `1 <= N, B, E <= 10^12`; the total fits in a signed 64-bit integer.
- Time limit: 1.0 second.

---

### Example

**Input**

```
N = 1001, B = 64, E = 3
```

**Output**

```
(16, 48)
```

**Explanation:** `ceil(1001 / 64) = 16`, so three epochs contain 48
optimizer steps.
