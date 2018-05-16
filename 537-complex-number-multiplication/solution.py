class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, (a.strip('i')).split('+'))
        b1, b2 = map(int, (b.strip('i')).split('+'))
        A, B = a1*b1 - a2*b2, a1*b2 + a2*b1
        return '{}+{}i'.format(A, B)   