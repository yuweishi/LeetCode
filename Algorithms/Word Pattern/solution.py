class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        s = str.split(' ')
        if len(pattern) != len(s): return False
        for i in range(len(s)):
            if s[i] not in dict1 and pattern[i] not in dict2:
                dict1[s[i]] = i
                dict2[pattern[i]] = i
            elif s[i] not in dict1 or pattern[i] not in dict2 or dict1[s[i]] != dict2[pattern[i]]:
                return False
        return True
