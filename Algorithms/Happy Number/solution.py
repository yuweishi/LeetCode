class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast, slow = self.check(self.check(n)), self.check(n)
        while fast != 1 and fast != slow:
            fast, slow = self.check(self.check(fast)), self.check(slow)
        return fast == 1
    def check(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n /= 10
        return sum
