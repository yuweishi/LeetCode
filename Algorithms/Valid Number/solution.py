class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #remove heading and trailing zeros and skip sign
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == ' ':
                left += 1
            elif s[right] == ' ':
                right -= 1
            else:
                break
        if left > right:
            return False
        s = s[left: right + 1]
        if s[0] in '-+':
            s = s[1:]
        #check start/end with . or e
        if s == '.' or not ((s[0].isdigit() or s[0] == '.' and s[1] != 'e') and (s[-1].isdigit() or s[-1] == '.')):
            return False
        #check within body
        occur1, occur2, i = 0, 0, 0
        while i < len(s):
            num = s[i]
            if not num.isdigit():
                if num == 'e' and occur2 or num == '.' and (occur1 or occur2):
                    return False
                if num == 'e': 
                    occur2 = 1
                    if i < len(s) - 1 and s[i + 1] in '-+':
                        i += 1
                elif num == '.': occur1 = 1
                else: return False
            i += 1
        return True
