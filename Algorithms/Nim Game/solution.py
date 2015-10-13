class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
	#Method 1: return directly
        return bool(n % 4)

	#Method 2: DP
	pre = [True] * 3
        while n > 3:
            for i in range(3):
                pre[i] = not (pre[0] & pre[1] & pre[2]) 
            n -= 3
        return pre[(n - 1) % 3]
