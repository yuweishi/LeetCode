class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return len(s)
        res = 0
        start1 = start2 = -1
        for i in xrange(1, len(s)):
            #same as previous one, do not move pointers
            if s[i] == s[i - 1]:
                continue
            #diff with previous one, but there're two different characters in total, only update start2
            if start2 < 0 or s[start2] == s[i]:
                start2 = i - 1
            #diff with previous one, there're 3 different characters in total, update res, start1 and start2
            else:
                res = max(res, i - start1 - 1)
                start1 = start2
                start2 = i - 1
        return max(res, len(s) - start1 - 1)
                
