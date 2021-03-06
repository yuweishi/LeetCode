class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Method 1: DP
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        res = 0
        dp = [1] * n
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

	#Method 2: Binary search
        res = 0
        dp = [1] * len(nums)
        for num in nums:
            i = bisect.bisect_left(dp, num, 0, res)
            dp[i] = num
            if i == res:
                res += 1
        return res
