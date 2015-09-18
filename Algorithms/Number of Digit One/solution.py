class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum, base = 0, 1
        while base <= n:
            left, cur, right = n / base / 10, (n / base) % 10, n % base
            sum += left * base
            if cur > 1:
                sum += base
            if cur == 1:
                sum += right + 1
            base *= 10
        return sum 
