# THE EARLY-STOPPING LEDGER

Intermediate | training | validation-metrics | early-stopping

**Difficulty:** Medium
**Tags:** Training, Validation Metrics, Early Stopping

---

### Story

A training monitor stops when validation loss has failed to improve for a
configured patience window. A boundary bug stops one epoch too early. Count
epochs according to the exact rule: improvement is strict, and stopping
occurs when consecutive non-improving epochs reach patience.

---

### The Math

Process validation losses in epoch order. The best loss initially is
`+infinity`. An epoch improves if and only if its loss is strictly smaller
than the best seen so far. Reset the non-improving counter on improvement;
otherwise increment it. Stop at the first epoch where the counter reaches
`patience`. If this never happens, stop after the final supplied epoch.

### Input Format

`losses` (length `n`), `patience`.

### Output Format

`(stop_epoch, best_loss)`, `stop_epoch` 1-based, `best_loss` 6 decimal
places.

### Constraints

- `1 <= n <= 10^5`, `1 <= patience <= 10^5`, losses finite.
- Time limit: 1.0 second.

---

### Example

**Input**

```
losses = [0.9, 0.8, 0.8, 0.81, 0.82, 0.7], patience = 2
```

**Output**

```
(4, 0.800000)
```

**Explanation:** Epoch 2 improves to `0.8`. Epoch 3 ties the best and is not
an improvement; epochs 3 and 4 are the two consecutive non-improving epochs,
so training stops at epoch 4.
