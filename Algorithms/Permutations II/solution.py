class Solution(object):
    #Method 1: recursive
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        return self.permute(sorted(nums))
    def permute(self, nums):
        return [[nums[i]] + p
        for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]
        for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]
   
    #Method 2: iterative
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = [[]]
        for num in nums:
            new_res = []
            n = len(res[0])
            for seq in res:
                for i in range(n + 1):
                    if i > 0 and seq[i - 1] == num:
                        break
                    new_res.append(seq[:i] + [num] + seq[i:])
            res = new_res
        return res
