class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = {}
        dic[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dic.setdefault(i, 0)
                dic[i] = max(dic[i], max(j, dic[j]) * max(i-j, dic[i-j]))
        return dic[n]