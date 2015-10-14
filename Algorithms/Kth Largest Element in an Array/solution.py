class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Method 1: time O(N*logN), space O(1)
        return sorted(nums)[len(nums) - k]
        
	#Method 2: using heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

	#Method 3: quick sort
        start, end = 0, len(nums) - 1
        while True:
            res = self.search(nums, start, end)
            if res == k - 1:
                return nums[res]
            if res > k - 1:
                end = res - 1
            else:
                start = res + 1
        
    def search(self, nums, start, end):
        pivot = nums[start]
        left, right = start + 1, end
        while left <= right:
            if nums[left] < pivot and nums[right] > pivot:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
            if nums[left] >= pivot:
                left += 1
            if nums[right] <= pivot:
                right -= 1
        nums[start], nums[right] = nums[right], nums[start]
        return right
