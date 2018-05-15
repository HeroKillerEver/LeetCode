class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
        return [idx+1 for idx, num in enumerate(nums) if num > 0]