class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype: int
            """
        dict, i, length, left = {}, 0, 0, 0
        while i < len(s):
            if s[i] in dict and dict[s[i]] >= left:
                length = max(length, i - left)
                left = dict[s[i]] + 1
            dict[s[i]] = i
            i += 1
        return max(length, i - left)