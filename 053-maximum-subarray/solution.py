class Solution(object):
    def maxSubArray_1(self, nums):
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)


class Solution(object):
    def maxSubArray_1(self, nums):
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(cursum+num, num)
            maxsum = max(maxsum, cursum)
        return maxsum