# K-Means: assignment step

Beginner | classical-ml | unsupervised | clustering | kmeans

### The problem, from first principles

`04-nearest-centroid` handed you labeled classes and their centroids, and asked which centroid a new point is closest to. Now flip the setup: there are no labels at all. You're just given a pile of points and told "there are `k` groups in here somewhere." You don't know where the groups are, only how many there should be.

You have to start somewhere, so K-Means starts by guessing: drop `k` centroids down at arbitrary positions, then figure out which points would belong to each one _if_ those centroids were right. That "if they were right, who'd be closest to whom" question is exactly the nearest-centroid question from `04-nearest-centroid`, just aimed at guessed centroids instead of true class means. Answer it once, and you've taken the first step of an algorithm that alternates this assignment with moving the centroids to fit what got assigned (`02-kmeans-centroid-update`) until the whole thing settles down.

### From theory to code

Implement `kmeans_assign(input, centroids)`, which measures every point against every centroid and reports, per point, which centroid is nearest. Theory below reduces this to the same distance-then-argmin shape as nearest centroid; the only actual work is doing it for centroids that are just current guesses, not settled class means.

### Constraints

- `input`: shape `(n_samples, n_features)`.
- `centroids`: shape `(k, n_features)`.
- Output: shape `(n_samples,)`, dtype int-like, one centroid index per sample.
- Reuse `01-knn`'s `pairwise_distances` for the distance computation, don't recompute distances by hand.
- A tie between two equidistant centroids resolves to the lower index.
- No explicit Python loop over samples or centroids.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

You already have a function that takes a set of "reference" points and a set of "query" points and returns every pairwise distance between them. Centroids are the reference points here; `input` is the queries.

</details>

<details>
<summary>Hint 2</summary>

`pairwise_distances(centroids, input)` returns shape `(n_samples, k)` — each row is one sample's distance to every centroid. The index you want per row is exactly what `np.argmin` along the centroid axis gives you.

</details>
