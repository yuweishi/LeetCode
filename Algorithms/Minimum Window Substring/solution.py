class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = collections.Counter(t)
        start, end, count, j = 0, float('inf'), len(t), 0
        for i in xrange(len(s)):
            if s[i] in dict:
                #if there's any missing s[i]
                if dict[s[i]] > 0:
                    count -= 1
                dict[s[i]] -= 1
                #when we meet a start point which is valid, stop here
                while j < i and not (s[j] in dict and dict[s[j]] >= 0):
                    if s[j] in dict:
                        dict[s[j]] += 1
                    j += 1
                #update start, end
                if not count and end - start > i - j:
                    end, start = i, j
        return "" if count else s[start: end + 1]
