## Idea

just _BFS_ right, when `level` goes up, we insert a new list `[]` at the beginning of `result`:
```
result.insert(0, [])
```
for the nodes in the same level:
```
result[0].append(node.val)
```