class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[nums[i]] + p
        for i in range(len(nums))
        for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]
