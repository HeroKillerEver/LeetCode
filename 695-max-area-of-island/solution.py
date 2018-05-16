class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        result = [[None] * self.n for _ in range(self.m)]
        self.seen = set()
        max_area = 0
        for m in range(self.m):
            for n in range(self.n):
                max_area = max(max_area, self.maxArea(m, n, grid))
                # result[m][n] = self.maxArea(m, n, grid)
        return max_area
        
        
    def maxArea(self, i, j, grid):
        if (i, j) in self.seen or grid[i][j] == 0:
            return 0
        self.seen.add((i, j))
        up = 0 if i == 0 else self.maxArea(i-1, j, grid)
        down = 0 if i == self.m - 1 else self.maxArea(i+1, j, grid)
        left = 0 if j == 0 else self.maxArea(i, j-1, grid) 
        right = 0 if j == self.n - 1 else self.maxArea(i, j+1, grid)
        return 1 + up + down + left + right