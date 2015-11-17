class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        n = len(nums)
        num_min = min(nums)
        num_max = max(nums)
        gap = int (math.ceil(1.0 * (num_max - num_min) / (n - 1)))
        if gap == 0:
            return 0
        bucket_min = [float('Inf')] * n
        bucket_max = [float('-Inf')] * n
        for num in nums:
            index = ((num - num_min) / gap)
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
        res = 0
        pre = bucket_max[0]
        for i in xrange(n):
            if bucket_min[i] != float('Inf'):
                res = max(res, bucket_min[i] - pre)
                pre = bucket_max[i]
        return res
