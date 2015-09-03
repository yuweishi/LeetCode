class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total, start, end, size = 0, 0, 0, None
        while end < len(nums):
            total += nums[end]
            while total >= s:
                if not size or size > end - start + 1:
                    size = end - start + 1
                total -= nums[start]
                start += 1
            end += 1
        return size if size else 0
