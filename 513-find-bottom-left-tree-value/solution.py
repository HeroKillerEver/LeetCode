# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level:
                    res.append(node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return res[-1]