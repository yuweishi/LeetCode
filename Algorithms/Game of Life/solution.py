class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                for p in xrange(max(0, i - 1), min(m, i + 2)):
                    for q in xrange(max(0, j - 1), min(n, j + 2)):
                        count += board[p][q] % 2
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
