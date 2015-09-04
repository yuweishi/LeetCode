class Solution(object):
    #Method 1: O(n) alg using two pointers
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

    #Method 2: O(nlogn) alg using binary search
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        base, sum, minlen = 0, [0], len(nums) + 1
        for num in nums:
            base += num
            sum += [base]
        for start in range(len(nums)):
            end = self.binsearch(s + sum[start], start + 1, len(nums), sum)
            if end == len(sum): break
            if end - start < minlen: minlen = end - start
        return minlen if minlen < len(sum) else 0
        
    def binsearch(self, target, lo, hi, sum):
        while lo <= hi:
            mid = (lo + hi) / 2
            if sum[mid] == target:
                return mid
            if sum[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
