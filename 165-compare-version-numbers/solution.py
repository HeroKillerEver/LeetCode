from collections import deque
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = deque(version1.split('.'))
        v2 = deque(version2.split('.'))
        while v1 and v2:
            if int(v1[0]) > int(v2[0]): return 1
            elif int(v1[0]) < int(v2[0]): return -1
            else:
                v1.popleft()
                v2.popleft()
        if sum(map(int,v1)): return 1
        if sum(map(int,v2)): return -1
        return 0