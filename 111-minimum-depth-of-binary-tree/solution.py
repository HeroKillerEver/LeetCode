# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if node:
                queue.extend([(node.left, level+1), (node.right, level+1)])
                if not node.left and not node.right:
                    return level
        return 0

class Solution(object):
    def minDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))