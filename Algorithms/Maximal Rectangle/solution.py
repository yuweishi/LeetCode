class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        dp = [0] * len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            res = max(res, self.largestRectangleArea(dp))
        return res
            
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                length = (i - 0) if not stack else i - (stack[-1] + 1)
                res = max(res, length * h)
            stack.append(i)
        return res
