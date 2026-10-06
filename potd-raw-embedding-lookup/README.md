# THE RAW EMBEDDING LOOKUP

Beginner | transformers

**Difficulty:** Easy
**Tags:** Transformers

---

### Story

An Azure Cognitive Services text pipeline needs the single most basic operation in any transformer:
turning token ids into vectors via table lookup, before any positional encoding or attention
touches them.

---

### The Math

Given embedding matrix `E` of shape `(V, d)` and a sequence of token ids, return `E[ids]`.

### Input Format

```
V d
E (V x d, row-major)
n
id_1 ... id_n
```

### Output Format

`n x d` matrix, one row per token, 6 decimals.

### Constraints

- `1 <= V <= 10^5`, `1 <= d <= 512`, `1 <= n <= 10^4`, ids in `[0, V-1]`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4 2
0.1 0.2
0.3 0.4
0.5 0.6
0.7 0.8
3
2 0 3
```

**Output**

```
0.500000 0.600000
0.100000 0.200000
0.700000 0.800000
```
