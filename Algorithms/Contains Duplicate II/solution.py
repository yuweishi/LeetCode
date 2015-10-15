class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = set()
        for i in xrange(len(nums)):
            if i > k:
                dict.remove(nums[i - k - 1])
            if nums[i] in dict:
                return True
            dict.add(nums[i])
        return False
