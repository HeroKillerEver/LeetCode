class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        length = len(S)
        ls = map(ord, S)
        total = sum(shifts)
        for i in range(length):
            ls[i] += total % 26
            total -= shifts[i] 
        return ''.join(map(chr, [i if i <= 122 else i - 26 for i in ls]))