# THE MULTI-QUERY CACHE HIT RATE

Intermediate | inference-systems | caching

**Difficulty:** Medium
**Tags:** Inference Systems, Caching, Performance Metrics

---

### Story

An embedding service caches repeated requests. Monitoring must report the
hit rate over a request window. A cache hit is defined as a request whose
key has appeared earlier in the same window; the first occurrence is a
miss.

---

### The Math

For a sequence of request keys `k_1, ..., k_n`, request `i` is a hit iff
there exists `j < i` with `k_j = k_i`. The hit rate is:

```
r = hits / n
```

### Input Format

`keys`: a list of integer request keys.

### Output Format

`(hits, misses, rate)`, rate to 6 decimal places.

### Constraints

- `1 <= n <= 10^6`, keys are signed 64-bit integers.
- Time limit: 1.0 second.

---

### Example

**Input**

```
keys = [4, 2, 4, 4, 2]
```

**Output**

```
3 2 0.600000
```

**Explanation:** The third, fourth, and fifth requests repeat a
previously seen key.
