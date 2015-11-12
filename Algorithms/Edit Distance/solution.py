class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        dp = range(len2 + 1)
        for i in xrange(len1):
            pre = i + 1
            for j in xrange(len2):
                if word1[i] != word2[j]:
                    cur = min(pre, dp[j], dp[j + 1]) + 1
                else:
                    cur = dp[j]
                dp[j] = pre
                pre = cur
            dp[len2] = pre
        return dp[-1]
