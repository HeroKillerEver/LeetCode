class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], idx]
            else:
                dic[num] = idx
        