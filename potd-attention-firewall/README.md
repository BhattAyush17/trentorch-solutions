# THE ATTENTION FIREWALL

Intermediate | transformers | attention

**Difficulty:** Medium
**Tags:** Transformers, Causal Masking, Softmax, Numerical Stability

---

### Story

A conversational model is decoding a response one token at a time. The
attention kernel receives only the keys and values in the visible prefix;
a regression in score scaling causes the final token to attend
incorrectly. Implement the scaled dot-product attention calculation for
that prefix and return its attention weights and output.

---

### The Math

Given query `q` (in `R^d`), keys `k_1..k_n` (each in `R^d`), and values
`v_1..v_n` (each in `R^dv`), the score for position `j` is:

```
s_j = (q . k_j) / sqrt(d)
```

The query is at position `n` (the last position), so every supplied key
and value is visible (no future positions exist to mask). Compute:

```
p_j = exp(s_j - max(s)) / sum_l exp(s_l - max(s))
o = sum_j p_j * v_j
```

### Input Format

`q` (length `d`), `keys` (`n x d`), `values` (`n x dv`).

### Output Format

`n` attention probabilities, then `dv` output components, both to 6
decimal places.

### Constraints

- `1 <= n <= 200`, `1 <= d, dv <= 32`, all values have absolute value at
  most `100`.
- Time limit: 1.0 second. Memory: 64 MB.

---

### Example

**Input**

```
q = [1, 0], keys = [[1, 0], [0, 1]], values = [[10], [20]]
```

**Output**

```
0.669762 0.330238
13.302379
```

**Explanation:** The scores are `1/sqrt(2)` and `0`. Stable softmax gives
probabilities near `0.669762` and `0.330238`, giving output near
`13.302379`.
