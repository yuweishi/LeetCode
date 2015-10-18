class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s: return []
        
        dp = collections.defaultdict(list)
        dp[0] = []
        for i in xrange(1, len(s) + 1):
            now = dp.keys()
            for start in now:
                if s[start: i] in wordDict:
                    dp[i] += [start]
        return self.insert([], dp, len(s), s, "")
        
    def insert(self, res, dp, end, s, pre):
        for start in dp[end]:
            if start == 0:
                res += [s[start: end] + pre]
            else:
                self.insert(res, dp, start, s, " " + s[start: end] + pre)
        return res
