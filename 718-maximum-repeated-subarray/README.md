## Idea

This Problem is very similar to [Longest Common Substring](https://www.geeksforgeeks.org/longest-common-subsequence/):

> Given two sequences, find the length of longest subsequence present in both of them. A subsequence is > a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, > “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n
>  different possible subsequences.

Let the input sequences be `X` and `Y` of lengths `m` and `n` respectively. Suppose we have a LCS solver `f(x, y)` which could return LCS. So we could find a recursive relationship:
```python
if x[-1] == y[-1]:
		f(x, y) = 1 + f(x[:-1], y[:-1])
else:
		f(x, y) = max(f(x[:-1], y), f(x, y[:-1]))
```
Next step is to optimize the recusion into dynamical programming, which is quite obvious, we just build a matrix `dp` of shape `(m, n)`. to represent `dp[i][j] = f(x[:i], y[:j])`. So the core algorithm could be written as:
```python
if x[i] == y[j]:
		dp[i][j] = 1 + dp[i-1][j-1]
else:
		dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

So for this problem, it seems like they need us to find a _**continuous**_ subarray, so the core could be slightly modified to be:

```python
if x[i] == y[j]:
		dp[i][j] = 1 + dp[i-1][j-1]
else:
		dp[i][j] = 0
```