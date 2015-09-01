class Solution(object):
    #Method 1: Solve by removing closed pair one by one
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pre = None
        while s and pre != s:
            pre = s
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if s:
            return False
        return True
        
    #Method 1: Using stack
    def isValid(self, s):
        map = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for char in s:
            if char in map:
                stack.append(map[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        return not stack
