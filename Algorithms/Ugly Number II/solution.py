class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] + [0] * (n - 1)
        index2, index3, index5 = 0, 0, 0
        u2, u3, u5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(u2, u3, u5)
            if ugly[i] == u2:
                index2 += 1
                u2 = 2 * ugly[index2]
            if ugly[i] == u3:
                index3 += 1
                u3 = 3 * ugly[index3]
            if ugly[i] == u5:
                index5 += 1
                u5 = 5 * ugly[index5]
        return ugly[-1]
