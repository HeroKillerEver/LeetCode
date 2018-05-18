# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if len(result) < level:
                    result.append([])
                result[-1].append(node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return result
        