class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for left in range(n - 1):
            if not nums[left]:
                right = left + 1
                while not nums[right]:
                    right += 1
                    if right == n:
                        return
                nums[left], nums[right] = nums[right], nums[left]
