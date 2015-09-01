class Solution(object):
    def singNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Method 1: swap, similiar to Find Missing Positive
        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

        #Method 2: bit manipulating
        res = 0
        for i in range(len(nums)):
            res ^= nums[i] ^ i
        return res ^ len(nums)

        #Method 3: sum
        res = (len(nums) + 1) * len(nums) / 2
        for i in range(len(nums)):
            res -= nums[i]
        return res
