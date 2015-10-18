class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s: return True
        dp = [0]
        for i in xrange(1, len(s) + 1):
            for start in reversed(dp):
                if s[start: i] in wordDict:
                    dp += [i]
                    break
        return dp[-1] == len(s)
