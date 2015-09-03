class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
	#Method 1: add 1 more loop to 3Sum, together with some restrictions.
	res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if nums[i] > target / 4:
                break
            if (i == 0 or nums[i] != nums[i - 1]):
                for h in range(i + 1, len(nums) - 2):
                    target3 = target - nums[i]
                    if nums[h] > target3 / 3:
                        break
                    if (h == i + 1 or nums[h] != nums[h - 1]):
                        target2 = target3 - nums[h]
			j, k = h + 1, len(nums) - 1
                        if nums[j] > target2 / 2 or nums[k] < target2 / 2:
                            continue
                        while j < k:
                            if target2 == nums[j] + nums[k]:
                                res.append([nums[i], nums[h], nums[j], nums[k]])
                                while j < k - 1 and nums[j] == nums[j + 1]: j += 1
                                while j < k - 1 and nums[k] == nums[k - 1]: k -= 1
                                j, k = j + 1, k - 1
                            elif target2 > nums[j] + nums[k]:           
                                j += 1
                            else: 
                                k -= 1
        return res
