# THE TOKEN-LEVEL TOP-P CUTOFF

Advanced | llm-sampling | nucleus-sampling

**Difficulty:** Hard
**Tags:** LLM Sampling, Nucleus Sampling, Probability

---

### Story

A language model sampler uses nucleus sampling. An implementation keeps
tokens whose cumulative probability is strictly below `p` and accidentally
drops the token that crosses the threshold. Sort probabilities descending,
keep the smallest prefix whose cumulative mass reaches or exceeds `p`,
and renormalize.

---

### The Math

Given non-negative probabilities `p_i` summing to one and threshold `r`
in `(0, 1]`: sort tokens by descending probability, breaking ties by
ascending original index. Keep the smallest prefix `S` such that:

```
sum_{i in S} p_i >= r
```

Set probabilities outside `S` to zero and renormalize the retained
probabilities to sum to one. Output in original token order.

### Input Format

`probs` (length `n`), `r`.

### Output Format

`n` renormalized probabilities in original order, 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, probabilities are non-negative and sum to one within
  `10^-6`, `0 < r <= 1`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
probs = [0.4, 0.3, 0.2, 0.1], r = 0.7
```

**Output**

```
0.571429 0.428571 0.000000 0.000000
```

**Explanation:** The first two tokens have cumulative mass `0.7`, so
retain both and renormalize by `0.7`.
