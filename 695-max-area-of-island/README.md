## Idea

Suppose we had a solver `maxArea` which can return the max island based on `grid[i][j]`. So the transition function can be written as:
```
maxArea(grid[i][j]) = 1 + maxArea(grid[i-1][j]) + maxArea(grid[i+1][j]) + maxArea(grid[i][j-1]) + maxArea(grid[i][j+1])
```

_Note_: 1. to reduce repetition, we need to keep a `seen` set to keep track of the node `grid[i][j]` we have already visited, and return `0`. 2. if `grid[i][j] = 0`, then the island is disconnected, we need to return `0`