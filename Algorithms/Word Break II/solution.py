class Solution(object):
    #Method 1: use dict to record all possible break ways, do not cache result
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

    #Method 2: use cache
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        #if input is empty, return [] directly
        if not s: return []
        #if not breakable, return []
        dp = [0]
        for i in xrange(1, len(s) + 1):
            for start in reversed(dp):
                if s[start: i] in wordDict:
                    dp += [i]
                    break
        if dp[-1] != len(s): return []
        #otherwise, generate the result one by one, cache previous result at the same time
        return self.insert(collections.defaultdict(list), dp, 0, len(dp) - 1, s, wordDict)
        
    def insert(self, map, dp, start, end, s, wordDict):
        string = s[dp[start]: dp[end]]
        #check whether we can get the result form cache directly
        if string in map:
            return map[string]
        #if couldn't, check whether the whole string in wordDict or not, if yes, add it
        res = [string] if string in wordDict else []
        #otherwise, try to break it and repeat this process
        for i in xrange(start + 1, end):
            if s[dp[start]: dp[i]] in wordDict:
                substr = s[dp[start]: dp[i]]
                res += [substr + ' ' + item for item in self.insert(map, dp, i, end, s, wordDict)]
        map[string] = res
        return res
