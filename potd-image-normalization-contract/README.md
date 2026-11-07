# THE IMAGE NORMALIZATION CONTRACT

Intermediate | computer-vision | preprocessing

**Difficulty:** Medium
**Tags:** Computer Vision, Preprocessing, Broadcasting

---

### Story

A vision inference service normalizes each RGB channel with channel-specific
means and standard deviations. A broadcasting bug applies the red channel's
statistics to all three channels; the fix must use each channel's own mean
and standard deviation.

---

### The Math

For each channel `c` in `{R, G, B}`:

```
z_c = (x_c - mu_c) / sigma_c
```

Each channel has its own mean `mu_c` and its own strictly positive standard
deviation `sigma_c`.

### Input Format

`x` (length 3, the RGB pixel), `mu` (length 3), `sigma` (length 3).

### Output Format

Three normalized RGB values, 6 decimal places.

### Constraints

- All values finite, `|x_c|, |mu_c| <= 10^6`, `0 < sigma_c <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
x = [255, 128, 0], mu = [127.5, 128, 10], sigma = [127.5, 64, 10]
```

**Output**

```
1.000000 0.000000 -1.000000
```

**Explanation:** Red is one standard deviation above its own mean, green is
exactly at its mean, and blue is one standard deviation below its mean.
