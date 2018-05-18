## Idea

Personally I do think this problem is quite similar to [515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/). 

The idea is to use a `stack` to keep track of every node we encountered, when `level` goes up, we just pop item `stack.pop()` and `result.append(stack.pop())`