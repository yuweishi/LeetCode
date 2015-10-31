class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method 1: time complexity O(n2), space complexity O(n2) 
        n = len(s)
        dp = [i for i in xrange(-1, n)]
        pal = [[False for j in xrange(i + 1)] for i in xrange(n)]
        for end in xrange(n):
            for start in xrange(end, -1, -1):
                if s[start] == s[end] and (end - start <= 2 or pal[end - 1][start + 1]):
                    pal[end][start] = True
                    dp[end + 1] = min(dp[end + 1], 1 + dp[start])
        return dp[-1]

        #Method 2: time complexity O(n2), space complexity O(n) 
        n = len(s)
        dp = [i for i in xrange(-1, n)]
        for center in xrange(n):
            size = 0
            while (center - size >= 0 and center + size < n) and s[center + size] == s[center - size]:
                    dp[center + size + 1] = min(dp[center + size + 1], 1 + dp[center - size])
                    size += 1
            size = 1
            while (center - size + 1 >= 0 and center + size < n) and s[center + size] == s[center - size + 1]:
                    dp[center + size + 1] = min(dp[center + size + 1], 1 + dp[center - size + 1])
                    size += 1
        return dp[-1]
