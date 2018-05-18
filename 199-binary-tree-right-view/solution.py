# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if level > len(res):
                    res.append(stack.pop())
                stack.append(node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return res + ([stack.pop()] if stack else [])