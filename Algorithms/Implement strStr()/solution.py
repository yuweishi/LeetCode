class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            for j in range(i, len(haystack) + 1):
                if j - i == len(needle):
                    return i
                if needle[j - i] != haystack[j]:
                    break
        return -1