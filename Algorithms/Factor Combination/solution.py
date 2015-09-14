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
        if n == 1:
            if len(pre) > 1:
                res += [pre]
            return
        while start ** 2 <= n:
            if n % start == 0:
                self.factors(start, n / start, pre + [start], res)
            start += 1
        self.factors(n, 1, pre + [n], res)
