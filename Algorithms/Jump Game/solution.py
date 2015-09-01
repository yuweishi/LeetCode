class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = 0
        for i in range(len(nums)):
            if step < i:
                return False
            step = max(step, nums[i] + i)
            if step >= len(nums) - 1:
                return True
