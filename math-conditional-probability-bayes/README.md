# Conditional Probability & Bayes' Theorem

Intermediate | probability | foundations

### The problem, from first principles

**Conditional probability**

"What's the chance it rains AND traffic is bad" is one question. "Given that it's raining, what's the chance traffic is bad" is a different, more useful one, it's the question you'd actually ask before deciding whether to leave early. The first is a joint probability, both things happening together. The second, conditional probability, restricts your attention to only the world where the condition holds, then asks about the other variable within that restricted world.

Turning a joint distribution over two variables into marginals (one variable alone) and conditionals (one variable, given a specific value of the other) is the basic manipulation every probabilistic model relies on, Naive Bayes (Classical ML) is built by combining conditional probabilities exactly like these.

**The chain rule**

**Naming collision, worth stating up front:** this "chain rule" has nothing to do with calculus's chain rule for differentiating composed functions, it's an unrelated rule that happens to share a name, because both describe "a chain of dependent steps multiplied together." Here, the chain rule of probability answers a very practical question: how do you compute the joint probability of several variables when you only know a chain of _conditional_ probabilities, `P(X)`, then `P(Y | X)`, then `P(Z | X, Y)`, and so on? This is exactly how autoregressive language models define the probability of an entire sequence: `P(\text{token}_1) \cdot P(\text{token}_2 \mid \text{token}_1) \cdot P(\text{token}_3 \mid \text{token}_1, \text{token}_2) \cdots`, each token's probability conditioned on every token before it, multiplied together into one number for the whole sequence.

**Bayes' theorem**

A medical test for a rare disease comes back positive. Should you be worried? Your gut says "the test is 99% accurate, so I'm almost certainly sick," but that's the wrong question, it ignores how rare the disease was in the first place. If the disease affects 1 in 100 people, and even a small fraction of HEALTHY people also test positive (a false positive rate), the healthy false-positives can vastly outnumber the sick true-positives in raw counts, even with a 99%-accurate test. The right question is: "of everyone who tests positive, healthy and sick combined, what fraction are actually sick?"

Bayes' theorem is the formula that answers exactly this: it takes a prior belief (how common is the disease, before any test), combines it with how the evidence behaves under each hypothesis (how likely is a positive test if you're sick, vs if you're not), and produces the correct, updated belief (how likely are you sick, given the positive test).

### From theory to code

**Conditional probability**

Theory represents a joint distribution over two discrete variables as a 2D array (`joint[i, j] = P(X=i, Y=j)`), gets a marginal by summing out the other variable, and gets a conditional by slicing to a fixed value of one variable and renormalizing so the slice becomes a valid probability distribution again.

Implement `marginal_x(joint)`, `marginal_y(joint)` and `conditional_x_given_y(joint, y_index)` against that reasoning. The signatures and docstrings are already in the editor.

**The chain rule**

Implement `joint_via_chain_rule(p_x, p_y_given_x, p_z_given_xy)` for the three-variable case, then `chain_rule_general(conditionals)`, generalizing to any number of variables given as a list of conditional-probability factors. The signatures and docstrings are already in the editor.

**Bayes' theorem**

Theory gives the raw formula (`posterior = likelihood * prior / evidence`) and, for the common binary-hypothesis case, shows how to compute the evidence term yourself from the two conditional likelihoods and the prior.

Implement `bayes_theorem(prior, likelihood, evidence)` first, the direct formula, then `posterior_binary(prior_h, likelihood_e_given_h, likelihood_e_given_not_h)`, which computes the evidence term and calls the first function.

### Constraints

**Conditional probability**

- `joint` is a 2D array summing to `1.0` overall (a valid joint probability table).
- Every returned distribution (marginal or conditional) must itself sum to `1.0`.
- `conditional_x_given_y` must renormalize, not just return the raw column slice.

**The chain rule**

- All probability arguments are floats in `[0, 1]`.
- `conditionals` is a non-empty list; its first entry is an unconditional probability, every entry after that is conditioned on all variables before it in the list's order.

**Bayes' theorem**

- All probabilities are plain floats in `[0, 1]`.
- `posterior_binary` must compute the evidence term itself (`P(evidence)`, the total probability of seeing the evidence at all, summed over both the H-true and H-false cases), not take it as a separate argument.
- `posterior_binary` should call `bayes_theorem` rather than reimplementing the same division.

### Hints

**Conditional probability**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Summing a 2D array along `axis=1` collapses columns (summing out the second index); `axis=0` collapses rows (summing out the first).

</details>

<details>
<summary>Hint 2</summary>

A single column of `joint` doesn't sum to 1 on its own, dividing by its own sum is what turns it into a valid conditional distribution.

</details>

**The chain rule**

<details>
<summary>Hint 1</summary>

`joint_via_chain_rule` is a single multiplication of its three arguments, no conditioning logic to implement, since each argument is already the correctly-conditioned probability.

</details>

<details>
<summary>Hint 2</summary>

`chain_rule_general` is `math.prod(conditionals)`, Python's `math.prod` multiplies every element of an iterable together, which is exactly what an arbitrary-length chain rule needs.

</details>

**Bayes' theorem**

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`bayes_theorem` is one line: multiply, then divide.

</details>

<details>
<summary>Hint 2</summary>

The evidence term is a weighted average: `P(evidence | H) * P(H) + P(evidence | not H) * P(not H)`, and `P(not H) = 1 - P(H)`.

</details>
