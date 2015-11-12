class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.dp = [[0] * (1 + len(matrix[0]) if len(matrix) else 0) for i in xrange(len(matrix) + 1)]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                self.dp[i + 1][j + 1] = self.dp[i][j + 1] + self.dp[i + 1][j] - self.dp[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
