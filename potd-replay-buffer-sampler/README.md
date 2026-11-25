# THE REPLAY BUFFER SAMPLER

Intermediate | reinforcement-learning | experience-replay | sampling

**Difficulty:** Medium
**Tags:** Reinforcement Learning, Experience Replay, Sampling

---

### Story

An off-policy RL agent samples transitions from a replay buffer using
supplied priorities. A bug samples uniformly despite the priority weights.
Compute the normalized sampling probability of each transition.

---

### The Math

Given non-negative priorities `p_i` and exponent `alpha >= 0`:

```
P(i) = p_i^alpha / sum_j(p_j^alpha)
```

For `alpha = 0`, every transition's unnormalized weight is `1`, including
when a priority is zero. If all weights are zero under `alpha > 0`, the
distribution is defined as uniform.

### Input Format

`priorities`, `alpha`.

### Output Format

A length-`n` list of sampling probabilities, each to 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `0 <= p_i <= 10^6`, `0 <= alpha <= 2`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
priorities = [1, 2, 1], alpha = 1
```

**Output**

```
[0.250000, 0.500000, 0.250000]
```

**Explanation:** Priorities sum to `4`, so probabilities are `1/4, 2/4,
1/4`.
