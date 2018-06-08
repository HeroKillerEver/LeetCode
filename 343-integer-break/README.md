## Idea

This problem is an obvious _DP_ problem, let us denote `f(j)` as the maximum product, so for a given number `i`, the maximum product could be:
```python
f(i) = max(  max(j, f(j)) * max(i-j, f(i-j)) ) for j in range(1, i)
```