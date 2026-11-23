# THE REWARD DISCOUNT LEDGER

Intermediate | reinforcement-learning | returns | discounting

**Difficulty:** Medium
**Tags:** Reinforcement Learning, Returns, Discounting

---

### Story

A reinforcement-learning evaluation service computes discounted returns from
a short episode. A reversed loop accidentally discounts the first reward
most heavily rather than the last reward.

---

### The Math

For rewards `r_0, ..., r_{T-1}` and discount `gamma in [0, 1]`, the return at
the start is:

```
G_0 = sum_{t=0}^{T-1} gamma^t * r_t
```

Use the reward order as supplied.

### Input Format

`rewards` (length `T`), `gamma`.

### Output Format

`G_0`, 6 decimal places.

### Constraints

- `1 <= T <= 10^5`, `0 <= gamma <= 1`, `|r_t| <= 10^6`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
rewards = [1, 2, 4], gamma = 0.5
```

**Output**

```
3.000000
```

**Explanation:** The return is `1 + 0.5*2 + 0.25*4 = 3`.
