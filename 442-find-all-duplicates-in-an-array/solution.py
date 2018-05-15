class Solution(object):
    def findDuplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Hash table
        time: O(n)
        space: O(n)
        """
        out = []
        seen = set()
        for item in nums:
            if item in seen: out.append(item)
            else: seen.add(item)
        return out


class Solution(object):
    def findDuplicates__2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        time: O(n)
        space: O(1)
        """
        result = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] *= -1
            else:
                result.append(abs(num))
        return result
