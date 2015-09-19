class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        robt, robf = 0, 0
        for num in nums:
            robt, robf = robf + num, max(robt, robf)
        return max(robt, robf)
