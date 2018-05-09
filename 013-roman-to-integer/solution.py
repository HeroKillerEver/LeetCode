class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        length = len(s)
        result = 0
        for i in range(length-1):
            if dic[s[i]] < dic[s[i+1]]:
                sign = -1
            else:
                sign = 1
            result += sign * dic[s[i]]
        
        return result + dic[s[-1]]