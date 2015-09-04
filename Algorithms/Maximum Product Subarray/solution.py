class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxpro, minpro, res = 1, 1, -float('inf')
        for num in nums:
            minpro, maxpro = min(num, num * minpro, num * maxpro), max(num, num * minpro, num * maxpro)
            res = max(res, maxpro)
        return res
