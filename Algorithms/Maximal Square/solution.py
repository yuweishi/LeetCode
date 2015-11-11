class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = pre = 0
        dp = [0] * (len(matrix[0]) + 1)
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                temp = dp[j +1]
                if matrix[i][j] == "1":
                    dp[j + 1] = 1 + min(dp[j], dp[j + 1], pre)
                    res = max(res, dp[j + 1])
                else:
                    dp[j + 1] = 0
                pre = temp
        return res * res
