# Joint Distributions & Independence

Intermediate | probability | foundations

### The problem, from first principles

**Joint & marginal probability**

Every question so far in this track has treated one random variable at a time. Real models almost never get that luxury: a classifier's output is a joint distribution over (predicted class, true class); a language model's training objective is a joint distribution over (every token in the sequence); a VAE's ELBO is built from a joint distribution over (data, latent code). **Joint probability**, `P(X=x, Y=y)`, is the probability that two random variables simultaneously take specific values, the natural generalization of a single PMF to a full table. **Marginalization** is the reverse operation: given the joint table, recover either variable's own PMF by summing the other one out, literally adding up a row or column and writing the total in the table's margin, which is where the name comes from.

**Independence**

`03-joint-independence` built joint distributions two ways: from the independence formula (`joint_from_independent`) and, implicitly, from any arbitrary table. This question makes that distinction operational: given _any_ joint distribution, how do you tell whether the two variables are actually independent, versus knowing one tells you something about the other? And when they're not independent, how do you compute the **conditional distribution**, "given that `Y` turned out to be a specific value, what's the updated distribution over `X`?" This is the single most-used probability operation in ML: a classifier literally _is_ a model of `P(\text{class} \mid \text{input})`, a conditional distribution.

### From theory to code

**Joint & marginal probability**

Implement `joint_from_independent(marginal_x, marginal_y)`, building a joint distribution table under the assumption that `X` and `Y` are independent, then `marginalize(joint, axis)`, recovering one variable's marginal PMF by summing the joint table over the other axis. The signatures and docstrings are already in the editor.

**Independence**

Implement `is_independent(joint, tol=1e-9)`, checking whether a joint distribution factorizes into the product of its own marginals, then `conditional_pmf_given_y(joint, y_index)`, computing `P(X \mid Y = y_index)`. The signatures and docstrings are already in the editor.

### Constraints

**Joint & marginal probability**

- `marginal_x` and `marginal_y` are 1D array-likes of non-negative floats that each sum to 1 (valid PMFs).
- `joint` is a 2D array-like where `joint[i, j] = P(X=x_i, Y=y_j)`.
- `axis` follows NumPy's own convention: it names the axis being summed _out_, not the one being kept.

**Independence**

- `joint` is a 2D array-like where `joint[i, j] = P(X=x_i, Y=y_j)`.
- `tol` is the absolute tolerance for the independence equality check (floating-point sums rarely match exactly).
- `y_index` always indexes a value of `Y` with non-zero marginal probability.

### Hints

**Joint & marginal probability**

<details>
<summary>Hint 1</summary>

`joint_from_independent` is a single call to `np.outer(marginal_x, marginal_y)`, the outer product of two vectors produces exactly the "multiply every pair" table the independence formula asks for.

</details>

<details>
<summary>Hint 2</summary>

`marginalize` is `joint.sum(axis=axis)`, NumPy's own `axis` parameter already means "collapse this dimension by summing over it," which is precisely marginalization.

</details>

**Independence**

<details>
<summary>Hint 1</summary>

`is_independent` needs both marginals first, `joint.sum(axis=1)` for `marginal_x`, `joint.sum(axis=0)` for `marginal_y` (same convention as `03-joint-independence`'s `marginalize`), then compares `joint` against `np.outer(marginal_x, marginal_y)` with `np.allclose`.

</details>

<details>
<summary>Hint 2</summary>

`conditional_pmf_given_y` is a single column of `joint` (`joint[:, y_index]`), divided by that column's total (`marginal_y[y_index]`) to renormalize it back into a valid PMF that sums to 1.

</details>
