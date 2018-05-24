class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [1.0] + [0.0] * N
        for n in range(1, N+1):
            start = max(n-W, 0)
            if n <= K:
                dp[n] = sum(dp[start: n]) / W
            else:
                dp[n] = sum(dp[start: K]) / W if dp[start: K] else 0
        return sum(dp[K:])