# Permutations & Combinations

Beginner | probability | foundations

### The problem, from first principles

`01-random-variables`'s Binomial PMF leaned on `binom{n}{k}`, "n choose k," without deriving it, this question fills that gap by building the two counting tools every discrete-probability formula eventually needs: **permutations** (how many ways to arrange `k` items out of `n`, where order matters, who finishes 1st/2nd/3rd in a race) and **combinations** (how many ways to _choose_ `k` items out of `n`, where order doesn't matter, who's on a 3-person committee). Every discrete distribution built from "count the favorable outcomes, divide by total outcomes", Binomial, Hypergeometric, Multinomial, starts here.

### From theory to code

Implement `permutations_count(n, k)` and `combinations_count(n, k)`, using Python's `math.factorial`. The signatures and docstrings are already in the editor.

### Constraints

- `n` and `k` are non-negative integers with `0 <= k <= n`.
- Use `math.factorial`, already imported in the starter.

### Hints

<details>
<summary>Hint 1</summary>

`permutations_count(n, k)` is `n! / (n-k)!` directly, Python's `//` performs exact integer division here since the result is always a whole number.

</details>

<details>
<summary>Hint 2</summary>

`combinations_count(n, k)` is `permutations_count(n, k)` divided again by `k!`, order-matters count, divided by the number of orderings of the `k` chosen items, removes the "order" information and leaves just "which items."

</details>
