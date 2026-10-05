# Ridge Regression (L2)

Intermediate | classical-ml | regression

### The problem, from first principles

`Linear Regression: closed form (Normal Equation)` solves for the EXACT weights that minimize training error, no compromise, whatever fits the training data best, wins. But `Generalization: train/val split and the generalization gap` already showed why "fits training data best" and "generalizes well" aren't the same goal: with enough features relative to data, the exact solution can chase every quirk in the training set, including noise, producing large, unstable weights that fit training data perfectly but generalize badly.

Ridge regression adds a second term to the objective: alongside "minimize prediction error," ALSO "keep the weights small." This tension, between fitting the data and staying simple, is regularization's whole idea, and Ridge specifically penalizes weights by their SQUARED magnitude, which (conveniently) keeps the problem exactly as solvable in closed form as plain linear regression was.

### From theory to code

Theory modifies the Normal Equation with one additional term, a small multiple of the identity matrix added before inverting, that shrinks every weight toward zero proportional to a tunable strength, `alpha`.

Implement `ridge_regression_closed_form(input, target, alpha=1.0)` against that reasoning, reusing `Linear Regression: closed form (Normal Equation)`'s own augmented-matrix structure.

### Constraints

- Augment `input` with a bias column, exactly like the plain Normal Equation.
- The regularization penalty applies to the WEIGHTS only, never the bias (the identity matrix's last diagonal entry must be `0`, not `alpha`).
- `alpha=0` should recover the plain Normal Equation's answer exactly.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Build the penalty matrix as `alpha * np.eye(d + 1)`, then explicitly zero out its very last diagonal entry (the bias position).

</details>

<details>
<summary>Hint 2</summary>

The rest of the formula is `Linear Regression: closed form (Normal Equation)`'s own `(X^T X)^-1 X^T y`, with `X^T X` replaced by `X^T X + penalty`.

</details>
