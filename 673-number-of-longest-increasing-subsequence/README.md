## Idea

This problem is a modified version of [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence). 

For this problem, we still need to find out the _LIS_, which is quite simple:
```python
for j in range(i):
	if nums[i] > nums[j]:
		dp[i] = max(dp[i], dp[j]+1)		
```
Note that `dp[i]` represents for the _LIS_ for element `i`. if `dp[i] == dp[j] + 1 and nums[i] > nums[j]`, this means that element `i` can be accessed from `j`:
```python
for j in range(i):
	if dp[i] == dp[j] + 1 and nums[i] > nums[j]:
		count[i] += count[j]
```