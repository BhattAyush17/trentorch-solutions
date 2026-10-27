# Scatter Plots: Colour, Size & Fits

Beginner | data-science | visualization | matplotlib | scatter

### The problem, from first principles

A scatter plot is the honest way to look at two numbers per observation: one dot per row, no line implying that neighbouring dots are connected. Its power is that a dot has more than a position. Its **size** can carry a third number (population, revenue), its **colour** can carry a fourth (a score, a temperature), and a line drawn over the dots can summarise the trend. A reader should be able to tell what each encoding means, which is why a colour scale needs a _colourbar_ and a fitted line needs a label.

This question builds the three layers of a typical scatter figure: the dots with size and colour, a least-squares trend line, and a second layer that marks the points that sit unusually far from the average.

### From theory to code

Implement `scatter_chart(x, y, sizes, values, label)`, `fit_line(ax, x, y)` and `highlight_outliers(ax, x, y, k)`. The signatures and docstrings are already in the editor.

### Constraints

- `scatter_chart` returns `(fig, ax, points)`: a new figure with one scatter of `(x, y)`, marker areas `sizes`, coloured by `values` with the `viridis` colormap, and a **colourbar** whose label is `label`. `points` is the scatter's collection.
- `fit_line(ax, x, y)` computes the ordinary least-squares line `y = slope * x + intercept` through the points and draws it on `ax` as **one line segment from the smallest `x` to the largest `x`**, colour `"red"`, label `"fit"`. It returns `(slope, intercept)` as Python floats.
- `highlight_outliers(ax, x, y, k)` draws, as a **second scatter** on `ax`, the points whose `y` differs from the mean of `y` by more than `k` times the (population) standard deviation of `y`. They are red, with marker area 80. It returns the number of outliers as an `int`. If there are none it draws nothing.
- `x`, `y`, `sizes`, `values` are equal-length sequences of numbers. Do not call `plt.show()`.

### Hints

<details>
<summary>Hint 1</summary>

`ax.scatter(x, y, s=sizes, c=values, cmap=...)` returns the collection a colourbar needs: `fig.colorbar(points, ax=ax, label=...)`.

</details>

<details>
<summary>Hint 2</summary>

`np.polyfit(x, y, 1)` returns the slope and intercept of the least-squares line.

</details>

<details>
<summary>Hint 3</summary>

Build a boolean mask for the outliers with NumPy, and count it with `mask.sum()`.

</details>
