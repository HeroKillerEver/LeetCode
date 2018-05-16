import math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        (m + m+k-1) * k / 2 = N
        k**2 +  (2*m - 1)*k - 2*N = 0
        m = ( 2*N - k**2 + k ) / (2*k)
        """
        K = int(math.ceil(0.5 * (-1 + math.sqrt(1+8*N))))
        result = 0
        for k in range(1, K+1):
            if (2*N - k**2 + k) / (2.*k) == int((2*N - k**2 + k) / (2.*k)):
                result += 1
        return result