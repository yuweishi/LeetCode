class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #Method1: compare each character twice
        res = []
        i = 0
        n = len(s)
        while i < n - 1:
            if s[i: i + 2] == '++':
                res += [s[:i] + '--' + s[i + 2:]]
            i += 1
        return res

	#Method2: compare each character once
        n, i, res = len(s), 0, []
        while i < n - 1:
            if s[i] == '+':
                while i + 1 < n and s[i + 1] == '+':
                    res += [s[:i] + '--' + s[i + 2:]]
                    i += 1
            i += 1
        return res
