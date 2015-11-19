class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #Method 1: DP
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if (n1 + n2) != n3:
            return False
        dp = [[False] * (n1 + 1) for i in xrange(n2 + 1)]
        dp[0][0] = True
        for i in xrange(n2 + 1):
            for j in xrange(n1 + 1):
                cur = i + j - 1
                if i and s3[cur] == s2[i - 1] and dp[i - 1][j] or j and s3[cur] == s1[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]

	#Method 2: BFS, worst case O(mn) time, O(mn) space
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if (n1 + n2) != n3:
            return False
        queue = [(0, 0)]
        visit = set()
        #(x, y) represent string contains s1[0, x) and s2[0, y)
        while queue:
            x, y = queue.pop(0)
            if x == n1 and y == n2:
                return True
            if (x, y) in visit:
                continue
            if x < n1 and s3[x + y] == s1[x]:
                queue += [(x + 1, y)]
            if y < n2 and s3[x + y] == s2[y]:
                queue += [(x, y + 1)]
            visit.add((x, y))
        return False

	#Method 3: DFS, worst case O(mn) time, O(mn) space
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if (n1 + n2) != n3:
            return False
        stack = [(0, 0)]
        visit = set()
        #(x, y) represent string contains s1[0, x) and s2[0, y)
        while stack:
            x, y = stack.pop()
            if x == n1 and y == n2:
                return True
            if (x, y) in visit:
                continue
            if x < n1 and s3[x + y] == s1[x]:
                stack += [(x + 1, y)]
            if y < n2 and s3[x + y] == s2[y]:
                stack += [(x, y + 1)]
            visit.add((x, y))
        return False
