class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if abs(n - m) > 1:
            return False
        for i in xrange(min(m, n)):
            if s[i] != t[i]:
                ps = i + (1 if n <= m else 0)
                pt = i + (1 if n >= m else 0)
                return s[ps:] == t[pt:]
        return n != m
