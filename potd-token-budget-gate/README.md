# THE TOKEN BUDGET GATE

Intermediate | llm-inference | context-windows

**Difficulty:** Medium
**Tags:** LLM Inference, Context Windows, Memory Accounting

---

### Story

A hosted language-model API must admit requests only when the prompt and
reserved generation tokens fit the model's context window. An off-by-one
error accepts a request that exceeds the supported sequence length.

---

### The Math

Let `P` be the prompt-token count, `R` the requested generation-token
count, and `C` the context limit. A request fits exactly when:

```
P + R <= C
```

The maximum generation budget still available for this prompt is:

```
R_max = max(0, C - P)
```

### Input Format

`P`, `R`, `C` (non-negative integers).

### Output Format

`R_max`, then whether the request fits (`True`/`False`).

### Constraints

- `0 <= P, R, C <= 10^18`.
- Time limit: 1.0 second. Memory: 64 MB.

---

### Example

**Input**

```
P = 7900, R = 300, C = 8192
```

**Output**

```
292 NO
```

**Explanation:** The prompt leaves `8192 - 7900 = 292` positions. A
request for `300` tokens exceeds the limit by `8`.
