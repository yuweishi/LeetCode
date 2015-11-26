class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = s + "#" + s[::-1]
        next = [-1] * len(new)
        i, j = -1, 0
        #generate the KMP table
        while j < len(new) - 1:  
            #needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or new[i] == new[j]:   
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
        #next[-1] is the len of longest match - 1, add the reverse of the rest of it before s
        return s[next[-1] + 1:][::-1] + s
