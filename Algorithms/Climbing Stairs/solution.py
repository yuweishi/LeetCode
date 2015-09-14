class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        way1, way2 = 1, 0
        for i in range(1, n):
            way1 = way1 + way2
            way2 = way1 - way2
        return way1 + way2
