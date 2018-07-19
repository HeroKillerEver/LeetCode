class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        layer, res = 0, 0
        for s in S:
            if s == '(':
                layer += 1
                flag = 1
            else:
                if flag:
                    res +=  2**(layer-1)
                    flag = 0
                layer -= 1
        return res