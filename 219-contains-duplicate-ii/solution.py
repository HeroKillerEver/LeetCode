class Solution(object):
    def containsNearbyDuplicate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        Brute force
        time: O(nk)
        space: O(1)
        """
        length = len(nums)
        for i in range(length):
            for j in range(max(0, i-k), min(i+k+1, length)):
                if nums[i] == nums[j]: 
                    if i != j:
                        return True
        return False

class Solution(object):
    def containsNearbyDuplicate_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        Hash table
        time: O(n)
        space: O(n)
        """
        dic = {}
        length = len(nums)
        for i in range(length-1):
            dic[nums[i]] = i
            if nums[i+1] in dic:
                if i+1 - dic[nums[i+1]] <= k:
                    return True
        return False