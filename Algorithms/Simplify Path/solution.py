class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path = path.split('/')
        for cur in path:
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur and cur != '.':
                stack += [cur]
        return '/' + '/'.join(stack)
