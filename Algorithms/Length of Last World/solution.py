class Solution(object):
    #Method 1: Pythonic way
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s.split() else len(s.split()[-1])
    
    #Method 2: General solution
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return 0 if not s.split() else len(s.split()[-1])
        i, count = len(s) - 1, 0
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        return count
