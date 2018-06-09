class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        """
        This problem is the same as LCS
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] += 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])            
        return m + n - (2*dp[-1][-1] if dp and dp[0] else 0)