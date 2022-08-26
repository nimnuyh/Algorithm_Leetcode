class Solution(object):
    def DFS(self, grid, x, y) :
        if x < 0 or y < 0 or x >= self.x_range or y >= self.y_range or grid[y][x] == 0 :
            return
        else :
            self.area += 1
            grid[y][x] = 0
            self.DFS(grid, x + 1, y)
            self.DFS(grid, x, y + 1)
            self.DFS(grid, x - 1, y)
            self.DFS(grid, x, y - 1)
    
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if sum([sum(x) for x in grid]) == 0 :
            return 0
        
        self.y_range = len(grid)
        self.x_range = len(grid[0])
        self.ans = []
        for y in range(self.y_range) :
            for x in range(self.x_range) :
                if grid[y][x] == 1 :
                    self.area = 0
                    self.DFS(grid, x, y)
                    self.ans.append(self.area)
        return max(self.ans)