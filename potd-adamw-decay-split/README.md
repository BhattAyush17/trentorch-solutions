# THE ADAMW DECAY SPLIT

Advanced | optimization | adamw

**Difficulty:** Hard
**Tags:** Optimization, AdamW, Weight Decay

---

### Story

A model fine-tuning job switches from Adam with L2 regularization to
AdamW. The implementation incorrectly adds weight decay to the gradient
before updating the moments. Use the specified decoupled decay order to
compute one parameter update.

---

### The Math

Given parameter `theta`, Adam's already-computed adaptive update `u`
(from gradient and moments), learning rate `eta`, and weight-decay
coefficient `lambda`:

```
theta' = theta - eta * u - eta * lambda * theta
```

Do not fold the decay term into `u`.

### Input Format

`theta`, `u`, `eta`, `lambda`.

### Output Format

The updated `theta`, 8 decimal places.

### Constraints

- `|theta|, |u| <= 10^6`, `0 <= eta <= 1`, `0 <= lambda <= 1`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
theta = 2, u = 0.5, eta = 0.1, lambda = 0.2
```

**Output**

```
1.91000000
```

**Explanation:** `theta' = 2 - 0.1*0.5 - 0.1*0.2*2 = 1.91`.
