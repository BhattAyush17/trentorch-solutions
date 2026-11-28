# Cosine Similarity

Beginner | problemset | maths-stats-for-ml | linear-algebra

Compute the cosine of the angle between two equal-length vectors.

Implement `solve(a, b)`.

**Returns.** Return a float in $[-1, 1]$. If either vector is all zeros the angle is undefined and the function returns `0.0`.

### Examples

**Example 1**

Input:

```python
solve([1.0, 0.0], [1.0, 1.0])
```

Output:

```text
0.707107
```

**Example 2**

Input:

```python
solve([1.0, 2.0], [-1.0, -2.0])
```

Output:

```text
-1.0
```
