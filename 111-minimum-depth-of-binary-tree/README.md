## Idea

This problem is quite similar to [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/), we also attack this problem using two approach _BFS_ and _DFS_. 

### BFS
Since _BFS_ runs layer-wise, so once we experience a leave node `not node.left and not node.right == 1`, we just return the `level` of this node. 

### DFS

Compared to [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/), we can come up with a naive recursive algorithm:
```
if not root:
		return 0
return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```
_Note_: there will be probelm when `node` have only `1` child, the algorithm will return `0` which is not correct.

A modified version:
```
if not root:
		return 0
if not root.left or not root.right:
		return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
```

