class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = [], []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    row += [i]
                    col += [j]
        col.sort()
        res, left, right = 0, 0, len(row) - 1
        while left < right:
            res += row[right] - row[left] + col[right] - col[left]
            right -= 1
            left += 1
        return res
