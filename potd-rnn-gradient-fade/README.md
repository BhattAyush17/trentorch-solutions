# THE RNN GRADIENT FADE

Advanced | sequence-models | rnns | backpropagation-through-time

**Difficulty:** Hard
**Tags:** Sequence Models, RNNs, Backpropagation Through Time

---

### Story

A sequence model's training dashboard reports vanishing gradients. For a
simplified recurrent cell, the gradient of the final hidden state with
respect to the initial one must be computed exactly as a product across
timesteps, not as an average of the per-step derivatives.

---

### The Math

The recurrence is `h_t = tanh(a*h_{t-1} + x_t)`. The local derivative at
step `t` is:

```
dh_t/dh_{t-1} = a * (1 - h_t^2)
```

Given already-computed hidden states `h_1, ..., h_T`, the gradient of the
final state with respect to the initial one is the exact product:

```
dh_T/dh_0 = product_{t=1}^{T} a * (1 - h_t^2)
```

### Input Format

`hidden_states` (length `T`, the already-computed `h_1..h_T`), `a`.

### Output Format

The scalar gradient.

### Constraints

- `1 <= T <= 10^5`, `|a| <= 2`, `-1 <= h_t <= 1`.
- Time limit: 1.0 second. Memory limit: 64MB.

---

### Example

**Input**

```
hidden_states = [0, 0.5, 0.8], a = 0.5
```

**Output**

```
0.0337500000
```

**Explanation:** The three factors are `0.5*(1-0)=0.5`, `0.5*(1-0.25)=0.375`,
and `0.5*(1-0.64)=0.18`. Their product is `0.5 * 0.375 * 0.18 = 0.03375`.
