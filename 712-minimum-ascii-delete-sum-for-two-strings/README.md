## Idea

This problem is a modification of [72. Edit Distance](https://leetcode.com/problems/edit-distance/description/). The idea is very similar, suppose that we have a function `f(x, y)` which could return the minimum distance for word `x` and `y`. Then we can have this recursive formula:
```python
if x[-1] != y[-1]:
	f(x, y) = min( f(x[:-1], y)+ord(x[-1]), f(x, y[:-1])+ord(y[-1]) ) 
	#delete x[-1], delete y[-1]
else:
	f(x, y) = f(x[:-1], y[:-1])
```