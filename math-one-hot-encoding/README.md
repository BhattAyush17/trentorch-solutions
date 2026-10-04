# One-hot encoding a categorical column

Intermediate | data-processing

### The problem, from first principles

A column of city names, `"NYC"`, `"LA"`, `"NYC"`, `"Chicago"`, can't be fed directly into `linear` (this curriculum's very first question) or any matrix-multiply-based model, there's no meaningful numeric distance between "NYC" and "LA" the way there is between the number `3` and `5`. Assigning `NYC=0, LA=1, Chicago=2` doesn't fix this, it silently implies Chicago is "twice as far" from NYC as LA is, a completely fabricated numeric relationship that doesn't exist in the underlying category.

One-hot encoding sidesteps the problem entirely: instead of one arbitrary number per category, use one dedicated 0/1 column per possible category. No category is numerically "closer" to any other, every pairwise distance between two different categories is identical, exactly the "no fabricated relationship" property a categorical variable actually has.

### From theory to code

Theory turns a length-`n` categorical column into an `(n, k)` binary matrix (`k` = number of distinct categories), one column per category, a single `1` per row marking that row's category. Implement the category-discovery step first, then the encoding itself, built to accept an explicit category list (not just always deriving one fresh) for the reason Theory's PyTorch section explains.

Implement `get_unique_categories(column)` and `one_hot_encode(column, categories=None)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `get_unique_categories` returns categories in a fixed, sorted order (so encoding is reproducible).
- `one_hot_encode`'s output shape is `(len(column), len(categories))`.
- Every row of the output sums to exactly `1` (exactly one category per row).
- If `categories` is passed explicitly, use it as-is, don't recompute from `column`.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

`np.unique` already returns sorted, distinct values in one call.

</details>

<details>
<summary>Hint 2</summary>

Build a `{category: column_index}` lookup dict once, then loop over rows, setting exactly one `1` per row using that lookup.

</details>
