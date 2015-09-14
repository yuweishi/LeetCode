class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Method 1: Congruence formula
        res = num % 9
        return res if (num == 0 or res != 0) else 9

	#Method 2: Recursive
	if num < 10:
            return num
        sum = 0
        while num:
            sum += num % 10
            num /= 10
        return self.addDigits(sum)
