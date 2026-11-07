# Entropy

Beginner | information-theory

### The problem, from first principles

A coin that's guaranteed to land heads tells you nothing new when you flip it, you already knew the answer. A fair coin, by contrast, is maximally surprising every single flip, you genuinely can't predict it. Entropy is the precise, quantitative version of "how surprising is this distribution, on average," and it's measured in **bits**: the number of yes/no questions you'd need, on average, to pin down an outcome drawn from that distribution.

This isn't an abstract curiosity: `02-cross-entropy` (Deep Learning Core) is named "cross"-entropy specifically because it's a close cousin of this exact quantity, and understanding entropy first makes cross-entropy's formula, and why it measures "how surprised the model was by the true answer," make actual sense rather than being a formula to memorize.

### From theory to code

Theory gives the exact entropy formula, `-sum(p * log(p))`, and flags a numerical edge case: `log(0)` is `-inf`, but `p * log(p)` should be treated as exactly `0` when `p = 0` (a zero-probability outcome contributes nothing to the average surprise, since it never happens).

Implement `entropy(probs, base=2.0)` against that reasoning. The signature and docstring are already in the editor.

### Constraints

- `probs` is a valid probability distribution (non-negative, sums to `1`).
- Clip probabilities before taking a log, don't let `log(0)` produce `nan` or crash.
- `base` controls the unit: `base=2` gives bits (the default), `base=np.e` gives nats.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.clip(probs, eps, 1.0)` keeps every probability comfortably away from exactly `0` before you take its log.

</details>

<details>
<summary>Hint 2</summary>

Changing `base` is a single division at the end: divide the natural-log-based sum by `log(base)` (a general change-of-base rule).

</details>
