# THE FRAUD LABEL SURPRISE

Beginner | information-theory

**Difficulty:** Easy
**Tags:** Information Theory

---

### Story

Stripe's risk team runs a daily check on how "surprising" the label mix looks: entropy near zero
means the day was almost entirely one class, worth a glance before trusting any model metric
computed on it.

---

### The Math

```
H(p) = -sum_i p_i * log2(p_i)
```

### Input Format

```
k
p_1 ... p_k
```

A valid probability distribution, given directly.

### Output Format

`H(p)`, 6 decimals.

### Constraints

- `2 <= k <= 100`, `sum(p_i) = 1` guaranteed within `1e-6`
- Time limit: 1.0 second.

---

### Example

**Input**

```
2
0.995 0.005
```

**Output**

```
0.045415
```
