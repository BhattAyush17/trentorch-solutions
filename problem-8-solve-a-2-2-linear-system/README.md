# Solve a 2×2 Linear System

Intermediate | problemset | maths-stats-for-ml | linear-algebra

Solve the system $ax+by=e$, $cx+dy=f$ for $x$ and $y$ without calling a linear solver. The six numbers arrive as the list `[a, b, c, d, e, f]`.

Implement `solve(coeffs)`.

**Returns.** Return `[x, y]` as a NumPy array. A singular system (determinant $0$) has no unique solution and raises `ValueError`.

### Examples

**Example 1**

Input:

```python
solve([2, 1, 1, 3, 5, 7])
```

Output:

```text
[1.6, 1.8]
```

**Example 2**

Input:

```python
solve([1, 2, 2, 4, 3, 6])
```

Output: Raises `ValueError`.
