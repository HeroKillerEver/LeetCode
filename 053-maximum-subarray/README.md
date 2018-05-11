## Idea

The tricky part is to detect this transition function:

```python
dp[i] = max(dp[i-1] + current, current)
```

then we just return the maximum of this `dp` array.
 

