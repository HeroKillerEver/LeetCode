class Solution(object):
    def findKthLargest_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1] # O(nlgn)

    def findKthLargest_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        for num in nums[:k]:
            heapq.heappush(res, num)
        for num in nums[k:]:
            heapq.heappushpop(res, num)
        return heapq.heappop(res) # (k + (n-k) * lgk)
