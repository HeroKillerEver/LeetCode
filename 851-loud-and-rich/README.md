## Idea

This problem looks complicated at first, it is basically a __dp__ problem, suppose we have a solver `f(x)`  which could return the quietest value for `x`, then we can write the recursive solution as:
```python
for y in x.neighbor:
	f(x) = min(f(x), f(y))
```
 we need to use the recursion with memorization. 