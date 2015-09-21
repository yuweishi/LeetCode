class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        larger = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1] and not larger or larger and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            larger = 1 - larger
