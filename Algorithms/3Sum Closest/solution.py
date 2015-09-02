class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = float('Inf')
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == target:
                        return target
                    if abs(nums[i] + nums[j] + nums[k] - target) < abs(res - target):
                        res = nums[i] + nums[j] + nums[k]
                    if nums[i] + nums[j] + nums[k] < target:           
                        j += 1
                    else: 
                        k -= 1
        return res
