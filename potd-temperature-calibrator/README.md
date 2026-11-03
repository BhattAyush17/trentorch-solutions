# THE TEMPERATURE CALIBRATOR

Intermediate | llms | sampling

**Difficulty:** Medium
**Tags:** LLMs, Sampling, Softmax, Temperature

---

### Story

A generation service exposes a temperature parameter. A client bug
multiplies logits by temperature instead of dividing by it, making high
temperature more deterministic (the opposite of its intent). Return the
next-token distribution for the specified positive temperature.

---

### The Math

For logits `z` and temperature `tau > 0`:

```
p = softmax(z / tau)
```

Use a numerically stable softmax after dividing each logit by `tau`.
This returns probabilities only; it does not sample a token.

### Input Format

`z` (length `d`), `tau`.

### Output Format

`d` probabilities, 6 decimal places.

### Constraints

- `1 <= d <= 10^5`, `10^-3 <= tau <= 10^3`, `|z_i| <= 10^4`.
- Time limit: 1.0 second. Memory: 64 MB.

---

### Example

**Input**

```
z = [2, 0, -2], tau = 2
```

**Output**

```
0.665241 0.244728 0.090031
```

**Explanation:** Dividing logits by `2` gives `(1, 0, -1)`, whose softmax
is approximately the displayed distribution.
