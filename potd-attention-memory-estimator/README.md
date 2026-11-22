# THE ATTENTION MEMORY ESTIMATOR

Intermediate | transformers | tensor-shapes | memory-accounting

**Difficulty:** Medium
**Tags:** Transformers, Tensor Shapes, Memory Accounting

---

### Story

A model engineer estimates the memory of a materialized attention-score
tensor. The estimate must account for batch, heads, query length, key
length, and bytes per score, rather than assuming a square sequence in every
workload.

---

### The Math

For batch `B`, heads `H`, query length `T_q`, key length `T_k`, and `b`
bytes per score, the score tensor occupies:

```
M = B * H * T_q * T_k * b  bytes
```

This excludes softmax intermediates, values, and gradients.

### Input Format

`B`, `H`, `Tq`, `Tk`, `b`.

### Output Format

`(bytes, mib)` where `1 MiB = 2^20` bytes; `mib` to 6 decimal places.

### Constraints

- All dimensions are positive integers at most `10^5`, `b in {2, 4, 8}`; the
  byte count fits in a signed 64-bit integer.
- Time limit: 1.0 second.

---

### Example

**Input**

```
B = 2, H = 8, Tq = 128, Tk = 256, b = 2
```

**Output**

```
(1048576, 1.000000)
```

**Explanation:** The score tensor contains `2 * 8 * 128 * 256` values, each
2 bytes, totaling 1 MiB.
