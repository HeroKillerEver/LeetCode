class Solution:
    def minimumDeleteSum_1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        """
        recursive solution with memorization: TLE
        """
        self.memo = {}
        return self.minimum(s1, s2)
    
    def minimum(self, s1, s2):
        if (s1, s2) in self.memo: return self.memo[(s1, s2)]
        
        if not s1:
            self.memo[(s1, s2)] = sum([ord(x) for x in s2])
            return self.memo[(s1, s2)]
        
        if not s2:
            self.memo[(s1, s2)] = sum([ord(x) for x in s1])   
            return self.memo[(s1, s2)]
        
        if s1[-1] != s2[-1]:
            self.memo[(s1, s2)] = min(self.minimum(s1[:-1], s2) + ord(s1[-1]),
                                      self.minimum(s1, s2[:-1]) + ord(s2[-1]))
            return self.memo[(s1, s2)]
        if s1[-1] == s2[-1]:
            return self.minimum(s1[:-1], s2[:-1])
        
class Solution:
    def minimumDeleteSum_2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        """
        dp[i][j] = min(s1[i:], s2[j:])
        dp[i][j] = min(dp[i+1][j] + s1[i+1], dp[i][j+1] + s2[j+1])
        """
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in reversed(range(m)):
            dp[i][n] = dp[i+1][n] + ord(s1[i])
        for j in reversed(range(n)):
            dp[m][j] = dp[m][j+1] + ord(s2[j])
        for i in reversed(range(m)):
            for j  in reversed(range(n)):
                if s1[i] == s2[j]: dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        return dp[0][0]       
        