class Solution(object):
    def missingNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Gauss formula
        """
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

class Solution(object):
    def missingNumber_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        bit manipulation
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

