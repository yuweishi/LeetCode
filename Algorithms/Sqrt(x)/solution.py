class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        start, end = 1, x
        while start < end - 1:
            mid = (start + end) / 2
            if mid ** 2 > x:
                end = mid
            elif mid ** 2 < x:
                start = mid
            else:
                return mid
        return start
