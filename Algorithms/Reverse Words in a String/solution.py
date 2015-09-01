class Solution(object):
    #Method 1: Pythonic way
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])
    #Method 2: General solution
    def reverseWords(self, s):
        s, i, j, start = list(s), 0, 0, -1
        while True:
            while i < len(s) and s[i] == ' ':
                i += 1
            if i == len(s):
                break
            if start != -1:
                s[j] = ' '
                j += 1
            start = j
            while i < len(s) and s[i] != ' ':
                s[j] = s[i]
                j += 1
                i += 1
            end = j - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        s = s[0:j]
        start, end = 0, j - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)
