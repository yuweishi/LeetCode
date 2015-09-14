class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 1 or k == 0:
            return n * k
        count1, count2 = k, 0
        for i in range(1, n):
            temp = (k - 1) * (count2 + count1)
            count2 = count1
            count1 = temp
        return count1 + count2
