# THE CONVOLUTION OUTPUT SHAPE

Intermediate | deep-learning | cnns

**Difficulty:** Medium
**Tags:** Deep Learning, CNNs, Tensor Shapes

---

### Story

A vision pipeline allocates output tensors for a convolution. A shape
calculation that ignores stride and padding causes buffer overruns. Compute
the output height and width for a 2D convolution with symmetric padding.

---

### The Math

For input dimension `I`, kernel `K`, padding `P`, and stride `S`:

```
O = floor((I + 2P - K) / S) + 1
```

Apply independently to height and width. The input guarantees positive
output dimensions.

### Input Format

`H`, `W`, `K`, `P`, `S`.

### Output Format

Output height and output width, as integers.

### Constraints

- `1 <= H, W <= 10^6`, `1 <= K, S <= 10^5`, `0 <= P <= 10^5`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
H=32, W=32, K=3, P=1, S=2
```

**Output**

```
16 16
```

**Explanation:** `floor((32 + 2 - 3) / 2) + 1 = 16` in both dimensions.
