class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, i, j, word, 0):
                    return True
        return False
    def check(self, board, i, j, word, pos):
        if pos == len(word):
            return True
        if i < len(board) and i >= 0 and j < len(board[0]) and j >= 0 and board[i][j] != '*' and board[i][j] == word[pos]:
            cur = board[i][j]
            #visit.add((i, j))
            board[i][j] = '*'
            pos += 1
            if self.check(board, i, j + 1, word, pos):
                return True
            if self.check(board, i, j - 1, word, pos):
                return True
            if self.check(board, i + 1, j, word, pos):
                return True
            if self.check(board, i - 1, j, word, pos):
                return True
            #visit.remove((i, j))
            board[i][j] = cur
        return False
