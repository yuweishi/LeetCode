class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
	#Method 1: DP
        arr = [0] + [float('Inf')] * n
        for i in range(n + 1):
            for j in range(1, int((n - i) ** 0.5) + 1):
                arr[i + j * j] = min(arr[i + j * j], arr[i] + 1)
        return arr[-1]

	#Method 2: DFS
