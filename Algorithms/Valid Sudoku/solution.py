class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Method 1: n = 9 *9, use O(9) space and O(3 * n) time complexity
        dict0 = {}
        for i in range(1, 10):
            dict0[str(i)] = 0
        for i in range(9):
            dict = dict0.copy()
            for j in range(9):
                if board[i][j] != '.':
                    if dict[board[i][j]]:
                        return False
                    dict[board[i][j]] = 1
        for i in range(9):
            dict = dict0.copy()
            for j in range(9):
                if board[j][i] != '.':
                    if dict[board[j][i]] == 1:
                        return False
                    dict[board[j][i]] = 1
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                dict = dict0.copy()
                for p in range(i, i + 3):
                    for q in range(j, j + 3):
                        if board[p][q] != '.':
                            if dict[board[p][q]]:
                                return False
                            dict[board[p][q]] = 1
        return True
        
        #Method 2: use O(n) time, and O(3 * n) space complexity
        row, col, cube = [[0] * 9 for i in range(9)], [[0] * 9 for i in range(9)], [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    k = i / 3 * 3 + j / 3
                    num = int(board[i][j]) - 1
                    if row[i][num] or col[j][num] or cube[k][num]:
                        return False
                    row[i][num] = 1
                    col[j][num] = 1
                    cube[k][num] = 1
        return True
