class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        list = map(str, nums)
        list.sort(cmp = lambda a,b : cmp(b + a, a + b) ) # a and b are strings
        return str(int(''.join(list)))
