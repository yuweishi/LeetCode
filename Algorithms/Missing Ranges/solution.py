class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        cur = lower
        for num in nums + [upper + 1]:
            if num > cur + 1:
                res += [str(cur) + "->" + str(num - 1)]
            elif num == cur + 1:
                res += [str(cur)]
            cur = num + 1
        return res
