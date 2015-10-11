class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        #Method 1: Iterative
        stack = []
        low = float('-inf')
        for val in preorder:
            if val < low:
                return False
            while stack and val > stack[-1]:
                low = stack.pop()
            stack.append(val)
        return True
