class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            res += [2 ** i + pre for pre in res[::-1]]
        return res
