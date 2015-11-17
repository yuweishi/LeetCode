class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Method 1: heap
        if not nums or not k:
            return []
        res = []
        heap = nums[:k]
        heapq.heapify(heap)
        for i in xrange(k, len(nums)):
            cur = heapq.nlargest(1, heap)
            res += cur
            if cur != nums[i - k]:
                heap.remove(nums[i - k])
            else:
                heap.remove(cur)
            heapq.heappush(heap, nums[i])
        res += heapq.nlargest(1, heap)
        return res

        #Method 2: deque
        if not nums or not k:
            return []
        deque = collections.deque()
        res = []
        for i in xrange(len(nums)):
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque += [i]
            if i >= k - 1:
                res += [nums[deque[0]]]
                if deque and deque[0] == i - k + 1:
                    deque.popleft()
        return res
