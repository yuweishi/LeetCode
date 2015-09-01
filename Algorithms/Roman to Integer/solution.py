class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        i = 0
        while i < len(s) - 1:
            if dict[s[i]] >= dict[s[i + 1]]:
                res += dict[s[i]]
            else:
                res -= dict[s[i]]
            i += 1
        return res + dict[s[i]]
