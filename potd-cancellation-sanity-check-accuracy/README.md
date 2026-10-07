# CANCELLATION SANITY CHECK

Beginner | metrics-and-evaluation

**Difficulty:** Easy
**Tags:** Metrics & Evaluation

---

### Story

A first-pass cancellation classifier needs one sanity-check number before the team invests in
anything more sophisticated than accuracy.

---

### The Math

```
Accuracy = (TP + TN) / n
```

### Input Format

```
n
p_1 y_1
...
p_n y_n
```

### Output Format

Scalar accuracy, 6 decimals.

### Constraints

- `1 <= n <= 10^6`
- Time limit: 1.0 second.

---

### Example

**Input**

```
6
1 1
0 0
1 0
1 1
0 0
0 1
```

**Output**

```
0.666667
```
