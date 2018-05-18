# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        queue.append((root, 0))
        while queue:
            node, level = queue.pop(0)
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[0].append(node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return res