# Matrix-Vector Product

Beginner | problemset | maths-stats-for-ml | linear-algebra

Multiply an $m\times n$ matrix by a length-$n$ vector by computing each output entry as the dot product of one matrix row with the vector.

Implement `solve(A, x)`.

**Returns.** Return a NumPy array of length $m$.

### Examples

**Example 1**

Input:

```python
solve([[1.0, 2.0], [3.0, 4.0]], [1.0, 1.0])
```

Output:

```text
[3.0, 7.0]
```

**Example 2**

Input:

```python
solve([[0.0, 1.0, 0.0]], [5.0, 6.0, 7.0])
```

Output:

```text
[6.0]
```
