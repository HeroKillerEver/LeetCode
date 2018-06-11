## Idea

This problem is like a benchmark problem for dynamical programming. suppose that we have a function `f(x, y)` which could return the minimum distance for word `x` and `y`. Then we can have this recursive formula:
```python
if x[-1] != y[-1]:
	f(x, y) = min( f(x[:-1], y)+1, f(x, y[:-1])+1, f(x[:-1], y[:-1])+1 ) 
	#delete x[-1], insert y[-1] into x[-1], replace x[-1] to y[-1]
else:
	f(x, y) = f(x[:-1], y[:-1])
```