class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Method 1: Based on Two Sum
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                dict = {}
                j = i + 1
                while j < len(nums):
                    if nums[j] not in dict:
                        dict[- nums[i] - nums[j]] = nums[j]
                    else:
                        res.append([nums[i], dict[nums[j]], nums[j]])
                        while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                            j += 1
                    j += 1
        return res

        #Method 2: Based on two pointers
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k - 1 and nums[j] == nums[j + 1]: j += 1
                        while j < k - 1 and nums[k] == nums[k - 1]: k -= 1
                        j, k = j + 1, k - 1
                    elif nums[i] + nums[j] + nums[k] < 0:           
                        j += 1
                    else: 
                        k -= 1
        return res
