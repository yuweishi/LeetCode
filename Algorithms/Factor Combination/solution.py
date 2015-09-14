class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.factors(2, n, [], res)
        return res
    def factors(self, start, n, pre, res):
        while start ** 2 <= n:
            if n % start == 0:
                res += [pre + [start, n / start]]
                self.factors(start, n / start, pre + [start], res)
            start += 1
