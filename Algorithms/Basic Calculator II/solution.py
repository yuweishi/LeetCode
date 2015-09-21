class Solution(object):
    #Method 1: use map and reduce
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return int(reduce(lambda x, y: int(x) + int(y), [
            reduce(lambda x, y: int(x) - int(y), map(self.calcu, add.split('-'))) for add in s.split('+')]))
    def calcu(self, s):
        res = 1
        num = 0
        sign = '*'
        for char in s + '*':
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '/*':
                if sign == '*':
                    res *= num
                else:
                    res /= num
                num = 0
                sign = char
        return res

    #Method 2: use stack
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign, stack = 0, 0, '+', []
        for char in s + '+':
            if char.isdigit():
                num = num * 10 + int(char)
            elif char != ' ':
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    pre = stack.pop()
                    stack.append(pre / num if pre > 0 else -((-pre) / num))
                sign, num = char, 0
        while stack:
            res += stack.pop()
        return res
