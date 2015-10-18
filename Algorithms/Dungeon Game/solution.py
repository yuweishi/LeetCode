class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]: return
        m, n = len(dungeon), len(dungeon[0])
        ans = [[0] * n for i in xrange(m)]
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if j == n - 1 and i == m - 1:
                    ans[i][j] = 1 - dungeon[i][j]
                elif j == n - 1:
                    ans[i][j] = ans[i + 1][j] - dungeon[i][j]
                elif i == m - 1:
                    ans[i][j] = ans[i][j + 1] - dungeon[i][j]
                else:
                    ans[i][j] = min(ans[i + 1][j], ans[i][j + 1]) - dungeon[i][j]
                ans[i][j] = max(1, ans[i][j])
        return ans[0][0]
