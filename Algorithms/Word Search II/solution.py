class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        res = set()
        for word in words:
            self.insert(trie, word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.check(board, i, j, trie, res, "")
        return list(res)
        
    def insert(self, root, word):
        for char in word:
            if char not in root:
                root[char] = {}
            root = root[char]
        root[None] = None
        
    def check(self, board, i, j, trie, res, pre):
        if i < len(board) and i >= 0 and j < len(board[0]) and j >= 0 and board[i][j] != '*' and board[i][j] in trie:
            #visit.add((i, j))
            pre += board[i][j]
            board[i][j] = '*'
            subtrie = trie[pre[-1]]
            if None in subtrie:
                res.add(pre)
            self.check(board, i, j + 1, subtrie, res, pre)
            self.check(board, i, j - 1, subtrie, res, pre)
            self.check(board, i + 1, j, subtrie, res, pre)
            self.check(board, i - 1, j, subtrie, res, pre)
            #visit.remove((i, j))
            board[i][j] = pre[-1]
