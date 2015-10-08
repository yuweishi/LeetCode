class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        start, end, n = 0, 0, len(s) - 1
        while start < n:
            while end < n and s[end + 1] != ' ':
                end += 1
            temp = end + 2
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            start = end = temp
        start, end = 0, n
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
