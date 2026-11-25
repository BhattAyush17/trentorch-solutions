# THE RETRIEVAL MRR SCORE

Advanced | information-retrieval | ranking-metrics | evaluation

**Difficulty:** Hard
**Tags:** Information Retrieval, Ranking Metrics, Evaluation

---

### Story

A search team measures mean reciprocal rank. A logging bug counts the
first relevant result at rank zero, causing a division by zero, while
another bug ignores queries with no relevant result entirely. The metric
contract defines a query with no relevant result as having reciprocal
rank zero.

---

### The Math

For each query, a ranked list contains relevance labels `r_j in {0, 1}`,
with rank starting at `1`. Its reciprocal rank is:

```
RR = 1 / j*     where j* = min{j : r_j = 1}
RR = 0          if no relevant result exists
```

Mean reciprocal rank is the arithmetic mean over all queries, including
queries with no relevant result.

### Input Format

`rankings`, a list of lists of relevance bits (one inner list per query).

### Output Format

MRR, to 6 decimal places.

### Constraints

- `1 <= Q <= 10^5`, `1 <= K <= 1000`, total `Q*K <= 2*10^6`.
- Time limit: 2.0 seconds.

---

### Example

**Input**

```
rankings = [[0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
```

**Output**

```
0.500000
```

**Explanation:** The reciprocal ranks are `1/2`, `0`, and `1`, whose mean
is `0.5`.
