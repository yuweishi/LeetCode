class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, num, res, sign = [], 0, 0, 1
        for chr in '(' + s + ')':
            if chr.isdigit():
                num = num * 10 + int(chr)
            elif chr == '+':
                res, num, sign= res + sign * num, 0, 1
            elif chr == '-':
                res, num, sign= res + sign * num, 0, -1
            elif chr == '(':
                stack += [res, sign]
                sign, res = 1, 0
            elif chr == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res
