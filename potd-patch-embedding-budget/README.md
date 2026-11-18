# THE PATCH EMBEDDING BUDGET

Intermediate | computer-vision | transformers | tensor-shapes

**Difficulty:** Medium
**Tags:** Computer Vision, Transformers, Tensor Shapes

---

### Story

A vision transformer converts an image into non-overlapping square patches. A
data loader silently drops border pixels when the image dimensions are not
divisible by the patch size. This task rejects such images rather than
silently dropping pixels.

---

### The Math

For image height `H`, width `W`, patch size `P`, and embedding dimension `D`,
patches are valid only if `H mod P == 0` and `W mod P == 0`. If valid, the
patch count is:

```
N = (H / P) * (W / P)
```

and the patch-projection weight matrix has `P^2 * C * D` parameters for `C`
input channels, excluding bias.

### Input Format

`H`, `W`, `P`, `C`, `D`.

### Output Format

If the dimensions are not divisible by `P`, return `None`. Otherwise return
`(N, params)`.

### Constraints

- `1 <= H, W <= 10^5`, `1 <= P, C, D <= 10^4`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
H = 224, W = 224, P = 16, C = 3, D = 768
```

**Output**

```
(196, 589824)
```

**Explanation:** The image has `14 x 14 = 196` patches. Projection weights
contain `16^2 * 3 * 768 = 589824` parameters.
