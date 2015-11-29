class Solution(object):
    #Method 1: dp
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for i in xrange(m + 1)]
        dp[0][0] = True
        for i in xrange(n):
            if p[i] == '*':
                #if found any consective '*' or '*' in p[0], invalid input
                if i == 0 or p[i - 1] == '*':
                    return False
                if dp[0][i - 1]:
                    dp[0][i + 1] = True
        #go through the array
        for i in xrange(m):
            for j in xrange(n):
                if dp[i][j] and (p[j] == '.' or s[i] == p[j]) or \
                p[j] == '*' and (dp[i + 1][j - 1] or dp[i][j + 1] and (p[j - 1] == '.' or s[i] == p[j - 1])):
                    dp[i + 1][j + 1] = True
        return dp[-1][-1]
