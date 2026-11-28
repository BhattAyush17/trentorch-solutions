# Normalize a Vector

Beginner | problemset | maths-stats-for-ml | linear-algebra

Return the unit vector that points in the same direction as a non-zero vector.

Implement `solve(x)`.

**Returns.** Return a NumPy array of the same shape with length 1. A zero vector has no direction, so it raises `ValueError`.

### Examples

**Example 1**

Input:

```python
solve([3.0, 4.0])
```

Output:

```text
[0.6, 0.8]
```

**Example 2**

Input:

```python
solve([0.0, 0.0])
```

Output: Raises `ValueError`.
