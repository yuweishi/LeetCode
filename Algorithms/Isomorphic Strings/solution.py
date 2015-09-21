class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            if s[i] not in dict1 and t[i] not in dict2:
                dict1[s[i]] = i
                dict2[t[i]] = i
            elif s[i] not in dict1 or t[i] not in dict2 or dict1[s[i]] != dict2[t[i]]:
                return False
        return True
