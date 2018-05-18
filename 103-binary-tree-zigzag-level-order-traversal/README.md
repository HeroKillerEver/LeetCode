## Idea

just _BFS_ right, when `level` goes up: 
```
result.append([])
```
for the nodes in the same level:
```
result[-1].append(node.val)
```

_Note_:  
```
if level % 2:
		res[-1].append(node.val)
else:
		res[-1].appendleft(node.val)
```