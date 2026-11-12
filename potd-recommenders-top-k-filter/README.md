# THE RECOMMENDER''S TOP-K FILTER

Intermediate | ranking | recommendation-systems

**Difficulty:** Medium
**Tags:** Ranking, Recommendation Systems, Top-K, Determinism

---

### Story

A recommendation service selects the top-k candidate titles from model
scores. Ties must be resolved deterministically by candidate ID so two
serving replicas return the same order.

---

### The Math

Each candidate has score `s_i` and a unique integer ID `id_i`. Sort by
descending score, breaking ties by ascending ID. Return the first `k`
candidates in that order.

### Input Format

`ids` (length `n`), `scores` (length `n`), `k`.

### Output Format

The IDs of the selected candidates in rank order.

### Constraints

- `1 <= k <= n <= 10^5`, IDs are distinct integers, `|s_i| <= 10^9`.
- Time limit: 1.0 second. Memory: 64 MB.

---

### Example

**Input**

```
ids = [40, 12, 7, 3, 22], scores = [0.8, 0.9, 0.9, 0.2, 0.8], k = 3
```

**Output**

```
7 12 22
```

**Explanation:** Scores `0.9` tie, so ID `7` precedes ID `12`. The next
score is `0.8`, where ID `22` precedes ID `40`.
