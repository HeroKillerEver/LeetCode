# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([(root, 1)])
        res = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level:
                    res.append(deque([]))
                if level % 2:
                    res[-1].append(node.val)
                else:
                    res[-1].appendleft(node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return [list(r) for r in res]