# UBER SURGE: DEMAND SMOOTHING

Beginner | computer-vision | pooling | array-manipulation | spatial-data

**Difficulty:** Easy
**Tags:** Computer Vision, Average Pooling, Spatial Data, Array Manipulation

---

### Story

Uber's dynamic pricing (surge pricing) divides a city into a high-resolution spatial grid to track
ride requests in real time. During a major event, a single city block can see a massive, localized
spike in demand. If the surge model reacts to that one block alone, riders get a fragmented
experience where crossing the street changes the price drastically.

To avoid this fragmentation, Uber's marketplace models use **Average Pooling** to smooth and
downsample the spatial demand features before they reach forecasting models like DeepETA. This is
the same operation as `02-average-pooling` in the Vision track, written from scratch. By averaging
demand over local patches, you smooth out extreme local spikes and shrink the grid for faster
downstream inference.

---

### The Math: Average Pooling

Given an `N x N` input matrix `X` (the high-resolution demand grid) and a pooling window of size
`F`, with a stride equal to `F` (the windows do not overlap), the output `Y` is an `M x M` matrix
where `M = N / F`.

For every output position `(i, j)` with `0 <= i < M` and `0 <= j < M`, the value is the arithmetic
mean of the matching `F x F` patch of the input:

```
Y[i][j] = mean( X[i*F + a][j*F + b] )   over all 0 <= a < F and 0 <= b < F
```

---

### Input Format

```
N F
x_{0,0} x_{0,1} ... x_{0,N-1}
...
x_{N-1,0} x_{N-1,1} ... x_{N-1,N-1}
```

- `N` is the size of the square input grid. It is always divisible by `F`.
- `F` is the size of the pooling window, and also the stride.
- The next `N` lines each hold `N` space-separated floats: the demand grid `X`.

### Output Format

Print `M` lines, each holding `M` space-separated floats: the smoothed, downsampled grid `Y`.

Print every value with exactly **4 decimal places**.

**Judging:** accepted if every output value is within `1e-4` absolute error of the reference
solution.

---

### Constraints

- `1 <= F <= N <= 1000`
- `N` is divisible by `F`
- values of `X` can be negative (normalized, z-scored demand)
- Time limit: 1.0 second. Memory limit: 64 MB.

---

### Example 1

**Input**

```
4 2
10.0 20.0 5.0 1.0
30.0 40.0 1.0 1.0
0.0 0.0 50.0 20.0
0.0 0.0 10.0 40.0
```

**Output**

```
25.0000 2.0000
0.0000 30.0000
```

**Explanation:** The `4 x 4` input is split into four `2 x 2` patches.

- Top-left patch: `(10.0 + 20.0 + 30.0 + 40.0) / 4 = 25.0000`: a strong, localized demand spike is
  smoothed out over the neighborhood.
- Top-right patch: `(5.0 + 1.0 + 1.0 + 1.0) / 4 = 2.0000`
- Bottom-left patch: `(0.0 + 0.0 + 0.0 + 0.0) / 4 = 0.0000`
- Bottom-right patch: `(50.0 + 20.0 + 10.0 + 40.0) / 4 = 30.0000`
