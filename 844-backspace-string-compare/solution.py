class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for s in S:
            if s == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(s)
        
        for t in T:
            if t == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(t)
        
        return stack1 == stack2