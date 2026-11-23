# THE REWARD-TO-GO BASELINE

Intermediate | reinforcement-learning | returns | advantage-estimation

**Difficulty:** Medium
**Tags:** Reinforcement Learning, Returns, Advantage Estimation

---

### Story

A policy-gradient training job uses a state-value baseline to reduce the
variance of its gradient estimate. Compute the one-step temporal-difference
target and advantage; a bug accidentally bootstraps from the current value
instead of the next-state value.

---

### The Math

Given reward `r`, current value `V_t`, next value `V_{t+1}`, discount
`gamma`, and terminal flag `d in {0, 1}`:

```
target = r + gamma * (1 - d) * V_{t+1}
advantage = target - V_t
```

A terminal transition (`d = 1`) has no bootstrapped next value.

### Input Format

`r`, `v_current`, `v_next`, `gamma`, `done`.

### Output Format

`(target, advantage)`, each to 6 decimal places.

### Constraints

- `|r|, |V_t|, |V_{t+1}| <= 10^6`, `0 <= gamma <= 1`, `done in {0, 1}`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
r = 1, v_current = 2, v_next = 10, gamma = 0.9, done = 0
```

**Output**

```
(10.000000, 8.000000)
```

**Explanation:** The target is `1 + 0.9*10 = 10`; subtracting the current
value of `2` gives an advantage of `8`.
