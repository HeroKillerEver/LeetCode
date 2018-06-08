class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
        dp[0][i][j] = 1
        res = 0
        for NN in range(N):
            for mm in range(m):
                for nn in range(n):
                    left = dp[NN][mm-1][nn] if mm-1 >= 0 else 0
                    right = dp[NN][mm+1][nn] if mm+1 < m else 0 
                    down = dp[NN][mm][nn-1] if nn-1 >= 0 else 0 
                    up = dp[NN][mm][nn+1] if nn+1 < n else 0 
                    dp[NN+1][mm][nn] +=  left + right + up + down  
                    if mm-1 < 0:
                        res += dp[NN][mm][nn]
                    if mm+1 >= m:
                        res += dp[NN][mm][nn]
                    if nn-1 < 0:
                        res += dp[NN][mm][nn]
                    if nn+1 >= n:
                        res += dp[NN][mm][nn]
        return res % (10**9 + 7)
        