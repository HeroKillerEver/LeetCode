import numpy as np
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        A = np.array(A)
        B = np.array(B)
        H, W = A.shape
        pad = A.shape[0] - 1
        A_pad = np.pad(A, pad, mode='constant')
        Hout = Wout = 2*pad + 1
        conv = np.zeros(shape=(Hout, Wout))
        for h in range(Hout):
            for w in range(Wout):
                conv[h, w] = np.sum(B * A_pad[h:h+H, w:w+W])
        return int(np.max(conv))
        