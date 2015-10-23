class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n, k, bias = len(nums), k % len(nums), 0
        while k:
            for i in range(k):
                nums[i + bias], nums[- k + i] = nums[- k + i], nums[i + bias]
            bias += k
            n -= k
            k %= n
