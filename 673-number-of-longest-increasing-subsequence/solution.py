class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        max_len = 1
        m = len(nums)
        dp = [1] * m
        count = [0] * m  
        count[0] = 1
        for i in range(m):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] > max_len:
                        max_len = dp[i]
            for j in range(i):
                if dp[i] == dp[j] + 1 and nums[i] > nums[j]:
                    count[i] += count[j]
            if count[i] == 0:
                count[i] = 1 
        return sum([count[i] for i, item in enumerate(dp) if item == max_len])