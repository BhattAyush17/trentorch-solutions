# PIN IMAGE DOWNSAMPLE

Beginner | computer-vision

**Difficulty:** Easy
**Tags:** Computer Vision

---

### Story

Pinterest downsamples every pin image before it reaches the visual-search backbone. This max-pool
layer is the very first operation in that backbone, run on millions of images a day.

---

### The Math

2D max pooling with kernel size `k`, stride `s`, no padding: output size
`floor((H - k) / s) + 1` per dimension, each output cell is the max over its receptive field.

### Input Format

```
H W k s
p_1,1 ... p_1,W
...
p_H,1 ... p_H,W
```

### Output Format

Pooled matrix, row by row, matching the input's own numeric type (integer values stay integer,
otherwise 6-decimal floats).

### Constraints

- `1 <= H, W <= 512`, `1 <= k <= min(H, W)`, `1 <= s <= k`
- Time limit: 1.0 second.

---

### Example

**Input**

```
4 4 2 2
1 3 2 4
5 6 7 8
9 1 2 3
4 5 6 0
```

**Output**

```
6 8
9 6
```
