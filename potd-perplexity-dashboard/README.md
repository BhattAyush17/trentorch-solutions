# THE PERPLEXITY DASHBOARD

Intermediate | language-models | cross-entropy

**Difficulty:** Medium
**Tags:** Language Models, Cross-Entropy, Perplexity

---

### Story

A language-model evaluation dashboard reports perplexity from token-level
negative log likelihoods. It accidentally exponentiates the sum rather
than the mean, causing scores to depend exponentially on evaluation-set
length.

---

### The Math

Given token negative log-likelihoods `l_1, ..., l_N` (already token-level
negative log likelihoods):

```
H   = mean(l)
PPL = e^H
```

### Input Format

`losses`: a list of `N` non-negative loss values.

### Output Format

`(mean_loss, perplexity)`, 6 decimal places.

### Constraints

- `1 <= N <= 10^5`, `0 <= l_i <= 20`.
- Time limit: 1.0 second.

---

### Example

**Input**

```
losses = [0.5, 1.0, 1.5]
```

**Output**

```
1.000000 2.718282
```

**Explanation:** The mean loss is `1`, so perplexity is `e^1`.
