class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        for i in xrange(1, len(s) + 1):
            if s[:i] == s[i-1::-1]:
                res += [[s[:i]] + list for list in self.partition(s[i:])]
        return res if res else [[]]
