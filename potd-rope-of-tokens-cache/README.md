# THE ROPE-OF-TOKENS CACHE

Advanced | llm-inference | kv-cache | sliding-windows

**Difficulty:** Hard
**Tags:** LLM Inference, KV Cache, Sliding Windows

---

### Story

A long-context serving engine uses a sliding-window attention cache. After
each new token, only the most recent `W` token states remain resident.
Compute cache occupancy for a batch of requests without allocating a
token-by-token cache.

---

### The Math

For a request with total generated-plus-prompt length `T` and sliding
window `W`, the resident token count is:

```
R = min(T, W)
```

Given per-token cache cost `C` bytes and number of concurrent sequences
`B`, total cache memory is:

```
M = B * C * R
```

Each query is independent; `C` already includes all layers and K/V tensors
for one token.

### Input Format

A list of `(B, T, W, C)` tuples, one per query.

### Output Format

For each query, `(R, M)`.

### Constraints

- All values are positive integers up to `10^12`; products fit a signed
  64-bit integer.
- Time limit: 1.0 second.

---

### Example

**Input**

```
queries = [(4, 1000, 128, 4096), (2, 32, 128, 4096)]
```

**Output**

```
[(128, 2097152), (32, 262144)]
```

**Explanation:** The first request retains `128` tokens per sequence
(`min(1000, 128)`); the second retains all `32` tokens (`min(32, 128)`).
