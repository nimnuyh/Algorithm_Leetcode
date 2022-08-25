class Solution(object):
    def DFS(self, grid, x, y) :
        if x < 0 or y < 0 :
            return
        elif x >= self.x_range or y >= self.y_range :
            return
        elif grid[y][x] == '0' :
            return
        else :
            grid[y][x] = '0'
            self.DFS(grid, x + 1, y)
            self.DFS(grid, x, y + 1)
            self.DFS(grid, x - 1, y)
            self.DFS(grid, x, y - 1)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.y_range = len(grid)
        self.x_range = len(grid[0])
        self.ans = 0
        for x in range(self.x_range) :
            for y in range(self.y_range) :
                if grid[y][x] == '1' :
                    self.DFS(grid, x, y)
                    self.ans += 1
        return self.ans