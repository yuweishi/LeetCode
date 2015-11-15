class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Method 1: use two pointers
        res = 0
        count = 0
        start = -1
        for i in xrange(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                res = max(res, i - start)
            if count == -1:
                start = i
                count = 0
        start = -1
        count = 0
        s1 = s[::-1]
        for i in xrange(len(s1)):
            if s1[i] == ')':
                count += 1
            else:
                count -= 1
            if count == 0:
                res = max(res, i - start)
            if count == -1:
                start = i
                count = 0
        return res

        #Method 2: use stack
        stack = []
        for i in xrange(len(s)):
            if s[i] == '(':
                stack += [i]
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack += [i]
        if not stack:
            return len(s)
        res = start = 0
        end = len(s)
        while stack:
            start = stack.pop()
            res = max(res, end - start - 1)
            end = start
        return max(res, end)
