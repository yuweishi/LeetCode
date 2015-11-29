class Solution(object):
    #Method 1: DP
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        if n - p.count('*') > m:
            return False
        dp = [[False] * (n + 1) for i in xrange(m + 1)]
        dp[0][0] = True
        for i in xrange(n):
            if p[i] == '*' and dp[0][i]:
                dp[0][i + 1] = True
        #go through the array
        for i in xrange(m):
            for j in xrange(n):
                if dp[i][j] and (p[j] == '?' or s[i] == p[j]) or \
                p[j] == '*' and (dp[i + 1][j] or dp[i][j + 1] or dp[i][j]):
                    dp[i + 1][j + 1] = True
        return dp[-1][-1]

    #Method 2: Greedy
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        i = j = 0
        star = -1
        while i < m:
            #both i, j need to move one step forward
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            #meet '*', move j, try to match without '*', record corresponding i's position
            elif j < n and p[j] == '*':
                j += 1
		star = j
                i1 = i
            #if there's no match, check if there's any star before to help.
            #try to match from i1 instead of from i
            elif star != -1:
                i1 += 1
                i = i1
                j = star
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n
