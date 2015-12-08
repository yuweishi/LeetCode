class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #discard all 0s in nums
        nums_new = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums_new)
        dp = [[0] * n for _ in xrange(n)]
        #dp[i][j] represent the max value we can obtain by burst the balloons within i and j
        for length in xrange(2, n):
            for left in xrange(0, n - length):
                right = left + length
                for i in xrange(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                           nums_new[left] * nums_new[i] * nums_new[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
