class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
