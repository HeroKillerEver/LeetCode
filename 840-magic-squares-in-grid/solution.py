class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        if m < 3 or n < 3: return res
        else:
            for i in range(m-2):
                for j in range(n-2):
                    res += self.check(grid[i][j], grid[i][j+1], grid[i][j+2], 
                                      grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                                      grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
        return res
        
    
    def check(self, a,b,c,d,e,f,g,h,i):
        
        all_set = set((1, 2, 3, 4, 5, 6, 7, 8, 9))
        return (a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g) \
                and all_set == set([a,b,c,d,e,f,g,h,i])