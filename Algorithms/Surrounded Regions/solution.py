class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        for i in xrange(m):
            if board[i][0] == 'O':
                self.bfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.bfs(board, i, n - 1)
        for j in xrange(n):
            if board[0][j] == 'O':
                self.bfs(board, 0, j)
            if board[m - 1][j] == 'O':
                self.bfs(board, m - 1, j)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def bfs(self, board, i, j):
        queue = [(i, j)]
        while queue:
            (i, j) = queue.pop(0)
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
                board[i][j] = 'N'
                queue += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            
