class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        for i in range(m):
            for j in range(m//2):
                A[i][j], A[i][~j] = A[i][~j], A[i][j]
        for i in range(m):
            for j in range(m): 
                A[i][j] ^= 1
        return A