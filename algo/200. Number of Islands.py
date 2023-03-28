class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(r,c)
                if (grid[r][c] == "1"):
                    self.helper(grid, r, c)
                    counter += 1
        return counter

    def helper(self, grid, x, y):
        if (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'):
            grid[x][y] = '#'
            self.helper(grid, x-1, y)
            self.helper(grid, x, y-1)
            self.helper(grid, x+1, y)
            self.helper(grid, x, y+1)

        