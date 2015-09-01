class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, level = 0, 1, 0
        while end < len(nums):
            for i in range(start, end):
                end = max(end, i + nums[i])
            start = i + 1
            end += 1
            level += 1
        return level
