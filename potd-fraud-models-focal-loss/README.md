# THE FRAUD MODEL''S FOCAL LOSS

Advanced | deep-learning | imbalanced-classification | loss-functions

**Difficulty:** Hard
**Tags:** Deep Learning, Imbalanced Classification, Loss Functions

---

### Story

A fraud model sees very few positive cases. The team adopts binary focal loss
to emphasize hard examples, but an implementation mixes up the true-class
probability and the predicted positive probability for negative examples.
Compute the per-example focal loss exactly as defined.

---

### The Math

For logit `z`, label `y in {0, 1}`, define `p = sigmoid(z)` and:

```
p_t = p       if y == 1
p_t = 1 - p   if y == 0

alpha_t = alpha      if y == 1
alpha_t = 1 - alpha  if y == 0
```

The focal loss for one example is:

```
L = -alpha_t * (1 - p_t)^gamma * log(p_t)
```

Return the mean loss over all examples.

### Input Format

`logits` (length `n`), `labels` (length `n`, binary), `alpha`, `gamma`.

### Output Format

Mean focal loss, 6 decimal places.

### Constraints

- `1 <= n <= 10^5`, `-20 <= z_i <= 20`, `0 <= alpha <= 1`, `0 <= gamma <= 5`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
logits = [0, 2], labels = [1, 0], alpha = 0.25, gamma = 2
```

**Output**

```
0.640440
```

**Explanation:** For the positive example, `p_t = 0.5`. For the negative
example with logit 2, `p_t = 1 - sigmoid(2) = 0.119203`. Applying the class
weights and focal factors gives a mean loss of about `0.640440`.
