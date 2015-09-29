class Solution(object):
    #Method 1: Recursive
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            return -self.div(abs(dividend), abs(divisor))[0]
        return self.div(abs(dividend), abs(divisor))[0]
    def div(self, dividend, divisor):
        if divisor > dividend:
            return 0, dividend
        if divisor + divisor > dividend:
            return 1, dividend - divisor
        temp1, remain1 = self.div(dividend, divisor + divisor)
        temp2, remain2 = self.div(remain1, divisor)
        return temp1 + temp1 + temp2, remain2 

    #Method 2: Iterative
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or dividend == -2147483648 and divisor == -1:
            return 2147483647
        sign = -1 if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0 else 1
        res, dividend, divisor = 0, abs(dividend), abs(divisor)
        while divisor <= dividend:
            temp, base = divisor, 1
            while temp <= dividend:
                res += base
                base <<= 1
                dividend -= temp
                temp <<= 1
        return sign * res
