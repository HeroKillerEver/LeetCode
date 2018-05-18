## Idea
​
This problem is not difficult to come up with a solution, we just split the `version` into list:
```
v = deque(version.split('.'))
```
then we compare the `element` of `v1` and `v2`, if they are different we just return which one is higher; if they are the same, then we just pop the `element`.
​
When `v1` or `v2` is `[]`, we find out which one is `[]`, return the one which is not `[]`. 
​
_Note_: it is very funny that there are version like `5.0.0.0.0` and `5.0`, they are the same version. 