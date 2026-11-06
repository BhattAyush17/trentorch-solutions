# THE K-MEANS EMPTY CLUSTER

Intermediate | unsupervised-learning | clustering

**Difficulty:** Medium
**Tags:** Unsupervised Learning, Clustering, Centroids

---

### Story

A playlist clustering job assigns tracks to centroids and recomputes
each centroid. One cluster receives no tracks. The pipeline must follow
a specified policy instead of dividing by zero or silently setting its
centroid to the origin.

---

### The Math

Each point `x_i` (in `R^d`) has an assigned cluster `c_i` in
`{0, ..., K-1}`. For each cluster `k`, recompute:

```
mu_k = mean of {x_i : c_i = k}
```

If cluster `k` has no assigned points, retain the supplied old centroid
for that cluster instead.

### Input Format

`points` (`n x d`), `assignments` (length `n`), `old_centroids`
(`K x d`).

### Output Format

`K` rows of `d` updated centroid coordinates, 6 decimal places.

### Constraints

- `1 <= n, K <= 10^5`, `1 <= d <= 20`, `0 <= c_i < K`.
- Coordinate magnitudes at most `10^6`. Time limit: 2.0 seconds.

---

### Example

**Input**

```
points = [[0,0], [2,2], [10,10]], assignments = [0, 0, 1]
old_centroids = [[5,5], [9,9]]
```

**Output**

```
1.000000 1.000000
10.000000 10.000000
```

**Explanation:** Cluster 0 averages its first two points. Cluster 1
receives one point, so its centroid becomes `(10, 10)`.
