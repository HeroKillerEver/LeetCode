class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.grayCode(n-1) + [2**(n-1) + x for x in reversed(self.grayCode(n-1))] if n else [0]