# THE UTILIZATION NUDGE

Beginner | optimization

**Difficulty:** Easy
**Tags:** Optimization

---

### Story

NVIDIA's internal GPU-scheduler team tunes a lightweight utilization-prediction model with plain
SGD before ever touching anything fancier. Every optimizer in the more advanced tracks builds on
getting this single update exactly right.

---

### The Math

```
theta <- theta - eta * grad
```

### Input Format

```
d eta
theta_1 ... theta_d
grad_1 ... grad_d
```

### Output Format

Updated `theta`, `d` values, 6 decimals.

### Constraints

- `1 <= d <= 10^4`
- Time limit: 1.0 second.

---

### Example

**Input**

```
2 0.1
1.0 2.0
0.2 -0.1
```

**Output**

```
0.980000 2.010000
```
