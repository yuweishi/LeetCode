class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        index_0, index_1, index_2 = -1, -1, -1
        for item in nums:
            if item == 0:
                index_2 += 1
                index_1 += 1
                index_0 += 1
                nums[index_2] = 2
                nums[index_1] = 1
                nums[index_0] = 0
            if item == 1:
                index_2 += 1
                index_1 += 1
                nums[index_2] = 2
                nums[index_1] = 1
            if item == 2:
                index_2 += 1
                nums[index_2] = 2
