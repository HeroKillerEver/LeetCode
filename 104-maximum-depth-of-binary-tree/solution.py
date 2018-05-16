# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


from collections import deque
class Solution(object):
    def maxDepth_2(self, root):
        if not root: return 0
        level = {root: 1}
        queue = deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                level[node.left] = 1 + level[node]
            if node.right:
                queue.append(node.right)
                level[node.right] = 1 + level[node]
        return max(level.values())