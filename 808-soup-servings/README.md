## Idea

This problem is quite obvious a _dp_ problem
```python
soup(n1, n2) = 0.25 * (soup(n1-100, n2) + soup(n1-75, n2-25)
+ soup(n1-50, n2-50) + soup(n1-25, n2-75))
```

__Note__: `soup(0, 0) = 0.5`, `soup(*, 0) = 0` and `soup(0, *) = 1`. when `n1` and `n2` is large enough, the probability is `1`