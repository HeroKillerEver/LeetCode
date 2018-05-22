## Idea

For a tree travesal problem, we have two approaches to takle it: _BFS_ and _DFS_. 

For a _BFS_, we just use a queue, it is the same as [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/), the code is following:
```python
res = []
queue = deque([root])
while queue:
		node = queue.popleft()
		if node:
				res.append(node.val)
				queue.extend([node.left, node.right])
return res
```
By changing the `queue` to `stack`, it will naturally give us _DFS_ search. This corresponds to __reorder__:
```python
res = []
stack = [root]
while stack:
		node = stack.pop()
		if node:
				stack.extend([node.right, node.left])
				res.append(node.val)
return res
```