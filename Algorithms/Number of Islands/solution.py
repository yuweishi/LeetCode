class Solution(object):
    #Method 1: bfs
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.bfs(grid, [[i, j]])
                    count += 1
        return count
    def bfs(self, grid, queue):
        while queue:
            [i, j] = queue.pop(0)
            if i >=0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                queue += [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]

    #Method 2: dfs
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, i, j):
        if i >=0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            for (x, y) in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                self.dfs(grid, x, y)
