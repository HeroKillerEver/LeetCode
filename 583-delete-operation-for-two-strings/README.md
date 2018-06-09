## Idea

This problem is the same problem as _LCS_. Let us denote `dp[i][j]` as the _LCS_ for `word1[:i]` and `word2[:j]`, as we can discover the subproblem as:
```python
dp[i][j] = dp[i-1][j-1] + 1 if word1[i] == word2[j]
dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if word1[i] != word2[j]
```
then we just return `len(word1)` + `len(word2)` - `2 * LCS`