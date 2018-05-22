# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        Recursive Traversal, trivial
        """
        if root is None:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
        
class Solution(object):
    def preorderTraversal_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        Iterative Traversal
        """
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.extend([node.right, node.left])
                res.append(node.val)
        return res