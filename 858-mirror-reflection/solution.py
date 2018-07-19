class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        m = self.gcd(p, q)
        x, y = (p/m) % 2, (q/m) % 2
        return 0 if (x, y) == (1, 0) else 1 if (x, y) == (1, 1) else 2
        
    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a