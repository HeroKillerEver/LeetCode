# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        max_list = [-float('inf')] * 10000
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                max_list[level] = max(max_list[level], node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return max_list[:level]



from collections import deque
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        cur_max = -float('inf')
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if len(result) < level:
                    result.append(cur_max)
                    cur_max = -float('inf')
                cur_max = max(cur_max, node.val)
                queue.extend([(node.left, level+1), (node.right, level+1)])
        return result + ([cur_max] if cur_max != -float('inf') else [])