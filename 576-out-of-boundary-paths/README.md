## Idea

This problem is a typical _DP_. we denote `dp[n][i][j]` as possible ways to be in node `(i, j)` as timestep `n`. 
As we can easily discover that:

```python
dp[n+1][i][j] = dp[n][i+1][j]+dp[n][i-1][j]+dp[n][i][j+1]+dp[n][i][j-1]
```
And for every timestep, we need to check whether `dp[n][i][j]` can jump out of the boundary. 

__Note__: carefully check the boundaries. 