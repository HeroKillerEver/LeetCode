## Idea

This problem is just to use _BFS_ to keep track of the largest element in each row.  The first naive approach comes into my mind it to build a `max_list` to correspond to the level:
```
max_list = [-float('inf')] * 10000
max_list[level] = max(max_list[level], node.val)
```
This is quite intuitive, the problem for this approach is that we don't know the height of the tree, which is not very optimal. 

------------

Let's try to improve this, we just build one single temp value `cur_max` and compare:
```
cur_max = max(cur_max, node.val)
```
if `level` go up, we just `result.append(cur_max)` then reset `cur_max = -float('inf')`
