class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []
        m, x, n = len(A), len(B), len(B[0])
        res = [[0] * n for i in xrange(m)]
        for i in xrange(m):
            for k in xrange(x):
                if A[i][k]:
                    for j in xrange(n):
                        if B[k][j]:
                            res[i][j] += A[i][k] * B[k][j]
        return res
