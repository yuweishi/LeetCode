class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ope = set(['+', '-', '*', '/'])
        stack = []
        for item in tokens:
            if item in ope:
                b = stack.pop()
                a = stack.pop()
                if item == '-':
                    res = a - b
                elif item == '+':
                    res = a + b
                elif item == '*':
                    res = a * b
                else:
                    res = a / b 
                    if res < 0 and a % b != 0:
                        res += 1
                stack += [res]
            else:
                stack += [int(item)]
        return stack.pop()
