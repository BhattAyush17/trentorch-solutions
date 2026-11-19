# THE DROPOUT INFERENCE MISMATCH

Advanced | deep-learning | dropout | training-vs-inference

**Difficulty:** Hard
**Tags:** Deep Learning, Dropout, Training vs Inference

---

### Story

A recommendation model's inference outputs are too small because the serving
code applies the training-time dropout mask without inverted scaling. Compute
the specified inverted-dropout result for a fixed mask so the behavior is
deterministic.

---

### The Math

For activation `x_i`, keep probability `q = 1 - p`, and binary mask
`m_i in {0, 1}`, inverted dropout during training returns:

```
y_i = m_i * x_i / q
```

During inference, dropout is disabled and `y_i = x_i`. The mode and mask are
given explicitly; if inference mode is selected, the mask is ignored.

### Input Format

`activations` (length `n`), `mask` (length `n`, binary), `mode`
(`"train"` or `"infer"`), `p` (drop probability).

### Output Format

`n` outputs, 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `0 <= p < 1`, `|x_i| <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
activations = [2, 4, -2, 8], mask = [1, 0, 1, 1], mode = "train", p = 0.5
```

**Output**

```
4.000000 0.000000 -4.000000 16.000000
```

**Explanation:** Kept activations are divided by `q = 0.5`; dropped
activations become zero.
