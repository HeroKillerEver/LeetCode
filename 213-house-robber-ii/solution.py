class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1, cur1, prev2, cur2 = 0, 0, 0, 0
        for i in range(len(nums)-1):
            cur1, prev1 = max(cur1, prev1 + nums[i]), cur1
        for i in range(1, len(nums)):
            cur2, prev2 = max(cur2, prev2 + nums[i]), cur2
        return nums[0] if len(nums) == 1 else max(cur1, cur2)