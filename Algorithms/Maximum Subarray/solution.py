class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        sum, maxsum = 0, nums[0]
        for num in nums:
            sum += num
            maxsum = max(maxsum, sum)
            sum = max(0, sum)
        return maxsum
