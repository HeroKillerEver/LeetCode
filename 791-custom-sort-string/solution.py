class Solution(object):
    def customSortString_1(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {}
        prefix = []
        suffix = []
        for idx, s in enumerate(S):
            dic[s] = idx
        for t in T:
            if t in dic:
                prefix.append((t, dic[t]))
            else:
                suffix.append(t)
        prefix.sort(key=lambda x: x[1])
        suffix.sort()
        return ''.join([char for char, key in prefix]) + ''.join(suffix)

class Solution(object):
    def customSortString_2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        return ''.join(sorted(T,key=lambda x: S.index(x) if x in S else ord(x)))
