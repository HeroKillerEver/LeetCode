class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        """
        Recursive solution with memorization: AC
        """
        self.memo = {}
        return self.prob(N, N) if N < 5000 else 1


    def prob(self, n1, n2):
        if (n1, n2) in self.memo: return self.memo[(n1, n2)]
        if n1 <= 0 and n2 <= 0: return 0.5
        if n1 <= 0: return 1
        if n2 <= 0: return 0
        self.memo[(n1, n2)] = 0.25 * (self.prob(n1-100, n2) + self.prob(n1-75, n2-25) 
                                      + self.prob(n1-50, n2-50) + self.prob(n1-25, n2-75)) 
        return self.memo[(n1, n2)]   