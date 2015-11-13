class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 1
        major = nums[0]
        for num in nums[1:]:
            if count == 0:
                major = num
                count += 1
            elif num == major:
                count += 1
            else:
                count -= 1
        return major
