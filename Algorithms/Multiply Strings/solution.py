class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = len(num1), len(num2)
        num = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            carry = 0
            for j in range(n2 - 1, -1, -1):
                carry, num[i + j + 1] = divmod(carry + num[i + j + 1] + int(num1[i]) * int(num2[j]), 10)
            if carry:
                num[i] = carry
        start = 0
        while start < len(num) - 1 and num[start] == 0:
            start += 1
        return ''.join(map(str, num[start:]))
