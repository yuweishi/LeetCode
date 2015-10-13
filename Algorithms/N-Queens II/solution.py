class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.search([0], n, 0, ['.' * n for i in xrange(n)], [0] * n, set(), set())[0]
    
    def search(self, res, n, col, cur, flagrow, flag45, flag135):
        if col == n:
            res[0] += 1
        else:
            for row in xrange(n):
                if not (flagrow[row] or (row - col) in flag45 or (row + col) in flag135):
                    flag45.add(row - col)
                    flag135.add(row + col)
                    flagrow[row] = 1
                    new = cur[:]
                    new[row] = '.' * (col) + 'Q' + '.' * (n - col - 1)
                    self.search(res, n, col + 1, new, flagrow, flag45, flag135)
                    flag45.remove(row - col)
                    flag135.remove(row + col)
                    flagrow[row] = 0
        return res
