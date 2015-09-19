class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robI(nums[1:]), self.robI(nums[0: len(nums) - 1]))
    
    def robI(self, nums):
        robt = robf = 0
        for num in nums:
            robt, robf = robf + num, max(robt, robf)
        return max(robt, robf)
