class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict = collections.defaultdict(int);
        for i in xrange(len(s)):
            dict[s[i]] += 1
            dict[t[i]] -= 1
        for v in dict.values():
            if v:
                return False
        return True
