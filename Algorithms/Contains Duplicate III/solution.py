class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        numsDict = {}
        for i in xrange(len(nums)):
            #generate new key
            bucket = nums[i] / (t + 1)
            #search around this new key, (nums[i] +/- t) / (t + 1) must within this range
            for key in [bucket - 1, bucket, bucket + 1]:
                #if there is a match, return true
                if key in numsDict and abs(numsDict[key] - nums[i]) <= t:
                    return True
            #otherwise, put the new key into the dict
            numsDict[bucket] = nums[i]
            #if there's any old key generated by nums[i - k], delete it for nums[i + 1]
            if i + 1 > k:
                #it will not has any ambiguity with another nums[j] / (t + 1) == nums[i - k] / (t + 1),
                #if this j exits, we will return j before arrive at this step
                pop_key = nums[i - k] / (t + 1)
                numsDict.pop(pop_key)
        return False
