class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] >= target:           
                    k -= 1
                else:
                    res += k - j
                    j += 1
        return res
