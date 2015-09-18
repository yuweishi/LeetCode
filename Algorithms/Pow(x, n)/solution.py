class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
	#Method 1: recursive
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x*x, n / 2)

        #Method 2: iterative
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        pow = 1
        while n:
            if n & 1:
                pow *= x
            n >>= 1
            x *= x
        return pow
