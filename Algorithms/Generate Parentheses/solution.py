class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(res, 0, n, '')
        return res
    def generate(self, res, right, left, pre):
        if left == 0:
            pre += ')' * right
            res += [pre]
        else:
            self.generate(res, right + 1, left - 1, pre + '(')
            if right > 0:
                self.generate(res, right - 1, left, pre + ')')
