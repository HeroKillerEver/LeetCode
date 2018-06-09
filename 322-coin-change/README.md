## Idea

This problem is very obvious _DP_ problem. we denote `dp[i]` as the minimum number of coins for money `i`. So the logic is:
```python
dp[i] = min( dp[i], dp[i-coin] +1 ) for coin in coins
```
then we just return `dp[-1]`