class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0
        dp = [1] * (1 + len(s))
        for i in xrange(len(t)):
            pre = 0
            for j in xrange(len(s)):
                cur = pre + (dp[j] if s[j] == t[i] else 0)
                dp[j] = pre
                pre = cur
            dp[-1] = pre
        return dp[-1]
